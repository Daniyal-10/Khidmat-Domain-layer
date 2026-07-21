# Donor & Resource Domain

## Purpose

Models the canonical humanitarian knowledge surrounding who funds Khidmat's
operations, under what commitment structure and restriction, and what
material and financial resources exist in stock and how they are allocated
before delivery.

This domain does not model finance software, accounting, ERP, procurement
software, warehouse management software, or workflow/business logic. It
models stable humanitarian knowledge: the entities, taxonomies, and
relationships that describe giving, funding commitment, and resource stock,
independent of any single organization's process.

## Maturity: Stage 8B, 8C, and 8D Implemented — Certified Canonical Domain

Authored in two sub-stages:

- **Stage 8B — Donor & Funding Intelligence (implemented):** `donor_profile`,
  `grant`, `contribution`, Islamic Giving taxonomy, funding lifecycle (grant
  status, contribution status, renewal, funding window, restriction
  reference).
- **Stage 8C — Material Resource & Logistics (implemented):** `resource`,
  `financial_resource`, `material_resource`, `inventory_item`,
  `storage_location`, `resource_allocation`, resource classification, stock
  movement classification, storage classification, allocation classification.
  Governed by ADR-028.

Both sub-stages are now present. Stage 8C's implementation did not modify any
Stage 8B entity, taxonomy, relationship, or data property (verified file-by-file
at the time).

- **Stage 8D — Governance Integration (implemented):** ADR-025 through
  ADR-028 ratified; `ontology_authority_matrix.md` and `GLOSSARY.md` updated;
  the five staged boundary-note/reference additions authored in Programs and
  Support Delivery.

Donor & Resource is now a fully certified, canonical part of the Khidmat
Knowledge Layer.

## Owns

### Stage 8B — Donor & Funding

**Entities**
- `donor_profile` — the giving-relationship profile attached BEHIND
  `shared:person` or `shared:organisation` (never both; see
  `ontology/relationships.yaml`).
- `grant` — a funding commitment instance, optionally funding one or more
  `programs:program` (additive to, not a replacement for, the existing
  `programs:program_funded_by` edge).
- `contribution` — a single discrete giving event, standalone or a tranche
  of a `grant`.

**Taxonomies**
- `donor_type`, `donor_engagement_pattern`, `anonymity_level` —
  `taxonomy/donor-classification.yaml`
- `islamic_giving_type`, `zakat_eligible_category` —
  `taxonomy/islamic-giving.yaml`
- `grant_status`, `contribution_status`, `renewal_status` —
  `taxonomy/funding.yaml`

### Stage 8C — Material Resource & Logistics

**Entities**
- `resource` — abstract supertype; owns no allocatable data itself, mirroring
  `shared:subject`'s discipline (ADR-018).
- `financial_resource` — specializes `resource` (`parent: resource`).
- `material_resource` — specializes `resource` (`parent: resource`).
- `inventory_item` — the trackable INSTANCE of a `resource`, at a
  `storage_location`, in a given quantity and condition. Never collapsed
  into `resource`.
- `storage_location` — a warehouse, distribution center, cold-chain
  facility, temporary storage site, or mobile storage unit.
- `resource_allocation` — the decision that reserves or commits a specific
  `inventory_item` to a `programs:program` or `case_management:case_plan`,
  before delivery. Not delivery itself.

**Taxonomies**
- `material_resource_category`, `financial_resource_category`,
  `resource_condition` — `taxonomy/resource-classification.yaml`
- `stock_movement_type` — `taxonomy/stock-movement.yaml` (classification
  scheme only; no per-instance movement log entity is authored — see that
  file's purpose note)
- `storage_location_type` — `taxonomy/storage.yaml`
- `allocation_priority`, `allocation_status`, `reservation_state` —
  `taxonomy/allocation.yaml`

## Does Not Own

- The `Person` and `Organisation` **entities** — owned by
  `shared/ontology/entities.yaml`. `donor_profile` attaches BEHIND these
  references (`profile_of_person`/`profile_of_organisation`), never
  redefining them, mirroring the `volunteer_profile`/`shared:actor` pattern
  (ADR-024, FLAG-006).
- **Program funding classification** (`funding_source_types`,
  `funding_restrictions`, `quota_types`, `compliance_checkpoints`,
  `audit_findings`) — owned by
  `programs/taxonomy/funding-and-compliance.yaml`. `grant` references these
  schemes directly; none is duplicated here.
- The **`programs:program_funded_by` relationship** — owned by
  `programs/ontology/relationships.yaml`, untouched by this domain. This
  domain adds separate, additive reference paths
  (`grant_funds_program`, `resource_allocation_allocated_to_program`),
  authored entirely within this domain's own `relationships.yaml`.
- The **`case_management:case_plan` entity** — owned by
  `case-management/ontology/entities.yaml`, untouched by this domain.
  `resource_allocation_allocated_to_case_plan` is additive-only, authored
  entirely within this domain's own `relationships.yaml`.
- **Any volunteer concept** — skills, certifications, availability,
  capability, capacity, deployment, or the assignment act remain entirely
  Volunteer Operations' concern (ADR-026). No entity, taxonomy, or
  relationship in this domain references, redefines, or duplicates any
  Volunteer Operations concept.
- **The custody chain and delivery execution** — `custody_transfer`,
  `custodian`, `delivery_event`, `proof_of_delivery`, and any dispatch
  workflow remain exclusively Support Delivery's. Inventory ends where
  custody begins (`governance.md` Rule 9): no entity or relationship in this
  domain references any of the four. Support Delivery's own
  `delivery_event_fulfilled_from_resource_allocation` reference row
  (`support-delivery/ontology/relationships.yaml`, added HKMP Stage 8D) is
  authored and owned on the Support Delivery side, not here.
- **Community organisation typology** — owned by
  `community-context/taxonomy/local-organizations.yaml`; referenced when
  typing a community/faith-based donor's underlying `organisation`, never
  re-derived.
- **Zakat eligibility evaluation** — `zakat_eligible_category` is a
  classification a Program's `eligibility_rule` may reference; this domain
  does not evaluate beneficiary eligibility itself.
- **Per-instance stock movement history** (a timestamped log of a specific
  inventory_item's movements) — `stock_movement_type` classifies the KIND of
  movement only; the runtime/instance movement log is deferred, mirroring
  the ADR-023 §19 boundary already applied to Volunteer Operations' Tier 2
  (`taxonomy/stock-movement.yaml` purpose note).

## Directory Structure

```
donor-resource/
├── README.md                          # this file
├── governance.md                      # boundary rules, cross-domain reference patterns
├── ontology/
│   ├── entities.yaml                  # Stage 8B: donor_profile, grant, contribution
│   │                                   # Stage 8C: resource, financial_resource,
│   │                                   # material_resource, inventory_item,
│   │                                   # storage_location, resource_allocation
│   ├── relationships.yaml
│   ├── data-properties.yaml
│   └── semantic-constraints.yaml
└── taxonomy/
    ├── donor-classification.yaml      # Stage 8B
    ├── islamic-giving.yaml            # Stage 8B
    ├── funding.yaml                   # Stage 8B
    ├── resource-classification.yaml   # Stage 8C
    ├── stock-movement.yaml            # Stage 8C
    ├── storage.yaml                   # Stage 8C
    └── allocation.yaml                # Stage 8C
```

No `lifecycle-constraints.yaml` is authored — funding lifecycle
(Stage 8B) and resource/allocation lifecycle (Stage 8C) are both expressed
through taxonomy schemes (`taxonomy/funding.yaml`,
`taxonomy/allocation.yaml`) plus the hard invariants in
`ontology/semantic-constraints.yaml`; no state-machine file was found
necessary at this scope for either sub-stage.

## Related Documents

- `governance.md` — boundary enforcement and cross-domain reference patterns
- `ontology_authority_matrix.md` — Donor & Resource Domain section (integrated
  HKMP Stage 8D)
- `GLOSSARY.md` — Donor & Resource Terms section (integrated HKMP Stage 8D)
- `architecture-decisions/ADR-025-donor-identity-model.md` through
  `ADR-028-resource-model.md` — ratified and indexed in
  `architecture-decisions/README.md` (HKMP Stage 8D)

## Stage 8 Status

HKMP Stage 8 (Donor & Resource Intelligence) is **complete**: 8B (Donor &
Funding), 8C (Material Resource & Logistics), and 8D (Governance Integration)
are all implemented and integrated. The one cross-domain edge anticipated
since Stage 8A's architecture design —
`delivery_event_fulfilled_from_resource_allocation` — is authored, on the
Support Delivery side, in `support-delivery/ontology/relationships.yaml`.

No further Stage 8 work is outstanding. Any future extension (e.g. the
gated "contributed labor as a donor-reported resource" Phase 2 candidate,
DR-FLAG-B in `governance.md`) is a new, separately-governed proposal, not
unfinished Stage 8 scope.
