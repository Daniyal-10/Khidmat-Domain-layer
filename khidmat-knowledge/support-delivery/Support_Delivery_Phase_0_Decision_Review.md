# Phase 0 Decision Review: Support Delivery

This document captures the final architectural decisions required before freezing the business model and commencing ontology and taxonomy authoring for the Support Delivery domain.

## 1. Fundamental Unit of Delivery
**Decision:** The fundamental unit is the **Delivery Event**.
**Rationale:** A single delivery action (e.g., a truck visiting a village or a volunteer arriving at a household) may bundle multiple `DeliveryItem`s, fulfill multiple `CasePlan`s, and result in multiple handovers. By grounding the model in the `DeliveryEvent` rather than the `InterventionExecution` or `DeliveryItem`, we preserve the real-world operational truth: logistics schedules events, and items are fulfilled as a consequence of those events.

## 2. Modeling Execution of Services vs. Physical Deliveries
**Decision:** Yes, Support Delivery must model both.
**Terminology:** We will use **Assistance Event** or **Execution Event** as the broad parent class, with `PhysicalHandover` and `ServiceFulfillment` as its primary specializations.
**Rationale:** The `CasePlan` does not differentiate between scheduling a food drop and scheduling a medical check-up. The Support Delivery domain must represent the conclusion of both types of assistance, though the `ProofOfDelivery` mechanisms will differ (e.g., photo of goods vs. signed timesheet).

## 3. Community-level Delivery
**Decision:** Classify now without changing existing domains. Requires no ADR.
**Rationale:** A community-level delivery (e.g., installing a water pump) can be modeled as a `DeliveryEvent` that references a `CommunityContext` or `Location` rather than a specific `Beneficiary`. The downstream `Outcome` measurement will track the community benefit. This avoids the need to invent a new `CommunityPlan` in Case Management.

## 4. Chain of Custody
**Decision:** Scope entirely within Support Delivery for V1. Requires no ADR.
**Rationale:** Chain of Custody is fundamentally a sequence of `Handover` states prior to the final `BeneficiaryHandover`. Creating a separate 'Integrity' domain is premature. We can model `CustodyTransfer` as a subclass of a broader `DeliveryEvent` entirely within the bounds of this domain.

## 5. Other Expensive Architectural Decisions
- **Proof Quality as a First-Class Concept:** We must decide if `ProofQuality` (e.g., blurred photo, illegible signature) is a property of `ProofOfDelivery` or a distinct verification entity that loops back to the Verification Operations domain.
  *Decision:* `ProofQuality` should be a property of `ProofOfDelivery` within Support Delivery to prevent circular dependencies with Verification Operations.
- **Handling Partial Fulfillments:** A `DeliveryEvent` might only deliver 5 out of 10 items.
  *Decision:* Support Delivery will log the *actual delivered quantity*. It is the responsibility of Case Management to reconcile this against the `CasePlan` and decide if the intervention is complete or if another delivery is needed. Support Delivery does not own the completion logic of the Case Plan.

## Recommendation
**Proceed to Implementation.**
All major structural and boundary ambiguities have been resolved in Phase 0. No further architectural decisions (ADRs) are required. We are ready to begin authoring the canonical ontology, taxonomy, and reasoning logic.
