# ADR-018: Shared Subject Supertype

**Date**: 2026-06-29
**Status**: Accepted
**Context**: Foundation Remediation Sprint

## Context
The Beneficiary Lifecycle references `shared-human-model/Subject` to represent an entity that can undergo a lifecycle (either an individual person or a household). However, no such authoritative concept existed in the Shared Foundation. This produced an unresolved semantic reference, leading to potential inconsistency and domain confusion, as domains would otherwise invent their own abstractions for handling either a Person or a Household.

## Decision
We are introducing `Subject` as an authoritative Shared ontology concept in `shared/ontology/entities.yaml`. 
`Subject` represents the common abstraction for:
- `Person`
- `Household`

`Person` remains authoritative for individuals, and `Household` remains authoritative for households. 

## Consequences
- **Positive:** `Subject` becomes an ontology concept solely acting as the semantic parent, enabling domains to reason over either type safely and consistently.
- **Positive:** All domains can safely reference `Subject` without inventing their own abstraction.
- **Constraint:** `Subject` owns no demographic data. It exists solely as a structural and semantic parent.
