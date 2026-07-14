# Impact Phase 0 Architectural Decision Review

## Executive Summary
This document captures the architectural decisions required before transitioning the Impact Business Architecture into the formal Khidmat AI ontology. It strictly evaluates all concepts against ADR-008 (Single Ownership), ADR-022 (Canonical Concepts), and ADR-023 (Ontology Vocabulary Extensions), breaking down every major concept into its appropriate structural type (Entity, Value Object, Role, Runtime Object, or Taxonomy).

---

## 1. Concept Classification & Validation

### 1.1 Impact Evaluation
- **Classification:** `Entity`
- **Reasoning:** An Impact Evaluation is the core aggregate root of this domain. It tracks the longitudinal change of a beneficiary over time, holding the state, the schedule, and the collection of measurements. It has a distinct lifecycle (e.g., Scheduled, In Progress, Abandoned, Completed).
- **Aggregate Structure:** The `ImpactEvaluation` acts as the aggregate root and contains `Measurement` as a child Entity (e.g., `ImpactEvaluation` `contains` `Measurement`).
- **Alternatives Considered:** Making it a Value Object on the `Case` entity. Rejected. ADR-008 governs ownership of concepts, the repository DAG governs dependency direction, and aggregate boundaries govern composition. Embedding the evaluation in the `Case` entity mixes these concerns and incorrectly forces the upstream Case Management domain to own downstream Impact concepts, violating the DAG.

### 1.2 Measurement
- **Classification:** `Entity`
- **Reasoning (ADR-023 Promotion):** A measurement is an immutable recording of a specific indicator at a specific point in time. It is promoted to a first-class Entity (from a Value Object) because it fails the ADR-023 Value Object promotion test: it requires outbound relationships and cross-domain references, it tracks distinct provenance, it serves as an explicit target for evaluator association, and it maintains independent identity within an `ImpactEvaluation`.
- **Temporal Classifications:** Baseline, Endline, and Longitudinal are temporal classifications of a `Measurement`. Under ADR-023, these are not Roles (Roles are held by Entities relative to other Entities). They should be represented later as either taxonomy values or semantic relationships (e.g., `has_baseline_measurement`).

### 1.3 Outcome Indicator
- **Classification:** `Taxonomy`
- **Reasoning:** Indicators (e.g., "Food Consumption Score", "School Attendance Rate") are standardized canonical lists against which measurements are made. They are not entities themselves. 
- **Alternatives Considered:** Entity. Rejected because indicators are globally standardized definitions, not transactional records.

### 1.4 Subjective vs Objective Evidence
- **Classification:** `Value Object` attribute / Taxonomy constraint.
- **Reasoning:** Every `Measurement` Value Object will require an `epistemic_type` attribute referencing a taxonomy (e.g., `Self-Reported`, `Observer-Measured`, `Third-Party-Verified`). This adheres to ADR-023 by avoiding boolean flags for complex epistemic states.

### 1.5 Measurement Schedule
- **Classification:** `Runtime Object` (Out of Scope for Ontology)
- **Reasoning:** The schedule dictates *when* to execute a survey (e.g., "Trigger survey 90 days after Case Closed"). Execution triggers and queues are orchestration logic, violating the knowledge layer boundaries if modeled as an Entity.

### 1.6 Confounding Factors & External Shocks
- **Classification:** `Relationship` (Cross-domain)
- **Reasoning:** External shocks (e.g., a flood) belong to the `Community Context` or `Risk` domains. The Impact domain will use a `was_confounded_by` relationship pointing from the `ImpactEvaluation` to the respective external event/risk entity.

### 1.7 Independent Evaluation Authority
- **Classification:** `Role`
- **Reasoning:** The person or organization conducting the measurement acts in the `Evaluator` Role, which maps back to the `Actor` or `Volunteer` entities in the Shared/Volunteer Operations domains relative to the `Measurement` Entity.

---

## 2. Cross-Domain Ownership & Repository DAG Validation

### 2.1 The Case Management Leak
- **Potential Issue:** Attempting to store the `Outcome` on the `CasePlan` entity.
- **Resolution:** A `CasePlan` produces outputs. The `ImpactEvaluation` evaluates outcomes. The DAG must flow from Impact -> Case Management (Impact points to the Case it evaluates, not vice versa). `ImpactEvaluation` `evaluates_case` `Case`.

### 2.2 The Needs Assessment Leak
- **Potential Issue:** Duplicating the initial `NeedsAssessment` scoring into a new "Baseline" entity inside Impact.
- **Resolution:** To prevent duplication, the `ImpactEvaluation` must contain a `Measurement` Entity that can either be collected directly OR reference the existing `NeedsAssessment` through a relationship (`baseline_derived_from`). All cross-domain references must originate from the `Measurement` Entity (e.g., baseline derived from `NeedsAssessment`, evaluated by `Volunteer` / `Actor`, measured against `Indicator`).

### 2.3 The Programs Domain Leak
- **Potential Issue:** Impact attempting to define what a "Success" is for a specific program.
- **Resolution:** Impact records the absolute change (e.g., "Income increased by 20%"). The *interpretation* of that change against program eligibility or success criteria belongs to the Programs domain. Impact stays strictly factual.

---

## 3. Outstanding Architectural Decisions (ADRs Required)

The following architectural decisions are documented in the Business Architecture and are confirmed as requiring formal ADRs before ontology authoring begins:

1. **Attribution vs Contribution:** How to formally model the relationship between a Khidmat intervention and external interventions within the `ImpactEvaluation` aggregate.
2. **Lost-to-Follow-Up / Attrition:** Establishing the lifecycle constraints for an `ImpactEvaluation` when a beneficiary cannot be reached (e.g., a `Terminated` status vs an `Inconclusive` status).
3. **Spillover Measurement Scope:** Deciding if a `SpilloverEvaluation` is a distinct Entity or merely a relationship linking a primary `ImpactEvaluation` to a secondary `Beneficiary`.

---

## 4. Final Recommendation
**Phase 0 Complete.**

The Impact Phase 0 Architectural Decision Review is structurally complete and ready for canonical ontology authoring.
