---
id: ARCHITECTURAL_RESET
title: Architectural Reset - Strategy & Alignment
status: Approved
owner: Governance
created: 2026-07-27
---

# Architectural Reset

## Purpose
This document records why the project methodology changed from a bottom-up engineering approach to a top-down, discovery-led ontological design approach. It serves as the canonical explanation of the repository strategy and clearly establishes the ultimate objective of the project.

## The Ultimate Objective
The ultimate objective of this repository is the successful design of the **Khidmat Humanitarian Ontology**.

The repository is NOT "doing Business Discovery" as an end in itself. Business Discovery, the Business Master Plan, the HBRM, Business Architecture, and Domain Discovery are preparation phases. Every completed discovery topic is an input into Ontology Design. Every methodology document exists to improve Ontology Design quality. Every governance activity exists to protect Ontology Design quality. The ontology is the destination; everything else is preparation.

## Original Direction
The initial direction of the project followed an engineering-first path:
`Ontology Engineering → Schema Design → Bottom-up modelling`

## Problems Identified
This approach led to premature commitments to data structures, schema classifications, and taxonomy hierarchies before the underlying humanitarian business reality was fully understood. It attempted to build software and taxonomies based on assumptions rather than validated humanitarian evidence.

## Corrected Direction
The project direction was corrected after architectural review to follow a rigorous, sequenced dependency chain:

```
Humanitarian Reality
↓
Business Discovery
↓
Business Master Plan
↓
Humanitarian Business Reference Model
↓
Business Architecture
↓
Domain Discovery
↓
Ontology Design
↓
Ontology Engineering
↓
Taxonomy Engineering
↓
Systems Engineering
```

## Architectural Principles & Rationale

- **Why discovery precedes ontology:** Ontology design must be grounded in validated humanitarian business reality, not assumptions. We cannot model a reality we have not first rigorously discovered.
- **Why ontology design precedes ontology engineering:** The conceptual and semantic framework (design) must be finalized, approved, and verified against reality before encoding it into machine-readable formats (engineering).
- **Why cognition must exist before architecture:** Architecture supports the cognitive goals of the system (understanding, reasoning, and responsible action). If the cognitive models are not defined, the architecture will be misaligned with the humanitarian purpose.
- **Why evidence precedes modelling:** All findings and models must trace back to Tiered evidence (Tier A/B/C/D) rather than conjecture or standard technical defaults.
- **Why governance precedes implementation:** Strict phase gates and human owner reviews prevent the downstream proliferation of errors, ensuring that the ontology remains aligned with its mandate and does not devolve into ad-hoc schema design.

## Phased Delivery and Lead Review
The immediate deliverable for the project lead is a complete Ontology Design for ONLY the following two sections:
1. **Domain Primitives**
2. **Ontology Layers** (including Facets, Entities, Relationships, Constraints, States, Events, Cognition, Coordination Patterns).

The repository will **STOP** after these two sections are designed. No further ontology work will continue until explicit approval is received. This acts as a critical architectural gate.

After approval, the project will continue with:
- Pillars
- Architecture Rules
- Ground Truth Reviews
- Evidence Framework
- Governance Framework
