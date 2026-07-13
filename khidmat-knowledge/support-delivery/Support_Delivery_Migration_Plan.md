# Support Delivery Migration Plan

## Phase 0 Decisions
- **Fundamental Unit**: The `DeliveryEvent` is the core structural unit, grouping multiple items or services.
- **Scope of Execution**: Support Delivery models both `PhysicalHandover` and `ServiceFulfillment`.
- **Domain Boundaries**: Support Delivery will strictly own the execution of assistance. It will not own eligibility or planning.
- **Dependency Strategy**: We will rely entirely on cross-domain references to `registration`, `case-management`, and `volunteer-operations` rather than duplicating any concepts.
- **Standardization**: Will follow the Canonical Ontology Schema and Canonical Taxonomy Schema exactly.

## Migration Phases
- **Phase 1: Discovery & Audit** (Completed)
- **Phase 2: Phase 0 Decision Review** (Completed)
- **Phase 3: Ontology Drafting** (Defining the core classes: DeliveryEvent, ProofOfDelivery, Handover)
- **Phase 4: Taxonomy Drafting** (Defining the state transitions, exception types, modalities)
- **Phase 5: Reasoning Rules** (Drafting the business logic for state changes and exception handling)
- **Phase 6: Canonical Implementation** (Authoring the final YAMLs)

## D-SD Decision Table
| Concept | Current Owner | Target Owner | Decision | Justification |
|---|---|---|---|---|
| Delivery Event | None | Support Delivery | Create | Core responsibility of SD, fundamentally grouping logistics. |
| Proof of Delivery | None | Support Delivery | Create | Necessary for accountability loop. |
| Chain of Custody | None | Support Delivery | Create | Scoped as `CustodyTransfer` within SD to avoid new domains. |
| Community-Level Delivery | None | Support Delivery | Create | Handled by referencing Location/CommunityContext instead of Beneficiary. |
| Volunteer Assignment | Volunteer Ops | Volunteer Ops | Reference | Respect ADR-008. |
| Case Plan | Case Management | Case Management | Reference | Respect ADR-008. |
| Partial Fulfillment | None | Case Management / SD | Split | SD logs actual quantity; CM calculates remaining need. |

## Content Gap Log
- `DeliveryException` (Needs formal taxonomy of reasons).
- `ServiceFulfillment` vs `PhysicalHandover` distinctions.

## Mechanical Work
- Set up directory structure for `support-delivery/` (ontology, taxonomy, reasoning, examples).
- Create skeleton YAML files adhering to canonical schemas.

## Human-authoring Work
- Define the precise semantic meaning of "Delivered" vs "Handed Over".
- Define the acceptable forms of Proof of Delivery in the humanitarian context.
- Outline the resolution pathways for Delivery Exceptions.

## Phase Gates
- **Gate 1**: Audit Approval (Completed).
- **Gate 2**: Phase 0 Decisions Frozen (Current).
- **Gate 3**: Schema Validation (Pre-YAML).
- **Gate 4**: Cross-domain consistency check (Ensuring no cycles).
- **Gate 5**: Final Merge Approval.
