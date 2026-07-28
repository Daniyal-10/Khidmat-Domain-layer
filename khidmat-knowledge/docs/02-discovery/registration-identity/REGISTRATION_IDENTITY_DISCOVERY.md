---
id: DOC-DISC-REGISTRATION_IDENTITY
title: REGISTRATION & IDENTITY DOMAIN DISCOVERY
version: 1.0
status: Draft
owner: Discovery
---

# 1. Purpose, Outcomes, Capabilities, and Activities

## Purpose
The Registration and Identity Domain exists to formally establish, verify, and maintain the trustworthy identity of humanitarian subjects (Individuals and Households) before any operational domain interacts with them. It solves the profound problem of knowing exactly *who* we are helping, preventing duplicate identities, and managing foundational consent.

## Business Outcomes
- A unified, universally trusted assertion of an individual's and household's existence and identity.
- Prevention of duplicate registrations and associated aid fraud.
- Centralized, legally compliant management of beneficiary consent and contact information.

## Business Capabilities
- Identity Registration & Intake
- Identity Verification & Biometric/Documentary Proofing
- Household Membership Management
- Consent & Privacy Management
- Duplicate Detection & Resolution

## Core Business Activities
- Capturing foundational biographical and biometric data from individuals.
- Grouping individuals into logical household structures based on self-reporting or cultural norms.
- Verifying identity claims using external evidence, community validation, or documentation.
- Recording and managing explicit consent for data processing and sharing.
- Continuously auditing the registry for duplicate profiles and merging them.

---

# 2. Stakeholders

## Actors (Enduring Participants)
- **Individual:** The human being seeking to establish their identity with the humanitarian system.
- **Household:** The enduring family or social unit to which individuals belong.
- **Community Leader / Validator:** A trusted external actor who vouches for an individual's identity when documentation is absent.

## Roles (Transient Responsibilities)
- **Registrar / Registration Officer:** The frontline humanitarian responsible for capturing identity data and household structures.
- **Verification Officer:** The role responsible for adjudicating complex identity claims or resolving duplication conflicts.
- **Data Protection Officer (DPO):** The role responsible for auditing consent and privacy compliance.

---

# 3. Domain Dependencies and Boundaries

## Owns
- The foundational definition of Identity (Biographical, Biometric).
- Household composition and membership lifecycles.
- Registration status (Active, Inactive, Deceased, Duplicated).
- Foundational Consent to be processed by the humanitarian organisation.

## Consumes
- **From Community/External Entities:** Identity evidence (passports, refugee cards, community leader validations).

## Produces
- **For Case Management:** Verified Identities and Household structures; Foundational Consent.
- **For Cross-Organisational Coordination:** Cryptographic identity hashes for deduplication against other NGOs.
- **For Accountability & Evaluation:** Verified contact information for post-distribution monitoring.

## Explicitly Out of Scope
- Assessing the vulnerability or needs of the individual (Case Management).
- Determining eligibility for aid (Programme Management).
- Distributing aid (Resource and Logistics).

---

# 4. Business Concepts

- Identity Profile
- Biographical Data
- Household / Family Unit
- Head of Household
- Dependent
- Identity Evidence (Documentary, Biometric, Testimonial)
- Registration Status
- Foundational Consent
- Duplicate Match
- Merge Record

---

# 5. Business Relationships

- An **Individual** is a member of a **Household**.
- A **Household** has a designated **Head of Household**.
- An **Identity Profile** requires **Identity Evidence** for verification.
- **Foundational Consent** authorizes the existence of the **Identity Profile**.
- A **Duplicate Match** links two **Identity Profiles**.

---

# 6. Knowledge Patterns

- **The Verification Gradient:** Claimed Identity -> requires -> Evidence -> elevates to -> Verified Identity. Identity is not binary; it exists on a spectrum of trust based on the weight of evidence.
- **Household Fluidity:** Individuals merge into and split from Households dynamically due to marriage, divorce, birth, death, or conflict displacement. The Household is a temporal container, while the Individual is permanent.

---

# 7. Policies and Constraints

## Policies
- **Universal:** Every individual has the right to be registered and recognized as a person before the humanitarian system, regardless of legal status.
- **Organisation:** An Identity Profile cannot be elevated to "Verified" without at least two distinct points of evidence (e.g., Biographical + Community Validation, or Biographical + Document).
- **Consent:** No Identity Profile can be retained beyond a temporary holding period if Foundational Consent is explicitly denied.

## Constraints
- **Legal:** Undocumented migrants or refugees may completely lack state-issued identity documents.
- **Cultural:** The definition of a "Household" varies wildly across cultures (e.g., polygamous families, extended intergenerational living, unaccompanied minors).
- **Security:** Capturing biometric data (e.g., fingerprints, iris scans) in conflict zones can put beneficiaries at extreme risk if databases fall into the hands of hostile state actors.

---

# 8. Exceptions

- **Unaccompanied Minors:** An individual lacking a legal guardian requires emergency proxy registration without standard household attribution.
- **Name Fluidity:** In many cultures, individuals change their primary name based on life events (e.g., becoming a parent), breaking standard biographical matching algorithms.
- **Refusal to Register:** An individual may desperately need aid but absolutely refuse formal registration due to fear of persecution.
- **Mass Registration Waivers:** During an acute, overwhelming influx (e.g., 100,000 refugees crossing a border in a week), strict identity verification is suspended to allow rapid "lite" registration.

---

# 9. Business Tensions

The Registration & Identity domain continuously balances competing operational forces:
- **Inclusion vs Integrity:** The tension between making registration extremely easy so no vulnerable person is left behind, versus making it strict to prevent fraud and duplicate identities.
- **Data Minimisation vs Deduplication:** The ethical mandate to collect as little data as possible to protect privacy versus the mathematical necessity of collecting rich data (like biometrics) to accurately detect duplicates.
- **Individual Sovereignty vs Household Efficiency:** The tension of treating every human as an independent sovereign entity versus the operational reality that aid is almost always calculated and distributed at the "Household" level.
- **State Identity vs Humanitarian Identity:** The conflict when a host government refuses to legally recognize a refugee's identity, forcing the humanitarian organisation to mint a parallel, de facto identity.

---

# 10. Business Events

- **Registration Initiated:** A new profile is created for an Individual.
- **Household Formed:** Individuals are grouped together into a household unit.
- **Identity Verified:** Sufficient evidence is gathered to elevate trust in the profile.
- **Duplicate Detected:** The system or an operator flags two profiles as potentially the same person.
- **Profiles Merged:** Two duplicate profiles are administratively combined into a single surviving profile.
- **Household Split:** A household is formally divided (e.g., due to divorce or displacement).
- **Consent Granted / Revoked:** Foundational permission to store identity is changed.

---

# 11. Business Lifecycles

## The Identity Lifecycle
1. **Intake / Pre-Registration:** Capturing basic unverified claims.
2. **Verification:** Gathering evidence (documents, biometrics, testimony).
3. **Active:** The identity is trusted and available for operational use.
4. **Suspended:** The identity is temporarily halted (e.g., pending a fraud investigation).
5. **Archived / Deceased:** The identity is permanently removed from active operational pools but retained for historical/audit purposes.

## The Household Lifecycle
1. **Formation:** Individuals are grouped together.
2. **Evolution:** Members are added (birth, marriage) or removed (death, departure).
3. **Dissolution:** The household completely ceases to exist as a cohesive unit.

---

# 12. Significant Business Decisions

## 1. Identity Verification Decision
- **Purpose:** Elevating a claimed identity to a verified status, unlocking downstream aid.
- **Decision Maker:** Verification Officer.
- **Supporting Evidence:** Passports, biometrics, community leader testimony.
- **Governing Policies:** Organisational Identity Assurance guidelines.
- **Constraints:** Lack of physical documents in refugee scenarios.
- **Preconditions:** Individual profile must exist.
- **Alternative Outcomes:** Verified, Rejected (Fraud), Pending (Insufficient Evidence).
- **Escalation Conditions:** Suspected identity theft or highly sophisticated fraud.
- **Review Triggers:** Routine quality assurance audits.
- **Appeal Mechanisms:** Individual can return with a community leader to appeal a rejection.
- **Human Override:** Verification Officer can manually verify an undocumented person based on deep interview consistency.
- **Uncertainty:** Forged documents and false community testimonies are common.

## 2. Duplicate Resolution Decision
- **Purpose:** Deciding whether two highly similar profiles represent the exact same human being.
- **Decision Maker:** Registration Officer / Verification Officer.
- **Supporting Evidence:** Facial similarity, matching biographical metadata, matching household members.
- **Governing Policies:** Anti-fraud deduplication protocols.
- **Constraints:** High prevalence of identical names and birthdates within specific communities.
- **Preconditions:** System flags a potential duplicate match.
- **Alternative Outcomes:** Merge Profiles, Mark as Distinct (False Positive), Escalate for physical interview.
- **Escalation Conditions:** Merging profiles would collapse two massive, active case histories into one.
- **Review Triggers:** Post-merge anomaly detection.
- **Appeal Mechanisms:** None required if resolved internally; beneficiary can complain if aid is disrupted.
- **Human Override:** Mandatory human review for all merges; algorithms cannot auto-merge identities.
- **Uncertainty:** Twins or culturally identical naming conventions routinely trigger false positives.

## 3. Household Composition Decision
- **Purpose:** Determining who legally or operationally belongs to a household.
- **Decision Maker:** Registrar, informed by the Head of Household.
- **Supporting Evidence:** Beneficiary testimony, physical cohabitation.
- **Governing Policies:** Definition of a "Household" (often defined by "eating from the same pot").
- **Constraints:** Culturally complex family structures (polygamy, unaccompanied minors living with neighbors).
- **Preconditions:** Registration of individuals.
- **Alternative Outcomes:** Joined to Household, Formed into new Household, Split from Household.
- **Escalation Conditions:** Dispute between spouses over who constitutes the Head of Household.
- **Review Triggers:** Re-registration drives.
- **Appeal Mechanisms:** Members can request to be split into independent households.
- **Human Override:** Registrar overrides strict biological definitions to accommodate de facto living situations.
- **Uncertainty:** Highly fluid living arrangements during active conflict.

---

# 13. Information Requirements

- **Biographical Data:** Names (current, aliases), Date of Birth, Place of Birth.
- **Biometric/Physical Data:** Photographs, fingerprints, iris scans (where policy permits).
- **Contact Data:** Phone numbers, physical addresses, GPS coordinates.
- **Kinship Data:** Relationships between individuals (Spouse, Child, Sibling).

---

# 14. Open Questions

- How is the continuous lifecycle of a Household mapped when the Head of Household dies, and a minor assumes responsibility?
- How is a "Merge Record" structurally un-done if a Duplicate Resolution Decision is later found to be incorrect?
- If Registration & Identity owns foundational consent, how does it physically communicate a "Consent Revoked" event to Case Management and Coordination to ensure downstream data destruction?

---

# 15. Discovery Evidence

## Established Facts
- Registration must precede Case Management assessment. Identity is the foundation upon which vulnerability is evaluated.
- Households are fluid temporal structures; Individuals are permanent entities.
- Algorithmic deduplication creates false positives; human adjudication is a mandatory business reality.

## Reasonable Assumptions
- The definition of a "Household" will vary drastically depending on the cultural context of the crisis.
- Beneficiaries will occasionally attempt to register multiple times to secure additional rations.

## Open Questions
Refer to Section 14 (10-open-questions.md).

## Knowledge Gaps
- The specific legal constraints of storing biometric data on cloud servers versus local devices in high-risk conflict zones.

---

# 16. Domain Invariants

- **The Primacy of the Individual:** An individual exists independently of a household. A household is merely a relational grouping.
- **Identity is Immutable, Attributes are Mutable:** A person's core existence cannot change, but their name, age (if estimated), and contact details can evolve over time.
- **Consent is Foundational:** The right to exist in the database is predicated on continuous, revocable consent.

---

# 17. Terminology

## Preferred Terms
- **Identity Profile:** The authoritative record of an individual's existence.
- **Household:** The operational unit of living and aid calculation.
- **Verification:** The act of proving an identity claim.

## Synonyms
- **Beneficiary / Person of Concern (PoC):** Used interchangeably with Individual, though Registration prefers Individual.
- **Intake:** Used interchangeably with Registration.

## Ambiguous Terminology
- **Registration:** Can mean the macro-act of recording an identity, or the micro-act of signing up for a specific training class (Programme Management). Here, it strictly means foundational Identity Registration.
- **Family vs. Household:** Family implies biological kinship; Household implies shared economic/living reality. The humanitarian system operates on Households.

---

# 18. Ontology Readiness

The following conceptual clusters appear highly stable and ready for subsequent formal Ontology Design (Stage 6):
- **The Identity-Evidence Triad:** Identity Profile -> verified by -> Identity Evidence.
- **The Household Composition Model:** Individual -> member of -> Household -> led by -> Head of Household.
- **The Deduplication Construct:** The mathematical and administrative reality of Profile A and Profile B being linked by a Merge Resolution.

These concepts can be modelled without requiring implementation assumptions.

---

# 19. Domain Completion Assessment

`
Overview: Complete
Boundaries: Complete
Concepts: Complete
Relationships: Complete
Business Rules: Complete
Events: Complete
Lifecycles: Complete
Decision Points: Complete
Information Requirements: Complete
Open Questions: 3 identified
Evidence: Complete
Domain Invariants: Complete
Business Language: Complete
Client Validation: Pending
Overall Discovery Maturity: READY FOR FREEZE
`

---

