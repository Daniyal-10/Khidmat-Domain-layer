# Support Delivery Domain

## Purpose

Governs how an approved intervention is physically delivered — bridging the gap between an approved, abstract Case Plan and the real-world handover to a vulnerable human being. It models the logistics, constraints, attempts, proofs, and accountability loops required to safely, fairly, and securely execute assistance.

## Scope

This domain is structurally active. It models the execution of assistance.

## Owns

- `delivery_event`
- `delivery_window`
- `delivery_attempt`
- `proof_of_delivery`
- `custody_transfer`
- `accountability_record`
- `operational_observation`
- `community_representative`
- `custodian`

## Does Not Own

- Support request *types* — what is needed (owned by Registration/Needs Assessment).
- Case orchestration or approval workflow (owned by Case Management).
- Volunteer matching (owned by Volunteer Operations).

## Directory Structure

```
support-delivery/
├── ontology/
└── taxonomy/
```
