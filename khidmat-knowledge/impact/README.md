# Impact Domain

## Purpose

Governs measurement of outcomes — whether interventions produced the intended
change in a beneficiary's situation. Requires longitudinal data from Beneficiary
Lifecycle to compare before/after states.

## Scope

**Canonical — complete.** Full `ontology/`+`taxonomy/` structure authored per
`docs/architecture/Canonical_Ontology_Schema.md` / `Canonical_Taxonomy_Schema.md`.

## Owns

- **Entities:** `impact_evaluation`, `measurement` (`ontology/entities.yaml`)
- **Relationships (Stage 7B):** `impact_evaluation` can now inform a
  `beneficiary_lifecycle:lifecycle_transition` via that domain's own
  `triggered_by_impact_evaluation` relationship (owned and defined in
  `beneficiary-lifecycle/ontology/relationships.yaml`, not here) — closing
  the previously missing Impact → Beneficiary Lifecycle link without this
  domain gaining any ability to set `engagement_stage` or
  `human_development_stage` directly.
- **Taxonomy:** attribution and contribution (`attribution.yaml`), evaluation
  lifecycle and findings (`evaluation.yaml`), indicator categories and hierarchy
  (`indicators.yaml`), measurement classification, timing, and confidence
  (`measurement.yaml`), outcome type, persistence, and decay (`outcomes.yaml`)

## Does Not Own

- The Beneficiary Lifecycle stage machinery itself (owned by
  `beneficiary-lifecycle/`) — this domain measures change *using* that
  longitudinal record, it doesn't own the record.
- Program-level targeting or budget (owned by `programs/`).
- The shared Outcome Indicator vocabulary once it exists — per
  `knowledge_layer_roadmap.md` Stage 6, that vocabulary is co-designed across
  case management, programs, and impact and lives in `shared/vocabulary/`, not
  solely here.

## Directory Structure

```
impact/
├── ontology/     # entities, data-properties, relationships, constraints
└── taxonomy/     # attribution, evaluation, indicators, measurement, outcomes
```

## Related Documents

- `ARCHITECTURE.md` — domain maturity and inventory
- `knowledge_layer_roadmap.md` — Stage 6 (Outcome Indicator Vocabulary,
  prerequisite) and Stage 9 context
- `ontology_authority_matrix.md` — Impact concept ownership
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy (historical — domain
  has since been migrated to canonical structure)
