# ADR-028

## Title
Resource Model

## Status
Accepted

## Date
2026-07-17 (drafted HKMP Stage 8A; ratified and integrated HKMP Stage 8D)

## Context
No material or financial resource concept existed anywhere in the repository prior to Stage 8C.
Support Delivery's own gap report names warehouse/inventory tracking as an explicitly deferred gap,
and its existing `custody_transfer`/`custodian` entities already model movement of goods *after*
they exist in some stock — nothing modeled the stock itself.

## Decision
A shallow type hierarchy, not a flat set and not a deep taxonomy-only model:

- `resource` — abstract supertype, owns no allocatable/trackable data itself (mirrors `subject`'s
  "owns no demographic data" discipline exactly).
  - `financial_resource` — money, vouchers-as-value (not vouchers-as-delivery-modality, which
    Support Delivery already owns; this is the *funded value*, not the *handover mechanism*).
  - `material_resource` — physical goods, with a `material_resource_category` taxonomy value
    (analogous discipline to `intervention_modality`) distinguishing food/medicine/shelter
    materials/clothing/hygiene kits/educational materials/medical equipment/vehicles/fuel/water/
    agricultural inputs at the taxonomy level rather than the entity level, unless implementation
    concretely found a subtype's property set diverging enough to warrant its own entity — that
    determination was deferred to implementation, not pre-decided here.
- `inventory_item` — the trackable **instance** of a `resource` (of either subtype) held at a
  `storage_location`, in a given quantity and condition. This entity/instance split is
  non-negotiable: `resource`/`financial_resource`/`material_resource` describe *what kind of thing
  this is*; `inventory_item` describes *how much of it exists, where, right now*.
- `storage_location` — a warehouse, distribution center, cold-chain storage facility, temporary
  storage site, or mobile storage unit holding `inventory_item`s.
- `resource_allocation` — the decision that reserves or commits a specific `inventory_item` to a
  `program` or `case_plan`, before delivery. Not delivery itself.

`equipment` and `asset`-like distinctions were **not** pre-committed as separate entities in this
ADR — they were left open, to be resolved as taxonomy values under `material_resource_category`
unless implementation found genuine structural divergence. This ADR committed to the *shape of the
decision process*, not to a premature answer on the deepest tier.

## Consequences
- **Positive:** Mirrors the repository's own most successful precedent (`subject`/ADR-018) for
  exactly this kind of common-abstraction-plus-specialization need.
- **Positive:** The `resource` type / `inventory_item` instance split gives Support Delivery a
  single, stable entity (`inventory_item`, reached via `resource_allocation`) to reference from
  `delivery_event`, regardless of how deep the type hierarchy under `resource` grows in the future.
- **Constraint:** `resource` itself must never be allocated, delivered, or transferred directly —
  only `inventory_item` (a concrete instance) can be. This mirrors `subject` never itself appearing
  in a case, only its specializations doing so.

## Deferred Question — Resolved During Implementation
Whether `consumable`/`equipment`/`asset` become full entities or remain taxonomy values under
`material_resource_category` was left open by this ADR's original draft, to be determined against
evidence of actual property divergence. **Resolution (Stage 8C implementation):** no property
divergence was found beyond `cold_chain_required` — a single boolean data property on
`material_resource`, applicable regardless of category — which does not, on its own, justify
splitting `material_resource` into further entities. `consumable`, `equipment`, and `asset`-like
distinctions remain `material_resource_category` taxonomy values (`food`, `medicine`,
`medical_equipment`, `vehicles`, etc.). If a future category requires materially different
structured properties (not just a different category label), this resolution should be revisited
against that concrete evidence — not speculatively. Recorded as `donor-resource/governance.md`
DR-FLAG-C (Resolved).

## Implementation Status
Fully implemented: `resource`, `financial_resource`, `material_resource`, `inventory_item`,
`storage_location`, `resource_allocation` (`donor-resource/ontology/entities.yaml`);
`inventory_item_instance_of_resource`, `inventory_item_stored_at_storage_location`,
`resource_allocation_allocates_inventory_item`, `resource_allocation_allocated_to_program`,
`resource_allocation_allocated_to_case_plan`, `resource_allocation_funded_by_grant`,
`resource_allocation_funded_by_contribution` (`donor-resource/ontology/relationships.yaml`);
`material_resource_category`, `financial_resource_category`, `resource_condition`
(`donor-resource/taxonomy/resource-classification.yaml`); `storage_location_type`
(`donor-resource/taxonomy/storage.yaml`); `allocation_priority`, `allocation_status`,
`reservation_state` (`donor-resource/taxonomy/allocation.yaml`); `stock_movement_type`
(`donor-resource/taxonomy/stock-movement.yaml`, classification only, no runtime log entity). See
`HKMP_STAGE8C_IMPLEMENTATION_REPORT.md`.

Support Delivery's own downstream reference row, `delivery_event_fulfilled_from_resource_allocation`
(`support-delivery/ontology/relationships.yaml`), was added per HKMP Stage 8D, authored on the
Support Delivery side per the "referencing domain owns the edge" discipline.

**HKMP Stage 8R Certification Remediation (post-Stage-8E/8F):** four corrections applied, none
altering this ADR's decision:
1. `resource_allocation_allocated_to_program` / `_case_plan` relationship verbs renamed from a
   shared `allocated_to` to `allocated_to_program` / `allocated_to_case_plan`; `resource_allocation_
   funded_by_grant` / `_contribution` renamed from a shared `funded_by` to `funded_by_grant` /
   `funded_by_contribution` — closing the Critical `Canonical_Ontology_Schema.md` §9 violation found
   in `HKMP_STAGE8E_SEMANTIC_INTEGRITY_AUDIT.md` §4.1.
2. `resource_id`/`resource_name` moved off the abstract `resource` entity onto
   `financial_resource`/`material_resource` individually (as `financial_resource_id`/`_name` and
   `material_resource_id`/`_name`), matching the `person_id`/`household_id` precedent this ADR's
   "mirrors `subject`'s discipline exactly" claim always intended — closing the Major finding in
   `HKMP_STAGE8E_SEMANTIC_INTEGRITY_AUDIT.md` §4.2.
3. `inventory_item.available_quantity` added, and `allocated_quantity_not_exceed_available`
   retargeted to check against it instead of raw `quantity_on_hand` — closing the Major
   multi-allocation over-commitment gap in `HKMP_STAGE8E_SEMANTIC_INTEGRITY_AUDIT.md` §4.3.
4. `financial_resource_category` given the same `distinct_from` reconciliation against
   `programs:intervention_modality` / `support_delivery:delivery_modality` that
   `material_resource_category` already had — closing `HKMP_STAGE8E_SEMANTIC_INTEGRITY_AUDIT.md`
   §5.2. See `HKMP_STAGE8R_CERTIFICATION_REMEDIATION_REPORT.md` for full detail.

## Related Documents
- ADR-018 (Shared Subject Supertype — structural precedent), `support-delivery/ontology/entities.yaml`
  (`custody_transfer`, `custodian` — referenced not modified),
  ADR-023 (value object vs. entity discipline, informing the resolved
  `consumable`/`equipment`/`asset` question)
