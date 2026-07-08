# Khidmat Knowledge Architecture

## Table of Contents

- [Current Active Phase](#current-active-phase)
- [Domain Inventory](#domain-inventory)
- [Knowledge Governance Files](#knowledge-governance-files)
- [Dependency Rules](#dependency-rules)
- [Shared Human Model](#shared-human-model)
- [Maturity Levels](#maturity-levels)
- [Future Domain Layers](#future-domain-layers)

---

## Current Active Phase

Repository Architecture Freeze — Canonical Ontology & Taxonomy Migration (Active / In Progress)

Status:

- Risk Domain complete (including core ontology and compound risk detection reasoning).
- Verification Operations core ontology and reasoning complete.
- Needs Assessment, Case Management, and Beneficiary Lifecycle domains complete (Level 1).
- The canonical `ontology/`+`taxonomy/` authoring contract has been frozen
  (`docs/architecture/Canonical_Ontology_Schema.md`, `docs/architecture/Canonical_Taxonomy_Schema.md`)
  and ADR-023 extends it with Value Objects, Roles, and Runtime/Reasoning Objects.
- Registration is the first domain migrated to the canonical structure
  (Phases 1–4 complete per `docs/architecture/Registration_Migration_Plan.md`; Phase 5
  cross-domain CURIE linking remains blocked on a repository-wide manifest).
- Community Context is substantially built (12 taxonomy files, full ontology module)
  but not yet migrated to the canonical structure.

## Domain Inventory

| Domain                  | Maturity       | Status               |
|-------------------------|----------------|----------------------|
| shared                  | Level 1        | Active               |
| shared/risk             | Level 1        | Complete             |
| registration            | Level 1        | Complete — canonical reference implementation |
| community-context       | Level 1 (pre-canonical) | Active / In Progress |
| verification-operations | Level 1        | Complete             |
| needs-assessment        | Level 1        | Complete             |
| case-management         | Level 1        | Complete             |
| beneficiary-lifecycle   | Level 1        | Complete             |
| consent-and-privacy     | Level 2   | Placeholder         |
| volunteer-operations    | Level 2   | Placeholder         |
| support-delivery        | Level 2   | Placeholder         |
| programs                | Level 2   | Placeholder         |
| impact                  | Level 2   | Placeholder         |

## Knowledge Governance Files

The following governance files are authoritative references for the knowledge layer:

* knowledge_layer_inventory.md
* ontology_authority_matrix.md
* ontology_completion_checklist.md
* knowledge_layer_roadmap.md
* architecture-decisions/ (Directory containing formal Architecture Decision Records)

Purpose:

* Inventory tracks what exists.
* Authority Matrix tracks concept ownership.
* Completion Checklist tracks progress.
* Roadmap tracks dependency order and activation sequencing.

All ontology work must remain consistent with these files.

## Dependency Rules

To maintain long-term ontological stability, single-source-of-truth knowledge graph normalization, and clear bounded context boundaries, the following rules govern cross-domain relationships:

- **Semantic Reference:** Domains may freely establish semantic references (via `*_ref` pointers in RDF/OWL equivalent property paths) to ontology concepts natively owned by other bounded contexts when required for cross-domain business logic.
- **Reference-Not-Redefine:** Consuming domains must *never* redefine, overload, or create competing taxonomy/ontology definitions for concepts owned elsewhere. Natively owned concepts remain canonical.
- **Concept Ownership:** Semantic referencing never transfers concept ownership. Canonical ownership always remains strictly with the originating bounded context as dictated by ADR-008 and `ontology_authority_matrix.md`.
- **Acyclic Dependencies:** Circular semantic dependencies between bounded contexts are strictly prohibited. The knowledge graph must form a Directed Acyclic Graph (DAG) across domain boundaries.
- **Shared Promotion Constraint:** Concepts must only be promoted to the `shared/` bounded context through an explicit architectural governance decision (e.g., an ADR). A concept is not promoted merely because multiple downstream domains happen to reference it.

## Shared Human Model

The Shared Human Model is the foundational layer for future humanitarian reasoning.

Location:

    shared/human-model/

Completed files:

* lifecycle-stages.yaml
* capabilities.yaml
* dependency.yaml
* family-structure.yaml
* health-conditions.yaml

The Shared Human Model owns:

* lifecycle concepts
* capability concepts
* dependency concepts
* family relationship concepts
* health condition concepts

No future domain may redefine these concepts.

These concepts have been promoted to shared ownership.

## Maturity Levels

Level 1: Taxonomy, ontology, reasoning, and questioning are fully defined
         and production-ready. Files are complete.

Level 2: Folder exists. README declares scope.
         Placeholder file lists concepts the domain will eventually own.
         No taxonomy or ontology is invented until the domain enters active development.

## Future Domain Layers

Completed foundational layer:

* Shared Human Model
* Risk Domain
* Needs Assessment Domain
* Verification Operations Domain
* Case Management Domain
* Beneficiary Lifecycle Domain

Upcoming layers:

* Community Context Domain (built, pending canonical migration)
* Outcome Measurement Layer
* Level 2 placeholder domains (Volunteer Operations, Support Delivery, Programs, Impact, Consent & Privacy)

These layers must activate according to knowledge_layer_roadmap.md dependencies.