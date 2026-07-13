# Volunteer Operations — Foundation Design Report

> **Phase 2 (Foundation Authoring).** Companion to the Domain Audit and Migration
> Plan (`docs/architecture/Volunteer_Operations_Domain_Audit.md`,
> `Volunteer_Operations_Migration_Plan.md`). **Governing decision:** ADR-024.
> **Status:** Canonical (Foundational) — Operational Deferred.

---

## 1. Foundation Design Summary

Volunteer Operations now holds a canonical, single-owned **foundational** ontology
and taxonomy — the organization-invariant concepts every humanitarian
volunteer-management system requires — while the operational/runtime layer remains
deliberately deferred.

The domain models the volunteer as a **persistent, qualified operational
resource**: a `volunteer_profile` that attaches *behind* the shared `Actor` and
records what the volunteer is *fit for*. It does not model the volunteer as an
actor (that is Shared), the `volunteer` role label (Shared), or the act of
assigning work (the operational domains). This is the exact boundary the prior
audit settled (VO-6 / FLAG-006) and it is now expressed in authored YAML, not only
in prose.

### Classification of the candidate concepts (validated, not blindly accepted)

| Candidate | Verdict | Home |
|---|---|---|
| Volunteer | **Entity** `volunteer_profile` | VO (behind `shared:actor`) |
| Volunteer Team | **Entity** `volunteer_team` (structural grouping only) | VO |
| Volunteer Assignment | **Rejected as a VO entity** | The assignment ACT is owned by verification-operations / case-management (FLAG-006). VO models *eligibility* as a data property, not the act. |
| Skill | **Taxonomy** `skill_category` (coded data property) | VO |
| Certification | **Taxonomy** `certification_type` (coded data property; future-entity candidate) | VO |
| Availability | **Taxonomy** `availability_type` (kinds, not schedules) | VO |
| Language | **Value Object** `language_competency` = {language `xsd:string`, `language_proficiency`} | VO (proficiency scheme); identity as string |
| Coverage Area | **Taxonomy** `coverage_type` (mode); the *area* link is deferred cross-domain | VO / community-context (deferred) |
| Affiliation | **Taxonomy** `affiliation_type` + `affiliated_with → shared_org:organisation` | VO / Shared |
| Training Record | **Taxonomy** `training_status` only; the *record* is deferred | VO (status); Tier 2 (record) |
| Volunteer Status / Type | **Taxonomy** `volunteer_status`, `volunteer_type` | VO |
| Assignment Types | **Taxonomy** `assignment_type` (for eligibility) | VO |
| the `Actor` entity | **Belongs to Shared** — referenced, never redefined | shared/ontology |
| the `volunteer` role label | **Belongs to Shared** — referenced, never redefined | shared/taxonomy/persons |

### Entities vs. Value Objects vs. Taxonomies vs. Shared
- **Entities (2):** `volunteer_profile`, `volunteer_team`. Both pass the §17 test
  for entity-hood (referenceable, independently identifiable, own lifecycle).
- **Value Object (1):** `language_competency` — an owner-scoped {language,
  proficiency} bundle with no independent identity (§17).
- **Taxonomies (10 schemes across 9 files):** volunteer_status, volunteer_type,
  skill_category, certification_type, availability_type, assignment_type,
  coverage_type, language_proficiency, affiliation_type, training_status.
- **In Shared (referenced, not owned):** `actor`, `organisation`, the `volunteer`
  role label.

---

## 2. Architectural Decisions

1. **ADR-024 — Foundational Layer Precedes Operational Activation.** The governing
   decision: refines D-VO1 ("author nothing") into a two-tier rule — the
   organization-invariant foundation is authored now; the operational/runtime
   layer stays gated by the Stage-9 trigger. Introduces the *Canonical
   (Foundational) — Operational Deferred* maturity state and the four-part Scope
   Test. Refines D-VO3 (top-level skill/certification/language categories authored;
   organization-specific decomposition deferred).
2. **Volunteer modeled as `volunteer_profile` behind `shared:actor`** (not a new
   actor) — ADR-018, ADR-008, D-VO5, FLAG-006.
3. **The assignment act is not modeled** — eligibility (`eligible_assignment_type`)
   is authored; the act stays owned by the operational domains (FLAG-006).
4. **Language identity as `xsd:string`, proficiency as a taxonomy** — mirrors the
   established registration pattern; only the stable proficiency band is
   controlled.
5. **All predicates domain-local** — none promoted to shared (no second active
   domain uses them yet; §11).
6. **Coverage-area cross-domain link deferred to Phase 5** — the same manifest/C-2
   blocker that parks Registration and Community Context.

---

## 3. Files Created / Modified

**Created (16):**
- `volunteer-operations/ontology/entities.yaml`
- `volunteer-operations/ontology/data-properties.yaml`
- `volunteer-operations/ontology/relationships.yaml`
- `volunteer-operations/ontology/semantic-constraints.yaml`
- `volunteer-operations/ontology/lifecycle-constraints.yaml`
- `volunteer-operations/taxonomy/volunteer-classification.yaml`
- `volunteer-operations/taxonomy/skills.yaml`
- `volunteer-operations/taxonomy/certifications.yaml`
- `volunteer-operations/taxonomy/availability.yaml`
- `volunteer-operations/taxonomy/assignment-types.yaml`
- `volunteer-operations/taxonomy/coverage.yaml`
- `volunteer-operations/taxonomy/languages.yaml`
- `volunteer-operations/taxonomy/affiliation.yaml`
- `volunteer-operations/taxonomy/training.yaml`
- `volunteer-operations/governance.md`
- `volunteer-operations/discovery/foundation-report.md` (this file)
- `architecture-decisions/ADR-024-foundational-layer-precedes-operational-activation.md`

**Modified (5):**
- `volunteer-operations/README.md`
- `volunteer-operations/_placeholder.yaml` (ADR-004 shape retained; status +
  do_not_implement_until scoped to the operational layer)
- `ontology_authority_matrix.md` (VO owned-concepts section; FLAG-006 update)
- `knowledge_layer_roadmap.md` (Stage-9 narrowed to the operational layer)
- `architecture-decisions/README.md` (ADR-024 index entry)

---

## 4. Validation Results

- **Canonical Ontology Schema:** five-file module present; headers are top-level
  YAML keys (`version`/`domain`/`file`/`status`), `domain: volunteer_operations`
  (snake_case); `entities:` a list keyed by `id`, hierarchy via `parent` only
  (none needed); `data_properties:` property-centric, each with `domain` and
  exactly one of `datatype`/`taxonomy_ref`/`fields`; `language_competency` is a
  §17 value-object row; `relationships:` reusable predicates with
  `from`/`relationship`/`to`, `{min,max}` cardinality, `inverse` where a reverse
  row exists; one constraint expressed as the §9 target-neutral structure. ✔
- **Canonical Taxonomy Schema:** every file has the four-key header;
  `schemes:` → `concepts:` are lists keyed by `id`; every concept has
  `description`; no `type: enum`, no embedded `subtypes`, no bare scalar lists;
  cross-references use `references` entries with `scheme`/`relation`/`note`. ✔
- **Identifier uniqueness:** all ontology `id`s unique within `volunteer_operations`
  across entities/data-properties/relationship-rows/constraints; taxonomy concept
  ids unique within their scheme. ✔
- **Entity ownership / ADR-008:** no concept owned elsewhere is redefined; `actor`,
  `organisation`, and the `volunteer` role are referenced only. ✔
- **Relationship ownership / §11:** all predicates domain-local; none collides with
  a shared predicate (`shared/ontology/relationships.yaml` is an empty placeholder).
  ✔
- **Repository consistency:** the authored boundary matches the audit (VO-6),
  FLAG-006, and the verification-operations one-directional statement. ✔

A machine YAML-parse check is recorded in the delivery summary.

---

## 5. Remaining Operational Gaps (Tier 2 — deferred, gated by Stage-9)

- Scheduling, rota/roster construction, slot allocation.
- Dispatch, routing, matching, workload balancing, optimization.
- Trust / performance scoring (a runtime finding — ADR-023 §19).
- The assignment ACT and per-instance assignment history (owned elsewhere / runtime).
- Per-course training RECORD (courses, dates, expiry tracking).
- Organization-specific decomposition of skills / certifications / proficiency.
- The cross-domain coverage-area link to community-context geography (Phase-5 /
  manifest / C-2).

None of these is a knowledge-layer authoring task available now; each requires an
operational trigger, operations-staff input, the Runtime/Instance-State Schema, or
the cross-domain CURIE layer.

---

## 6. Readiness Score

**Foundational maturity: ~65% of full domain maturity.**

| Dimension | State |
|---|---|
| Ontology (foundational) | ✔ authored |
| Taxonomy (foundational) | ✔ authored |
| Ownership / governance | ✔ authored (matrix + governance.md + ADR-024) |
| Documentation | ✔ authored (README, foundation report) |
| Canonical conformance | ✔ against both frozen contracts |
| Scheduling / dispatch / optimization | ✖ deferred (Tier 2) |
| Trust / workload / runtime reasoning | ✖ deferred (Tier 2) |
| Operational policies | ✖ deferred (Tier 2) |

This is the intended stopping point: a canonical foundational domain with
operational behavior deliberately deferred.
