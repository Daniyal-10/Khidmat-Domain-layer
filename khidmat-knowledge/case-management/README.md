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
  `case_origin`, `case_outcome`, `administrative_closure_reason`
  (`taxonomy.yaml`)
- **Entities:** `Case`, `CasePlan`, `Referral`, `FollowUp`, `CaseAssignment`,
  `CaseNote` (`ontology.yaml`)
- **Relationships:** `has_case_plan`, `has_referral`, `has_follow_up`,
  `has_case_assignment`, `has_case_note`, `has_case_outcome`

## Does Not Own

- `Subject` — referenced from the Shared domain.
- `BeneficiaryLifecycle` — referenced from `beneficiary-lifecycle/`.
- `NeedsAssessment` output — referenced from `needs-assessment/`, not redefined.
- Intervention delivery mechanics (owned by the `support-delivery/` placeholder).
- Registration-time case data — the intake `Case` entity belongs to
  `registration/`.

## Directory Structure

```
case-management/
├── taxonomy.yaml     # case_status, priority_level, referral_status, ...
└── ontology.yaml      # Case, CasePlan, Referral, FollowUp, CaseAssignment, CaseNote
```

## Related Documents

- `ARCHITECTURE.md` — Stage 5 in the domain activation sequence
- `knowledge_layer_roadmap.md` — prerequisites (Risk Domain, Needs Assessment) and
  what this domain enables (Outcome Indicator Vocabulary, Stage 6)
- `ontology_authority_matrix.md` — Case Management concept ownership
- `consent-and-privacy/` — the minimal `Consent` placeholder this domain
  references
