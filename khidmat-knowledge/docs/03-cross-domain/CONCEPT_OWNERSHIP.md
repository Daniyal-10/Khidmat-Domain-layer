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
- **ADR Required:** How should Consent (currently leaning towards Registration & Identity) propagate when a Case Worker needs to share specific medical vulnerability data with a partner organization?
- **Uncertainty:** Where does the concept of a "Community" live? Is it a logical grouping in Registration, or a contextual entity in Programme Management?
