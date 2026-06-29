# Transition Semantics Recommendations
**Date**: 2026-06-29
**Domain**: Beneficiary Lifecycle
**Context**: Phase 4 Knowledge Engineering Improvements

## Objective
Review `LifecycleTransition` attributes (`exit_reason`, `suspension_reason`, `review_trigger`) to determine whether they should be mutually constrained by transition type, preparing for future reasoning logic.

## Analysis
Currently, `LifecycleTransition` defines these attributes as optional:
- `exit_reason`
- `suspension_reason`
- `review_trigger`

When a transition occurs, only the reason corresponding to the `new_stage` (the transition type) should be populated. Allowing multiple reasons (e.g., both an `exit_reason` and a `suspension_reason`) on a single transition event creates semantic ambiguity.

## Recommendations for Future Reasoning Constraints

### 1. Mutually Exclusive Payload Constraints
We recommend introducing a `SHACL` or equivalent constraint to enforce mutual exclusivity based on the `new_stage`:
* **If `new_stage` == `exited`:** `exit_reason` MUST be present. `suspension_reason` and `review_trigger` MUST be null.
* **If `new_stage` == `suspended`:** `suspension_reason` MUST be present. `exit_reason` and `review_trigger` MUST be null.
* **If `new_stage` == `review_required`:** `review_trigger` MUST be present. `exit_reason` and `suspension_reason` MUST be null.
* **For all other stages:** All three attributes SHOULD be null, as they represent specific anomaly/terminal transitions.

### 2. Transition Subclasses (OWL Readiness)
For a more mature RDF/OWL representation in the future, consider defining subclasses of `LifecycleTransition` instead of placing optional properties on a monolithic class:
* `ExitTransition` (subclass of `LifecycleTransition`) -> strictly owns `exit_reason`
* `SuspensionTransition` (subclass of `LifecycleTransition`) -> strictly owns `suspension_reason`
* `ReviewTransition` (subclass of `LifecycleTransition`) -> strictly owns `review_trigger`

This prevents sparsity in the ontology and leverages structural type constraints rather than conditional property constraints.

**Next Steps**: Do not implement these logic constraints yet. They are documented here to guide the next phase of formal reasoning and ontology typing.
