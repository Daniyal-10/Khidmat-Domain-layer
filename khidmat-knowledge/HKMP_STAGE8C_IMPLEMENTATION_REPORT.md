# HKMP Stage 8C — Material Resource & Logistics Intelligence Implementation Report

**Scope implemented:** Material Resource & Logistics Intelligence only —
`resource`, `financial_resource`, `material_resource`, `inventory_item`,
`storage_location`, `resource_allocation`, and their supporting taxonomies.
Donor, Grant, and Contribution (Stage 8B) were not revisited — see §5 for the
line-by-line confirmation.

**Architecture followed:** `HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md`
ADR-DRAFT-028, treated as frozen. No decision in that document was
revisited. Continues the same conservative "author the edge from this
domain's own files" strategy used successfully in Stage 8B.

---

## 1. Files Created

### New taxonomy files (`donor-resource/taxonomy/`)

| File | Contents |
|---|---|
| `resource-classification.yaml` | `material_resource_category` (11 concepts), `financial_resource_category` (5 concepts), `resource_condition` (7 concepts) — 23 concepts across 3 schemes |
| `stock-movement.yaml` | `stock_movement_type` (8 concepts: receiving, dispatch, transfer, replenishment, loss, damage, spoilage, return) — classification scheme only, no per-instance movement log entity |
| `storage.yaml` | `storage_location_type` (5 concepts: warehouse, distribution_center, cold_chain_storage, temporary_storage, mobile_storage) |
| `allocation.yaml` | `allocation_priority` (4 concepts), `allocation_status` (5 concepts), `reservation_state` (3 concepts) — 12 concepts across 3 schemes |

**Total: 4 new files, 48 new taxonomy concepts across 8 schemes.**

No new top-level document was created for this stage beyond this report — the
domain-level docs (`README.md`, `governance.md`,
`PREPARED_GOVERNANCE_ADDITIONS.md`) were extended in place (§2), not
duplicated, since they describe the whole `donor-resource/` domain rather
than one sub-stage.

## 2. Files Modified

**Within `donor-resource/` only — extended, never altering Stage 8B content:**

| File | Nature of change |
|---|---|
| `ontology/entities.yaml` | Appended 6 new entities (`resource`, `financial_resource`, `material_resource`, `inventory_item`, `storage_location`, `resource_allocation`) after the existing 3 Stage 8B entities, under a clearly marked section header. The 3 Stage 8B entities are byte-for-byte unmodified. |
| `ontology/relationships.yaml` | Extended the `namespaces:` block with one new alias (`case_management`); appended 8 new relationship rows under a marked section header. Every Stage 8B relationship row is unmodified. The file's header comment was extended (not altered in substance) to list `case-management` among the domains referenced-but-not-written-to. |
| `ontology/data-properties.yaml` | Appended 20 new data properties under a marked section header, plus one header-comment addendum noting the Stage 8C addition. Every Stage 8B property is unmodified. |
| `ontology/semantic-constraints.yaml` | Appended 9 new constraints under a marked section header. Every Stage 8B constraint is unmodified. |
| `README.md` | Updated the domain-level maturity statement from "Stage 8B Implemented — Stage 8C Deferred" to "Stage 8B and 8C Implemented"; added the Stage 8C "Owns"/"Does Not Own" entries; extended the directory-structure diagram to list the 4 new taxonomy files. Stage 8B's own "Owns" entries are unmodified in substance (reorganized under a "Stage 8B —" subheading for symmetry with the new "Stage 8C —" subheading). |
| `governance.md` | Updated the Maturity section; renumbered/added Boundary Enforcement Rules 7–11 (Rule 7 rewritten to describe the now-real Stage 8B/8C seam rather than a deferral; Rules 9–11 are new); added 3 new Cross-Domain Reference Pattern entries; resolved DR-FLAG-C; added DR-FLAG-D. Rules 1–6 (all Stage 8B) are unmodified in substance. |
| `PREPARED_GOVERNANCE_ADDITIONS.md` | Extended the drafted Authority Matrix section with the 6 new entities, 3 new taxonomy-scheme rows, and 8 new relationships; extended the drafted Glossary section with 4 new terms; added 2 new drafted boundary-note items (§3.4, §3.5) for Support Delivery's own future reference row; updated the drafted roadmap entry. Nothing in this file has been integrated into an actual governance file — it remains staged. |

**No file outside `donor-resource/` was created or modified.** Verified by
`git status --porcelain` before and after this pass (§5).

## 3. Cross-Domain References Added

All authored entirely within `donor-resource/`, zero modification to the
referenced domain's own files — continuing Stage 8B's discipline exactly:

| Reference | From (owned here) | To (referenced, not modified) | Row location |
|---|---|---|---|
| `resource_allocation_allocated_to_program` | `resource_allocation` | `programs:program` | `donor-resource/ontology/relationships.yaml` |
| `resource_allocation_allocated_to_case_plan` | `resource_allocation` | `case_management:case_plan` | `donor-resource/ontology/relationships.yaml` |

**Domain-internal (both entities owned here, connecting Stage 8C to Stage 8B):**
- `resource_allocation_funded_by_grant` → `grant`
- `resource_allocation_funded_by_contribution` → `contribution`
- `inventory_item_instance_of_resource` → `resource` (polymorphic reference to
  the abstract supertype, mirroring `beneficiary_lifecycle_tracks_journey_of_subject`'s
  reference to `shared:subject`)

**Not yet added (staged, per this phase's "do not integrate governance" rule):**
- Authority Matrix rows for the 6 new entities and their relationships
  (`PREPARED_GOVERNANCE_ADDITIONS.md` §1, extended this pass)
- Glossary entries for Resource, Inventory Item, Storage Location, Resource
  Allocation (`PREPARED_GOVERNANCE_ADDITIONS.md` §2, extended this pass)
- The Support Delivery-side reference row,
  `delivery_event_fulfilled_from_resource_allocation` — deliberately **not**
  authored by this domain. Per the "referencing domain owns the edge"
  discipline used throughout both Stage 8B and 8C, this edge's `from` entity
  (`delivery_event`) belongs to Support Delivery, so Support Delivery must
  author it, not this domain. Staged as a ready-to-review proposal in
  `PREPARED_GOVERNANCE_ADDITIONS.md` §3.4–§3.5.
- The three-way `distinct_from` extension to
  `support-delivery/taxonomy/delivery-modalities.yaml`'s existing note
  (staged, `PREPARED_GOVERNANCE_ADDITIONS.md` §3.2)
- `programs/ontology/entities.yaml#eligibility_rule`'s optional reference note
  to `zakat_eligible_category` (Stage 8B item, still staged, unaffected by
  this pass)

## 4. Support Delivery Boundary — Explicit Confirmation

Per the Stage 8C brief's own rule ("inventory ends where custody begins"),
the following were checked and confirmed **absent** from every file this pass
touched:

| Concept | Found? |
|---|---|
| `custody_transfer` | Not referenced, modeled, or duplicated anywhere in `donor-resource/` |
| `delivery_event` | Not referenced as a `from`/`to` target in any relationship; named only in prose (entity descriptions, taxonomy notes) explaining where this domain's boundary sits, never as a graph edge |
| `proof_of_delivery` | Not referenced anywhere |
| `custodian` | Not referenced anywhere |
| Dispatch workflow (any process/scheduling logic) | Not modeled; `stock_movement_type#dispatch` is a classification VALUE only, not a workflow or process entity |

`storage_location`, `inventory_item`, and `resource_allocation` collectively
model everything up to and including the pre-delivery reservation decision;
nothing crosses into execution, custody, or handover.

## 5. Stage 8B Non-Revisitation — Explicit Confirmation

Checked line-by-line: `donor_profile`, `grant`, and `contribution`
(`ontology/entities.yaml`), all 9 Stage 8B relationship rows
(`ontology/relationships.yaml`), all 17 Stage 8B data properties
(`ontology/data-properties.yaml`), and all 6 Stage 8B semantic constraints
(`ontology/semantic-constraints.yaml`) are present verbatim, unchanged from
the state `HKMP_STAGE8B_IMPLEMENTATION_REPORT.md` left them in. The only
edits touching text before the Stage 8C section markers in each ontology file
were two narrow header-comment additions (a one-line addendum in
`entities.yaml` and `data-properties.yaml` noting the Stage 8C section exists
below) — no entity, relationship, property, or constraint definition itself
was altered.

## 6. Validation Results (Self-Audit)

| Check | Result |
|---|---|
| **Duplicate entity audit** | None. `resource`, `financial_resource`, `material_resource`, `inventory_item`, `storage_location`, `resource_allocation` were grepped against the full repository — each occurs only in `donor-resource/ontology/entities.yaml`. |
| **Duplicate taxonomy audit** | None. `material_resource_category`, `financial_resource_category`, `resource_condition`, `stock_movement_type`, `storage_location_type`, `allocation_priority`, `allocation_status`, `reservation_state` were grepped against the full repository — each occurs only within `donor-resource/`. |
| **Ownership audit** | No violation found. `programs:program`, `case_management:case_plan`, `programs:intervention_modality`, `support_delivery:delivery_modality`, `support_delivery:delivery_status` are all referenced by CURIE/prose cross-reference, never redefined, and no file outside `donor-resource/` was written to (§2). |
| **Semantic collision audit** | All collisions named in `HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 5 that apply to Stage 8C's scope carry an explicit reconciliation note: `material_resource_category` vs. `intervention_modality`/`delivery_modality` (`resource-classification.yaml`'s two-part `references:` block, extending the existing `delivery-modalities.yaml` note); `inventory` vs. `custody` (governance.md Rule 9; `stock-movement.yaml`'s `distinct_from` note against `support_delivery:delivery_status`); `allocation` vs. `delivery` (entity-level `ownership_boundary` prose on `resource_allocation`, and the taxonomy note on `allocation_status#fulfilled`). |
| **Relationship validation** | Every relationship with an `inverse:` field has its inverse row present and reciprocally cross-referenced (`inventory_item_stored_at_storage_location` ↔ `storage_location_holds_inventory_item`). `inventory_item_instance_of_resource`, `resource_allocation_allocates_inventory_item`, the two `allocated_to_*` rows, and the two `funded_by_*` rows correctly have no inverse authored — either because they are polymorphic/domain-internal one-directional facts, or (for the two cross-domain `allocated_to_*` rows) because authoring an inverse would require writing into Programs' or Case Management's own files, which this domain does not do. All `taxonomy_ref` values in the Stage 8C section of `data-properties.yaml` resolve to a scheme defined in this pass's own `taxonomy/` files, cross-checked by hand. |
| **Repository boundary validation** | Confirmed via `git status --porcelain` (run before this pass began and again just before writing this report): the only paths that changed are inside `donor-resource/` plus this new report at the repository root. No certified file (Programs, Support Delivery, Case Management, Shared Ontology, Volunteer Operations, Community Context, `ontology_authority_matrix.md`, `GLOSSARY.md`) was touched. |
| **ADR compliance review** | ADR-DRAFT-028 (Resource Model): satisfied — the `resource`/`financial_resource`/`material_resource` type hierarchy plus `inventory_item` as the distinct trackable instance is exactly the shallow, ADR-018-mirroring shape the draft specifies; the deferred `consumable`/`equipment`/`asset` question was resolved empirically during this pass (DR-FLAG-C, `governance.md`) by finding no property divergence beyond `cold_chain_required` (captured as a boolean on `material_resource`, not an entity split). ADR-008 (Single Ownership): satisfied, per the Ownership Audit row above. ADR-009 (Dependency-Driven Activation): satisfied — this addition depends only on already-active domains (Programs, Case Management, Shared Ontology) plus its own Stage 8B, and makes no already-active domain depend on it. ADR-018 (Shared Subject precedent): directly applied — `resource` mirrors `subject`'s "abstract, owns no data" discipline, and `inventory_item_instance_of_resource`'s polymorphic targeting of the abstract supertype directly mirrors `beneficiary_lifecycle_tracks_journey_of_subject`'s identical pattern. ADR-023 (Value Objects / runtime boundary): `stock_movement_type` is correctly kept as a classification scheme only, with the per-instance movement log explicitly deferred as runtime/instance state, mirroring the §19 boundary already applied to Volunteer Operations' Tier 2. Canonical_Ontology_Schema.md §9 (closed constraint-type vocabulary): every new constraint uses only the four types already present in the repository (`cardinality`, `required_if`, `mutually_exclusive`) — no new constraint `type` was invented; cross-entity structural invariants (e.g. `allocated_quantity_not_exceed_available`) reuse the `cardinality` type's `expression` parameter, the same mechanism registration's own `beneficiary_age_validation` and `urgency_score` constraints already established as valid for general boolean invariants, not just literal min/max counts. |

**Self-audit outcome: no unresolved defect found.**

## 7. Remaining Stage 8 Work

1. **Ratify ADR-DRAFT-025 through ADR-DRAFT-028** — still outstanding from
   Stage 8B, unaffected by this pass.
2. **Integrate `PREPARED_GOVERNANCE_ADDITIONS.md`** (now covering both 8B and
   8C) into `ontology_authority_matrix.md`, `GLOSSARY.md`, and the five named
   existing files' boundary notes (§3.1–§3.5 of that document).
3. **Author the Support Delivery reference row**
   (`delivery_event_fulfilled_from_resource_allocation`) — on the Support
   Delivery side, per the staged proposal in
   `PREPARED_GOVERNANCE_ADDITIONS.md` §3.4. This is the one remaining edge in
   the full Stage 8 context diagram
   (`HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 3) not yet authored
   anywhere in the repository — by design, since it belongs to a domain this
   effort does not own.
4. **Extend the `distinct_from` note** in
   `support-delivery/taxonomy/delivery-modalities.yaml` to a three-way note
   (staged, `PREPARED_GOVERNANCE_ADDITIONS.md` §3.2).
5. **Revisit DR-FLAG-A and DR-FLAG-B** only as their own separately-governed
   future proposals, per the conditions already recorded in `governance.md`
   — not part of any currently-planned Stage 8 work.
6. With both 8B and 8C now implemented, **HKMP Stage 8 (Donor & Resource
   Intelligence) is feature-complete at the ontology-drafting level**; the
   only remaining work is governance integration (items 1–2 above) and the
   one cross-domain row that belongs to Support Delivery (item 3).

---

**Net result (this pass):** 6 new entities, 8 new relationship rows
(2 additive cross-domain, 3 domain-internal, 3 domain-local structural), 20
new data properties, 9 new semantic constraints, and 4 new taxonomy files
totaling 48 concepts across 8 schemes — with zero modification to any file
outside `donor-resource/`, zero modification to Stage 8B's own entities,
relationships, properties, or constraints, and every governance-facing
addition staged for review rather than integrated. Combined with Stage 8B,
the Donor & Resource domain now spans 9 entities, 17 relationship rows, 37
data properties, 15 semantic constraints, and 7 taxonomy files across the
full donor-to-delivery funding and resource chain, stopping precisely at the
boundary Support Delivery owns.
