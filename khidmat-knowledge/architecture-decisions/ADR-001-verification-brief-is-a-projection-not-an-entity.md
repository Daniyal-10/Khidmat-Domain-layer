# ADR-001

## Title
Verification Brief is a Projection, Not an Entity

## Status
Accepted

## Context
If the brief were stored independently, it would become a second source
of truth about the case. Any update to the case after brief generation
would require a synchronisation step to keep the brief current.
In humanitarian operations, cases are frequently updated — new information
emerges, contact details change, needs are re-classified. A stored brief
would routinely be stale.

A projection approach means the brief is always current because it is
always generated from the canonical record.

## Decision
The Verification Brief is generated from the Case at the point of closure.
It is not stored as an independent entity. It is a point-in-time view
of the Case and its contained entities.

## Alternatives Considered
- Storing the brief independently: rejected due to synchronisation risk.
- Versioning the brief as an entity: rejected as premature complexity for V1.

## Consequences
When a volunteer is assigned, the brief they receive is a snapshot
generated at the moment of assignment. If the case is subsequently
updated before the field visit, a new brief must be generated and
re-issued to the volunteer. This re-issuance mechanism is a
responsibility of the verification-operations domain (not yet active).

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- architecture-decisions/README.md (ADR index; supersedes the retired DECISIONS.md log)
