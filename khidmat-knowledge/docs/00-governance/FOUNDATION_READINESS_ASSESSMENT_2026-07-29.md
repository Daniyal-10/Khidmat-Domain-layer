---
id: DOC-GOV-REVIEW-001
title: Independent Foundation Readiness Assessment
version: 1.0
status: Independent Review — non-normative, advisory to the Package A gate
owner: Enterprise / Ontology Architecture Review
reviewers: Project Lead, Domain Approval Authority
created: 2026-07-29
last_updated: 2026-07-29
depends_on: docs/00-governance/PROJECT_OVERVIEW.md (v1.0), docs/00-governance/CONSTITUTION.md (v1.0), docs/00-governance/KHIDMAT_FOUNDATION_PIPELINE.md, docs/01-methodology/ONTOLOGY_DESIGN.md (v1.0.0)
scope_reviewed: entire repository (212 files) plus the client Direct Relief blueprint
consumed_by: Package A approval decision; Stage 5 remediation; Stage 6 Ontology Design Prerequisites
layer: 00-governance
domain: Foundation
tags: [review, readiness, ontology-first, foundation-gaps, package-a]
decision: FOUNDATION INCOMPLETE
---

> **Status note.** This is an independent architectural review, not a normative document.
> It originates no philosophy, principle, or mandate (Constitution Article XV) and binds
> nothing. It is advisory input to the Domain Approval Authority's Package A decision
> under Article XVI. Every prior review, certification, and remediation report in this
> repository was deliberately treated as an untrusted assertion; all conclusions below are
> re-derived from primary repository content.

# Khidmat AI — Independent Foundation Readiness Assessment

**Reviewer role:** Chief Enterprise Architect / Chief Ontology Architect / Humanitarian Knowledge Architect / Project Lead
**Date:** 2026-07-29
**Scope reviewed:** entire `khidmat-knowledge` repository (212 files), plus the client's `direct-relief-architecture.html` blueprint
**Question answered:** *Has the repository produced the complete business-knowledge foundation required before Ontology Design begins?*
**Method:** every prior review, certification and remediation report was treated as an untrusted assertion. Conclusions below are re-derived from primary repository content.

---

## 1. Executive Summary

The repository is a serious, unusually disciplined piece of knowledge engineering. Its governance layer is genuinely strong, its ontology-design *framework* (`ONTOLOGY_DESIGN.md`) is one of the better ontology-first method documents I have read, and its Stage 5 discovery captures the **operational machinery** of humanitarian assistance — events, states, decisions, handoffs, exceptions and tensions — with real fidelity.

It does not, however, capture **humanitarian reality itself**.

The central finding of this review is structural, not cosmetic:

> **The repository has discovered how humanitarian organisations operate. It has not discovered what a human being in humanitarian need actually *is*.**

Across all seven Stage 5 domains, the entire vocabulary describing a person's lived reality amounts to four lines of text (`case-management/04-relationships.md:5,7`, `registration-identity/03-concepts.md:7`, and one NGO-capacity reference). There is no health, no nutrition, no capability, no dependency structure, no livelihood, no education, no income, no shelter condition, no settlement context anywhere in the canonical discovery corpus. Yet `PROJECT_OVERVIEW.md` Ch 1.2 makes exactly these dimensions the definition of the problem the project exists to solve, and explicitly delegates their refinement to "later foundational documents such as the Humanitarian Business Reference Model and the Ontology Design." The HBRM (Stage 3, Frozen) never performs that refinement — its nine chapters are entirely about actors, tensions, lifecycles, capabilities, value streams, intervention categories, objectives, governance and boundary conditions.

That content *does* exist in the repository — in `GLOSSARY.md` (~120 normative terms) and in `98-archive/execution_cleanup/BUSINESS_ARCHITECTURE_BLUEPRINT.md` §§5–13 (Human, Family, Household, Community, Needs, Vulnerability, Risk, Support, Outcome models). But the glossary asserts it with **no discovery evidence and no provenance**, and the archived blueprint is explicitly deprecated, self-flagged as "should not be treated as frozen or authoritative," and expressly excluded as a binding input by `ONTOLOGY_DESIGN.md`'s own preamble.

So the repository holds two disconnected strata of knowledge:

| Stratum | Content | Evidence | Canonical status |
|---|---|---|---|
| **Legacy / deep** | Person, family, household, community, capability, dependency, health, risk composition, resilience, giving, verification operations, needs assessment | None traceable | Deprecated (archive) or unevidenced (glossary) |
| **Current / shallow** | Seven operational domains: registration, case, programme, logistics, accountability, coordination, partners | Partly cited (TD-01–06), uncited (02-discovery) | Canonical |

**The canonical chain contains only the shallow stratum.** An ontology architect starting tomorrow and obeying this project's own evidence rules would find the Entities, Relationships, Constraints, States, Events, Coordination Patterns and Governance layers substantially derivable — and the **Facets** layer, which is where a person's multidimensional reality lives, essentially empty.

Compounding this, the single most load-bearing test in the entire methodology — the Reality Knowledge / Operational Knowledge boundary (Constitution Art. IV, Pillar P1, Rule AR-1) — is applied **inconsistently and contradictorily** across the seven domains. `Consent` is Reality Knowledge in one domain and Operational Knowledge in another. `Programme` is classified Operational Knowledge despite a ratified Human Owner decision (CL-001) declaring it "a distinct humanitarian business concept." A primitive set derived from a corpus that disagrees with itself about which concepts are even admissible will be wrong, and the primitive set is *closed* once ratified.

Finally, the formal gates are not passed. The repository holds **two mutually contradictory certifications** for the same body of work (`03-cross-domain/STAGE5_CERTIFICATION.md`: "CERTIFIED READY… cleared to commence Stage 6"; `03-cross-domain/VALIDATION/CERTIFICATION.md`: "NOT CERTIFIED"). The remediation report says the layer is "eligible for an independent re-validation" — which never occurred. Constitution Article XVI requires Package A approval by the Domain Approval Authority before ontology design begins; no such approval exists, and the "decision ledger" that Articles XVII and XIX require does not exist as an artifact.

**Verdict: FOUNDATION INCOMPLETE** — but narrowly and closably so. My estimate is that roughly 70% of the required foundation is present, and that the remaining 30% is *mostly recovery and validation of knowledge the project already produced once*, not fresh discovery. The specific work is enumerated in §10. I judge it 4–6 weeks of focused effort, not a restart.

---

## 2. Assessment Against the Khidmat Foundation Pipeline

`KHIDMAT_FOUNDATION_PIPELINE.md` marks Stages 1–4 ✅ Done, Stage 5 🟡 Active, Stage 6 🔴 Blocked. Assessed against the pipeline's own stated stage contents:

| Stage | Claimed | Actual | Assessment |
|---|---|---|---|
| **1. Project Overview** | ✅ Done | Present, v1.0, coherent, genuinely load-bearing | **SUPPORTED** |
| **2. Business Master Plan** | ✅ Done (Frozen) | Authored, covers strategy, phasing, structure, sustainability, risk, measures | **SUPPORTED** — with a scope contradiction (see §7) |
| **3. HBRM** | ✅ Done (Frozen) | Authored. But the pipeline says Stage 3 exists to make cognition and coordination "stable enough to build the ontology's cognition and coordination-pattern layers on top of." HBRM Ch 4 restates the Overview's seven capabilities; it adds no epistemic or coordination substance beyond them, and adds **nothing** on the person-reality dimensions the Overview delegated to it | **PARTIALLY SUPPORTED** |
| **4. Business Architecture** | ✅ Done (Frozen) | The pipeline's Stage 4 action list required: review the blueprint section-by-section, flag each section keep/revise/replace, and *separate out content that belongs to HBRM*. **None of this was done.** The canonical `BUSINESS_ARCHITECTURE.md` (124 lines) does not carry forward §§5–13 of the blueprint; that material was archived, not reconciled. The pipeline's own precondition for marking Stage 4 done was not met | **UNSUPPORTED as executed** |
| **5. Domain Discovery** | 🟡 Active | Seven domains, 20-section standard, 20 decision points, ~70 events. Real substance. But three domains still record `Evidence: Pending Discovery` in STATUS while simultaneously being marked Frozen/Ready; every domain records `Client Validation: Pending`; and none carries a single source citation | **PARTIALLY SUPPORTED** |
| **6. Ontology Design Prerequisites** | 🔴 Blocked | **This is the decisive finding.** Stage 6.1 requires working definitions for all six Stable Core elements — Identity, Relationships, Evidence, Uncertainty, Temporal change, Context — plus a cross-check that every Stage 5 qualified concept can be described in those terms, plus a "Stable Core Definitions" note. `FOUNDATION_CONCEPTS.md` is the nearest artifact and defines four *different* things: Beneficiary, Organisation, Consent, Evidence. **Four of six stable-core elements — Relationships, Uncertainty, Temporal change, Context — have no working definition anywhere in the repository.** The cross-check was never run; the note does not exist | **UNSUPPORTED** |

The pipeline's own Stage 6 gate has therefore not merely been "not started" — it has been silently skipped by a Stage 5 certification that declared readiness for Stage 6 without performing Stage 6's prerequisite work. That Uncertainty and Temporal Change in particular have no working definition maps directly onto the Project Lead's warning: these are the two stable-core elements the Cognition layer is built from.

---

## 3. Assessment Against the Project Lead's Ontology-First Methodology

The Project Lead's diagnosis was: *"What you have done is ontology engineering and not ontology-first design. You went bottom-up and schema-first."*

**Where the repository has genuinely corrected course.** `ONTOLOGY_DESIGN.md` v1.0 is a real fix. It defines primitives as discovered-by-abstraction rather than imported from an upper ontology (§1.2), names all eight required layers in the Project Lead's own order, gives Cognition the fullest treatment of any layer ("This is the layer without which the architecture will fail" — §2.7), makes Coordination Patterns last-designed and highest-scrutiny (§2.8), translates the five principles into seven testable Pillars (§3), states ten Architecture Rules including a promotion test designed for inter-author convergence (AR-2) and a design-purity rule that bans schema leakage (AR-7), and explicitly disqualifies prior engineering artifacts as binding inputs. `docs/98-archive/README.md` confirms the schema-first `engineering-layer/` was deleted. This is ontology-first method, properly stated. Credit where due.

**Where the schema-first reflex has survived, undetected.** Three concrete instances:

**(a) The domain decomposition reproduces the NGO software module list.** `BUSINESS_ARCHITECTURE.md` §2 organises the business into Case Management, Programme Management, Resource & Logistics, Accountability & Evaluation, Cross-Organisational Coordination; `02-discovery/` adds Registration & Identity and Organisation & Partner Management. Compare `PROJECT_OVERVIEW.md` Ch 6.1, which names exactly this as the failure mode to avoid: *"not organized around Organisational departments, software modules, or the functional categories common to existing NGO systems (registration, case management, donation management). Organizing this way would recreate the exact fragmentation Chapter 1 identified."* Constitution Article VI codifies the prohibition. `ONTOLOGY_DESIGN.md` AR-8 repeats it for the ontology.

A fair counter-argument exists: Article VI targets how *capabilities* are organised, and `BUSINESS_ARCHITECTURE.md` §6 does derive its capability set from the cognitive lifecycle. But the practical consequence is unaffected. Because Stage 5 discovery is scoped *per department*, every concept list, relationship list, event list and decision list in the repository is cut along departmental lines. The ontology will have to re-cut all of it along reality lines — and when it does, it will discover that the reality side is thin, precisely because department-shaped discovery never asked reality-shaped questions. Nobody asked "what is a household, and how does it change?" because no department owned households. The result: `CONCEPT_OWNERSHIP.md` has no owner for **Household**, no owner for **Family**, and §7 explicitly records Community as unresolved — *"Where does the concept of a 'Community' live?"* Three of the four social units in the Overview's own model (individual / family / household / community) are unowned.

**(b) The Stage 5 certification is written in schema-first language.** `STAGE5_CERTIFICATION.md` §2.6 states: *"Stage 6 Ontology Design requires stable classes, properties, and relationships. The current discovery artifacts provide exactly this. The 'Reality Knowledge' and 'Operational Knowledge' concepts within each domain directly map to ontological classes. The 'Business Relationships' explicitly define the object properties."* This is exactly the inversion the Project Lead diagnosed, written into a certifying document. Reality/Operational is an *admission test* (Article IV) — a filter deciding whether a concept may enter the foundation at all — not a class hierarchy. Treating it as one, and treating natural-language relationship sentences as object properties, is bottom-up schema derivation. The validation layer caught the same species of error in `SHARED_CONCEPT_CATALOG.md` (finding CRIT-01, "Foundation:Identity as a class") but never audited the certification itself.

**(c) The eight layers are unevenly supplied by the discovery.** Discovery produced excellent Events, States, Constraints and Coordination-Pattern material — the layers that describe *process*. It produced almost nothing for Facets — the layer that describes *a person*. That asymmetry is the signature of process-first discovery, and it is why the Project Lead's specific warning about Cognition generalises: the same gap exists one layer over, in Facets, and nobody has flagged it.

**Verdict on §3:** the *method* is now ontology-first. The *inputs* the method will consume are still organisation-first. Fixing the method document did not retroactively re-cut the discovery.

---

## 4. Assessment of the Repository as an Integrated Knowledge Foundation

Reading the repository as a single body of knowledge rather than as documents:

**What the repository knows well.** How aid organisations are structured and how they fail each other; how a case moves and loops; who decides what, on what evidence, with what override and what uncertainty; how organisations establish, suspend and lose trust in one another; how consent gates cross-boundary sharing and how revocation is supposed to cascade; how a claim becomes evidence becomes a decision; how goods and cash move under custody; why accountability must sit structurally apart from execution; and — unusually well — the *tensions* that make all of the above hard. The 20 decision points across the seven domains are the strongest single asset: each names its evidence, policies, constraints, preconditions, alternative outcomes, escalations, review triggers, appeal mechanisms, human override and residual uncertainty. That is a very good substrate for a Cognition layer.

**What the repository does not know.** What a person is. What a household is beyond "a grouping that changes." What a family is (the glossary distinguishes it from household; no discovery does). What a community is or who owns it. What makes someone vulnerable, in substance. What a need actually consists of, at case altitude — its categories, its severity, its relationships to other needs. What "improved" means. Where any of this is happening (no deployment geography, anywhere, per AR-002). Who funds it, and under what religiously or legally restricted terms.

**The integrity problem that connects them.** The repository's own validation layer established the correct standard — *"If an architectural boundary 'makes sense' but is not explicitly supported by discovery, it is marked as unsupported"* (`VALIDATION/README.md`). Applied consistently, that standard invalidates far more than the four findings it produced. `GLOSSARY.md` is `status: Normative`, v1.0, and defines roughly 120 terms — Absorptive Capacity, Role Substitution Capacity, Risk Composition, Protective Factor, Livelihood Diversity, Treatment Continuity Active, Hazard Category, Exposure, Risk Horizon, Compound Risk, Intervention Readiness, Intervention Objective Category, Protection Indicator, Finding Consensus, Chain of Custody, Zakat-Eligible Category, the seven Islamic Giving forms, and more. **Not one of these appears in any Stage 5 discovery document.** They are normative assertions about humanitarian reality with no discoverable evidence chain, in a repository whose Constitution Article V states that an assertion is not evidence merely because it has been recorded, and whose `ONTOLOGY_DESIGN.md` §6 applies that rule reflexively to the ontology's own design decisions including those sourced from frozen artifacts.

This is the repository's deepest structural problem: **its richest knowledge is its least evidenced, and its best-evidenced knowledge is its shallowest.**

---

## 5. Assessment of Every Ontology Prerequisite

### 5.1 Domain Primitives

**Support status: PARTIALLY SUPPORTED**

**Repository evidence.** `PROJECT_OVERVIEW.md` Ch 5.1 names the predicted stabilisation point (identity, relationships, evidence, uncertainty, temporal change, context). `ONTOLOGY_DESIGN.md` §1.2 gives a sound four-step derivation procedure. The concept corpus available for abstraction is large enough: ~150 named concepts across `02-discovery/*/03-concepts.md`, `GLOSSARY.md`, `FOUNDATION_CONCEPTS.md` and `SHARED_CONCEPT_CATALOG.md`.

**Remaining gaps.** Two, both material.

First, §1.2 step 4 requires a coverage test: *"Every currently validated business concept must be classifiable somewhere in the candidate set without forced fit."* Coverage tested against a corpus missing the person-reality stratum will validate a primitive set that has never been exercised against health, capability, dependency, livelihood, shelter or community-context concepts. Since §1.4 makes the primitive set **closed** — extendable only through Tier 3 foundational governance — deriving it now guarantees a foundational amendment later. This is the strongest single argument for closing the Facets gap *before* rather than *during* ontology design.

Second, step 3 requires each candidate to pass the Knowledge Foundation Boundary (Article IV). The repository applies that test inconsistently. Documented contradictions:

| Concept | Classification A | Classification B | Conflict |
|---|---|---|---|
| Consent | Reality Knowledge (`case-management/03`) | "Foundational Consent" = Operational Knowledge (`registration-identity/03`) | Also declared a cross-domain foundational concept (`FOUNDATION_CONCEPTS.md` §3) — three-way |
| Programme | Operational Knowledge (`programme-management/03`) | "a distinct humanitarian business concept… shall remain independent throughout the Khidmat Foundation and future Ontology Design" (CL-001, **ratified by the Human Owner**) | Discovery contradicts a ratified governance decision |
| Grant / Budget / Eligibility Rule | Operational Knowledge (`programme-management/03`) | Glossary Donor & Resource / Programmes Terms; `CONCEPT_OWNERSHIP.md` §3.2 canonical owned concepts | Eligibility rules gate who receives aid — self-evidently decision-changing under Art. IV |
| Head of Household | Operational Knowledge (`registration-identity/03`) | Subject of a full Business Decision (`registration-identity/08` §3) with cultural constraints | Culturally real, decision-bearing |
| Delivery Event | Reality Knowledge (`case-management/03`) | Delivery Confirmation = Operational (`resource-logistics/03`) | Same phenomenon, opposite sides of the boundary |
| Referral | Operational Knowledge (`case-management/03`) | Core produced concept of Coordination; Glossary Case Management Term | Cross-organisational continuity is Reality Knowledge by Ch 6.1 |

**Would an ontology architect have to invent business reality?** Not the primitives themselves — but they would have to **re-adjudicate the admission test across the whole corpus** before deriving anything, because the corpus's own classifications cannot be relied upon. That re-adjudication is business-architecture work, not ontology work, and it is a prerequisite.

---

### 5.2 Layer — Facets

**Support status: UNSUPPORTED**

**Repository evidence.** `PROJECT_OVERVIEW.md` Ch 1.2 lists thirteen contextual dimensions and then states plainly: *"This list is not exhaustive. It establishes the conceptual need for multidimensional understanding, not the complete conceptual model — these dimensions are expected to be refined and expanded in later foundational documents such as the Humanitarian Business Reference Model and the Ontology Design."* The HBRM does not refine them. `BUSINESS_ARCHITECTURE.md` does not. No Stage 5 domain does.

Searched exhaustively across `02-discovery/*/03-concepts.md` and `*/09-information-requirements.md` for the vocabulary of lived reality — lifecycle stage, capability, dependency, caregiving, health, nutrition, disability, livelihood, shelter, settlement, education, income, employment. **Total yield: four lines**, of which one refers to NGO technical capacity rather than to a person:

- `case-management/04-relationships.md:5` — "A **Caregiver** represents a **Dependent Individual**."
- `case-management/04-relationships.md:7` — Engagement Stage vs Human Development Stage
- `registration-identity/03-concepts.md:7` — "Dependent"
- `organisation-partner-management/03-concepts.md:5` — "Technical Capacity / Sector Expertise (e.g., WASH, Health)" *(about organisations)*

`registration-identity/09-information-requirements.md` gives biographical, biometric, contact and kinship data — a registry record. `case-management/09-information-requirements.md` gives identity & context, claims, evidence, rules & budgets, fulfilment status — a workflow record. Neither describes a person.

**Why this must exist before ontology design.** `ONTOLOGY_DESIGN.md` §2.1 defines a Facet as *"an independently varying dimension of something else"* and gives its rationale directly from Ch 1.2: *"two families identical on paper may live in completely different realities."* The Facets layer exists precisely to carry the multidimensional reality of a person. Facets is one of the two deliverables of Package B. You cannot design the dimensions of a person's reality without first discovering which dimensions materially change humanitarian understanding — that determination is the Article IV admission test applied to reality, and it is business discovery by definition, not modelling.

**Why it cannot be derived.** The content exists in exactly two places, both disqualified:

1. `98-archive/execution_cleanup/BUSINESS_ARCHITECTURE_BLUEPRINT.md` §§5–13 (Human Model with lifecycle stages and five capability classes; Family Model with typed dependency and responsibility; Household Model with housing, utilities, shelter condition and four resilience capacities; Community Model with settlement, services, local fabric, seasonal risk; Needs Model with seven categories and need dynamics; Vulnerability Model; Risk Model with horizon/trend/severity/compounding; Support Model; Outcome Model). This document self-declares *"Should not be treated as frozen or authoritative until reconciled,"* sits in a directory whose README defines it as "Deprecated normative documents," and is explicitly excluded by `ONTOLOGY_DESIGN.md`'s preamble: prior artifacts *"are not binding inputs to ontology design… every concept they name must re-enter through the discovery, evidence, and promotion discipline defined here, exactly as if it had never been modeled."*

2. `GLOSSARY.md` Human Model Terms, Risk and Vulnerability Terms, Community Context Terms — normative, but with zero provenance and zero corroboration in any discovery document, failing `ONTOLOGY_DESIGN.md` §6's evidence test.

An architect obeying the project's own rules has nothing. An architect breaking them inherits a decade-old draft nobody has validated. Under AR-9 ("Flag, don't guess") the correct action in both cases is to stop and escalate — which is what this assessment does.

**Would business reality have to be invented?** In part, yes. Recovering the archived material is validation, not invention. But deciding *which* health conditions, capabilities, dependency types, livelihood forms, shelter conditions and community factors materially change humanitarian understanding — and doing so for the actual population Khidmat will serve — is discovery of business reality that no repository artifact supports.

---

### 5.3 Layer — Entities

**Support status: SUPPORTED (with one caveat)**

**Repository evidence.** Entity candidates with independent identity are well attested: Individual/Beneficiary and Household (`FOUNDATION_CONCEPTS.md` §1; `registration-identity` throughout), Organisation (`FOUNDATION_CONCEPTS.md` §2; `organisation-partner-management` in full), Programme (ratified distinct by CL-001), Case, Support Plan, Need, Claim, Evidence, Identity Profile, Grievance, Partnership/Consortium, Intervention Offering, Delivery Event, Inventory Item, Vendor/FSP, Coordination Cluster, External Referral.

Identity criteria — the obligation §2.2 imposes — are partly supplied and unusually well grounded for the hardest case: `registration-identity/08` Decision 2 (Duplicate Resolution) establishes that algorithmic matching produces false positives (twins, identical naming conventions), that all merges require mandatory human review, and that merges are contested and sometimes wrong. `registration-identity/12-domain-invariants.md` gives "Identity is Immutable, Attributes are Mutable" and "The Primacy of the Beneficiary" (a person exists independently of a household). `SHARED_CONCEPT_CATALOG.md` §1 correctly identifies that Identity must be decoupled from the roles it plays.

**Remaining gaps.** Household identity criteria are the weak point. The repository repeatedly asserts that households split, merge and dissolve (`registration-identity/04b`, `07`, `case-management/04b`, `05b`) and treats it as an open question — `SHARED_CONCEPT_CATALOG.md` §1: *"How does the system handle an Identity that splits?"*; `VALIDATION/FINDINGS.md` REC-01 recommends assigning someone the job of answering it. Nobody has. Household is also unowned in `CONCEPT_OWNERSHIP.md`. Family is absent entirely from discovery despite the glossary distinguishing it from Household.

**Invention required?** For Person, Organisation, Case, Programme and the operational entities: no. For Household re-identification across splits/merges, and for Family as a distinct entity: yes, business reality must still be established.

---

### 5.4 Layer — Relationships

**Support status: PARTIALLY SUPPORTED**

**Repository evidence.** Every domain has an `04-relationships.md`; roughly 45 relationships are named in business language across the seven. `SHARED_CONCEPT_CATALOG.md`, `CROSS_DOMAIN_DEPENDENCIES.md` and `KNOWLEDGE_TRANSFORMATION_PATTERNS.md` add cross-domain connective tissue. `GLOSSARY.md` supplies one genuinely sophisticated relationship — `need_influences_need` with `contributes_to` / `blocks` / `compounds` — which is exactly the kind of relational insight the Overview's Ch 1.2 demands.

**Remaining gaps.** `ONTOLOGY_DESIGN.md` §2.3 imposes four mandatory obligations on every relationship kind: what it connects and whether direction matters; **temporal validity**; **expected plurality, stated explicitly and never assumed**; and epistemic treatment. The discovery supplies the first and gestures at the fourth. It supplies almost nothing on the second and third, and these are facts about reality, not modelling choices:

- May a person belong to two households concurrently? (Displacement makes this routine; the repository never says.)
- May a case have more than one concurrent Support Plan? Never stated.
- May a household have more than one head? `registration-identity/08` §3 records spousal disputes over headship but does not answer the cardinality question.
- May one person be simultaneously beneficiary and volunteer? The client's draft assumes role fluidity; the repository never addresses it.
- Do dependency relationships have types (care / financial / decision / legal)? Only the archived blueprint §6 says so.

Also unsupported: `need_influences_need` and `assertion_influences_assertion` — arguably the most ontologically consequential relationships in the glossary — have no discovery evidence at all.

**Invention required?** Yes, for temporal validity and plurality across most relationship kinds, and for the whole typed-dependency structure.

---

### 5.5 Layer — Constraints

**Support status: SUPPORTED**

**Repository evidence.** This is a strength. Each domain's `05-business-rules.md` delineates policy by altitude exactly as the Stage 5 standard requires — Universal / Donor / Regional-Government / Organisation / Programme — and each `12-domain-invariants.md` states enduring truths. `HBRM` Ch 9 supplies the three-layer scope framework directly (Universal Business Principles / Regional Business Practices / Organisation-Specific Operational Policies), which is precisely what AR-5's universal-or-variable tag needs.

Strong universal candidates, multiply attested: evidence precedes execution; separation of assessment from delivery; anti-fraud separation of duties; consent gates external sharing; identity precedes action; no organisation may override another's independent assessment; liability flows upward to the prime grant holder; the right to complain without retribution; trust is not transitive.

Strong variable candidates with named scope: household definition varies by culture; two-points-of-evidence verification (organisation-scoped); three-quote procurement minimum (donor-scoped); localization funding quotas (donor-scoped); national disaster-response frameworks (government-scoped).

The exception structures are unusually good — the necessity-exception clause (necessity, proportionality, minimum information, transparency as soon as possible, continued human accountability) is stated consistently across five domains and traces cleanly to Constitution Article IX.

**Remaining gaps.** Constraint *content* on the reality side is thin because the reality side is thin — there are no constraints about what combinations of household composition, health condition or capability are possible or impossible, because none of those concepts exist. And every universal tag will remain permanently marked *untested* (see §5.9).

**Invention required?** For process constraints: no. For reality constraints: yes, but as a consequence of the Facets gap rather than independently.

---

### 5.6 Layer — States

**Support status: SUPPORTED**

**Repository evidence.** The strongest layer in the repository. Ten distinct state progressions are discovered and, importantly, kept distinct from one another:

- Engagement Stage vs Human Development Stage — the dual-lifecycle separation, asserted in `GLOSSARY.md`, `HBRM` Ch 3, `case-management/07`, `case-management/14`, and corroborated externally by TD-03 (BD-TD03-002, High confidence, ≥4 sources)
- Identity lifecycle: Intake → Verification → Active → Suspended → Archived/Deceased
- Household lifecycle: Formation → Evolution → Dissolution
- Organisational Trust lifecycle: Unknown → Vetted → Trusted → Suspended → Blacklisted
- Partnership lifecycle (6 stages); Programme cycle (5 stages); Procurement and Fulfilment lifecycles; CFM lifecycle; Evaluation lifecycle (Baseline → PDM → Endline → Impact)

§2.5's plurality obligation — multiple simultaneous states across different aspects — is directly supported by the dual-lifecycle finding and by `HBRM` Ch 3's worked case (actively enrolled while in acute crisis). §2.5's epistemic-honesty obligation is supported by the claim/evidence discipline running through every domain.

**Remaining gaps.** Need state is underspecified (`open / matched / fulfilled` appears only in the client's draft, not in the repository). Human Development Stage transition criteria — what evidence moves someone from stabilization to recovery — are undiscovered, and `HBRM` Ch 7 logs this as an explicit Open Discovery Assumption.

**Invention required?** For state *sets*: no. For transition criteria on the human-development trajectory: yes.

---

### 5.7 Layer — Events

**Support status: SUPPORTED**

**Repository evidence.** Approximately 70 business events across seven `06-business-events.md` files, all stated in business language, all as point-in-time occurrences, with clear causal relationships to state transitions. Case Management alone contributes 24, including the epistemically interesting ones — Evidence Verified, Evidence Invalidated, Evidence Expired, Consent Withdrawn, Duplicate Identified, Safeguarding Concern Raised, Appeal Submitted. §2.6's no-rewriting discipline is supported by the repository's audit-trail requirements (Constitution Art. X(c)) and by `KNOWLEDGE_TRANSFORMATION_PATTERNS.md`.

**Remaining gaps.** One category is entirely missing: **life events**. `PROJECT_OVERVIEW.md` Ch 1.2 explicitly names *"significant life events, displacement, crises, or disasters"* as a foundational dimension, and Ch 4.1's worked example turns on them. The repository's 70 events are all *system* events — things that happen to a record or a process. Birth, death, marriage, separation, displacement, injury, illness onset, job loss, school dropout, return, resettlement appear nowhere. These are the causal spine of "how circumstances came to exist," which §2.6 identifies as the reason the Events layer exists at all. The client's own Flow C ("Aisha's father has got a job so we will reduce their food cycle need") is a life event driving a need revision — and the repository cannot represent it.

**Invention required?** Yes, for the life-event taxonomy. This is a smaller and more tractable gap than Facets but belongs to the same root cause.

---

### 5.8 Layer — Cognition

**Support status: PARTIALLY SUPPORTED — better than the Project Lead may fear, weaker than it looks**

This is the layer the Project Lead singled out. My assessment is more optimistic than his warning implies, with one important qualification.

**Repository evidence — substantial.**

- Claim / Evidence / Verified Claim / Finding separation is the most consistently applied idea in the repository, present in all seven domains and reinforced as the "Verification Barrier" (`case-management/04b`) and "Verification Gradient" (`registration-identity/04b`: *"Identity is not binary; it exists on a spectrum of trust based on the weight of evidence"*)
- Constitution Article III's four-part Standard of Understanding, and Article VIII's human-review threshold, are stated once, normatively, and referenced rather than restated — good discipline
- `PROJECT_OVERVIEW.md` Ch 5.2 gives seven named evidence-strength factors: source credibility, method of collection, relevance, timeliness, completeness, corroboration, consistency. This is the business criteria for confidence, and it is explicitly non-numeric and explainable — satisfying Article X and Pillar P4
- Ch 5.2 also mandates preservation of conflicting evidence with provenance, and defines "operationally accepted" as revisable — the claim/accepted-conclusion distinction §2.7 requires
- `GLOSSARY.md` supplies Claim Basis (first_hand / second_hand / observational / inferred, "determines verification weight"), Confidence Level (high / medium / low / highly uncertain), Gap (with critical / high / medium severity), Finding Consensus, Reverification Trigger, Verification Finding
- **The 20 decision points are the strongest asset in the repository for this layer.** Every one names its supporting evidence, its uncertainty, and its human override. `registration-identity/08` §2: *"Mandatory human review for all merges; algorithms cannot auto-merge identities."* `case-management/08` §1: *"May rely on unverified community assertions in acute crisis."* `accountability-evaluation/08` §2: *"Often a 'he said, she said' scenario with no hard proof."* This is real epistemic content about real decisions
- Polymorphic evidence validity — some evidence immutable, some expiring — is established and correctly remediated (MAJ-01 / REM-02)

**Remaining gaps — real but narrower than the other layers.**

- `DISCOVERY_HARMONIZATION_REPORT.md` §2 names it directly: *"Domains recognize that data is often unverified or highly uncertain, but lack a unified mechanism to represent this uncertainty formally."* The recommended fix — ADR: Standardized Epistemic Wrappers (Claimed / Community Validated / Document Verified) — was recommended and never written; no ADR exists anywhere in the repository
- `case-management/11-evidence.md` lists as a Knowledge Gap: *"How is uncertainty formally represented when an assessor suspects a vulnerability but lacks hard evidence?"* and *"How are conflicting evidence sources reconciled in practice when community validation contradicts documentary proof?"*
- Stage 6.1's stable-core working definitions for **Uncertainty** and **Temporal change** were never produced (see §2)
- The claim/evidence discipline is applied thoroughly to *identity* and *verification*, and thinly to *need and vulnerability* — because those concepts are themselves thin

**Where I part company with the framing.** The formal *representation* of uncertainty is squarely ontology-design work — §2.7 exists to do exactly that, and the harmonization report's "lack a unified mechanism" is a complaint that ontology design has not yet happened. That is not a foundation gap. What *is* a foundation gap is thinner: the repository never establishes, from practice, **what evidence grades practitioners actually recognise** and **what threshold of evidence is treated as sufficient to act** for each decision class. Ch 5.2 gives the factors; `registration-identity/05` gives one concrete rule ("two distinct points of evidence"). Everything else is unstated.

**Invention required?** Modest. An architect could design a defensible Cognition layer today from Ch 5.2 + Article III + Article VIII + the 20 decision points + the glossary's epistemic vocabulary. They would be inventing the specific evidence-sufficiency thresholds. **The Project Lead's warning is correct in direction but should be redirected: Cognition is recoverable; Facets is not.**

---

### 5.9 Layer — Coordination Patterns

**Support status: SUPPORTED — the strongest-evidenced layer after Events**

**Repository evidence.** `KNOWLEDGE_TRANSFORMATION_PATTERNS.md` supplies five fully-analysed patterns, each with business meaning, rationale, participating concepts, decision points, and uncertainty: the Epistemic Justification Loop, the Feedback and Adaptation Loop (Objective Distance), the Consent and Visibility Chain, the Institutional Trust Triad, the Hierarchical Constraint Pattern. Each domain's `04b-knowledge-patterns.md` adds two more, giving roughly nineteen distinct patterns in total.

Critically, these are stated as *shapes*, not procedures — which is exactly what §2.8 requires and what it warns is hardest to police. `cross-organisational-coordination/04b`: *"Context Over Control: Information is shared as an Alert or a Recommendation, never as an Execution Trigger across organisational boundaries."* That is a coordination pattern with a constraint, stated without a single workflow mechanic. `accountability-evaluation/04b`: *"The Objective Distance Pattern: Evaluator must have zero operational authority over Executor."* Also correct in form.

The External Referral lifecycle (`cross-organisational-coordination/07`) gives a five-step multi-party handshake with an explicit trust precondition and a feedback loop. The Deduplication Conflict Resolution decision (`cross-organisational-coordination/08` §2) is genuinely sophisticated: it names four alternative outcomes including two failure modes (*"Both proceed (wasting resources), Both withdraw (harming the beneficiary)"*), names the absence of command authority as the governing constraint, and names beneficiary preference as a human override.

**Remaining gaps.** The Consent Revocation Cascade is identified as a pattern and simultaneously identified as unsolved — three separate domains log it as an open question, and `DISCOVERY_HARMONIZATION_REPORT.md` §2 calls the mechanical flow of the "kill signal" across autonomous domains "highly ambiguous." That is honest and correct; it is a known unknown, properly logged, and modellable as an open pattern with an unresolved resolution step.

**Invention required?** No. This layer is derivable today.

---

### 5.10 Business Pillars

**Support status: SUPPORTED — already authored**

`ONTOLOGY_DESIGN.md` §3 supplies P1–P7, each traced to a specific Overview chapter and Constitution article, each stated as a test rather than an aspiration, and each correctly distinguished from a Constraint ("a Constraint is conditionally true of reality somewhere; a Pillar is true of *this project* everywhere"). P6 in particular — "Understanding precedes automation, structurally" — correctly makes the canonical sequence a property of the knowledge rather than of the software. The Pillars are derived from Article II's five principles without adding to them, honouring the prohibition. Nothing to invent.

---

### 5.11 Architecture Rules

**Support status: SUPPORTED — already authored, with one recommended addition**

`ONTOLOGY_DESIGN.md` §4 supplies AR-1 through AR-10. The promotion test (AR-2) is well constructed: eight ordered questions designed so two authors converge independently, with an explicit instruction to escalate rather than guess, and a requirement to pressure-test the test itself against a mixed sample before first use. AR-3 (one concept, one definition, one home), AR-5 (no silent universals), AR-6 (history is never rewritten), AR-7 (design purity) and AR-9 (flag, don't guess) are all sound and directly answer failure modes this repository has actually experienced.

The one thing missing is a rule enforcing Article VI at the ontology-content level against the departmental structure of the discovery corpus. AR-8 forbids organising the ontology around organisational departments but says nothing about the *inputs* being so organised. Recommended addition in §10.

---

### 5.12 Ground Truth Reviews

**Support status: PROCESS SUPPORTED / EXECUTION STRUCTURALLY BLOCKED**

**Repository evidence.** `ONTOLOGY_DESIGN.md` §5 defines the review well: what is reviewed (primitive set, definitions and placements, universal tags), who constitutes ground truth (practitioners *and* the people the ontology models — an important and correct distinction), when reviews occur (three trigger points, all already in the canonical documents), and how conflicts resolve (reality wins). Constitution Article XI(b) mandates direct engagement with domain experts, field practitioners and observed practice before structural modelling.

**Remaining gap — and it is severe.** No ground truth channel exists, and the repository knows it. `TD-01` Tier A Disposition: *"This discovery process has no mechanism to conduct direct elicitation with a human practitioner… This is a structural limitation of the execution environment."* Tier A was executed **zero times across six dossiers**. Every one of the seven domain STATUS files records `Client Validation: Pending`. `DISCOVERY_PHASE_REVIEW_01.md` §7 rates evidence quality as *"Good for Tiers B–D; structurally incomplete overall,"* noting Tier A absence underlies half the assumption register. `ONTOLOGY_DESIGN.md` §5 states the consequence itself: *"Until a channel to practitioners and affected communities exists, no Ground Truth Review can pass, and content dependent on one — every universal Constraint tag above all — remains marked untested, however strong its documentary evidence."*

**Is this a Foundation Gap under the stated definition?** Strictly, no — the knowledge in the repository is discoverable, so an architect is not forced to invent. But it means the entire foundation rests on sector literature and internal inference, never once checked against the reality of the actual population, the actual partners, or the actual context Khidmat will serve. Constitution Article XIV places Reality above every document; the repository has never consulted it. I classify this as the **single largest architectural risk** rather than a gap, and note that it is the one item on this list that only the Project Lead can unblock.

---

### 5.13 Evidence

**Support status: PARTIALLY SUPPORTED**

**Repository evidence.** The discipline is well specified: `ONTOLOGY_DESIGN.md` §6 scales evidence requirements to structural commitment, requires declared qualitative confidence traceable to specific evidence, requires assumptions to remain visibly assumptions with owner and overturn condition, and requires contradictions to be preserved rather than smoothed. The machinery exists and has been used well in places: `ASSUMPTION_REGISTER.md` holds 14 entries each with why-necessary, owner and overturn condition; `CONTRADICTION_LOG.md` holds two, both routed to and resolved by the Human Owner with recorded rationale; `HUMAN_OWNER_DECISION_BRIEF_01.md` presents options without recommending; `VALIDATION/TRACEABILITY_MATRIX.md` grades 14 claims with evidence strength and status, correctly marking two Unsupported and two Insufficient/Partial. TD-01 through TD-06 carry real citations — roughly 45 external sources, tiered, with confidence ratings and corroboration counts, and with limitations declared rather than smoothed.

**Remaining gaps — two, both structural.**

First: **the seven Stage 5 domain discoveries carry no citations at all.** Not one source, tier, confidence rating or corroboration count appears in any of the ~140 files under `02-discovery/`. Their `11-evidence.md` files assert "Established Facts" with no provenance whatsoever. Much of the content is plausible and matches sector practice — but §6 states the governing rule explicitly: *"An assertion in any prior project artifact — including frozen ones — is not evidence for a design decision merely because it was recorded; its provenance must itself be evaluable."* Under the repository's own rule, the entire Stage 5 corpus is inadmissible as evidence for ontology design decisions. It cannot be weighed, confidence cannot be declared on it, and evidence requirements cannot be scaled to commitment against it.

Second: three of seven domains (`case-management`, `programme-management`, `resource-logistics`) record `Evidence: Pending Discovery` in their own STATUS files while being simultaneously treated as frozen and certified ready. `case-management/CASE_MANAGEMENT_DISCOVERY.md` is marked `status: Frozen`; the other six are `status: Draft`. Three lack the "READY FOR FREEZE" line the other four carry. The corpus does not agree with itself about its own maturity.

**Invention required?** Not invention — but a provenance retrofit across all seven domains is a prerequisite, because without it the ontologist cannot execute §6 at all.

---

### 5.14 Governance

**Support status: SUPPORTED (content) / UNSUPPORTED (execution)**

**Repository evidence — content.** `CONSTITUTION.md` is genuinely well built. Nineteen articles, each traced to an Overview chapter, none introducing new philosophy. Article XIV establishes the authority hierarchy with Reality above every document. Article XVI establishes the dependency chain and the two approval gates, and codifies the standing prohibition born of this project's own failure: *"A certification issued for a document whose content does not exist or has skipped a gate is void."* Article XVII composes the Domain Approval Authority; Article XVIII composes the Audit Authority with power to suspend deployment. `ONTOLOGY_DESIGN.md` §7 adds three change tiers scaled to blast radius, with Coordination Patterns escalated to Tier 2 minimum given their proximity to the automation boundary. This is a complete and coherent governance model.

**Remaining gaps — execution.**

1. **Two contradictory certifications stand simultaneously.** `03-cross-domain/STAGE5_CERTIFICATION.md`: *"CERTIFIED READY… The project is cleared to commence Stage 6."* `03-cross-domain/VALIDATION/CERTIFICATION.md`: *"NOT CERTIFIED… cannot be handed to Ontology Engineers."* `REMEDIATION_REPORT.md` says the layer is *"now eligible for an independent re-validation to achieve final certification"* — that re-validation never happened. There is no valid certification, and one invalid one asserting the opposite.
2. **The Stage 5 certification is itself void under Article XVI.** It certifies readiness for Stage 6 while Stage 6's own prerequisite work (Stable Core Alignment) has not been performed — a skipped gate.
3. **Package A has never been approved.** Article XVI makes Package A (Khidmat Foundation) approval by the Domain Approval Authority a precondition for ontology design. `PROJECT_STATUS.md` §9 records only CL-001 and CL-002 as Human Owner decisions. No Package A approval exists in any form.
4. **The decision ledger does not exist.** Articles XVII and XIX both require formal written decisions "recorded in the repository's decision ledger (the governance ledger)." `HUMAN_OWNER_DECISION_BRIEF_01.md` records that the directory scoped for this was deleted. A repository search finds no ledger, no ADRs, and no RFC mechanism — while at least five ADRs have been formally recommended (three in `DISCOVERY_HARMONIZATION_REPORT.md` §6, two in `CONCEPT_OWNERSHIP.md` §7).
5. Minor: the Constitution's own Validation Summary states *"Articles XVII, XVIII, and XIX are explicitly marked Reserved rather than populated with invented governance mechanisms"* — but all three **are** populated. A normative document contradicting its own validation summary.

**Invention required?** No business knowledge. But the gates must actually be run.

---

## 6. Architectural Strengths

1. **Governance is genuinely load-bearing, not ceremonial.** The Constitution derives every article from the Overview, refuses to invent philosophy, states the human-review rule exactly once and references it thereafter, and codifies the void-certification prohibition as a standing rule learned from a real failure. Few projects at this stage have this.
2. **The ontology-design framework is excellent.** `ONTOLOGY_DESIGN.md` deliberately contains no ontology, gives a discovery-first primitive derivation, motivates each of the eight layers from a specific property of humanitarian reality, and makes Cognition and Coordination Patterns first-class rather than afterthoughts. It correctly identifies that the ontology must model *what the system is entitled to believe*, not only what is true.
3. **The claim/evidence/verification spine is applied with real consistency.** It appears in identity, vulnerability, delivery, partner vetting and grievance investigation — five different contexts, same epistemic structure. That recurrence is exactly what §1.2's "kind-question" abstraction needs.
4. **Decision points are the repository's best asset.** Twenty decisions, each with evidence, policies, constraints, preconditions, alternative outcomes, escalation, review triggers, appeals, human override and uncertainty. This is a ready-made substrate for the Cognition layer and for Article VIII threshold representation.
5. **Business tensions are captured rather than resolved away.** Twenty-eight tensions across seven domains, each stated as a genuine pull between two legitimate interests. `programme-management/05c` ("Coverage vs Depth"), `registration-identity/05c` ("Inclusion vs Integrity", "Data Minimisation vs Deduplication") and `accountability-evaluation/05c` ("Accountability vs Assessment Fatigue") are the kind of thing that only comes from taking the domain seriously.
6. **Altitude discipline.** The programme/case split is discovered independently three times (TD-03, TD-04, TD-05, TD-06) and correctly maintained in the terminology harmonization. It is a real structural feature of humanitarian work, and getting it right early prevents a large class of modelling errors.
7. **Coordination patterns are stated as shapes, not procedures** — the hardest discipline in §2.8, and largely achieved.
8. **The validation layer did real work.** `VALIDATION/` treated the harmonization as untrusted, traced 14 claims, caught genuine ontology leakage and a genuine over-generalisation, and issued NOT CERTIFIED. That the certification was then simply contradicted rather than re-earned is a governance failure, not a validation failure — the validation itself was sound.
9. **Assumptions and contradictions are handled honestly.** Tier A's absence is declared repeatedly rather than smoothed; AR-002's geography gap is named as recurring; TD-01's Discovery Limitation explicitly warns future authors not to read the dossier as equivalent to a closed topic.

---

## 7. Architectural Weaknesses

1. **The knowledge is stratified and the canonical chain contains the wrong stratum** (§1, §4). This is the root cause of most other weaknesses.
2. **The domain decomposition mirrors the NGO software module list** the Overview Ch 1.1 and Constitution Article VI both name as the failure mode, and departmental discovery produced departmental knowledge (§3).
3. **The Reality/Operational admission test — the gate everything passes through — is applied contradictorily** in at least six documented cases (§5.1).
4. **The Stage 5 corpus has zero provenance**, making it formally inadmissible under the project's own evidence rules (§5.13).
5. **Stage 6.1 was skipped**; four of six stable-core elements have no working definition (§2).
6. **The strategic scope of Khidmat is internally contradictory.** `BUSINESS_MASTER_PLAN.md` §2 places *"Direct delivery of humanitarian aid or material resources"* and *"Building or replacing proprietary end-user case management workflows"* firmly **out of scope**, and §5 commits that *"Khidmat AI will never become a humanitarian aid-delivery organisation."* Stage 5 then discovers, in depth, a full aid-delivery operating model — procurement, warehousing, dispatch, FSP cash execution, last-mile distribution — and a full case-management workflow. This is defensible if the intent is to *understand* delivery without performing it, but the repository never says so, and the ambiguity is not harmless: Pillar P1 and Rule AR-1 turn on distinguishing reality from a particular organisation's operations, and you cannot apply that test crisply when it is unclear whose operations are in view.
7. **Three of the four social units are unowned.** Household, Family and Community have no canonical owner; `CONCEPT_OWNERSHIP.md` §7 leaves Community explicitly unresolved.
8. **The donor and giving side is ratified in principle and never discovered.** (§8, FG-4.)
9. **No ADRs exist** despite five being formally recommended; no decision ledger exists despite two Constitutional articles requiring one.
10. **Two contradictory certifications stand**, and Package A has never been approved (§5.14).
11. **`GLOSSARY.md` has drifted into being a de facto ontology.** It is `Normative`, it defines relationship semantics (`need_influences_need` with three qualifiers), it enumerates value sets (four resilience capacities, seven Islamic giving forms, eight asnaf categories, four trajectory values, four claim-basis values), and it assigns concept ownership. Under AR-7 (design purity) and AR-3 (one concept, one definition, one home), a normative glossary that pre-commits enumerated value sets is a structural commitment made before ontology design — the precise failure Ch 5.1 warns against.

---

## 8. Foundation Gaps

Each gap below states what business knowledge is missing, why it must exist before ontology design, which repository areas were reviewed, and why it cannot be derived. Gaps are ordered by blast radius.

---

### FG-1 — The dimensional model of a person's humanitarian reality (the Facet substrate)

**What is missing.** A discovered, evidenced account of the dimensions along which a human being's humanitarian reality varies: health (acute, chronic, disability, mental, nutritional), capability (physical, cognitive, educational, economic, caregiving), lifecycle stage as a developmental reality, education and skills, livelihood and income, economic circumstance and debt, documentation and legal status, displacement status, and protection exposure.

**Why it must exist before ontology design.** Facets is one of the eight required layers and one of the two Package B deliverables. `ONTOLOGY_DESIGN.md` §2.1 defines a Facet as an independently varying dimension of something, motivated directly from Ch 1.2's "two families identical on paper." Determining which dimensions materially change humanitarian understanding *is* the Article IV admission test applied to reality — business discovery, not modelling. Additionally, §1.2's primitive coverage test cannot be validly run against a corpus that excludes this material, and the primitive set is closed once ratified.

**Repository areas reviewed.** All seven `02-discovery/*/03-concepts.md`; all seven `*/09-information-requirements.md`; all seven `*/04-relationships.md`; `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch 1–9; `BUSINESS_ARCHITECTURE.md`; `FOUNDATION_CONCEPTS.md`; `SHARED_CONCEPT_CATALOG.md`; `PROJECT_OVERVIEW.md` Ch 1.2, 5.1; TD-01 through TD-06.

**Why it cannot be derived.** Total canonical yield is four lines (§5.2). The Overview explicitly defers refinement to the HBRM and the HBRM does not perform it. The content exists only in a deprecated archive document that `ONTOLOGY_DESIGN.md`'s preamble expressly excludes as a binding input, and in a glossary with no provenance that fails §6's evidence test.

**Severity: Blocking.**

---

### FG-2 — Family, Household and Community as discovered realities

**What is missing.** Household composition and its change rules (who counts, cultural variation, splits, merges, re-identification, concurrent membership); Family as distinct from Household with typed relationships (kinship, dependency, responsibility) and typed dependency (care, financial, decision, legal); Community context (settlement type, service access, local organisations, livelihood patterns, seasonal and environmental hazard).

**Why it must exist before ontology design.** These are three of the four social units in the Overview's own model. §2.2 requires stated identity criteria for every Entity kind, warning that without them "the deduplication and continuity failures of Ch 1.1 are rebuilt inside the ontology itself." §2.3 requires plurality and temporal validity stated explicitly for every Relationship. Household membership is the paradigm case for both and is unanswered.

**Repository areas reviewed.** `registration-identity/` in full (the domain closest to owning this); `case-management/03,04,04b,05b`; `CONCEPT_OWNERSHIP.md`; `FOUNDATION_CONCEPTS.md`; `SHARED_CONCEPT_CATALOG.md` §1; `GLOSSARY.md`; `HBRM` Ch 9.

**Why it cannot be derived.** The repository repeatedly asserts that these are complex and variable, and repeatedly logs the question rather than answering it — `registration-identity/10` Q1, `SHARED_CONCEPT_CATALOG.md` §1 ("How does the system handle an Identity that splits?"), `VALIDATION/FINDINGS.md` REC-01 (recommends assigning someone to answer it, unassigned), `CONCEPT_OWNERSHIP.md` §7 (Community unresolved). Family and Community substance exist only in the archived blueprint §§6, 8 and in glossary terms with no discovery.

**Severity: Blocking.**

---

### FG-3 — Vulnerability, Risk and Protection as business content

**What is missing.** What actually makes a person or household vulnerable; how risk factors compound; what hazard categories exist; what protective factors and resilience capacities are; how risk severity, horizon and trend are actually judged in practice.

**Why it must exist before ontology design.** The Overview's success measure (Ch 9.2) is "earlier identification of vulnerability before crisis escalation." Vulnerability drives needs, needs drive plans, plans drive delivery. Under Article IV this is the clearest possible case of decision-changing knowledge. Vulnerability content also determines large parts of Facets and Constraints.

**Repository areas reviewed.** `case-management/03` (four bare names: Vulnerability, Vulnerability Indicator, Risk, Safeguarding Concern, with no definitions); `case-management/04` ("A Vulnerability generates a Need", "A Risk influences a Priority"); `GLOSSARY.md` Risk and Vulnerability Terms (~25 terms, richly defined); `SHARED_CONCEPT_CATALOG.md`; `FOUNDATION_CONCEPTS.md` (does not include vulnerability among its four foundational concepts).

**Why it cannot be derived.** The glossary's 25 risk terms — Risk Composition, Risk Characterization, Risk Profile, Hazard Category, Exposure, Risk Horizon, Trend, State, Severity, Compound Risk, Protective Factor, Absorptive/Adaptive/Recovery Capacity, Support Redundancy, Role Substitution Capacity, Buffering Capacity, Financial Buffer, Livelihood Diversity, Treatment Continuity Active, Protection Indicator — have **zero corroboration** anywhere in the discovery corpus. This is not derivation, it is faith. §6 forbids it explicitly.

**Severity: Blocking** — though closable primarily by validation rather than fresh discovery.

---

### FG-4 — The giving, funding and resource-origin side

**What is missing.** How giving actually works as humanitarian reality: donor intent and motivation; the distinction between institutional grant funding and individual giving; restricted vs unrestricted funds as constraints on who may receive what; and — critically — the Islamic giving model. `GLOSSARY.md` asserts seven canonically distinct forms (Zakat, Sadaqah, Sadaqah Jariyah, Waqf, Fidya, Kaffarah, Qurbani), each with "its own obligation basis and restriction shape," plus eight Zakat-Eligible Categories (asnaf) that an eligibility rule may reference. `HBRM` Ch 1 and Ch 9 describe the vertical/horizontal philanthropy split as a real structural distinction.

**Why it must exist before ontology design.** Zakat eligibility is a **constraint on who may receive what** — indisputably Reality Knowledge under Article IV, and directly decision-changing on fairness and appropriateness grounds. CL-002 was ratified by the Human Owner: *"Donor is a valid humanitarian business concept. The exclusion of donor-facing functionality from Khidmat V1 is strictly an implementation-scope decision and not a statement about humanitarian reality."* A ratified concept with no discovery cannot enter the ontology.

**Repository areas reviewed.** All of `02-discovery/` (grep for zakat/sadaqah/giving returns **zero** hits; "donor" appears only as an external constraint-setter in programme and logistics rules); `GLOSSARY.md` Donor & Resource Terms; `HBRM` Ch 1, Ch 9; `BUSINESS_MASTER_PLAN.md` §3, §9; TD-01 BD-TD01-006 (Medium confidence, two sources, narrow scope); AR-013 (open).

**Why it cannot be derived.** There is no discovery domain for it. `programme-management/03` classifies Grant and Budget as *Operational* Knowledge and its boundaries exclude fundraising; `resource-logistics` owns procurement but not funding origin. TD-01's single finding establishes only that a vertical/horizontal split exists — it does not supply the seven forms, their obligation bases, or the asnaf categories. AR-013 remains open on which other cultural frameworks are even in scope.

**Severity: Blocking for any programme/eligibility modelling; high-impact given the client's own product is donor-driven.**

---

### FG-5 — Applicability context: where, for whom, with whom

**What is missing.** A stated deployment geography, population, crisis type and partner set.

**Why it must exist before ontology design.** AR-5 requires every Constraint to carry a universal-or-variable tag, and *"A variable Constraint names the scope in which it holds. No Constraint's scope is ever left implicit."* With no stated context, every variable constraint is unscopeable and every universal tag is an untestable strong claim. `ONTOLOGY_DESIGN.md` §5 additionally requires reviews against "at least one real context" — there is none nominated.

**Repository areas reviewed.** Every document. AR-002 states it flatly: *"No document reviewed anywhere in this project states an initial deployment geography, so no narrower scope could be tested against even if desired."* `DISCOVERY_PHASE_REVIEW_01.md` §4 identifies it as the assumption most likely to propagate silently into everything downstream. TD-01 Open Gap 3 repeats it.

**Why it cannot be derived.** It is a fact about the project, not about the world. Only the Project Lead and client can state it. *(Note: the client's own blueprint answers much of this — Karachi Zone 4, Pakistan-based beneficiaries, UAE-based donors, PKR/AED currencies, an offline-first field context. This has never entered the repository.)*

**Severity: Blocking, and the cheapest of all to close.**

---

### FG-6 — Need, intervention fit and outcome at case altitude

**What is missing.** What a need consists of at case level: its categories, its severity determination, its expiry and resolution conditions, and its relationships to other needs. What makes a given intervention appropriate for a given person beyond categorical eligibility. What counts as an outcome — what "worked" means.

**Why it must exist before ontology design.** Need is the pivot of the whole model (Overview Ch 4.1's worked example turns on it; `SHARED_CONCEPT_CATALOG.md` §3 calls it "the primary driver of all downstream humanitarian action"). Outcome is how Ch 9.2's success is measured.

**Repository areas reviewed.** TD-06 (excellent, but programme-altitude: Sector × Modality × Temporal Phase); `case-management/03` (Need as a bare name); `SHARED_CONCEPT_CATALOG.md` §3; `accountability-evaluation/` (Baseline, Endline, Indicator, Logframe — programme-altitude again); `GLOSSARY.md` (Outcome Indicator; Intervention Readiness; Intervention Objective Category; Intervention Relationship — all uncorroborated).

**Why it cannot be derived.** The repository explicitly logs this as unresolved rather than answering it. `HBRM` Ch 7 carries a standing Open Discovery Assumption: *"The specific, informal criteria the client and domain team currently use in practice to judge whether an intervention 'worked'… remains an unresolved discovery topic."* AR-011 repeats it. `case-management/10` asks the same question. Need categories exist only in the archived blueprint §9.

**Severity: Blocking for the Need/Intervention/Outcome cluster; moderate for the rest of the ontology.**

---

### FG-7 — Life events

**What is missing.** The taxonomy of events in a person's life that change their humanitarian reality: birth, death, marriage, separation, displacement, return, injury, illness onset, recovery, job loss, employment, school enrolment and dropout, eviction, disaster exposure.

**Why it must exist before ontology design.** §2.6 states the Events layer exists because "explanation is causal history, and Events are its unit," citing Ch 1.2's *"significant life events, displacement, crises, or disasters."* All ~70 discovered events are system or process events; none is a life event.

**Repository areas reviewed.** All seven `06-business-events.md`; `PROJECT_OVERVIEW.md` Ch 1.2, 4.1; `GLOSSARY.md` (Lifecycle Transition, Trajectory).

**Why it cannot be derived.** Not present. Partially inferable from `registration-identity/06` (Household Formed, Household Split) and from glossary Trajectory values (structural / crisis_triggered / progressive / acute), but the taxonomy itself must be discovered.

**Severity: Moderate — smaller than FG-1 and closable alongside it.**

---

## 9. Architectural Risks

**R1 — Premature primitive closure.** §1.4 closes the primitive set on ratification. Deriving it from a corpus missing FG-1 through FG-4 guarantees a Tier 3 foundational amendment later — the most expensive change class the governance model defines. *Likelihood: high if design starts now. Impact: high.*

**R2 — Departmental structure leaking into the ontology.** AR-8 forbids it, but every input is departmentally scoped and no rule governs the inputs. The most likely concrete failure is a Case-Management-shaped Person entity and a Registration-shaped Identity entity coexisting as near-duplicates — the exact split-brain problem `CONCEPT_OWNERSHIP.md` §4 warns about, reintroduced at the ontology level. *Likelihood: medium-high. Impact: high.*

**R3 — Unfalsifiable ontology.** With no ground truth channel, every universal constraint stays untested and every layer placement rests on literature and inference. `ONTOLOGY_DESIGN.md` §5 requires this be "recorded, not worked around." Recording it honestly means shipping an ontology whose reality-correspondence is unverified — which is in tension with the mandate itself. *Likelihood: certain unless the Project Lead opens a channel. Impact: high.*

**R4 — Glossary-as-ontology precedent.** `GLOSSARY.md` already pre-commits enumerated value sets and relationship semantics with no evidence trail. If it is treated as authoritative input, the ontology inherits unvalidated structural commitments; if it is discarded, the project loses its richest content. Neither is decided. *Likelihood: high. Impact: medium-high.*

**R5 — Certification drift.** Two contradictory certifications stand, one of them void under Article XVI, and no decision ledger exists to adjudicate. The project has already suffered a void certification once and codified a rule against it; the rule is currently being violated. *Likelihood: present. Impact: medium-high, mostly to credibility and auditability.*

**R6 — Scope ambiguity corrupting the admission test.** Until it is settled whether Khidmat is a neutral knowledge utility (BMP) or a full aid operating model (Stage 5, client draft), P1/AR-1 cannot be applied with confidence, and the Reality/Operational split will keep drifting. *Likelihood: high. Impact: high — it is the gate every concept passes through.*

**R7 — Client-repository divergence.** The client's blueprint centres trust scoring, escrow, fraud detection, offline-first field ops, ID cards and multi-tenancy — all explicitly excluded by the archived blueprint §17 and none re-adjudicated in canonical documents. Two specific collisions are worth naming now, because they are governance issues rather than preferences: a 0–1000 computed trust score used as a **gate on receiving aid** ("Restricted 0–199: receive aid only") sits directly against Constitution Article X (need evaluated through evidence, never through assumptions or scoring about a person) and Pillar P4 (no unexplainable confidence scores); and beneficiary-facing autonomous action at ">80% of operations without human review" sits against Article VIII unless each automated action class is shown to fall below the consequence threshold. *Likelihood: high. Impact: high — discovered late, this is a rebuild.*

---

## 10. Recommendations

Only genuine blockers to beginning ontology design are listed. Improvements that would merely make the repository better are deliberately excluded.

### Blocking — business knowledge (must close before Package B)

**B1. State the applicability context.** One page: deployment geography, population, crisis type(s), initial partner organisations, cultural and religious giving context, languages. Closes FG-5 and unblocks every constraint scope tag. *Effort: hours. Owner: Project Lead. This is the highest leverage item in this report.*

**B2. Run a Human Reality discovery domain.** A Stage 5 domain — same 20-section standard — covering Person, Family, Household and Community as realities: lifecycle stage, capability, health, dependency (typed), education, livelihood and income, documentation status, displacement, household composition and change rules, housing and utilities, community context and seasonality. Use the archived blueprint §§5–8 and the relevant glossary terms as **candidate input requiring re-validation**, exactly as `ONTOLOGY_DESIGN.md`'s preamble prescribes — not as inherited truth. Closes FG-1, FG-2, and most of FG-7.

**B3. Run a Vulnerability, Risk and Protection discovery domain.** Same standard. Re-validate the ~25 glossary risk terms against evidence, or retire them. Closes FG-3.

**B4. Run a Giving and Resource-Origin discovery domain.** Donor types and intent; grants, contributions and restrictions as constraints; the Islamic giving model with its seven forms, obligation bases and restriction shapes; Zakat asnaf categories as eligibility-bearing classifications. Closes FG-4 and honours the ratified CL-002.

**B5. Complete the Need / Intervention-Fit / Outcome discovery at case altitude.** Need categories, severity determination, need-to-need relationships, expiry and resolution; what makes an intervention appropriate for a person; what "worked" means. Explicitly closes the standing Open Discovery Assumptions in `HBRM` Ch 7 and AR-011. Closes FG-6.

### Blocking — knowledge integrity (must close before Package B)

**B6. Re-adjudicate the Reality/Operational classification across the entire concept corpus, in one pass, against one written rubric.** Resolve the six documented contradictions in §5.1. Reconcile `programme-management`'s classification of Programme as Operational Knowledge against ratified decision CL-001. Publish the rubric so AR-1 is reproducible.

**B7. Retrofit provenance onto the seven Stage 5 domains.** Each asserted fact gets a source, tier and confidence, or is demoted to an assumption with an owner and overturn condition. Without this the corpus is formally inadmissible under §6 and no design decision built on it can declare confidence.

**B8. Perform Stage 6.1 Stable Core Alignment and publish the Stable Core Definitions note.** Working definitions for all six: Identity, Relationships, Evidence, **Uncertainty**, **Temporal change**, **Context** — the last three of which currently have none. Then run the mandated cross-check: confirm every qualified concept can be described in stable-core terms. This is the pipeline's own gate and it has been skipped.

### Blocking — scope and governance (must close before Package B)

**B9. Settle what Khidmat is.** Reconcile `BUSINESS_MASTER_PLAN.md` §2/§5 (never delivers aid; does not build case-management workflows) against Stage 5's full delivery and case-management discovery, and against the client's Direct Relief blueprint. A single ratified statement of whether Khidmat *understands* delivery, *performs* delivery, or both. Without it, P1 and AR-1 are unapplicable. Record it as the first ADR.

**B10. Establish the decision ledger and clear the certification contradiction.** Create the governance ledger Articles XVII and XIX require. Formally void `STAGE5_CERTIFICATION.md` (skipped gate, Article XVI) and either re-run validation to certification or record NOT CERTIFIED as the standing state. Write the five outstanding recommended ADRs: Location ownership; Household-split responsibility; Consent propagation; Epistemic evidence grading; Immutable snapshots for MEAL.

**B11. Assign owners for Household, Family and Community**, and resolve `CONCEPT_OWNERSHIP.md` §7. My recommendation is that B2's Human Reality domain owns all three, but the assignment must be recorded, not assumed.

**B12. Obtain Package A approval from the Domain Approval Authority**, in writing, in the ledger, after B1–B11. Article XVI makes this non-optional.

### Blocking — validation capability

**B13. Open a ground truth channel.** Even a minimum viable one: three to five practitioner sessions and one consented affected-person consultation per reality stratum. Tier A has been executed zero times in six dossiers and the repository has said so honestly every time. Only the Project Lead can unblock it. Without it, no Ground Truth Review can pass, every universal constraint stays untested, and the mandate's own standard ("Reality above every document") is never met.

### Recommended, not blocking

**B14. Add AR-11 to `ONTOLOGY_DESIGN.md`:** *"Reality strata over organisational strata. No layer content may be named, grouped, or scoped by an operational domain. Domain provenance is recorded as metadata only. Where a concept exists in multiple domains, the ontology names it once, by what it is in reality, never by which department discovered it."* This closes the gap between AR-8 (which governs the ontology) and the departmental structure of the inputs, and directly answers the Project Lead's bottom-up critique.

**B15. Downgrade `GLOSSARY.md` from Normative to Candidate Vocabulary** until each term has provenance, and strip its enumerated value sets pending ontology design (AR-7). Its current status makes unevidenced value sets binding.

---

## 11. Final Reflection

*If I were appointed Chief Ontology Architect tomorrow, prohibited from interviewing stakeholders or performing additional business discovery, could I begin the ontology-first process using only this repository?*

**Partially — and not far enough to deliver Package B.**

I could begin, and I would get further than I expected before reading the repository closely. I could derive a defensible candidate primitive set. I could design Entities, Relationships (structurally), Constraints, States, Events and Coordination Patterns to a reviewable standard, because the discovery genuinely knows how humanitarian organisations operate and states it in business language. I could design a Cognition layer of real quality from Ch 5.2's evidence factors, Articles III and VIII, the twenty decision points and the glossary's epistemic vocabulary — the Project Lead's warning about Cognition is directionally right but, on the evidence, that layer is recoverable.

I would stop at **Facets**, and I would stop hard.

Facets is where a person's reality lives, and the canonical repository contains four lines of it. I would open `PROJECT_OVERVIEW.md` Ch 1.2, find thirteen dimensions and an explicit statement that they are *not* the model and that the HBRM will refine them. I would open the HBRM and find it does not. I would search all seven discovery domains and find no health, no capability, no dependency, no livelihood, no education, no shelter, no community context. I would then find all of it in a document stamped "Deprecated" that my own governing framework forbids me to use as a binding input, and in a glossary with no provenance that my own evidence rules forbid me to trust.

At that point AR-9 gives me exactly one legitimate move: flag and escalate. Guessing would mean inventing what makes a human being vulnerable, and inventing it for a population whose location the repository has never stated (AR-002) and whose practitioners it has never once spoken to (Tier A, zero of six).

And I could not honestly proceed even on the layers I *could* build, because §1.2's coverage test binds the primitive set to the whole validated corpus, and §1.4 closes that set on ratification. Ratifying primitives now, then discovering the human-reality stratum, would force a Tier 3 foundational amendment — the most expensive change the governance model recognises. Sequencing forbids starting.

There is a second, quieter reason I would stop. I would notice that `PROJECT_OVERVIEW.md` Ch 1.1 diagnoses the sector's failure as systems built around registration, case management and donation management — and that Stage 5 has discovered exactly registration, case management, programme management, logistics, M&E, coordination and partner management. The repository has, with great rigour and complete sincerity, described the thing it exists to replace. That is not a fatal error; the operational knowledge is real and needed. But it means the reality-side discovery still has to happen, and it explains cleanly why FG-1 through FG-4 all point the same direction.

What I want to state plainly, because it changes the character of the recommendation: **this is not a failing repository.** The governance is better than most funded programmes achieve. The ontology framework is genuinely good. The discovery, within the scope it chose, is thorough and honest — it declares its own limitations repeatedly rather than hiding them. The gap is a **scoping error compounded by an archiving error**: Stage 5 asked departmental questions, and Stage 4's reconciliation step — which the pipeline itself specified, and which was never performed — quietly dropped the human-reality model out of the canonical chain when the old blueprint was archived rather than reconciled.

Both are recoverable. Most of the missing content has already been written once; it needs to be re-earned through evidence, not re-imagined. That is weeks of work, not a restart.

---

## 12. Final Decision

# FOUNDATION INCOMPLETE

**Justified entirely on repository evidence:**

1. **Stage 6.1 Stable Core Alignment — the pipeline's own gate immediately before ontology design — has not been performed.** Four of six stable-core elements (Relationships, Uncertainty, Temporal change, Context) have no working definition anywhere in the repository. The mandated cross-check was never run and the required Stable Core Definitions note does not exist. *(`KHIDMAT_FOUNDATION_PIPELINE.md` §6.1 vs `FOUNDATION_CONCEPTS.md`.)*

2. **The Facets layer — one of two Package B deliverables — has no canonical source.** Total yield across all seven discovery domains: four lines. The Overview delegated these dimensions to the HBRM; the HBRM did not supply them; Stage 4's reconciliation step was skipped and the content was archived rather than carried forward. *(`PROJECT_OVERVIEW.md` Ch 1.2; `HBRM` Ch 1–9; `02-discovery/*/03,04,09`; `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §§5–13.)*

3. **The Article IV admission test is applied contradictorily**, including a Stage 5 classification that contradicts a Human-Owner-ratified decision. Every primitive and every layer placement passes through this gate. *(Six documented contradictions, §5.1; CL-001.)*

4. **The Stage 5 corpus carries no provenance and is therefore inadmissible under the repository's own evidence rules**, while three of seven domains simultaneously record `Evidence: Pending Discovery` and all seven record `Client Validation: Pending`. *(`ONTOLOGY_DESIGN.md` §6; `02-discovery/*/STATUS.md`.)*

5. **Ratified business concepts have no discovery behind them.** CL-002 ratified Donor as a valid humanitarian business concept; there is no giving or resource-origin discovery, and zero occurrences of Zakat, Sadaqah or Islamic giving anywhere in `02-discovery/`, despite the glossary making Zakat-eligibility an eligibility-bearing classification.

6. **No applicability context exists anywhere in the project**, making AR-5's mandatory scope tags unassignable. *(AR-002, stated flatly and never closed.)*

7. **The formal gates are not passed.** Two contradictory certifications stand; the affirmative one is void under Article XVI for skipping Stage 6; Package A has never been approved; and the decision ledger that Articles XVII and XIX require does not exist.

**What this decision does not say.** It does not say the work is poor — much of it is excellent, and §6 records that in detail. It does not say ontology artifacts are missing; the absence of primitives, layers and modules is correct and expected at this stage, and I have deliberately not counted any of it against the repository. It says only this: **specific business reality that should have been discovered before ontology design has not been discovered, and a specific prerequisite stage the project itself defined has been skipped.**

**Distance to READY:** thirteen items (B1–B13), of which four are one-page decisions, four are validation-and-provenance passes over material that already exists, four are genuine discovery domains at the standard the project has already proven it can execute, and one — the ground truth channel — requires only that the Project Lead open a door.

---
---

# Appendix A — How I Would Execute the Ontology-First Process

*Answering: "if you were the ontologist, how would you have covered all these as per the project?"*

This is what I would actually do, in order, under this project's own rules.

## A.0 — Re-cut the knowledge base along reality strata (before anything else)

The single most important move, and the one that answers the Project Lead's bottom-up critique structurally rather than rhetorically. I would stop using the seven operational domains as the organising axis and re-index every discovered concept under six **reality strata**:

| Stratum | What lives here | Fed by |
|---|---|---|
| **I. Subject** | Person, Family, Household, Community — who exists and how they relate | registration-identity; **B2 (new)** |
| **II. Circumstance** | Condition, capability, need, vulnerability, risk, protection, resilience — what is true of them | case-management; **B2, B3 (new)** |
| **III. Warrant** | Claim, evidence, verification, confidence, uncertainty, gap, contest, sufficiency | all seven; strongest asset |
| **IV. Response** | Intervention, plan, delivery, resource, outcome — what is done and what changes | programme, logistics; **B5 (new)** |
| **V. Institution** | Organisation, programme, partnership, mandate, trust, donor, grant | org-partner, programme; **B4 (new)** |
| **VI. Coordination** | Referral, deduplication, consent propagation, escalation, handoff, custody | coordination, accountability |

The seven domains survive as **provenance metadata** on every concept — "discovered in case-management" — never as structure. This is AR-11 (recommendation B14) applied from day one. It costs a week and it prevents the ontology from inheriting the fragmentation the Overview exists to end.

## A.1 — Domain Primitives

Following §1.2 exactly: abstract from the corpus, ask the kind-question recursively, test each candidate against Article IV, then test the set for coverage.

My **candidate** set, derived from the corpus and offered as the output of that recursion rather than as an answer (the real set must be derived after B2–B5 close, or the coverage test is invalid):

| Primitive | What it categorises | Why the recursion produced it |
|---|---|---|
| **Identity** | That which persists and can be re-identified | Person, Household, Organisation, Programme, Case all recur across every domain as things that must be the *same thing* across encounters (`registration-identity/12`, `FOUNDATION_CONCEPTS.md` §1–2) |
| **Relation** | That which holds between identified things | Kinship, dependency, membership, custody, partnership, trust, referral — recur in all seven `04-relationships.md` |
| **Condition** | That which is true of something across a span and can change | Health, shelter, engagement state, development stage, need, vulnerability, trust level, stock level |
| **Occurrence** | That which happens at a point | ~70 discovered events plus the life events of FG-7 |
| **Evidence** | That which grounds belief | Document, biometric, testimony, observation, attestation, proof of delivery (`SHARED_CONCEPT_CATALOG.md` §2) |
| **Epistemic Stance** | What the system is entitled to believe | Claim status, confidence, uncertainty, gap, contest, review requirement (Ch 5.2; Art. III, VIII) |
| **Norm** | That which bounds what is permissible or valid | Eligibility rule, policy, invariant, consent authorization, mandate, Zakat restriction, MoU term |
| **Context** | The frame relative to which meaning holds | Place, culture, season, crisis phase, organisational and programme scope, applicability scope (`HBRM` Ch 9) |

Against the Overview's predicted six: Identity, Relation, Evidence and Context map directly; Uncertainty becomes **Epistemic Stance** (widened, because the corpus needs claim status and review requirement, not only confidence); Temporal change splits into **Condition** (span) and **Occurrence** (point), because §2.5/§2.6 make that distinction load-bearing. **Norm** is the one genuine addition, and I would defend it explicitly: eligibility rules, invariants, consent authorizations, donor restrictions and organisational mandates recur across all seven domains, are decision-determining under Article IV, and classify nowhere else without forced fit. Minimality: remove Context and every regional practice becomes a false universal — the exact failure §2.4 names. Remove Epistemic Stance and Articles III and VIII become unrepresentable — the Project Lead's warning.

Then the coverage test, run publicly against every concept in the repository, with the misfits published rather than hidden. Example placements: *Zakat-Eligible Category* → Norm within Context; *Household Resilience* → Condition; *Chain of Custody* → Relation over Occurrences; *Trust Level* → Epistemic Stance about an Identity; *Deduplication Alert* → Occurrence carrying an Epistemic Stance; *Gap* → Epistemic Stance.

## A.2 — The eight layers, in dependency order (AR-10)

**Entities first.** Few, each with stated identity criteria. The two hard ones get explicit treatment rather than deferral: *Person* (biometric + biographical + community attestation, with human adjudication mandatory per `registration-identity/08` §2, and false positives modelled as normal rather than exceptional) and *Household* (a temporal container — I would state the re-identification rule across split, merge and dissolution as the first thing designed, because `SHARED_CONCEPT_CATALOG.md` §1 and `VALIDATION` REC-01 both flag it and neither answers it).

**Facets second** — the layer this repository cannot currently supply, organised as facet families per subject kind:

- *Person:* lifecycle stage; health (acute / chronic / disability / mental / nutritional, incl. clinical staging); capability (physical / cognitive / educational / economic / caregiving); education and skills; livelihood and income; documentation and legal status; displacement status; protection exposure
- *Household:* composition; headship; housing tenure and condition; utilities and WASH access; economic profile (income sources, debt source, debt characteristic, financial buffer); resilience (absorptive / adaptive / recovery capacity, support redundancy, role substitution, caregiving continuity, decision continuity)
- *Community:* settlement type; service access and distance; livelihood pattern; local organisations; seasonal and environmental hazard calendar; social capital

Every facet designed as an **evidence-bearing assertion** per §2.1 — carrying observer, time, method and epistemic stance. Never a bare attribute. This is the design decision that makes Ch 5.2's "who observed this, when, how sure are we" structural rather than optional.

**Relationships third**, each with all four §2.3 obligations discharged explicitly — and I would treat *plurality* as the discipline that catches the most errors: state, for every relationship, whether more than one may hold concurrently, and refuse to accept a design that leaves it implicit. Typed dependency (care / financial / decision / legal) and `need_influences_need` (contributes_to / blocks / compounds) are the two highest-value relationships in the whole model and both need real evidence before they are admitted.

**States fourth**, plural and concurrent by default: engagement, human development, identity assurance, need, case, verification, consent, organisational trust, inventory. Each an evidence-based belief carrying provenance, per §2.5 — *"We believe this situation has stabilized, based on this evidence, as of this date."*

**Events fifth**, unified: the ~70 discovered process events plus the missing life events, all immutable, corrections layered rather than overwritten (§2.6).

**Constraints sixth**, every one tagged universal-or-variable, universals marked *untested* until B13 delivers ground truth, variables naming their scope from `HBRM` Ch 9's three-layer framework.

**Cognition seventh** — designed as a single epistemic envelope that every assertion-bearing element carries, not a parallel catalogue:

| Element | Content | Source |
|---|---|---|
| Assertion status | claimed / corroborated / verified / contested / superseded / expired | Ch 5.2; MAJ-01 polymorphic validity |
| Claim basis | first_hand / second_hand / observational / inferred | `GLOSSARY.md`; determines verification weight |
| Confidence | qualitative, justified by Ch 5.2's seven named factors, never a bare score | Ch 5.2; Art. X; P4 |
| Gap | what is unknown, its severity, what evidence would close it | `GLOSSARY.md`; Art. III(c) |
| Contest | competing assertions preserved side by side with provenance; Finding Consensus as governed resolution | Ch 5.2; Art. V |
| Sufficiency | Article III's four conditions as representable predicates over a decision | Art. III |
| Consequence class | whether Article VIII's threshold applies to this conclusion — the *fact*, not the queue | Art. VIII; Ch 7.2 |
| Expiry / re-verification trigger | evidence ages; some evidence does not | `case-management/06`; `GLOSSARY.md` |

The boundary I would police hardest: consequence class is Reality Knowledge; escalation mechanics are Operational Knowledge and stay out (Ch 7.2 says so explicitly).

**Coordination Patterns last**, composed from everything above: Referral Handshake; Deduplication Collision and Resolution; Consent Propagation and Revocation Cascade (with its resolution step honestly modelled as open); Trust Establishment and Suspension; Execution Handoff; Chain of Custody; Objective-Distance Evaluation; Hierarchical Constraint Cascade; Escalation to Human Judgment; Cross-Altitude Aggregation. Every one a shape, never a procedure — and every one reviewed at Tier 2 minimum per §7.

## A.3 — Pillars, Rules, Ground Truth, Evidence, Governance

**Pillars:** keep P1–P7 verbatim; add a written test procedure per pillar so "checked against the Pillars" is auditable rather than asserted.

**Architecture Rules:** keep AR-1–AR-10; add AR-11 (reality strata over organisational strata). Pressure-test AR-2 before first use exactly as §4 requires — I would use a deliberately mixed 40-concept sample and require two independent authors to converge before the test is trusted.

**Ground Truth Reviews:** sequence a minimum viable programme against B13 — three to five practitioner sessions plus one consented affected-person consultation per reality stratum. And I would adopt one standing test the repository already contains: `PROJECT_OVERVIEW.md` Ch 4.1's flood-displaced family must be representable end to end — every fact in that vignette, including the unverified observations and the relatives in another district — as a permanent regression test on the model. If the ontology cannot hold the Overview's own worked example, it is wrong.

**Evidence:** build the provenance register B7 requires and make it the ontology's own design record — every concept carrying source, tier, confidence, corroboration and the assumption it rests on. Continue the Assumption Register and Contradiction Log unchanged; they work.

**Governance:** instantiate the ledger, void the invalid certification, run Package A, then Package B, then stop — as `PROJECT_STATUS.md` §3 already commits.

---

# Appendix B — Reading the Client's Direct Relief Blueprint Against This Foundation

The client's blueprint is a **runtime and application design**: nine agents, Kafka, pgvector, escrow, ONNX, a six-pass pipeline, trust tiers, multi-tenancy. Under Constitution Article IV the great majority of it is **Operational Knowledge** and correctly stays out of the knowledge foundation. That is not a criticism — it is what an application blueprint should be.

But it contains genuine **Reality Knowledge that the repository currently lacks**, and it should be mined as Tier C evidence against exactly the gaps this assessment identifies:

| In the client blueprint | Reality Knowledge it evidences | Gap it feeds |
|---|---|---|
| Malnutrition classification (SAM / MAM / normal) from age, weight, height, MUAC; age-banded food baskets | Person health facet: nutritional condition with clinical staging; lifecycle stage as a driver of need | **FG-1** |
| Household of five: mother, three children, elderly father; guardian required for under-18 | Household composition; dependency and guardianship as typed relationships | **FG-2** |
| Need with severity index, urgency flag, expiry date, `circumstance_resolved` status, versioned history | Need as a dynamic entity with severity, lifecycle and revision — the case-altitude need model | **FG-6** |
| "Father has got a job, reduce their food cycle need to May only" | A **life event** (employment) causing a circumstance change that revises a need — precisely Ch 1.2's longitudinal reasoning, currently unrepresentable | **FG-7**, FG-6 |
| Donor intent in natural language; matching to specific beneficiary needs; recurring giving; redirect on closure | Donor intent as real business content; giving as a relationship not a transaction | **FG-4** |
| Karachi Zone 4; PKR and AED; Dubai donors; offline field conditions | Applicability context | **FG-5** |
| Face match + GPS + timestamped photo as proof of delivery | Evidence kinds and sufficiency thresholds for fulfilment | Cognition, §5.8 |
| Permanent human-readable ID with checksum; QR; temp offline ID reconciled on sync | Identity portability and assurance; the beneficiary's own access to their record (Art. IX) | Entities, FG-2 |
| Community vouching (max 3 per person) | Community attestation as an evidence kind with a stated limit | Evidence, Constraints |

**Two collisions the client should hear early**, both grounded in their own governing documents rather than my preference:

1. **Trust score as an aid gate.** A computed 0–1000 score that places beneficiaries in a "Restricted 0–199: receive aid only" tier sits against Constitution Article X — *"Humanitarian need shall be evaluated through evidence, never through assumptions about a person's or group's identity. Bias shall not be mitigated through protected-attribute rules or demographic scoring"* — and against Pillar P4's prohibition on unexplainable confidence scores. Trust as an *organisational* property earned through verified history is well supported (`organisation-partner-management` models it properly). Trust as a *number attached to a beneficiary that gates their access* is a different thing and is prohibited. This is fixable: replace the beneficiary score with evidence-based identity assurance and explicit verification state, which the repository already models well.

2. **">80% of operations without human review."** Article VIII permits automation below the consequence threshold and forbids it above, regardless of confidence. Several of the nine agents act above it — Fraud Agent auto-suspending at >85% confidence, Trust Agent auto-suspending at a threshold, Profile Update Agent auto-applying a new medical need at 94%. Each automated action class needs an explicit consequence-class determination, which is exactly what the Cognition layer exists to make representable. The client's own low-confidence path (<80% → volunteer confirms) shows the mechanism already exists; it is the threshold basis that needs to change from *confidence* to *consequence*.

**The constructive framing for the client conversation:** their blueprint is a good application design sitting on a knowledge foundation that is not yet finished. The repository is right that the foundation must come first. The client is right that the foundation has drifted away from the reality their product must serve. Both are fixable by the same work — B1 through B5 — and the client's blueprint is the best single source of Tier C evidence available for four of the five.

---

*End of assessment.*
