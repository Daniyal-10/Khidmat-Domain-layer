# Registration Domain

## Purpose

Models a single intake conversation end-to-end — from first contact through to a
case being ready for field verification. This is the most mature domain in the
repository and the **canonical reference implementation**: the first domain
migrated onto the frozen `docs/architecture/Canonical_Ontology_Schema.md` and
`Canonical_Taxonomy_Schema.md` contracts (Phases 1–4 of
`docs/architecture/Registration_Migration_Plan.md` are complete; Phase 5
cross-domain CURIE linking remains blocked on a repository-wide manifest).

## Scope

Everything needed to conduct a registration conversation, detect information gaps,
classify needs and their severity, assess coherence, and determine when a case is
ready to hand off for verification. It does **not** cover what happens after
verification (case orchestration, intervention delivery, outcome tracking) — those
are owned by later domains.

## Owns

- **Entities:** Registrant, Beneficiary, Household, HouseholdMember, Situation,
  Need, Claim, Evidence, SupportIntervention, Case, Lead, VolunteerReview
  (`ontology/entities.yaml`)
- **Attributes / Value Objects:** all scalar and composite properties of the
  entities above, including the ADR-023 Value Objects (`contact_point`,
  `location`, `income`, `treatment_plan`, `cost_estimate`, `requested_amount`,
  `non_resident_guardian`), and `situation.protection_indicators_observed` —
  referencing the Risk Domain's `exploitation_and_coercion_indicators`
  vocabulary rather than authoring a parallel one (`ontology/data-properties.yaml`)
- **Relationships:** registrant↔case, case↔beneficiary/household/situation/need/
  claim/evidence/support-intervention, the `guardian_of` role relationship, and
  `need_influences_need` — a diagnosed relationship (contributes_to / blocks /
  compounds) between two confirmed needs in the same case
  (`ontology/relationships.yaml`)
- **Structural constraints:** e.g. age and household-size validation
  (`ontology/semantic-constraints.yaml`)
- **Taxonomy:** registrant/actor roles and claim basis, need categories and
  severity, situation triggers and trajectory, debt source and debt
  characteristic (elaborating the economic domain's unmanageable_debt
  indicator), claim types and quality dimensions, case outcomes, lead
  statuses, referral sources, evidence types, support intervention types
  (placeholder — see below)
- **Reasoning:** inference rules, severity rules, case-coherence rules,
  gap-detection rules, evidence rules (`reasoning/`)
- **Gaps:** the gap-type vocabulary and severity classification (`gaps/`)
- **Questioning:** conversational strategy and question templates (`questioning/`)
- **Readiness:** the conditions under which a case may transition to
  `ready_for_verification` (`readiness/`)
- **Verification projection:** the (non-stored) Verification Brief projection and
  verification requirement derivation logic (`verification/`)

## Does Not Own

- Person role *identities* (owned by `shared/taxonomy/persons.yaml` — registration
  only adds registration-specific epistemic detail: `default_claim_basis`,
  `questioning_note`, proxy sub-roles).
- Field verification activities, findings, or confidence (owned by
  `verification-operations/`).
- Case orchestration after registration closes — case plans, referrals, follow-ups
  (owned by `case-management/`).
- What Khidmat can actually deliver as assistance — `support-interventions.yaml`
  is a declared placeholder pending an operational intervention catalogue from
  programme staff (a genuine content gap, not a structural one).

## Directory Structure

```
registration/
├── ontology/
│   ├── entities.yaml               # Registrant, Beneficiary, Household, Need, Claim, ...
│   ├── data-properties.yaml        # scalar properties + Value Objects (ADR-023)
│   ├── relationships.yaml          # structural + role relationships
│   ├── semantic-constraints.yaml   # target-neutral structural constraints
│   └── lifecycle-constraints.yaml  # placeholder — no lifecycle semantics authored yet
├── taxonomy/                       # actors, needs, situations, claims, case-outcomes,
│                                   # lead-statuses, referral-sources, evidence,
│                                   # support-interventions (placeholder)
├── reasoning/                      # inference, severity, case-coherence,
│                                   # gap-detection, evidence rules
├── gaps/                           # gap-types.yaml
├── questioning/                    # questioning-strategy, question-templates
├── readiness/                      # readiness-rules.yaml
└── verification/                   # verification-brief-projection, verification-requirements
```

## Related Documents

- `docs/architecture/Registration_Migration_Plan.md` — the domain's own migration
  plan, decision table, and open Content Gap Log
- `docs/architecture/Registration_Domain_Audit.md` — structural conformance audit
- `docs/architecture/Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`
  — the contracts this domain conforms to
- `architecture-decisions/ADR-001` through `ADR-006` (Verification Brief,
  Situation/Need, Claim Quality, Placeholder Domains, Claim Basis, Safety Flag),
  and `ADR-023` (ontology vocabulary extension applied in this domain's Phase 4)
- `GLOSSARY.md` — Core Terms section defines most concepts owned here
