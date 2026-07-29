# Cross-Domain Dependency Architecture

## 1. Executive Overview
The Khidmat Domain Layer operates as an ecosystem of autonomous but highly interdependent bounded contexts. The dependencies between these domains form the nervous system of the humanitarian response. This document maps the repository-wide dependency architecture, defining the flow of information, the rationale for handoffs, reciprocal relationships, and the systemic risks when dependencies are violated.

## 2. Purpose and Scope
This document outlines **how** and **why** domains communicate. A dependency in Khidmat is never just a technical API call; it represents a fundamental business handoff where one domain has reached the limit of its epistemic authority and must rely on another to continue the lifecycle of aid.

## 3. Dependency Mapping and Flow

### 3.1. The Strategic Definition Flow
- **Producer:** Programme Management
- **Consumer:** Case Management
- **Dependency:** `Eligibility Rules` and `Intervention Catalogues`.
- **Rationale:** Case Management cannot invent aid. It can only assess need. Programme Management provides the rigid financial and strategic boundaries dictating what interventions are available and the mathematical rules for who is allowed to receive them.
- **Business Consequence:** If Case Management cannot consume these rules, it operates blindly, recommending interventions that the organization cannot fund, leading to broken promises and beneficiary trauma.

### 3.2. The Execution Handoff Flow
- **Producer:** Case Management
- **Consumer:** Resource and Logistics
- **Dependency:** `Execution Trigger` (Approved Support Plan).
- **Rationale:** The separation of assessment from delivery is a core anti-fraud invariant. Case Management decides *who* gets *what*, but Resource & Logistics physically executes the delivery.
- **Business Consequence:** If this handoff is broken, assessed individuals remain perpetually in need (bottleneck), or Logistics delivers goods without verifiable need (fraud).

### 3.3. The Accountability Feedback Flow
- **Producer:** Resource & Logistics / Case Management
- **Consumer:** Accountability and Evaluation
- **Dependency:** `Fulfillment Records` and `Closed Cases`.
- **Rationale:** To evaluate impact objectively, Accountability must consume the raw operational data of what was actually delivered and to whom, independent of the operational teams' self-reported success.
- **Business Consequence:** Without this dependency, the organization has no independent truth. It operates entirely on confirmation bias.

### 3.4. The Identity Anchoring Flow
- **Producer:** Registration and Identity
- **Consumer:** Case Management
- **Dependency:** `Authenticated Identity`.
- **Rationale:** Before Case Management can assess a vulnerability, it must know *who* it is assessing. Identity provides the enduring anchor ensuring the case worker is not talking to a duplicate profile or a malicious actor.
- **Business Consequence:** If Case Management bypasses this dependency, the system floods with duplicate records, allowing a single individual to draw multiple rations while others starve.

## 4. Reciprocal Relationships
Reciprocal relationships exist where the flow of data creates a continuous operational loop.
- **Execution Loop:** Case Management sends an `Execution Trigger` to Resource & Logistics. In return, Resource & Logistics sends a `Fulfillment Status` (Success/Failure) back to Case Management. 
- **Rationale:** Case Management must know if the aid arrived so it can transition the Case state to "Monitoring" or trigger a reassessment.

## 5. Circular Dependencies and Risks
A strict architectural invariant in Khidmat is the **Prohibition of Circular Dependencies** in core business logic execution.
- **The Risk:** If Domain A cannot complete its state transition without Domain B, and Domain B cannot complete its state transition without Domain A, the system will deadlock.
- **Example of Mitigated Circularity:** Case Management requires an `Eligibility Rule` from Programme Management to approve a `Support Plan`. Programme Management requires aggregated `Support Plans` to adjust budgets. This is mitigated by separating the operational (synchronous) read of the rule from the strategic (asynchronous) aggregation of the data. They do not depend on each other at the exact same moment in time.

## 6. Missing Reciprocal Dependencies
Our current architectural discovery highlights critical missing reciprocal dependencies:
- **Missing Link (Systemic Learning):** Accountability & Evaluation produces `Systemic Learning Mandates` indicating a program has failed. However, there is no formal enforcement mechanism for Programme Management to consume and act upon these mandates.
- **Consequence:** Accountability functions merely as an observer rather than a governor. A structural mechanism must be defined where a critical negative evaluation forcibly suspends Programme Eligibility Rules until a "Management Response" is registered.
- **Missing Producer Dependency (Programme Baselines):** `accountability-evaluation` explicitly lists the consumption of programmatic baseline data to measure impact. However, `programme-management` discovery does not list structured baselines as an output it produces.
- **Consequence:** M&E expects data that Programme Management is not formally contracted to provide. Handoffs fail if the producer does not know they are required to produce the data.

## 7. Business Consequences of Dependency Failures
- **Latency Over Availability:** If the dependency between Identity and Case Management experiences latency, humanitarian intake stops. In conflict zones, this means people wait in dangerous lines. The architecture must prioritize asynchronous caching (e.g., offline identity verification) to prevent network-level dependencies from causing physical harm.
- **Data Privacy Violations:** If Cross-Organisational Coordination pulls data from Case Management without properly consuming the `Consent History` dependency from Registration & Identity, the organization violates international data protection laws, risking immediate expulsion from the operating country.

## 8. Potential Architectural Improvements
- **Event-Driven Choreography:** To reduce tight coupling, most dependencies should be implemented via an Event Bus. For example, instead of Case Management directly calling Resource & Logistics, Case Management publishes a `SupportPlanApproved` event, which Logistics consumes at its own pace.
- **Immutable Projections:** Consuming domains should maintain read-only, point-in-time projections of upstream data. If Programme Management changes an `Eligibility Rule` on Tuesday, Case Management should retain the historical rule for an assessment finalized on Monday to preserve auditability.
