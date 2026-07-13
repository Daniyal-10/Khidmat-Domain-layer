# Khidmat Volunteer Operations — Governance and Documentation

**Authority:** Knowledge Layer Architect
**Source:** Companion governance document for `volunteer-operations/ontology/*.yaml`
and `volunteer-operations/taxonomy/*.yaml`
**Governing ADRs:** ADR-024 (Foundational Layer Precedes Operational Activation),
ADR-004, ADR-008, ADR-009, ADR-018, ADR-023
**Purpose:** Boundary-enforcement rules, the foundational/operational (Tier 1 /
Tier 2) split, cross-domain reference patterns, and flagged boundary cases for the
Volunteer Operations domain. Written as a standalone governance document so the
YAML files stay flat and mechanical while single-ownership (ADR-008) is enforced.

---

## Maturity: Canonical (Foundational) — Operational Deferred

Under ADR-024, this domain is authored in two tiers:

- **Tier 1 — Foundational (authored now).** The organization-invariant ontology
  and taxonomy: the `volunteer_profile` behind the shared Actor, the
  `volunteer_team` grouping, and the stable vocabularies that qualify a volunteer
  (status, type, skills, certifications, languages, availability kinds, coverage
  mode, assignment-type eligibility, affiliation, training status).
- **Tier 2 — Operational / runtime (deferred).** Scheduling, dispatch, routing,
  workload balancing, optimization, trust/performance scoring, the assignment
  ACT, per-instance assignment/training history, and any organization-specific
  decomposition of the foundational vocabularies. Gated by the Stage-9 activation
  trigger; not authored here.

Every concept authored now passes the ADR-024 Scope Test: organization-invariant,
no process/policy/algorithm, no runtime finding, single-owned.

---

## Boundary Enforcement Rules (per file)

### 1. `volunteer_profile` vs. the shared Actor and the `volunteer` role (ADR-008, ADR-018, FLAG-006)
- `volunteer_profile` (ontology/entities.yaml) owns the volunteer's
  **qualification/capacity profile** only.
- It **must not** redefine or duplicate the `Actor` entity
  (`shared/ontology/entities.yaml#actor`) or the `volunteer` role label
  (`shared/taxonomy/persons.yaml#person_roles.volunteer`). It attaches *behind* the
  Actor via `profile_of` (ontology/relationships.yaml), which is the sole link.

### 2. Fitness/eligibility vs. the assignment ACT (FLAG-006)
- Volunteer Operations owns **who is fit to be assigned** — expressed by the
  `eligible_assignment_type` data property over `assignment-types.yaml`.
- It **must not** own the **assignment event**: `VerificationAssignment`
  (verification-operations) and `CaseAssignment` (case-management) are the sole
  owners. No entity or relationship here models, duplicates, or points at the
  assignment act.

### 3. Classification vs. mutable operational state
- Taxonomy files classify **stable, immutable** kinds (availability *type*,
  coverage *mode*, skill *category*). Operational, mutable state (a concrete
  schedule, a live roster, current workload, a trust score) is **excluded** and
  deferred to Tier 2. This mirrors the Community Context "Exclusion of Mutable
  State" rule.

### 4. Skills vs. the Shared Human Model capability vocabulary (ADR-008)
- `skills.yaml#skill_category` classifies a volunteer's **task skills** (what work
  they can do). It **must not** redefine
  `shared/human-model/taxonomy/capabilities.yaml`, which classifies a person's
  **functional capacity** (a different concept). No overlap is authored.

### 5. Language identity vs. proficiency
- `languages.yaml` owns **only** `language_proficiency` bands. Language identity is
  an `xsd:string` on the `language_competency` value object — the repository does
  not maintain a controlled world-language vocabulary (registration models
  `language` as `xsd:string` for the same reason).

### 6. Affiliation kind vs. the organisation reference (ADR-008)
- `affiliation.yaml#affiliation_type` owns the **kind** of affiliation. The
  specific organisation is referenced via `affiliated_with → shared_org:organisation`
  (ontology/relationships.yaml); `shared/taxonomy/organisations.yaml` remains the
  sole owner of the organisation vocabulary.

---

## Cross-Domain Reference Patterns

### Pattern: Volunteer Profile → Shared Actor
The profile attaches behind the forward-declared `shared:actor` via `profile_of`
(cardinality 1:1). No second actor is minted; no reverse edge is authored in the
shared module (this domain does not own it).

### Pattern: Volunteer Profile → Shared Organisation
`affiliated_with → shared_org:organisation`, mirroring the community-context
precedent (`built_infrastructure_operated_by_organization`). The organisation
vocabulary is referenced, never redefined.

### Pattern: Volunteer Coverage → Community Context Geography (DEFERRED)
A volunteer's actual coverage AREA references community-context's
`geographic_hierarchy`. This cross-domain edge is **blocked on the repository-wide
manifest + C-2 ratified base IRI** — the same Phase-5 blocker that parks
Registration and Community Context. `coverage_mode` (the *mode*) is the authored
foundational stand-in; the area link activates with the CURIE layer.

---

## Ontology Boundary Rules

### 7. No operational workflow ownership
`volunteer_profile` and `volunteer_team` **shall not** own or originate scheduling,
dispatch, routing, workload distribution, or optimization. There are no outbound
edges to Case Management, Verification Operations, or Support Delivery workflows.
Volunteer Operations supplies *fitness/qualification* that those domains consume;
it does not model their process.

### 8. No runtime/reasoning findings in the ontology (ADR-023 §19)
Trust scores, performance ratings, workload signals, and assignment history are
reasoning-produced or per-instance runtime state. They are **not** authored as
entities, value objects, or data properties. Their representation is reserved for
the future Runtime/Instance-State Schema.

---

## Flagged Boundary Cases (domain-local; mirrored in `ontology_authority_matrix.md`)

### VO-FLAG-A: `certification` as a Future Entity Candidate
`certification` is authored today as a coded data property
(`certification_type`). Once Support Delivery / quality assurance need to
reference and re-validate a **specific** credential across time, it may meet the
Canonical_Ontology_Schema.md §17 promotion test and be reclassified as an Entity
(§20 Future Entity Candidate). Recorded here so the deferral is a tracked,
revisitable decision, not a silent default.

### VO-FLAG-B: `language_proficiency` promotion candidate
`language_proficiency` is single-owned here today. If a second domain needs a
spoken-language proficiency vocabulary, it is promoted to `shared/` under the
existing §11 governance (proposed, reviewed, references updated) — never copied.

### VO-FLAG-C: assignment-type eligibility vs. assignment act (FLAG-006)
The authoritative statement of this boundary is `ontology_authority_matrix.md`
FLAG-006. Recorded here for domain-local visibility: eligibility is VO's; the
assignment act is the operational domains'.
