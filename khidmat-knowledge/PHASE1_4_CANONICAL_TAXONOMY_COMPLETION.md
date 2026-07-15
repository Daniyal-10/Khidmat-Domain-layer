# Phase 1.4 — Canonical Taxonomy Completion

**Basis:** every `schemes:` block and every `taxonomy_ref` usage in the repository, re-extracted
mechanically before and after implementation. Ontology (entities, relationships, ownership) was
read only to determine what a taxonomy scheme classifies — none was modified.

---

## 1. Executive Summary

At the start of this pass: 200 unique taxonomy scheme IDs (202 scheme declarations, 2
collisions), 994 concepts, 167 `taxonomy_ref` usages with 18 unresolved (14 literal
`'# TODO Phase 5'` placeholders, 1 Blueprint-deferred, 1 self-inflicted-in-a-prior-pass
placeholder, 2 pointing at a non-canonically-shaped scheme).

After this pass: 210 unique scheme IDs (210 declarations, **zero collisions**), 1032 concepts,
167 `taxonomy_ref` usages with **3 unresolved**, all three deliberately deferred with an
inline rationale rather than left as silent gaps. Zero duplicate concept IDs within any scheme,
confirmed by exhaustive scan, not spot-check.

Ten of twelve originally-unresolved TODO placeholders were resolved — six by referencing an
already-existing canonical scheme (no new content authored, per this phase's "never duplicate
schemes" principle), four by authoring a new, narrowly-scoped scheme where no canonical
equivalent existed. One pre-existing structural gap (a scheme trapped in a non-canonical shape)
was normalized, resolving two further unresolved references as a side effect. Two duplicate
scheme IDs were resolved by renaming the non-consuming or more-recently-established declaration.
One new collision, introduced by this pass's own new scheme, was caught during validation and
fixed before delivery.

**Decision: PHASE 1 TAXONOMY COMPLETE**, with three named, correctly-deferred exceptions — none
of which is a Phase 1 blocker (detailed in §6).

---

## 2. Taxonomy Completion Report (Per Domain)

| Domain | Schemes Before | Schemes After | Status |
|---|---|---|---|
| Shared | 5 files, unchanged | unchanged | Complete — `location_precision`/`location_stability` now have consumers (previously authored, unreferenced) |
| Registration | 9 taxonomy files + 1 non-canonical (verification-requirements.yaml) | 9 + 1 now canonical | Complete except `evidence_subtype` and `functional_capacity` (deferred, §6) |
| Verification Operations | 8 files | unchanged | Complete — its two `priority_classification` references now resolve, without any change to this domain's own files |
| Needs Assessment | 4 files | unchanged file count; 1 scheme renamed | Complete — `need_severity` (added Phase 1.3A) confirmed still resolving; `finding_status` collision resolved |
| Case Management | 10 files | 11 files (+`follow_up_status.yaml`) | Complete — `follow_up_status` authored; `suspension_reason` collision resolved |
| Beneficiary Lifecycle | 4 files | unchanged | Complete — no gap found |
| Community Context | 12 files | unchanged | Complete — no gap found |
| Human Model | non-canonical, unchanged | unchanged | Not touched — `capabilities.yaml`'s non-canonical shape is what blocks `functional_capacity` (§6); resolving it is a structural migration, not a taxonomy-content gap, correctly out of this phase's scope |
| Risk | non-canonical, unchanged | unchanged | No taxonomy_ref in the repository targets any Risk taxonomy scheme unresolved; no gap found |
| Programs | 6 files | unchanged | Complete — no gap found; `suspension_reasons` (plural, programs) noted as a naming-convention inconsistency with `case_suspension_reason`/beneficiary-lifecycle's `suspension_reason`, not a collision (distinct IDs), not fixed (would be non-consensual renaming of an unrelated, already-working scheme, out of proportion to the actual problem) |
| Support Delivery | 7 files | unchanged | Complete — no gap found |
| Volunteer Operations | 9 files | unchanged | Complete — no gap found |
| Consent & Privacy | 1 file (non-canonical placeholder) | unchanged | Correctly minimal — Blueprint §16 marks this domain planned, not delivered; no taxonomy work indicated |
| Impact | 5 files | unchanged | Complete except `outcome_indicator` (deferred, §6, Blueprint §16) |

---

## 3. Modified Taxonomies

| File | Change |
|---|---|
| `registration/taxonomy/actors.yaml` | Added `gender`, `documentation_status`, `legal_status`, `registration_channel` schemes |
| `registration/taxonomy/lead-statuses.yaml` | Added `lead_review_decision` scheme |
| `registration/taxonomy/needs.yaml` | Added `income_frequency` scheme |
| `registration/verification/verification-requirements.yaml` | Normalized `priority_classification` from a flat, non-canonical list into a proper `schemes:` block — same content, no concept added, removed, or reworded |
| `needs-assessment/taxonomy/finding.yaml` | Renamed scheme `finding_status` → `need_assertion_status` (collision resolution) |
| `needs-assessment/ontology/data-properties.yaml` | Retargeted `finding_status` property's `taxonomy_ref` to `need_assertion_status` (property id unchanged) |
| `case-management/taxonomy/suspension_reason.yaml` | Renamed scheme `suspension_reason` → `case_suspension_reason` (collision resolution) |
| `case-management/ontology/data-properties.yaml` | `follow_up_status` note updated to reflect the scheme now exists |
| `impact/ontology/data-properties.yaml` | Added inline deferral rationale to `outcome_indicator` |
| `registration/ontology/data-properties.yaml` | 10 `taxonomy_ref` values fixed (see §5); 2 (`functional_capacity`, `evidence_subtype`) given inline deferral rationale instead of a bare TODO; `namespaces:` block added |

## 4. Added Taxonomies

| File | Scheme | Reason |
|---|---|---|
| `case-management/taxonomy/follow_up_status.yaml` (new file) | `follow_up_status` | Follow-up entity (added Phase 1.2) had no taxonomy scheme for its mandatory status property |
| `registration/taxonomy/actors.yaml` | `gender`, `documentation_status`, `legal_status`, `registration_channel` | Standard, low-risk demographic/process classifications with no existing canonical equivalent to reference |
| `registration/taxonomy/lead-statuses.yaml` | `lead_review_decision` | A volunteer review's decision is a narrower set (4 values) than `lead_statuses`' full 8-state machine; referencing the parent scheme would have permitted invalid values |
| `registration/taxonomy/needs.yaml` | `income_frequency` | No existing scheme covered payment cadence |

No new taxonomy scheme was authored for any concept requiring business/operational input not
yet available — consistent with the standing treatment of `support-interventions.yaml` and
`outcome_indicator` throughout this project's history.

## 5. Retired Taxonomies

None retired. Two schemes were **renamed** (not retired — their content and every existing
consumer relationship were preserved):
- `finding_status` (needs-assessment) → `need_assertion_status`
- `suspension_reason` (case-management) → `case_suspension_reason`

---

## 6. taxonomy_ref Validation Report

**167 total usages, 3 unresolved, all deliberately deferred:**

| Property | Domain | Reason Deferred |
|---|---|---|
| `impact.measurement.outcome_indicator` | Impact | Blueprint §16 marks the outcome-indicator vocabulary "Planned, not yet delivered." Authoring it now would mean inventing outcome categories ahead of the Blueprint's own sequencing. |
| `registration.beneficiary/household_member.functional_capacity` | Registration | Canonical source (`shared/human-model/taxonomy/capabilities.yaml#capability_levels`) exists but is trapped in a non-canonical shape (not a `schemes:` list) that `taxonomy_ref` cannot target without either restructuring an already-active file (redesign, out of scope) or duplicating its 4 concepts (forbidden). |
| `registration.evidence.evidence_subtype` | Registration | Canonical source (`shared/taxonomy/document-types.yaml`) exists but is split across 5 separate schemes with no single unified scheme id a `taxonomy_ref` could target; resolving requires a taxonomy-design decision on which scheme(s) apply, not a same-shape fix this pass could make unilaterally. |

**10 previously-unresolved references fixed:**

| Property | Fixed via |
|---|---|
| `beneficiary/household_member.gender` | New scheme |
| `beneficiary.documentation_status` | New scheme |
| `beneficiary.legal_status` | New scheme |
| `support_intervention.requested_duration` | Reference to existing `need_duration` |
| `case.registration_channel` | New scheme |
| `lead.registrant_persona` | Reference to existing `registrant_types` |
| `lead.lead_source` | Reference to existing `referral_types` |
| `volunteer_review.decision` | New scheme (`lead_review_decision`) |
| `beneficiary.location.precision` | Reference to existing `shared:location_precision` |
| `beneficiary.location.stability` | Reference to existing `shared:location_stability` |
| `household_snapshot.income.frequency` | New scheme |
| `need.cost_estimate.estimate_confidence` | Reference to existing `needs_assessment:confidence_level` |
| `case-management.follow_up.follow_up_status` | New scheme, new file |
| `verification-operations` × 2 (`requirement_priority`, `queue_priority`) | Fixed indirectly — the target scheme (`registration:priority_classification`) was normalized into canonical shape; zero change to verification-operations' own files |

---

## 7. Duplicate Scheme Resolution Report

| Duplicate | Resolution | Consumers Updated |
|---|---|---|
| `finding_status` (needs-assessment vs. verification-operations) | Renamed needs-assessment's to `need_assertion_status` — genuinely different concepts (need_assertion governance state vs. verification activity outcome) sharing a generic name, not true redundancy | 1 (`needs-assessment/ontology/data-properties.yaml`) |
| `suspension_reason` (beneficiary-lifecycle vs. case-management) | Renamed case-management's to `case_suspension_reason` — again genuinely different concepts (beneficiary-lifecycle suspension vs. case suspension) | 0 — confirmed via search that no `taxonomy_ref` anywhere targeted case-management's scheme by its old bare id before this rename |
| `review_decision` (registration's own new scheme vs. pre-existing verification-operations scheme) | **Caught during this pass's own validation, not pre-existing.** Renamed registration's newly-authored scheme to `lead_review_decision` before delivery | 1 (`registration/ontology/data-properties.yaml`, same edit that introduced it) |

No scheme was found to be a true content duplicate (same concept, same values, different
owner) anywhere in the repository — every collision found was two different real-world concepts
sharing a generic name, resolved by disambiguating the name rather than merging or choosing one
as authoritative over the other.

---

## 8. Cross-Domain Taxonomy Validation

Every new or retargeted cross-domain `taxonomy_ref` was confirmed by direct lookup, not
assumed:

- `registration_tax:need_severity` (needs-assessment → registration, added Phase 1.3A) — confirmed still resolving
- `shared:location_precision`, `shared:location_stability` (registration → shared) — confirmed present, previously authored but unreferenced
- `needs_assessment:confidence_level` (registration → needs-assessment) — confirmed present
- `registration:priority_classification` (verification-operations → registration) — confirmed resolving after the target file's shape normalization

No cross-domain reference was found pointing at a retired or renamed scheme without being
updated — both renames in §7 had their one real consumer (if any) updated in the same pass.

---

## 9. Repository Taxonomy Statistics

| Metric | Before | After |
|---|---|---|
| Total taxonomy scheme declarations | 202 | 210 |
| Unique scheme IDs | 200 | 210 |
| Duplicate scheme IDs | 2 | 0 |
| Total taxonomy concepts | 994 | 1032 |
| `taxonomy_ref` usages | 165 | 167 |
| Resolved references | 147 | 164 |
| Unresolved references | 18 | 3 |
| Duplicate concept IDs (within any scheme) | 0 (not previously checked exhaustively) | 0 (confirmed exhaustively) |
| Empty schemes (`schemes: []`) | 1 (`registration/taxonomy/support-interventions.yaml`) | 1 (unchanged — correctly deferred, Blueprint-blocked on programme-staff input, not touched) |

---

## 10. Final Decision

# A.

## PHASE 1 TAXONOMY COMPLETE

The three remaining unresolved `taxonomy_ref` values are not genuine Phase 1 blockers:

- `outcome_indicator` is explicitly out of Phase 1 delivery scope per the Business Blueprint
  itself (§16).
- `functional_capacity` and `evidence_subtype` both have a clear, already-identified canonical
  source; what blocks them is a structural shape question (a non-canonical file, and a
  multi-scheme target) that requires a decision beyond taxonomy content authoring, not missing
  taxonomy content. Both are documented inline with the exact condition that would resolve them.

`registration/taxonomy/support-interventions.yaml` remains empty, and remains correctly so —
its own header has stated since before this session began that it is blocked on operational
input from programme staff that the knowledge layer cannot invent, and nothing in this pass's
scope changes that.
