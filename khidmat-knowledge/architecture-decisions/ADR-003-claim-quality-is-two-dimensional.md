# ADR-003

## Title
Claim Quality is Two-Dimensional

## Status
Accepted

## Context
A single quality score collapses two different problems. A claim can be
complete (all key information is present) but contradictory (the stated
facts conflict with each other). It can also be consistent (no internal
contradictions) but partial (important details are missing).

These require different responses: sufficiency gaps require more questions;
consistency failures require gentle challenge and clarification.
A combined score would produce incorrect responses — more questions
when what is needed is a challenge, or a challenge when what is needed
is more questions.

## Decision
Claim quality is assessed along two independent axes:
`information_sufficiency` (how much do we know) and
`information_consistency` (does what we know hold together).

## Alternatives Considered
- Single quality score: rejected because it produces incorrect AI behaviour.
- Three or more dimensions: rejected as over-engineering for V1.

## Consequences


## Future Review Considerations
Not specified in original decision log.

## Related Documents
- DECISIONS.md
