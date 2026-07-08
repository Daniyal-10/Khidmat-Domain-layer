# Programs Domain

## Purpose

Governs structured programs that group interventions under defined criteria —
targeting rules, eligibility, duration, funding constraints, and reporting
requirements — as distinct from ad-hoc, case-by-case assistance.

## Scope

**Level 2 placeholder.** Scope is declared; no taxonomy or ontology content is
authored until the domain activates (ADR-004, ADR-009).

## Owns (concepts this domain will own, per its placeholder declaration)

- `program_definition`
- `eligibility_criteria`
- `program_cycle`
- `beneficiary_enrollment_in_program`
- `program_budget`
- `program_reporting`

## Does Not Own

- Individual case assistance decisions (owned by `case-management/`).
- Intervention delivery mechanics (owned by `support-delivery/`).
- Outcome/impact measurement of a program's results (owned by `impact/`).

## Directory Structure

```
programs/
└── _placeholder.yaml    # scope, owned concepts, activation condition
```

## Related Documents

- `_placeholder.yaml` — this domain's formal scope declaration
- `ARCHITECTURE.md` — Level 2 maturity definition
- `knowledge_layer_roadmap.md` — Stage 9 (activates when a structured program
  distinct from ad-hoc assistance is defined by the client)
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy
