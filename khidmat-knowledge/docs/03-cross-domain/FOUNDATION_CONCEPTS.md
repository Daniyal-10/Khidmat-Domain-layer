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

---
---

# Part II — Stable Core Definitions

*(Added under remediation B8. `KHIDMAT_FOUNDATION_PIPELINE.md` Stage 6.1 requires a working definition for each of the six Stable Core elements named in `PROJECT_OVERVIEW.md` Ch5.1, a cross-check that every qualified concept can be described in those terms, and a "Stable Core Definitions" note as the stage output. That stage was never performed. Part I above defines four cross-domain concepts — Beneficiary, Organisation, Consent, Evidence — which are **not** the same list: it covers Evidence, partially covers Identity, and omits Relationships, Uncertainty, Temporal change and Context entirely. Part II supplies the missing stage output.)*

**What these are.** `PROJECT_OVERVIEW.md` Ch5.1 states that certain forms of knowledge are foundational "because every humanitarian domain depends upon them — concepts such as identity, relationships, evidence, uncertainty, temporal change, and humanitarian context provide the minimum structure required to understand reality regardless of whether the domain is health, education, shelter, livelihoods, disaster response, or another future area."

**What these are not.** `KHIDMAT_FOUNDATION_PIPELINE.md` Stage 7 is explicit: *"the Stable Core does not generate primitives — discovery does. The Stable Core governs how a discovered primitive is modeled."* These six are therefore **governing dimensions**, not an ontology and not a primitive set. Deriving the primitive set remains the first authoring act of ontology design (`ONTOLOGY_DESIGN.md` §1.4).

## SC-1 — Identity

**Working definition.** That which makes a thing the *same thing* across separate observations, conversations, organisations and years, and therefore that on which continuity of understanding depends.

**Repository basis.** `PROJECT_OVERVIEW.md` Ch1.2 (systems capture a person "as a single point in time rather than as a continuously evolving human journey"); Ch1.3 (knowledge resets between programmes); `registration-identity/12-domain-invariants.md` ("Identity is Immutable, Attributes are Mutable"; "The Primacy of the Beneficiary"); `SHARED_CONCEPT_CATALOG.md` §1 (identity must be decoupled from the roles it plays).

**Cross-check against Ch1.2 and Ch5.2.** Ch1.2's dimension "personal identity and life history" is covered. Ch5.2 requires that a source's reliability accumulate over time, which presupposes the source has identity — covered.

**Known weakness.** Household re-identification across splits and merges is unanswered (`human-reality/HUMAN_REALITY_DISCOVERY.md` Open Question 2).

## SC-2 — Relationships

**Working definition.** A connection between things that already have identity, itself capable of carrying meaning, duration, plurality and evidence — not an attribute of either party.

**Repository basis.** `PROJECT_OVERVIEW.md` Ch5.1 ("deeply relational, where meaning emerges from relationships rather than isolated records"); Ch1.2 ("understanding one person therefore requires understanding the relationships in which they exist"); the ~45 relationships across the seven domains' `04-relationships.md` files; `human-reality/HUMAN_REALITY_DISCOVERY.md` §9 (typed, directional dependency); `GLOSSARY.md` (`need_influences_need`, qualified three ways).

**Cross-check.** Ch1.2's dimensions "family and household structure" and "relationships between family members and dependents" are covered by the Human Reality domain. Ch5.2's requirement that evidence attach to claims is a relationship that itself bears epistemic status — covered.

**Known weakness.** Temporal validity and plurality are unevidenced for most relationships. This is recorded rather than resolved; `ONTOLOGY_DESIGN.md` §2.3 makes stating them a design obligation, and they cannot be stated from current evidence.

## SC-3 — Evidence

**Working definition.** Any observation, record, testimony, measurement or artifact that contributes to understanding humanitarian reality and **whose origin can be identified and evaluated**. An unsupported assertion is not evidence because it has been recorded.

**Repository basis.** `PROJECT_OVERVIEW.md` Ch5.2; `CONSTITUTION.md` Article V; Part I §4 of this document; the claim/evidence/verification spine present in all seven original domains.

**Strength factors, as stated in Ch5.2:** source credibility, method of collection, relevance, timeliness, completeness, corroboration, and consistency with other trusted evidence. These are the repository's canonical criteria and are qualitative by construction.

**Cross-check.** Ch1.2's dimension "evidence supporting observed circumstances" is covered. Note the polymorphic validity established under finding MAJ-01 and remediation REM-02: some evidence is immutable, some expires.

## SC-4 — Uncertainty

**Working definition.** The explicit representation of what is *not* known or not settled about an assertion — its claim status, the confidence it currently deserves, what evidence would change it, what remains unknown, and whether the conclusion it supports requires human review.

**Repository basis.** `PROJECT_OVERVIEW.md` Ch1.2 names "levels of uncertainty, confidence, and verification for every important conclusion" as a foundational dimension; Ch2.3 requires that "significant uncertainties are explicitly identified rather than ignored"; Ch5.2 requires conflicting evidence to be preserved rather than resolved prematurely and defines a conclusion as "operationally accepted" yet "open to revision"; `CONSTITUTION.md` Article III(c) and Article VIII; `GLOSSARY.md` supplies Confidence Level, Claim Basis, Gap and Finding Consensus; the twenty decision points across the seven domains each state their residual uncertainty.

**Cross-check.** This element had **no working definition anywhere in the repository before this section**, which the accepted assessment recorded as directly material to the Cognition layer.

**Known weakness.** `DISCOVERY_HARMONIZATION_REPORT.md` §2 records that the domains "lack a unified mechanism to represent this uncertainty formally," and `case-management/10-open-questions.md` asks how a suspected but unevidenced vulnerability is represented. Designing that representation is ontology-design work (`ONTOLOGY_DESIGN.md` §2.7); what is missing at foundation level is the practitioner-recognised evidence-sufficiency thresholds, which are gated on B13.

## SC-5 — Temporal Change

**Working definition.** The distinction between a condition holding across a *span* of time and an occurrence happening at a *point* in time, together with the requirement that history be preserved rather than overwritten when either is revised.

**Repository basis.** `PROJECT_OVERVIEW.md` Ch5.1 ("continuously evolving rather than static"); Ch1.2 (systems "rarely preserve how circumstances have changed, what events led to the current situation"); the ten state progressions across the seven domains; the ~70 business events; `human-reality/HUMAN_REALITY_DISCOVERY.md` §8.5 (life events) and §11 (the Longitudinal Revision Pattern); `GLOSSARY.md` Trajectory and Lifecycle Transition; `CONSTITUTION.md` Article X(c) (auditability after the fact).

**Cross-check.** Ch1.2's dimension "significant life events, displacement, crises, or disasters" is covered by the Human Reality domain's life-event catalogue. Ch1.2's requirement to preserve "how previous interventions have influenced future outcomes" is covered in shape by the outcome model, with the caveat that outcome criteria remain open (AR-011).

**This element also had no working definition before this section.**

## SC-6 — Context

**Working definition.** The frame relative to which a statement holds — geographic, cultural, temporal, organisational or programmatic — such that a regularity observed in one setting is never silently treated as universal.

**Repository basis.** `PROJECT_OVERVIEW.md` Ch1.2 (the multidimensional layers of context, including community relationships, housing and environment, institutional interactions); Ch6.1 (universal capability, locally adaptable execution); `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch9, which supplies the three-layer framework directly — Universal Business Principles, Regional Business Practices, Organisation-Specific Operational Policies; the per-domain policy altitudes in every `05-business-rules.md`; `BUSINESS_MASTER_PLAN.md` §2 Initial Applicability Context (added under B1).

**Cross-check.** This is the element that makes Rule AR-5's universal-or-variable tag operable. Before remediation B1 no applicability context existed, so no variable Constraint could name its scope; that is now possible.

**Known weakness.** `ASSUMPTION_REGISTER.md` AR-013 remains open on which cultural frameworks beyond Islamic giving are in scope.

---

## Stage 6.1 Cross-Check — Can every qualified concept be described in Stable Core terms?

`KHIDMAT_FOUNDATION_PIPELINE.md` §6.1 requires confirmation that every Stage 5 qualified concept "can be described in terms of the core (has identity, participates in relationships, carries evidence, exists in time, carries uncertainty, exists in context)," and states that "a concept that can't be aligned this way is a signal to revisit Stage 5, not to bypass the core."

The check was run across the concept inventories of all ten domains (the seven original plus Human Reality, Vulnerability/Risk/Protection, and Giving/Resource-Origin). Result: **no concept was found that cannot be described in Stable Core terms.** Two classes required attention and are recorded rather than forced:

1. **Concepts whose *uncertainty* description is empty.** Most Operational Knowledge concepts (Case Note, Waybill, Registration Status) carry no epistemic status because they are records rather than claims about reality. This is correct behaviour, not misalignment — Article IV excludes them from the shared foundation in any case.

2. **Concepts whose *context* scope cannot yet be named.** Every Constraint tagged universal in the seven original domains falls here. They are describable in Stable Core terms; their scope tag is simply untested. Rule AR-5 and `ONTOLOGY_DESIGN.md` §5 both require these to remain visibly untested, which they do.

**Two concepts were flagged as not yet alignable and returned to their domains rather than accepted:**

- **Priority / Severity** — cannot be described in evidence or uncertainty terms because no repository source states how it is derived. Held unclassified per the B6 rubric; recorded as an open question in `case-management/03b-need-model.md` §4.
- **Human Development Stage transition** — the states are describable, the transitions are not, because no evidence criteria exist for movement between them. Recorded as an open question in `accountability-evaluation/03b-outcome-model.md` §7.

Per the pipeline's own instruction, these are signals to revisit discovery, not grounds to bypass the core. Both are logged in their owning domains.

---

## Stage 6.2 Readiness Gate — Status

`KHIDMAT_FOUNDATION_PIPELINE.md` §6.2 lists five conditions. Their state as of this document:

| Condition | State |
|---|---|
| Business Master Plan authored and signed off (Stage 2) | Authored; amended v1.3 under B1. Sign-off is part of Package A (B12). |
| HBRM drafted and signed off (Stage 3) | Drafted and frozen. Sign-off is part of Package A. |
| Business Architecture reconciled and adopted (Stage 4) | Adopted. The reconciliation step the pipeline specified was performed retrospectively under remediation B2. |
| Provisional Constitution governance answers exist (domain-approval authority, audit authority) | **Satisfied.** `CONSTITUTION.md` Articles XVII and XVIII compose both authorities. |
| Stage 5 output exists for the domain being designed | Ten domains exist. Three are marked REQUIRES FURTHER DISCOVERY and all ten record `Client Validation: Pending`. |

**Gate status: not passed.** It cannot be passed by this remediation phase. It is blocked on remediation B12 (Package A approval, which only the Domain Approval Authority may grant) and B13 (ground truth channel, which only the Project Lead may open).
