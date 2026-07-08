# Support Delivery Domain

## Purpose

Governs how an approved intervention is physically delivered — vendor
relationships, delivery logistics, payment processing, and proof of delivery.
Entirely separate from registration: registration describes *what* is needed;
this domain describes *how* it is provided.

## Scope

**Level 2 placeholder.** Scope is declared; no taxonomy or ontology content is
authored until the domain activates (ADR-004, ADR-009).

## Owns (concepts this domain will own, per its placeholder declaration)

- `delivery_task`
- `vendor`
- `payment_instruction`
- `delivery_proof`
- `escrow` (if a financial mechanism is used)

## Does Not Own

- Support request *types* — what is needed (owned by
  `registration/taxonomy/support-interventions.yaml`). This domain owns only how
  an approved request is fulfilled.
- Case orchestration or approval workflow (owned by `case-management/`).

## Directory Structure

```
support-delivery/
└── _placeholder.yaml    # scope, owned concepts, activation condition
```

## Related Documents

- `_placeholder.yaml` — this domain's formal scope declaration
- `ARCHITECTURE.md` — Level 2 maturity definition
- `knowledge_layer_roadmap.md` — Stage 9 (activates once Case Management is
  active and an intervention approval workflow exists)
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy
