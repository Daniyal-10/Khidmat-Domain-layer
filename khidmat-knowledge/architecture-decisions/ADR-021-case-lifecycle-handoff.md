# ADR-021

## Title
Case Lifecycle Handoff Between Registration and Case Management

## Status
Accepted

## Context
The Authority Matrix declares `Case` as owned by Case Management. However, the Registration domain also defines a `case` entity with its own `case_statuses` (`in_progress`, `ready_for_verification`, `requires_review`, `unsafe_to_verify`, `duplicate_suspected`, `on_hold`, `referred_externally`). Case Management defines `case_status` values (`opened`, `planning`, `active`, `suspended`, `closed`). There is no declared relationship between these two status vocabularies or whether they describe the same entity.

## Decision
The two status vocabularies (`registration/taxonomy/case-outcomes.yaml#case_statuses` and `case-management/taxonomy.yaml#case_status`) are declared as sequential phases of the same lifecycle for the exact same `Case` entity. The `Case` entity is canonical and owned by Case Management. The Registration phase statuses represent pre-operational readiness states. When a case completes the registration phase (e.g., transitions beyond `ready_for_verification`), it undergoes a phase transition to the Case Management lifecycle, typically starting at `opened`. No new entity is created; the `Case` persists across this handoff.

## Alternatives Considered
- Declaring the Registration Case as a distinct entity `RegistrationRecord` that promotes to a Case Management `Case` at a handoff event: Rejected because it introduces unnecessary entity duplication for the same real-world object.

## Consequences
- The seam between the Registration and Case Management domains is explicitly defined.
- AI agents reasoning about a case's state can seamlessly map a registration-phase case to its operational case management phase.
- No changes to existing ontology structure or definitions are required, only this governance declaration.

## Future Review Considerations
Review if/when additional domains introduce their own intermediate statuses.

## Related Documents
- `DECISIONS.md`
- `ontology_authority_matrix.md`
