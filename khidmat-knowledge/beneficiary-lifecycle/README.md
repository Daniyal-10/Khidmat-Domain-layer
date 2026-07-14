# Beneficiary Lifecycle Domain

## Purpose

Tracks the macro-state of a beneficiary's engagement with Khidmat across multiple
registrations, interventions, and time periods — the persistent journey, not any
single case. Answers "where is this person/household in their journey" and
records how they got there.

## Scope

The engagement-stage state machine (identified → registration_initiated →
registered → verification_pending → active → engaged → monitored → ...), exit and
suspension reasons, review triggers, and the event-sourced transition history
between stages.

## Owns

- **Taxonomy:** `engagement_stage`, `exit_reason`, `suspension_reason`, `review_trigger` (in `taxonomy/`)
- **Entities:** `beneficiary_lifecycle`, `lifecycle_transition` (in `ontology/`)
- **Relationships:** `tracks_journey_of`, `has_transition_history`, `followed_by`, `triggered_by_registration_completion`, `triggered_by_verification_outcome`, `triggered_by_risk_assessment`, `triggered_by_case_decision`

## Does Not Own

- The per-case Beneficiary entity produced at intake (owned by `registration/`).
- Risk assessment itself (owned by `shared/risk/` — this domain only reacts to a risk assessment as a transition trigger).
- Case orchestration (owned by `case-management/`).
- A persistent, identity-resolved Person record spanning domains — this domain tracks *stage*, not identity.

## Directory Structure

```
beneficiary-lifecycle/
├── taxonomy/                                   # engagement-stage.yaml, exit-reasons.yaml, ...
├── ontology/                                   # entities.yaml, data-properties.yaml, ...
├── engagement-stage-semantics.md               # stage-by-stage semantic detail
└── transition_semantics_recommendations.md     # transition-rule recommendations
```

## Related Documents

- `ARCHITECTURE.md` — Stage 7 in the domain activation sequence
- `knowledge_layer_roadmap.md` — prerequisites and enabled domains
- `ontology_authority_matrix.md` — concept ownership
