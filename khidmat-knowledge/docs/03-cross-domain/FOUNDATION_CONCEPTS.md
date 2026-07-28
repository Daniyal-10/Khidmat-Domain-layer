# Foundation Concepts

## Executive Overview
The Khidmat AI project operates across multiple domains (Case Management, Programme Management, Registration & Identity, Accountability & Evaluation, Organisation & Partner Management, Cross-Organisational Coordination, Resource & Logistics). However, certain business concepts transcend these domains, acting as the fundamental building blocks of the entire humanitarian ecosystem. This document identifies these cross-domain foundational concepts and establishes their definitions, invariant rules, and justification for inclusion in the Stable Core.

## 1. Beneficiary / Individual

### Definition
A sovereign human being who is the subject of humanitarian assistance, possessing an immutable existence independent of their current living situation, vulnerability, or engagement with any specific organisation.

### Why it is Foundational
The entire humanitarian system exists to serve the individual. Every claim, need, distribution, and grievance ultimately points back to a human being. Without a clear representation of the individual, duplicate aid, fragmented care, and safeguarding failures become systemic.

### Discovery Evidence
- **Registration & Identity** captures the biographical/biometric existence.
- **Case Management** tracks their vulnerabilities and changing needs.
- **Accountability & Evaluation** receives their grievances and measures their recovery.
- **Resource & Logistics** hands them physical resources.

### Cross-Domain Usage
- Used as the root anchor for Identity Profiles, Cases, Support Plans, and Feedback loops.

### Relationships
- An Individual is a member of a **Household**.
- An Individual raises a **Claim** or **Grievance**.
- An Individual provides **Consent**.

### Business Invariants
- An individual's existence is immutable; only their attributes (name, age, contact) are mutable.
- A person exists independently of any household grouping.

### Constraints & Known Ambiguities
- Cultural definitions of identity often clash with rigid bureaucratic structures (e.g. name fluidity based on life events).
- Verification relies heavily on external evidence which may be impossible to procure in conflict zones.

### Candidate Stable Core Justification
The Beneficiary is the absolute center of the humanitarian ecosystem. It must be modelled as a highly stable, universally accessible core entity that all domains reference, ensuring a single source of truth across the architecture.

---

## 2. Organisation

### Definition
An enduring institutional entity (such as an NGO, INGO, or UN agency) that holds an operational mandate, possesses technical capabilities, and executes interventions.

### Why it is Foundational
Humanitarian response is executed by a complex web of independent organisations. Trust, funding, and liability flow between these entities. Understanding who is operating, what they can do, and their vetting status is necessary before any coordination or execution can occur.

### Discovery Evidence
- **Organisation & Partner Management** creates and vets the organisation.
- **Cross-Organisational Coordination** brokers trust and referrals between them.
- **Programme Management** funds them to execute programmes.
- **Case Management** interacts with them as service providers or referral targets.

### Cross-Domain Usage
- Used to define liability, mandate, and execution boundaries.

### Relationships
- An Organisation holds a **Mandate**.
- An Organisation employs **Roles** (Case Workers, Registrars).
- An Organisation partners with another **Organisation**.

### Business Invariants
- Legal liability flows upward to the primary grant holder.
- An organisation must formally exist and be recognized (vetted) before holding a programmatic mandate or distributing resources.

### Constraints & Known Ambiguities
- Grassroots organisations may lack formal legal registration, complicating standard vetting structures.
- Consortia act as a single entity to donors but remain multiple independent entities on the ground.

### Candidate Stable Core Justification
Every action in the system is executed *by* an organisation or *on behalf of* an organisation. Therefore, the definition of an Organisation and its trust state must be globally available and structurally stable.

---

## 3. Consent

### Definition
The explicit, informed, and revocable permission granted by an individual to allow the humanitarian system to capture, store, process, and share their data.

### Why it is Foundational
Informed consent is the ethical and legal bedrock of humanitarian intervention. Without it, the system risks violating privacy, endangering lives, and breaching international data protection laws (like GDPR).

### Discovery Evidence
- **Registration & Identity** captures Foundational Consent.
- **Case Management** relies on consent to conduct assessments and propose support plans.
- **Cross-Organisational Coordination** requires explicit consent before sharing encrypted context with external partners.

### Cross-Domain Usage
- Gates the progression of workflows: data cannot be shared, and certain interventions cannot proceed without it.

### Relationships
- Granted by a **Beneficiary**.
- Authorizes a **Shared Context** or **Activity**.

### Business Invariants
- The right to exist in the database is predicated on continuous, revocable consent.
- If consent is revoked at the root, the revocation must propagate across the entire chain.

### Constraints & Known Ambiguities
- "Emergency overrides" exist where consent is bypassed to save a life, requiring careful audit trails and human accountability.
- How to practically revoke consent across a distributed, cross-organisational network remains a profound challenge.

### Candidate Stable Core Justification
Because consent governs the legality and ethics of data processing across all domains, its state (Granted, Revoked, Emergency Override) must be a first-class, foundational concept accessible by the entire architecture.

---

## 4. Evidence / Verification

### Definition
The objective, independently corroborated proof that supports a claim of identity, vulnerability, or delivery.

### Why it is Foundational
The transition from unverified claims to trusted facts is the primary mechanism of risk mitigation in humanitarian work. The system must structurally distinguish between what a person *says* and what has been *proven*.

### Discovery Evidence
- **Registration & Identity** uses evidence (passports, community testimony) to verify identity.
- **Case Management** uses evidence (observations, medical records) to verify vulnerability.
- **Resource & Logistics** uses evidence (signatures, cryptographic proofs) to verify fulfillment.
- **Accountability & Evaluation** uses evidence to verify programme impact.

### Cross-Domain Usage
- Represents the epistemic confidence level of data across the system.

### Relationships
- **Evidence** supports a **Claim**.
- **Evidence** elevates a status (e.g., to **Verified Identity** or **Confirmed Delivery**).

### Business Invariants
- Evidence precedes execution: A verified understanding of reality must exist before material resources are committed.
- Unverified claims cannot trigger automated resource distribution.

### Constraints & Known Ambiguities
- In acute crises, formal documentary evidence is often impossible to acquire, forcing reliance on "community validation."
- Different organisations possess different thresholds for what constitutes acceptable evidence.

### Candidate Stable Core Justification
The structural separation between an assertion (Claim) and its proof (Evidence) is a universal knowledge pattern. Modeling this at the foundation prevents domains from tightly coupling their decision logic to unverified data.
