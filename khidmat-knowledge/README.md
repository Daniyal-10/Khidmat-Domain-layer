# Khidmat Humanitarian Domain Model

Welcome to the Khidmat Humanitarian Domain repository. This project contains the definitive conceptual and semantic foundation for Khidmat AI—a system designed not merely to record humanitarian transactions, but to understand humanitarian reality.

## 1. The Khidmat Domain

Humanitarian systems historically store data but rarely understand it. Most software is built to register cases and track donations, focusing on the question: *What did the person ask for?*

Khidmat requires a deeper understanding to function as a true Humanitarian Operating System. It must be able to answer:
> What does this person need? Why do they need it? What will happen if the need is unmet? Who else is affected? What support pathway exists? What future risks are developing?

To answer these questions, Khidmat needs a **Domain Layer**—a rigorous, structured description of reality. A malnourished child is malnourished whether or not a system records it; a household's shelter condition exists independently of the verification process. The Khidmat Domain Model separates reality from software implementation, creating a shared intelligence foundation that models the people, vulnerabilities, interventions, and outcomes that constitute humanitarian work.

## 2. What the Ontology Provides

The ontology within this repository translates our humanitarian and business understanding into a formal, machine-readable structure. It provides:
- **A shared semantic vocabulary**: Defining exactly what things are, how they relate, and what rules govern them.
- **A foundation for reasoning**: Enabling AI systems and workflows to understand context, vulnerability composition, and impact, rather than just processing flat records.
- **An architectural blueprint**: Establishing the core concepts from which all future databases, APIs, state machines, and user interfaces must be derived.

The ontology represents the definitive domain-semantic baseline. It models reality fully, while deferring technical implementation limits and software sequencing to the architecture phase.

## 3. Ontology Design Lifecycle

The domain model was developed through a rigorous, evidence-based sequence. The process began by establishing a thorough understanding of the business and humanitarian context, which informed the structural design. The resulting foundation was then subjected to strict validation and governance to ensure accuracy and structural integrity.

```text
Humanitarian / Business Evidence
            ↓
Business Understanding
            ↓
Domain Discovery
            ↓
Reference Model
            ↓
Ontology Foundation
  ├── Domain Primitives
  ├── Layers
  ├── Pillars
  └── Architecture Rules
            ↓
Ground Truth Review
            ↓
Evidence Integration
            ↓
Governance
            ↓
Closure / Remediation
            ↓
FINAL ONTOLOGY BASELINE
            ↓
ARCHITECTURE
```

- **Stages 1–4 (Ontology Foundation)** establish the structural core of the ontology.
- **Stages 5–7** are not independent ontology layers; they constitute the validation, evidence integration, refinement, and governance process used to test and finalize that foundation.
- **Closure / Remediation** represents the final alignment, establishing the definitive baseline.

## 4. Current Ontology Structure

The final, governed Khidmat Humanitarian Domain ontology is structured around:

- **7 Domain Primitives**: The irreducible, foundational categories of concepts from which all other elements are derived.
- **8 Ontology Layers**: The structural dimensions defining how primitives combine to represent operational realities.
- **7 Ontology Pillars**: The vertical, domain-specific capability areas mapped across the structural layers.

The **8 Ontology Layers** define the model's precise semantics:
1. **Facets**: Granular attributes and characteristics.
2. **Entities**: Identifiable, distinct actors and objects.
3. **Relationships**: How entities associate and relate.
4. **Constraints**: Rules, boundaries, and limitations governing entities and relationships.
5. **States**: The condition or status of entities at a given time.
6. **Events**: Occurrences that trigger state changes.
7. **Cognition**: Analytical, intent-based, and decision-making representations.
8. **Coordination Patterns**: Multi-actor workflows and systemic orchestrations.

## 5. What the Ontology Defines (and Does Not Define)

**The ontology defines WHAT exists and WHAT it means.**
It definitively establishes the semantic rules of the domain. For example:
- **Organisation vs. Programme:** The ontology strictly defines these as distinct entities connected via the relationship `Organisation → operates → Programme` (as established by the Stage 7 G1 governance ruling).
- **Temporal constraints (CCR-7):** The semantic distinction of dual-clock requirements is recognized and retained as a governed, unresolved domain tension (G2).

**The ontology does NOT define HOW it is implemented.**
It does not specify software architecture. The following concerns are entirely outside the ontology's scope:
- Database schemas and persistence mechanisms.
- API contracts and service boundaries.
- Concrete workflow execution and event-handling implementations.
- Algorithm design and temporal database implementations (e.g., CCR-7 does not mandate a universal dual-clock database architecture).

*Note: If technical implementation discovers a genuinely new domain-semantic requirement, it must be routed back through ontology governance, rather than being invented silently within the software architecture.*

## 6. Project Status & Next Phase

**ONTOLOGY DESIGN IS COMPLETE.**
The ontology has passed all structural, validation, and governance checks. There are no remaining unbounded domain-semantic blockers requiring architecture to invent semantics. The current baseline is authoritative and ready for architecture.

### Two things that remain reversible only by explicit ruling

Two decisions in this repository are foundational but were made by the design process itself rather than independently ratified before use. Both have since been closed by explicit Stage 7 governance rulings and are recorded here so future readers can find them without searching:

1. **The definition of a Domain Primitive** (category of concept vs. concrete irreducible)
   — ratified by governance ruling **G3**. Open to reversal only via a new, explicit Lead or governance ruling — never by a downstream document silently assuming the other reading.

2. **The Organisation/Programme split**
   — ratified by governance ruling **G1**, amended at source in `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4. Open to reversal only via a new governance ruling that also re-amends the Tier 1 source.

See `docs/05-ontology/07-STAGE-7-GOVERNANCE-DECISIONS.md` for both rulings in full.

**THE NEXT PHASE IS ARCHITECTURE.**
The repository represents a baselined, architecture-ready domain model. The project now transitions to the software and AI architecture phase, which will consume this ontology to build the operational Khidmat system.

## 7. Repository Structure

This repository contains the complete documentation of the domain model, from raw evidence to the final governed ontology.

- `docs/01-evidence/` → Upstream humanitarian evidence and domain source material.
- `docs/02-understanding/` → The merged business and functional understanding of Khidmat.
- `docs/03-discovery/` → Analysis of domain gaps, scope, and coverage.
- `docs/04-reference-model/` → The comprehensive Khidmat Humanitarian Domain Reference Model (the conceptual source of truth).
- `docs/05-ontology/` → The formal ontology definition (primitives, layers, pillars, rules), along with validation and governance records.
- `docs/06-review-package/` → Artifacts and materials prepared for reviews.

## 8. Documentation Map

The core ontology is defined by the following primary files in `docs/05-ontology/`:

| Document | Purpose |
| :--- | :--- |
| `01-DOMAIN-PRIMITIVES.md` | Defines the 7 foundational domain primitives. |
| `02-ONTOLOGY-LAYERS.md` | Defines the 8 structural ontology layers derived from the primitives. |
| `03-ONTOLOGY-PILLARS.md` | Defines the 7 ontology pillars mapped across the layers. |
| `04-ARCHITECTURE-RULES.md` | Outlines the foundational architectural rules governing ontology composition. |
| `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md` | The framework used to conduct practitioner Ground Truth reviews. |
| `05-GROUND-TRUTH-REVIEW-MATRIX.md` | The summary matrix of Ground Truth validation. |
| `06-STAGE-6-EVIDENCE-INTEGRATION-REPORT.md` | Preserves the analysis of integrating Ground Truth evidence. |
| `07-STAGE-7-GOVERNANCE-DECISIONS.md` | Records the final governance rulings (e.g., G1, G2) that resolved conflicts. |

*(Note: The `GT-*` records within the ontology directory serve as individual practitioner Ground Truth review logs, preserving raw validation evidence at a high level without acting as standalone authoritative definitions.)*
