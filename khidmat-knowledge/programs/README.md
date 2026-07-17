# Programs Domain

## Purpose

Governs structured programs that group interventions under defined criteria —
targeting rules, eligibility, duration, funding constraints, and reporting
requirements — as distinct from ad-hoc, case-by-case assistance.

## Scope

**Canonical — complete.** Full `ontology/`+`taxonomy/` structure authored per
`docs/architecture/Canonical_Ontology_Schema.md` / `Canonical_Taxonomy_Schema.md`.

## Owns

- **Entities:** `program`, `program_version`, `program_variant`, `eligibility_rule`,
  `intervention_offering`, `enrollment`, `humanitarian_override`, `appeal`,
  `compliance_checkpoint` (`ontology/entities.yaml`)
- **Taxonomy:** eligibility, enrollment status, and intervention readiness
  (`eligibility-and-enrollment.yaml`), funding sources and compliance
  (`funding-and-compliance.yaml`), override/appeal governance
  (`governance-and-exceptions.yaml`), intervention modalities and objective
  categories (`interventions.yaml`), program lifecycle and status
  (`lifecycle-and-status.yaml`), program topology and thematic sectors
  (`structure.yaml`)
- **Relationships (added Stage 6):** `offering_prerequisite_for`,
  `offering_mutually_exclusive_with`, `offering_reinforces`,
  `offering_substitutes_for` — intervention-offering-level counterparts to the
  existing program-level `program_prerequisite_for` /
  `program_mutually_exclusive_with` (`ontology/relationships.yaml`)

## Does Not Own

- Individual case assistance decisions (owned by `case-management/`).
- Intervention delivery mechanics (owned by `support-delivery/`).
- Outcome/impact measurement of a program's results (owned by `impact/`).

## Directory Structure

```
programs/
├── ontology/     # entities, data-properties, relationships, constraints
└── taxonomy/     # eligibility-and-enrollment, funding-and-compliance,
                  # governance-and-exceptions, interventions, lifecycle-and-status, structure
```

## Related Documents

- `ARCHITECTURE.md` — domain maturity and inventory
- `knowledge_layer_roadmap.md` — dependency order and activation sequencing
- `ontology_authority_matrix.md` — Programs concept ownership
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy (historical — domain
  has since been migrated to canonical structure)
