# Impact Business Architecture

## 1. What is Impact?
The Impact domain exists to measure, evaluate, and understand the real-world changes in human wellbeing resulting from humanitarian interventions. While other domains track inputs, vulnerabilities, and outputs, the Impact domain shifts the system's focus from "What did we do?" to "Did it actually help?" by capturing long-term outcomes, subjective wellbeing, and systemic changes.

## 2. What Impact Owns
Impact exclusively owns measurement and evaluation.
- Outcome indicators and their definitions
- Baseline and endline measurement records
- Longitudinal tracking and evaluation schedules
- Measurement confidence and evaluation metadata
- Records of intervention success, failure, relapse, and unintended consequences

## 3. What Impact Never Owns
Impact strictly observes the boundaries of other domains:
- **Interventions:** It does not own the intervention itself.
- **Delivery:** It does not own the logistics or proof of delivery (Support Delivery).
- **Assessments:** It does not own the initial vulnerability or risk scoring (Needs Assessment).
- **Eligibility:** It does not own program rules or criteria (Programs).
- **Case Management:** It does not orchestrate or close the case.

## 4. Core Business Concepts
- **Impact Evaluation:** A structured assessment of the overall change in a beneficiary's or community's situation.
- **Outcome Indicator:** A standardized metric used to measure change.
- **Spillover & Exclusion Effects:** The measured impact (positive or negative) of an intervention on non-beneficiaries or the broader system.

## 5. Outcome Types
- **Individual:** Changes in personal wellbeing (e.g., child malnutrition reversed).
- **Household:** Changes affecting the living unit (e.g., household income stabilized).
- **Community:** Systemic changes across a localized group (e.g., increased access to clean water).
- **Programme:** Aggregate success or failure of a specific humanitarian initiative.
- **System:** Broad changes to social cohesion, institutional resilience, or local economic markets.

## 6. Measurement Concepts
- **Baseline:** The recorded state of an indicator before intervention.
- **Endline:** The recorded state of an indicator upon completion of the intervention.
- **Longitudinal:** Follow-up surveys conducted over time after case closure.
- **Counterfactual:** The theoretical trajectory of what would have happened without the intervention.
- **Persistence Horizon:** Categorization of outcomes as temporary, sustained, or irreversible.
- **Outcome Decay:** The gradual loss of a positive outcome over time.
- **Relapse:** A complete reversion to the baseline state or worse after an initial improvement.
- **Measurement Schedule:** A defined timeline determining when follow-up surveys occur based on the intervention's theory of change.

## 7. Indicator Concepts
- **Objective:** Observable, factual metrics (e.g., "School attendance rate").
- **Subjective:** Self-reported perceptions of wellbeing (e.g., "I feel safer").
- **Proxy:** Indirect indicators used when direct measurement is impossible or intrusive.
- **Composite:** An aggregated score derived from multiple underlying indicators.
- **Hierarchical indicators:** Governance ensuring local metrics map correctly to standardized program and global outcomes.

## 8. Attribution Concepts
- **Contribution:** Acknowledging that Khidmat played a part in the outcome without claiming sole causation.
- **Confounding Factors:** External variables that independently alter the outcome trajectory.
- **Multiple Intervening Actors:** Recognizing the compounded reality of government, NGO, and community interventions acting simultaneously.
- **External Shocks:** Systemic events (e.g., natural disasters, economic crises) that mask or erase the intervention's impact.

## 9. Evaluation Concepts
- **Independent Evaluation:** Ensuring that those who measure the impact are ideally independent from those who delivered the intervention to avoid reporting bias.
- **Survivor Bias:** The risk of artificially inflating impact scores by only measuring those who remain engaged.
- **Attrition:** Beneficiaries lost to follow-up during longitudinal measurement.
- **Measurement Confidence:** Epistemic weight applied to an evaluation based on the source and validity of the data.
- **Measurement Termination:** Formal ending of longitudinal tracking before completion (e.g., due to funding loss), without failing the intervention itself.

## 10. Humanitarian Principles
- **Epistemic Humility:** Acknowledging that impact measurements are often subjective claims, requiring strict separation between self-reported feelings and observable facts.
- **Do No Harm:** Vigilance in capturing iatrogenic harm (interventions causing new vulnerabilities) and managing survey fatigue.
- **Beneficiary Voice:** Ensuring the beneficiary has a mechanism to disagree with or dispute the recorded impact rating.

## 11. Cross-Domain Dependencies
- **Case Management:** Case closure or milestone completion triggers the start of impact measurement.
- **Needs Assessment:** Provides the initial vulnerability data serving as the baseline.
- **Support Delivery:** Confirms the output has been delivered so the outcome measurement window can begin.
- **Programs:** Consumes aggregated impact data for program evaluation and redesign.
- **Community Context:** Provides data on external shocks and absorbs rolled-up individual impacts into community resilience scores.

## 12. Operational Patterns
- **The Pre-Post Pattern:** Baseline measurement at enrollment, followed by endline measurement at closure.
- **The Longitudinal Pattern:** Periodic follow-ups triggered automatically after delivery is completed.
- **The Cohort Evaluation Pattern:** Aggregating individual impact scores across a specific demographic.
- **The Exception Pattern:** Immediate escalation when an impact assessment reveals worsening conditions, triggering a new Needs Assessment.

## 13. Business Rules
- Impact evaluations must explicitly state whether the evidence is subjective or objective.
- Negative impacts or unintended consequences must immediately generate new Risk signals.
- A case cannot definitively claim "irreversible impact" until the persistence horizon has been observed longitudinally.
- Proxy measurements must explicitly denote the proxy bias.

## 14. Known Edge Cases
- **Ghost Beneficiaries:** Beneficiary cannot be located for endline measurement.
- **Conflicting Reports:** A volunteer observes improvement, but the beneficiary reports feeling worse.
- **Intervention Interruption:** A case is suspended halfway through delivery, complicating partial impact measurement.
- **Catastrophic External Events:** A successful intervention is wiped out by a subsequent flood before endline measurement.
- **Survey Fatigue:** Beneficiaries refusing follow-up due to over-surveying.

## 15. Scope
Impact covers the measurement, recording, and evaluation of changes in wellbeing resulting from interventions, spanning individual, household, and community levels, and managing the epistemic validity of these measurements over time.

## 16. Out of Scope
- Defining what the interventions actually are.
- Handling the physical logistics of aid delivery.
- Creating the initial needs assessment or case plan.
- Arbitrating program eligibility criteria.

## 17. Delivered in V1
- Structural differentiation between Output (Support Delivery) and Outcome (Impact).
- Core measurement concepts (Baseline, Endline, Longitudinal).
- Epistemic tracking (Subjective vs Objective).
- Recognition of Relapse, Decay, and Persistence Horizons.
- Attribution and Confounding Factor frameworks.

## 18. Future V2
- Advanced causal attribution algorithms.
- Automated surveying tools for longitudinal data collection.
- Deep integration with global canonical indicator frameworks (e.g., UN SDGs).
- Community-level spillover tracking at scale.

## 19. Open Architectural Decisions
1. **Attribution vs Contribution:** Should Impact attempt causal attribution or only record observed contribution?
2. **Lost-to-Follow-Up / Attrition:** How should beneficiaries lost during longitudinal measurement affect outcome calculations?
3. **Spillover Measurement Scope:** Should Impact measure only enrolled beneficiaries or broader community/system effects?
4. **Subjective vs Objective Evidence:** How should conflicting beneficiary-reported and objectively observed outcomes be represented?
