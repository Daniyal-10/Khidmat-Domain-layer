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
infrastructure is built on: ontology, business methodology, and governance content,
not application code or runtime behavior.

---

## Reading Order

1. **[`docs/00-governance/PROJECT_OVERVIEW.md`](docs/00-governance/PROJECT_OVERVIEW.md)** (v1.0) — the mandate, philosophy, knowledge-layer principles, business-capability model, and ethics. Read this in full before anything else.
2. **[`docs/00-governance/CONSTITUTION.md`](docs/00-governance/CONSTITUTION.md)** (v1.0) — the enforceable rules derived from the Overview: mandate, principles, epistemology, governance, constitutional order, and standards of success.
3. **[`docs/00-governance/VISION.md`](docs/00-governance/VISION.md)** — the normative vision statement, synchronized against the Overview.
4. **[`docs/00-governance/GLOSSARY.md`](docs/00-governance/GLOSSARY.md)** — ubiquitous language (pending full term-by-term reconciliation against the Overview — see the note at the top of that file).
5. **The dependency chain for everything downstream** (per the Constitution's Dependency Hierarchy, Article XVI):

   ```
   Project Overview (v1.0, frozen)
           ↓
   Constitution (v1.0, frozen) / Foundation / Philosophy / Principles   (docs/00-governance)
           ↓
   Business Master Plan                     (docs/01-methodology — not yet authored; see note below)
           ↓
   Humanitarian Business Reference Model    (docs/01-methodology — not yet authored)
           ↓
   Business Architecture → Domain Discovery → Ontology Design → Ontology Engineering
   ```

**This repository contains no executable code.** There is nothing to install, build,
or run — every file is Markdown (documentation/governance) or, in the archived
engineering layer, YAML (ontology/taxonomy declarations).

---

## Current Status

| Layer | Status |
|---|---|
| Project Overview | ✅ **Frozen, v1.0** — canonical conceptual authority |
| Constitution | ✅ **Frozen, v1.0** — canonical governance authority. Articles XVII (Domain Approval Authority) and XVIII (Audit Authority) remain explicitly reserved pending a governance decision; Article XIX is reserved for a future amendment procedure. |
| Vision | ✅ Synchronized against Overview v1.0 |
| Foundation, Philosophy, Principles | ⬜ Not yet authored — empty stubs at `docs/00-governance/` |
| Business Master Plan | ⬜ **Not yet authored.** A prior session produced a full governance trail (review, resolution, certification) describing this as complete — that trail was found to describe content that was never actually written. It contained no unique canonical information and has been removed (recoverable from git history); its four genuinely-grounded discovery topics were merged into `docs/01-methodology/BUSINESS_MASTER_PLAN_BLUEPRINT.md` §7, which remains the valid authoring methodology. |
| Humanitarian Business Reference Model | ⬜ Not yet authored. Its Blueprint (`docs/01-methodology/HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT.md`) is genuinely complete and internally consistent, and governs future authoring once the Business Master Plan exists. |
| Ontology Design | ⬜ Not yet authored. Draft blueprint (`docs/01-methodology/ONTOLOGY_DESIGN_BLUEPRINT.md`) exists at v0.1.0. |
| Business Architecture, Domain Discovery, Knowledge Layer methodology, Taxonomy Engineering, Ontology Engineering | ⬜ Not yet authored — empty stubs at `docs/01-methodology/` |
| `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, `KHIDMAT_AI_BUSINESS_OVERVIEW.html` | ⬜ **Flagged, not yet synchronized.** Both predate the Overview/Constitution and contain a principle list and pipeline terminology that differ from the now-canonical versions. Located at `docs/02-architecture/`. See the in-file sync banners for specifics. |
| Prior domain ontology/taxonomy engineering (Registration, Community Context, Verification Operations, and others) | 🗄 **Removed from the working tree, recoverable from git history.** This content was schema-first ontology-engineering work that predates and does not follow the Overview's ontology-first discovery methodology (Chapters 5–6), and cannot be treated as canonical input regardless of where it is stored (Constitution Article XV). It contained no unique canonical information beyond what git history already preserves and has been deleted rather than kept in the live archive; recoverable from git history at commit `d28d17e` and its ancestors if ever needed for reference. |

For the full reasoning behind this table, see the Repository Synchronization Report,
Integrity Report, and Provenance Report produced during the Overview v1.0
synchronization pass.

---

## Repository Structure

```
khidmat-knowledge/
├── README.md
└── docs/
    ├── 00-governance/       # Overview, Constitution (both canonical, frozen v1.0), Foundation,
    │                        # Vision, Philosophy, Principles (pending), Glossary
    ├── 01-methodology/      # Business Master Plan, HBRM, Ontology Design, and their blueprints
    │                        # (flat structure — every methodology document lives directly here)
    ├── 02-architecture/     # Canonical schemas, reference models (pending); also the
    │                        # versioned business-logic spec and client-facing overview
    │                        # (both flagged for terminology sync)
    ├── 03-domains/ … 05-systems/   # Reserved layers, not yet active
    ├── 80-decisions/        # Reserved for the ADR ledger
    ├── 90-reports/          # Non-normative status reports (historical)
    ├── 98-archive/          # Superseded/deprecated documents that retain institutional value
    │   └── superseded-reviews/     # Valid, completed reviews whose recommendations are now fulfilled
    │                               # (the engineering-layer and invalid-lifecycles categories were
    │                               #  reviewed and deleted — no unique canonical information remained;
    │                               #  see docs/98-archive/README.md for what was removed and why)
    └── 99-references/       # Reserved for external references
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
