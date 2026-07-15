# KHIDMAT KNOWLEDGE LAYER — FINAL PHASE 1 FREEZE AUDIT (v2.0)

**Audit date:** 2026-07-15
**Basis:** Independent re-derivation from implemented YAML. All 171 YAML files parsed and
mechanically verified. No prior audit, report, or review was trusted or consulted as evidence.
**Blueprint role:** context only (`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`), used solely to
establish what a legitimate Phase 1 business scenario is.

---

## 1. Executive Summary

The Khidmat Knowledge Layer contains genuinely excellent humanitarian ontology thinking. The
family/household distinction, the situation-contextualises-need separation, claim epistemics,
and the verification-operations model are better than most production humanitarian data models
I have reviewed. The taxonomy work is broad, well-normalised, and — importantly — correctly
India-deployable while remaining country-neutral.

It cannot be frozen as Phase 1.

The reason is not missing scope. The blueprint's §16 deferrals (Programs, Support Delivery,
Impact, Volunteer runtime, Consent) are honestly declared and are **not** defects under this
audit's rules. The reason is that **the things the blueprint claims are already delivered do
not actually connect to each other.**

Three findings are decisive and independent of any roadmap opinion:

1. **There is no persistent human identity.** `registration:beneficiary` has **no identifier
   property at all** — while `case`, `need`, `claim`, `evidence`, `lead`, `situation`, and
   `household_member` all have one. No relationship anywhere links `beneficiary` to
   `shared:person` or `shared:subject`. Blueprint §5.1 states: *"A person is a persistent
   entity, not a per-case record… Every downstream promise about longitudinal reasoning rests
   on this principle."* The implementation is the exact inverse of its own foundational
   principle.

2. **`case` is defined twice with contradictory semantics**, and downstream domains have
   already split across the two definitions — `beneficiary-lifecycle` points at
   `registration:case`, `impact` points at `case_management:case`, and
   `verification-operations` points at **both**. The ambiguity is not theoretical; it has
   already propagated.

3. **55% of the repository's YAML bytes cannot participate in the knowledge graph.** The
   `shared/human-model/` and `shared/risk/` subtrees (14 files, 680 KB) declare no
   `namespaces` and no `entities`. They are unaddressable by CURIE. The `family` concept —
   which its own file says *"reasoning must reference"* — is referenced by exactly zero
   relationships in the entire repository.

A freeze now would permanently canonicalise an identity model that the blueprint itself
describes as wrong, and would guarantee breaking changes in Phase 2.

**Decision: NOT READY FOR PHASE 1 FREEZE.**

---

## 2. Repository Architecture Assessment

**Declared architecture (7 layers):** ontology → taxonomy → reasoning → questioning →
verification → readiness → gaps.

**Implemented reality:**

| Layer | Domains implementing it | Coverage |
|---|---|---|
| ontology/ | 11 of 12 | good |
| taxonomy/ | 10 of 12 | good |
| reasoning/ | **2 of 12** (registration, verification-operations) | 17% |
| questioning/ | **1 of 12** (registration) | 8% |
| verification/ | **1 of 12** (registration) | 8% |
| readiness/ | **1 of 12** (registration) | 8% |
| gaps/ | **1 of 12** (registration) | 8% |

Only `registration` implements the architecture the repository declares. Every other domain is
ontology + taxonomy only. This is defensible as sequencing — but it means the architecture is
currently a hypothesis proven in one domain, not a validated pattern.

**The two-schema split (structural, not stylistic):**

| Schema world | Files | Bytes | CURIE-addressable |
|---|---|---|---|
| Canonical (`version`/`domain`/`file`/`status`/`namespaces`/`entities`/`schemes`) | 156 | 560 KB | yes |
| Non-canonical (`ontology_version`/`authority`/`owner_domain` + bespoke keys) | **14** | **681 KB (55%)** | **no** |

8% of the files hold 55% of the knowledge and conform to a different schema with no
namespaces, no `entities:` list, and no `schemes:` list. A graph loader cannot ingest them
without a bespoke per-file adapter. This is the largest architectural liability in the repo.

**Namespace system:** there is no namespace *system*. The same logical prefix binds to
different things in different files:

- `registration` → `http://khidmat.org/ontology/registration` **and** `khidmat:registration:core` **and** bare `registration`
- `shared_org` → `http://khidmat.org/ontology/shared/organisations` (programs) **and** `shared/taxonomy/organisations.yaml` (community-context, volunteer-operations)
- `shared_human` → `http://khidmat.org/ontology/shared/human-model` (programs) **and** `shared/human-model/ontology/entities.yaml` (community-context) — **a file that does not exist**

Three IRI conventions are live simultaneously (`http://`, `https://`, `khidmat:x:core`), and
some prefixes bind to filesystem paths rather than IRIs — a category error.

**Repository DAG:** no import cycles were detected. Cross-domain dependency direction is
sensible. This is a genuine strength and is not among the blockers.

**Stale governance artifacts:** `_placeholder.yaml` files in `community-context/`, `impact/`,
and `programs/` all declare `status: not_yet_active` and `do_not_implement_until: …` while each
domain has a fully implemented 5-file `ontology/`. `impact/_placeholder.yaml` is directly
contradicted by `impact/ontology/`. These files now actively misinform any reader or agent.

**Score: 4/10**

---

## 3. Ontology Assessment

### What is genuinely correct

- **The family/household foundational distinction** (`shared/human-model/ontology/family-structure.yaml`)
  is excellent: family = relationships and obligations, persists through displacement;
  household = co-residence and shared economy, a snapshot. *"Registrations capture households.
  Reasoning must reference families."* This is a sophisticated, correct insight.
- **`situation` contextualises `need` rather than generating it** (ADR-002) — correct, and
  correctly implemented as `situation_contextualises_need {min:0}`.
- **Verification Brief as a projection, not an entity** (ADR-001) — correct and disciplined.
- **Claim epistemics** — `claim_basis` inherited from registrant (ADR-005), two-dimensional
  claim quality (ADR-003). This is genuinely good epistemic modelling that most systems omit.
- **`subject` as an abstract parent for person/household** — the right abstraction.
- **verification-operations** is the best-built domain: 7 entities, 24 relationships, a real
  reasoning layer, clean separation of activity/observation/finding/review.

### Incorrect identity modelling — the central defect

`registration/ontology/data-properties.yaml`, verified by enumeration:

| Entity | Has identifier? |
|---|---|
| `case` | **yes** (`case_id`) |
| `need`, `claim`, `evidence`, `situation`, `lead`, `volunteer_review`, `household_member`, `support_intervention` | yes |
| **`beneficiary`** | **NO** |
| **`household`** | **NO** |
| **`registrant`** | **NO** |

A Beneficiary is identified only by `name` (`xsd:string`, min 1 max 1). The two entities that
*must* persist for longitudinal reasoning are the two with no identity.

`shared/ontology/data-properties.yaml` is `status: placeholder` with `data_properties: []`, so
`person`, `subject`, and shared `household` have **zero properties** — including no identifier.
`shared/ontology/relationships.yaml` is also empty (`relationships: []`). The shared spine that
owns `subject`/`person`/`household`/`actor` is an empty shell: 4 of its 5 files are placeholders.

No relationship in the repository links `registration:beneficiary` → `shared:person` or
`shared:subject`. `beneficiary_lifecycle_tracks_journey_of_subject` tracks a `subject` that
registration never produces.

**Consequence:** the longitudinal spine is severed at its single most important joint.
Re-registration is handled by `previous_case_id: xsd:string` — a dangling string, not a
relationship, untraversable by any graph engine — plus `re_registration_reason: xsd:string`
with no taxonomy.

### Duplicate ownership — direct violation of the repo's own governance

ADR-008 ("Single Ownership of Concepts", **Accepted**) requires exactly one authoritative owner
per concept, maintained via `ontology_authority_matrix.md`. That matrix states:

> `| household | Household | shared/ontology/entities.yaml | Shared Ontology | Authoritative concept for households. **Must not be redefined.** |`

`registration/ontology/entities.yaml` redefines `household`. Verified violation.

Worse, there are **three mutually contradictory statements of who owns `household`**:
1. `ontology_authority_matrix.md`: owned by `shared/ontology/entities.yaml`, "must not be redefined"
2. `family-structure.yaml` `boundary_note`: *"The household entity is owned by the registration domain's ontology"*
3. The implementation: **both** define it, with different semantics (shared's has `parent: subject`; registration's does not)

Registration's `household` lacking `parent: subject` means that if registration's definition
wins, households fall out of the Subject hierarchy and `beneficiary_lifecycle` cannot track
them.

`case` is duplicated with genuinely contradictory meanings:

- `registration:case` — *"The structured record produced by a completed registration
  conversation… All other entities exist within it."* (`exactly_one`)
- `case_management:case` — *"The central, long-lived operational container coordinating
  holistic support for a Subject."*

These are different things. One is a per-conversation artifact; one is a lifetime container.
The split has already propagated: `beneficiary-lifecycle` → `registration:case`; `impact` →
`case_management:case`; `verification-operations` → **both**.

### Orphaned concepts

`family`, `family_member`, `family_entity` — 70 KB of the best ontology in the repository — are
referenced by **zero** relationships, because they have no entity id and no namespace. The file
that declares *"reasoning must reference families"* has made families unreferenceable.

Same for the entire risk model: `risk_characterization` is a top-level YAML key, not an entity.
Two domains (`beneficiary-lifecycle`, `verification-operations`) point relationships at
`shared_risk:risk_characterization`, which cannot resolve.

### Missing entity: Organisation

Four relationships across three domains range over `shared_org:organisation`:
`program_funded_by`, `program_implemented_by`, `built_infrastructure_operated_by_organization`,
`volunteer_profile_affiliated_with_organisation`. **`organisation` is not an entity anywhere.**
`shared/taxonomy/organisations.yaml` is a *taxonomy* of organisation *types*
(hospital_or_clinic, ngo_or_charity…). Four relationships range over a classification scheme as
if it were an entity — a category error. Organisation is a genuinely missing Phase 1 entity:
programs are funded and implemented by organisations, and referrals go to them.

**Score: 4/10** — outstanding conceptual work, broken structural spine.

---

## 4. Taxonomy Assessment

**This is the strongest part of the repository and should be preserved through any remediation.**

202 schemes across 10 domains. Semantic quality is high, descriptions are careful, and the
classification instincts are sound. Specific credit:

- `community-context/taxonomy/geographic-hierarchy.yaml` — country → region/state → district →
  **block/sub-district/tehsil** → cluster → municipality → village → ward →
  neighbourhood/hamlet. Correctly India-deployable *without* being India-coupled. The C3
  remediation note (removing `informal_settlement` as a geographic level because formality is
  orthogonal, owned by `settlement-types.yaml`) is exactly right thinking.
- `local-organizations.yaml` — `elected_community_council` covers Gram Panchayat,
  `micro_savings_and_credit_collective` covers SHGs, `womens_collective` covers Mahila Mandal.
  Neutral vocabulary, full India coverage.
- `shared/taxonomy/document-types.yaml` — `national_id` (Aadhaar maps cleanly), `ration_card`
  explicitly present, `voter_registration_card`, `government_benefit_letter`.
- `verification-operations` taxonomy (8 files, 63 KB) is thorough and well-governed, with
  explicit `scope`/`out_of_scope`/`design_notes`.
- `human-model` taxonomies (health-conditions 278 KB, capabilities 80 KB, lifecycle-stages
  36 KB) are unusually rich.

**Defects:**

1. **`registration/taxonomy/support-interventions.yaml` is `schemes: []`** — empty,
   `status: placeholder`, `do_not_implement_until: operational catalogue confirmed`. See
   Blocker B-4 — this collides with a mandatory ontology cardinality.
2. **Duplicate scheme ids across domains break bare-reference resolution.** 155 of 165
   `taxonomy_ref` usages are **bare** (unprefixed), which only works if scheme ids are globally
   unique. They are not:
   - `finding_status` — defined in **both** `needs-assessment` and `verification-operations`,
     and **both** domains reference it bare. A resolver cannot disambiguate.
   - `suspension_reason` — defined in `beneficiary-lifecycle` **and** `case-management`; a
     third variant `suspension_reasons` (plural) in `programs`. Three concepts, near-identical
     names, no shared parent.
3. **17 unresolved `taxonomy_ref`s**, including **14 literal `taxonomy_ref: '# TODO Phase 5'`**
   shipped as quoted string data in `registration/ontology/data-properties.yaml` — the
   foundation domain. Also `impact:outcome_indicator` (no such scheme) and
   `registration:priority_classification` ×2 (no such scheme).
4. **Reference style is inconsistent** — `beneficiary-lifecycle` uses prefixed refs;
   `case-management`, `community-context`, `programs`, `registration`, `support-delivery`,
   `volunteer-operations` use bare; `needs-assessment` and `verification-operations` mix both.
5. **Granularity asymmetry** — `health-conditions.yaml` is 278 KB while
   `case-management/taxonomy/referral_type.yaml` has two concepts (`internal`, `external`). The
   depth of investment does not track operational importance.

**Score: 7/10** — the best asset here; fix the plumbing, keep the content.

---

## 5. Reasoning Assessment

Present in **2 of 12 domains** (plus `shared/risk/reasoning/compound-risk-detection.yaml`).

Where it exists, quality is good: `registration/reasoning/` (severity, inference, gap-detection,
case-coherence, evidence) and `verification-operations/reasoning/` (confidence composition,
contradiction detection, escalation, reverification, completeness) are thoughtfully constructed
with declared `inputs`/`outputs`/`governance`.

Where it does not exist, it matters:

- **`case-management` has no reasoning** — yet case planning, prioritisation, and closure are
  the core of NGO operations.
- **`beneficiary-lifecycle` has no reasoning** — yet lifecycle transitions *are* longitudinal
  reasoning.
- **`needs-assessment` has no reasoning** — yet need severity and prioritisation are its purpose.

`shared/risk/reasoning/compound-risk-detection.yaml` references
`protective-factors.yaml#protective_factors.extended_family_support_active` — a **file-anchor
path, not a CURIE**. Reasoning in the non-canonical world addresses concepts by filesystem
location. This will not survive any refactor and cannot be executed by a rule engine operating
on a graph.

**Score: 3/10** — good where present, absent in 9 of 12 domains, and the non-canonical rules
are not executable against the canonical graph.

---

## 6. Business Simulation Results

Simulated using only implemented ontology + taxonomy + reasoning, against blueprint scenarios.
"Representable" means the graph can express it; "AI-reasonable" means rules/relationships exist
to act on it.

### Fully representable

| Scenario | Notes |
|---|---|
| Registration (single beneficiary) | Blocked only by B-4 (`support_intervention` min 1, empty taxonomy) |
| Proxy registration | Strong — `registrant_type: proxy` + `relationship_to_beneficiary` + `proxy_consent` enforced by `required_if` constraints. Genuinely well done. |
| Widow | `beneficiary` + `household` + `household_member` + `situation(trigger_event)`; `death_certificate` in evidence |
| Orphan | `member_is_guardian_of_member` + `non_resident_guardian` value object. The ADR-023 note on inferring guardian residency from which representation is populated is elegant. |
| Disabled beneficiary | `functional_capacity` + `capabilities.yaml` + `health-conditions.yaml` (rich) |
| Medical emergency | `situation.trajectory: acute` + `trigger_event` + `safety_flag` (ADR-006: triggers assessment, not closure — correct) |
| Flood / fire / earthquake | `hazard-categories.yaml` + `community-hazards.yaml` + `seasonal-events.yaml` — strong |
| Urban slum / tribal village | `settlement-types.yaml` + `geographic-hierarchy.yaml` + `remoteness` — strong |
| Food insecurity / education / health / livelihood | `need_categories` + `livelihood-patterns.yaml` |
| Verification / failed verification | Best-modelled flow in the repository |
| Fraud suspicion | `information_consistency` + contradiction-detection rules + `escalation-reasons.yaml` |
| Multiple simultaneous needs | `case_has_needs {min:1,max:unbounded}` + `need_severity` |
| Compound vulnerability | `compound-risk-detection.yaml` — good content, but see B-7 (unaddressable) |
| Community intervention | `community-context` ontology is solid |

### NOT representable — with the single missing concept named

| Scenario | Single missing semantic concept |
|---|---|
| **Returning beneficiary** | **Persistent Person identity.** `beneficiary` has no id; no `beneficiary → person` link. Cannot assert two registrations are the same human. |
| **Re-registration** | Same. `previous_case_id` is an untraversable `xsd:string`, not a relationship. |
| **Longitudinal beneficiary journey** | Same. `beneficiary_lifecycle` tracks `subject`; registration produces `beneficiary`; nothing joins them. |
| **Household evolution** | **Persistent Household identity.** `household` has no id and no `household → household` succession relationship. |
| **Duplicate registration** | Person identity + a resolution relationship. `case_superseded_by_case` exists only in `case-management`, over the *other* `case` concept. Registration has no case→case link. |
| **Impact evaluation** | Person identity. `impact_has_baseline_measurement` / `endline` exist, but with no persistent subject there is nothing to measure change *on*. `taxonomy_ref: outcome_indicator` is also unresolved. |
| **Government referral** | **Referral target.** `referral` has only `ref_status` and `ref_type ∈ {internal, external}`. No `referred_to`, no reason, no outcome, no scheme identity. |
| **NGO referral** | Same — indistinguishable from a government referral; both are `external`. |
| **Follow-up** | **Follow-up as an entity.** Modelled as `type: string` inside the `case_timeline` value object. No due date, assignee, status, or outcome. |
| **Monitoring** | Same — `case_note: string`. No author, timestamp, or type. Nothing to reason over. |
| **Community recovery** | Temporal community state. `community` has no state history or recovery trajectory. |
| **Multi-program support** | Deferred per blueprint §16 — **not counted as a defect.** |
| **Volunteer assignment / support delivery / programme enrolment** | Deferred per blueprint §16 — **not counted as a defect.** |

### Structural cardinality limits observed

- `beneficiary: exactly_one` and `household: exactly_one` per case. A **joint family** with
  separate hearths sharing one compound must be forced into either one coarse household or
  N disconnected cases — there is no `household ↔ household` relationship and no
  hearth/sub-household concept. Given India is the target deployment, this is a real
  limitation, though workable at coarse grain (rated HIGH, not blocker).
- `beneficiary_is_member_of_household {min:1,max:1}` forbids dual household membership —
  **migration** (member of origin household + destination household) cannot be represented.
  Rated HIGH.
- `lead: required, exactly_one` per case forces every case through the lead pipeline, while
  `case_management.case_origin` offers 8 origins including `self_request` and `walk-in`-style
  paths. The two domains disagree about how cases begin.

---

## 7. Humanitarian Coverage

Broad and thoughtful. Vulnerability, exposure, hazard, resilience, protective factors,
capabilities, dependency, lifecycle stages, health (incl. SAM/MAM clinical staging) are all
modelled with real domain understanding. The insight that *"two households with the same need
are not equally vulnerable if one can absorb the shock and the other cannot"* is implemented,
not just stated.

Gaps that matter for humanitarian practice:

- **No beneficiary feedback / grievance mechanism.** Blueprint §16 lists it as planned
  ("principle stated here; mechanism to follow"), so **not counted as a blocker** — but for a
  national-scale humanitarian platform, accountability-to-affected-populations is close to a
  licence-to-operate requirement. Flag for Phase 2 priority.
- **No do-no-harm / protection-incident concept** beyond `safety_flag` + `safety_notes`.
- **Referral outcome is unrepresentable**, so the NGO cannot know whether anyone it referred
  ever received help. For a referral-heavy Indian NGO this is a significant operational blind
  spot.

**Score: 6/10**

---

## 8. India Readiness

**I found no *essential* India concept missing from the taxonomy**, and I want to be explicit
that the absence of literal `Aadhaar`, `Panchayat`, `MGNREGA`, or `BPL` strings is **not** a
defect — it is correct neutrality with correct coverage:

- Aadhaar → `national_id`; ration card → `ration_card` (explicitly present); voter card →
  `voter_registration_card`
- Gram Panchayat → `elected_community_council`; SHG → `micro_savings_and_credit_collective`
- Tehsil/block → `block` (labelled "Block / Sub-District / Tehsil")
- Tribal → `minority_or_indigenous_advocacy_group` + `settlement-types` + `remoteness`
- Multiple languages → `beneficiary.language` + `volunteer-operations/taxonomy/languages.yaml`

This is a well-executed neutral-core design. Real India gaps:

1. **Government scheme linkage is unrepresentable** (referral has no target). The single
   highest-value function of an Indian NGO — connecting a widow to a widow pension, a family to
   Antyodaya, a patient to Ayushman Bharat — cannot be recorded. This is a genuine Phase 1 gap,
   surfacing as B-9.
2. **Migration** — `beneficiary_is_member_of_household {max:1}` cannot express a member split
   across origin and destination households. Migration is central to Indian poverty.
3. **Joint family** — no hearth/sub-household concept (see §6).
4. **DPDP** — `consent-and-privacy` is a 241-byte placeholder whose single entity `Consent` is
   PascalCase while `case-management` references it as lowercase `consent`, so the reference is
   broken. DPDP Act compliance requires consent purpose, scope, retention, and withdrawal.
   Blueprint §16 declares Consent planned, so this is **not counted as a blocker** — but it is
   a legal gate for Indian deployment and must not be frozen in this state.
5. **Caste** — near-absent (1 file). This is defensible as deliberate neutrality/dignity design
   and I am **not** classifying it as a defect, but it should be a conscious, documented
   decision, since targeting and reservation-scheme eligibility often require it.

**Score: 6/10** — good neutral design; blocked operationally by referral targeting, not by vocabulary.

---

## 9. AI / Knowledge Graph Readiness

| Capability | Status |
|---|---|
| Knowledge Graph load | **Fails.** 55% of bytes have no namespaces/entities; 12 broken cross-domain refs; 2 duplicate entity ids. |
| GraphRAG | **Fails.** `family`, `vulnerability`, `risk`, `capabilities`, `protective_factors` — the richest retrieval content — are unreachable by CURIE. |
| Semantic search | Partial. Descriptions are high-quality and would embed well; the graph structure behind them would not resolve. |
| LLM grounding | Unsafe. An LLM asked "has this person been helped before?" cannot be grounded — no persistent identity. It would hallucinate or answer from `name` string matching. |
| Rule engines | Partial. Registration + verification rules are executable; `compound-risk-detection.yaml` addresses concepts by file-anchor path and is not. |
| Decision support / case recommendation | Fails. No `case-management` reasoning; `case` is ambiguous. |
| Planning / agentic AI | Fails. No follow-up entity, no referral target, no intervention taxonomy — an agent has no action vocabulary. |
| Longitudinal reasoning | **Fails.** The severed identity spine. |

The bare-`taxonomy_ref` convention (155 of 165) combined with proven non-unique scheme ids
(`finding_status`, `suspension_reason`) means an automated resolver produces **silently wrong**
resolutions rather than errors. That is worse than a hard failure.

**Score: 3/10**

---

## 10. Phase 2 Readiness

The ADR culture (23+ ADRs), authority matrix, roadmap, and inventory are real assets — the
repository knows how to make and record decisions. Domain boundaries are drawn sensibly and the
DAG is acyclic.

But the concepts that must be corrected are **foundational, not peripheral**: person identity,
case semantics, household ownership. Freezing now does not defer this cost — it converts it
from a Phase 1 fix into a Phase 2 breaking migration touching every domain, plus every
instance record created in the interim.

**Score: 5/10**

---

## 11. Verified Strengths

1. Family/household foundational distinction — genuinely excellent ontology.
2. Claim epistemics (ADR-003, ADR-005) — claim basis inherited from registrant; two-dimensional
   claim quality. Rare and correct.
3. Verification Brief as projection, not entity (ADR-001) — disciplined.
4. `situation` contextualises `need` (ADR-002) — correct causal modelling.
5. `safety_flag` triggers assessment, not automatic closure (ADR-006) — humane and correct.
6. Geographic hierarchy — India-deployable, country-neutral, with the correct orthogonality fix.
7. verification-operations — the reference implementation for the whole repo.
8. Proxy registration — `required_if` constraints properly enforce relationship + consent.
9. Household resilience (absorptive/adaptive/recovery) — real humanitarian sophistication.
10. Acyclic, sensibly directed cross-domain dependency graph.
11. Strong ADR and governance culture.
12. All 171 files parse cleanly — no YAML syntax debt.

## 12. Verified Weaknesses

1. Two incompatible schema worlds; 55% of bytes non-canonical.
2. No namespace system — same prefix, different bindings, three IRI conventions, prefixes bound
   to file paths.
3. Reasoning in 2 of 12 domains; questioning/readiness/gaps/verification in 1 of 12.
4. 155 of 165 `taxonomy_ref`s bare, with proven id collisions → silent misresolution.
5. 14 `taxonomy_ref: '# TODO Phase 5'` literals in the foundation domain.
6. Stale `_placeholder.yaml` files contradicting implemented domains.
7. Granularity asymmetry (278 KB health taxonomy vs 2-concept referral_type).
8. `shared/` spine is 4/5 placeholders; `shared/vocabulary/controlled-terms.yaml` parses to
   `None` (comments only).
9. Four "forward-declared" placeholder entities in `shared` (`actor`, `assessment_tool`,
   `humanitarian_sector`, `intervention_type`) carry 8+ live relationships from 5 domains.
10. `case_note` / `follow_up` typed as bare `string`.

## 13. Verified Missing Concepts (Phase 1 only)

Each blocks a scenario the blueprint describes as in-scope:

1. **Persistent Person identity** — `beneficiary` as per-case snapshot bound to a durable
   `person`. (Blueprint §5.1 declares this foundational.)
2. **Persistent Household identity** — `household_id` + household succession/evolution.
3. **Organisation** — as an *entity*, not a type taxonomy. 4 relationships already depend on it.
4. **Referral target + reason + outcome** — `referral → organisation` / government scheme.
5. **Follow-up** — as an entity with due date, assignee, status, outcome.
6. **Case-to-case succession in registration** — a real relationship, not `previous_case_id: string`.
7. **Support intervention taxonomy** — mandated at `min:1` by the ontology but empty.

## 14. Verified Missing Domains (Phase 1 only)

**None.** Every domain the blueprint requires for V1 exists in some form. The deferred domains
(Programs, Support Delivery, Impact, Volunteer runtime, Consent) are declared in blueprint §16
and are **correctly excluded** from this audit's defect list. The problem is depth and wiring
inside existing domains, not absent domains.

## 15. Edge Cases That Cannot Be Represented

1. Same widow registering in 2024 and 2026 — cannot be linked.
2. Joint family, separate hearths, one compound — no hearth concept, no household↔household link.
3. Migrant labourer in origin + destination household — `max:1` membership forbids it.
4. "Was this family helped before, and did it work?" — the core longitudinal question.
5. Referral to a government scheme with an outcome.
6. A scheduled follow-up with an owner and a due date.
7. Two field workers disagreeing across domains on `finding_status` — ambiguous resolution.
8. Community recovery trajectory over time.
9. A case that is a lifetime container *and* a registration record — the `case` collision.
10. Consent withdrawal under DPDP.

## 16. Freeze Risks

| Risk | Severity |
|---|---|
| Identity model frozen as the inverse of blueprint §5.1; every longitudinal promise voided | **Critical** |
| `case` ambiguity canonicalised while 3 domains already point at different definitions | **Critical** |
| `household` frozen in violation of the repo's own authority matrix and ADR-008 | **Critical** |
| 680 KB of the best content permanently outside the graph | **Critical** |
| Phase 2 forced into breaking migrations across all 12 domains + all instance data | High |
| GraphRAG/LLM grounding built on silently-misresolving bare refs | High |
| DPDP consent frozen as a broken 241-byte placeholder | High (legal) |

## 17. Scores

| Dimension | Score |
|---|---|
| Architecture | 4/10 |
| Ontology | 4/10 |
| Taxonomy | **7/10** |
| Reasoning | 3/10 |
| Humanitarian | 6/10 |
| India | 6/10 |
| AI / Knowledge Graph | 3/10 |
| Extensibility | 5/10 |
| **Overall** | **4.5/10** |

## 18. Final Decision

# NOT READY FOR PHASE 1 FREEZE

## 19. Genuine Release Blockers

Ordered by severity. Each is mechanically verified and each blocks a blueprint-described Phase 1
scenario. Roadmap items and blueprint §16 deferrals are deliberately **excluded**.

**B-1 — No persistent Person identity.** `beneficiary` has no identifier; no relationship links
it to `shared:person`/`subject`; `shared` has zero data properties. Blueprint §5.1 declares
persistent identity the foundation of the system. Blocks: returning beneficiary, re-registration,
longitudinal journey, impact measurement, household evolution, duplicate detection.
*Fix:* give `person` a durable identifier; make `beneficiary` a per-case snapshot with
`beneficiary_observes_person → shared:person`; add `person_id`/`household_id`.

**B-2 — `case` is defined twice with contradictory semantics.** `registration:case` (per-conversation
record) vs `case_management:case` (long-lived container). Three domains already point at
different definitions; `verification-operations` points at both.
*Fix:* rename one (e.g. `registration:registration_record`) and define the succession
relationship between them.

**B-3 — `household` redefined in violation of ADR-008 and `ontology_authority_matrix.md`**, with
three contradictory ownership statements across matrix, `family-structure.yaml`, and code.
*Fix:* pick one owner, delete the other definition, reconcile the matrix and the boundary note.

**B-4 — The ontology mandates an entity whose taxonomy is empty and deferred.**
`case_has_support_interventions {min:1}` and `need_addressed_by_intervention {min:1}` are
required, but `registration/taxonomy/support-interventions.yaml` is `schemes: []`,
`status: placeholder`, `do_not_implement_until: operational catalogue confirmed`. **No
registration case can be validly instantiated.** Blueprint §16 concedes this taxonomy is
blocked on programme staff.
*Fix:* relax to `min:0` for Phase 1, or land a minimal intervention taxonomy. Do not freeze a
contract the repository cannot satisfy.

**B-5 — `needs-assessment` ships two parallel contradictory ontologies.** The legacy monoliths
`needs-assessment/ontology.yaml` + `taxonomy.yaml` (PascalCase `Assessment`, `AssessmentFinding`,
`IdentifiedNeed`, `khidmat:x:core` CURIEs) coexist with the canonical modules (snake_case
`assessment_session`, `need_assertion`, `observation`, URI namespaces). Any loader walking the
domain ingests both. `case-management` got its `retire legacy monoliths` commit (bdf9b52);
`needs-assessment` did not. The migration is half-finished.
*Fix:* delete the monoliths.

**B-6 — 12 of 49 cross-domain references (24%) do not resolve.** Includes 4 refs to
`shared/human-model/ontology/entities.yaml`, **a file that does not exist**;
`community_context:location` (no such entity); `consent_and_privacy:consent` (entity is
`Consent`); `shared_risk:risk_characterization` ×2 (not an entity); `shared_org:organisation` ×4
(**never defined — a genuinely missing Phase 1 entity**).

**B-7 — 55% of YAML bytes cannot enter the knowledge graph.** `shared/human-model/` and
`shared/risk/` (14 files, 681 KB) declare no `namespaces` and no `entities`. `family` — which
its own file says reasoning must reference — has zero inbound references.
*Fix:* migrate to canonical schema, or ratify an adapter + base IRI. This need not be
beautiful, but it must be addressable.

**B-8 — 17 unresolved `taxonomy_ref`s in the foundation domain**, incl. 14 literal
`'# TODO Phase 5'` strings, plus ambiguous bare refs to the colliding `finding_status` and
`suspension_reason` ids.

**B-9 — `referral` has no target, reason, or outcome.** Only `ref_status` and
`ref_type ∈ {internal, external}`. Government referral and NGO referral — both explicitly
required Phase 1 scenarios — are indistinguishable and untargetable. For an Indian NGO this
voids the highest-value workflow.

---

### What is explicitly NOT a blocker

To be unambiguous, none of the following counted against this audit:

- Programs, Support Delivery, Impact, Volunteer Operations runtime, Consent & Privacy depth —
  all declared as planned in blueprint §16.
- Absence of literal Aadhaar/Panchayat/MGNREGA vocabulary — correct neutrality with correct
  coverage.
- Predictive engines, donor matching, resource optimisation, trust scoring, biometrics,
  runtime/orchestration — blueprint §17 out-of-scope.
- Beneficiary feedback/grievance — §16 planned (flagged as Phase 2 priority, not a Phase 1 defect).
- Absence of caste modelling — reads as a deliberate dignity/neutrality decision.

---

## 20. Path to Freeze

The repository is closer than the score suggests. The taxonomy — the most labour-intensive
asset and the hardest to get right — is genuinely good and should survive remediation almost
untouched. The blockers are concentrated in **wiring and identity**, not in humanitarian
understanding.

Ordered remediation:

1. **B-1 + B-2 + B-3** — settle identity and ownership. One decision session: what is a Person,
   what is a Case, who owns Household. This unblocks 6 of the 10 unrepresentable edge cases.
2. **B-5 + B-6 + B-8** — delete the needs-assessment monoliths; define `organisation`; ratify a
   single base IRI and namespace registry; make every `taxonomy_ref` prefixed. Largely
   mechanical, and a CI validator (essentially the checks run in this audit) should be committed
   to prevent regression.
3. **B-4 + B-9** — relax the `support_intervention` cardinality; give `referral` a target.
4. **B-7** — migrate or adapt human-model + risk into addressability.

The single highest-value validation step remains proving one vignette — a widow registered,
verified, planned, supported, followed up, re-registered two years later, and measured —
end-to-end through the implemented YAML. Every blocker above would have surfaced from that one
exercise, and none of them would survive it.

---

*End of Phase 1 Freeze Audit v2.0.*
