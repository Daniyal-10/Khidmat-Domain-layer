# ADR-022

## Title
Canonical Concepts and Regional Localization Strategy

## Status
Accepted

## Context
The Knowledge Layer is intended to become a long-term humanitarian knowledge graph. The ontology must remain globally reusable while supporting deployments in different countries (India first, later Pakistan, Bangladesh, Middle East, Africa, etc.). Recent architectural review identified that many canonical concepts are internationally valid, but the terminology exposed to users differs significantly between countries. The ontology must not become country-specific.

## Problem Statement
Country-specific terminology (e.g., ASHA in India, Lady Health Worker in Pakistan, Gram Panchayat in India) creates pressure to introduce redundant concepts into the core ontology. If developers create `indian_asha_worker` and `pakistani_lady_health_worker`, the ontology will fracture. This would violate the single ownership principle established in ADR-008 and destroy the global applicability of the Shared Human Model and cross-domain reasoning, thereby breaking Knowledge Graph, RDF/OWL compatibility, and Explainable AI (XAI) capabilities. 

## Decision
Establish the principle that every semantic concept in the Knowledge Layer shall have exactly one canonical concept, exactly one canonical identifier, and exactly one semantic definition.

Localization shall never create new ontology concepts.

Localization shall instead provide:
- regional aliases
- localized labels
- multilingual labels
- deployment-specific terminology

The semantic meaning remains identical. Regional aliases are presentation mappings and are NOT semantic concepts.

Canonical concepts are stable. Localization is presentation. Reasoning MUST always use canonical concepts. APIs MUST always expose canonical identifiers. User interfaces and LLMs MAY display or translate canonical concepts into regional terminology for natural conversation. Ontology remains language-independent.

The following practices are explicitly prohibited:
- ❌ Country-specific ontology concepts (e.g., `indian_asha_worker`, `pakistani_lady_health_worker`, `country_phc`)
- ❌ Country-specific taxonomy ownership
- ❌ Country-specific ontology relationships
- ❌ Country-specific reasoning rules
- ❌ Duplicate semantic definitions
- ❌ Localized concepts becoming canonical concepts

## Alternatives Considered
- **Country-specific Ontologies (e.g., India-specific ontology):** Rejected. This would create duplicate concepts and destroy the global reusability of the semantic layer, violating long-term sustainability.
- **Overloading Canonical Concepts:** Rejected. Changing canonical identifiers to match a specific country's terminology (e.g., changing `community_health_worker` to `asha_worker`) would alienate other deployments and violate language independence.

## Consequences
- The Shared Human Model and all domain ontologies remain globally applicable, preserving consistency with ADR-008 (Single Ownership of Concepts).
- The DAG structure of the knowledge graph remains intact, ensuring RDF/OWL compatibility and seamless Explainable AI (XAI) inference.
- Long-term sustainability is guaranteed as new countries only require a presentation-level mapping, not a structural ontology rewrite.

## Governance Impact
- Any attempt to introduce country-specific or region-specific nodes into the canonical ontology must be rejected during architectural review. 
- Concept definitions must remain culturally and geographically neutral.

## Repository Impact
No changes to existing ontology structure, taxonomy, reasoning, or governance documents are required. The canonical concepts already present in the repository remain the single source of truth.

## Examples

**Canonical Concept:** `community_health_worker`
**Regional Aliases:**
- India: ASHA
- Pakistan: Lady Health Worker
- Bangladesh: Community Health Worker

**Canonical Concept:** `early_childhood_care_center`
**Regional Aliases:**
- India: Anganwadi

**Canonical Concept:** `primary_health_center`
**Regional Aliases:**
- India: PHC

**Canonical Concept:** `village_council`
**Regional Aliases:**
- India: Gram Panchayat

## Future Work
Recommend introducing a dedicated Localization Layer (or Regional Vocabulary Layer). This layer will contain:
- aliases
- multilingual labels
- country packs
- deployment vocabulary
- UI labels

This layer will serve as the presentation mapping for UIs and LLMs, operating completely independently without modifying the core ontology, taxonomy, reasoning, or governance documents.
