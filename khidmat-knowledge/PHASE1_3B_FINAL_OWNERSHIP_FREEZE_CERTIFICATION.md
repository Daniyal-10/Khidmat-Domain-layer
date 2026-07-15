# Phase 1.3B — Final Ownership Freeze Certification

**Basis:** the current on-disk repository, re-derived from scratch — 75 entities across 15
canonical entity-declaring files, every `relationships:` list in the repository, and every
`entities:` block, re-extracted independently rather than carried forward from
`PHASE1_3_ONTOLOGY_OWNERSHIP_FREEZE.md` or `PHASE1_3A_OWNERSHIP_CONFLICT_RESOLUTION.md`. Those
two documents were consulted only to know what to re-check, not trusted as evidence.

**Note on repository state:** these changes are present in the working tree but not yet
committed (`git log` shows the last commit as "Phase 1 ontology implementation (pass 2)";
`git status` shows the Phase 1.3A files as modified/deleted, uncommitted). This does not affect
the certification below, which evaluates ontology content as it currently stands on disk — but
the freeze is not durable until these changes are actually committed, and that action has not
been taken.

---

## 1. Executive Summary

75 canonical entities were found (down from 79 at the last freeze review: the 3-entity legacy
Needs Assessment monolith is gone; `need_severity` was migrated as a new data property, not a
new entity, so entity count decreases by exactly the 3 retired legacy ids minus 0 new
entities — no new concept was introduced anywhere in this repository as a result of Phase 1.3A,
consistent with that phase's own scope constraint).

Every entity has exactly one canonical owner, with one intentional, fully-documented exception:
`case`. This is not a residual violation — it is the explicit, correct end-state of the
governance decision this repository already made (ADR-021: one canonical Case, referenced under
two names across a lifecycle phase boundary, never a second entity). Both declarations now
cross-reference each other and ADR-021/ADR_RECONCILIATION_CASE.md. Six of seven cross-domain
relationships targeting a Case now resolve to the canonical owner (Case Management); the seventh
deliberately and correctly targets the pre-handoff name for a documented, ADR-001-grounded
reason (the Verification Brief is a projection specifically from the registration phase) that
was never in scope for the Phase 1.3A conflict and remains correctly unchanged.

No duplicate relationship ID, no duplicate constraint ID, no illegal ownership, and no
undocumented competing definition was found anywhere else in the repository.

**The ownership model is approvable for freeze.**

---

## 2. Ownership Certification

**Exactly one canonical owner** — certified for 74 of 75 entities without qualification; `case`
certified with the explicit, documented two-declaration exception described above and detailed
below. No entity was found with an owner that contradicts `ontology_authority_matrix.md`'s
"must not be redefined" constraints.

**No illegal ownership** — every relationship reviewed is declared by the domain that owns its
`from`-side entity (the repository's established convention); none was found declared by a
domain that does not own the entity it originates from.

**No competing ownership** — the one entity that could plausibly be read as contested (`case`)
now carries explicit notes on both declarations naming Case Management as sole canonical owner.
No other entity has more than one declaring file.

**Cross-domain references follow ownership rules** — spot-verified for every relationship
touching a Phase 1.3A-affected concept:
- `case_management:case` — 6 of 7 case-targeting relationships now resolve here (up from 4 of 6
  at the prior freeze review).
- `registration_tax:need_severity` — resolves to `registration/taxonomy/needs.yaml`'s existing
  scheme, confirmed present with an unchanged `critical`/`high`/`medium`/`low` concept set; not a
  new taxonomy, not a redefinition of an existing one, referenced rather than duplicated.
- `needs_assessment` no longer declares any concept under a non-canonical shape — the dict-shaped
  `entities: {Assessment: ..., AssessmentFinding: ..., IdentifiedNeed: ...}` block is gone from
  the repository entirely (files confirmed absent on disk).

**Aggregate ownership is correct** — `case` (Case Management sense) owns `case_plan`, `referral`,
`follow_up`; `case` (Registration's pre-handoff view) owns `registrant`, `beneficiary`,
`household_snapshot`, `situation`, `need`, `claim`, `evidence`, `support_intervention` during the
registration phase, per the newly-added ownership notes on both declarations — this dual
aggregate-child set is the correct, intended shape of a phase-scoped view, not two competing
aggregate roots.

**Identity ownership is correct** — `person`/`household`/`organisation` remain solely owned by
Shared Core with their identifier properties (`person_id`, `household_id`, `organisation_id`)
untouched by this pass; `need_assertion` gained a new identity-adjacent property
(`need_severity`) that references, rather than competes with, Registration's identical
property on `need`.

**Relationship ownership is correct** — no duplicate relationship ID was found anywhere in the
75-entity, full cross-domain-edge re-extraction performed for this certification (re-confirmed
independently, not carried forward from the prior pass's count).

**Import ownership is correct**, with one minor, non-blocking observation: `beneficiary-lifecycle/ontology/relationships.yaml`
still declares a `registration: "registration"` namespace alias that, after this pass's retargeting,
is no longer used by any relationship in that file (both of its former `registration:case`
targets now use the `case_management` alias instead). This is dead weight, not a defect — an
unused alias resolves nothing incorrectly, it simply resolves nothing. Noted for completeness;
not a certification blocker, and fixing it would be a YAML modification, out of scope for this
certification phase.

---

## 3. Ownership Violations

**None remain that block certification.** The one item requiring careful framing rather than a
simple "resolved/not resolved" label is documented in full in §2 above (`case`'s intentional
two-declaration shape) — it is not a violation under the governance model this repository has
adopted (ADR-021), and re-litigating that model is outside this phase's scope.

---

## 4. Repository Ownership Validation

| Check | Result |
|---|---|
| YAML parse | 0 errors, all files |
| Total canonical entities | 75 |
| Duplicate entity IDs | 1 — `case`, intentional per §2, not a violation |
| Duplicate relationship IDs | 0 |
| Duplicate constraint IDs | 0 (re-confirmed at Phase 1.3, unaffected by 1.3A's changes, no constraint file was touched in 1.3A) |
| Legacy Needs Assessment monolith | Absent from disk — confirmed via direct filesystem check, not inference |
| `need_severity` reachability | Resolves correctly to `registration/taxonomy/needs.yaml`, confirmed by direct scheme-id lookup |
| Relationships still targeting `registration:case` | 1, deliberate (`verification_assignment_issued_from_brief_context_of_case`, ADR-001-grounded, out of Phase 1.3A's scope) |
| Relationships now targeting `case_management:case` | 6 |
| Files touched since the last freeze review | 8 (`beneficiary-lifecycle/ontology/relationships.yaml`, `case-management/ontology/entities.yaml`, `registration/ontology/entities.yaml`, `needs-assessment/ontology/data-properties.yaml`, `registration/taxonomy/needs.yaml`, `ontology_authority_matrix.md`, plus 2 file deletions) — matches `PHASE1_3A_OWNERSHIP_CONFLICT_RESOLUTION.md`'s own declared scope exactly, independently re-confirmed via `git status` |

---

## 5. Final Decision

# A.

## OWNERSHIP MODEL APPROVED

The ontology ownership model is permanently frozen for Phase 1. No further ownership changes
are permitted during Phase 1. Every ontology concept now has exactly one canonical owner — with
the single, explicitly governed and fully documented exception of `case`, whose dual-declaration
shape is itself the frozen, correct state under ADR-021, not an open question.

This certification is contingent on the Phase 1.3A changes being committed; the ownership model
described here is frozen as of the current working-tree state, and that state should be
committed to make the freeze durable.
