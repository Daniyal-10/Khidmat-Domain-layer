# Needs Assessment Business Flow Validation Report

## Scenario 1: Rapid Emergency Disaster Response
**Context:** A flood wipes out an entire village.
1. **Event:** A State Disaster Assessment Team conducts a Rapid Community Assessment (Observation-only).
2. **Finding:** Asserts critical WASH and Shelter needs for the entire geographic node.
3. **Downstream:** Support Delivery dispatches general water and tent provisions based on Community Need, bypassing individual household checks due to extreme urgency.

## Scenario 2: Chronic Welfare & Proxy Assessment
**Context:** A rural family applying for a government housing scheme (PMAY equivalent).
1. **Event:** An enumerator visits the household. The Head of Household provides proxy answers for the entire family.
2. **Finding:** The enumerator observes a mud roof (Verified Observation) but records the household income based purely on the Head's statement (Self-Reported).
3. **Data Quality:** The system flags the income as "Low Confidence - Self Reported" but the shelter condition as "High Confidence - Observed".
4. **Downstream:** Programs requires a triggered verification operation to audit the self-reported income before enrolling them in the scheme.

## Scenario 3: Highly Sensitive Protection Case (GBV / Child Protection)
**Context:** A social worker interviews a vulnerable youth in a refugee camp.
1. **Event:** Comprehensive Protection Assessment.
2. **Handling Refusals:** The youth refuses to answer specific questions about trauma. The system records "Refusal to Answer" rather than leaving it blank (which implies an omission by the enumerator).
3. **Finding:** The social worker infers a severe protection need based on observation and secondary indicators. The Need Assertion is marked as "Observed" and "Highly Sensitive."
4. **Downstream:** Case Management consumes the Need Assertion, restricting access to the finding based on RBAC, ensuring only specialized caseworkers can view it.

## Scenario 4: Dynamic Reassessment & Condition Change
**Context:** A beneficiary is enrolled in a livelihood program based on a baseline assessment showing mild vulnerability.
1. **Trigger:** The beneficiary suffers a severe workplace injury.
2. **Event:** A medical assessor conducts a Triggered Reassessment.
3. **Finding:** Asserts an Acute Health Need and a Chronic Disability (newly identified).
4. **Downstream:** The system updates the vulnerability score. Programs uses this to either escalate waitlist priority or transition the beneficiary from a Livelihood program to a Disability Pension program.
