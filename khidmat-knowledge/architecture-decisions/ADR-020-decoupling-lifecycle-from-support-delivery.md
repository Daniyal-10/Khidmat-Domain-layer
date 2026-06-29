# ADR-020: Decoupling Lifecycle Progression from Support Delivery

**Date**: 2026-06-29
**Status**: Accepted
**Context**: Phase 3 Humanitarian Semantics Review

## Context
The `engagement_stage` taxonomy previously contained a `receiving_support` stage. This created an overlap with the Support Delivery domain, which should be the authoritative owner of what support is being delivered, when, and how. 

## Decision
We are replacing the `receiving_support` stage with `engaged` in the `engagement_stage` taxonomy.

## Rationale
Coupling the macro-level lifecycle progression directly to operational delivery ("receiving support") violates domain boundaries. A beneficiary's lifecycle state should reflect their standing in the ecosystem (e.g., they are `engaged` in a program). The actual mechanism of receiving support belongs to Support Delivery. By using `engaged`, the lifecycle maintains a neutral humanitarian state that reflects formal admission into the ecosystem's programs without usurping the operational details of aid delivery.

## Consequences
- The Beneficiary Lifecycle remains decoupled from Support Delivery mechanics.
- Support Delivery is solely authoritative for tracking active distributions, interventions, and aid receipt.
- `engaged` provides a stable, neutral lifecycle state during the intervention phase.
