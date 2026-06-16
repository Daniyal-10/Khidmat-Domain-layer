# AI_WORKFLOW.md — Khidmat Knowledge Layer AI Collaboration Workflow

**Authority:** Human Owner
**Status:** Accepted Governance Document
**Scope:** All AI activity on the Khidmat knowledge layer

---

# Purpose

The Khidmat Knowledge Layer is built collaboratively by multiple AI systems operating under human governance. Without explicit workflow rules, AI collaboration produces ontology drift: concepts are invented by the wrong domain, defined in multiple places, activated before their prerequisites are met, and governed by no single authoritative source.

This document defines how AI systems collaborate, who owns what decision, how changes are made, and how governance files are maintained.

This is a governance document. It is not an ontology document. It is not an implementation guide.

All AI activity on this repository must conform to this workflow.

---

# AI Roles

## Human Owner

The Human Owner holds final authority over all decisions on the Khidmat Knowledge Layer.

**Responsibilities:**
- Strategic direction of the knowledge layer
- Final approval of all ontology design and architectural decisions
- Domain activation approval
- Resolution of architectural disputes between AI systems

No domain activates, no concept is promoted to shared ownership, and no architectural decision is finalised without Human Owner approval.

---

## ChatGPT — Chief Knowledge Architect

ChatGPT operates as the primary ontology design intelligence. It reviews, proposes, and validates ontological structure but does not modify files directly.

**Responsibilities:**
- Ontology design: proposing concept structures, hierarchies, and relationships
- Taxonomy review: evaluating classification decisions and vocabulary choices
- Domain boundary review: ensuring concepts are owned by the correct domain
- Reasoning model review: evaluating inference rules, severity rules, and coherence rules
- Authority review: identifying ownership conflicts and recommending resolution
- Roadmap review: assessing whether proposed work is sequenced correctly

**Limitations:**
- Does not directly modify repository files
- All designs produced by ChatGPT must be reviewed by the Human Owner before implementation

---

## Claude Supervisor

Claude operates as the governance and compliance layer. It audits against existing governance files but does not generate ontology concepts.

**Responsibilities:**
- Governance review: verifying that proposed changes conform to ARCHITECTURE.md, DECISIONS.md, and ADRs
- Checklist maintenance: updating ontology_completion_checklist.md to reflect progress
- Roadmap compliance: ensuring domain activation follows knowledge_layer_roadmap.md dependencies
- Authority matrix compliance: ensuring concept ownership is correctly declared in ontology_authority_matrix.md
- Progress tracking: reporting current state against checklist and roadmap

**Limitations:**
- Does not create ontology concepts
- Does not approve designs — approval is the Human Owner's responsibility

---

## Antigravity Agent

Antigravity operates as the implementation layer. It writes files, generates YAML, and maintains documentation under instruction.

**Responsibilities:**
- File creation: producing new YAML, Markdown, and governance files
- File editing: applying approved changes to existing files
- YAML generation: translating approved ontology designs into structured files
- Repository maintenance: keeping file structure consistent with the roadmap
- Documentation updates: updating ARCHITECTURE.md, DECISIONS.md, GLOSSARY.md, and governance files as directed

**Limitations:**
- Does not create new ontology concepts without prior architectural review and Human Owner approval
- Implements only what has been reviewed and approved
- May flag inconsistencies but does not resolve them unilaterally

---

# Mandatory Workflow

Every change to the knowledge layer — whether a new concept, a new file, a structural change, or a governance update — must follow this sequence:

```
Idea
  ↓
Architecture Review
  (ChatGPT proposes; Claude audits against governance files)
  ↓
Implementation Plan
  (Antigravity proposes complete file content before writing)
  ↓
Human Approval
  (Human Owner reviews and approves or modifies the plan)
  ↓
Antigravity Implementation
  (Files are created or edited)
  ↓
Governance Audit
  (Claude verifies governance files are updated correctly)
  ↓
Commit
```

No file is written before Human Approval is given.
No governance file is left out of date after implementation.
No concept enters the repository without an identified owner.

---

# Governance File Responsibilities

## knowledge_layer_inventory.md

**Purpose:** Single source of truth for every file in the repository — what it owns, what it owes, its maturity, and its known gaps.

**Update when:** A new file is created, a file's ownership changes, a known gap is resolved, or a new gap is identified.

**Authority:** Knowledge Layer Architect.

---

## ontology_authority_matrix.md

**Purpose:** Declares the authoritative owner for every concept in the knowledge layer. Enforces single ownership per ADR-008.

**Update when:** A new concept is introduced, a concept's ownership changes, or a concept is promoted from a domain file to shared ownership.

**Authority:** Knowledge Layer Architect, with Human Owner final approval.

---

## ontology_completion_checklist.md

**Purpose:** Tracks progress across all taxonomy, ontology, reasoning, and governance files. The single source of truth for what is done, in progress, missing, and future.

**Update when:** A file is completed, a file moves to in-progress, or a missing item is identified or resolved.

**Authority:** Claude Supervisor maintains; Human Owner approves status changes.

---

## knowledge_layer_roadmap.md

**Purpose:** Defines the dependency order for all stages of knowledge layer development. Governs domain activation sequencing.

**Update when:** A stage completes, a dependency changes, or a new domain is added to the planned sequence.

**Authority:** Knowledge Layer Architect, with Human Owner final approval. This file is authoritative for activation order.

---

## ARCHITECTURE.md

**Purpose:** Domain inventory, dependency rules, maturity level definitions, governance file references, shared human model declaration, and future domain layer declarations.

**Update when:** A domain activates, a new domain is declared, a maturity level changes, or a new governance section is required.

**Authority:** Human Owner.

---

## DECISIONS.md

**Purpose:** Architectural Decision Log. Records every significant design decision — what was decided, why, and what alternatives were rejected. Entries are never removed; reversals are recorded as new entries.

**Update when:** A design decision is made or reversed.

**Authority:** Human Owner approves each ADR before it is recorded.

---

## GLOSSARY.md

**Purpose:** Ubiquitous language for the Khidmat knowledge layer, organised by ownership boundary. All contributors — human and AI — use these definitions.

**Update when:** A new concept enters the vocabulary, a concept is moved between sections due to ownership reclassification, or a definition requires correction.

**Authority:** Knowledge Layer Architect proposes; Human Owner approves.

---

# Governance Update Checklist

After any ontology, taxonomy, reasoning, or domain change, the following files must be reviewed before work is considered complete.

| Change Type | Files To Review |
|---|---|
| New concept introduced | ontology_authority_matrix.md, GLOSSARY.md |
| New file created | knowledge_layer_inventory.md, ontology_completion_checklist.md |
| File completed | ontology_completion_checklist.md |
| Domain activation | ARCHITECTURE.md, knowledge_layer_roadmap.md, ontology_completion_checklist.md |
| Architectural decision | DECISIONS.md |
| New vocabulary term | GLOSSARY.md |
| Ownership change | ontology_authority_matrix.md, knowledge_layer_inventory.md |

Review does not necessarily imply modification. However, every listed file must be checked before work is considered complete.

This checklist exists to prevent future AI systems from closing a task without completing the corresponding governance updates.

---

# Repository Authority Order

When governance files disagree, authority is resolved in the following order:

1. Human Owner decisions
2. DECISIONS.md (accepted ADRs)
3. ARCHITECTURE.md
4. knowledge_layer_roadmap.md
5. ontology_authority_matrix.md
6. knowledge_layer_inventory.md
7. ontology_completion_checklist.md
8. GLOSSARY.md

Lower-ranked files must be updated to align with higher-ranked files.

Conflicts must not be resolved by silent modification of a lower-ranked file if doing so contradicts a higher-ranked file. When a genuine conflict exists between two files at different authority levels, it should be surfaced and resolved through a new ADR rather than resolved silently.

This order becomes essential as the repository grows and multiple AI sessions operate across the same governance layer.

---

# Concept Ownership Rules

Governed by ADR-008: Single Ownership of Concepts.

**The rule:**

> Every concept in the knowledge layer must have exactly one authoritative owner. A concept may be referenced by many files but may only be defined by one.

**In practice:**

```
One concept → One owner → Many references
```

- The owner is the single file that defines the concept: its meaning, values, and constraints.
- All other files that use the concept reference the owner. They do not redefine it.
- If the same concept appears as a definition in two places, this is an ownership conflict and must be resolved before the concept can be used in reasoning.

**How ontology_authority_matrix.md is used:**

When a concept is introduced, its owner is declared in ontology_authority_matrix.md. This declaration is the governance record of ownership. If a concept is later promoted from a domain file to shared ownership, the matrix is updated to reflect the new owner. The matrix is audited by Claude Supervisor at each governance review.

No concept may be used in a reasoning rule if its ownership is undeclared or contested.

---

# Domain Activation Rules

Governed by ADR-009: Dependency-Driven Domain Activation, and knowledge_layer_roadmap.md.

**Rules:**

1. **Placeholder domains remain inactive.** A placeholder domain declares scope and concept ownership intentions but does not implement taxonomy, ontology, or reasoning rules until activation is approved.

2. **Prerequisites must be satisfied before activation.** No domain activates until the domains it depends on are substantially complete. Substantially complete means the concepts that the activating domain requires are stable — not that every edge case is resolved.

3. **knowledge_layer_roadmap.md is the authoritative activation sequence.** The roadmap stage order is not a suggestion. Activating a domain before its prerequisites introduces ontology drift: the domain will invent concepts it should not own.

4. **Activation requires Human Owner approval.** No domain transitions from placeholder to active without explicit approval.

5. **Premature activation is a governance failure.** Any AI system that proposes or implements domain concepts ahead of the roadmap sequence is operating outside its mandate.

---

# Current Priority

**Current focus: shared/human-model/**

The Shared Human Model is the active design and implementation priority. It is Stage 2 of the knowledge_layer_roadmap.md and is a prerequisite for every subsequent stage.

**Planned files:**

| File | Concepts |
|---|---|
| `lifecycle-stages.yaml` | Lifecycle stages from infant to elderly; reasoning-level developmental contexts |
| `capabilities.yaml` | Human capabilities as strengths and assets; not deficit-only |
| `dependency.yaml` | Dependency relationships: developmental, physical, financial, emotional, legal |
| `family-structure.yaml` | Family as a social unit; distinct from household; internal relationships |
| `health-conditions.yaml` | Health condition vocabulary; chronic disease; disability; malnutrition staging |

**Governance constraint:**

No Risk Domain work begins until the Shared Human Model design is complete and approved.

The Risk Domain (Stage 3) depends on lifecycle stage and capability concepts from the Shared Human Model. Proceeding without those foundations causes the Risk Domain to invent person concepts it does not own, violating ADR-007 and ADR-008.

---

# Architectural Principle

The Khidmat AI system is built in layers, from reality to software. Each layer depends on the layer below it being correct before the layer above can function.

```
Model Reality
  ↓
Model Ontology
  ↓
Model Taxonomy
  ↓
Model Reasoning
  ↓
Model Operations
  ↓
Model Software
```

**Ontology is the primary intelligence layer of Khidmat AI.**

The quality of every downstream capability — gap detection, severity classification, inference, verification brief generation, intervention fit, outcome measurement — depends entirely on the correctness and completeness of the ontology layer.

Software can be rewritten. Operations can be reorganised. Reasoning rules can be extended. But if the ontology is wrong, every layer built on top of it reasons incorrectly.

This is why concept ownership, domain activation sequencing, and governance file accuracy are not administrative tasks. They are the foundational engineering work that makes Khidmat AI trustworthy.
