# HKMP Stage 8G — Final Certification Verification

**Posture:** Final certification authority. `HKMP_STAGE8R_CERTIFICATION_REMEDIATION_REPORT.md` is
treated as an unverified claim set — every remediation it describes was independently re-checked
against the current repository content in this session, not accepted on the report's word. No
repository file was modified to produce this verification.

---

## 1. Verification Methodology

Every checklist item in the Stage 8G brief was checked with a direct command against the live
repository, run in this session:

1. **Critical checklist** — grepped every `type: mutually_exclusive` constraint in
   `donor-resource/ontology/semantic-constraints.yaml` and every relationship row's `id:`/
   `relationship:` pair in `donor-resource/ontology/relationships.yaml`, then cross-matched each
   constraint's `property`/`with` values against the actual declared verbs (not against the Stage 8R
   report's claims about them). Checked for duplicate verbs across all 17 relationship rows.
   Re-quoted `Canonical_Ontology_Schema.md` §9 directly rather than trusting Stage 8R's citation of it.
2. **Major checklist** — grepped `donor-resource/ontology/data-properties.yaml` for any remaining
   `domain: resource` data property; grepped for the new `financial_resource_id`/`_name` and
   `material_resource_id`/`_name` properties and their `domain:` values; re-confirmed
   `shared/ontology/data-properties.yaml` still declares zero properties on `subject` (the precedent
   being matched); grepped for `available_quantity`'s declaration, its bounding constraint, and the
   retargeted `allocated_quantity_not_exceed_available` expression; grepped
   `donor-resource/taxonomy/resource-classification.yaml` for the two new `financial_resource_category`
   reconciliation entries.
3. **Optional-fix checklist** — grepped for remaining `required_if` constraints (expecting exactly one,
   the pre-existing, correctly-shaped `zakat_grant_requires_eligible_category`); grepped the
   `programs_tax` namespace value; grepped every touched file's `version:` header; grepped the three
   named ADRs for a Stage 8R implementation note.
4. **Repository integrity** — ran a standard YAML loader against every file touched across Stage
   8B–8R; grepped the full repository for duplicate occurrences of every entity/property id introduced
   or renamed in this pass; grepped `inverse:` fields to confirm they still resolve; ran
   `git diff --stat` and a full `git diff` (deletions only) on the five existing-repository files Stage
   8D/8R touched to independently confirm the changes remain additive-only.
5. **Regression check** — compared the full `git diff` of the five external files line-by-line for
   anything beyond a version-string change and previously-known additive content; checked whether the
   new `cold_chain_integrity_constraint` expression introduces any syntax with no precedent elsewhere
   in the repository (it does — noted as an advisory observation, not a defect, since expression syntax
   is explicitly non-normative per §9).

---

## 2. Remediation Verification Matrix

### Critical

| Checklist item | Verified? | Evidence |
|---|---|---|
| No `mutually_exclusive` constraint references a relationship row ID | **Confirmed** | All three constraints (`donor_profile_attachment_exclusive`, `resource_allocation_target_exclusive`, `resource_allocation_funding_source_exclusive`) use `profile_of_person`/`profile_of_organisation`, `allocated_to_program`/`allocated_to_case_plan`, `funded_by_grant`/`funded_by_contribution` — none of these strings is a row `id:` anywhere in `relationships.yaml` (row ids remain `donor_profile_of_person`, `resource_allocation_allocated_to_program`, etc. — distinct from the verbs) |
| Every `property`/`with` value references a canonical relationship verb | **Confirmed** | Each of the six values above was matched against an actual `relationship:` field in `relationships.yaml`; all six resolve |
| Relationship naming now matches established repository precedent | **Confirmed** | No relationship verb is duplicated across any two of the 17 rows in `donor-resource/ontology/relationships.yaml` (checked via `sort \| uniq -d`, zero output) — the same one-verb-per-sibling-row shape as `needs-assessment`'s `evaluates_person`/`evaluates_household`/`evaluates_community` |

**Critical finding: fully resolved.**

### Major

| Checklist item | Verified? | Evidence |
|---|---|---|
| Identity ownership matches repository inheritance precedent | **Confirmed** | Zero data properties remain with `domain: resource`; `financial_resource_id`/`financial_resource_name` are declared with `domain: financial_resource`, `material_resource_id`/`material_resource_name` with `domain: material_resource`; independently re-confirmed `shared:subject` (the precedent) still declares zero data properties of its own |
| Allocation invariant references `available_quantity` | **Confirmed** | `allocated_quantity_not_exceed_available`'s expression reads `allocated_quantity <= inventory_item.available_quantity`, not `quantity_on_hand` |
| `available_quantity` is consistently declared and constrained | **Confirmed** | Declared once (`data-properties.yaml`, `domain: inventory_item`, `xsd:decimal`, `{min:1,max:1}`); bounded by exactly one constraint, `inventory_item_available_quantity_bounds` (`0 <= available_quantity <= quantity_on_hand`); referenced by exactly one other constraint, the retargeted `allocated_quantity_not_exceed_available` — no orphan or conflicting declaration found |
| Financial resource taxonomy reconciliation is complete | **Confirmed** | `resource-classification.yaml`'s `references:` block now contains four entries total: the original two for `material_resource_category` plus two new ones for `financial_resource_category` against `programs:intervention_modality` and `support_delivery:delivery_modality`, matching the pre-existing entries' structure and depth |

**All four Major findings: fully resolved.**

### Optional Fixes (non-blocking, confirmed as claimed)

| Item | Verified? | Evidence |
|---|---|---|
| `required_if` cleanup | **Confirmed** | Exactly one `required_if` constraint remains in the file (`zakat_grant_requires_eligible_category`), and it is the one correctly-shaped usage that was never flagged (an otherwise-optional property becoming conditionally required). `contribution_date_not_before_grant_window` and `cold_chain_integrity_constraint` are both now `type: cardinality` |
| Namespace consistency | **Confirmed** | `data-properties.yaml`'s `programs_tax` namespace value is `programs` (domain-name form), matching every other namespace declaration in the domain |
| Version metadata | **Confirmed** | All ten files identified as previously stale now carry incremented version strings (`1.0.0`→`1.1.0` on nine files, `1.1.0`→`1.2.0` on `delivery-modalities.yaml`) |
| ADR implementation status updates | **Confirmed** | ADR-025, ADR-027, and ADR-028 each contain a Stage 8R note; ADR-026 (Volunteer Boundary) correctly has none, since none of the Stage 8R changes touch anything ADR-026 governs |

---

## 3. Regression Assessment

**No new defect was introduced by Stage 8R.** Specifically checked and ruled out:

- **Broken inverse pairs:** all `inverse:` fields in `relationships.yaml` still name a row `id` that
  exists, unaffected by the verb renames (inverses reference row ids, which were never changed).
- **Broken cross-domain references:** the full `git diff` of the five externally-touched files
  (`programs/ontology/entities.yaml`, `programs/taxonomy/funding-and-compliance.yaml`,
  `support-delivery/ontology/{relationships,entities}.yaml`,
  `support-delivery/taxonomy/delivery-modalities.yaml`) shows exactly six deleted lines across all
  five files: five are version-string replacements, one is the pre-existing whitespace trim already
  present before Stage 8R. No content was redefined or removed.
- **New duplicate IDs:** every entity id, and every newly-introduced or renamed data-property id
  (`available_quantity`, `financial_resource_id`, `financial_resource_name`, `material_resource_id`,
  `material_resource_name`), was independently grepped across the entire repository — each occurs in
  exactly one file.
- **Namespace regression:** `programs_tax: programs` does not collide with the pre-existing
  `programs: programs` alias in `relationships.yaml` — two differently-named aliases resolving to the
  same domain-name value is an already-established repository pattern (e.g. Programs' own
  `relationships.yaml` historically pointed both `shared_org` and `shared_human` at the same shared
  namespace value).
- **YAML structural integrity:** every touched file (19 total, spanning `donor-resource/`, Programs,
  and Support Delivery) parses successfully with a standard loader.

**One advisory-level observation surfaced during regression checking, not a defect:** the rewritten
`cold_chain_integrity_constraint` expression introduces the phrase `NOT INSTANCE OF` / `INSTANCE OF`,
which has no precedent anywhere else in the repository's constraint expressions. This is not a
compliance issue — `Canonical_Ontology_Schema.md` §9 explicitly leaves expression *syntax*
non-normative (a generator concern) — but it is new vocabulary a future author should be aware isn't
yet a repository-wide convention. Recorded in §5 as an advisory observation.

---

## 4. Repository Integrity Assessment

| Check | Result |
|---|---|
| No new duplicate IDs | **Pass** — verified repository-wide for every id touched this pass |
| YAML validity | **Pass** — all 19 relevant files load cleanly |
| Relationship integrity | **Pass** — all `inverse:` pairs resolve; no relationship verb duplicated across sibling rows anywhere in the domain |
| Semantic constraint integrity | **Pass** — every constraint's `property`/`with`/`entities` values resolve to a real relationship verb or data-property id; the one new constraint (`inventory_item_available_quantity_bounds`) and the one retargeted constraint both reference `available_quantity`, which is declared exactly once |
| Namespace integrity | **Pass** — `programs_tax` now uses the domain-name form consistently with the rest of the domain; no alias collision |
| Cross-domain references remain additive only | **Pass** — independently re-verified via full `git diff`, not merely re-reading Stage 8R's claim |

**No blocking repository-integrity issue found.**

---

## 5. Advisory Observations (do not affect correctness or repository integrity)

1. **Novel expression syntax (`INSTANCE OF` / `NOT INSTANCE OF`)** in `cold_chain_integrity_constraint`
   has no precedent elsewhere in the repository's semantic constraints. Non-blocking because
   expression syntax is explicitly non-normative, but future constraint authors should be aware this
   phrase is new, not an established repository idiom, if they want to write consistently with it.
2. **`Canonical_Ontology_Schema.md` §9's worked example** still illustrates only the sibling-data-
   property case for `mutually_exclusive`, not the sibling-relationship-with-distinct-verbs case this
   remediation and the `needs-assessment` precedent both now demonstrate work correctly. Carried
   forward from Stage 8F as a documentation-enhancement opportunity, not a defect — no schema change
   was made or is required.
3. **`available_quantity` synchronization** remains, by disclosed design, a reasoning/application-layer
   responsibility rather than an ontology-enforced process (consistent with this domain's existing
   `stock_movement_type` and Volunteer Operations' Tier-2 precedent). This is a scope boundary, not a
   gap — noted here only so a future reviewer does not mistake the absence of a synchronization
   *mechanism* for an oversight; the bounding *invariant* is fully declared and constrained.

None of these three observations names a defect requiring a code or ontology change before
certification.

---

## 6. Certification Decision

**All four checklist categories (Critical, Major, Optional, Repository Integrity) pass independent
verification.** Every remediation claimed in `HKMP_STAGE8R_CERTIFICATION_REMEDIATION_REPORT.md` was
checked directly against the repository, not accepted on the report's word, and every claim held up.
No new defect was introduced by the remediation pass. The two blocking-finding sets from Stage 8E/8F
(the Critical schema-contract violation and the three remaining Major findings) are both fully closed.

## 7. Final Recommendation

**Certified with Advisory Observations.**

The Donor & Resource domain, as it now exists in the repository, satisfies every blocking finding
raised across Stage 8E and confirmed in Stage 8F. The three items in §5 are advisory only — style and
documentation-completeness notes that do not affect correctness, schema compliance, or repository
integrity, and do not require further action before this domain is treated as a certified, canonical
part of the Khidmat Knowledge Layer.
