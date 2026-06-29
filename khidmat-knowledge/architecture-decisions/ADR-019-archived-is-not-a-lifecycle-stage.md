# ADR-019: Removal of Archived as a Lifecycle Stage

**Date**: 2026-06-29
**Status**: Accepted
**Context**: Phase 3 Humanitarian Semantics Review

## Context
The `engagement_stage` taxonomy for the Beneficiary Lifecycle previously included an `archived` stage, defined as a "long-term historical record". 

## Decision
We are removing `archived` from the `engagement_stage` taxonomy.

## Rationale
"Archived" is a data retention, software implementation, or governance concept. It does not represent a humanitarian state or a phase in a beneficiary's journey. The humanitarian relationship ends at `exited`. What the software system does with the `exited` record after a retention period (i.e., archiving it) is outside the scope of the semantic Beneficiary Lifecycle.

## Consequences
- The lifecycle cleanly ends at `exited`.
- Data retention policies must track system-level metadata (e.g., `retention_status`) rather than manipulating the semantic lifecycle stage.
