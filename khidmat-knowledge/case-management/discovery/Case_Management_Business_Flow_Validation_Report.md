# Case Management Business Flow Validation Report

## 1. Multi-Agency Coordination & Duplicate Referrals
*Condition:* One household is engaged by 5 NGOs, Government, Hospital, Police, Legal Aid, and a Protection Team.
*Validation:* A "Free-for-all" creates chaos. The architecture enforces a `Lead Coordinator` role (a Role on an Actor) on the Household Case. All other actors hold `Participating Agency` roles. The Lead Coordinator approves the master Case Plan. Duplicate referrals are flagged by the system checking the shared `Household` entity's active plans.

## 2. Emergency Case Management (Disaster Scenarios)
*Condition:* Mass flooding displaces 10,000 people. Individual case planning is impossible.
*Validation:* Individual Case Management is suspended. The response shifts to the `Community Context` and `Support Delivery` (Mass Distribution). Case Management re-engages only during the recovery phase (e.g., targeted livelihood rebuilding) when individualized tracking becomes viable and necessary again. It is an architectural error to open 10,000 identical "Flood Cases"; mass needs belong outside Case Management.

## 3. Statutory Authority Revocation
*Condition:* An NGO is managing a child protection case. The Child Welfare Committee (CWC) discovers negligence and revokes the NGO's mandate.
*Validation:* The CWC (Statutory Owner) revokes Operational Authority. The NGO's `CaseWorker` role is terminated. The Case transitions to `Suspended` or is immediately reassigned. The Case Timeline immutable logs the revocation event.

## 4. The Funding-Starved Case
*Condition:* A Case Plan includes a $500 surgery and 6 months of rehab. The surgery is completed, but the NGO's rehab grant expires.
*Validation:* The Case cannot graduate. The specific Objective is marked `Suspended_Due_To_Funding`. The Case Management domain relies on a signal from the Programs domain (Funding Exhausted). The Lead Coordinator must now initiate a Referral to a State scheme to cover the rehab, transitioning the Case from internally-funded to externally-referred.

## 5. Long-term Reactivation
*Condition:* A refugee family was successfully graduated 5 years ago. A new conflict displaces them again.
*Validation:* The old case remains `Graduated` (historical immutable record). A new Case is opened, linked to the same persistent `Household` entity in the Shared domain, allowing the new Case Worker to query the historical Timeline for past interventions and vulnerabilities.
