# Case Management Domain

## Purpose

Orchestrates the ongoing coordination of support for a Subject once a case has
moved beyond intake and verification: the case's operational lifecycle, its plan,
referrals, follow-ups, assignments, and notes.

## Scope

The `Case` as a long-lived operational container, from opening through planning,
active coordination, and closure. Distinct from the per-conversation `Case` record
`registration/` produces at intake — this domain's `Case` is the durable
coordination record that persists across referrals and follow-ups.

## Owns

- **Taxonomy:** `case_status`, `priority_level`, `referral_status`,
  `case_origin`, `closure_reason`, `case_plan_status`, `delegation_status`,
  `objective_status`, `referral_type`, `suspension_reason`
  (`taxonomy/`)
- **Entities:** `case`, `case_plan`, `referral`; `follow_up` and `case_note`
  are nested Value Object fields on `case` (`ontology/`)
- **Relationships:** `case_has_case_plan`, `case_has_referral`,
  `case_superseded_by_case`, `case_has_primary_subject`,
  `case_plan_references_need_assertion`, `case_plan_addressed_by_intervention`
  (added Stage 7B — links to `registration:support_intervention`, closing the
  Case Plan → Intervention lifecycle gap), `referral_references_consent`,
  `case_has_lead_coordinator`, `case_has_statutory_owner`

## Does Not Own

- `Subject` — referenced from the Shared domain.
- `BeneficiaryLifecycle` — referenced from `beneficiary-lifecycle/`.
- `NeedsAssessment` output — referenced from `needs-assessment/`, not redefined.
- Intervention delivery mechanics (owned by `support-delivery/`).
- Registration-time case data — the intake `Case` entity belongs to
  `registration/`.

## Directory Structure

```
case-management/
├── taxonomy/     # case_status, priority_level, referral_status, ...
└── ontology/     # case, case_plan, referral, and their data properties/relationships
```

## Related Documents

- `ARCHITECTURE.md` — Stage 5 in the domain activation sequence
- `knowledge_layer_roadmap.md` — prerequisites (Risk Domain, Needs Assessment) and
  what this domain enables (Outcome Indicator Vocabulary, Stage 6)
- `ontology_authority_matrix.md` — Case Management concept ownership
- `consent-and-privacy/` — the minimal `Consent` placeholder this domain
  references
