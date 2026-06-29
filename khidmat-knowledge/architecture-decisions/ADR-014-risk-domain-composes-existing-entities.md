# ADR-014

## Title
Risk Domain Composes Existing Entities

## Status
Accepted

## Context
Prevents ontology drift and maintains the Shared Human Model as the single source of truth.

## Decision
The Risk Domain references lifecycle stages, capabilities, dependencies, health conditions, and family structures by reference. It does not redefine them.

## Alternatives Considered


## Consequences
Must use `*_ref` patterns defined in risk-domain-governance.md.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- DECISIONS.md
