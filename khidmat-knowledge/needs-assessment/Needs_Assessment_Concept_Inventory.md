# Needs Assessment Concept Inventory

## Core Entities
1. **Assessment Instrument:** The formalized questionnaire, matrix, or guideline used to conduct the evaluation.
2. **Assessment Session:** The episodic event of applying an instrument to a subject (timestamped, location-bound, status-tracked).
3. **Observation:** A raw, uninterpreted piece of evidence gathered during a session (can be declared, observed, or documented).
4. **Need Assertion (Finding):** The synthesized conclusion that a subject has a specific deficit, vulnerability, or capacity gap.
5. **Finding Consensus:** The governance record that resolves conflicting findings or elevates a finding to "authoritative" after supervisor review.

## Taxonomies Required
1. **Session Status:** Completed, Partially Completed, Interrupted, Abandoned, Scheduled.
2. **Evidence Types:** Declared (Self-Reported), Proxy-Reported, Document Verified, Assessor Observed, Inferred.
3. **Confidence Levels:** High, Medium, Low, Highly Uncertain, Disputed.
4. **Missing Data Reasons:** Beneficiary Refusal, Safety/Protection Risk, Question Skipped, Language Barrier, Abandoned Session.
5. **Finding Status:** Provisional, Supervisor Approved, Under Review, Disputed, Consensus Reached, Expired, Invalidated.
6. **Invalidation Reasons:** Time Decay/Expiry, Mass Disaster Event, Superseded by Reassessment, Fraud Detected.
7. **Thematic Sectors:** WASH, Shelter, Food Security, Livelihood, Health, Protection, Education.
8. **Need Urgency/Severity:** Critical, Severe, Moderate, Mild, None.

## Relationships & Cross-Domain Links
- Assessment Session `uses` Assessment Instrument
- Assessment Session `evaluates` (Person | Household | Geographic Area)
- Assessment Session `yields` Observation
- Observation `synthesizes_into` Need Assertion
- Need Assertion `resolved_by` Finding Consensus
- Need Assertion `invalidated_by` (Disaster Event / Expiry Rule)
