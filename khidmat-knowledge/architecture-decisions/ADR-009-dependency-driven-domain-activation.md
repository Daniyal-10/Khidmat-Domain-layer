# ADR-009

## Title
Dependency-Driven Domain Activation

## Status
Accepted

## Context
Premature activation causes domains to invent concepts they do not own.

Dependency-first activation preserves architectural integrity.

## Decision
Domains activate according to the dependency order defined in knowledge_layer_roadmap.md.

Placeholder domains remain inactive until prerequisites are satisfied.

## Alternatives Considered
* Activating domains on implementation demand alone.
* Allowing placeholder domains to define concepts early.

## Consequences
Roadmap dependencies become governance constraints.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- architecture-decisions/README.md (ADR index; supersedes the retired DECISIONS.md log)
