# ADR-007

## Title
Shared Human Model as a First-Class Knowledge Layer

## Status
Accepted

## Context
Future domains require a consistent representation of human development, household relationships, dependency structures, and capabilities.

Allowing each domain to define its own person model would create ontology drift.

A dedicated human model establishes a single source of truth.

## Decision
Lifecycle stages, capabilities, dependencies, family structures, and health conditions will be modelled in a dedicated Shared Human Model layer.

These concepts are promoted to shared ownership.

## Alternatives Considered
* Defining lifecycle concepts independently in each domain.
* Extending registration ontology to own human concepts.
* Delaying human modelling until beneficiary lifecycle activation.

## Consequences
Future domains must reference the Shared Human Model rather than defining competing human concepts.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- architecture-decisions/README.md (ADR index; supersedes the retired DECISIONS.md log)
