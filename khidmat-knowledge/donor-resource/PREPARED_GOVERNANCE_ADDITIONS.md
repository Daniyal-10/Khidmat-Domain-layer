# Prepared Governance Additions — Donor & Resource (Stage 8B + 8C)

**Status: INTEGRATED (HKMP Stage 8D).** Every item below has been copied into
its target governance file — `ontology_authority_matrix.md`, `GLOSSARY.md`,
`programs/taxonomy/funding-and-compliance.yaml`,
`support-delivery/taxonomy/delivery-modalities.yaml`,
`programs/ontology/entities.yaml`, `support-delivery/ontology/relationships.yaml`,
`support-delivery/ontology/entities.yaml`, `knowledge_layer_roadmap.md`, and
`architecture-decisions/` (ADR-025 through ADR-028) — exactly as drafted here,
with no redesign. This document is retained as the historical staging record
of what Stage 8D integrated and why, per `HKMP_STAGE8D_INTEGRATION_REPORT.md`.
It is no longer the live source of truth for any of these facts — the target
files themselves are.

---

## 1. Authority Matrix Addition (drafted; not integrated)

To be appended to `ontology_authority_matrix.md` as a new "Donor & Resource
Domain" section, in the same format as the existing Programs / Case
Management / Volunteer Operations sections:

> ## Donor & Resource Domain
>
> **Authoritative files:** `donor-resource/ontology/`, `donor-resource/taxonomy/`
> **Owner domain:** Donor & Resource
> **Introduced:** HKMP Stage 8B (Donor & Funding Intelligence); extended
> HKMP Stage 8C (Material Resource & Logistics Intelligence)
> **Governing ADRs:** ADR-025, ADR-026, ADR-027,
> ADR-028 (pending ratification and numbering)
>
> | Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
> |---|---|---|---|---|
> | `donor_profile` | Donor Profile | `donor-resource/ontology/entities.yaml` | Donor & Resource | Attaches behind `shared:person` or `shared:organisation` (never both); must not redefine either. Must not be redefined elsewhere. |
> | `grant` | Grant | `donor-resource/ontology/entities.yaml` | Donor & Resource | References `programs:funding_source_types` / `programs:funding_restrictions`; does not redefine them. Funds `programs:program` additively via `grant_funds_program`, coexisting with the untouched `programs:program_funded_by`. Must not be redefined elsewhere. |
> | `contribution` | Contribution | `donor-resource/ontology/entities.yaml` | Donor & Resource | Must not be redefined elsewhere. |
> | `donor_type`, `donor_engagement_pattern`, `anonymity_level` | Donor Classification Taxonomy | `donor-resource/taxonomy/donor-classification.yaml` | Donor & Resource | `donor_type` is distinct from `programs:funding_source_types` — see that file's `distinct_from` reference block. Must not be redefined elsewhere. |
> | `islamic_giving_type`, `zakat_eligible_category` | Islamic Giving Taxonomy | `donor-resource/taxonomy/islamic-giving.yaml` | Donor & Resource | `zakat_eligible_category` is referenceable by, but does not redefine or supersede, `programs:eligibility_rule`. Not subject to ADR-022 regional-synonym collapse (see that file's purpose note). Must not be redefined elsewhere. |
> | `grant_status`, `contribution_status`, `renewal_status` | Funding Lifecycle Taxonomy | `donor-resource/taxonomy/funding.yaml` | Donor & Resource | Must not be redefined elsewhere. |
> | `resource` | Resource (abstract) | `donor-resource/ontology/entities.yaml` | Donor & Resource | Abstract supertype; owns no allocatable data. Never itself allocated or delivered. Must not be redefined elsewhere. |
> | `financial_resource`, `material_resource` | Resource Specializations | `donor-resource/ontology/entities.yaml` | Donor & Resource | `parent: resource`. Must not be redefined elsewhere. |
> | `inventory_item` | Inventory Item | `donor-resource/ontology/entities.yaml` | Donor & Resource | The tracked instance of a resource. Must not be collapsed into `resource`. Must not be redefined elsewhere. |
> | `storage_location` | Storage Location | `donor-resource/ontology/entities.yaml` | Donor & Resource | Physical storage concept only. Must not be redefined elsewhere. |
> | `resource_allocation` | Resource Allocation | `donor-resource/ontology/entities.yaml` | Donor & Resource | The pre-delivery reservation/commitment decision. Allocates `programs:program` or `case_management:case_plan` additively via `resource_allocation_allocated_to_program` / `_case_plan`, coexisting with untouched Programs/Case Management files. Must not reference `delivery_event`, `custody_transfer`, `custodian`, or `proof_of_delivery` (Support Delivery, untouched). Must not be redefined elsewhere. |
> | `material_resource_category`, `financial_resource_category`, `resource_condition` | Resource Classification Taxonomy | `donor-resource/taxonomy/resource-classification.yaml` | Donor & Resource | `material_resource_category` is distinct from `programs:intervention_modality` and `support_delivery:delivery_modality` — see that file's `distinct_from` reference block. Must not be redefined elsewhere. |
> | `stock_movement_type` | Stock Movement Taxonomy | `donor-resource/taxonomy/stock-movement.yaml` | Donor & Resource | Classification scheme only; no per-instance movement log entity exists at this maturity. Must not be redefined elsewhere. |
> | `storage_location_type` | Storage Taxonomy | `donor-resource/taxonomy/storage.yaml` | Donor & Resource | Must not be redefined elsewhere. |
> | `allocation_priority`, `allocation_status`, `reservation_state` | Allocation Taxonomy | `donor-resource/taxonomy/allocation.yaml` | Donor & Resource | Must not be redefined elsewhere. |
>
> **Relationships Owned:**
> - `donor_profile_of_person`, `donor_profile_of_organisation`
> - `grant_issued_by_donor_profile` / `donor_profile_issues_grant`
> - `contribution_given_by_donor_profile` / `donor_profile_gives_contribution`
> - `contribution_contributes_to_grant` / `grant_receives_contribution`
> - `grant_funds_program` (cross-domain, additive; no inverse authored in Programs)
> - `inventory_item_instance_of_resource` (polymorphic, domain-internal)
> - `inventory_item_stored_at_storage_location` / `storage_location_holds_inventory_item`
> - `resource_allocation_allocates_inventory_item`
> - `resource_allocation_allocated_to_program` (cross-domain, additive; no inverse authored in Programs)
> - `resource_allocation_allocated_to_case_plan` (cross-domain, additive; no inverse authored in Case Management)
> - `resource_allocation_funded_by_grant` / `resource_allocation_funded_by_contribution` (domain-internal)
>
> **Explicit References Only (Owned Elsewhere):**
> - `person`, `organisation` (Shared Ontology)
> - `program` (Programs)
> - `funding_source_types`, `funding_restrictions` (Programs)
> - `eligibility_rule` (Programs) — `zakat_eligible_category` is a
>   referenceable value, not an owned relationship into this concept
> - `case_plan` (Case Management)
> - `local-organizations` typology (Community Context) — referenced only when
>   typing a community/faith-based donor's underlying `organisation`, never
>   authored as a relationship from this domain
>
> **Explicitly Not Owned (Support Delivery, permanent exclusion):**
> - `custody_transfer`, `custodian`, `delivery_event`, `proof_of_delivery`,
>   any dispatch workflow. Inventory ends where custody begins.
>
> **Explicitly Not Owned (Volunteer Operations, permanent exclusion):**
> - Any volunteer skill, certification, availability, capability, capacity,
>   deployment, or assignment concept. See ADR-026.

---

## 2. Glossary Additions (drafted; not integrated)

To be appended to `GLOSSARY.md` under a new "Donor & Resource Terms" heading,
each cross-referencing the terms the Stage 7C certification review's Glossary
finding (the unreconciled duplicate "Case" entries) shows must not be added
without cross-reference:

> ## Donor & Resource Terms
>
> **Donor Profile**
> The record of a person's or organisation's giving relationship with
> Khidmat — never an independent identity. Attaches behind an existing
> `shared:person` or `shared:organisation` record, mirroring how Volunteer
> Profile attaches behind the shared Actor. See Volunteer Profile, below.
>
> **Grant**
> A funding commitment instance issued by a Donor Profile, optionally funding
> one or more Programs. Distinct from, and additive to, a Program's existing
> direct funding-by-organisation relationship — a Program may be funded
> directly, via a Grant, or both.
>
> **Contribution**
> A single discrete act of giving: one gift, or one disbursement tranche of a
> Grant. Distinct from Grant itself — a Contribution records that one
> transfer occurred; a Grant represents the ongoing commitment.
>
> **Resource**
> An abstract kind of thing Khidmat holds and can allocate — financial or
> material. Not to be confused with **Recovery Resources** (Risk Domain — see
> that existing Glossary entry), which describes a household's own
> internally-mobilizable coping assets; this is an entirely distinct,
> unrelated concept describing humanitarian stock Khidmat itself holds. A
> Resource is never itself allocated or tracked with a quantity — see
> Inventory Item.
>
> **Inventory Item**
> The tracked instance of a Resource: a specific quantity, in a specific
> condition, at a specific Storage Location, right now. Never collapsed into
> Resource — Resource describes the kind; Inventory Item describes the
> tracked stock.
>
> **Storage Location**
> A physical space (warehouse, distribution center, cold-chain facility,
> temporary storage site, or mobile storage unit) holding Inventory Items.
> Not a software or database concept.
>
> **Resource Allocation**
> The decision that reserves or commits a specific Inventory Item to a
> Program or a Case Plan, before delivery. Distinct from delivery itself,
> which remains Support Delivery's Delivery Event.
>
> **Islamic Giving**
> Seven distinct, canonically defined charitable-giving forms recognized in
> this knowledge layer: Zakat, Sadaqah, Sadaqah Jariyah, Waqf, Fidya,
> Kaffarah, and Qurbani. Each has its own obligation basis and restriction
> shape; none is a synonym or regional alias for another. See
> `donor-resource/taxonomy/islamic-giving.yaml`.
>
> **Zakat-Eligible Category**
> One of the eight classical recipient categories (asnaf) to which Zakat
> funds may be distributed. A classification a Program's Eligibility Rule may
> reference when a Program is zakat-restricted — not a second eligibility
> engine.

---

## 3. Boundary Notes for Existing Files (drafted; not integrated)

These are proposed additions to *existing, certified* files' own
reconciliation-note blocks — none has been written into those files. They are
staged here for the maintainers of those files to review and add at their own
discretion, consistent with "reference only, never redefine."

### 3.1. `programs/taxonomy/funding-and-compliance.yaml`
Proposed addition to this file's own notes (not authored): a short
`distinct_from` block noting that `donor-resource:donor_type` classifies the
giving party while this file's `funding_source_types` classifies the
program's funding category — mirroring the reconciliation note already
authored on the Donor & Resource side
(`donor-resource/taxonomy/donor-classification.yaml`'s `references:` block).

### 3.2. `support-delivery/taxonomy/delivery-modalities.yaml`
Proposed extension (not authored) to this file's existing `distinct_from`
note block: now that Stage 8C's `material_resource_category` exists, this
file's reconciliation note should be extended to a three-way note
(`intervention_modality` / `delivery_modality` / `material_resource_category`)
rather than left as its current two-way note, per
`HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 5. The Donor & Resource
side of this reconciliation is already authored
(`donor-resource/taxonomy/resource-classification.yaml`'s `references:`
block); this entry stages the mirror-image addition on the Support Delivery
side.

### 3.3. `programs/ontology/entities.yaml` (`eligibility_rule`)
Proposed addition (not authored): a note on `eligibility_rule` stating it may
optionally reference `donor-resource:zakat_eligible_category` when a Program
is zakat-restricted. No property or relationship is proposed to be added to
`eligibility_rule` itself at this pass — this is a documentation-only note
for future authors, staged, not implemented.

### 3.4. `support-delivery/ontology/relationships.yaml`
Proposed addition (not authored): a new row,
`delivery_event_fulfilled_from_resource_allocation` (`from: delivery_event`,
`relationship: fulfilled_from`, `to: donor_resource:resource_allocation`),
authored on the Support Delivery side following this domain's own
"referencing domain owns the edge" discipline. This is the one reference row
this domain's discovery and architecture documents always anticipated being
authored by Support Delivery, not by Donor & Resource — staged here as a
ready-to-review proposal, not authored in either domain's files by this pass.

### 3.5. `support-delivery/ontology/entities.yaml` (`delivery_event`)
Proposed addition (not authored): a note on `delivery_event` cross-referencing
`donor_resource:resource_allocation` as the pre-delivery decision a delivery
event fulfills, once 3.4 above is authored — documentation-only, staged.

---

## 4. Roadmap Entry (drafted; not integrated)

Proposed addition to `knowledge_layer_roadmap.md`, explicitly disambiguating
this stage from the roadmap's own pre-existing, unrelated "Stage 8: Community
Context":

> **HKMP Stage 8B: Donor & Funding Intelligence** (requires: Programs, Shared
> Ontology) **and HKMP Stage 8C: Material Resource & Logistics Intelligence**
> (requires: Stage 8B, Programs, Case Management, Shared Ontology; boundary
> with Support Delivery at custody/dispatch) — both distinct from this
> roadmap's own numbered "Stage 8: Community Context," which is a separate,
> already-complete numbering track — see
> `HKMP_STAGE8_DONOR_RESOURCE_DOMAIN_DISCOVERY_REPORT.md` §7 for the
> disambiguation this entry resolves.
> ↓ enables: Support Delivery's `fulfilled_from` reference row (§3.4 above)
