# Needs Assessment Domain Audit

## 1. Domain Definition
The Needs Assessment domain is the authoritative system for evaluating, recording, and quantifying the vulnerabilities, capacities, and acute/chronic deficits of individuals, households, or communities. It acts as the critical bridge between identity (Registration) and action (Programs / Support Delivery).

## 2. Core Mandate (What it Owns)
- **Vulnerability Profiling:** Identifying the specific risks and deficits (e.g., food insecurity, medical emergency, lack of shelter).
- **Assessment Events:** The actual occurrence of an evaluation (rapid, comprehensive, remote, observed).
- **Need Assertions:** The discrete outputs of an assessment stating that a subject requires a specific intervention or sector-level support.
- **Evidence & Veracity:** Tracking how a need was identified (self-reported, verified by a medical professional, proxy-reported by a community leader).
- **Scoring & Severity:** Standardized metrics (like vulnerability indices) that allow Programs to rank and prioritize beneficiaries.
- **Assessment Lifecycle:** The flow from an initial baseline assessment to triggered or scheduled reassessments.

## 3. Exclusion Mandate (What it Must NEVER Own)
- **Identity & Demographics:** Registration owns the foundational person/household records. Needs Assessment *references* them.
- **Program Eligibility Rules:** Programs owns the criteria. Needs Assessment provides the data (the "Need") that Programs evaluates against.
- **Case Plans:** Case Management owns the long-term strategic plan to resolve the need.
- **Aid Delivery:** Support Delivery owns the actual logistics and handover of relief items or services.
- **Registration of Target Groups:** Whether a person is a "Refugee" or "Citizen" is Registration. Needs Assessment evaluates if that Refugee is "Starving."

## 4. Key Cross-Domain Interactions (ADR-008 Compliance)
- **Registration:** Needs Assessment assesses subjects defined in Registration (`shared_human:person`, `shared_human:household`).
- **Programs:** Programs consumes Need Assertions and Vulnerability Scores to drive waitlist prioritization and eligibility logic.
- **Case Management:** Assessments trigger Case Management interventions; Case Managers routinely conduct reassessments.
- **Support Delivery:** SD fulfills the needs identified; SD might trigger a reassessment if delivery fails or if conditions on the ground are visibly different.

## 5. Humanitarian Standards Alignment
This domain aligns closely with:
- **Sphere Standards:** Minimum standards in WASH, Food Security, Shelter, and Health.
- **UNHCR & WFP Targeting:** Proxy Means Testing (PMT) and vulnerability targeting.
- **Protection Frameworks:** GBV, Child Protection, and Disability inclusion assessments, requiring high sensitivity and privacy logic.
