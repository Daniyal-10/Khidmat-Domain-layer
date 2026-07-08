# Khidmat Knowledge Layer

## Vision

Khidmat AI is not a registration system. It is a **Humanitarian Operating System** —
software designed to understand people, families, households, communities,
vulnerabilities, capabilities, risks, and support pathways so that assistance can be
delivered accurately, fairly, proactively, and at scale.

Most systems answer *"what did this person ask for?"*. Khidmat is designed to answer
*"what does this person need, why do they need it, what happens if the need goes
unmet, who else is affected, and what support pathway exists?"* — including needs
that are implied, emerging, or likely to occur in the future, before the beneficiary
has to ask.

See [`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`](KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md)
for the full statement of that vision.

This repository is the **canonical humanitarian knowledge layer** underneath that
vision. It is not application code, and it does not implement runtime behaviour. It
is the ontology, taxonomy, reasoning, and governance substrate that every future
Khidmat AI agent, service, or reasoning engine is expected to be built on top of.

---

## Repository Purpose

This repository defines, for the humanitarian domain Khidmat operates in:

- **Ontology** — the entities, relationships, and structural constraints that
  describe what exists (a Beneficiary, a Household, a Need, a Risk, a Verification
  Activity, and how they relate).
- **Taxonomy** — the controlled vocabularies used to classify those entities (need
  categories, situation triggers, risk hazard categories, verification outcomes).
- **Reasoning** — deterministic, human-readable inference, severity, gap-detection,
  and coherence rules that describe how the AI should reason over the ontology.
- **Questioning** — the conversational strategy and question templates an AI
  registration agent uses to fill knowledge gaps responsibly.
- **Readiness** — the conditions under which a case is considered complete enough
  to progress (e.g. to verification).
- **Verification** — how claims made during registration are confirmed in the
  field, and how that evidence feeds back into the knowledge model.
- **Governance** — how ownership, authority, and change control are enforced across
  every domain, so that the knowledge graph stays internally consistent as it grows.

Everything here is intentionally declarative. It is designed to be consumed by an
AI reasoning layer (not yet built in this repository — see
[Architecture](#architecture)) rather than to execute anything itself.

---

## Current Status

| Layer | Status |
|---|---|
| Repository Architecture (canonical file/module contract) | ✅ Frozen — `docs/architecture/Canonical_Ontology_Schema.md` and `Canonical_Taxonomy_Schema.md` |
| Canonical Ontology Structure | ✅ Stable — ratified 5-file `ontology/` module shape (`entities`, `data-properties`, `relationships`, `semantic-constraints`, `lifecycle-constraints`) |
| Canonical Taxonomy Structure | ✅ Stable — ratified `schemes:` → `concepts:` module shape |
| Registration Domain | ✅ Canonical Reference Implementation — first domain migrated to the canonical structure (Phases 1–4 complete; Phase 5 cross-domain CURIE linking blocked on a repository-wide manifest) |
| Shared Domain (base taxonomy, Human Model, Risk) | ✅ Stable |
| Needs Assessment, Case Management, Beneficiary Lifecycle Domains | ✅ Complete (Level 1) |
| Verification Operations Domain | ✅ Core ontology and reasoning complete |
| Community Context Domain | 🚧 Substantially built (12 taxonomy files, full ontology module) — not yet migrated to the canonical structure |
| Volunteer Operations, Support Delivery, Programs, Impact, Consent & Privacy | 🚧 Level 2 placeholders — scope declared, not yet active |

For the authoritative, continuously-updated view of what is done, in progress, and
missing, see `ontology_completion_checklist.md` and `knowledge_layer_roadmap.md` —
this table is a snapshot for orientation, not the source of truth.

---

## Repository Structure

```
khidmat-knowledge/
├── shared/                    # Cross-domain foundation: base taxonomy, Human Model, Risk
├── registration/              # Intake conversation domain — the canonical reference implementation
├── community-context/         # Geographic, environmental, and social context of a household
├── verification-operations/   # Field verification of claims made during registration
├── needs-assessment/          # Synthesizes claims + verified facts into identified needs
├── case-management/           # Case orchestration: plans, referrals, follow-ups, assignments
├── beneficiary-lifecycle/     # Macro-state tracking of a beneficiary's engagement over time
├── support-delivery/          # (placeholder) How an approved intervention is actually delivered
├── programs/                  # (placeholder) Structured, multi-case programmatic assistance
├── impact/                    # (placeholder) Longitudinal outcome and impact measurement
├── volunteer-operations/      # (placeholder) Volunteer profile, capacity, and dispatch
├── consent-and-privacy/       # (placeholder) Consent, minimal today, required by Case Management
├── architecture-decisions/    # ADR-001 … ADR-023 — the authoritative decision log
└── docs/architecture/         # Canonical schema contracts, migration methodology, audits
```

**shared/** — The single-ownership home for concepts used by two or more domains:
person/organisation/location/document/time vocabulary, the Shared Human Model
(lifecycle stages, capabilities, dependency, family structure, health conditions),
and the Risk Domain (hazard, exposure, vulnerability, household resilience, risk
composition). Per ADR-008, nothing here may be redefined elsewhere.

**registration/** — Models a single intake conversation end-to-end: actors, needs,
situations, claims, evidence, support interventions, gap detection, severity
classification, case coherence, questioning strategy, and readiness-for-verification
rules. This is the most mature domain and the first one migrated to the canonical
`ontology/`+`taxonomy/` structure — treat it as the reference pattern for future
domain migrations.

**community-context/** — Models the geographic, infrastructural, environmental, and
social fabric a household sits inside (settlement type, accessibility, hazards,
seasonal events, local organisations). Built out extensively but still pending
migration to the canonical structure.

**verification-operations/** — Produces verification knowledge (field observations,
findings, confidence, escalation, reverification triggers) from activities performed
against registration outputs.

**needs-assessment/** — A synthesis layer: turns registration claims and
verification findings into `IdentifiedNeed`s with explicit confidence, decoupled
from case orchestration.

**case-management/**, **beneficiary-lifecycle/** — Orchestration and longitudinal
tracking once a case exists: case plans, referrals, follow-ups, and the
macro-lifecycle (lead → registration → verification → beneficiary → support →
outcome) a person moves through over time.

**support-delivery/**, **programs/**, **impact/**, **volunteer-operations/**,
**consent-and-privacy/** — Declared Level 2 placeholders (ADR-004). Each has a
scope statement and an explicit concept-ownership boundary, but no taxonomy or
ontology content is authored until the domain is activated per
`knowledge_layer_roadmap.md`.

---

## Architecture

The knowledge layer is built in dependency order, from business reality down to a
form an AI agent can reason over:

```
Business Blueprint (KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md)
        ↓
     Ontology            — what exists, and how it relates (entities, relationships)
        ↓
     Taxonomy            — controlled vocabularies for classifying it
        ↓
     Reasoning           — deterministic inference, severity, gap, and coherence rules
        ↓
   Knowledge Graph       — the composed, cross-domain semantic model
        ↓
    AI Agents            — the (not-yet-built) runtime that consumes this layer
```

Every domain's `ontology/` module follows one fixed, frozen file contract —
`entities.yaml`, `data-properties.yaml`, `relationships.yaml`,
`semantic-constraints.yaml`, `lifecycle-constraints.yaml` — and every `taxonomy/`
module follows one fixed `schemes:` → `concepts:` contract. Concept ownership is
single-sourced (ADR-008): a concept is referenced by many domains but defined in
exactly one. Cross-domain dependencies must form a Directed Acyclic Graph — no
domain may create a circular reference to another.

**This repository stops at the knowledge layer.** It defines what an AI agent
should know and how it should reason; it does not yet define the runtime,
orchestration, or working-memory layer that would execute that reasoning against a
live case. That is deliberately out of scope here (see `AI_WORKFLOW.md`'s
architectural principle) and is expected to be designed against this layer once it
is stable.

---

## Documentation Guide

Start here, in order:

1. [`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`](KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md)
   — the business vision this repository exists to serve.
2. [`ARCHITECTURE.md`](ARCHITECTURE.md) — domain inventory, dependency rules,
   maturity levels.
3. [`docs/architecture/Canonical_Ontology_Schema.md`](docs/architecture/Canonical_Ontology_Schema.md)
   and [`docs/architecture/Canonical_Taxonomy_Schema.md`](docs/architecture/Canonical_Taxonomy_Schema.md)
   — the normative, frozen authoring contracts every domain's ontology/taxonomy
   module must conform to.
4. [`docs/architecture/Repository_Migration_Methodology.md`](docs/architecture/Repository_Migration_Methodology.md)
   — the general process by which a legacy domain is brought into conformance with
   the two contracts above (used by, e.g., `docs/architecture/Registration_Migration_Plan.md`).
5. [`architecture-decisions/`](architecture-decisions/) — the ADR log (ADR-001
   through ADR-023) recording every significant design decision and its rationale.
6. [`GLOSSARY.md`](GLOSSARY.md) — the ubiquitous language, organised by ownership
   boundary.

For day-to-day governance mechanics — who owns what, how a change is proposed and
reviewed, and what must never be done — see [`AI_WORKFLOW.md`](AI_WORKFLOW.md) and
[`AGENT_HANDOFF.md`](AGENT_HANDOFF.md). For what exists, what's in progress, and
what's missing, see `knowledge_layer_inventory.md`, `ontology_authority_matrix.md`,
`ontology_completion_checklist.md`, and `knowledge_layer_roadmap.md`.

---

## Current Roadmap

Registration is the completed reference implementation for the canonical
architecture. The Shared Human Model, Risk Domain, Verification Operations, Needs
Assessment, Case Management, and Beneficiary Lifecycle domains are substantively
complete. Remaining work is migrating the older domains (Community Context and the
other Level 1 domains built before the canonical contract was frozen) onto the same
structure, closing the small number of genuine content gaps recorded in each
domain's own migration plan (e.g. registration's support-intervention taxonomy,
which depends on an operational intervention catalogue from programme staff), and
then activating the remaining Level 2 placeholder domains in the dependency order
`knowledge_layer_roadmap.md` defines. Internal migration task lists live in
`docs/architecture/` and the domain-specific migration plans, not here.

---

## Design Principles

- **Single ownership of concepts** (ADR-008) — every concept has exactly one
  authoritative owner, declared in `ontology_authority_matrix.md`. Every other
  file references it; none redefine it.
- **Separation of ontology and taxonomy** — entities/relationships (what exists,
  how it connects) are governed independently from controlled vocabularies (how
  values are classified), each with its own frozen schema contract.
- **Domain-driven knowledge organization** — each bounded context (registration,
  risk, verification, etc.) owns its own concepts and activates only once its
  prerequisites are substantially complete (ADR-009), preventing premature
  invention and ontology drift.
- **Reasoning separated from knowledge** — `reasoning/` rules consume the ontology
  and taxonomy but never define concepts of their own; a reasoning-produced
  finding (a gap, a flag, a score) is never modeled as an ontology entity (ADR-023,
  `Canonical_Ontology_Schema.md` §19).
- **Multi-agent readiness** — concept boundaries, the acyclic cross-domain
  dependency rule, and the frozen file contracts exist so that multiple AI systems
  (design, audit, implementation) and, eventually, multiple reasoning agents, can
  operate over the same knowledge graph without producing conflicting or
  duplicate definitions.
