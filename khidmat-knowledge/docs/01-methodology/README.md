# 01-methodology

## Purpose
Methodology. Frameworks, standards of practice, and rules for engineering.

## Scope
- **In Scope**: Business Master Plan, Discovery frameworks, Ontology engineering rules.
- **Out of Scope**: Actual Domain logic, Actual Ontologies, Code.

## Upstream Dependencies
- 00-governance

## Downstream Consumers
- 02-architecture, 03-domains, 04-semantics

## Methodology Lifecycle (corrected — Repository Canonicalization Audit)

The lifecycle for every methodology in this directory has two distinct phases, not one undifferentiated Blueprint→Review→Resolution→Certification→Final chain. Conflating them is exactly what produced the Business Master Plan's invalid certification (a full governance trail issued for content that was never authored):

1. **Blueprint Lifecycle** (governs the *method*): Blueprint → Blueprint Review → Blueprint Resolution → Blueprint Certification. This certifies only that the methodology for authoring is sound and ready to use. File names must carry an explicit `_BLUEPRINT_` infix at every stage (e.g. `..._BLUEPRINT_REVIEW.md`, `..._BLUEPRINT_CERTIFICATION.md`) so the artifact under review is unambiguous.
2. **Authoring** (the step the prior lifecycle skipped): the Final Methodology document itself must actually be written, using the certified Blueprint, before any further review can occur. No review, resolution, or certification may reference chapter numbers or content of a Final document that does not yet exist.
3. **Methodology Lifecycle** (governs the *content*, only after Authoring): Final Methodology → Methodology Review → Methodology Resolution → Methodology Certification. File names for this phase carry no `_BLUEPRINT_` infix, precisely because they review different content than phase 1.

A certification issued for a document whose content does not exist is void (Constitution Article XVI).

## Contents (flat structure — every methodology document lives directly in this directory)
- `BUSINESS_DISCOVERY_BLUEPRINT.md` — draft, v0.1.0. Governs the evidence-gathering activity that precedes/feeds Business Master Plan authoring (elaborates BMP Blueprint §7/§9; does not amend Article XVI — see its §2 for the open governance question). Not the same document as `DOMAIN_DISCOVERY.md` below.
- `BUSINESS_MASTER_PLAN_BLUEPRINT.md` — active methodology; `BUSINESS_MASTER_PLAN.md` (its target) not yet authored.
- `HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT.md` + its Architecture Review, Resolution, and Freeze Certification — complete, internally consistent blueprint lifecycle; `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` (its target) not yet authored.
- `ONTOLOGY_DESIGN_BLUEPRINT.md` — draft, v0.1.0.
- `BUSINESS_ARCHITECTURE.md`, `DOMAIN_DISCOVERY.md` (post-Business-Architecture domain *sequencing* decision — distinct from Business Discovery above), `KNOWLEDGE_LAYER.md`, `ONTOLOGY_ENGINEERING.md`, `TAXONOMY_ENGINEERING.md`, `ONTOLOGY_DESIGN.md` — empty stubs, not yet authored.
