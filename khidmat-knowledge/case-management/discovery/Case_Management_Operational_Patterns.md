# Case Management Operational Patterns

These patterns represent the standardized methods for executing complex humanitarian coordination within the Case Management architecture.

## 1. The Statutory Handoff Pattern
- **Trigger:** A beneficiary requires long-term institutional care (e.g., State orphanage).
- **Execution:** The current NGO (Operational Owner) prepares a Case Summary. A `CaseConference` (Value Object) is logged. A `Decision` (Runtime Object) is generated to transfer the case. The `StatutoryOwner` role is formally transferred to the State. The NGO's `LeadCoordinator` role is revoked. The Case Status changes to `Transferred`.

## 2. The Conference-Driven Pivot Pattern
- **Trigger:** A Case Plan is failing (e.g., a child keeps dropping out of referred schools).
- **Execution:** A `CaseConference` is convened involving the parent, the school, and the social worker. The conference produces a `ReviewDecision` (Runtime Object). The existing `Objective` is marked "Failed", and a new `Objective` (e.g., Vocational Training) is added to the `CasePlan`.

## 3. The Funding-Suspension Pattern
- **Trigger:** The Programs Domain signals that the grant funding a specific surgical intervention is exhausted.
- **Execution:** The Case Management engine receives this constraint. The intervention's status changes to `Suspended_Due_To_Funding`. The system generates a `Recommendation` (Runtime Object) to initiate a `Referral` (Value Object) to an alternative CSR program.

## 4. The Unified Household Coordination Pattern
- **Trigger:** Five different agencies want to help one vulnerable household.
- **Execution:** The system enforces the assignment of a single `LeadCoordinator` (Role). The other four agencies are assigned `ParticipatingAgency` (Role). All interventions are logged into a single unified `CasePlan` (Entity) attached to the Shared `Household` (Entity), ensuring no duplicate rations or conflicting medical advice.
