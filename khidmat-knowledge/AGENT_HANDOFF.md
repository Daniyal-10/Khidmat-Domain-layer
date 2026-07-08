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
| Registration Domain | Complete (Level 1) — canonical reference implementation (Phases 1–4 of its migration plan complete; Phase 5 blocked on a repository-wide manifest) |
| Shared Domain — base taxonomy | Active |
| Shared Human Model | Complete |
| Risk Domain | Complete |
| Verification Operations Domain | Complete (core ontology and reasoning) |
| Needs Assessment Domain | Complete |
| Case Management Domain | Complete |
| Beneficiary Lifecycle Domain | Complete |
| Community Context Domain | Active / In Progress — substantially built, pending canonical migration |
| Governance Layer | Complete, including the frozen `docs/architecture/Canonical_Ontology_Schema.md` and `Canonical_Taxonomy_Schema.md` contracts and ADR-023 |
| All other placeholder domains (Volunteer Operations, Support Delivery, Programs, Impact, Consent & Privacy) | Level 2 — inactive |

Source of truth: `ontology_completion_checklist.md`, `knowledge_layer_roadmap.md`

---

# Current Phase

**Repository Architecture Freeze — Canonical Migration (Active / In Progress)**

The Risk Domain, Verification Operations, Needs Assessment, Case Management, and
Beneficiary Lifecycle domains are complete. The canonical `ontology/`+`taxonomy/`
authoring contract is frozen and Registration has been migrated onto it as the
reference implementation. The current focus is completing the remaining registration
content gaps (see `docs/architecture/Registration_Migration_Plan.md`'s Content Gap
Log) and migrating Community Context onto the same canonical structure.

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
- registration/ontology/{entities,data-properties,relationships,semantic-constraints,lifecycle-constraints}.yaml
  (canonical structure; supersedes the retired `attributes.yaml`)

Governance completed:

- knowledge_layer_inventory.md
- ontology_completion_checklist.md
- ontology_authority_matrix.md
- knowledge_layer_roadmap.md
- shared/human-model/governance.md
- shared/risk/governance.md
- verification-operations/verification-operations.yaml (Core Ontology)
- docs/architecture/Canonical_Ontology_Schema.md, Canonical_Taxonomy_Schema.md,
  Repository_Migration_Methodology.md (frozen structural and process contracts)
- architecture-decisions/ADR-023 (ontology vocabulary extension: Value Objects, Roles,
  Runtime/Reasoning Objects, Future Entity Candidate)

Current objective:

Close registration's remaining Content Gap Log entries (genuine content gaps requiring
a domain-knowledgeable author, per `docs/architecture/Repository_Migration_Methodology.md`
§6) and begin Community Context's migration to the canonical structure.

No new domain activation should begin until architecture review and Human Owner approval.

---

# Immediate Objective

Community Context is the next domain targeted for canonical migration, following
Registration's completed reference implementation. The Support Intervention Taxonomy
in the registration domain remains a genuine content gap — it is blocked on an
operational intervention catalogue from programme staff, not on architecture.

---

# What Must Not Be Done

- Do not activate the remaining Level 2 placeholder domains (Volunteer Operations, Support Delivery, Programs, Impact, Consent & Privacy)
- Do not redefine concepts already owned by the shared layer
- Do not bypass `ontology_authority_matrix.md`
- Do not create ontology concepts without architectural review and Human Owner approval
- Do not modify operational software
- Do not author ontology or taxonomy YAML off the canonical file-shape contracts (`docs/architecture/Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`)

---

# Governance References

Review these files before beginning any ontology work:

| File | Purpose |
|---|---|
| `AI_WORKFLOW.md` | Who does what; mandatory workflow; authority order |
| `ARCHITECTURE.md` | Domain inventory; dependency rules; maturity levels |
| `docs/architecture/Canonical_Ontology_Schema.md` | Frozen file-shape contract every domain's `ontology/` module must follow |
| `docs/architecture/Canonical_Taxonomy_Schema.md` | Frozen file-shape contract every domain's `taxonomy/` module must follow |
| `docs/architecture/Repository_Migration_Methodology.md` | The process by which a legacy domain is brought into conformance with the two contracts above |
| `DECISIONS.md` | Architectural Decision Log — mirrors ADR-001 through ADR-014 only; ADR-015 onward exist only in `architecture-decisions/` |
| `GLOSSARY.md` | Authoritative term definitions by ownership boundary |
| `knowledge_layer_inventory.md` | Every file's ownership, maturity, and known gaps |
| `ontology_authority_matrix.md` | Single-owner concept registry |
| `ontology_completion_checklist.md` | What is done, in progress, missing, and future |
| `knowledge_layer_roadmap.md` | Stage-by-stage dependency and activation order |

For general onboarding and reading order, `README.md` is the canonical guide — this
table is scoped specifically to what to check before an ontology change, not a full
onboarding path.

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

Repository Architecture Freeze — Canonical Migration (Active / In Progress)

Recent completion: Registration's canonical migration through Phase 4
(`docs/architecture/Registration_Migration_Plan.md`) — `registration/ontology/attributes.yaml`
has been deleted and replaced by the canonical `entities.yaml` / `data-properties.yaml` /
`relationships.yaml` / `semantic-constraints.yaml` / `lifecycle-constraints.yaml` set.

Next active implementation target:
1. Close the remaining entries in the Registration Content Gap Log
   (`docs/architecture/Registration_Migration_Plan.md`) — genuine content gaps requiring a
   domain-knowledgeable author, not architecture work.
2. Begin Community Context's migration onto the canonical `ontology/`+`taxonomy/` structure
   (`docs/architecture/Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`,
   `Repository_Migration_Methodology.md`), following Registration as the reference pattern.
