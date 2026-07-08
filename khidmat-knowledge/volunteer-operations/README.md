# Volunteer Operations Domain

## Purpose

Governs volunteer identity, capacity, assignment, routing, performance, and trust.
Entirely separate from the registration domain — a volunteer appears in
registration only as a `registrant_type`; their full profile lives here.

## Scope

**Level 2 placeholder.** Scope is declared; no taxonomy or ontology content is
authored until the domain activates (ADR-004, ADR-009).

## Owns (concepts this domain will own, per its placeholder declaration)

- `volunteer_profile`
- `volunteer_availability`
- `volunteer_geographic_coverage`
- `volunteer_trust_score`
- `volunteer_assignment_history`
- `volunteer_training_status`

## Does Not Own

- The registrant-role label `volunteer` itself (owned by
  `shared/taxonomy/persons.yaml`; this domain owns the full profile behind that
  role, not the role label).
- Anything in registration, verification, or case management.

## Directory Structure

```
volunteer-operations/
└── _placeholder.yaml    # scope, owned concepts, activation condition
```

## Related Documents

- `_placeholder.yaml` — this domain's formal scope declaration
- `ARCHITECTURE.md` — Level 2 maturity definition
- `knowledge_layer_roadmap.md` — Stage 9 (activates when a volunteer management
  workflow is defined with operations staff)
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy
