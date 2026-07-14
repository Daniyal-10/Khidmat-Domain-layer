# Needs Assessment — Legacy Migration Dependency Report

## Purpose

Documents every currently-live dependency on the legacy monolith files
`needs-assessment/ontology.yaml` and `needs-assessment/taxonomy.yaml`, so that
these files are not deleted or merged while real references still target them.
No implementation or redesign is proposed here — this is a dependency inventory
only, produced in response to Repository Hardening Batch 2, item 6.

## Why the legacy files cannot simply be retired

The canonical `needs-assessment/ontology/` + `needs-assessment/taxonomy/`
folder defines a **different concept set** than the legacy monolith
(`assessment_instrument`, `assessment_session`, `need_assertion`,
`finding_status`, `need_urgency`, … vs. the legacy `Assessment`,
`AssessmentFinding`, `IdentifiedNeed`, `assessment_depth`, `finding_confidence`,
`need_severity`, …). The two are not a superseded/superseding pair — they are
two divergent models of the same domain, and the dependents below target
concepts that exist **only** in the legacy file. Deleting the legacy file today
would break every dependency listed here. Reconciling the two concept sets is a
content/ownership decision for a future pass, not a mechanical fix.

## Dependency Table

| Dependent File | Referenced Concept | Reference Form | Why Migration Is Blocked |
|---|---|---|---|
| `registration/taxonomy/needs.yaml` (lines 202–213) | `needs-assessment/taxonomy.yaml#need_severity` | Comment-documented placeholder: Registration authors its own local `need_severity` scheme (`critical/high/medium/low`) with an explicit comment marking it as temporary "pending Phase 5 reconciliation" with the legacy file | Registration's own migration plan (`Registration_Migration_Plan.md`, decision D5) explicitly defers this reconciliation to a future phase. `need_severity` does not exist under that name anywhere in the canonical `needs-assessment/` folder — the closest canonical concept is the `need_urgency` scheme in `needs-assessment/taxonomy/finding.yaml`, but no decision has been made on whether these are the same concept or two distinct ones. |
| `verification-operations/taxonomy/verification-findings.yaml` (line 46) | `needs-assessment/ontology.yaml#AssessmentFinding` | Structured `cross_references:` list entry, with prose noting `AssessmentFinding.based_on_verified_fact` consumes this file's `finding_status`-equivalent vocabulary | `AssessmentFinding` does not exist in the canonical folder. Canonical needs-assessment does not define an entity of that name — the nearest canonical analogue is `need_assertion` (`ontology/entities.yaml`), but `need_assertion` is not structurally identical to `AssessmentFinding` (different relationships, different owning properties), so this is not a safe like-for-like rename without a content review. |
| `verification-operations/taxonomy/review-decisions.yaml` (lines 153–160) | `needs-assessment/ontology.yaml#IdentifiedNeed.superseded_by` | Free-text design-rationale prose (illustrative precedent, not a structural field) | `IdentifiedNeed` does not exist in the canonical folder. This is a lower-severity dependency (it is commentary, not a resolvable structural reference), but it still names a legacy-only concept and would read as broken/undefined if the legacy file were removed. |
| `ontology_authority_matrix.md` (Needs Assessment Domain section) | `assessment_depth`, `assessment_urgency`, `assessment_scope`, `assessment_status`, `assessment_methodology`, `finding_confidence`, `need_severity`, `Assessment`, `AssessmentFinding`, `IdentifiedNeed` | Governance ownership table, `Authoritative File` column | These ten concepts are declared owned by the legacy monolith and have no equivalent entries for the canonical folder's concept set. Per Batch 2 scope, this table was intentionally left unmodified (item 6 instructs no merge/redesign); it remains an accurate record of the legacy file's current ownership, but it does not yet reflect the canonical folder's concepts at all — a separate synchronization gap, not a broken reference. |

## What would need to happen to retire the legacy files (not undertaken here)

1. A content-owner decision on whether each legacy concept (`need_severity`,
   `finding_confidence`, `AssessmentFinding`, `IdentifiedNeed`, `assessment_depth`,
   `assessment_urgency`, `assessment_scope`, `assessment_status`,
   `assessment_methodology`) maps onto an existing canonical concept, needs a new
   canonical concept authored, or is genuinely retired as out of scope.
2. Repointing the three dependent files above to the resulting canonical concept
   IDs.
3. Updating `ontology_authority_matrix.md`'s Needs Assessment section to the
   canonical file paths and concept IDs.
4. Only then deleting `needs-assessment/ontology.yaml` and
   `needs-assessment/taxonomy.yaml`.

None of the four steps above were performed in this pass. The legacy files
remain unchanged, per instruction.
