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
between stages — the beneficiary's *administrative* relationship to Khidmat.

Also owns, as a strictly independent axis (added Stage 6), the beneficiary's or
household's own *humanitarian developmental* trajectory (crisis →
stabilization → recovery → self_reliance → resilience →
community_contribution — `human_development_stage`). This is never to be
merged with, collapsed into, or used as a proxy for engagement_stage: a
beneficiary's administrative status and their developmental stage are
independent facts that can diverge in either direction (e.g. `engaged` while
still at `crisis`, or `exited` while at `resilience`). See
`taxonomy/engagement-stage.yaml`'s design note for the full distinction.

## Owns

- **Taxonomy:** `engagement_stage`, `human_development_stage`, `exit_reason`,
  `suspension_reason`, `review_trigger` (in `taxonomy/`)
- **Entities:** `beneficiary_lifecycle`, `lifecycle_transition` (in `ontology/`)
- **Relationships:** `tracks_journey_of`, `has_transition_history`, `followed_by`, `triggered_by_registration_case`, `triggered_by_verification_finding`, `triggered_by_risk_characterization`, `triggered_by_case_decision`, `triggered_by_impact_evaluation` (added Stage 7B, closing the Impact → Beneficiary Lifecycle gap), `part_of_lifecycle`

## Does Not Own

- The per-case Beneficiary entity produced at intake (owned by `registration/`).
- Risk assessment itself (owned by `shared/risk/` — this domain only reacts to a risk assessment as a transition trigger).
- Case orchestration (owned by `case-management/`).
- A persistent, identity-resolved Person record spanning domains — this domain tracks *stage*, not identity.

## Directory Structure

```
beneficiary-lifecycle/
├── taxonomy/                                   # engagement-stage.yaml (incl. per-stage semantics), exit-reasons.yaml, ...
└── ontology/                                   # entities.yaml, data-properties.yaml, ...
```

## Related Documents

- `ARCHITECTURE.md` — Stage 7 in the domain activation sequence
- `knowledge_layer_roadmap.md` — prerequisites and enabled domains
- `ontology_authority_matrix.md` — concept ownership
