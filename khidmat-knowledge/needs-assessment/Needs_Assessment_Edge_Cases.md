# Needs Assessment Edge Cases

## 1. The Interrupted Session
Gunfire erupts, or the respondent simply walks away angrily. The Assessment Session ends abruptly.
- *Handling:* The Session is marked "Interrupted." The ontology must allow Partial Findings to be saved, with specific missing data flags indicating that the rest of the instrument was not applied, without penalizing the assessor for incomplete data.

## 2. Safety-Driven Omissions (The Silent Assessor)
A protection officer is interviewing a woman, but her husband (the abuser) refuses to leave the room. The officer skips the GBV section of the instrument to protect the woman's life.
- *Handling:* The system records "Safety/Protection Risk" as the missing data reason. This signals to Case Management that there is a latent protection concern, without exposing the woman to immediate harm by recording a direct finding.

## 3. Mass Disaster Invalidation
An earthquake destroys a district. All previous housing and shelter baseline assessments are instantly wrong.
- *Handling:* The system supports Mass Invalidation events, forcefully expiring all Need Assertions of specific sectors (e.g., Shelter, WASH) in a defined `geographic_area`, resetting the baseline.

## 4. The Liar's Dilemma & Assessor Calibration
A community leader colludes with households to hide assets during a Proxy Means Test to ensure they get enrolled in a cash program. The assessor records "Declared Need" but adds an "Observation" that contradicts it (e.g., "Respondent claims zero income, but brand new tractor parked outside").
- *Handling:* The Need Assertion is flagged with "Internal Conflict" and "Low Confidence." A Supervisor Review or a secondary Verification Operation is triggered before consensus is reached.

## 5. Overlapping NGO Triangulation
Three different NGOs assess the same household within a week. One says Moderate Need, two say Severe Need.
- *Handling:* The `Finding Consensus` entity allows a lead agency or coordination body to formally merge the conflicting Need Assertions into a single authoritative finding, tracing lineage back to the disparate sessions.
