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

- **Taxonomy:** `engagement_stage`, `exit_reason`, `suspension_reason`,
  `review_trigger` (`taxonomy.yaml`)
- **Entities:** `BeneficiaryLifecycle`, `LifecycleTransition` (`ontology.yaml`)
- **Relationships:** `tracksJourneyOf`, `hasTransitionHistory`, `followedBy`,
  `triggeredByRegistrationCompletion`, `triggeredByVerificationOutcome`,
  `triggeredByRiskAssessment`, `triggeredByCaseDecision`

## Does Not Own

- The per-case Beneficiary entity produced at intake (owned by `registration/`).
- Risk assessment itself (owned by `shared/risk/` — this domain only reacts to a
  risk assessment as a transition trigger).
- Case orchestration (owned by `case-management/`).
- A persistent, identity-resolved Person record spanning domains — this domain
  tracks *stage*, not identity; see `ontology_completion_checklist.md`'s Person
  Entity item.

> **Note:** a `_placeholder.yaml` from this domain's earlier Level-2 placeholder
> phase still exists alongside its now-complete `taxonomy.yaml`/`ontology.yaml`.
> The taxonomy and ontology files are the current, active, Level 1 definition of
> this domain; the placeholder file is a superseded artifact, not a second source
> of truth.

## Directory Structure

```
beneficiary-lifecycle/
├── taxonomy.yaml                              # engagement_stage, exit_reason, ...
├── ontology.yaml                               # BeneficiaryLifecycle, LifecycleTransition
├── engagement-stage-semantics.md               # stage-by-stage semantic detail
├── transition_semantics_recommendations.md     # transition-rule recommendations
└── _placeholder.yaml                           # superseded pre-activation scope note
```

## Related Documents

- `ARCHITECTURE.md` — Stage 7 in the domain activation sequence
- `knowledge_layer_roadmap.md` — prerequisites (Shared Human Model, Outcome
  Indicator Vocabulary) and what this domain enables (Impact, Community Context)
- `ontology_authority_matrix.md` — Beneficiary Lifecycle concept ownership
