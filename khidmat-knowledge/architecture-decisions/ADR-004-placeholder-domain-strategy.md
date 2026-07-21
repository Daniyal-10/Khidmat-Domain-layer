# ADR-004

## Title
Placeholder Domain Strategy

## Status
Accepted

## Context
Declaring domain boundaries before implementation prevents concept drift.
Without declared ownership, concepts get added to whichever domain is
currently active. This produces a bloated registration domain that
owns things it should not, requiring later refactoring. The placeholder
strategy locks ownership before the implementation pressure begins.

## Decision
Future domains (verification-operations, case-management, beneficiary-lifecycle,
volunteer-operations, support-delivery, programs, impact) are declared as
Level 2 placeholders. Each placeholder contains:
- A scope statement
- A list of concepts the domain will own
- An explicit list of concepts it does not own
- A `do_not_implement_until` condition

## Alternatives Considered
- Single large domain: rejected because it produces an unmanageable
  ontology and violates separation of concerns.
- No placeholder declarations: rejected because undeclared boundaries
  are always violated under time pressure.

## Consequences
Developers may not add concepts to placeholder domains. Any concept
that turns out to be needed earlier than expected must be promoted
to the shared domain or the owning domain must be activated.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- architecture-decisions/README.md (ADR index; supersedes the retired DECISIONS.md log)
