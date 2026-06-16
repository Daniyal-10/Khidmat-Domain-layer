# AGENT_HANDOFF.md — Khidmat Knowledge Layer Quick-Start Briefing

**For:** Any AI agent entering this project
**Read time:** Under 2 minutes
**Full governance:** See AI_WORKFLOW.md

---

# Project Overview

The Khidmat Knowledge Layer models humanitarian domain knowledge for an
AI-assisted beneficiary registration and case management system. This
repository contains ontology, taxonomy, reasoning rules, and governance
documents. It is not application code. Do not treat it as software.

The primary intelligence of the Khidmat AI system lives here.

---

# Current State

| Layer | Status |
|---|---|
| Registration Domain | Largely complete (Level 1) |
| Shared Domain — base taxonomy | Partially complete |
| Governance Layer | Established (Phase 2.0) |
| Shared Human Model | Not yet implemented |
| Risk Domain | Planned, not yet activated |
| All other placeholder domains | Level 2 — inactive |

Source of truth: `ontology_completion_checklist.md`, `knowledge_layer_roadmap.md`

---

# Current Phase

**Phase 2.0 — Shared Human Model**

Active implementation target: `shared/human-model/`

| File | Purpose |
|---|---|
| `README.md` | Scope declaration |
| `lifecycle-stages.yaml` | Developmental stages as reasoning contexts |
| `capabilities.yaml` | Human capabilities as strengths, not deficits |
| `dependency.yaml` | Care and support dependency relationships |
| `family-structure.yaml` | Family unit distinct from household |
| `health-conditions.yaml` | Chronic disease, disability, malnutrition vocabulary |

---

# Immediate Objective

Complete the Shared Human Model. It is the foundational prerequisite for:

- Risk Domain (Stage 3)
- Beneficiary Lifecycle Domain (Stage 7)
- Future community-level modelling
- Future impact measurement capabilities

**No Risk Domain work begins before Shared Human Model completion.**
This is a hard governance constraint per `knowledge_layer_roadmap.md` and ADR-007.

---

# What Must Not Be Done

- Do not activate placeholder domains
- Do not create Risk Domain files
- Do not redefine concepts already owned by the shared layer
- Do not bypass `ontology_authority_matrix.md`
- Do not create ontology concepts without architectural review and Human Owner approval
- Do not modify operational software

---

# Governance References

Review these files before beginning any ontology work:

| File | Purpose |
|---|---|
| `AI_WORKFLOW.md` | Who does what; mandatory workflow; authority order |
| `ARCHITECTURE.md` | Domain inventory; dependency rules; maturity levels |
| `DECISIONS.md` | Architectural Decision Log (ADR-001 through ADR-009) |
| `GLOSSARY.md` | Authoritative term definitions by ownership boundary |
| `knowledge_layer_inventory.md` | Every file's ownership, maturity, and known gaps |
| `ontology_authority_matrix.md` | Single-owner concept registry |
| `ontology_completion_checklist.md` | What is done, in progress, missing, and future |
| `knowledge_layer_roadmap.md` | Stage-by-stage dependency and activation order |

---

# AI Roles

The **Human Owner** holds final approval authority over all decisions.
**ChatGPT** acts as Chief Knowledge Architect — it designs ontology and
reviews domain boundaries but does not write files. **Claude Supervisor**
audits governance compliance, maintains the checklist, and enforces roadmap
sequencing but does not create concepts. **Antigravity Agent** implements
approved designs — creating and editing files — but does not invent concepts
without prior architectural review.

---

# Current Next Step

Design and implement `shared/human-model/` in full before any Risk Domain
work begins. Read `knowledge_layer_roadmap.md` Stage 2 for the complete
scope. All designs require Human Owner approval before implementation.
