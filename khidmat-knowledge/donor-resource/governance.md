# Khidmat Donor & Resource — Governance and Documentation

**Authority:** Knowledge Layer Architect
**Source:** Companion governance document for `donor-resource/ontology/*.yaml`
and `donor-resource/taxonomy/*.yaml`
**Governing ADRs:** ADR-025 (Donor Identity Model), ADR-026
(Volunteer Boundary), ADR-027 (Grant Ownership), ADR-028 (Resource
Model) — ratified and integrated into `architecture-decisions/` per HKMP
Stage 8D Governance Integration; drafted in full (pre-ratification) in
`HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 2. Also governed by
ADR-008 (Single Ownership), ADR-009 (Dependency-Driven Domain Activation),
ADR-018 (Shared Subject Supertype — structural precedent), ADR-022 (Canonical
Concepts and Regional Localization Strategy — see Rule 5 below), ADR-024
(Foundational Layer Precedes Operational Activation — structural precedent for
this domain's own two-stage 8B/8C split).
**Purpose:** Boundary-enforcement rules, cross-domain reference patterns, and
flagged boundary cases for the Donor & Resource domain. Written as a
standalone governance document so the YAML files stay flat and mechanical
while single-ownership (ADR-008) is enforced.

---

## Maturity: Stage 8B, 8C, and 8D Implemented — Fully Integrated

This domain is authored in two sub-stages, mirroring the Tier 1 / Tier 2 split
ADR-024 already established for Volunteer Operations:

- **Stage 8B — Donor & Funding Intelligence (implemented).** `donor_profile`,
  `grant`, `contribution`, the Islamic Giving taxonomy, and funding lifecycle
  vocabulary.
- **Stage 8C — Material Resource & Logistics (implemented).** `resource`,
  `financial_resource`, `material_resource`, `inventory_item`,
  `storage_location`, `resource_allocation`, resource classification, stock
  movement classification, storage classification, and allocation
  classification. Governed by ADR-028.

Stage 8C's implementation added to, and did not modify, any Stage 8B entity,
taxonomy, relationship, or data property — verified file-by-file in
`HKMP_STAGE8C_IMPLEMENTATION_REPORT.md` §5.

- **Stage 8D — Governance Integration (implemented).** ADR-025 through
  ADR-028 ratified into `architecture-decisions/`; this domain's ownership
  declared in `ontology_authority_matrix.md`; Glossary terms added to
  `GLOSSARY.md`; the five boundary-note/reference additions in Rule 8 above
  authored; `knowledge_layer_roadmap.md` updated with a disambiguated HKMP
  Stage 8 entry. No ontology was redesigned, and no entity, taxonomy, or
  relationship beyond what Stage 8B/8C already staged was added — see
  `HKMP_STAGE8D_INTEGRATION_REPORT.md`.

---

## Boundary Enforcement Rules (per file)

### 1. `donor_profile` vs. `shared:person` / `shared:organisation` (ADR-025, ADR-008, ADR-018)
- `donor_profile` (`ontology/entities.yaml`) owns the giving-relationship
  profile only: segmentation, anonymity posture, and the aggregation point
  for grants/contributions.
- It **must not** redefine or duplicate `person` or `organisation`
  (`shared/ontology/entities.yaml`) — name, contact, demographic data,
  organisation type all remain exclusively theirs. It attaches *behind*
  whichever applies via `profile_of_person`/`profile_of_organisation`
  (`ontology/relationships.yaml`; renamed from a shared `profile_of` per
  HKMP Stage 8R Certification Remediation, no semantic change), never
  minting a third identity concept (the FLAG-005 failure mode this ADR was
  written specifically to avoid repeating).
- A `donor_profile` attaches to **at most one** of `person`/`organisation`,
  never both — enforced by `donor_profile_attachment_exclusive`
  (`ontology/semantic-constraints.yaml`).
- Zero attachment is an **explicitly permitted** state (a genuinely
  untraceable donor), not an error or an omission.

### 2. `grant` vs. Programs' funding classification (ADR-027, ADR-008)
- `grant` owns the funding-commitment **instance** and its lifecycle/window/
  renewal state.
- It **must not** redefine `funding_source_types`, `funding_restrictions`,
  `quota_types`, `compliance_checkpoints`, or `audit_findings`
  (`programs/taxonomy/funding-and-compliance.yaml`) — `grant.funding_source_type`
  and `grant.funding_restriction` (`ontology/data-properties.yaml`) reference
  those schemes by `taxonomy_ref`, and no parallel scheme is authored in
  `taxonomy/funding.yaml`.
- It **must not** modify `programs:program_funded_by`
  (`programs/ontology/relationships.yaml`). The additive funding path
  (`grant_funds_program`) is authored entirely within this domain's own
  `ontology/relationships.yaml`, referencing `programs:program` by CURIE —
  zero lines are added to or changed in any Programs file.

### 3. Volunteer exclusion (ADR-026, ADR-008, ADR-009)
- This domain owns **zero** volunteer-related content, in this pass and for
  the foreseeable Stage 8C pass as currently scoped.
- Every term in the original Stage 8 brief's volunteer list (volunteers,
  volunteer resources, capability, skills, availability, assignment,
  capacity, specialization, certification, deployment) is either already
  owned by Volunteer Operations' foundational tier or explicitly deferred to
  its Tier 2 (ADR-024) — this domain is not a party to either category and
  authors no reference to `volunteer_profile`, `volunteer_team`, or any
  Volunteer Operations taxonomy.
- Any future "contributed labor as a donor-reported resource" requirement is
  a separately-governed Phase 2 addition (ADR-026, Alternative B),
  gated on its own review — not authored speculatively here.

### 4. Islamic Giving vs. Programs' eligibility engine (ADR-027 discussion, §16 of the discovery report)
- `zakat_eligible_category` (`taxonomy/islamic-giving.yaml`) is a
  classification a Program's `eligibility_rule`
  (`programs/ontology/entities.yaml`) **may** reference. It is **not** a
  second eligibility-evaluation mechanism.
- This domain does not evaluate beneficiary eligibility, does not gate
  enrollment, and does not author any relationship into Case Management or
  Registration to that effect.

### 5. Islamic Giving vs. ADR-022 (Regional Localization Strategy)
- `islamic-giving.yaml`'s seven giving-type concepts (zakat, sadaqah,
  sadaqah_jariyah, waqf, fidya, kaffarah, qurbani) and the eight
  `zakat_eligible_category` concepts are **not** subject to ADR-022's
  regional-synonym-collapse discipline (the discipline that produced e.g.
  `micro_savings_and_credit_collective` replacing "SHG"/"Chama"/"Stokvel").
  Each is an independently defined religious-legal category, not a regional
  alias for a generic concept. This is stated explicitly here, and in
  `taxonomy/islamic-giving.yaml`'s own purpose note, so a future ADR-022
  compliance audit does not mistake deliberate non-collapse for a violation.

### 6. Donor classification vs. Programs' funding classification (§16 of the discovery report)
- `donor_type` (`taxonomy/donor-classification.yaml`) classifies the giving
  **party**. `funding_source_types`
  (`programs/taxonomy/funding-and-compliance.yaml`) classifies a **program's**
  funding category. Both axes may be populated for the same funding
  relationship without duplication — see the `distinct_from` reference block
  at the end of `donor-classification.yaml`.

---

## Cross-Domain Reference Patterns

### Pattern: Donor Profile → Shared Person / Organisation
`profile_of_person` / `profile_of_organisation` (distinct verbs per HKMP
Stage 8R Certification Remediation), cardinality 0..1 on each of two
relationship rows (`donor_profile_of_person`, `donor_profile_of_organisation`),
mutually exclusive, both optional. Mirrors `volunteer_profile_profile_of_actor`
(`volunteer-operations/ontology/relationships.yaml`) applied to a two-target
case.

### Pattern: Grant → Programs Program (additive funding path)
`grant_funds_program`, authored entirely within
`donor-resource/ontology/relationships.yaml`, referencing `programs:program`
by CURIE. No row is added to `programs/ontology/relationships.yaml`. This is
the same "referencing domain owns the edge" discipline already used by
`volunteer_profile_affiliated_with_organisation` and
`case_plan_addressed_by_intervention`.

### Pattern: Grant / Contribution → Programs Funding Taxonomy (reference, not duplication)
`grant.funding_source_type` and `grant.funding_restriction`
(`ontology/data-properties.yaml`) use `taxonomy_ref` to point directly at
`programs/taxonomy/funding-and-compliance.yaml`'s existing schemes. Mirrors
`needs-assessment`'s `need_severity` referencing
`registration_tax:need_severity`.

### Pattern: Donor Classification → Community Context (typing reference, deferred to instance data)
A community or faith-based donor's underlying `organisation` may itself be
typed via `community-context/taxonomy/local-organizations.yaml` (e.g.
`local_philanthropic_trust`, `faith_based_organization`) — that typing is
Community Context's own field on the `organisation`/local-collective side,
not a relationship this domain authors. No row in this domain's
`relationships.yaml` references Community Context directly.

### Pattern: Resource Allocation → Programs Program / Case Management Case Plan (additive targets)
`resource_allocation_allocated_to_program` and
`resource_allocation_allocated_to_case_plan`, both authored entirely within
`donor-resource/ontology/relationships.yaml`, referencing `programs:program`
and `case_management:case_plan` by CURIE respectively. No row is added to
either domain's own relationship file — the same "referencing domain owns
the edge" discipline as `grant_funds_program` (Stage 8B).

### Pattern: Inventory Item → Resource (polymorphic type reference)
`inventory_item_instance_of_resource` targets the abstract `resource`
supertype directly (domain-internal, not cross-domain), mirroring
`beneficiary_lifecycle_tracks_journey_of_subject`
(`beneficiary-lifecycle/ontology/relationships.yaml`), which targets
`shared:subject` directly rather than requiring a row per concrete subtype.

### Pattern: Material/Financial Resource Classification → Programs / Support Delivery Taxonomy (reconciliation, not reference)
`material_resource_category` (`taxonomy/resource-classification.yaml`) does
not reference `programs:intervention_modality` or
`support_delivery:delivery_modality` via `taxonomy_ref` — the three schemes
classify different things at different scopes (stock kind vs. catalogued
offering form vs. delivery-event handling) and none is derived from another.
The relationship is a `distinct_from` reconciliation note (this file's own
`references:` block), not a `taxonomy_ref` reference, since there is no
value to inherit from the other schemes — only an ambiguity to prevent.

---

## Ontology Boundary Rules

### 7. `contribution_status#allocated` vs. `resource_allocation` (Stage 8B/8C seam)
`contribution_status#allocated` (`taxonomy/funding.yaml`, Stage 8B) describes
a contribution's funds having a designated purpose within the funding
chain — it is **not** the Stage 8C `resource_allocation` entity
(`ontology/entities.yaml`), which is the decision reserving/committing a
specific tracked `inventory_item`. The two are related but independent: a
`resource_allocation` may optionally be `funded_by_contribution` a
`contribution` (`ontology/relationships.yaml`; renamed from a shared
`funded_by` per HKMP Stage 8R Certification Remediation) whose own
`contribution_status` happens to be `allocated`, but neither property drives
or is derived from the other.
`taxonomy/funding.yaml`'s own note on `contribution_status#allocated`
records this distinction explicitly.

### 8. Modification to certified domains is additive-only, and limited to Stage 8D
No file outside `donor-resource/` was created or modified by either the
Stage 8B or Stage 8C implementation pass — every cross-domain fact through
Stage 8C was expressed as an outbound reference authored within this
domain's own files. HKMP Stage 8D Governance Integration subsequently made
five narrow, explicitly-staged additions to existing files (all previously
staged before being integrated): a `distinct_from` note in
`programs/taxonomy/funding-and-compliance.yaml`, an extended `distinct_from`
note in `support-delivery/taxonomy/delivery-modalities.yaml`, a documentation
note on `programs:eligibility_rule`, a documentation note on
`support_delivery:delivery_event`, and one new relationship row in
`support-delivery/ontology/relationships.yaml`
(`delivery_event_fulfilled_from_resource_allocation`, authored on the
Support Delivery side, per Rule 9). No row or entity owned by this domain
was ever authored anywhere but here; every addition to another domain's
files was either documentation-only or an edge authored by the domain that
owns the edge's `from` entity.

### 9. Support Delivery boundary: inventory ends where custody begins
`inventory_item`, `storage_location`, and `resource_allocation` model
everything **before** goods enter the custody chain. No entity or
relationship in this domain references, models, or duplicates
`custody_transfer`, `custodian`, `delivery_event`, `proof_of_delivery`, or
any dispatch workflow (all exclusively Support Delivery's,
`support-delivery/ontology/entities.yaml`). The boundary is the moment stock
is dispatched (`stock_movement_type#dispatch`,
`taxonomy/stock-movement.yaml`) — modeled here only as a classification
value, never as an event this domain tracks the progress of. Support
Delivery's own `delivery_event_fulfilled_from_resource_allocation` reference
row (`support-delivery/ontology/relationships.yaml`, added per HKMP Stage
8D) is authored and owned on the Support Delivery side — this domain grants
no reciprocal reference back into `delivery_event`, `custody_transfer`,
`custodian`, or `proof_of_delivery` in exchange.

### 10. Resource type/instance split is non-negotiable (ADR-028)
`resource`, `financial_resource`, and `material_resource` describe WHAT KIND
of thing exists; they own no quantity, condition, or location. `inventory_item`
describes HOW MUCH of a kind exists, in what condition, WHERE, right now. No
future extension may collapse these — e.g. adding a quantity field directly
to `material_resource` would violate this rule and must be rejected in
review.

### 11. Storage and cold-chain are physical concepts, not software
`storage_location` and `storage_location_type` (`taxonomy/storage.yaml`)
classify physical storage space only. No database, tracking system,
application, or software concept is modeled as a `storage_location`.

---

## Flagged Boundary Cases (domain-local; integrated into `ontology_authority_matrix.md` per HKMP Stage 8D)

### DR-FLAG-A: Donor-as-role vs. a future shared `funding_source_party` supertype
`donor_profile` attaches to `person`/`organisation` via two separate
relationship rows today (Alternative B, per
`HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 1 Decision 1). If a second
future domain independently needs a generic Person-or-Organisation
abstraction, promoting to a shared supertype (Alternative C, rejected for now
as disproportionate for a single consumer) should be revisited — not before.

### DR-FLAG-B: Contributed labor as a donor-reported resource
Named in ADR-026 as a gated Phase 2 candidate. Not authored in Stage
8B or the currently-scoped Stage 8C. Any future authoring must re-run the
volunteer-boundary analysis in ADR-026 against Volunteer Operations'
state at that time, not assume this pass's analysis remains current
indefinitely.

### DR-FLAG-C: `consumable` / `equipment` / `asset` as entities vs. taxonomy values — RESOLVED
Resolved during Stage 8C implementation: `consumable`, `equipment`, and
`asset`-like distinctions are modeled as `material_resource_category`
taxonomy values (`taxonomy/resource-classification.yaml` — `food`,
`medicine`, `medical_equipment`, `vehicles`, etc.), not as separate entities.
No property divergence was found at this maturity to justify entity-level
specialization beyond `material_resource` itself: `cold_chain_required` (the
one genuinely structural per-kind property difference identified —
medicine-like categories vs. durable-equipment-like categories) is captured
as a single boolean data property on `material_resource`, applicable
regardless of category, rather than as an entity-splitting criterion. If a
future category requires materially different structured properties (not
just a different category label), revisit this resolution against that
concrete evidence — not speculatively.

### DR-FLAG-D: Cross-domain namespace additions in this pass
Stage 8C added `case_management` to `ontology/relationships.yaml`'s
`namespaces:` block (Stage 8B had declared only `shared` and `programs`).
This is an addition to the namespace map, not a modification of any Stage 8B
relationship row's own content — recorded here so a future reviewer
distinguishes "extended the map" from "changed what Stage 8B said."
