# Phase 1.3A — Ownership Conflict Resolution

**Scope:** the two blockers identified in `PHASE1_3_ONTOLOGY_OWNERSHIP_FREEZE.md`. No other
concept was reviewed or touched.

---

## 1. Ownership Conflict Resolution Report

### Conflict 1 — Case ownership

Implemented the determination already recorded in `ADR_RECONCILIATION_CASE.md` (ADR-021
stands): the Case entity is canonical to Case Management and persists across the
Registration-to-Case-Management phase handoff; no second entity is created.

Concretely: Beneficiary Lifecycle's two relationships that targeted `registration:case`
(`lifecycle_transition_triggered_by_registration_case_case`,
`lifecycle_transition_triggered_by_case_decision_case`) now target `case_management:case`,
matching how Verification Operations already referenced the same canonical Case. Registration's
`case` entity entry was not deleted — ADR-021 explicitly rejected introducing a distinct
`RegistrationRecord` entity, and deleting the entry outright would have broken every
Registration-internal relationship that attaches claims, needs, evidence, etc. to it. Instead,
its description was extended with an explicit ownership note stating it is the pre-operational-phase
view of the single canonical Case owned by Case Management, not an independent entity. A
symmetric note was added to Case Management's own `case` entity, so both declarations
cross-reference each other and ADR-021/ADR_RECONCILIATION_CASE.md rather than standing as two
silent, potentially-contradictory claims.

### Conflict 2 — Needs Assessment legacy monolith

Reviewed `needs-assessment/ontology.yaml` and `needs-assessment/taxonomy.yaml` concept-by-concept
against the canonical `needs-assessment/ontology/` and `needs-assessment/taxonomy/` folders:

| Legacy concept | Disposition |
|---|---|
| `Assessment` | **Superseded** by `assessment_session` |
| `AssessmentFinding` | **Superseded** by `observation` + `need_assertion` (split across two canonical entities) |
| `IdentifiedNeed` | **Superseded** by `need_assertion` |
| `assessment_depth`, `assessment_urgency`, `assessment_methodology` | **Superseded** — identical scheme names already exist canonically in `needs-assessment/taxonomy/session.yaml` |
| `assessment_scope` (individual/household/community) | **Superseded** — re-expressed as the `session_evaluates_person`/`_household`/`_community` relationship trio plus the `community_scope_excludes_individual_household` semantic constraint, a strictly more expressive equivalent |
| `assessment_status` | **Superseded** by `session_status` (data property) and the `assessment_session` lifecycle-constraints state machine |
| `finding_confidence` | **Superseded** by `confidence_level` (`needs-assessment/taxonomy/evidence.yaml`) — same role (epistemic confidence in a finding), confirmed by direct comparison of both schemes' definitions |
| **`need_severity`** | **Unique — not superseded.** No canonical property or scheme carries this concept. Migrated (see §3). |

This determination was cross-checked against `needs-assessment/Needs_Assessment_Legacy_Migration_Dependency_Report.md`,
which had previously blocked retirement on three dependencies. Two of those three
(`verification-operations/taxonomy/verification-findings.yaml` and
`verification-operations/taxonomy/review-decisions.yaml`) were found, on inspection, to have
already been updated since that report was written — both now reference `need_assertion` and
contain zero remaining mentions of `AssessmentFinding` or `IdentifiedNeed` (confirmed by direct
grep). The third dependency (`registration/taxonomy/needs.yaml`'s `need_severity` placeholder)
was live and is resolved by this pass (§3). The report's fourth item
(`ontology_authority_matrix.md` synchronization) is resolved by §4.

**Disposition: B — unique content existed. Migrated, then retired.**

---

## 2. Files Modified

| File | Change |
|---|---|
| `beneficiary-lifecycle/ontology/relationships.yaml` | Two relationships retargeted `registration:case` → `case_management:case`; `case_management` namespace added |
| `registration/ontology/entities.yaml` | `case` entity description extended with an ownership note (no structural change) |
| `case-management/ontology/entities.yaml` | `case` entity description extended with a symmetric ownership note |
| `needs-assessment/ontology/data-properties.yaml` | Added `need_assertion.need_severity`, referencing `registration_tax:need_severity`; `registration_tax` namespace added |
| `registration/taxonomy/needs.yaml` | Comment on the `need_severity` scheme updated from "pending Phase 5 reconciliation" to reflect the reconciliation is complete — **no scheme content, ids, or values changed** |
| `ontology_authority_matrix.md` | Needs Assessment Domain section updated: legacy-monolith note changed from "not yet retired" to "retired," legacy concept list changed from "superseded, not yet retired" to a full disposition table, `need_severity` added to "Explicit References Only" |
| `needs-assessment/ontology.yaml` | **Deleted** |
| `needs-assessment/taxonomy.yaml` | **Deleted** |

No file outside this set of eight was touched. No entity, relationship, or taxonomy scheme was
redesigned — every change either retargets an existing relationship, adds a documentation note,
adds one new data property referencing an existing scheme, or removes files whose content was
verified fully accounted for elsewhere.

---

## 3. Exact Ontology Changes

**`beneficiary-lifecycle/ontology/relationships.yaml`:** `to: registration:case` → `to:
case_management:case` on both `lifecycle_transition_triggered_by_registration_case_case` and
`lifecycle_transition_triggered_by_case_decision_case`. `case_management: "case_management"`
added to `namespaces:`.

**`needs-assessment/ontology/data-properties.yaml`:** new entry —
```
- id: need_severity
  domain: need_assertion
  taxonomy_ref: registration_tax:need_severity
  cardinality: { min: 1, max: 1 }
```
`registration_tax: http://khidmat.org/ontology/registration/taxonomy` added to `namespaces:`.
This references, not duplicates, the existing `critical`/`high`/`medium`/`low` scheme already
authored in `registration/taxonomy/needs.yaml` — no new taxonomy scheme was created, satisfying
the "do not redesign taxonomy" constraint while still closing the content gap.

**`needs-assessment/ontology.yaml`, `needs-assessment/taxonomy.yaml`:** deleted in full.

---

## 4. Migration Impact

- **Beneficiary Lifecycle:** two relationship targets changed. No cardinality, no relationship
  id, and no other relationship in the file was affected. The change is a pure retarget — any
  consumer that was correctly resolving `registration:case` as "the canonical Case at its
  pre-handoff name" (which is how Verification Operations already treated it) sees no semantic
  difference, only a more direct reference.
- **Needs Assessment:** one new required property (`need_severity`, `min:1`) on `need_assertion`.
  This is an *addition* to the entity's contract, not a breaking change to any existing property,
  relationship, or lifecycle state — but it does mean any future instance data conforming to the
  prior canonical schema (without `need_severity`) would need this field populated to satisfy
  the new `min:1` cardinality. No instance data exists yet in this repository (knowledge layer
  only), so this has no migration cost today.
- **Registration:** zero structural impact — the `need_severity` scheme's `id`, `concepts`, and
  cardinality contract on `need.need_severity` are byte-identical to before this pass; only the
  explanatory comment changed.
- **Deleted files:** verified via repository-wide grep (both before and after deletion) that no
  YAML file anywhere referenced `needs-assessment/ontology.yaml`, `needs-assessment/taxonomy.yaml`,
  or any of their PascalCase concept ids. Deletion is a clean removal with zero dangling references.

---

## 5. Repository Validation

| Check | Result |
|---|---|
| YAML parse | 0 errors |
| Duplicate entity IDs | `case` still appears in two files — **by design**, see §6 |
| Cross-domain relationship resolution | 51 of 54 resolved by the automated checker; the 3 unresolved are the same pre-existing bare-word namespace convention (`shared_ontology`, `shared_risk` ×2) manually confirmed correct by direct file inspection in the prior verification pass — unrelated to and unaffected by this pass's changes |
| taxonomy_ref resolution | 167 total (+1, the new `need_severity` reference), 18 unresolved — unchanged count of unresolved refs; the one new reference resolves correctly (confirmed: `registration_tax:need_severity` → `registration/taxonomy/needs.yaml#need_severity`, which declares `critical`/`high`/`medium`/`low`) |
| Dangling references to deleted files | None found, before or after deletion |
| Files touched vs. declared scope | `git status` confirms exactly the 8 files listed in §2 |

---

## 6. Ownership Validation

**Case:** the entity id `case` is mechanically declared in two files, exactly as it was before
this pass, and exactly as ADR-021 prescribes ("No new entity is created; the Case persists
across this handoff" — meaning Registration's declaration was never meant to be deleted). What
changed is not the mechanical fact of two declarations, but the ownership *ambiguity*: before
this pass, the two declarations had no cross-reference and different descriptions with no
stated relationship between them, and two of Beneficiary Lifecycle's relationships pointed at
the pre-handoff name while everything else pointed at the canonical one. Now: both declarations
explicitly state Case Management is the sole canonical owner, both cross-reference ADR-021 and
each other, and every cross-domain relationship in the repository targeting a Case (6 total: 4
pre-existing to `case_management:case`, 2 now retargeted from `registration:case`) resolves to
the same owner. **The ownership question is resolved; the entity-id duplication is an
intentional, documented artifact of the accepted governance model, not an unresolved
violation.** A future stricter ownership validator would need to special-case
"same id, cross-referenced phase-view declaration" as distinct from "two competing,
undocumented definitions" — noted here as a tooling observation, not a remaining ontology issue.

**Needs Assessment:** zero duplicate concepts remain. `Assessment`/`AssessmentFinding`/`IdentifiedNeed`
and six other legacy concepts are gone; `need_severity` has exactly one owner (Registration,
referenced cross-domain, not redefined) and one consumer relationship
(`need_assertion.need_severity`). `ontology_authority_matrix.md` accurately reflects both.

---

## 7. Final Decision

# A.

## OWNERSHIP CONFLICTS RESOLVED

Ownership Freeze may now be re-run.
