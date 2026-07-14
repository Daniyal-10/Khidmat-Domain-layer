# Needs Assessment Phase 0 Decision Review

## 1. Scope & Ownership
- **Decision:** Needs Assessment owns the epistemological tracking of a need (session, observation, finding, consensus, evidence quality).
- **Exclusion:** It does NOT own program eligibility, identity (Registration), or service fulfillment (Support Delivery).

## 2. Evidence Epistemology (ADR-00X)
- **Decision:** Needs are not absolute truths. The ontology must model `evidence_type` (Declared, Verified, Inferred, Observed) and `confidence_level`.
- **Reasoning:** In humanitarian scenarios, self-reported data often conflicts with observations. Both must be retained.

## 3. The "Missing Data" Concept
- **Decision:** Missing data is categorized actively via `missing_data_reason` (e.g., Safety Risk, Refusal).
- **Reasoning:** A blank field in a GBV assessment could indicate a lethal threat (Safety Risk) or an accidental skip. The distinction drives automated Case Management triggers.

## 4. Lifecycles & Time Decay
- **Decision:** Need Assertions have an explicitly modeled validity window (`validity_window_end`) and state (`provisional`, `authoritative`, `expired`, `invalidated`).
- **Reasoning:** Assessments age. Earthquakes mass-invalidate housing assessments. Needs are temporal.

## 5. Finding Consensus
- **Decision:** `finding_consensus` acts as the governance resolution mechanism for conflicting assertions across overlapping NGO triangulations.
- **Reasoning:** Avoids deleting or overwriting assessor field data while providing a unified view for downstream Programs.
