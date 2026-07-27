# 01-methodology

## Purpose
Methodology. Frameworks, standards of practice, and rules for engineering.

## Scope
- **In Scope**: Business Master Plan, Discovery frameworks, Ontology engineering rules.
- **Out of Scope**: Actual Domain logic, Actual Ontologies, Code.

## Strategic Alignment
The ultimate objective of this project is the successful design of the **Khidmat Humanitarian Ontology**.
Every methodology document in this directory exists solely to improve Ontology Design quality. The Business Discovery process is preparation work, meant to ground the ontology in validated humanitarian business reality. The methodology enforces a strict sequence: 
`Business Discovery ↓ Business Master Plan ↓ HBRM ↓ Business Architecture ↓ Domain Discovery ↓ Ontology Design`. 
Ontology engineering and downstream schemas are strictly forbidden until the Ontology Design is complete and approved.

## Upstream Dependencies
- 00-governance

## Downstream Consumers
- (None for now, awaiting future pipeline stages)

## Methodology Lifecycle (corrected — Repository Canonicalization Audit)

The lifecycle for every methodology in this directory has two distinct phases, not one undifferentiated Blueprint→Review→Resolution→Certification→Final chain. Conflating them is exactly what produced the Business Master Plan's invalid certification (a full governance trail issued for content that was never authored):

1. **Blueprint Lifecycle** (governs the *method*): Blueprint → Blueprint Review → Blueprint Resolution → Blueprint Certification. This certifies only that the methodology for authoring is sound and ready to use. File names must carry an explicit `_BLUEPRINT_` infix at every stage (e.g. `..._BLUEPRINT_REVIEW.md`, `..._BLUEPRINT_CERTIFICATION.md`) so the artifact under review is unambiguous.
2. **Authoring** (the step the prior lifecycle skipped): the Final Methodology document itself must actually be written, using the certified Blueprint, before any further review can occur. No review, resolution, or certification may reference chapter numbers or content of a Final document that does not yet exist.
3. **Methodology Lifecycle** (governs the *content*, only after Authoring): Final Methodology → Methodology Review → Methodology Resolution → Methodology Certification. File names for this phase carry no `_BLUEPRINT_` infix, precisely because they review different content than phase 1.

A certification issued for a document whose content does not exist is void (Constitution Article XVI).

## Contents (flat structure — every methodology document lives directly in this directory)
- `BUSINESS_MASTER_PLAN_BLUEPRINT.md` — active blueprint needed for the current pipeline stage execution.
- `ONTOLOGY_DESIGN.md` — canonical methodology/framework document.
- `discovery/` — active directory containing the discovery dossiers required to author the Business Master Plan.
