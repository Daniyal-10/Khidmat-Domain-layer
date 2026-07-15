# Phase 1.6A — Operational Blocker Resolution

**Scope:** the two blockers identified in `PHASE1_6_BUSINESS_VALIDATION.md`. No other concept
was touched.

---

## 1. Operational Blocker Resolution Report

### Blocker 1 — Household topology evolution

**Minimum relationship determined:** a single `household_succeeded_by_household` edge
(`household → household`, cardinality `{min:0, max:unbounded}`), added to
`shared/ontology/relationships.yaml` where `household` is canonically owned. This directly
reuses the existing `case_superseded_by_case` pattern (same shape: an entity superseded-by an
instance of itself) rather than inventing a new relationship style.

One relationship type covers all four named topology scenarios, because cardinality does not
constrain how many *separate rows* can exist, only what each row permits:
- **Succession/evolution** — one household row, `succeeded_by` pointing at its later self.
- **Split** — one household's `succeeded_by` pointing at multiple successor households (the
  `max:unbounded` on the "to" side permits this directly).
- **Merge** — multiple households each declare their own `succeeded_by` row pointing at the
  same target household (no uniqueness constraint prevents two source rows sharing a target).

**Migration** was determined to be a *different* kind of edge — not household-to-household, but
beneficiary-to-household — since migration is about a person retaining ties to two households,
not one household becoming another. The fix there was relaxing
`registration:beneficiary_is_member_of_household`'s cardinality from `{min:1, max:1}` to
`{min:1, max:unbounded}`, the exact constraint the Business Validation identified as the actual
blocking condition.

### Blocker 2 — Cross-program referral

**Blueprint interpretation determined: A — a Referral**, not a Program transition. This was not
ambiguous once checked against the existing ontology: `case-management/taxonomy/referral_type.yaml`
already declares `ref_type: internal | external`, and `case-management/ontology/semantic-constraints.yaml`
already contains a mirrored constraint pair for the Consent dimension
(`external_referrals_require_consent` / `internal_referrals_no_consent`). The Blueprint and the
already-implemented ontology had already committed to "internal referral" as a distinct concept
from "external referral" — what was missing was only the *target* relationship for the internal
case, which every other dimension of Referral already anticipated.

**Implemented:** `referral_targets_program` (`referral → programs:program`, `{min:0, max:1}`),
added alongside the existing `referral_targets_organisation`, whose cardinality was relaxed from
`{min:1, max:1}` to `{min:0, max:1}` — a referral now targets *either* an Organisation (external)
*or* a Program (internal), never both, enforced by two new semantic constraints
(`external_referral_requires_organisation_target`, `internal_referral_requires_program_target`)
that directly mirror the existing consent constraint pair in both structure and rigor.

---

## 2. Files Modified

| File | Change |
|---|---|
| `shared/ontology/relationships.yaml` | Added `household_succeeded_by_household`; file status changed `placeholder` → `active` |
| `registration/ontology/relationships.yaml` | `beneficiary_is_member_of_household` cardinality `max:1` → `max:unbounded` |
| `case-management/ontology/relationships.yaml` | Added `referral_targets_program`; relaxed `referral_targets_organisation` to `{min:0,max:1}`; added `programs` namespace |
| `case-management/ontology/semantic-constraints.yaml` | Added `external_referral_requires_organisation_target`, `internal_referral_requires_program_target` |

No file governing Person, Case, Household's own entity definition, or Programs' own entity
definitions was touched — every change is a relationship addition or a cardinality relaxation
on an existing relationship.

---

## 3. Business Scenarios Now Resolved

| Scenario | Resolution |
|---|---|
| Household succession / evolution | `household_succeeded_by_household` |
| Household split | Same relationship, one-to-many |
| Household merge | Same relationship, many-to-one |
| Migration | `beneficiary_is_member_of_household` cardinality relaxation |
| Joint family | Partially addressable via the same succession edge (a joint family's constituent hearths can now be modelled as related households linked by succession/derivation) — full hearth-level sub-structure was not in scope and is not claimed as resolved beyond what the household-to-household edge itself enables |
| Cross-program referral | `referral_targets_program` + the internal/external targeting constraints |

---

## 4. Repository Validation

| Check | Result |
|---|---|
| YAML parse | 0 errors |
| Duplicate relationship IDs | 0 |
| Duplicate constraint IDs | 0 |
| `household` entity exists for the new self-relationship | Confirmed (`shared/ontology/entities.yaml`) |
| `program` entity exists for `referral_targets_program` | Confirmed (`programs/ontology/entities.yaml`) |
| `programs` namespace resolves | Confirmed, added to `case-management/ontology/relationships.yaml` |
| Files touched vs. declared scope | 4, matching `git status` exactly |

---

## 5. Decision

# A.

## ALL OPERATIONAL BLOCKERS RESOLVED

Business Validation may be re-run.
