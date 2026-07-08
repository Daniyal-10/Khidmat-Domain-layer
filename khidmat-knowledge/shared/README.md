# Shared Domain

## Purpose

The single-ownership home for concepts used by two or more domains. Per ADR-008
(Single Ownership of Concepts) and ADR-007 (Shared Human Model as a First-Class
Knowledge Layer), a concept that multiple domains need must be defined exactly once,
here, rather than invented independently by each consumer.

## Scope

- Base person, organisation, location, document, and time vocabulary used across
  the whole repository.
- The **Shared Human Model** (`shared/human-model/`): lifecycle stages,
  capabilities, dependency relationships, family structure, and health conditions —
  the foundational representation of a human being that every domain reasoning
  about people, families, or households builds on.
- The **Risk Domain** (`shared/risk/`): hazard categories, exposure, vulnerability,
  protective factors, household resilience, and risk composition/characterization.

## Owns

- `subject`, `person`, `household`, `assessment_tool`, `humanitarian_sector`,
  `intervention_type`, `actor` (`shared/ontology/entities.yaml`)
- Person role labels, age classification, gender vocabulary
  (`shared/taxonomy/persons.yaml`)
- Organisation type vocabulary (`shared/taxonomy/organisations.yaml`)
- Location precision and stability vocabulary (`shared/taxonomy/locations.yaml`)
- Document type vocabulary (`shared/taxonomy/document-types.yaml`)
- Temporal vocabulary — duration bands, onset recency, recurrence patterns,
  temporal status, observation windows, evidence freshness
  (`shared/taxonomy/time.yaml`)
- Lifecycle stages, capabilities, dependency types, family structure, health
  conditions (`shared/human-model/`) — see its own README for detail
- Hazard categories, exposure, vulnerability, protective factors, household
  resilience, risk composition/characterization/profile
  (`shared/risk/`) — see its own README for detail

## Does Not Own

- Domain-specific detail built on top of these base concepts (e.g. registration's
  actor epistemic detail in `registration/taxonomy/actors.yaml` extends, but does
  not redefine, `shared/taxonomy/persons.yaml`'s role labels).
- Intervention recommendations or case orchestration (Case Management, Support
  Delivery).
- A fully-populated, cross-domain **persistent** Person entity — `person` is
  declared in `shared/ontology/entities.yaml` but is a bare label today; see
  `ontology_completion_checklist.md`.

> **Note:** `household` is currently declared independently in both
> `shared/ontology/entities.yaml` and `registration/ontology/entities.yaml`. This
> is a flagged, unresolved single-ownership question (see `ontology_authority_matrix.md`,
> FLAG-005) — not a documentation error, but worth knowing before treating either
> definition as sole-authoritative.

## Directory Structure

```
shared/
├── taxonomy/            # persons, organisations, locations, document-types, time
├── ontology/             # entities, data-properties, relationships, constraints
├── vocabulary/           # controlled-terms.yaml (placeholder)
├── human-model/          # Shared Human Model — see shared/human-model/README.md
│   ├── taxonomy/         # lifecycle-stages, capabilities, dependency, health-conditions
│   └── ontology/         # family-structure
└── risk/                 # Risk Domain — see shared/risk/README.md
    ├── taxonomy/         # hazard-categories, protective-factors
    ├── ontology/          # exposure, vulnerability, household-resilience, risk
    └── reasoning/         # compound-risk-detection
```

## Related Documents

- `ARCHITECTURE.md` — dependency rules, Shared Human Model declaration
- `ontology_authority_matrix.md` — concept ownership registry (including FLAG-005)
- `ontology_completion_checklist.md` — what's complete vs. missing in this domain
- `shared/human-model/README.md`, `shared/human-model/governance.md`
- `shared/risk/README.md`, `shared/risk/governance.md`
- ADR-007 (Shared Human Model), ADR-008 (Single Ownership), ADR-010–ADR-014 (Risk Domain), ADR-018 (Shared Subject Supertype)
