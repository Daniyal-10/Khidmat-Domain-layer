# KHIDMAT AI Architecture Review

**Reviewer role:** Independent systems architect
**Scope:** Read-only review. No documents rewritten, no architecture invented, no ontology redesigned.
**Date of review:** 2026-07-22

---

## Executive Summary

Khidmat AI is not one project at one stage — it is **two tracks running at very different maturities under one repository name.**

1. **The Knowledge Engineering track** (repository root: `shared/`, `registration/`, `case-management/`, `architecture-decisions/`, `catalog.yaml`, `ontology_authority_matrix.md`, `knowledge_layer_roadmap.md`, `docs/architecture/`) is mature, disciplined, and substantially advanced — 29 ratified/proposed ADRs, a frozen canonical ontology/taxonomy authoring contract, a dependency-gated activation roadmap through "Stage 9," and 12 of 13 domains at "Level 1 / Complete."

2. **The Documentation Operating System track** (`docs/00-governance/` through `docs/99-references/`) was created two commits ago. It is a numbered-layer scaffold that is almost entirely placeholder skeletons — empty frontmatter and a heading — with exactly two exceptions: `VISION.md` (fully written, normative) and `KHIDMAT_AI_PROJECT_OVERVIEW.md` (a working draft, explicitly labeled pre-foundation).

These two tracks are **not yet reconciled with each other.** The repository's own canonical entry point (root `README.md`) does not mention the new `docs/00-governance` system at all. The new system's governance files (`docs/00-governance/GLOSSARY.md`, a template stub) sit alongside an already-complete, already-referenced, already-in-use canonical `GLOSSARY.md` at the repository root. This is the central architectural fact this review surfaces: **the project is not missing foundational documents — it has two candidate homes for them, one populated and one empty, and no decision yet about which one is authoritative going forward.**

Given this, the project's current stage is best described as **Ontology Engineering (substantially advanced)** running ahead of a **Business/Governance Foundation (only just beginning formal codification)**. This is not a crisis — the project's own stated philosophy already governed the ontology work informally (via `AI_WORKFLOW.md`, the ADR log, and the roadmap) even though the formal Constitution/Foundation/Business Master Plan documents describing that philosophy are still blank. The recommended next milestone is narrow and dependency-driven, not a call to fill every empty file.

---

## Current Project Understanding

**What Khidmat AI is:** A "Humanitarian Intelligence Infrastructure" / "Humanitarian Operating System" — a canonical knowledge substrate (ontology + taxonomy + reasoning + governance) intended to sit *underneath* future AI agents and applications, not an application itself. The repository states this explicitly and consistently across `README.md`, `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, and `docs/00-governance/VISION.md`: applications are built on top of the intelligence layer, not the reverse.

**The problem it targets:** Existing humanitarian software (registration systems, case management, donor CRMs) records transactions but does not model the *context* around a person — family structure, dependency, risk trajectory, community setting — so it cannot reason, only store. Khidmat's stated remedy is a strict operating sequence: **Knowledge → Understanding → Reasoning → Automation**, with automation permitted only after understanding is established.

**What differentiates it from existing humanitarian software:** Most comparable systems are schema-first (a form, a database, a CRUD app). Khidmat is explicitly knowledge-first: the repository is pure declarative ontology/taxonomy/reasoning content with "no executable code" (README's own words), meant to be read by humans now and by a reasoning engine that does not yet exist. The philosophy of "Reference-Not-Redefine" and single concept ownership (ADR-008) is enforced with unusual rigor for a project at this stage — via a machine-checkable authority matrix, not just prose convention.

**Long-term vision:** A full humanitarian knowledge graph (`knowledge_layer_roadmap.md`, "Stage 10") reasoning simultaneously across Person → Family → Household → Community → Case, capable of proactive risk detection (e.g., flood-season shelter risk) and outcome-aware intervention matching — not merely donation logistics.

**Current direction:** Two simultaneous efforts are visible in the git history: (a) continued ontology remediation and domain completion (Donor & Resource domain, ADR-025 through ADR-029, most recently), and (b) a brand-new initiative, starting with the last two commits, to formally write the governance/methodology layer (`docs/00-governance` through `99-references`) that the ontology work has so far proceeded *without* in written form.

---

## Repository Assessment

**Two parallel canonical-document sets exist:**

| | Root-level system | New `docs/00-*` system |
|---|---|---|
| Age | Established over ~29 ADR cycles | 2 commits old |
| Entry point | `README.md` (populated, cross-linked) | `docs/README.md` (2 lines) |
| Vision doc | `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` (404 lines) | `docs/00-governance/VISION.md` (populated) + `KHIDMAT_AI_PROJECT_OVERVIEW.md` (draft) |
| Glossary | `GLOSSARY.md` (populated, in active use) | `docs/00-governance/GLOSSARY.md` (empty template) |
| Architecture | `ARCHITECTURE.md` (populated, domain inventory table) | `docs/02-architecture/ARCHITECTURE.md` (empty template) |
| Schema contracts | `docs/architecture/Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md` (ratified, in force) | `docs/02-architecture/CANONICAL_SCHEMAS.md` (empty template) |
| Governance workflow | `AI_WORKFLOW.md` (populated, defines AI roles) | no equivalent yet |
| Decision log | `architecture-decisions/` — 29 ADRs, indexed | `docs/80-decisions/README.md` (scope note only) |

Note the path collision risk: `docs/architecture/` (legacy, populated, referenced everywhere) and `docs/02-architecture/` (new, empty) are sibling-looking paths inside the same `docs/` folder with overlapping subject matter and no note connecting them.

**Which documents are complete (canonical, in active use):**
- Root: `README.md`, `ARCHITECTURE.md`, `GLOSSARY.md`, `AI_WORKFLOW.md`, `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, `catalog.yaml`, `ontology_authority_matrix.md`, `knowledge_layer_roadmap.md`, `OPERATIONAL_VALIDATION_SUITE.md`.
- `architecture-decisions/ADR-001` through `ADR-029` (one, ADR-023, and one, ADR-029, explicitly marked "Proposed / pending ratification" — correctly flagged as such, not silently treated as accepted).
- `docs/architecture/Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`, `Repository_Migration_Methodology.md`, plus domain-specific migration plans and audits (`Registration_Migration_Plan.md`, `Volunteer_Operations_Domain_Audit.md`, `Volunteer_Operations_Migration_Plan.md`).
- Domain-level `README.md` + `governance.md` for most active domains (`shared/human-model`, `shared/risk`, `volunteer-operations`, `community-context`, `donor-resource`).
- `docs/00-governance/VISION.md` — the one fully-written file in the new system, and a strong one.

**Which are intentional placeholders (correctly, not a defect):**
- `docs/00-governance/CONSTITUTION.md`, `FOUNDATION.md`, `PHILOSOPHY.md`, `PRINCIPLES.md`, `GLOSSARY.md` — empty frontmatter + heading only.
- All of `docs/01-methodology/*` (Business Architecture, Business Master Plan, Domain Discovery, Humanitarian Business Reference Model, Ontology Design, Knowledge Layer, Ontology Engineering, Taxonomy Engineering) — same empty-template pattern.
- `docs/02-architecture/*`, and the section `README.md`s for `03-domains`, `04-semantics`, `05-systems`, `80-decisions`, `90-reports`, `98-archive`, `99-references` — scope statements only, no content, and (correctly) no content is expected yet at `90-reports`/`98-archive` since there is nothing to report or archive under the new system yet.
- `consent-and-privacy/` domain (Level 2 per ADR-004) — deliberately undeveloped pending activation trigger.
- Volunteer Operations' operational/runtime (Tier 2) layer — deliberately deferred per ADR-024, with the foundational (Tier 1) layer already authored. This is the strongest example in the repository of the "placeholder, not gap" pattern working as designed.

**A real gap, not a placeholder:** `extensions/humanitarian/islamic/` and `extensions/governance/compliance/` contain authored `entities.yaml`/taxonomy YAML (Islamic giving/asnaf categories, compliance clearance types) but **appear in none of** `knowledge_layer_roadmap.md`, `ARCHITECTURE.md`'s Domain Inventory, or `ontology_authority_matrix.md`. Under the project's own ADR-008 rule ("no concept may be used in a reasoning rule if its ownership is undeclared"), this is a live governance gap, not a stylistic one — these concepts exist but their ownership is currently undeclared in the authority matrix that is supposed to be the single record of it. (Note: `donor-resource/taxonomy/islamic-giving.yaml` *is* properly declared under the Donor & Resource section of the authority matrix — the extensions-folder Islamic content appears to be a separate, earlier or parallel effort that was never reconciled with it.)

---

## Documentation Assessment

The new documentation operating system's layer scope statements (`00-governance` → `99-references`, each with its own `README.md` declaring Purpose/Scope/Upstream/Downstream) are well-formed as an *information architecture* — the layering logic (governance → methodology → architecture → domains → semantics → systems → decisions → reports → archive → references) is coherent and mirrors standard enterprise-architecture practice.

What is missing is not content inside that structure — that is expected at this stage — but a **migration or coexistence decision**: does `docs/00-governance/GLOSSARY.md` eventually *replace* root `GLOSSARY.md`, *link to* it, or *duplicate* it? The same question applies to `ARCHITECTURE.md`, the canonical schema contracts, and the ADR log. Until that is decided, every future contributor who lands on `docs/00-governance/README.md` first will not learn that a mature, 29-ADR-deep knowledge layer already exists two directories away.

The Blueprint document (`docs/00-governance/KHIDMAT_AI_PROJECT_OVERVIEW_BLUEPRINT.md`) is the most useful artifact in the new system for planning purposes: it lays out nine chapters in an explicit dependency order ("Chapters 1-2 ... must precede all other chapters ... Chapters 3-4 ... Depends on the mandate from Ch 1-2," etc.) and states which interview questions each chapter must answer before being written. Chapter 1 (`VISION.md`, committed as "complete chapter 1 humanitarian reality") is done. Chapter 2 (Philosophy/Principles) is the explicitly-declared next chapter and is currently empty (`PHILOSOPHY.md`, `PRINCIPLES.md`).

---

## Ontology Assessment

This is the strongest part of the repository. Findings:

- **Governance discipline is real, not aspirational.** `ontology_authority_matrix.md` is not a description of a principle — it is a working ledger with per-concept ownership rows, a "Flagged Boundary Cases" section that tracks *and resolves* concrete ownership ambiguities (e.g., FLAG-005's `household` vs. `household_snapshot` conflict was identified and fixed, not just noted), and cross-references to the ADR that ratified each resolution.
- **The canonical ontology/taxonomy authoring contract** (`docs/architecture/Canonical_Ontology_Schema.md`) is unusually rigorous for this project stage: it fixes a single five-file module shape, a single cardinality model, forbids OWL/SHACL syntax from being hand-authored into source files (target-neutral constraints only), and explicitly separates what is RATIFIED from what is PROPOSED section-by-section — an honest, auditable way to freeze architecture incrementally rather than all-at-once.
- **Domain activation is dependency-gated in practice, not just in the roadmap prose.** ADR-009 and ADR-024 ("Foundational Layer Precedes Operational Activation") show the roadmap's staging rules being applied to a real decision (Volunteer Operations) rather than existing only as an abstract policy.
- **Migration is incremental and honestly tracked.** Registration and Community Context are explicitly the only two domains confirmed migrated onto the frozen canonical contract; the README's Domain Inventory does not claim more progress than the migration plans support, and open items (e.g., Phase 5 CURIE linking blocked on a still-unratified repository-wide manifest/base-IRI) are named as blockers rather than silently deferred.
- **Ownership gap:** as noted above, the `extensions/` domains are the one clear exception to this otherwise-consistent discipline.

**Does the ontology still support the Project Overview's vision?** Yes, and unusually well for a project at this stage. The Overview's central claim — "Knowledge must always precede automation" — is *operationalized*, not just stated: ADR-004 (Placeholder Domain Strategy) and ADR-009 (Dependency-Driven Domain Activation) are the ontology-engineering-layer implementation of exactly that philosophical claim, months before the Constitution/Philosophy documents that are supposed to state it formally were written.

---

## Architectural Alignment

**Consistent:** The Overview's "Reality → Knowledge → Models → Intelligence → Software" sequence, and its claim that ontology design must precede ontology engineering, is reflected in the roadmap's stage-gating and in `AI_WORKFLOW.md`'s human-approval-required workflow. The vision documents and the engineering practice are not contradicting each other — they describe the same discipline from two different altitudes.

**Duplicated concepts:** `GLOSSARY.md` / `ARCHITECTURE.md` / canonical schema contracts each now exist in two places (root and `docs/`), one populated and one templated. Not yet a content conflict (the templated copies are empty), but a structural one waiting to happen the moment someone starts filling the templates without first checking the root versions.

**Conflicting ideas:** None found at the ontology-content level — the authority matrix's own self-auditing (Flagged Boundary Cases) is evidence the project actively looks for and resolves these rather than accumulating them silently. The one live conflict is organizational: two unreconciled documentation systems.

**Outdated assumptions worth revisiting eventually (not now):** `docs/02-architecture/README.md` states architecture's "Out of Scope" includes "Domain models," while `03-domains/README.md` states its own scope is domain models depending on `02-architecture` — this dependency direction is fine, but it presumes `02-architecture/ARCHITECTURE.md` will eventually be the canonical architecture document, which conflicts with the fact that the *actual* canonical `ARCHITECTURE.md` and its Domain Inventory table already live at the repository root and are actively maintained there.

---

## Current Project Stage

Using the requested scale (Vision → Business Understanding → Conceptual Modelling → Ontology Design → Ontology Engineering), the honest answer is that **the two tracks are at different stages simultaneously**:

- **Knowledge/Ontology Engineering track:** well into **Ontology Engineering**, arguably approaching **Ontology Maturity/Migration** — 12 of 13 domains complete at Level 1, a frozen authoring contract, two domains already migrated onto it, an ADR log documenting real design decisions and their resolutions.
- **Documentation/Governance track:** at **Vision**, having just completed its first formal chapter, with **Business Understanding** and **Conceptual Modelling** (Business Master Plan, Business Architecture, Domain Discovery, Ontology Design) still unwritten as formal documents — even though, informally, this thinking already happened (it is visible throughout the ADR log and `AI_WORKFLOW.md`) and simply has not yet been captured in the new document set's canonical form.

The project is not "behind" — it did the engineering work first and is now going back to formally write the governance layer that should, by its own stated methodology, have preceded it. That retroactive-formalization pattern is explicit in the git history itself (commit "refactor(docs): complete Phase A knowledge preservation" precedes "establish documentation operating system").

---

## Identified Risks

1. **Two unreconciled canonical-document homes.** If `docs/00-governance`/`01-methodology`/`02-architecture` are filled in without an explicit decision about their relationship to the root-level `README.md`/`ARCHITECTURE.md`/`GLOSSARY.md`/ADR log, the project risks producing two divergent sources of truth for the same concepts — the exact "ontology drift" failure mode `AI_WORKFLOW.md` was written to prevent, now recurring at the documentation-architecture level instead of the ontology level.
2. **`extensions/` domains have undeclared ownership.** Real content exists outside the authority matrix's coverage, which is a live violation of the project's own single-ownership rule (ADR-008), however small in surface area today.
3. **Path collision between `docs/architecture/` (legacy, populated) and `docs/02-architecture/` (new, empty).** Low current risk, but a naming trap for a future contributor or AI collaborator who is told to "update the architecture docs."
4. **The new documentation system's `README.md`s do not link to the mature root system.** A first-time reader entering through `docs/` alone would not discover that 29 ADRs and a working ontology already exist.

---

## Recommendations

- Before writing any further content into `docs/01-methodology` or `docs/02-architecture`, make one explicit governance decision (recorded as an ADR, consistent with the project's own practice) about whether the new `docs/00-*` system **absorbs, links to, or is superseded by** the root-level `README.md`/`ARCHITECTURE.md`/`GLOSSARY.md`/`architecture-decisions/` system. This is cheap to decide now and expensive to unwind later, exactly the class of decision this project already knows to ADR rather than let drift.
- Reconcile `extensions/humanitarian/islamic/` and `extensions/governance/compliance/` into `ontology_authority_matrix.md` and `knowledge_layer_roadmap.md`, or explicitly document why they are intentionally out of band.
- Do not fill `docs/98-archive` or `docs/90-reports` proactively — per their own scope statements, they are correctly empty until something is actually deprecated or a point-in-time report is actually produced.

---

## Recommended Next Milestone

**Write Chapter 2 of the documentation operating system — `docs/00-governance/PHILOSOPHY.md` and `PRINCIPLES.md`.**

Reasoning, by dependency rather than by absence:

- The Blueprint document that governs the new documentation track explicitly states Chapters 1–2 "must precede all other chapters" and that Chapters 3–4 (what Khidmat *is*, and the automation sequencing rules) *depend on* the mandate established in Chapters 1–2. Chapter 1 (`VISION.md`) is done. Every subsequent chapter in that track — including the Business Architecture and Ontology Design methodology documents that would otherwise look like the "obvious" next gap to fill — is blocked on Chapter 2 by the project's own stated logic, not by this review's judgment.
- This does not block or compete with the separate Knowledge/Ontology Engineering track, which has its own independent next steps (the operationally-blocked support-intervention taxonomy, and the repository-wide manifest/base-IRI ratification blocking Phase 5 CURIE linking for Registration and Community Context) — those may proceed in parallel.
- Writing Chapter 2 is also the natural moment to make the reconciliation decision flagged above (risk #1), since Chapter 2's "unbreakable laws" content is exactly where a principle like "the knowledge layer's existing governance artifacts are canonical; this document system extends, not replaces, them" would belong if that is the intended relationship — making the decision explicit rather than discovering it by accident three chapters later.
