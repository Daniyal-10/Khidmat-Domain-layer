# Shared Concept Catalog

## Executive Overview
The Shared Concept Catalog serves as the definitive architectural repository for business concepts that transcend individual domain boundaries within the Khidmat AI business architecture. During Stage 5 Discovery, independent domains naturally developed localized definitions of core concepts such as Identity, Evidence, Need, and Assessment. This catalog synthesizes these disparate definitions into canonical, repository-wide architectural understandings. It prevents semantic drift and ensures that ontology engineers receive a unified conceptual model, rather than fragmented, domain-specific views.

## Purpose
The purpose of this document is to analyze and harmonize every shared business concept. It moves beyond simple glossary definitions to provide deep architectural analysis, explaining *why* a concept exists, *how* it is used across the business, where conceptual boundaries conflict, and the architectural implications of those conflicts.

## Scope
This catalog encompasses concepts identified as existing in two or more of the seven Stage 5 discovery domains (`case-management`, `registration-identity`, `programme-management`, `resource-logistics`, `accountability-evaluation`, `cross-organisational-coordination`, `organisation-partner-management`). 

---

## 1. Identity

### Definition
Identity is the fundamental, foundational recognition of an entity (whether a human individual, a legal organization, or a conceptual group) that interacts with the humanitarian business ecosystem. It is the core referent around which all rights, claims, histories, and interventions are anchored.

### Business Meaning
In humanitarian reality, Identity is the linchpin of trust and continuity. Without a stable Identity, accountability is impossible, assistance is duplicated, and vulnerability cannot be tracked over time. Identity represents the formal business assertion that "this entity exists, is uniquely distinguishable from others, and is the subject of our business processes."

### Why Identity Exists in Humanitarian Reality
The humanitarian sector operates in environments where state-issued identities are often lost, destroyed, or weaponized. Therefore, the business must establish its own robust, verifiable identity structures to guarantee the impartial and targeted delivery of aid, ensuring the protection of rights and the prevention of fraud.

### Business Responsibilities Involving Identity
* Uniquely distinguishing individuals and organizations.
* Anchoring consent and data protection rights.
* Serving as the primary subject for needs assessments and vulnerability claims.
* Providing the historical continuity required for accountability and evaluation.

### Relationship to Other Concepts
* **Individual/Person:** An Individual is the biological realization of a human Identity.
* **Household:** A group Identity composed of multiple Individual Identities sharing socio-economic realities.
* **Organisation:** A formalized, legal, or structural Identity.
* **Consent:** Consent is exclusively granted by a verified Identity.
* **Evidence:** Evidence is attached to an Identity to verify Claims.
* **Assessment & Case:** Identities are the subjects of Assessments and the beneficiaries of Cases.

### How Every Domain Understands Identity
* **registration-identity:** Views Identity as a raw asset to be created, deduplicated, biometrically verified, and protected. It is the primary product of this domain.
* **case-management:** Views Identity as a "Client" or "Subject" whose vulnerabilities must be addressed over time.
* **programme-management:** Views Identity as a demographic target or "Beneficiary" meeting specific programmatic criteria.
* **organisation-partner-management:** Views Identity as a legal partner or implementing agency.
* **accountability-evaluation:** Views Identity as a data point for measuring longitudinal impact and handling feedback/complaints.

### Discovery Evidence
The `registration-identity` domain explicitly notes the tension between capturing enough data to ensure uniqueness versus minimizing data to ensure protection. `case-management` highlights that without a stable ID from registration, case continuity fractures. `cross-organisational-coordination` flags Identity as the primary payload transferred during inter-agency referrals.

### Architectural Implications
Identity cannot be treated as a simple string or database ID. It is a complex business state machine (Unverified &rarr; Verified &rarr; Suspended &rarr; Deactivated). The architecture must decouple the core Identity from the roles it plays (e.g., separating the concept of the "Person" from the "Beneficiary Role").

### Known Unresolved Questions
* Should synthetic identities (e.g., anonymized profiles for M&E) be treated architecturally identically to verified human identities?
* How does the system handle an Identity that splits (e.g., a household dissolving into two households)?

### Candidate Ontology Significance
Identity is a highly stable, universally utilized business concept. It should act as a core foundational anchor for downstream knowledge modeling, representing the parent category for concepts like Person, Household, and Organisation without dictating technical implementation.

---

## 2. Evidence

### Definition
Evidence is a verifiable artifact, observation, or formal attestation provided to substantiate a Claim, an Identity, or a Need.

### Business Meaning
Humanitarian operations are constrained by limited resources and governed by strict donor accountability rules. Evidence provides the business justification for transitioning an entity's status from "Claimed" to "Verified," thereby unlocking access to decisions, resources, and interventions.

### Why Evidence Exists in Humanitarian Reality
Decisions in humanitarian contexts (who gets cash, who gets relocated, who is prioritized for medical care) are high-stakes. Evidence exists to remove subjectivity and mitigate fraud, bias, and error, providing an auditable trail that justifies business actions.

### Relationship to Other Concepts
* **Claim:** Evidence is the counterweight to a Claim. A Claim is an assertion; Evidence is the proof.
* **Identity:** Biometrics, ID cards, and community attestations act as Evidence of Identity.
* **Assessment:** Assessments generate Evidence (e.g., a vulnerability score) or consume Evidence to reach a Decision.
* **Decision:** No formal Decision should occur without linked Evidence.

### How Every Domain Understands Evidence
* **registration-identity:** Views Evidence as foundational documents (birth certificates, biometrics) required to establish an identity.
* **case-management:** Views Evidence as ongoing behavioral observations, medical reports, or protection incident reports required to justify a Support Plan.
* **accountability-evaluation:** Views Evidence as field monitoring reports, financial receipts, and beneficiary feedback required to prove Impact.
* **resource-logistics:** Views Evidence as waybills, signed delivery notes, and warehouse receipts proving the movement of goods.

### Architectural Implications
Evidence is polymorphic in its structure and its validity periods. It can be a physical document, a digital signature, a biometric hash, or a structured professional assessment. Its validity may be point-in-time (expirable) or immutable. The architecture must model Evidence not just as a file attachment, but as a first-class business object with properties such as `Source`, `ValidityPeriod`, `VerificationLevel`, and `ConfidenceScore`.

### Known Conflicts
There is a repository-wide conflict regarding the lifecycle of Evidence. Does Evidence expire? `case-management` treats evidence of a vulnerability (e.g., malnutrition) as point-in-time and subject to expiration, whereas `registration-identity` treats evidence of birth date as immutable. 

### Future Harmonization Considerations
The business architecture must establish a unified "Evidentiary Standard" that defines how different domains weigh and trust Evidence produced by other domains.

---

## 3. Need

### Definition
A Need is a formally recognized state of lacking, vulnerability, or requirement experienced by an Identity, which the humanitarian ecosystem aims to address.

### Business Meaning
Need is the primary driver of all downstream humanitarian action. It is the delta between a current state of vulnerability and a desired standard of safety, dignity, or well-being. Recognizing a Need transitions the business from passive observation to active intervention planning.

### Why Need Exists in Humanitarian Reality
Humanitarian action is strictly needs-based, independent of political, religious, or social affiliation. The precise articulation of Needs ensures that limited resources are directed toward the most severe vulnerabilities.

### Relationship to Other Concepts
* **Assessment:** Needs are identified, quantified, and validated through Assessments.
* **Priority:** Not all Needs can be met. Priority is the business ranking applied to a Need.
* **Intervention & Resource:** Interventions deliver Resources specifically designed to satisfy a Need.
* **Outcome:** An Outcome is achieved when a Need is demonstrably reduced or eliminated.

### How Every Domain Understands Need
* **case-management:** Views Need as highly individualized, complex, and deeply personal (e.g., "Child protection need due to separation").
* **programme-management:** Views Need in aggregate, demographic terms (e.g., "WASH needs in Camp A").
* **resource-logistics:** Consumes Need as aggregated demand signals used to trigger supply chain procurement.
* **cross-organisational-coordination:** Views Need as the trigger for a Referral when the current organization cannot fulfill it.

### Discovery Evidence
Discovery highlights a friction point: `programme-management` often designs programmes based on macro-level Needs, but `case-management` deals with micro-level Needs that frequently fall outside predefined programmatic boundaries. 

### Architectural Implications
Need must be modeled distinctly from the Intervention. The architecture must allow a Need to exist even if no Programme or Resource currently exists to fulfill it. This separation ensures the business can identify gaps in its response capabilities.

---

## 4. Assessment

### Definition
Assessment is the structured business process—and the resulting knowledge artifact—of evaluating an entity's claims, needs, risks, or capabilities against a set of predefined criteria or standards.

### Business Meaning
Assessment represents the business cognition required to move from raw data to actionable knowledge. It is the analytical engine that ingests Observations and Evidence and outputs Decisions, Needs, and Priorities.

### Relationship to Other Concepts
* **Evidence:** Assessments consume Evidence.
* **Decision:** Assessments strictly precede and inform Decisions.
* **Need & Risk:** Assessments identify and quantify Needs and Risks.

### How Every Domain Understands Assessment
* **case-management:** Conducts deep, qualitative vulnerability and protection assessments.
* **programme-management:** Conducts macro-level needs assessments and eligibility targeting.
* **accountability-evaluation:** Conducts post-distribution monitoring and impact assessments.
* **organisation-partner-management:** Conducts capacity and due diligence assessments on partner NGOs.

### Discovery Evidence
The `accountability-evaluation` domain reveals that Assessments are often duplicated. A beneficiary may be assessed by Registration, then by a Case Worker, then by an M&E officer, leading to assessment fatigue.

### Architectural Implications
Assessment must be recognized as a universal business pattern rather than a domain-specific action. The architecture should model the `Assessment Event` independently of the domain executing it, standardizing the inputs (Evidence) and outputs (Decisions/Needs) to enable cross-domain sharing of Assessment results.

## Summary
This catalog demonstrates that core concepts are deeply intertwined. The subsequent documents in this layer (`CONCEPT_OWNERSHIP.md`, `CROSS_DOMAIN_DEPENDENCIES.md`) will define how the business governs and shares these concepts across its organizational boundaries.
