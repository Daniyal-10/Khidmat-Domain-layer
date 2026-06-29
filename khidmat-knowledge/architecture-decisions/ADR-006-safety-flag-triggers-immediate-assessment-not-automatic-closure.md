# ADR-006

## Title
Safety Flag Triggers Immediate Assessment, Not Automatic Closure

## Status
Accepted

## Context
In domestic violence situations, a safety flag is raised automatically.
But the beneficiary may have already moved to a safe location, or may
have a specific safe contact protocol that makes verification feasible.
Automatically marking cases as `unsafe_to_verify` without assessment
would block legitimate verifications and increase case review burden
unnecessarily.

## Decision
When a safety flag is raised during registration, the AI must conduct
a safety assessment before closing the case, but the case is not
automatically marked `unsafe_to_verify`. The outcome of the assessment
determines the final status.

## Alternatives Considered
- Automatic `unsafe_to_verify` on any safety flag: rejected as too blunt.
- No safety gate at all: rejected as a safeguarding failure.

## Consequences
The AI must ask the safety assessment question in every case where a
safety flag is raised. The question and the response must be recorded
in `situation.safety_notes`. The resulting status depends on the answer.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- DECISIONS.md
