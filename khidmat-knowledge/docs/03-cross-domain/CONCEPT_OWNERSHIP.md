# Concept Ownership Architecture

## 1. Executive Overview
In the Khidmat Domain Layer, the concept of **Ownership** is the fundamental structural principle that prevents logical contradictions, ensures data integrity, and establishes clear accountability for business operations. Every core business concept—whether an entity, a policy, or a capability—must have exactly one authoritative domain owner. This document defines the philosophical underpinnings of ownership, the criteria for establishing it, canonical ownership boundaries, and the severe business consequences of duplicating concepts.

## 2. Purpose and Definition of Ownership
### Why Ownership Exists
In a complex humanitarian ecosystem, the same entity is often viewed through different lenses by different operational units. For instance, a "Person" is a vulnerable subject to Case Management, a logistical destination to Resource & Logistics, and a statistical data point to Accountability & Evaluation. Without strict ownership, these domains would create conflicting definitions and records for the same real-world entity, leading to fragmented truth, duplicate aid delivery, and an inability to audit decisions.

### What Ownership Means
Ownership is **epistemic authority**. The owning domain is the singular source of truth for the lifecycle, state transitions, and validation rules of a concept.
- **Authority:** Only the owning domain can create, modify, or retire the concept.
- **Verification:** The owning domain defines what constitutes "truth" or "validity" for that concept.
- **Obligation:** The owning domain must expose this truth in an immutable, read-only format for consuming domains.

## 3. Canonical Concept Owners

### 3.1. Case Management Domain
- **Owns:** Case, Support Plan, Claim, Vulnerability, Needs Assessment.
- **Business Justification:** Case Management is uniquely positioned to evaluate human context. They are the domain that interacts directly with the individual to gather claims and verify them against reality.
- **Producer Role:** Produces verified Needs and Execution Triggers (Support Plans) for other domains.
- **Consumer Role:** Consumes Eligibility Rules from Programme Management to determine if a verified Need qualifies for assistance.

### 3.2. Programme Management Domain
- **Owns:** Intervention Catalogue, Eligibility Rule, Logical Framework, Programme Budget.
- **Business Justification:** Programme Management defines the strategic intent, financial boundaries, and overarching rules of what assistance the organization provides and who qualifies for it, independent of any single individual's context.
- **Producer Role:** Produces the constraints and catalogues that govern Case Management operations.
- **Consumer Role:** Consumes aggregated demographic and impact data to adjust strategic planning.

### 3.3. Resource and Logistics Domain
- **Owns:** Inventory, Fulfillment Event, Dispatch Record, Vendor Contract.
- **Business Justification:** Moving physical goods or financial resources requires a completely different skill set and risk management profile than evaluating human vulnerability.
- **Producer Role:** Produces Fulfillment Statuses confirming aid delivery.
- **Consumer Role:** Consumes Execution Triggers from Case Management.

### 3.4. Accountability and Evaluation Domain
- **Owns:** Grievance, Feedback, Post-Distribution Monitoring (PDM), Impact Evaluation.
- **Business Justification:** Objectivity mandates separation. The domain evaluating the success of a program or investigating a complaint cannot be the same domain that designed the program or delivered the aid.
- **Producer Role:** Produces systemic learning mandates and independent investigation resolutions.
- **Consumer Role:** Consumes closed cases, logical frameworks, and dispatch records to baseline their evaluations.

### 3.5. Registration and Identity Domain
- **Owns:** Identity Core, Consent History, Biometric/Cryptographic Identity Anchors.
- **Business Justification:** Identity is an enduring construct that survives beyond any single intervention. It must be managed independently from a transient "Case" to ensure long-term deduplication and privacy rights.
- **Producer Role:** Produces the authenticated subject for Case Management.
- **Consumer Role:** Consumes field biometric data or demographic assertions from entry points.

### 3.6. Cross-Organisational Coordination Domain
- **Owns:** Inter-Agency Referral, Deduplication Hash, Trust Network Rule.
- **Business Justification:** Coordination across sovereign NGO boundaries requires a specialized domain focused on protocol negotiation, encrypted matching, and trust brokering, totally distinct from internal operations.

## 4. The Perils of Duplication
Duplicating a concept across domains destroys epistemic integrity.
- **The Split-Brain Problem:** If Case Management and Resource & Logistics both implement their own version of a "Beneficiary," updates in one system will not reflect in the other.
- **Audit Failures:** In the event of fraud, if the Support Plan (owned by Case Management) and the Fulfillment Event (owned by Logistics) use differently defined concepts of eligibility, proving compliance becomes mathematically impossible.
- **Architectural Rule:** A concept must never be duplicated. If a domain needs data from another domain, it must hold a **Reference** (a read-only projection) to the authoritative concept, not a copy.

## 5. Known Conflicts and Boundary Tensions
- **Case Worker vs. Assessor:** There is a known tension where Case Management views "Assessment" as its core function, but Accountability & Evaluation also conducts "Assessments" (PDMs). The resolution is strictly semantic: Case Management conducts *Vulnerability Assessments*, while Accountability conducts *Impact Assessments*.
- **Identity vs. Case:** Decoupling a person's enduring identity from their active case is conceptually difficult for legacy practitioners who view "registration" and "intake" as the same event.

## 6. Alternative Models Considered
- **The Monolithic Beneficiary Model:** A design where all domains update a single, massive "Beneficiary Record" entity. **Rejected:** This violates the bounded context principle, creates massive concurrency bottlenecks, and muddles accountability (who is responsible if a field is wrong?).
- **Event Sourced Projections without Strict Ownership:** Allowing any domain to publish events that alter a concept's state. **Rejected:** Lack of a single writer/owner leads to race conditions and prevents strict enforcement of business rules (e.g., bypassing Programme Eligibility).

## 7. Remaining Uncertainties and Required ADRs
- **ADR Required:** How should Consent (currently leaning towards Registration & Identity) propagate when a Case Worker needs to share specific medical vulnerability data with a partner organization? — **Now raised as ADR-003 in `docs/00-governance/DECISION_LEDGER.md` (remediation B10). Remains open; the ledger records it rather than leaving it as a note.**
- **ADR Required (Location Ownership):** Canonical ownership of "Location" is currently Unresolved / Pending ADR. There is a documented tension between `resource-logistics` (which needs operational locations like warehouses and camps) and `organisation-partner-management` (which needs administrative locations like partner offices). — **Now raised as ADR-002 in the decision ledger (remediation B10). Remains open.**
- **Uncertainty:** Where does the concept of a "Community" live? Is it a logical grouping in Registration, or a contextual entity in Programme Management? — **RESOLVED under remediation B11. See §9.**

---

## 8. Reality / Operational Classification — Cross-Domain Resolutions

*(Added under remediation B6. The rubric itself is in `docs/00-governance/STAGE_5_DISCOVERY_STANDARD.md` §6. This section records only those adjudications where two or more domains had classified the same concept differently, or where a discovery classification contradicted a ratified decision. Domain-local reclassifications are recorded inline in each domain's `03-concepts.md`.)*

| Concept | Prior conflicting classifications | Resolution | Basis |
|---|---|---|---|
| **Consent** | Reality Knowledge in `case-management/03`; "Foundational Consent" = Operational Knowledge in `registration-identity/03`; foundational cross-domain concept in `FOUNDATION_CONCEPTS.md` §3 | **Split.** *Consent* — the person's act of authorising — is **Reality Knowledge**, owned by Registration & Identity. *Consent Record* — the organisational artifact recording it — is **Operational Knowledge**, also held by Registration & Identity. | Rubric Q1 and Q2; Constitution Article IX makes consent a right of the person. Rubric §6.3 split rule. |
| **Programme** | Operational Knowledge in `programme-management/03`; ratified as "a distinct humanitarian business concept" by CL-001 (Human Owner, 2026-07-27) | **Reality Knowledge**, owned by Programme Management. | A discovery classification may not contradict a ratified governance decision. Corroborated by TD-01 BD-TD01-003 and HBRM Ch1. |
| **Eligibility / Eligibility Rule** | Eligibility = Operational in `case-management/03`; Eligibility Rule = Operational in `programme-management/03`; both are canonical owned concepts in §3.1–3.2 of this document | **Both Reality Knowledge.** *Eligibility Rule* owned by Programme Management; the *eligibility determination* about a specific person owned by Case Management. | Rubric Q2 — nothing determines who receives assistance more directly. |
| **Intervention Offering / Intervention Catalogue** | Operational in both `case-management/03` and `programme-management/03` | **Reality Knowledge**, owned by Programme Management, referenced by Case Management. | Rubric Q2. |
| **Grant** | Operational in `programme-management/03`; a Donor & Resource Term in `GLOSSARY.md` | **Reality Knowledge**, owned by the Giving and Resource-Origin domain (created under remediation B4), referenced by Programme Management. | Rubric Q2 — grants carry restrictions that constrain recipient eligibility. |
| **Delivery Event** | Reality Knowledge in `case-management/03`; "Delivery Confirmation / Receipt" = Operational in `resource-logistics/03` | **Delivery Event is Reality Knowledge**, owned by Resource & Logistics. *Delivery Confirmation / Receipt* remains Operational as its record. | Rubric Q1; `GLOSSARY.md` Support Delivery Terms already assigns Delivery Event to this subject matter. |
| **Referral** | Operational in `case-management/03`; core produced concept of Cross-Organisational Coordination | **Reality Knowledge.** *Internal Escalation / Handoff* owned by Case Management; *External Referral* owned by Cross-Organisational Coordination — the split already established in `TERMINOLOGY_HARMONIZATION.md` §4.3. | Rubric Q2. |
| **Head of Household** | Operational in `registration-identity/03` | **Retained as Operational Knowledge**, owned by Registration & Identity. The underlying *responsibility for household decision-making* is Reality Knowledge, owned by Human Reality. | Rubric §6.3 — a role is Operational; the relationship beneath it is Reality. |
| **Priority / Severity** | Operational in both `case-management/03` and `programme-management/03` | **Not classified.** Held as Operational pending evidence of how it is determined. Recorded as an open question in `case-management/03b-need-model.md` §4. | Rubric §6.3 — a ranking with no stated derivation is not classified until its basis exists. Pillar P4 forbids unexplainable scores. |

**Standing rule.** Where a future domain classifies a concept differently from this table, the table governs until amended through the governance tier appropriate to the change.

---

## 9. Ownership of the Social Units

*(Added under remediation B11. The accepted assessment recorded that three of the four social units in the Project Overview's own model — Family, Household and Community — had no canonical owner, and that §7 above left Community explicitly unresolved.)*

| Concept | Canonical owner | Business justification |
|---|---|---|
| **Person / Individual** | **Human Reality** *(`docs/02-discovery/human-reality/`)* | The person persists across cases, programmes and organisations. `registration-identity/12-domain-invariants.md` establishes "The Primacy of the Beneficiary"; `FOUNDATION_CONCEPTS.md` §1 establishes the person as the root anchor. Registration & Identity owns the *assurance* that two encounters concern the same person; Human Reality owns what is true of that person. |
| **Family** | **Human Reality** | `GLOSSARY.md` defines Family as distinct from Household, connected through kinship, caregiving, marriage or guardianship, with multiple families possible within one household. No prior domain claimed it. |
| **Household** | **Human Reality** | The household as a social unit — its resilience, internal dependencies, housing, utilities and community context. Registration & Identity retains ownership of household *membership recording and adjudication* as part of registry integrity, including the Household Composition Decision (`registration-identity/08` §3), which is unchanged. |
| **Community** | **Human Reality** | Resolves the open uncertainty in §7. Neither candidate proposed there is correct: Registration is a registry function and cannot hold settlement type, service access, local organisations, livelihood patterns or seasonal hazard; Programme Management is forbidden from evaluating anything below population aggregate (`programme-management/12-domain-invariants.md`). Community context is reality about where a household lives, which is this domain's subject matter. |

**Responsibility for the Household split rule.** `VALIDATION/FINDINGS.md` REC-01 recommended that responsibility for resolving how a household splits be assigned, and it never was. It is assigned here to **Human Reality**, and is recorded as Open Question 2 in that domain's Section 18. Assigning the owner does not answer the question; the answer requires evidence gated on remediation B13.

**Boundary with Registration & Identity, stated once.** Registration & Identity answers *"is this the same human being, and is this household composition correctly recorded?"* Human Reality answers *"what is true of this person, and what kind of social unit is this?"* Recorded in `registration-identity/02-boundaries.md` and `human-reality/HUMAN_REALITY_DISCOVERY.md` §16.
