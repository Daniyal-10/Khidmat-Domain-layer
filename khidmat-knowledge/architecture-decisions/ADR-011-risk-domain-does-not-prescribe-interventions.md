# ADR-011

## Title
Risk Domain Does Not Prescribe Interventions

## Status
Accepted

## Context
Intervention logic belongs to Case Management (Stage 5). Mixing risk identification with intervention logic creates a monolithic reasoning layer.

## Decision
The Risk Domain produces signals (risk level, risk trend, compound risk flags) but does not define what should be done in response.

## Alternatives Considered


## Consequences
Risk rules must not recommend interventions.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- architecture-decisions/README.md (ADR index; supersedes the retired DECISIONS.md log)
