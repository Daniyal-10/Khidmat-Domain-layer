# ADR-016

## Title
Lifecycle Descriptive Placeholders Remain Descriptive Until Ontology Stabilization

## Status
Accepted

## Context
The lifecycle-stages.yaml file was created before dependency.yaml and capabilities.yaml. Consequently, it uses string descriptions to define the characteristic dependencies and capabilities associated with each life stage. Although the capability and dependency taxonomies are now complete, retrofitting strict references into the lifecycle stages immediately poses an architectural churn risk before the ontology is globally stabilized.

## Decision
Lifecycle descriptive placeholders in lifecycle-stages.yaml will remain descriptive until the knowledge layer achieves total ontology stabilization. Hard references will be introduced only when appropriate.

## Alternatives Considered
- Immediately refactoring lifecycle-stages.yaml to use strict IDs (e.g., capability_ref). Rejected because it requires premature rewriting of an accepted file and distracts from downstream domain activation.

## Consequences
The descriptive strings in lifecycle-stages.yaml must not be treated as a shadow taxonomy. Automated agents and human architects must understand that these are informal annotations pointing conceptually to the authoritative files.

## Future Review Considerations
Once Case Management and Support Delivery are active and the core entity structures are locked, a refactoring sprint should formalize these references.

## Related Documents
- shared/human-model/lifecycle-stages.yaml
- knowledge_layer_inventory.md
- ontology_authority_matrix.md
