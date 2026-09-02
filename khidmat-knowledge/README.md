# Khidmat Humanitarian Domain Model

Welcome to the Khidmat Humanitarian Domain repository. This project contains the definitive conceptual and semantic foundation for Khidmat AI. It is designed to model humanitarian reality—separating what actually exists in the field from how software systems track it.

## 1. Why the Domain Layer Exists

Historically, humanitarian systems are built to record transactions: *What did this person ask for? What did we give them?*

Khidmat is designed to understand reality, answering deeper questions: *Why is this need occurring? What happens if it remains unmet? How does one household member's vulnerability cascade to others?*

To answer these questions, Khidmat requires a **Domain Layer**. A malnourished child is malnourished whether or not a database records it; a household's vulnerability exists independently of an agency's verification process. This repository provides a rigorous, evidence-based description of that domain reality, ensuring that the software architecture is built on true humanitarian semantics rather than administrative convenience.

## 2. What the Ontology Provides

The ontology defines **what exists and what it means**. It provides:
- **A shared semantic vocabulary**: Defining the exact categories, entities, relationships, and constraints of humanitarian action.
- **A foundation for reasoning**: Formalizing concepts like open-world uncertainty (knowing that we don't know), dependency cascades, and temporal states.
- **An architectural baseline**: Establishing the core domain rules that future databases, APIs, and AI workflows must respect.

**What the ontology does NOT provide:**
It does not define software architecture. Database schemas, API contracts, temporal event-sourcing implementations, and concrete workflow execution mechanics are entirely outside the scope of this domain model.

## 3. Ontology Structure and Components

The governed ontology has three principal structural components, systematically derived from project evidence:

- **7 Domain Primitives**: The irreducible categories of concepts—the *kinds of things* that can exist.
  - *Condition, Context, Epistemic Stance, Entity, Norm, Occurrence, Relation.*
- **8 Ontology Layers**: The structural dimensions derived from the primitives.
  - *Facets, Entities, Relationships, Constraints, States, Events, Cognition, Coordination Patterns.*
- **7 Ontology Pillars**: Vertical, domain-specific capability areas mapped across the structural layers to represent coherent realities.
  - *Human & Social Subject, Context & Environment, Vulnerability & Need, Epistemics & Knowledge, Actors & Ecosystem, Action & Coordination, Resources & Support.*

## 4. Development, Validation, and Governance

The domain model was developed through a strict, sequential process designed to ground the ontology in actual humanitarian practice:
1. **Foundation (Stages 1-4)**: Deriving Primitives, Layers, Pillars, and Architectural Rules from the authoritative Khidmat Reference Model.
2. **Ground Truth Validation (Stage 5)**: Testing the structural foundation against documented practitioner evidence.
3. **Evidence Integration (Stage 6)**: Refining the ontology based on field reality (e.g., corroborating the separation of a person's life trajectory from their programme engagement).
4. **Governance (Stage 7)**: Issuing formal rulings on structural conflicts identified during validation.

## 5. Current Governed Status

**The ontology is structurally stable, baselined, and architecture-ready.**
The foundational structural framework (primitives, layers, pillars) is established and governed against authoritative sources, while specific individual semantic classifications remain provisional.

However, the model carefully preserves the distinction between what is structurally known and what is operationally open or uncertain:
- **Structurally Resolved**: Major domain semantics are closed. For example, Risk and Need are formally classified as Conditions (G5). The primitive definition is locked as a category of concept (G3). `Organisation` and `Programme` are explicitly split into distinct Entities connected by a relationship (G1).
- **Provisional / Single-Source**: Certain coordination patterns and practitioner classifications (such as Outcome ownership and Case Orchestration) are structurally resolved but rest on single-source evidence (G4) and remain provisional pending broader corroboration.
- **Unresolved / Explicitly Absent**: Meaningful uncertainty is retained rather than hidden. The exact composition formula for Vulnerability remains an undefined "Source-Absent Parameter". The CCR-7 dual-clock temporal requirement remains an unresolved architectural guideline (G2), not a mandatory universal constraint. The precise entities and workflows of the "giving" side are structurally accommodated but remain unpopulated.

## 6. The Next Phase: Architecture

With the ontology structurally stable, baselined, and architecture-ready—while explicitly preserving provisional and bounded-unresolved matters—**the next phase is software and AI architecture**. The architecture phase will consume this domain model to design the technical implementations—schemas, state machines, interfaces, and API boundaries—required to operate the Khidmat system.

## 7. Repository Structure

This repository preserves the complete journey from raw evidence to final governed decisions:

- `docs/01-evidence/` → Upstream humanitarian evidence and domain source material.
- `docs/02-understanding/` → The merged business and functional understanding of Khidmat.
- `docs/03-discovery/` → Analysis of domain gaps, scope, and coverage.
- `docs/04-reference-model/` → The comprehensive Reference Model (the conceptual source of truth).
- `docs/05-ontology/` → The formal ontology definition, validation records, and governance decisions.
- `docs/06-review-package/` → Artifacts and materials prepared for domain and design reviews.
- `docs/07-closure-archive/` → Archived documentation and historical records of project closures.

## 8. Authoritative Ontology Documents

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
| `07-STAGE-7-GOVERNANCE-DECISIONS.md` | Records Stage 7 governance rulings, including resolved, provisional, and bounded-unresolved decisions. |

*(Note: The `GT-*` records within the ontology directory serve as individual practitioner Ground Truth review logs, preserving raw validation evidence, rather than acting as standalone authoritative definitions.)*
