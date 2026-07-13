# Programs: Edge Cases

These scenarios test the robustness of the Programs model against severe humanitarian friction:

## 1. Mid-Cycle Regulatory Amendment
A government changes the income threshold for a welfare scheme halfway through the fiscal year. 
**Resolution:** The Program creates a new `Amendment/Version`. Enrolled beneficiaries are evaluated. The domain must support "Grandfathering" (allowing current cohorts to finish under the old criteria) versus "Immediate Termination."

## 2. Program Suspension (Conflict / Funding Cuts)
An INGO loses access to a conflict zone, or funding collapses overnight.
**Resolution:** The entire Program enters a `Suspended` state. This cascades down to freeze all Case Plans and Support Deliveries linked to it. When funding returns, it enters a `Reopened` state.

## 3. The Mutually Exclusive Double-Dip
A beneficiary applies for a CSR-funded housing grant but is already enrolled in a government housing subsidy. The CSR donor strictly prohibits co-funding.
**Resolution:** Programs define `Mutually_Exclusive` relationships. Case Management detects the conflict during enrollment proposal and forces a choice.

## 4. Humanitarian Override (The Exception)
A severely malnourished infant does not meet the strict geographic residency criteria of a nutrition program because they are internally displaced.
**Resolution:** A Program Manager exercises a `Humanitarian_Override`, forcing enrollment. The enrollment record retains an explicit audit trail linking to the overriding authority, rather than corrupting the demographic profile to pass the rules.

## 5. Successor Continuity (Program Splitting)
"Emergency Relief 2025" ends, but the crisis persists. It is replaced by "Recovery Support 2026".
**Resolution:** Programs uses a `Successor_Relationship` to map the old program to the new one, allowing Case Management to execute bulk cohort transitions without re-registering every beneficiary.

## 6. Waitlist Starvation
A program has 500 slots and 2000 eligible applicants.
**Resolution:** The Program utilizes an `Enrollment_Prioritization` rule (e.g., sorting by composite vulnerability score from the Risk domain) rather than simple first-come-first-served.
