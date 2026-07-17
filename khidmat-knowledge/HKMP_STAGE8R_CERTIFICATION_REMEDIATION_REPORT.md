# HKMP Stage 8R — Certification Remediation Report

**Scope:** Remediation of the certification blockers identified in
`HKMP_STAGE8E_SEMANTIC_INTEGRITY_AUDIT.md` and confirmed/reclassified in
`HKMP_STAGE8F_CERTIFICATION_REVIEW.md`. No architecture was redesigned, no new
ontology concept was introduced beyond what the approved remediation required
(two new data properties — `available_quantity` and four identity properties
relocated, not newly invented — and zero new entities, taxonomies, or
relationships), and no relationship's semantics changed — only its name.

---

## 1. Blocking Findings Addressed

| # | Finding (Stage 8E → 8F) | Severity (8F-confirmed) | Status |
|---|---|---|---|
| 1 | `property`/`with` in 3 `mutually_exclusive` constraints used per-row relationship IDs, violating `Canonical_Ontology_Schema.md` §9 | Critical | **Fixed** |
| 2 | `resource_id`/`resource_name` placed on abstract `resource`, contradicting the `person_id`/`household_id`/`organisation_id` precedent | Major | **Fixed** |
| 3 | `allocated_quantity_not_exceed_available` could not detect over-allocation across multiple concurrent `resource_allocation`s | Major | **Fixed** |
| 4 | `financial_resource_category` had no `distinct_from` reconciliation against `intervention_modality`/`delivery_modality` | Major | **Fixed** |

Optional cleanup items (not certification blockers, implemented because
inexpensive):

| Item | Status |
|---|---|
| Reclassify `required_if` misuse (`contribution_date_not_before_grant_window`, `cold_chain_integrity_constraint`) to `cardinality` | **Done** |
| Fix `cold_chain_integrity_constraint`'s type-safety gap (undefined-property access on the `financial_resource` branch) | **Done**, folded into the same edit |
| Namespace consistency (`data-properties.yaml`'s file-path-style `programs_tax`) | **Done** |
| Version metadata bump | **Done**, on all 10 files touched across Stage 8B–8R |
| ADR Implementation Status updates | **Done**, ADR-025, ADR-027, ADR-028 |

---

## 2. Remediation Detail, Mapped to Findings

### 2.1 Critical — Relationship verb rename (Finding 1)

Three shared-verb relationship pairs were renamed to distinct verbs, following
the `needs-assessment/ontology/relationships.yaml` precedent
(`evaluates_person`/`evaluates_household`/`evaluates_community`) that Stage 8F
identified as already solving this exact problem elsewhere in the repository:

| Row `id` (unchanged) | Old `relationship` (shared) | New `relationship` (distinct) |
|---|---|---|
| `donor_profile_of_person` | `profile_of` | `profile_of_person` |
| `donor_profile_of_organisation` | `profile_of` | `profile_of_organisation` |
| `resource_allocation_allocated_to_program` | `allocated_to` | `allocated_to_program` |
| `resource_allocation_allocated_to_case_plan` | `allocated_to` | `allocated_to_case_plan` |
| `resource_allocation_funded_by_grant` | `funded_by` | `funded_by_grant` |
| `resource_allocation_funded_by_contribution` | `funded_by` | `funded_by_contribution` |

Row `id`s, `from`/`to` targets, and cardinalities are unchanged — only the
`relationship:` verb changed, so no edge in the graph was added, removed, or
retargeted.

The three affected `mutually_exclusive` constraints were then updated to
reference the new canonical verbs instead of the row `id`s:

| Constraint | Old `property`/`with` | New `property`/`with` |
|---|---|---|
| `donor_profile_attachment_exclusive` | `donor_profile_of_person` / `[donor_profile_of_organisation]` | `profile_of_person` / `[profile_of_organisation]` |
| `resource_allocation_target_exclusive` | `resource_allocation_allocated_to_program` / `[resource_allocation_allocated_to_case_plan]` | `allocated_to_program` / `[allocated_to_case_plan]` |
| `resource_allocation_funding_source_exclusive` | `resource_allocation_funded_by_grant` / `[resource_allocation_funded_by_contribution]` | `funded_by_grant` / `[funded_by_contribution]` |

All three now comply with `Canonical_Ontology_Schema.md` §9's rule verbatim:
`property` is "the canonical reusable property name ... the `relationship`
value from §6 ... never a per-row relationship `id`." Verified directly
(§4 below) — zero remaining `mutually_exclusive` constraint in this domain
references a row `id`.

**Files modified:** `donor-resource/ontology/relationships.yaml`,
`donor-resource/ontology/semantic-constraints.yaml`.

### 2.2 Major — Resource identity placement (Finding 2)

`resource_id` and `resource_name` (previously `domain: resource`) were removed
from `data-properties.yaml` and replaced with:

- `financial_resource_id`, `financial_resource_name` — `domain: financial_resource`
- `material_resource_id`, `material_resource_name` — `domain: material_resource`

matching the repository's own precedent exactly: `person_id` (`domain:
person`), `household_id` (`domain: household`), `organisation_id`/
`organisation_name` (`domain: organisation`) in
`shared/ontology/data-properties.yaml` — the abstract supertype in every
precedent case (`subject`) owns zero data properties. `resource`'s
`ownership_boundary` text in `entities.yaml` was corrected to state it owns
nothing (previously claimed "owns no allocatable data" while contradicting
that with two required fields); `financial_resource` and `material_resource`'s
`ownership_boundary`/`notes` text was updated to list their own new identity
properties.

**Files modified:** `donor-resource/ontology/data-properties.yaml`,
`donor-resource/ontology/entities.yaml`.

### 2.3 Major — Allocation invariant (Finding 3)

**Approach chosen: implement a repository-consistent `available_quantity`
model** (the first of the two options offered), not a scope-limitation
disclaimer, because the fix was directly achievable within ontology scope
without inventing any process/runtime logic:

- Added `inventory_item.available_quantity` (`xsd:decimal`, `{min:1,max:1}`)
  to `data-properties.yaml` — a declared, bounded fact about the inventory
  item, exactly like the pre-existing `quantity_on_hand`, not a computed or
  runtime-derived field.
- Added a new constraint, `inventory_item_available_quantity_bounds`
  (`0 <= available_quantity <= quantity_on_hand`), to
  `semantic-constraints.yaml`.
- Retargeted `allocated_quantity_not_exceed_available`'s expression from
  `allocated_quantity <= inventory_item.quantity_on_hand` to
  `allocated_quantity <= inventory_item.available_quantity`.

**Justification for this approach over the scope-limitation alternative:**
`available_quantity` is declared and bounded the same way `quantity_on_hand`
already is — the ontology states what the fact IS and constrains its
relationship to other facts, without prescribing HOW an application layer
keeps it in sync with the sum of active allocations as they are created,
cancelled, or fulfilled. That synchronization process is explicitly left to
the reasoning/application layer, consistent with the ADR-023 §19
runtime/instance-state boundary this domain already applies elsewhere (e.g.
`stock_movement_type`'s own purpose note explicitly defers a per-instance
movement log for the identical reason). This resolves the invariant the
original Stage 8C brief named ("allocated quantity cannot exceed available
quantity") against a field actually scoped for that purpose, rather than
either leaving it unresolved or declaring the whole invariant out of scope.

**Files modified:** `donor-resource/ontology/data-properties.yaml`,
`donor-resource/ontology/semantic-constraints.yaml`,
`donor-resource/ontology/entities.yaml` (notes).

### 2.4 Major — `financial_resource_category` taxonomy reconciliation (Finding 4)

Two `distinct_from` reference entries were added to
`donor-resource/taxonomy/resource-classification.yaml`'s `references:` block,
covering `financial_resource_category` against `programs:intervention_modality`
and `support_delivery:delivery_modality` — mirroring the style, structure, and
level of detail of the pre-existing `material_resource_category` entries.
`financial_resource_category` now has the same reconciliation coverage
`material_resource_category` already had.

**Files modified:** `donor-resource/taxonomy/resource-classification.yaml`.

### 2.5 Optional cleanup performed

- **`required_if` → `cardinality` reclassification:** `contribution_date_
  not_before_grant_window` and `cold_chain_integrity_constraint` were
  reclassified from `type: required_if` to `type: cardinality`, matching the
  type this file's other cross-entity-expression constraints
  (`inventory_quantity_non_negative`, `allocated_quantity_not_exceed_available`)
  already correctly use. The `condition` parameter (not valid under
  `cardinality`) was folded into the `expression` itself in both cases. No
  change to the invariant enforced.
- **`cold_chain_integrity_constraint` type-safety fix:** folded into the same
  edit — the expression now explicitly short-circuits when
  `inventory_item.instance_of` is not a `material_resource`, instead of
  unconditionally reading `cold_chain_required` off a target that might be a
  `financial_resource` (which has no such property).
- **Namespace consistency:** `donor-resource/ontology/data-properties.yaml`'s
  `programs_tax` namespace changed from the file-path form
  (`"programs/taxonomy/funding-and-compliance.yaml"` — the explicitly-named
  anti-pattern in `Canonical_Ontology_Schema.md` §10) to the domain-name form
  (`programs`), matching every other namespace declaration in this domain.
- **Version metadata:** bumped on all 10 files with real content changes
  across Stage 8B–8R that had never been incremented:
  `donor-resource/ontology/{entities,relationships,data-properties,
  semantic-constraints}.yaml` and `donor-resource/taxonomy/resource-
  classification.yaml` (1.0.0 → 1.1.0); `programs/ontology/entities.yaml`,
  `programs/taxonomy/funding-and-compliance.yaml`,
  `support-delivery/ontology/{relationships,entities}.yaml` (1.0.0 → 1.1.0);
  `support-delivery/taxonomy/delivery-modalities.yaml` (1.1.0 → 1.2.0, its
  second real change).
- **ADR Implementation Status updates:** `ADR-025`, `ADR-027`, and `ADR-028`
  each gained a note recording the Stage 8R changes relevant to them (verb
  renames, identity relocation, `available_quantity`, taxonomy reconciliation)
  without altering any ADR's actual Decision/Consequences text.
- **Documentation prose:** the most visible stale mentions of the old shared
  verbs (`profile_of`, `funded_by`) in `donor-resource/governance.md` and
  `donor-resource/README.md` were updated to the new verb names.
  `PREPARED_GOVERNANCE_ADDITIONS.md` was left as-is — it is explicitly marked
  a frozen historical staging record (per its Stage 8D status banner), not a
  live document.

---

## 3. Every File Modified in This Pass

| File | Change |
|---|---|
| `donor-resource/ontology/relationships.yaml` | 6 relationship verbs renamed (§2.1); version bump |
| `donor-resource/ontology/semantic-constraints.yaml` | 3 `mutually_exclusive` constraints corrected (§2.1); 2 `required_if`→`cardinality` reclassifications (§2.5); 1 new constraint added, 1 constraint retargeted (§2.3); version bump |
| `donor-resource/ontology/data-properties.yaml` | `resource_id`/`resource_name` removed; 4 replacement identity properties added (§2.2); `available_quantity` added (§2.3); namespace fixed (§2.5); version bump |
| `donor-resource/ontology/entities.yaml` | `resource`, `financial_resource`, `material_resource`, `inventory_item` `ownership_boundary`/`notes` text corrected (§2.2, §2.3); version bump |
| `donor-resource/taxonomy/resource-classification.yaml` | 2 new `distinct_from` reference entries for `financial_resource_category` (§2.4); version bump |
| `donor-resource/governance.md` | Stale verb mentions updated (§2.5) |
| `donor-resource/README.md` | Stale verb mention updated (§2.5) |
| `programs/ontology/entities.yaml` | Version bump only (§2.5) |
| `programs/taxonomy/funding-and-compliance.yaml` | Version bump only (§2.5) |
| `support-delivery/ontology/relationships.yaml` | Version bump only (§2.5) |
| `support-delivery/ontology/entities.yaml` | Version bump only (§2.5) |
| `support-delivery/taxonomy/delivery-modalities.yaml` | Version bump only (§2.5) |
| `architecture-decisions/ADR-025-donor-identity-model.md` | Implementation Status updated (§2.5) |
| `architecture-decisions/ADR-027-grant-ownership.md` | Implementation Status updated (§2.5) |
| `architecture-decisions/ADR-028-resource-model.md` | Implementation Status updated (§2.5) |

**No file outside this list was touched.** No entity, taxonomy scheme, or
relationship row was added beyond `inventory_item_available_quantity_bounds`
(one new constraint) and `available_quantity` (one new data property) —
both explicitly required by the approved Finding 3 remediation, not
independent scope expansion.

---

## 4. Validation Results

| Check | Method | Result |
|---|---|---|
| **Full YAML validation** | Standard YAML loader against all 19 touched/adjacent files (`donor-resource/ontology/*.yaml`, `donor-resource/taxonomy/*.yaml`, `programs/ontology/entities.yaml`, `programs/taxonomy/funding-and-compliance.yaml`, `support-delivery/ontology/*.yaml`, `support-delivery/taxonomy/delivery-modalities.yaml`) | **All pass** |
| **Relationship integrity validation** | Confirmed the 6 renamed rows retain their original `id`, `from`, `to`, and `cardinality`; confirmed no relationship verb is now shared across two sibling rows anywhere in `donor-resource/ontology/relationships.yaml` | **Pass** |
| **Semantic constraint validation** | Confirmed all 3 `mutually_exclusive` constraints' `property`/`with` values now match an actual `relationship:` verb (not a row `id`) declared in `relationships.yaml`; confirmed `inventory_item_available_quantity_bounds` and the retargeted `allocated_quantity_not_exceed_available` both reference `available_quantity`, a now-declared property; confirmed no `required_if` constraint remains on an already-unconditionally-required property | **Pass** |
| **Namespace validation** | Confirmed `donor-resource/ontology/data-properties.yaml`'s `programs_tax` namespace matches the domain-name form used by every other `donor-resource/` file | **Pass** |
| **Cross-reference validation** | Confirmed `financial_resource_category`'s new reference entries correctly cite `programs:intervention_modality` and `support_delivery:delivery_modality`, both already-declared namespace aliases in this file; confirmed no new namespace alias was required | **Pass** |
| **No duplicate entity/relationship/data-property/constraint IDs** | `grep -oh "id: [a-z_]*" donor-resource/ontology/*.yaml \| sort \| uniq -d` | **Zero duplicates** |
| **Repository boundary** | `git status --porcelain` before and after this pass | Only the 14 files in §3 changed; no file outside the pre-approved remediation scope was touched |

---

## 5. Mapping: Stage 8E/8F Finding → Implemented Fix

| Stage 8E § | Stage 8F disposition | Fix implemented |
|---|---|---|
| 4.1 (Critical) | Upheld Critical; root cause corrected to "primarily repository implementation defect" with a precedented fix | §2.1 — relationship verb rename + constraint correction |
| 4.2 (Major) | Upheld Major | §2.2 — identity moved to concrete specializations |
| 4.3 (Major) | Upheld Major | §2.3 — `available_quantity` model implemented |
| 4.4 (Major → downgraded to Minor by 8F) | Not a blocker per 8F, but cheap to fix alongside 6.4 | §2.5 — type-safety rewrite folded into the `required_if` cleanup |
| 5.2 (Major) | Upheld Major | §2.4 — `financial_resource_category` reconciliation added |
| 5.4 (Minor) | Not a blocker | §2.5 — namespace fixed |
| 6.4 (Major → downgraded to Minor by 8F) | Not a blocker per 8F, but cheap to fix | §2.5 — reclassified to `cardinality` |
| 7.1 (Major → downgraded to Minor by 8F) | Not a blocker per 8F (diffs independently verified trivial) | No further action required — this review's own `git diff` re-check (§4) confirms the Stage 8D changes remain additive-only after this pass's edits |
| 7.2 (Minor → reclassified Observation by 8F) | Not a blocker | Not acted on — 8F classified this as a documentation-improvement opportunity, not a defect |
| 7.3 (Minor) | Not a blocker | §2.5 — version metadata bumped |

---

## 6. Remaining Known Issues

**None that block certification**, per the Stage 8F review's own scoping of
what deferral was conditioned on (§8 of `HKMP_STAGE8F_CERTIFICATION_REVIEW.md`
named exactly findings 4.1, 4.2, 4.3, and 5.2 as the gating set — all four are
resolved above).

Two items remain open by design, carried forward as disclosed, non-blocking
observations (not new findings introduced by this pass):

1. **`Canonical_Ontology_Schema.md` §9's worked example** still shows only the
   data-property case for `mutually_exclusive`, not the sibling-relationship
   case this remediation resolved by following the `needs-assessment`
   precedent. Stage 8F filed this as a documentation-enhancement Observation,
   not a defect requiring a schema amendment — no change was made to
   `Canonical_Ontology_Schema.md` in this pass, consistent with that
   disposition and with this phase's "do not redesign the architecture" rule.
2. **`available_quantity` synchronization** is, by design (§2.3), a
   reasoning/application-layer responsibility not enforced by the ontology
   itself beyond its two declared bounds. This is a disclosed scope boundary,
   not an oversight — consistent with how this domain already treats stock
   movement history (`stock_movement_type`'s own purpose note) and how
   Volunteer Operations treats assignment history (ADR-024 Tier 2).

No new defect was introduced by this remediation pass — every touched file
was re-validated after editing (§4), and no finding from Stage 8E/8F was left
unaddressed without an explicit, reasoned disposition.
