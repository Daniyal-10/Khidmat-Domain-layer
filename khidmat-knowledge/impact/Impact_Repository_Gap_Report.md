# Impact Repository Gap Report

## Current State Analysis
The existing Khidmat V1 Blueprint explicitly places "Impact Measurement" as a planned future capability. Currently, the repository models Needs, Risks, and Support Delivery (outputs), but lacks the vocabulary for Outcomes and Impact.

## Identified Gaps
1. **Lack of Outcome Ontology**: No entities or properties exist to define `OutcomeIndicator`, `Baseline`, `Endline`, or `ImpactEvaluation`.
2. **Taxonomy Deficiencies**: Missing standardized taxonomies for common humanitarian outcome metrics (e.g., Food Consumption Score, Coping Strategy Index).
3. **Lifecycle Disconnect**: The Beneficiary Lifecycle ends at `Outcome Measurement -> Impact Measurement`, but these stages have no underlying technical implementation or data structures.
4. **Epistemic Tracking for Outcomes**: Need a mechanism to distinguish between "Observed Outcome" and "Self-Reported Outcome".

## Remediation Strategy
- **Phase 2 (Ontology)**: Introduce core Impact entities.
- **Phase 3 (Taxonomy)**: Define standardized humanitarian indicators.
