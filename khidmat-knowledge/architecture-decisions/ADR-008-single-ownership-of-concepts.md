# ADR-008

## Title
Single Ownership of Concepts

## Status
Accepted

## Context
Duplicate ownership creates ontology drift and inconsistent reasoning.

Concepts may be referenced by many files but defined by only one file.

## Decision
Every concept in the knowledge layer must have exactly one authoritative owner.

Ownership is maintained through ontology_authority_matrix.md.

## Alternatives Considered
* Distributed ownership.
* Duplicate definitions across domains.

## Consequences
When a concept appears in multiple locations, one location must be designated canonical and all others become references.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- DECISIONS.md
