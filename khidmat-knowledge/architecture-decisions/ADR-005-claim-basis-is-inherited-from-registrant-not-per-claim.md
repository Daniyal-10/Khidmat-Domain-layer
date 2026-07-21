# ADR-005

## Title
Claim Basis is Inherited from Registrant, Not Per-Claim

## Status
Accepted

## Context
In most registrations, the registrant's epistemic relationship to the
information is consistent throughout the conversation. A self-registering
beneficiary makes first-hand claims throughout. A volunteer makes
observational claims throughout. Recording basis per-claim when it does
not change would be noisy and add friction to data entry.

## Decision
Each registrant has a `default_claim_basis` (first_hand, second_hand,
observational, or inferred). Claims inherit this basis unless explicitly
overridden. Only claims where the basis differs from the registrant
default need an explicit `claim_basis` value.

## Alternatives Considered
- Per-claim basis with no default: rejected because it increases data
  entry burden without proportional accuracy gain in typical cases.

## Consequences
When the AI detects a claim whose basis should differ from the registrant
default (e.g., a proxy claiming first-hand knowledge of the beneficiary's
emotional state), it must explicitly set `claim_basis` on that claim.
The absence of an explicit value means the registrant default applies.

## Future Review Considerations
Not specified in original decision log.

## Related Documents
- architecture-decisions/README.md (ADR index; supersedes the retired DECISIONS.md log)
