# Case Management Domain Migration Plan

## Context
This migration plan is the result of auditing the existing Level 1 `taxonomy.yaml` and `ontology.yaml` against the comprehensive Business Discovery Phase documents, specifically enforcing ADR-023 (Value Objects & Roles) and the strict boundary delineations for the Khidmat Humanitarian Operating System. 

This document serves as the blueprint for the upcoming clean refactor of the Case Management YAMLs.

---

### 1. Concepts that are still correct
- **`Case` (Entity):** The central coordination container correctly remains an Entity.
- **`CasePlan` (Entity):** Correctly modeled as an Entity, given it is a complex, versionable operational strategy that aggregates multiple interventions.
- **Taxonomy Foundations:** `priority_level` and `case_origin` are structurally sound, though their specific values may need slight expansion.

### 2. Concepts that must be removed
- **`CaseOutcome` (Entity):** Must be removed as an independent Entity. An outcome is not a distinct referenceable thing; it is a terminal state fact bundle about the Case. It must be collapsed into the `Case` entity's state properties.

### 3. Concepts that must be renamed
- **`case_status: closed`:** Should be refined or supplemented with `graduated` to differentiate a successful completion from a generic closure.
- **`case_assignment_status`:** If `CaseAssignment` becomes a Role, the concept of a "historical" assignment shifts to the temporal tracking of that Role (e.g., `Role.end_date`), meaning this specific taxonomy might be deprecated or renamed to `role_status`.

### 4. Entities that should become Value Objects (ADR-023 Enforcement)
The current ontology suffers from "Entity Explosion" by promoting fact bundles into full Entities. The following must be demoted to **Value Objects** embedded within the `Case` or `CasePlan`:
- **`Referral`:** A request sent to another agency. It has no meaning outside the Case.
- **`FollowUp`:** A scheduled event.
- **`CaseNote`:** A qualitative observation.
- **`TimelineEntry` (New):** To replace the need for "historical" entities by logging state changes.

### 5. Entities that should become Roles (ADR-023 Enforcement)
- **`CaseAssignment`:** This is currently modeled as an Entity connecting a Case to an Actor. Per ADR-023, this is a **Role**. It must be replaced by explicitly defined Roles: `StatutoryOwner`, `LeadCoordinator`, and `ParticipatingAgency`, which are assumed by `Actor` entities.

### 6. Missing Runtime Objects
The ontology entirely misses diagnostic outputs and events generated during active case management:
- **`Escalation`:** A reasoning-produced finding (e.g., "Referral Stalled for 30 days").
- **`ReviewDecision`:** The output of a Case Conference that triggers a change in the Case Plan.
- **`Recommendation`:** System-suggested interventions.
*(These will not be in the ontology YAML, but must be explicitly reserved per ADR-023 §19).*

### 7. Missing Lifecycle States
- **In `case_status`:** Missing `graduated` (success) and `reopened` (reactivation).
- **Missing Taxonomy:** `suspension_reason`. The `suspended` state exists, but lacks the crucial reason (e.g., `funding_exhausted`, `statutory_hold`, `beneficiary_refusal`).
- **Missing Taxonomy:** `delegation_status` (e.g., active, revoked) for statutory handoffs.

### 8. Missing Relationships
- **Funding/Programs Boundary:** Missing a relationship like `constrained_by_program` to link a Case/CasePlan to the external `Program` entity (for funding dependency).
- **Statutory Custody:** Missing relationships reflecting `has_statutory_owner` and `has_lead_coordinator` (once the Roles are established).
- **Community Context:** Missing a way to link a Suspended Case to a `CommunityEvent` (like a mass disaster) if individual tracking is paused.

### 9. Boundary Violations
- **`references_lifecycle` (Case -> BeneficiaryLifecycle):** The ontology places `BeneficiaryLifecycle` in the "Shared Human Model." However, `BeneficiaryLifecycle` is its own distinct domain (as seen in the repo structure and `ARCHITECTURE.md`). This external reference definition is pointing to the wrong domain owner.
- **Needs Assessment Overreach:** If `CasePlan` duplicates any diagnosis rather than strictly linking to `AssessmentFinding`, it is a violation. The current `references_assessment` points to the `Assessment` container rather than the specific `IdentifiedNeed` or `AssessmentFinding`.

### 10. ADR-023 Violations Summary
The current YAMLs were clearly written *before* ADR-023 was ratified.
- **Violation:** Promoting `Referral`, `FollowUp`, `CaseNote`, and `CaseOutcome` to Entities (violates §17 Value Objects).
- **Violation:** Modeling operational responsibility as a `CaseAssignment` entity instead of a Role on the Actor (violates §18 Roles).
- **Correction:** The next phase must wipe these 5 Entities from `ontology.yaml` and rewrite them as composite Value Object schemas inside a `data-properties.yaml`, and define the `LeadCoordinator` / `StatutoryOwner` in `relationships.yaml`.
