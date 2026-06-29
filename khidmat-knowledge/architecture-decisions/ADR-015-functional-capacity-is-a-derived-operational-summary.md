# ADR-015

## Title
Functional Capacity is a Derived Operational Summary

## Status
Accepted

## Context
During the Foundation Audit Remediation, it was identified that the unctional_capacity attribute in persons.yaml (full, partial, dependent) was an early proto-capability concept that predated the mature Shared Human Model layer. With capabilities.yaml fully established as the authoritative capability vocabulary, unctional_capacity faced the risk of being a competing source of truth.

## Decision
The unctional_capacity enum is formally declared a derived operational summary rather than an independent authoritative trait. The capabilities.yaml ontology remains the authoritative source for all physical, cognitive, and social function assessment.

## Alternatives Considered
- Deprecating unctional_capacity entirely. Rejected because it provides a useful high-level heuristic for operational triage that is harder to calculate dynamically in simple views.
- Moving unctional_capacity ownership to the Shared Human Model. Rejected to keep the Shared Human Model focused on atomic traits rather than derived statuses.

## Consequences
Any future reasoning rules that depend on unctional_capacity must trace back to the authoritative capabilities defined in capabilities.yaml. Alignment tasks will cross-reference the summary to the granular capabilities.

## Future Review Considerations
Review if the operational summary becomes redundant once complex capability querying is fully integrated into the client application layer.

## Related Documents
- shared/taxonomy/persons.yaml
- shared/human-model/capabilities.yaml
- ontology_authority_matrix.md
