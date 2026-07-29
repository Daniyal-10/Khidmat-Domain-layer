---
id: DOC-DISC-HUMAN_REALITY
title: HUMAN REALITY DOMAIN DISCOVERY
version: 1.0
status: Draft
owner: Discovery
created: 2026-07-29
remediation: B2 (closes Foundation Gaps FG-1, FG-2, FG-7)
governed_by: docs/00-governance/STAGE_5_DISCOVERY_STANDARD.md
---

# Human Reality Domain Discovery Report

> **Provenance statement — read first.**
> This domain was authored under remediation B2 of the accepted Foundation Readiness Assessment. It is **not new discovery**. Its root cause is recorded in that assessment: `KHIDMAT_FOUNDATION_PIPELINE.md` Stage 4 required the prior business architecture blueprint to be reviewed section-by-section and its content separated between HBRM and Business Architecture. That step was never performed. The human-reality content was archived instead of reconciled, and the canonical chain lost it.
>
> This document performs that skipped reconciliation. Every statement below is a **promotion of existing repository content**, carrying its source. Nothing is added because it is common humanitarian practice. Where repository evidence is insufficient, that is stated rather than filled.
>
> **Evidence tiers used** (per the Business Discovery Blueprint tiering already in use in TD-01–TD-06):
> - **Tier C — project-internal artifacts:** `PROJECT_OVERVIEW.md` Ch1.2; `98-archive/execution_cleanup/BUSINESS_ARCHITECTURE_BLUEPRINT.md` §§5–8 (deprecated, re-entering through this document exactly as `ONTOLOGY_DESIGN.md`'s preamble requires); `GLOSSARY.md` Human Model Terms and Community Context Terms; client blueprint `direct-relief-architecture.html`.
> - **Tier A/B/D — not executed.** No practitioner elicitation, sector-standard retrieval, or literature pass was performed for this domain. This is a **Discovery Limitation carried at document level**, identical in kind to the limitation every TD dossier carries, and it is the reason this domain is `status: Draft` and not `READY FOR FREEZE`.

---

## 1. Purpose

The Human Reality Domain exists to hold the **multidimensional reality of the people humanitarian assistance serves** — the person, the family, the household, and the community — as reality, prior to and independent of any organisational process applied to them.

It solves a problem the repository created for itself. `PROJECT_OVERVIEW.md` Ch1.1 diagnoses the sector's failure as systems "designed to manage Programmes and transactions, rather than to understand people and their lived reality," and Ch1.2 states that "most systems capture a person as a single point in time rather than as a continuously evolving human journey." Stage 5 discovery, organised by operational domain, described the processes applied to people (registration, casework, delivery, evaluation) and did not describe the people. Registration & Identity holds a registry record; Case Management holds a workflow record. Neither holds a person.

No other domain can own this. Registration & Identity's own boundary statement (`registration-identity/02-boundaries.md`) explicitly excludes "assessing the vulnerability or needs of the beneficiary." Case Management's boundary is the case, which is bounded and closable, whereas a person persists across cases by design (`GLOSSARY.md`, Engagement Stage vs Human Development Stage). Programme Management "never evaluates the specific vulnerability of an individual household; it evaluates population aggregates" (`programme-management/12-domain-invariants.md`).

**Boundary against Registration & Identity, stated explicitly.** Registration & Identity owns *identity assurance* — establishing and proving that a person is who they are claimed to be, deduplicating, and holding foundational consent. This domain owns *what is true of that person* once identified, and the social units they exist within. The seam is: Registration answers "is this the same human being?"; Human Reality answers "what is this human being's situation?"

## 2. Business Outcomes

- A representation of a person as a persisting human being with a life history, not as a per-case record.
- A representation of the family, household and community a person exists within, such that the wellbeing of one member is understandable in terms of those they depend on and who depend on them.
- The dimensional substrate that makes it possible to say *why* two households that appear identical on paper are not equally vulnerable.
- A record of the life events through which circumstances came to exist, so that change over time is explainable rather than merely observed.

## 3. Stakeholders

### Actors (Enduring Participants)
- **Person / Individual:** The human being. Persists across cases, programmes, organisations and time. *(Source: `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §5.1 "A person is a persistent entity, not a per-case record"; `FOUNDATION_CONCEPTS.md` §1; `registration-identity/12-domain-invariants.md` "The Primacy of the Beneficiary".)*
- **Family:** A social unit connected through kinship, caregiving, marriage or guardianship. Distinct from a household. *(Source: `GLOSSARY.md`, Human Model Terms: "A family is distinct from a household. Multiple families may exist within a household.")*
- **Household:** The unit of people sharing living conditions and pooled resources; the primary context for assessing vulnerability and need. *(Source: `GLOSSARY.md`, Core Terms.)*
- **Community:** The settlement and social fabric within which households exist. *(Source: `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §8; `GLOSSARY.md`, Community Context Terms.)*

### Roles (Transient Responsibilities)
- **Head of Household:** The member recognised, by the household itself or by local convention, as holding representational authority for it. *(Source: `registration-identity/08-decision-points.md` §3, which records that headship is disputed in practice and is a decision, not a fact.)*
- **Caregiver:** A person carrying responsibility for the care of a dependent member. *(Source: `case-management/01b-stakeholders.md`; `GLOSSARY.md` Dependency.)*
- **Dependant:** A person relying on another for care, support, resources, supervision, protection or decision-making. *(Source: `GLOSSARY.md`, Dependency; `registration-identity/03-concepts.md`.)*
- **Income Earner / Provider:** The member(s) carrying responsibility for household income. *(Source: `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §6, "Responsibility — who is responsible for income, caregiving, education, decision-making".)*

**Note on Beneficiary.** *Beneficiary* is not an actor in this domain. It is a transient role a person occupies when interacting with the humanitarian system, per `TERMINOLOGY_HARMONIZATION.md` §5: "We adopt **Individual** as the structural entity, and **Beneficiary** strictly as a transient role."

## 4. Business Capabilities

This domain owns no execution capability. It is a knowledge domain, and the capabilities that read from it are owned elsewhere (Evidence & Knowledge Acquisition and Understanding Formation, both allocated to Case Management by `BUSINESS_ARCHITECTURE.md` §6). What this domain owns is the **subject matter** those capabilities form an understanding *of*.

Stated as capabilities of the knowledge foundation rather than of an organisation:
- Representation of the person as a persisting subject with a life history.
- Representation of family, household and community structure and their change over time.
- Representation of the dimensions along which a person's situation varies.
- Representation of dependency and responsibility between people.

## 5. Core Business Activities

- Recording the composition of a household and the family relationships within it.
- Recording who depends on whom, for what.
- Recording the dimensions of a person's situation as they are observed.
- Recording life events as they occur and revising the above accordingly.
- Recording the community context a household sits within.

*(These are activities of the knowledge foundation. The operational procedures by which any organisation performs them — forms, intake scripts, survey instruments — are Operational Knowledge under Constitution Article IV and are out of scope.)*

## 6. Business Decisions

Only decisions genuinely evidenced in the repository are recorded. Two exist.

### 6.1 Household Composition Decision
*This decision is already discovered and owned in `registration-identity/08-decision-points.md` §3. It is referenced here, not duplicated, per Rule AR-3 (one concept, one definition, one home). Its content is unchanged.*

Summary of the reference: determining who operationally belongs to a household; decided by the Registrar informed by the Head of Household; governed by a definition often expressed as "eating from the same pot"; constrained by culturally complex family structures; outcomes are joined / newly formed / split; escalates on spousal dispute over headship; the Registrar may override strict biological definitions to reflect de facto living situations; and it carries high uncertainty during active conflict.

### 6.2 Dependency Attribution Decision
- *Purpose:* Determining who depends on whom, for what, and therefore whose vulnerability cascades to whom.
- *Decision Maker:* Not evidenced. **Insufficient repository evidence.**
- *Supporting Evidence:* Household composition; observed caregiving and income responsibility. *(Source: `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §6.)*
- *Governing Policies:* Not evidenced.
- *Constraints:* Dependency is frequently informal and unrecorded; the same person may be simultaneously dependant and provider.
- *Preconditions:* Household composition recorded.
- *Alternative Outcomes:* Not evidenced.
- *Escalation / Review / Appeal / Override:* Not evidenced.
- *Uncertainty:* The repository asserts the *consequence* of dependency — "a vulnerability in one member cascades to those who depend on them: a mother's risk is her infant's risk" (`98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §6) — without evidencing how the dependency itself is established in practice.

**Recorded gap.** Both decisions above are thinner than the twenty decision points in the existing seven domains. That is a truthful reflection of the evidence available, not an omission. Closing it requires Tier A (remediation B13).

## 7. Information Requirements

- Household composition and the kinship relations within it.
- Who carries responsibility for income, caregiving, education and decision-making.
- The dimensions of each member's situation (Section 8).
- The community and settlement the household sits within.
- Life events affecting any of the above.

## 8. Business Concepts

Concepts are grouped by the subject they describe. Every group carries its source. Classification under Constitution Article IV (Reality Knowledge vs Operational Knowledge) follows the rubric added to `STAGE_5_DISCOVERY_STANDARD.md` §6 under remediation B6.

### 8.1 Person — dimensions of a person's situation
*Source: `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §5; `PROJECT_OVERVIEW.md` Ch1.2; `GLOSSARY.md` Human Model Terms; client blueprint (nutrition).*

**Reality Knowledge**
- **Lifecycle Stage** — a developmental stage of life carrying characteristic dependencies, capabilities, vulnerabilities and expected outcomes. Explicitly *not* merely an age band. *(`GLOSSARY.md`; blueprint §5.2, which names infant, toddler, early childhood, school-age child, adolescent, young adult, adult, older adult, elderly.)*
- **Capability** — a person's ability to perform activities, contribute to household wellbeing, participate in society, or support others; represents strengths and assets rather than deficits. Blueprint §5.3 names five classes: physical, cognitive, educational, economic, caregiving.
- **Health Condition** — blueprint §5.4 distinguishes five kinds: acute conditions, chronic conditions, disabilities, mental health conditions, and nutritional conditions. Nutritional conditions are evidenced as carrying clinical staging (the blueprint names malnutrition, stunting, wasting, and SAM/MAM staging; the client blueprint independently uses SAM/MAM/normal classification derived from age, weight, height and MUAC).
- **Education and Skills** — `PROJECT_OVERVIEW.md` Ch1.2 names "education, skills, employment, and livelihood" as a foundational contextual dimension.
- **Livelihood and Employment** — same source; blueprint §9 names livelihood as a need category, implying the underlying dimension.
- **Economic Circumstance** — `PROJECT_OVERVIEW.md` Ch1.2, "economic circumstances and financial resilience."
- **Documentation and Legal Status** — blueprint §5.2 names documentation as part of identity; `registration-identity/05-business-rules.md` records that undocumented migrants and refugees may wholly lack state-issued documents, and `registration-identity/05c` names the State-Identity-vs-Humanitarian-Identity tension.
- **Displacement Status** — `PROJECT_OVERVIEW.md` Ch1.2, "significant life events, displacement, crises, or disasters."
- **Prior Assistance History** — `PROJECT_OVERVIEW.md` Ch1.2, "previous humanitarian assistance and intervention history."
- **Institutional Participation** — `PROJECT_OVERVIEW.md` Ch1.2, "government scheme participation and institutional interactions."

**Insufficient repository evidence — recorded, not filled:** no repository source enumerates which specific health conditions, capability levels, education levels or livelihood forms are recognised, nor what values any of these dimensions take. The *dimensions* are evidenced; their *value sets* are not, and are deliberately not invented here. (`ONTOLOGY_DESIGN.md` AR-7 in any case defers enumerated value sets to engineering.)

### 8.2 Family
*Source: `GLOSSARY.md` Human Model Terms; blueprint §6.*

**Reality Knowledge**
- **Family** — a social unit connected through kinship, caregiving, marriage, guardianship or other recognised relationships; distinct from Household; multiple families may exist within one household.
- **Kinship Relation** — blueprint §6 names parent, child, guardian, caregiver, spouse. `registration-identity/09-information-requirements.md` independently names spouse, child, sibling.
- **Dependency** — a relationship in which one person relies on another for care, support, resources, supervision, protection or decision-making; may be developmental, physical, financial, emotional or legal (`GLOSSARY.md`). Blueprint §6 evidences dependency as *typed and directional* and as *cascading*.
- **Responsibility** — who is responsible for income, caregiving, education, decision-making (blueprint §6).

### 8.3 Household
*Source: `GLOSSARY.md` Core Terms and Risk/Vulnerability Terms; blueprint §7; `registration-identity`.*

**Reality Knowledge**
- **Household** — the unit of people sharing living conditions and pooled resources; the primary context for assessing vulnerability and need.
- **Household Composition** — already named in `case-management/03-concepts.md`.
- **Housing Tenure** — ownership, rental, temporary shelter (blueprint §7).
- **Shelter Condition** — safe, damaged, flood-prone, roof leakage (blueprint §7).
- **Utilities Access** — water, electricity, sanitation (blueprint §7).
- **Household Resilience** — the composite household-level capacity to maintain essential functioning, adapt to disruption, and recover from adversity (`GLOSSARY.md`). Its components are owned by the Vulnerability, Risk and Protection domain; see Section 16.

**Operational Knowledge**
- **Head of Household** — a representational role assigned by convention and adjudicated by a Registrar, not a fact about reality. *(Classification reconciled under remediation B6; see `CONCEPT_OWNERSHIP.md` §8.)*

### 8.4 Community
*Source: blueprint §8; `GLOSSARY.md` Community Context Terms.*

**Reality Knowledge**
- **Community** — the village, neighbourhood or district context a household sits within.
- **Settlement Type** — the classification of a community's physical settlement pattern, e.g. rural, peri-urban, informal urban (`GLOSSARY.md`).
- **Service Access** — the presence, distance and quality of access to schools, hospitals, markets and employment opportunities (blueprint §8).
- **Local Organisation** — a persistent, community-native civic, economic or mutual-aid institution, distinct from formally registered external organisations (`GLOSSARY.md`). Independently corroborated as a real actor category by TD-01 Finding BD-TD01-005 (High confidence, ≥3 independent source families) — the only concept in this domain carrying external corroboration.
- **Livelihood Pattern** — the dominant, persistent community-level economic activity base; a macro-economic classification distinct from any household's own employment status (`GLOSSARY.md`).
- **Seasonal and Environmental Hazard** — flooding, rainy season, heat waves, drought, and the seasonal calendar (blueprint §8). Hazard classification itself is owned by the Vulnerability, Risk and Protection domain.

### 8.5 Life Events
*Source: `PROJECT_OVERVIEW.md` Ch1.2 and Ch4.1; `GLOSSARY.md` Trajectory and Lifecycle Transition; client blueprint Flow C. Closes FG-7.*

**Reality Knowledge**
- **Life Event** — an occurrence in a person's life that changes their humanitarian reality. `PROJECT_OVERVIEW.md` Ch1.2 requires the foundation to preserve "what events led to the current situation"; Ch4.1's worked example turns on displacement, a chronic condition, interrupted schooling, prior assistance, and housing loss.
- **Trajectory** — the pattern by which a situation developed over time: structural (chronic, pre-existing), crisis_triggered (caused by an event), progressive (gradually worsening), or acute (sudden onset) (`GLOSSARY.md`).

Life events evidenced in the repository, by source:
| Life event | Source |
|---|---|
| Displacement | `PROJECT_OVERVIEW.md` Ch1.2, Ch4.1 |
| Housing loss | `PROJECT_OVERVIEW.md` Ch4.1 |
| Onset of a chronic condition | `PROJECT_OVERVIEW.md` Ch4.1 |
| Interruption of schooling | `PROJECT_OVERVIEW.md` Ch4.1; blueprint §5.1 ("a child in school at first contact has dropped out by the second") |
| Birth | `registration-identity/06-business-events.md` ("Household Updated: composition changes (e.g., birth, separation)") |
| Death | `registration-identity/07-business-lifecycles.md` (Archived / Deceased); `registration-identity/10-open-questions.md` (death of Head of Household) |
| Marriage | `registration-identity/04b-knowledge-patterns.md` |
| Divorce / separation | `registration-identity/04b`, `06-business-events.md` (Household Split) |
| Injury | blueprint §11 ("loss of income after injury") |
| Loss of income | blueprint §11 |
| Gaining employment | Client blueprint Flow C ("father has got a job"), which drives a need revision |
| Onset of an acute medical need | Client blueprint Flow B |

**Insufficient repository evidence:** return, resettlement, eviction and disaster exposure are plausible life events not evidenced in any repository source, and are deliberately **not** added.

## 9. Business Relationships

Stated in natural language, per the Discovery Standard. Temporal validity and plurality are stated where the repository evidences them and marked unevidenced where it does not — `ONTOLOGY_DESIGN.md` §2.3 requires both to be explicit, and honest gaps are more useful to that layer than guesses.

- A **Person** is a member of a **Household**. *(Temporal: membership begins and ends — `registration-identity/04b` "Households are fluid temporal structures; Beneficiaries are permanent." Plurality: **unevidenced** — whether a person may hold concurrent membership in two households is not answered anywhere in the repository.)*
- A **Person** belongs to a **Family**. *(Plurality: `GLOSSARY.md` states multiple families may exist within a household; whether a person belongs to more than one family is unevidenced.)*
- A **Family** is distinct from, and may be contained within, a **Household**. *(Source: `GLOSSARY.md`.)*
- A **Household** exists within a **Community**. *(Plurality and temporal validity: unevidenced.)*
- A **Person** depends on a **Person**, for a stated kind of support. *(Typed and directional — blueprint §6. Plurality: many-to-many is implied by the cascade example but not stated.)*
- A **Person** carries responsibility for a **Household function** (income, caregiving, education, decision-making). *(Source: blueprint §6.)*
- A **Household** designates a **Head of Household**. *(Plurality: `registration-identity/08` §3 records disputes over headship but does not state whether more than one head is possible.)*
- A **Life Event** changes a **Person's** situation, a **Household's** composition, or both. *(Source: `PROJECT_OVERVIEW.md` Ch1.2; client blueprint Flow C.)*
- A **Capability** of a **Person** offsets a **Dependency** in a **Household**. *(Source: blueprint §5.3 read with §7's role-substitution concept; relationship is inferred from two internal sources and marked **Tier C inference**, not a Finding.)*

## 10. Business Events

Life events are catalogued in Section 8.5. The business events by which this domain's knowledge changes are:

- **Household Composition Recorded** — the membership of a household is established.
- **Household Composition Changed** — a member joins or leaves. *(Already named as "Household Updated" in `registration-identity/06-business-events.md`; referenced, not duplicated.)*
- **Household Split** / **Household Formed** / **Household Dissolved** — *(Already named in `registration-identity/06` and `07`; referenced, not duplicated.)*
- **Dependency Recorded** / **Dependency Changed**.
- **Life Event Recorded** — an occurrence in a person's life is entered into the foundation.
- **Situation Dimension Observed** — a dimension of a person's or household's situation is observed or re-observed.

## 11. Knowledge Patterns

- **The Cascade Pattern.** A condition affecting one person propagates to those who depend on them: *Condition of Person A → Dependency (B depends on A) → altered situation of Person B.* Blueprint §6 states it directly: "a mother's risk is her infant's risk."
- **The Longitudinal Revision Pattern.** *Life Event → revises Situation Dimension → revises Need.* `PROJECT_OVERVIEW.md` Ch1.2 requires preservation of "how circumstances have changed, what events led to the current situation"; the client blueprint Flow C is a worked instance (employment event → food need reduced and given an expiry).
- **Household Fluidity.** *(Already named in `registration-identity/04b-knowledge-patterns.md` and `case-management/04b`; referenced, not duplicated.)* Individuals merge into and split from households dynamically; the household is a temporal container, the person is permanent.
- **The Equivalence Fallacy.** Two households with identical recorded facts are not equally vulnerable, because their resilience, dependency structure and community context differ. `PROJECT_OVERVIEW.md` Ch1.2: "Two families may appear identical on paper while living in completely different realities." Blueprint §7 restates it for resilience specifically.

## 12. Policies

- **Universal.** A person exists independently of any household grouping. *(Source: `registration-identity/12-domain-invariants.md`, "The Primacy of the Beneficiary"; `FOUNDATION_CONCEPTS.md` §1.)*
- **Universal.** A person's core existence is immutable; their attributes are mutable. *(Source: `registration-identity/12-domain-invariants.md`.)*
- **Universal.** People are represented as persons within evolving networks of relationships, history and context — never reduced to a current deficiency or a demographic category. *(Source: `ONTOLOGY_DESIGN.md` Pillar P5, itself derived from `PROJECT_OVERVIEW.md` Ch1.3 and Ch8.2.)*
- **Regional / Cultural.** The definition of a household varies by cultural context. *(Source: `case-management/05-business-rules.md`; `registration-identity/05-business-rules.md`; `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch9.)*

## 13. Constraints

- **Cultural.** Household definitions vary widely — polygamous families, extended intergenerational living, unaccompanied minors living with neighbours. *(Source: `registration-identity/05-business-rules.md`.)*
- **Cultural.** In many cultures a person's primary name changes on life events such as becoming a parent. *(Source: `registration-identity/05b-exceptions.md`.)*
- **Cultural.** Individual consent may be culturally superseded by household consent. *(Source: `TERMINOLOGY_HARMONIZATION.md` §7, recorded there as an open question.)*
- **Ethical.** Collection must be proportionate; `PROJECT_OVERVIEW.md` Ch1.2 states the purpose is "enough contextual understanding for humanitarian decisions to be made responsibly… not to create an exhaustive profile of a person." This is a binding constraint on the breadth of this domain.
- **Operational.** Living arrangements are highly fluid during active conflict and displacement. *(Source: `registration-identity/08-decision-points.md` §3.)*

## 14. Terminology

**Preferred terms:** Person (the enduring human being); Household (shared living and pooled resources); Family (kinship and caregiving unit); Dependency (typed, directional reliance); Capability (ability and asset, not deficit).

**Ambiguous terminology already resolved elsewhere, referenced not restated:** *Family vs. Household* (`registration-identity/13-business-language.md`); *Beneficiary vs. Individual* (`TERMINOLOGY_HARMONIZATION.md` §5); *Capacity → Capability vs. Scale* (`TERMINOLOGY_HARMONIZATION.md` §4.5 — note that harmonization concerns organisational capacity; **person-level Capability in this domain is a different concept sharing the word**, and this collision is recorded here as new and unresolved).

## 15. Exceptions

- **Unaccompanied minors.** A person lacking a legal guardian, requiring representation without standard household attribution. *(Source: `registration-identity/05b-exceptions.md`.)*
- **Household headship vacancy.** The Head of Household dies and a minor assumes responsibility. *(Source: `registration-identity/10-open-questions.md`, recorded there as unanswered.)*
- **Person as both dependant and provider.** Evidenced implicitly by blueprint §6's caregiving-capability class combined with its dependency model; not treated explicitly anywhere.

## 16. Domain Dependencies

**Knowledge consumed from:**
- **Registration & Identity:** the verified identity of the person this domain describes, and the fact that two encounters concern the same person.

**Knowledge produced for:**
- **Vulnerability, Risk and Protection:** the dimensions, dependencies and household structure from which vulnerability and resilience are assessed.
- **Case Management:** the situational context against which needs are identified and support planned.
- **Programme Management:** aggregated population characteristics (consumed as aggregate only — `programme-management/12-domain-invariants.md` forbids it from evaluating individual households).
- **Accountability & Evaluation:** the baseline human situation against which outcome change is measured.

**Boundary reconciliation with Registration & Identity.** `registration-identity/02-boundaries.md` currently claims ownership of "Household composition and membership lifecycles." Under remediation B11 that claim is refined, not removed: Registration & Identity owns the *recording and adjudication* of household membership as part of registry integrity; this domain owns the *household as a social unit* — its resilience, its internal dependencies, its housing and utilities, and its community context. Recorded in `CONCEPT_OWNERSHIP.md` §8.

## 17. Business Tensions

- **Depth of understanding vs. proportionate collection.** `PROJECT_OVERVIEW.md` Ch1.2 demands multidimensional understanding and in the same paragraph forbids exhaustive profiling. Every dimension in Section 8 sits inside this tension.
- **Person as sovereign vs. household as the unit of assistance.** *(Already named in `registration-identity/05c-business-tensions.md` as "Beneficiary Sovereignty vs Household Efficiency"; referenced, not duplicated.)*
- **Stable representation vs. fluid reality.** Households split and merge continuously while the foundation must retain a re-identifiable account of them.
- **Capability framing vs. deficit framing.** `GLOSSARY.md` defines Capability as strengths "rather than deficits," while the operational domains reason predominantly in vulnerabilities and needs. `TERMINOLOGY_HARMONIZATION.md` §7 records the unresolved question of whether "Vulnerability" should be reframed as "Resilience Gap."

## 18. Discovery Evidence

### Established Facts
*(Facts asserted by more than one independent repository source.)*
- A person is a persistent entity, not a per-case record. *(Blueprint §5.1; `registration-identity/12`; `FOUNDATION_CONCEPTS.md` §1.)*
- Households are fluid temporal containers; persons are permanent. *(`registration-identity/04b`; `case-management/04b`; blueprint §7.)*
- Family and Household are distinct concepts. *(`GLOSSARY.md`; `registration-identity/13`.)*
- Lifecycle stage is a developmental reality carrying characteristic needs, not an age band. *(`GLOSSARY.md`; blueprint §5.2.)*
- Vulnerability in one household member propagates to dependants. *(Blueprint §6; corroborated in shape by `case-management/04-relationships.md`, "A Caregiver represents a Dependent Individual.")*
- Community-native local organisations are legitimate actors. *(TD-01 BD-TD01-005, High confidence, ≥3 external source families — the only externally corroborated statement in this domain.)*

### Reasonable Assumptions
- The five capability classes (physical, cognitive, educational, economic, caregiving) and five health-condition kinds (acute, chronic, disability, mental health, nutritional) in blueprint §§5.3–5.4 are treated as a plausible starting decomposition, on the strength of a single internal source. **They are not Findings.** Recorded as AR-015.
- The nine lifecycle stages named in blueprint §5.2 are treated similarly. Recorded as AR-015.

### Open Questions
1. May a person hold concurrent membership in more than one household?
2. How is a household re-identified across a split or a merge — which resulting household, if any, is the continuation of the original? *(`SHARED_CONCEPT_CATALOG.md` §1 asks this and does not answer it; `VALIDATION/FINDINGS.md` REC-01 recommends assigning an owner. Ownership is assigned by this document; the answer still requires evidence.)*
3. How is a dependency established in practice, and by whom?
4. May a household have more than one Head of Household?
5. What value sets do the dimensions in Section 8.1 actually take in practice?
6. Does person-level Capability collide materially with organisational Capability as harmonized in `TERMINOLOGY_HARMONIZATION.md` §4.5?

### Knowledge Gaps
- **Tier A, B and D are entirely absent for this domain.** No practitioner, sector-standard or literature evidence has been gathered for any statement above except BD-TD01-005. This is the dominant limitation and is the reason this domain cannot be frozen.
- No repository source enumerates the values of any dimension in Section 8.1.
- Decision content (Section 6) is materially thinner than in the seven original domains.

## 19. Ontology Readiness

Conceptual clusters that appear stable enough to inform later modelling. **This section identifies clusters; it does not model them.**

- **The Person–Family–Household–Community nesting**, with the person persisting and the social units being temporal containers.
- **The typed, directional dependency structure** and its cascade behaviour.
- **The dimensional description of a situation** — the substrate the Facets layer of `ONTOLOGY_DESIGN.md` §2.1 requires, which was previously absent from the canonical chain.
- **Life event as the causal unit of change**, linking an occurrence to a revised situation.

## 20. Domain Completion Assessment

**❌ REQUIRES FURTHER DISCOVERY**

**Justification.** This domain closes the *structural* gap identified as FG-1, FG-2 and FG-7: the canonical chain now contains a discovered account of person, family, household, community and life event, with the dimensional substrate the Facets layer requires, and with a named owner. That was the accepted finding, and it is addressed.

It does not close the *evidentiary* gap. Every statement here rests on Tier C internal sources, one of which was previously archived. One statement carries external corroboration. No practitioner has validated any of it. Marking this domain `READY FOR FREEZE` would repeat precisely the failure the Constitution prohibits in Article XVI — a completion claim outrunning its content.

The honest state is: **sufficient for ontology design to proceed against, explicitly flagged as unvalidated, and blocked from freeze on remediation B13.**
