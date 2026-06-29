# ADR-017

## Title
Controlled Interim Support Intervention Taxonomy for Verification Operations

## Status
Accepted

## Context
Verification Operations (Stage 4) requires the Support Intervention Taxonomy (Stage 1) to be complete in order to specify what interventions are being verified. However, defining the full, authoritative Support Intervention Taxonomy requires extensive input from programme operations staff, which is currently a blocker. Halting Verification Operations development creates an unacceptable bottleneck.

## Decision
Verification Operations may use a controlled interim Support Intervention taxonomy until the complete, program-validated taxonomy is finalized.

## Alternatives Considered
- Pausing Verification Operations until Stage 1 is fully complete. Rejected because it blocks downstream development of Case Management which relies on verification flows.
- Inventing a Support Intervention Taxonomy solely within the knowledge layer. Rejected because interventions must map to real-world Khidmat operational capacities, not theoretical structures.

## Consequences
The Verification Operations domain is permitted to activate with placeholder or mocked intervention types, assuming Technical Debt. When the authoritative Support Intervention taxonomy is delivered, Verification Operations must be reconciled against it.

## Future Review Considerations
This interim taxonomy must be deprecated the moment the operational Support Intervention Taxonomy is approved.

## Related Documents
- verification-operations/verification-operations.yaml
- knowledge_layer_roadmap.md
