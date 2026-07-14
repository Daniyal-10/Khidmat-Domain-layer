# Beneficiary Lifecycle — Phase 0 Decision Review

## Validation Details
- **Domain**: Beneficiary Lifecycle
- **Status**: Structurally compliant with the canonical repository standards

## Entity vs Value Object
- `beneficiary_lifecycle` is a Core Entity because it has a unique lifecycle identity (`lifecycle_id`) and tracks the state of the beneficiary across multiple cases over time.
- `lifecycle_transition` is an Entity with a distinct `transition_id`, immutably recording state changes.

## Runtime Objects
- The Beneficiary Lifecycle model defines structural states (`engagement_stage`) and transition events. Runtime updates are driven by events from external domains.
- Reasoning triggers blur the line between persistent ontology and Runtime/Reasoning Objects (ADR-023 §19), but are maintained structurally valid pending the Runtime/Instance-State Schema.

## Roles
- Role interactions are implicit via transitions.

## Aggregate Roots
- `beneficiary_lifecycle` serves as the Aggregate Root for the domain, encapsulating the `lifecycle_transition` history which is strictly bound to it via `part_of_lifecycle`.

## Cross-domain ownership
- This domain strictly owns the macro `engagement_stage` state machine.
- It explicitly references cross-domain concepts using CURIEs, including `shared_ontology:subject`, `registration:case`, `verification_operations:verification_finding`, and `shared_risk:risk_characterization`.
- Follows ADR-008 strictly by referencing cross-domain concepts without redefining them.

## Repository DAG
- The repository structure follows standard canonical directories (`ontology/`, `taxonomy/`) preventing circular references. Dependencies point outwards via proper namespaces.

## ADR-023 Promotion Tests
- Ontology entities have been segregated into `entities.yaml`, `data-properties.yaml`, and `relationships.yaml`.
- Semantic and lifecycle constraints have been split appropriately and use target-neutral structure.
- Taxonomies have been broken down into distinct files per scheme, using canonical `schemes:` and `concepts:` lists.
- 100% of legacy concepts successfully mapped to canonical forms.
