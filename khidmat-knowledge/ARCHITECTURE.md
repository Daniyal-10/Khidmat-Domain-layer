# Khidmat Knowledge Architecture

## Current Active Phase

Stage 3 — Risk Domain

Status:

- Shared Human Model complete
- Risk Domain architecture review pending Human Owner approval
- No Risk Domain ontology implementation approved

## Domain Inventory

| Domain                  | Maturity  | Status              |
|-------------------------|-----------|---------------------|
| shared                  | Level 1   | Active              |
| registration            | Level 1   | Active              |
| verification-operations | Level 2   | Placeholder         |
| case-management         | Level 2   | Placeholder         |
| beneficiary-lifecycle   | Level 2   | Placeholder         |
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

Purpose:

* Inventory tracks what exists.
* Authority Matrix tracks concept ownership.
* Completion Checklist tracks progress.
* Roadmap tracks dependency order and activation sequencing.

All ontology work must remain consistent with these files.

## Dependency Rules

- registration/ may import from shared/
- No other domain may import from registration/
- Future domains may import from shared/
- No circular dependencies permitted
- Concepts shared between two or more domains must be promoted to shared/

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

Upcoming layers:

* Risk Domain (Current Active Target)
* Community Context Domain
* Outcome Measurement Layer

These layers must activate according to knowledge_layer_roadmap.md dependencies.