# Community Context Domain

## Purpose

Models the geographic, infrastructural, environmental, and social fabric that a
household sits inside — the context Khidmat's Business Blueprint calls the
"Community Model": settlement type, accessibility, hazards, seasonal events,
essential services, local organisations, and livelihood patterns.

## Scope

Substantially built out (12 taxonomy files, a full ontology module), but authored
**before** the canonical `ontology/`+`taxonomy/` contract was frozen. It is the
next domain targeted for migration onto
`docs/architecture/Canonical_Ontology_Schema.md` / `Canonical_Taxonomy_Schema.md`
(see `docs/architecture/Repository_Migration_Methodology.md`) — its content is not
in question, its file structure is.

## Owns

- **Entities:** `community`, `geographic_area`, `built_infrastructure`,
  `natural_resource`, `transportation_network_asset`, `local_collective`
  (`ontology/entities.yaml`)
- **Taxonomy (each file has an exclusive, non-overlapping boundary — see
  `community-context-governance.md`):**
  - `transportation.yaml` — routes, edges, transit nodes
  - `infrastructure-types.yaml` — built infrastructure that isn't transportation
  - `community-assets.yaml` — non-infrastructural natural resources
  - `accessibility.yaml` — access-mode constraints
  - `physical-environment.yaml` — pure physical geography
  - `geographic-hierarchy.yaml` — spatial granularity levels
  - `settlement-types.yaml` — settlement formality
  - `local-organizations.yaml` — community-native, informal collectives
  - `community-hazards.yaml`, `seasonal-events.yaml`, `essential-services.yaml`,
    `livelihood-patterns.yaml`

## Does Not Own

- Formally registered/statutory organisations (hospitals, government offices,
  international NGOs) — owned by `shared/taxonomy/organisations.yaml`; only
  community-native, informal collectives are modeled here.
- Individual beneficiary data or tracking (owned by `registration/` /
  `beneficiary-lifecycle/`) — this domain owns macro-level, population-shared
  systemic patterns only.
- Mutable operational state (e.g. a route being temporarily closed) — taxonomy
  here is immutable semantic classification; mutable instance state belongs in a
  downstream ontology/runtime layer.
- Population & demographics, market integration, governance & institutions,
  social cohesion/exclusion dynamics, culture, safety & security, and public
  health context — all explicitly deferred (see `_placeholder.yaml` and
  `community_context_discovery_report.md`) until Volunteer Operations or Support
  Delivery need them.

## Directory Structure

```
community-context/
├── taxonomy/
│   ├── accessibility.yaml
│   ├── community-assets.yaml
│   ├── community-hazards.yaml
│   ├── essential-services.yaml
│   ├── geographic-hierarchy.yaml
│   ├── infrastructure-types.yaml
│   ├── livelihood-patterns.yaml
│   ├── local-organizations.yaml
│   ├── physical-environment.yaml
│   ├── seasonal-events.yaml
│   ├── settlement-types.yaml
│   └── transportation.yaml
├── ontology/
│   ├── entities.yaml
│   ├── relationships.yaml
│   ├── lifecycle-constraints.yaml
│   └── semantic-constraints.yaml
├── community-context-governance.md          # boundary rules between the 12 taxonomy files
├── community_context_discovery_report.md    # architecture discovery and deferred scope
└── _placeholder.yaml                        # deferred scope areas (see "Does Not Own")
```

## Related Documents

- `community-context-governance.md` — the authoritative boundary rules between
  this domain's own taxonomy files
- `community_context_discovery_report.md` — architecture discovery
- `docs/architecture/Canonical_Ontology_Schema.md`,
  `Canonical_Taxonomy_Schema.md` — the contract this domain will migrate onto
- `docs/architecture/Repository_Migration_Methodology.md` — the migration process
- `knowledge_layer_roadmap.md` — Stage 8 (Community Context)
