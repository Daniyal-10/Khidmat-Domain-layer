---
id: DOC-ONT-001
title: Khidmat Humanitarian Ontology — Domain Primitives
version: 1.0
status: Draft — Ontology Design Phase 1, submitted for Project Lead review
owner: Chief Enterprise Ontologist
reviewers: Project Lead, Domain Approval Authority
created: 2026-07-29
depends_on: docs/00-governance/PROJECT_OVERVIEW.md (v1.0), docs/00-governance/CONSTITUTION.md (v1.0), docs/01-methodology/ONTOLOGY_DESIGN.md (v1.0.0)
consumed_by: Ontology Design Phase 2 (Ontology Layers)
layer: 04-ontology
domain: Ontology Design
tags: [ontology, primitives, phase-1, package-b]
---

# Khidmat Humanitarian Ontology — Domain Primitives

## 1. Introduction

This document is the first authoring act of the Khidmat Humanitarian Ontology. It identifies the canonical set of Domain Primitives from which every later ontology layer will be derived.

It is conceptual ontology design. It contains no layers, no architecture, no engineering, and no implementation artifact of any kind.

Its sole input is the frozen Foundation repository. No concept appears below that is not already supported by Foundation evidence, and where the Foundation is silent or divided, that is recorded as uncertainty rather than resolved by invention.

`ONTOLOGY_DESIGN.md` §1.4 states that producing the ratified primitive list is the first authoring act of the ontology, performed under that framework, from the discovery procedure of its §1.2, and approved under Constitution Article XVI as part of Package B. This document is that act. It is submitted as a draft for review; the primitive set is not closed until ratified.

---

## 2. Purpose of Domain Primitives

The primitive set answers the first question asked of any candidate concept: **what kind of thing is this?**

Its purpose is to make every later modelling decision decidable by rule rather than by the instinct of whoever is authoring that week. Without a fixed set of categories, two authors examining the same Foundation concept will place it differently, and the ontology will accumulate the same fragmentation `PROJECT_OVERVIEW.md` Ch1.1 diagnoses in the sector it serves.

The warrant for the layer comes from Ch5.1, which states that certain forms of knowledge are foundational because every humanitarian domain depends on them, and names identity, relationships, evidence, uncertainty, temporal change and humanitarian context as the minimum structure required to understand reality regardless of domain. Domain Primitives is where that observation becomes operative: before any domain's concepts are modelled, the ontology fixes the categories all domains share.

Two consequences follow, both from `ONTOLOGY_DESIGN.md` §1.4:

- **The set is closed once ratified.** An author who meets a concept that seems to need a new primitive escalates; they do not extend.
- **Every concept is classified under exactly one primary primitive.** Where a concept genuinely appears to need two, the tension is treated as information and escalated, not resolved by permitting dual classification.

---

## 3. Primitive Design Methodology

### 3.1 Governing framework

The method is `ONTOLOGY_DESIGN.md` §1.2 — primitives are discovered by abstraction from validated business reality, never invented in the abstract:

1. Start from evidence, not imagination.
2. Ask the kind-question repeatedly, until answers stop multiplying and begin repeating.
3. Test each candidate against the Knowledge Foundation Boundary (Constitution Article IV).
4. Test the set as a whole for coverage — every validated concept must classify without forced fit.

### 3.2 A methodological reconciliation, stated openly

The phase instruction defines a Domain Primitive as *"an irreducible concept of humanitarian reality"* that *"exists independently in reality."* The canonical framework defines it as *"one of the small, closed set of foundational categories of concept… not a business concept; it is the kind of thing a business concept can be"*, and disqualifies anything concrete enough that *"a future business glossary could sensibly contain an entry for it."*

Read literally, these produce different outputs. The first admits *Person*, *Household*, *Need*. The second excludes them as too concrete and admits *Identity*, *Relation*, *Condition*.

**This document follows the framework reading**, treating "irreducible concept of humanitarian reality" as **irreducible category of humanitarian reality**. Three reasons, offered so the choice can be challenged rather than assumed:

1. **Constitutional.** `ONTOLOGY_DESIGN.md` is canonical and, under Article XIV, supreme over all downstream ontology design content. A phase instruction does not override it.
2. **Structural.** The phase instruction itself states that every later layer — Facets, Entities, Relationships, Constraints, States, Events, Cognition, Coordination Patterns — *"must be derived from these primitives."* If a primitive were *Person*, no derivation would occur: Person would simply **be** an entity. Only categories can stand above eight layers that include both Entities and Relationships.
3. **Internal to the instruction.** It states that *"different terms may refer to the same primitive"* and *"a single term may refer to different primitives depending on context,"* and that the ontology must model reality rather than vocabulary. Both statements presuppose primitives sitting beneath vocabulary — which is what a category does and a concrete concept does not.

The phase instruction's seven tests are nonetheless applied in full, as an additional screen alongside the framework's. Where the two impose different requirements, both must pass.

### 3.3 What was excluded by construction

Rejected without further examination, per the phase instruction: workflows, business processes, organisational structures, software objects, database entities, reports, interfaces, implementation conveniences, derived classifications, policies as documents, and procedures.

---

## 4. Primitive Identification Method

Every candidate below was tested against all twelve criteria — the phase instruction's seven and the framework's five.

| # | Test | Source |
|---|---|---|
| T1 | **Ontological Independence** — exists independently of organisations, policies, workflows, software | Phase instruction |
| T2 | **Irreducibility** — cannot be decomposed into simpler domain categories without losing identity | Phase instruction |
| T3 | **Reality** — exists in humanitarian reality rather than documentation, language or implementation | Phase instruction |
| T4 | **Persistence** — would continue to exist if every humanitarian organisation disappeared | Phase instruction |
| T5 | **Necessity** — removal would leave humanitarian reality fundamentally incomplete | Phase instruction |
| T6 | **Non-Derivation** — not created by combining other accepted primitives | Phase instruction |
| T7 | **Foundation Evidence** — supported by evidence already in the Foundation | Phase instruction |
| T8 | **Abstract** — a category of concept, not itself a catalogue concept | `ONTOLOGY_DESIGN.md` §1.3 |
| T9 | **Universal across humanitarian domains** — required whether health, education, shelter, livelihoods, disaster response, or a domain not yet discovered | §1.3 |
| T10 | **Minimal** — removing it leaves some class of validated knowledge unclassifiable, not merely awkward | §1.3 |
| T11 | **Evidence-grounded in use** — at least one validated Foundation concept already requires it | §1.3 |
| T12 | **Knowledge Foundation Boundary** — its omission would materially change understanding of humanitarian reality or the quality, safety, fairness or appropriateness of a humanitarian decision | Constitution Article IV |

A candidate failing any one test is not accepted.

---

## 5. Domain Primitive Identification Process

### 5.1 Evidence base

The kind-question was asked of the concept inventories of all ten Foundation domains, together with `FOUNDATION_CONCEPTS.md` Parts I and II, `SHARED_CONCEPT_CATALOG.md`, `CONCEPT_OWNERSHIP.md` §§8–9, `KNOWLEDGE_TRANSFORMATION_PATTERNS.md`, and `GLOSSARY.md` in its status as Candidate Vocabulary. Approximately 150 concepts were examined.

### 5.2 Recursion to stability

Asking *what kind of thing is this?* of each concept, and then of each answer, the answers stopped multiplying at eight. A representative trace:

| Foundation concepts examined | Kind-answer reached |
|---|---|
| Person · Household · Family · Community · Organisation · Programme · Case · Grievance · Inventory Item · Coordination Cluster | that which persists and must be re-identified |
| Kinship · dependency · household membership · guardianship · partnership · custody transfer · referral · need-influences-need · trust edge | a connection between things that already persist |
| Health condition · shelter condition · capability · livelihood · engagement stage · development stage · need status · trust level · resilience · stock level | something true of a thing across a span, which can change |
| Registration initiated · consent granted · displacement · birth · death · job loss · verification visit · delivery · complaint received · trust suspended · profiles merged | something that happened at a point |
| Document · biometric · testimony · community attestation · field observation · proof of delivery · baseline measurement | that which grounds a belief |
| Claim versus verified · confidence level · gap · contested finding · finding consensus · consequence class · reverification trigger | the warrant the system holds for what it asserts |
| Eligibility rule · consent authorisation · funding restriction · Zakat recipient restriction · operational mandate · separation of duties · domain invariant | that which bounds what is permitted or valid |
| Geographic area · settlement type · cultural context · seasonal calendar · crisis phase · programme scope · organisational scope · applicability scope | the frame relative to which a statement holds |

Eight answers, each recurring across multiple independent domains. No ninth answer survived a second pass.

### 5.3 Relation to the Stable Core

`FOUNDATION_CONCEPTS.md` Part II defines six Stable Core elements. `ONTOLOGY_DESIGN.md` §1.2 anticipates that this list *"predicts roughly where this recursion will stabilize,"* while requiring the actual set to be derived rather than copied. The derivation reached a set that overlaps but is not identical:

- **SC-1 Identity, SC-2 Relationships, SC-3 Evidence, SC-6 Context** — reached directly, as **Identity, Relation, Evidence, Context**.
- **SC-4 Uncertainty** — reached in a **wider** form. The corpus requires not only uncertainty but claim status, informational gaps, contest between assertions, and the consequence class triggering human review. **Epistemic Stance** is the category these share.
- **SC-5 Temporal Change** — reached as **two** categories. The Foundation distinguishes span from point repeatedly and consequentially (SC-5 itself states the distinction), and neither derives from the other. **Condition** and **Occurrence**.
- **Norm** — reached as an **eighth** category with no Stable Core counterpart. Justified in §7.2.

### 5.4 Candidates examined and rejected

Recorded because rejection reasoning is part of the design record.

| Candidate | Rejected because |
|---|---|
| **Person** | Fails T8 (abstract). A concrete concept the Foundation catalogues. Classifies under Identity. |
| **Need** | Fails T8. Classifies under a primitive — but *which* is genuinely contested by Foundation evidence; recorded as an open classification tension in §9.3, not resolved here. |
| **Time** | Fails T2 and T8. `VALIDATION/CERTIFICATION.md` §7 names Time among foundational concepts, so it was examined seriously. Time is the medium in which Condition and Occurrence are distinguished, not a category a humanitarian concept can be classified under. Nothing in the corpus classifies as "a Time." |
| **Place / Location** | Fails T6. Decomposes: a warehouse or settlement is an Identity; an applicability frame is a Context. The Foundation's own unresolved ADR-002 concerns exactly this split, which supports the decomposition rather than a primitive. |
| **Role** | Fails T6. The Foundation separates Actors from Roles in every domain, so this was examined closely. A role is a responsibility held by an identity across a span — Identity plus Condition, or Identity plus Relation. It decomposes without loss. |
| **Trust** | Fails T6. `PROJECT_OVERVIEW.md` Ch6.1 itself classifies Trust as an *emergent property*, *"not a capability that any organisation performs, but an outcome."* An Epistemic Stance accumulated over Evidence. |
| **Capability** | Fails T8 and T6. A Condition of a person. |
| **Dignity** | Fails T3 as a category. A binding commitment (Pillar P5), not a kind of thing a concept can be. Nothing classifies as "a Dignity." |
| **Understanding** | Fails T6. The state of holding an Epistemic Stance judged sufficient under Article III. |
| **Harm / Suffering** | Fails T6. Realised harm is a Condition or an Occurrence; prospective harm is an Epistemic Stance about a Condition. |
| **Intent / Purpose** | Fails T7 and T6. Foundation evidence is thin — `giving-resource-origin` §6.2 mentions donor stated intent only in passing. Where intent is operative it appears as a Norm (a restriction) or a Condition. Recorded as an uncertainty in §9.4 rather than admitted. |
| **Process / Workflow** | Excluded by construction and by Article IV — Operational Knowledge. |
| **Quantity / Measure** | Fails T8 and T9. A dimension of a Condition, and the Foundation consistently prefers qualitative characterisation (`GLOSSARY.md` uses "qualitative" seven times across the risk definitions). |

---

## 6. Canonical Domain Primitives

Eight primitives. Presented alphabetically by name; the order carries no meaning and implies no structure.

---

### P1 — Condition

**1. Primitive Name.** Condition.

**2. Canonical Definition.** That which is true of something across a span of time, and which can change while what it is true of persists.

**3. Humanitarian Reality Represented.** The state a person, household, community or institution is actually in — their health, their shelter, their capability, their livelihood, their vulnerability, their resilience, where they stand in a recovery journey, whether an institution is currently trusted. This is the substance of the sentence *"this is how things are for this family right now."*

**4. Why it is Irreducible.** A condition cannot be decomposed into occurrences without loss: a chronic illness is not the sum of the moments it was observed, and a household's absorptive capacity is not the sum of the shocks it has absorbed. Nor can it be decomposed into relations — a person's malnutrition is true of them, not between them and something else. Removing Condition leaves no category for anything that is *the case* rather than something that *happened*.

**5. Why it Exists Independently of Implementation.** A child is malnourished whether or not any system records it. A roof leaks in the absence of a shelter assessment. `PROJECT_OVERVIEW.md` Ch1.1 grounds the whole project in the observation that these realities exist and current systems fail to represent them.

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** Condition cannot be produced by combining the other seven. It is not an Occurrence (point versus span), not an Identity (it does not persist in its own right and cannot be re-identified except through what it qualifies), not an Epistemic Stance (a condition is about the world; a stance is about what the system may believe of the world), and not a Norm (a condition holds; it does not bind).

**7. Foundation Evidence.** `human-reality/HUMAN_REALITY_DISCOVERY.md` §8.1 (health, capability, education, livelihood, economic circumstance, documentation status, displacement status), §8.3 (housing tenure, shelter condition, utilities access); `vulnerability-risk-protection/` §8.1 and §8.3 (vulnerability; the resilience decomposition into absorptive, adaptive and recovery capacity, corroborated across blueprint §7 and `GLOSSARY.md`); `GLOSSARY.md` Engagement Stage and Human Development Stage; `organisation-partner-management/07` (organisational trust lifecycle); `FOUNDATION_CONCEPTS.md` SC-5.

**8. Known Boundaries.** Condition ends where independent re-identification begins: the moment something must be tracked in its own right across encounters rather than through the thing it qualifies, it is not a Condition. It also ends at the point-in-time boundary — an observation of a condition is an Occurrence; the condition observed is not.

**9. Known Assumptions or Uncertainties.** The Foundation evidences the *dimensions* along which conditions vary but not the *values* they take (`human-reality/` §8.1 states this explicitly and declines to invent them). Whether a condition is held qualitatively or admits degree is unresolved and, per AR-016 and AR-018, several condition-bearing decompositions rest on single unevidenced internal sources.

---

### P2 — Context

**1. Primitive Name.** Context.

**2. Canonical Definition.** The frame relative to which a statement holds — geographic, cultural, temporal, institutional or programmatic — such that what is true within it is not thereby true outside it.

**3. Humanitarian Reality Represented.** That humanitarian reality is local. A household means different things in different cultures. A season turns a damaged roof into an emergency. A rule that binds inside one programme does not bind outside it. The same act of giving carries different obligations in different religious frameworks.

**4. Why it is Irreducible.** Context cannot be decomposed into the things it frames. Remove it and every regularity observed in one setting becomes a claim about all settings — the failure `ONTOLOGY_DESIGN.md` §2.4 names as the gravest of its kind, *"a regularity observed in one context silently encoded as if true everywhere."* No other category carries scope.

**5. Why it Exists Independently of Implementation.** Cultures, seasons and geographies are not artefacts of any system. `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch9 establishes the three-layer distinction between universal principles, regional practices and organisation-specific policies as a feature of humanitarian work itself.

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** A context is not a thing with identity (though places and institutions that have identity may delimit one), not a condition (it is not true *of* something, it is that *relative to which* something is true), and not a norm (it does not bind; it bounds where binding applies).

**7. Foundation Evidence.** `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch9 (Universal / Regional / Organisation-Specific); `BUSINESS_MASTER_PLAN.md` §2 Initial Applicability Context; `FOUNDATION_CONCEPTS.md` SC-6; every domain's `05-business-rules.md`, each of which delineates policy by altitude; `human-reality/` §8.4 (settlement type, livelihood pattern, seasonal hazard calendar); `case-management/05-business-rules.md` and `registration-identity/05-business-rules.md` on cultural variation in the meaning of household.

**8. Known Boundaries.** Context frames; it does not participate. A geographic area that is itself tracked, funded and reported on has crossed into Identity. Context also stops short of the rule it scopes — the scope is Context, the rule is a Norm.

**9. Known Assumptions or Uncertainties.** The Foundation states one applicability context, derived from client-supplied material and explicitly not practitioner-validated. AR-013 remains open on which cultural frameworks beyond Islamic giving are in scope. Two dimensions of the stated context — initial partner set and languages — are recorded as unstated.

---

### P3 — Epistemic Stance

**1. Primitive Name.** Epistemic Stance.

**2. Canonical Definition.** The warrant a knowing system holds for an assertion — whether it is merely claimed or has been verified, how much confidence it currently deserves, what remains unknown about it, whether it is contested, and whether acting on it requires human judgement.

**3. Humanitarian Reality Represented.** That humanitarian reality is never observed whole, only through partial and sometimes conflicting evidence, and that the difference between *what a family said* and *what has been confirmed* is itself a fact about the situation. A registration is a collection of claims until verification says otherwise; two aid workers may report different household compositions and both reports are real.

**4. Why it is Irreducible.** A stance is not the evidence that supports it — the same evidence may warrant different confidence at different times, and a gap in understanding is a stance held with no evidence at all. Nor is it a condition of the world: it is a condition of the *knowing*, and collapsing the two produces exactly the false confidence `PROJECT_OVERVIEW.md` Ch4.2 identifies as the central danger of premature automation.

**5. Why it Exists Independently of Implementation.** Uncertainty about a person's circumstances exists whether or not any system records it. A field worker who is unsure is unsure. Ch1.2 names *"levels of uncertainty, confidence, and verification for every important conclusion"* among the foundational dimensions of humanitarian reality itself, not among the properties of software.

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** It cannot be assembled from the other seven. Without it, Constitution Article III's four-part Standard of Understanding and Article VIII's human-review threshold reference facts the ontology cannot express, and the sequence Knowledge → Understanding → Reasoning → Responsible Action becomes an implementation convention rather than a property of the knowledge.

**7. Foundation Evidence.** `PROJECT_OVERVIEW.md` Ch1.2, Ch2.3 and Ch5.2; `CONSTITUTION.md` Articles III, V and VIII; `FOUNDATION_CONCEPTS.md` SC-4; `GLOSSARY.md` Confidence Level, Claim Basis, Gap, Finding Consensus, Reverification Trigger; the twenty decision points across the Foundation domains, each of which states its residual uncertainty; `registration-identity/04b` ("Identity is not binary; it exists on a spectrum of trust based on the weight of evidence"); `case-management/04b` (the Verification Barrier).

**8. Known Boundaries.** A stance is about an assertion; it is never itself an assertion about humanitarian reality. It also stops at the operational boundary: that a conclusion requires human review is within this primitive; how an escalation is queued, routed or notified is Operational Knowledge and outside the foundation entirely (Ch7.2).

**9. Known Assumptions or Uncertainties.** The Foundation supplies the criteria by which evidence strength is judged (Ch5.2's seven factors) but not the grading scheme practitioners actually recognise — ADR-004 is open on exactly this. `case-management/10-open-questions.md` records unanswered how a suspected but unevidenced vulnerability is represented. Both are content questions inside this primitive, not challenges to its status.

---

### P4 — Evidence

**1. Primitive Name.** Evidence.

**2. Canonical Definition.** That which grounds a belief about humanitarian reality and whose origin can itself be identified and examined.

**3. Humanitarian Reality Represented.** The observations, documents, testimony, measurements and artefacts through which humanitarian circumstances become knowable — a birth certificate, a biometric, a community elder's word, a field observation, a signature at handover, a baseline measurement.

**4. Why it is Irreducible.** Evidence is not the stance it supports; the same document may be decisive in one matter and irrelevant in another. It is not an occurrence, though occurrences frequently generate it and are often themselves evidential. It is not a condition of the thing it concerns. Remove it and Constitution Article V's central distinction — between an assertion recorded and an assertion grounded — becomes inexpressible.

**5. Why it Exists Independently of Implementation.** A document exists, a person's testimony was given, a measurement was taken, whether or not any system holds them. `PROJECT_OVERVIEW.md` Ch5.2 defines evidence by the examinability of its origin, which is a property of the thing rather than of any store.

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** No combination of the other seven produces it. The temptation is to fold it into Epistemic Stance; the Foundation resists this deliberately and so does this design. Ch5.2 treats evidence as a thing that is gathered, weighed, corroborated, preserved when conflicting, and capable of expiring — none of which is true of a stance.

**7. Foundation Evidence.** `PROJECT_OVERVIEW.md` Ch5.2; `CONSTITUTION.md` Article V; `FOUNDATION_CONCEPTS.md` Part I §4 and SC-3; `SHARED_CONCEPT_CATALOG.md` §2 (evidence as polymorphic across documents, biometrics, attestations and professional assessments); the claim–evidence–verification spine present in all ten domains; validation finding MAJ-01 and remediation REM-02 establishing polymorphic validity, some evidence immutable and some expiring.

**8. Known Boundaries.** Evidence stops at the belief it grounds. It also stops short of the record that holds it: the proof carried by a delivery receipt is Evidence; the receipt as an administrative artefact is Operational Knowledge (`resource-logistics/03-concepts.md`, reconciled under remediation B6).

**9. Known Assumptions or Uncertainties.** What weight practitioners actually assign to each kind of evidence is undiscovered (ADR-004). `registration-identity/05-business-rules.md` supplies the Foundation's only concrete sufficiency rule — two distinct points of evidence to reach Verified — and it is organisation-scoped, not universal.

---

### P5 — Identity

**1. Primitive Name.** Identity.

**2. Canonical Definition.** That which persists through time and must be recognisable as the same thing across separate encounters, organisations and years.

**3. Humanitarian Reality Represented.** The continuity on which every other kind of understanding accumulates — that this woman presenting today is the same woman assessed eighteen months ago, that this household is the one that received assistance last winter, that this organisation is the one whose accreditation lapsed.

**4. Why it is Irreducible.** Persistence and re-identifiability cannot be assembled from anything simpler. A thing's conditions, relations and history are all predicated on there being a *thing* they attach to; remove Identity and there is nothing for them to attach to, and the knowledge-reset failure of `PROJECT_OVERVIEW.md` Ch1.3 is rebuilt inside the ontology.

**5. Why it Exists Independently of Implementation.** A person is the same person across organisational boundaries whether or not any registry recognises them. `registration-identity/12-domain-invariants.md` states it as an invariant: *"The Primacy of the Beneficiary — a beneficiary exists independently of a household,"* and *"Identity is Immutable, Attributes are Mutable."*

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** It is presupposed by three of the other seven rather than derived from any. It is not a condition (conditions are true *of* identities), not a relation (relations hold *between* them), not an occurrence (occurrences happen *to* them).

**7. Foundation Evidence.** `FOUNDATION_CONCEPTS.md` Part I §§1–2 and SC-1; `human-reality/HUMAN_REALITY_DISCOVERY.md` §3 and §8 (person, family, household, community); `organisation-partner-management/` (organisation, consortium); `CONTRADICTION_LOG.md` CL-001 (Programme ratified as distinct); `SHARED_CONCEPT_CATALOG.md` §1 (*"Identity cannot be treated as a simple string… the architecture must decouple the core Identity from the roles it plays"*); `registration-identity/08` §2, which establishes that re-identification is contested, produces false positives, and requires human adjudication.

**8. Known Boundaries.** Identity stops where independent re-identification stops. A dimension findable only through the thing it qualifies is not an Identity. It also stops short of the assurance that two encounters concern the same thing — that judgement is an Epistemic Stance about an Identity, not the Identity itself.

**9. Known Assumptions or Uncertainties.** Identity criteria for Household are undiscovered: how a household is re-identified across a split or merge is recorded as an open question in `human-reality/` §18 and was never answered by the Foundation, despite `SHARED_CONCEPT_CATALOG.md` §1 raising it. This is the single most consequential open question bearing on this primitive.

---

### P6 — Norm

**1. Primitive Name.** Norm.

**2. Canonical Definition.** That which bounds what is permitted, required or valid — independently of whether it is observed in any given instance.

**3. Humanitarian Reality Represented.** The obligations and permissions that actually govern who may receive what: an eligibility criterion, a funding restriction that follows money from its giver to its recipient, a religious obligation attaching to a form of giving, a person's authorisation to have their information shared, a mandate an organisation holds, a safeguarding protocol, a separation of duties.

**4. Why it is Irreducible.** A norm is not a condition. A condition holds; a norm binds, and it continues to bind when it is breached — which is precisely why breach is meaningful. Nor is it a relation between identities, though it frequently governs one. Remove Norm and eligibility rules, consent authorisations, funding restrictions, mandates and invariants are all homeless, and with them the Foundation's most decision-determining knowledge.

**5. Why it Exists Independently of Implementation.** Obligation is not created by recording it. The clearest Foundation case is Zakat: `giving-resource-origin/` establishes that recipient-category restriction is an obligation carried by the resource itself, not a configurable policy — it would bind whether or not a single humanitarian organisation existed to administer it. Kinship obligations, religious duties and the customary authority of a community elder are of the same kind.

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** This is the one primitive with no Stable Core counterpart, so its warrant is set out at greater length. Three attempts to derive it were made and each failed. As a **Condition of an Identity** — fails, because a norm survives the identity it governs and applies to identities not yet existing. As a **Relation** — fails, because a norm binds absent any second party, as a household's own customary obligation does. As **Context** — fails, and the distinction matters most here: Context says *where* something holds, Norm says *what* holds. A rule and its scope are two things, and `ONTOLOGY_DESIGN.md` AR-5 requires them to be separately stated, which is impossible if they are one category.

The corroborating evidence is that the Foundation's most consequential content is normative. `KNOWLEDGE_TRANSFORMATION_PATTERNS.md` §4.5 traces an unbroken chain — donor mandate, programme allocation, intervention catalogue, eligibility rule, support plan approval — in which every link is a Norm, and observes that this chain is where the ethical friction of humanitarian work is generated.

**7. Foundation Evidence.** `programme-management/03-concepts.md` (Eligibility Rule, reclassified as Reality Knowledge under remediation B6 precisely because it determines who receives assistance); `giving-resource-origin/` §8.2 (Zakat-Eligible Category as a classification an eligibility rule may reference) and §12; `registration-identity/03-concepts.md` (Foundational Consent, reclassified as Reality Knowledge under B6 on the ground that Constitution Article IX makes consent a right of the person); `organisation-partner-management/` (operational mandate); every domain's `12-domain-invariants.md`; `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch9; `STAGE_5_DISCOVERY_STANDARD.md` §6.2, whose second rubric question — *does the concept determine, constrain, or justify who receives what assistance?* — is in effect a test for this primitive.

**8. Known Boundaries.** Norm stops at the organisational procedure that implements it. An eligibility rule is a Norm; an internal approval chain is Operational Knowledge (Article IV). It also stops short of the judgement that a norm is satisfied in a particular case — that judgement is an Epistemic Stance.

**9. Known Assumptions or Uncertainties.** The Foundation's most significant normative content is deliberately unpopulated: the obligation basis and restriction shape of each of the seven Islamic giving forms, and the eight Zakat recipient categories, are recorded in `giving-resource-origin/` §8.2 as undiscovered and explicitly not invented, under AR-017. Within the stated applicability context this is eligibility-determining content. It constrains what can be *populated* under this primitive; it does not affect the primitive's status.

---

### P7 — Occurrence

**1. Primitive Name.** Occurrence.

**2. Canonical Definition.** That which happens at a point in time and, once happened, is part of history.

**3. Humanitarian Reality Represented.** The events through which circumstances came to be what they are — a displacement, a birth, a death, a marriage, an injury, the loss of a job, the gaining of one, a child leaving school, a verification visit, a handover of goods, the withdrawal of consent, the suspension of a partner.

**4. Why it is Irreducible.** An occurrence cannot be reconstructed from the conditions it produced: a household that lost its home and a household that never had one may be in the same condition and did not arrive there the same way. `PROJECT_OVERVIEW.md` Ch1.2 requires the foundation to preserve *"what events led to the current situation"*; explanation is causal history, and no other category carries it.

**5. Why it Exists Independently of Implementation.** Floods occur, people are born and die, and jobs are lost whether or not any system observes them. The Foundation's own worked example (Ch4.1) is a family arriving at a relief camp after flooding — an occurrence preceding every record of it.

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** Not derivable from Condition — the point/span distinction is exactly what separates them, and `FOUNDATION_CONCEPTS.md` SC-5 states that distinction as foundational. Not an Identity: an occurrence is never re-identified as the same event continuing. Not Evidence, though many occurrences are evidential; the verification visit and the grounds it produced are two things.

**7. Foundation Evidence.** Approximately seventy business events across the Foundation domains' `06-business-events.md` files; `human-reality/HUMAN_REALITY_DISCOVERY.md` §8.5, which catalogues twelve life events each with a repository source and declines four for lack of evidence; `FOUNDATION_CONCEPTS.md` SC-5; `GLOSSARY.md` Lifecycle Transition and Trajectory; `CONSTITUTION.md` Article X(c) on the traceability of the evidence chain after the fact.

**8. Known Boundaries.** Occurrence stops at the span: a condition that obtained over a period is not an occurrence, however precisely its onset is known. It also stops at the record: the event happened, the record of it is a separate matter, and the Foundation's discipline that history is never silently rewritten depends on that separation.

**9. Known Assumptions or Uncertainties.** The Foundation's life-event catalogue is explicitly non-exhaustive and Tier C — `human-reality/` §8.5 names return, resettlement, eviction and disaster exposure as plausible but unevidenced, and declines to add them.

---

### P8 — Relation

**1. Primitive Name.** Relation.

**2. Canonical Definition.** That which holds between things that persist, and which carries meaning of its own beyond the things it connects.

**3. Humanitarian Reality Represented.** The connections in which humanitarian reality actually consists — a mother and the infant who depends on her, a household and the people who compose it, a guardian and a minor, a caregiver and the person cared for, two organisations bound by a partnership, an unmet need that blocks another from being addressed.

**4. Why it is Irreducible.** A relation is not a property of either party. `PROJECT_OVERVIEW.md` Ch5.1 states that humanitarian reality is *"deeply relational, where meaning emerges from relationships rather than isolated records"*, and Ch1.2 that understanding one person requires understanding the relationships in which they exist. If a connection were reducible to an attribute of one side, nothing could be said about the connection itself — that it is claimed but unverified, that it began after a displacement, that it ended — without distorting one of the parties.

**5. Why it Exists Independently of Implementation.** Kinship, dependency and cohabitation exist whether or not recorded. `human-reality/` §8.2 records dependency as typed, directional and cascading, on the strength of Foundation evidence about how households actually work.

**6. Why it Qualifies as a Primitive rather than a Derived Concept.** It presupposes Identity but is not composed of it: two identities do not constitute a relation, and the same two may stand in several at once. It is not a Condition of either party, and not a Norm, though norms frequently attach to relations.

**7. Foundation Evidence.** `PROJECT_OVERVIEW.md` Ch1.2 and Ch5.1; `FOUNDATION_CONCEPTS.md` SC-2; roughly forty-five relationships across the Foundation domains' `04-relationships.md` files; `human-reality/` §8.2 (kinship, typed dependency, responsibility) and §9; `GLOSSARY.md` need-influences-need with its three qualifiers; `organisation-partner-management/04-relationships.md` (partnership, consortium); `cross-organisational-coordination/04b` (the consent chain).

**8. Known Boundaries.** Relation requires both terms to persist; a connection to something with no independent identity is a dimension of one party, not a relation. It also stops short of the recurring multi-party configurations the Foundation documents as patterns — a single connection is within this primitive; a recurring shape composed of many is not, and its treatment belongs to a later phase.

**9. Known Assumptions or Uncertainties.** The Foundation evidences that relations exist but frequently not their temporal validity or plurality — whether a person may hold concurrent membership in two households is recorded as unanswered in `human-reality/` §18, and the same silence affects most relations in the corpus. `GLOSSARY.md`'s need-influences-need qualifiers are Carried unvalidated under AR-018.

---

## 7. Primitive Design Rationale

### 7.1 Why eight

The recursion of §5.2 stabilised at eight, and each survives the minimality test T10 — removing any one leaves a class of validated Foundation knowledge unclassifiable rather than merely awkward:

| Remove | What becomes unclassifiable |
|---|---|
| Condition | Everything that is the case rather than something that happened |
| Context | Scope; every regional practice silently becomes universal |
| Epistemic Stance | Constitution Articles III and VIII reference facts the ontology cannot express |
| Evidence | Article V's distinction between an assertion recorded and one grounded |
| Identity | Continuity; the knowledge-reset failure of Ch1.3 returns |
| Norm | Eligibility rules, consent authorisations, funding restrictions, mandates, invariants |
| Occurrence | Causal history; nothing can be explained |
| Relation | The connections in which Ch5.1 says humanitarian meaning consists |

### 7.2 The two departures from the Stable Core, justified

**Splitting Temporal Change into Condition and Occurrence.** Justified because the Foundation makes the point/span distinction load-bearing rather than incidental — SC-5 defines the element by that distinction, and neither side derives from the other. Merging them would place a chronic illness and the moment of its diagnosis in one category, which no Foundation source treats as one kind of thing.

**Adding Norm.** Justified in full at P6.6. In summary: the derivation attempts fail; the Foundation's most decision-determining content is normative; and the B6 rubric's second question already operates as a test for it.

### 7.3 Why Person, Need and Household are absent

Not because they are unimportant — they are the most important concepts in the Foundation. They are absent because they are concepts, and this phase identifies the categories concepts fall under. Their placement is the work of the next phase, and pre-empting it here would be doing that phase's work under this phase's name.

---

## 8. Primitive Design Principles

Applied throughout and recorded so that the next phase inherits them:

- **Reality before implementation.** No primitive presupposes a system.
- **Cognition before workflow.** Epistemic Stance is a primitive; escalation mechanics are excluded entirely.
- **Concepts before schemas.** Nothing below is a class, attribute, property or hierarchy.
- **Evidence before assumptions.** Every primitive cites Foundation evidence; every uncertainty is recorded rather than closed.
- **Discovery before modelling.** The set was reached by abstraction from ~150 Foundation concepts, not adopted from any upper ontology.
- **One canonical meaning per primitive.** No two primitives cover the same ground; the nearest pairs (Evidence/Epistemic Stance, Condition/Occurrence, Context/Norm) are separated explicitly in their Known Boundaries.
- **Record uncertainty rather than invent certainty.** Twelve candidates were rejected with reasons; three classification tensions are recorded unresolved in §9.
- **The ontology models reality, not language.** *Vulnerability* names a Condition in one Foundation usage and an Epistemic Stance in another; that is a fact about the word, and it is recorded rather than legislated away.

---

## 9. Known Design Assumptions

### 9.1 Inherited from the Foundation, and material to this phase

The Foundation is Tier C throughout at declared Medium confidence, with no practitioner validation (remediation B13 deferred). Every primitive is therefore abstracted from evidence that is internally coherent and externally unvalidated. `ONTOLOGY_DESIGN.md` §6 permits this for concept admission and layer placement while forbidding it as the basis for tagging anything universal — a restriction that binds later phases and is noted here so it is not lost.

### 9.2 Assumption of the methodological reconciliation

§3.2's reading of "primitive" as category rather than concrete concept is a design decision, not a Foundation finding. If the Project Lead intends the concrete reading, this document does not answer the question asked, and the correct response is to say so at review rather than to reinterpret it later.

### 9.3 Recorded classification tensions — not resolved here

`ONTOLOGY_DESIGN.md` §1.4 requires that a concept appearing to need two primitives be escalated as information rather than resolved by dual classification. Three such tensions surfaced and are escalated:

- **Need.** `GLOSSARY.md` defines it as a gap between current state and a standard of wellbeing, which is a Condition. `case-management/03b-need-model.md` records it as tracked across its lifetime, versioned, and standing in typed relations to other needs, which is Identity. Both readings are Foundation-supported.
- **Location.** Decomposes into Identity and Context, as §5.4 records. The Foundation's own ADR-002 is open on the related ownership question.
- **Consent.** Remediation B6 split it into the person's act and the organisational record. On this primitive set the act is an Occurrence and the authorisation it creates is a Norm — arguably a third split. Recorded for the next phase.

### 9.4 Candidates left open rather than rejected outright

**Intent.** Rejected at §5.4 on thin Foundation evidence rather than on principle. Should practitioner contact surface intent as operative in its own right, this would be a legitimate primitive-set escalation under §1.4 rather than a defect in this derivation.

---

## 10. Primitive Completeness Assessment

### 10.1 Validation against the five required conditions

**Every accepted primitive passed the Primitive Identification Method.**

| | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Condition | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Context | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Epistemic Stance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Evidence | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Identity | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Norm | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Occurrence | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Relation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

One test warrants comment rather than a tick alone. **T4 (Persistence)** applied to Epistemic Stance was examined closely, since a stance appears to require a knower. It passes because the Foundation locates uncertainty in reality rather than in systems: `PROJECT_OVERVIEW.md` Ch1.2 names levels of uncertainty and verification among the dimensions of humanitarian reality itself, and a field worker's uncertainty about a family's circumstances exists independently of any organisation persisting.

**No accepted primitive is derivable from another.** Every pair was tested. The four closest pairs, and why each holds apart: Evidence / Epistemic Stance — the ground versus the warrant, separable because the same ground supports different warrants over time. Condition / Occurrence — span versus point, the distinction SC-5 makes foundational. Context / Norm — where a rule holds versus what it requires, which AR-5 requires be separately statable. Identity / Relation — relations presuppose identities but are not composed of them.

**No accepted primitive is implementation-dependent.** None references a system, store, format, interface or process. The two that most invite it were tested specifically: Epistemic Stance excludes escalation mechanics (Ch7.2); Evidence excludes the records that hold it (`resource-logistics/03-concepts.md`, per B6).

**No accepted primitive duplicates another.** Each Known Boundaries section states where the primitive stops relative to its nearest neighbour.

**The set provides a sufficient conceptual foundation for the subsequent phase.** Demonstrated by the coverage test required at `ONTOLOGY_DESIGN.md` §1.2 step 4, run across the concept inventories of all ten Foundation domains. Every concept classified without forced fit, with three exceptions, all recorded rather than concealed:

- **Need**, **Location** and **Consent** classify under two primitives each. Per §1.4 these are escalated as information (§9.3), not resolved by dual classification. Note that a concept resolvable to *two* primitives is evidence the set covers it, not evidence of a gap — the gap case is a concept resolvable to *none*, and none was found.
- Concepts correctly excluded by Article IV as Operational Knowledge — case notes, waybills, registration status, queue mechanics — classify nowhere, which is the intended behaviour.

### 10.2 Assessment

The set is sufficient to proceed. It is minimal, mutually irreducible, evidence-grounded in the frozen Foundation, and demonstrably covers the Foundation's concept inventory.

Two limitations qualify that assessment without undermining it. The evidential base is Tier C and unvalidated by practitioners, so the set is as sound as the Foundation and no sounder. And the set is a **draft**: under §1.4 it becomes closed only on ratification, and the three classification tensions and one open candidate recorded in §9 are precisely the material a reviewer should test it against.

**Assessment: the Domain Primitive set is sufficient to progress to Ontology Layers.** That work is not begun, outlined or anticipated here.

---

*End of Ontology Design Phase 1. This document contains no ontology layers, no architecture, no governance design, and no engineering artifact. It is submitted for Project Lead review under Constitution Article XVI.*
