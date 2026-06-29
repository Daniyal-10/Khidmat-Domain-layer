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
| Registration Domain | Complete (Level 1) |
| Shared Domain — base taxonomy | Active |
| Governance Layer | Complete (Phase 4.0) |
| Shared Human Model | Complete (Phase 2.4) |
| Risk Domain | Complete (Phase 3.0) |
| Verification Operations Domain | Active / In Progress (Phase 4.0) |
| All other placeholder domains | Level 2 — inactive |

Source of truth: `ontology_completion_checklist.md`, `knowledge_layer_roadmap.md`

---

# Current Phase

**Phase 4.0 — Verification Operations (Active / In Progress)**

The Risk Domain (including reasoning) is complete. The Verification Operations core ontology (verification-operations.yaml) is complete. Operational verification models remain pending.

Completed:

- lifecycle-stages.yaml
- dependency.yaml
- capabilities.yaml
- family-structure.yaml
- health-conditions.yaml
- hazard-categories.yaml
- exposure.yaml
- vulnerability.yaml
- protective-factors.yaml
- household-resilience.yaml
- risk.yaml
- compound-risk-detection.yaml
- verification-operations.yaml

Governance completed:

- knowledge_layer_inventory.md
- ontology_completion_checklist.md
- ontology_authority_matrix.md
- knowledge_layer_roadmap.md
- health-conditions-governance.md
- risk-domain-governance.md
- verification-operations/verification-operations.yaml (Core Ontology)

Current objective:

Verification Operations is now the active / in progress architecture target.

No Case Management implementation should begin until architecture review and Human Owner approval.

| File | Purpose |
|---|---|
| `verification-operations.yaml` | Declares core Verification Operations ontology concepts and relationships |

---

# Immediate Objective

Verification Operations is now the active / in progress architecture target.

**Stage 1 Dependency Anomaly Note:**
The Verification Operations core ontology is completed. However, there is a recognized Stage 1 dependency anomaly: the Support Intervention Taxonomy, Evidence Taxonomy, and Evidence attributes in the registration domain are incomplete.

The immediate next priority is to reconcile these missing Stage 1 requirements to support the physical integration of Verification Operations without causing schema mismatch on Evidence.

---

# What Must Not Be Done

- Do not activate placeholder domains
- Do not create Case Management files
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

Phase 4.0 — Verification Operations (Active / In Progress)

Recent completion: verification-operations/verification-operations.yaml

Next active implementation target:
1. Address the missing Stage 1 prerequisites (specifically `Evidence` attribute schema in registration/ontology/attributes.yaml and registration/taxonomy/evidence.yaml).
2. Plan and implement Verification Operations reasoning rules and operational models (e.g., assignment, field visit, claim confirmation).
