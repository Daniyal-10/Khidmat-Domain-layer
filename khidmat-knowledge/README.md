# Khidmat Knowledge Layer

## Current Authority

The canonical conceptual foundation of this repository is
[`docs/00-governance/PROJECT_OVERVIEW.md`](docs/00-governance/PROJECT_OVERVIEW.md),
**frozen as Version 1.0**. The canonical governance authority is
[`docs/00-governance/CONSTITUTION.md`](docs/00-governance/CONSTITUTION.md), **Version 1.0**,
which converts the Overview's concepts into enforceable rules and is supreme over
every methodology and architecture document in this repository. Start with the
Overview, then the Constitution, not with this README, for vision, mandate,
philosophy, and governing rules.

This README is an orientation and status document, not a philosophical or
governance source.

---

## What This Repository Is

Khidmat AI is a **Humanitarian Intelligence Infrastructure** — not an application, a
registration platform, a donation platform, or an NGO CRM (Project Overview,
Chapter 3.1). This repository is the canonical humanitarian knowledge layer that
infrastructure is built on.

**Strategic Objective:** The ultimate objective of this repository is the successful design of the **Khidmat Humanitarian Ontology**. The immediate architectural goal is to map the specific domains via **Domain Discovery** (Stage 5), after which work will proceed to Ontology Design.

---

## Reading Order

1. **[`docs/00-governance/PROJECT_OVERVIEW.md`](docs/00-governance/PROJECT_OVERVIEW.md)** (v1.0) — the mandate, philosophy, knowledge-layer principles, business-capability model, and ethics. Read this in full before anything else.
2. **[`docs/00-governance/CONSTITUTION.md`](docs/00-governance/CONSTITUTION.md)** (v1.0) — the enforceable rules derived from the Overview: mandate, principles, epistemology, governance, constitutional order, and standards of success.
3. **[`docs/00-governance/VISION.md`](docs/00-governance/VISION.md)** — the normative vision statement, synchronized against the Overview.
4. **[`docs/00-governance/GLOSSARY.md`](docs/00-governance/GLOSSARY.md)** — ubiquitous language (pending full term-by-term reconciliation against the Overview — see the note at the top of that file).
5. **The dependency chain for everything downstream** (per the Constitution's Dependency Hierarchy, Article XVI):

   ```
   Project Overview (v1.0, frozen)
           â†“
   Constitution (v1.0, frozen) / Foundation / Philosophy / Principles   (docs/00-governance)
           â†“
   Business Master Plan                     (v1.0, frozen)
           â†“
   Humanitarian Business Reference Model    (v1.0, frozen)
           â†“
   Business Architecture (v1.0, frozen) â†’ Domain Discovery (Active) â†’ Ontology Design â†’ Ontology Engineering
   ```

**This repository contains no executable code.** There is nothing to install, build,
or run — every file is Markdown (documentation/governance) or, in the archived
engineering layer, YAML (ontology/taxonomy declarations).

---

## Current Status

| Layer | Status |
|---|---|
| Project Overview | âœ… **Frozen, v1.0** — canonical conceptual authority |
| Constitution | âœ… **Frozen, v1.0** — canonical governance authority. Articles XVII (Domain Approval Authority) and XVIII (Audit Authority) remain explicitly reserved pending a governance decision; Article XIX is reserved for a future amendment procedure. |
| Vision | âœ… Synchronized against Overview v1.0 |
| Foundation, Philosophy, Principles | â¬œ Not yet authored — empty stubs at `docs/00-governance/` |
| Business Master Plan | âœ… **Frozen** | Canonical Stage 2 completed and frozen. |
| Humanitarian Business Reference Model | âœ… **Frozen** | Canonical Stage 3 completed and frozen. |
| Ontology Design | â¬œ Not yet authored. Draft blueprint (`docs/01-methodology/ONTOLOGY_DESIGN_BLUEPRINT.md`) exists at v0.1.0. |
| Business Architecture | âœ… **Frozen** | Canonical Stage 4 completed and frozen. |
| Domain Discovery | ðŸŸ¡ **Active** | Stage 5 is currently active and mapping domains. |
| `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, `KHIDMAT_AI_BUSINESS_OVERVIEW.html` | ðŸ—„ **Superseded.** Replaced by the formal Stage 2, 3, and 4 artifacts. |
| Prior domain ontology/taxonomy engineering (Registration, Community Context, Verification Operations, and others) | ðŸ—„ **Removed from the working tree, recoverable from git history.** This content was schema-first ontology-engineering work that predates and does not follow the Overview's ontology-first discovery methodology (Chapters 5"“6), and cannot be treated as canonical input regardless of where it is stored (Constitution Article XV). It contained no unique canonical information beyond what git history already preserves and has been deleted rather than kept in the live archive; recoverable from git history at commit `d28d17e` and its ancestors if ever needed for reference. |

For the full reasoning behind this table, see the Repository Synchronization Report,
Integrity Report, and Provenance Report produced during the Overview v1.0
synchronization pass.

---

## Repository Structure

```
khidmat-knowledge/
â”œâ”€â”€ README.md
â””â”€â”€ docs/
    â”œâ”€â”€ 00-governance/       # Overview, Constitution (both canonical, frozen v1.0), Foundation,
    â”‚                        # Vision, Philosophy, Principles (pending), Glossary
    â”œâ”€â”€ 01-methodology/      # Business Master Plan, HBRM, Ontology Design, and their blueprints
    â”‚                        # (flat structure — every methodology document lives directly here)
    â”œâ”€â”€ 02-architecture/     # Canonical schemas, reference models (pending); also the
    â”‚                        # versioned business-logic spec and client-facing overview
    â”‚                        # (both flagged for terminology sync)
    â”œâ”€â”€ 03-domains/ "¦ 05-systems/   # Reserved layers, not yet active
    â”œâ”€â”€ 80-decisions/        # Reserved for the ADR ledger
    â”œâ”€â”€ 90-reports/          # Non-normative status reports (historical)
    â”œâ”€â”€ 98-archive/          # Superseded/deprecated documents that retain institutional value
    â”‚   â””â”€â”€ superseded-reviews/     # Valid, completed reviews whose recommendations are now fulfilled
    â”‚                               # (the engineering-layer and invalid-lifecycles categories were
    â”‚                               #  reviewed and deleted — no unique canonical information remained;
    â”‚                               #  see docs/98-archive/README.md for what was removed and why)
    â””â”€â”€ 99-references/       # Reserved for external references
```

**No project documentation remains at the repository root.** Only this README lives
there.

---

## Design Principles

The full principle set lives in Project Overview Chapter 2.2 and Constitution
Article II. In summary: knowledge precedes automation, understanding precedes
intelligence, evidence precedes conclusions, verification precedes trust, and human
dignity is the purpose of every decision. Every document in this repository is
expected to be explainable through these five — not through a separate,
locally-invented principle list.
