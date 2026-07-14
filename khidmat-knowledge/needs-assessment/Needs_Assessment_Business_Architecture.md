# Needs Assessment Business Architecture

## 1. Architectural Philosophy
Needs Assessment cannot be a generic "survey tool" or a flat list of questions. In humanitarian and welfare contexts, an assessment is an epistemological event: it establishes *what is known*, *how strongly it is believed*, *who claimed it*, and *how quickly it expires*. The architecture must separate the **Instrument** (the tool), the **Session** (the act of assessing), the **Evidence** (the raw data/observation), and the **Finding** (the asserted need).

## 2. Core Architectural Pillars

### A. Instruments and Sessions
- **Assessment Instrument:** The formalized tool, questionnaire, or indicator matrix (e.g., Sphere Standards Checklist, SECC Survey, WHO Disability Schedule).
- **Assessment Session:** The specific episodic event where an instrument is applied. Sessions can be *completed*, *interrupted*, *abandoned*, or *partially completed*.

### B. Epistemology of Evidence
Humanitarian data is rarely absolute truth. The architecture models:
- **Declared Needs:** Self-reported by the beneficiary (e.g., "We have no food").
- **Verified Needs:** Backed by documentation or biometric evidence.
- **Inferred Needs:** Deduced through professional judgment (e.g., a caseworker infers latent trauma based on behavioral observation).
- **Observation:** Direct sensory evidence by the assessor (e.g., "Roof is collapsed").
- **Confidence & Uncertainty:** Every finding carries an evidence confidence score. If observations contradict declarations (e.g., beneficiary says they are starving, but observation shows full grain silos), the system captures the conflict without erasing either data point.

### C. The Missing Data Reality
Missing data in humanitarian contexts is data in itself.
- **Refused Response:** Beneficiary explicitly declines.
- **Safety-Driven Omission:** Assessor intentionally skips a question because asking it is unsafe (e.g., political minders or abusers are present).
- **Unknown/Non-Response:** True absence of information.

### D. Time-Decay, Aging, and Expiry
Needs are highly temporal.
- **Validity Windows:** A cholera risk finding may expire in 7 days; a chronic disability finding may last 5 years.
- **Evidence Freshness:** As time passes, confidence in the finding decays.
- **Mass Invalidation:** A localized disaster (e.g., an earthquake) instantly invalidates all previous shelter and health assessments for that geographic area, resetting the baseline to zero.

### E. Consensus and Governance
Assessments frequently conflict (e.g., two NGOs assess the same household, or a junior social worker disagrees with a doctor).
- **Supervisor Review:** Quality assurance gates before findings are locked.
- **Peer Review & Calibration:** Aligning assessor scoring to prevent systematic bias (e.g., one assessor consistently marking "Critical" while another marks "Moderate").
- **Assessment Consensus:** The formal resolution of conflicting findings into a single authoritative Need Assertion for downstream Programs.

## 3. India Readiness Integration
This architecture naturally maps to Indian welfare mechanics:
- **Government Welfare Assessors:** ASHA workers or Anganwadi workers conducting continuous micro-sessions (observations) rather than massive one-off surveys.
- **Disaster Assessment Teams:** SDRF mass-invalidating previous structural baselines after a cyclone and deploying rapid instruments.
- **CSR Baseline Surveys:** Deploying structured instruments with supervisor review workflows for data quality.
