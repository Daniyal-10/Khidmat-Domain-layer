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
- Governance review: verifying that proposed changes conform to ARCHITECTURE.md and the ADR log (architecture-decisions/)
- Roadmap compliance: ensuring domain activation follows knowledge_layer_roadmap.md dependencies
- Authority matrix compliance: ensuring concept ownership is correctly declared in ontology_authority_matrix.md
- Progress tracking: reporting current state against the roadmap

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
- Documentation updates: updating ARCHITECTURE.md, GLOSSARY.md, and governance files (recording decisions as ADRs in architecture-decisions/) as directed

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

## catalog.yaml

**Purpose:** The machine-readable repository manifest — namespaces, canonical prefixes, module paths, and the cross-domain dependency graph. The authoritative inventory of what exists in the repository.

**Update when:** A new domain or module is added, a namespace/prefix changes, or a dependency edge changes.

**Authority:** Knowledge Layer Architect.

---

## ontology_authority_matrix.md

**Purpose:** Declares the authoritative owner for every concept in the knowledge layer. Enforces single ownership per ADR-008.

**Update when:** A new concept is introduced, a concept's ownership changes, or a concept is promoted from a domain file to shared ownership.

**Authority:** Knowledge Layer Architect, with Human Owner final approval.

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

## architecture-decisions/

**Purpose:** The Architecture Decision Record (ADR) log — the complete, authoritative record of every significant design decision, its context, consequences, and rejected alternatives. Indexed by `architecture-decisions/README.md`. ADR files are immutable; a reversal is recorded as a new ADR.

**Update when:** A design decision is made or reversed.

**Authority:** Human Owner approves each ADR before it is accepted.

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
| New file created | catalog.yaml |
| Domain activation | ARCHITECTURE.md, knowledge_layer_roadmap.md |
| Architectural decision | architecture-decisions/ (new ADR) |
| New vocabulary term | GLOSSARY.md |
| Ownership change | ontology_authority_matrix.md |

Review does not necessarily imply modification. However, every listed file must be checked before work is considered complete.

This checklist exists to prevent future AI systems from closing a task without completing the corresponding governance updates.

---

# Repository Authority Order

This repository has two distinct kinds of governance, and a file disagreement is
resolved differently depending on which kind it is. Do not apply one order to a
question the other kind governs.

## A. Concept Ownership Governance

Governs *what a domain may model* — which concept exists, who owns it, whether a
domain is allowed to activate. When files in this list disagree:

1. Human Owner decisions
2. The ADR log (`architecture-decisions/`) — the complete, authoritative record
3. `ARCHITECTURE.md`
4. `knowledge_layer_roadmap.md`
5. `ontology_authority_matrix.md`
6. `catalog.yaml` (repository manifest)
7. `GLOSSARY.md`

## B. Canonical File-Shape Governance

Governs *how a domain's `ontology/`/`taxonomy/` files must be structured* —
header shape, entity/property/relationship serialization, constraint format.
When a file's shape and a domain's actual YAML disagree, or when applying a
migration:

1. Human Owner decisions
2. `docs/architecture/Canonical_Ontology_Schema.md` and
   `docs/architecture/Canonical_Taxonomy_Schema.md` (frozen and ratified — "when
   this document and a domain file disagree, this document wins")
3. `docs/architecture/Repository_Migration_Methodology.md` (governs *how* a
   domain migrates onto the two contracts above; never overrides them)
4. A domain's own migration plan (e.g. `docs/architecture/Registration_Migration_Plan.md`)

A domain's ontology/taxonomy content (what it means) is never decided by order B —
that is always order A's concern. Order B only decides the shape a already-approved
concept is serialized into.

Lower-ranked files, in either order, must be updated to align with higher-ranked
files. Conflicts must not be resolved by silent modification of a lower-ranked file
if doing so contradicts a higher-ranked one. When a genuine conflict exists between
two files at different authority levels, it should be surfaced and resolved through
a new ADR (for order A) or a documented amendment to the relevant contract (for
order B) rather than resolved silently.

This order becomes essential as the repository grows and multiple AI sessions
operate across the same governance layer.

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

**Current focus: Repository Architecture Freeze — Canonical Migration**

The Shared Human Model, Risk Domain, Verification Operations, Needs Assessment, Case
Management, and Beneficiary Lifecycle domains are all complete. The knowledge layer's
active priority has moved on from domain content to repository-wide structural
conformance:

- The canonical `ontology/`+`taxonomy/` authoring contract is frozen
  (`docs/architecture/Canonical_Ontology_Schema.md`, `docs/architecture/Canonical_Taxonomy_Schema.md`),
  extended by ADR-023 (Value Objects, Roles, Runtime/Reasoning Objects, Future Entity
  Candidate).
- **Registration is canonical through Phase 4** of its migration plan
  (`docs/architecture/Registration_Migration_Plan.md`) — `attributes.yaml` has been
  deleted and replaced by the canonical `entities.yaml` / `data-properties.yaml` /
  `relationships.yaml` / `semantic-constraints.yaml` / `lifecycle-constraints.yaml` set.
  Phase 5 (cross-domain CURIE linking) remains blocked on a repository-wide manifest.
- **Community Context is the next domain targeted for canonical migration**, following
  Registration as the reference pattern (`docs/architecture/Repository_Migration_Methodology.md`).

**Governance constraint:**

No new domain concept is authored ahead of the canonical file-shape contracts.
Registration's own remaining Content Gap Log entries (genuine content gaps, not
structural ones) must be closed by a domain-knowledgeable author before Registration's
migration is considered fully complete — see
`docs/architecture/Registration_Migration_Plan.md`.

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
