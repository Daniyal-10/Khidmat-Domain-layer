# Stage 5 Discovery Harmonization Report

## 1. Executive Summary
This report analyzes the cross-domain harmony of the Khidmat AI business discovery repository at the conclusion of Stage 5. It evaluates the interactions between Case Management, Programme Management, Registration & Identity, Accountability & Evaluation, Resource & Logistics, Organisation & Partner Management, and Cross-Organisational Coordination. The objective is to identify systemic conflicts, establish architectural resolutions, and present recommended Architectural Decision Records (ADRs) prior to proceeding to Stage 6 Ontology Design.

## 2. Repository Strengths and Weaknesses

### Strengths
- **Clear Separation of Concerns:** The domains demonstrate highly mature boundaries. The separation between defining a rule (Programme Management), assessing against a rule (Case Management), and executing a rule (Resource & Logistics) is structurally sound.
- **Epistemic Rigor:** The recurring pattern of separating claims from evidence is deeply embedded across multiple domains (Identity Verification, Case Vulnerability, Accountability Grievances).
- **Domain Invariants:** Explicit invariants such as "Evidence Precedes Execution" and "Consent is King" provide clear, unambiguous guardrails for future architectural decisions.

### Weaknesses
- **Household Fluidity Complexity:** While acknowledged, the mathematical and temporal realities of dynamically splitting and merging households (especially when one member transfers to another NGO) are under-specified.
- **Cross-Domain Revocation Mechanics:** The system asserts that if consent is revoked, data must be purged downstream. However, the mechanical flow of this "kill signal" across autonomous domains is highly ambiguous.
- **Uncertainty Representation:** Domains recognize that data is often unverified or highly uncertain, but lack a unified mechanism to represent this uncertainty formally.

## 3. Cross-Domain Conflicts and Analysis

### Conflict 1: The "Needs Assessment" Collision
- **Source of Conflict:** Both Programme Management and Case Management claim ownership over "Needs Assessment."
- **Analysis:** This is a collision of terminology, not capability. Programme Management performs a *macro-level* needs assessment (evaluating population aggregates to secure funding). Case Management performs a *micro-level* needs assessment (evaluating a specific household to determine individual eligibility).
- **Resolution:** Formalize the terminology. Programme Management conducts "Population Vulnerability Assessments." Case Management conducts "Individual Needs Assessments."

### Conflict 2: The Independent Accountability Loop
- **Source of Conflict:** Accountability & Evaluation must remain structurally independent of Programme Management and Case Management. However, it relies entirely on their data (closed cases, distribution logs) to function.
- **Analysis:** If Accountability cannot access the raw operational data, it cannot evaluate impact. If it is integrated too tightly, it loses its objective distance.
- **Resolution:** Accountability must consume *immutable snapshots* of Case and Logistics data. It must not have write-access to the operational databases, and its generated learnings must be formally proposed (not automatically enforced) to Programme Management via a dedicated feedback interface.

### Conflict 3: Deduplication vs Privacy
- **Source of Conflict:** Cross-Organisational Coordination wants to broadcast identity data to prevent duplicate aid. Registration & Identity mandates strict privacy and data minimization.
- **Analysis:** Sharing raw biometric or biographical data across NGO boundaries violates consent and endangers beneficiaries.
- **Resolution:** The architecture must enforce Zero-Knowledge Proofs or Cryptographic Hashing for external deduplication. Coordination receives an alert that a hash collided; it does not receive the raw identity data.

## 4. Remaining Risks

- **Offline Synchronization:** The discovery assumes a connected state for cross-domain handshakes (e.g. Case Management passing an Execution Trigger to Logistics). In deep field operations, connectivity is intermittent, risking massive state desynchronization.
- **Culturally Subjective Rules:** The rigid implementation of a "Household" structure risks breaking down in complex cultural contexts (e.g. polygamous structures) if hardcoded too strictly into the core ontology.
- **Scale of Exception Handling:** The sheer volume of "Emergency Overrides" (bypassing consent, bypassing procurement rules) identified across all domains suggests that the exception may become the rule in acute crises, potentially overwhelming the system's audit capabilities.

## 5. Architectural Observations

- **Event-Driven Architecture is Mandatory:** The domains are highly reactive. An event in Registration (e.g., Household Split) must cascade to Case Management (reassess support plan) and Logistics (split rations). The architecture should inherently support publish-subscribe patterns.
- **The Centrality of the Trust State:** A single trust failure (e.g., an NGO fails an anti-terrorism audit) must immediately halt interactions across the entire ecosystem. Trust must be a global, universally accessible state.

## 6. Recommended Architectural Decision Records (ADRs)

Based on the harmonized discovery, the following ADRs are recommended for immediate drafting:
1. **ADR: Implement Immutable Snapshots for MEAL:** Mandating that Accountability & Evaluation operates on read-only, point-in-time snapshots of operational data to preserve objective distance.
2. **ADR: Cryptographic Deduplication Standards:** Mandating that Cross-Organisational deduplication relies exclusively on hashed identity tokens rather than raw PII exchange.
3. **ADR: Standardized Epistemic Wrappers:** Mandating that all critical data payloads across all domains include an "Evidence Level" wrapper (e.g., Claimed, Community Validated, Document Verified).

## 7. Outstanding Business Questions

- How do we mathematically reconcile a situation where NGO A classifies a beneficiary as "High Risk," NGO B classifies the identical beneficiary as "Low Risk," and they attempt to coordinate aid?
- In the event of a catastrophic host-government demand for data access, how does the architecture physically sever the Cross-Organisational Coordination links to protect local NGOs from retaliation?
- How is the financial "burn rate" of a Programme dynamically updated if Resource & Logistics procures goods locally at a wildly different price than originally budgeted?
