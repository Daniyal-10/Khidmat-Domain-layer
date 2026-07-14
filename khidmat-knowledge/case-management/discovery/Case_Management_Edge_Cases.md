# Case Management Edge Cases

The business architecture handles complex realities through strict separation of concerns and robust lifecycle states.

## 1. The Multi-Decade Refugee Case
- **Situation:** A refugee family is supported for 20 years. Children are born, elders die.
- **Handling:** The `Household` entity (Shared Domain) handles the demographic changes. The `Case` remains Open. Objectives within the `CasePlan` are achieved and replaced. The `Timeline` stores the 20-year history as immutable Value Objects.

## 2. Statutory Custody Disputes
- **Situation:** A Court appoints a guardian, but the biological parents dispute it and refuse NGO intervention.
- **Handling:** The `StatutoryOwner` Role is assigned to the Court. The `Case` is moved to `Suspended` (Reason: Beneficiary Refusal / Legal Dispute) while the legal system resolves the issue. The architecture does not attempt to solve the legal dispute; it accurately records the operational paralysis.

## 3. The "Orphaned" Case (Implementing Partner Collapses)
- **Situation:** An NGO managing 500 cases goes bankrupt and ceases operations overnight.
- **Handling:** The `DelegatedAuthority` is revoked for all 500 cases. The `LeadCoordinator` role becomes vacant. The system flags all 500 cases with a Runtime Object (`Escalation: Unassigned Case`), notifying the `StatutoryOwner` (e.g., the State Government) to reassign them.

## 4. Sub-Household Abuse (Domestic Violence)
- **Situation:** A father is abusing the mother in a household currently receiving livelihood support.
- **Handling:** A new, highly secure Protection Case is opened for the mother (Individual). The existing Livelihood Case (Household) may be suspended or transferred. The architecture's separation of Individual Cases and Household Cases prevents exposing the mother's protection plan to the broader household interventions.
