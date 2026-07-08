# Impact Domain

## Purpose

Governs measurement of outcomes — whether interventions produced the intended
change in a beneficiary's situation. Requires longitudinal data from Beneficiary
Lifecycle to compare before/after states.

## Scope

**Level 2 placeholder.** Scope is declared; no taxonomy or ontology content is
authored until the domain activates (ADR-004, ADR-009).

## Owns (concepts this domain will own, per its placeholder declaration)

- `outcome_indicator`
- `measurement_event`
- `baseline` (pre-intervention state)
- `endline` (post-intervention state)
- `change_assessment`

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
└── _placeholder.yaml    # scope, owned concepts, activation condition
```

## Related Documents

- `_placeholder.yaml` — this domain's formal scope declaration
- `ARCHITECTURE.md` — Level 2 maturity definition
- `knowledge_layer_roadmap.md` — Stage 6 (Outcome Indicator Vocabulary,
  prerequisite) and Stage 9 (this domain's activation)
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy
