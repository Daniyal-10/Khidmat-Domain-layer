# Case Management Concept Inventory

## 1. Core Entities (The Backbone)
- **Case:** The overarching coordination container for a beneficiary (Individual or Household).
- **Case Plan:** The structured roadmap of objectives and planned interventions.

## 2. Roles (Per ADR-023)
- **Statutory Owner:** The legal/governmental custodian of the case.
- **Operational Owner (Lead Coordinator):** The primary agency or individual responsible for executing the plan.
- **Participating Agency / Co-worker:** Additional actors contributing to the case.
- **Delegated Authority:** The formal permission granted to an operational owner.

## 3. Value Objects (Facts and Records, Per ADR-023)
- **Objective / Goal:** The desired outcome within a Case Plan.
- **Referral:** A formal request sent to another agency or internal department.
- **Follow-up:** A scheduled or completed check-in.
- **Case Note:** A qualitative observation.
- **Case Conference:** A multi-stakeholder review event.
- **Timeline Entry:** A chronological record of an event in the case.
- **Case Assignment:** The record of assigning a worker to the case.

## 4. Runtime / Reasoning Objects (Diagnostic/Decision Outputs, Per ADR-023)
- **Escalation:** A diagnostic flag raised (e.g., by a reasoning engine detecting a stalled critical referral).
- **Review Decision:** The outcome of a Case Conference (e.g., "Change objective", "Transfer case").
- **Recommendation:** System-generated suggestions for interventions.

## 5. Lifecycle and Taxonomy State
- **Case Status:** Open, Active, Paused, Suspended, Graduated, Administratively Closed, Reopened.
- **Priority Level:** Routine, Urgent, Emergency.
- **Closure Reason:** Goal Met, Lost Contact, Refused Service, Deceased, Transferred.
- **Suspension Reason:** Funding Exhausted, Statutory Hold, Beneficiary Unavailable.
