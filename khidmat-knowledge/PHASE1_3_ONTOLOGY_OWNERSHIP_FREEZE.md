# Phase 1.3 — Canonical Ontology Ownership Freeze

**Nature of this document:** governance only. No YAML was read for the purpose of modification,
and none was changed. Every entity and relationship cited below was re-extracted directly from
the committed, verified Phase 1 ontology (all 79 entities across every domain; all 51
cross-domain relationship edges) to ensure this freeze document is accurate rather than
restating prior claims.

---

## 1. Executive Summary

The Phase 1 ontology contains 79 declared entities across 15 files and 12 domains (14 Domain
Inventory bounded contexts, with Shared decomposed into Shared Core / Shared Human Model /
Shared Risk). Every entity has exactly one owning file with two exceptions, both already
governed by standing decisions rather than left ambiguous:

- **`case`** — genuinely duplicated (Case Management and Registration each declare it).
  Governed by `ADR_RECONCILIATION_CASE.md`, which determined ADR-021's single-canonical-Case
  model should stand; the duplication itself remains unresolved pending that reconciliation's
  own implementation, and is documented here as the sole open ownership question.
- **`Assessment` / `AssessmentFinding` / `IdentifiedNeed`** — the pre-canonical Needs Assessment
  monolith (`needs-assessment/ontology.yaml`) duplicates concepts now canonically owned by
  `needs-assessment/ontology/entities.yaml` (`assessment_session`, `need_assertion`,
  `finding_consensus`). Flagged as a genuine ownership violation in §7 — this was identified,
  not fixed, in the prior implementation pass, and is formally logged here rather than silently
  carried forward.

Every other entity, every relationship, every value object, and every identity concept has a
single, unambiguous owner with a consistent reference pattern. **The ownership model is
approvable for freeze conditional on both open items being logged as excluded, not silently
resolved by this document.**

---

## 2. Canonical Ownership Matrix

Grouped by owning domain. "Reference Domains" is derived from actual relationship targets found
in the committed ontology, not from aspiration.

### Shared Core (`shared/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `subject` | Beneficiary Lifecycle, Case Management | No — abstract parent, never instantiated directly | No | Yes |
| `person` | Registration, Needs Assessment, Community Context, Programs | No | No | Yes |
| `household` | Registration, Needs Assessment | No | No | Yes |
| `actor` | Case Management, Verification Operations, Needs Assessment, Volunteer Operations | Yes — via specialization (Volunteer Profile) | No | Yes |
| `organisation` | Community Context, Programs, Volunteer Operations, Case Management | No | No | Yes |
| `assessment_tool` | Needs Assessment (specialized by `assessment_instrument`) | Yes — via specialization | No | Yes |
| `humanitarian_sector` | None (forward-declared, currently unreferenced by any relationship) | Yes — via specialization, when a consuming domain activates | No | Yes |
| `intervention_type` | None (forward-declared, currently unreferenced by any relationship) | Yes — via specialization, when a consuming domain activates | No | Yes |

### Shared Human Model (`shared/human-model/ontology/family-structure.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `family` | Case Management | No | No | Yes |
| `family_member` | None yet (declared, not yet referenced by any relationship) | No | No | Yes |

### Shared Risk (`shared/risk/ontology/risk.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `risk` | None yet (declared, not yet referenced by any relationship) | No | No | Yes |
| `risk_characterization` | Beneficiary Lifecycle, Verification Operations | No | No | Yes |

### Registration (`registration/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `registrant` | Support Delivery | No | No | Yes |
| `beneficiary` | Support Delivery, Case Management (transitively, via Delivery) | No | No | Yes |
| `household_snapshot` | None cross-domain (Registration-internal; observes `shared:household`) | No | No | Yes |
| `household_member` | None cross-domain (Registration-internal) | No | No | Yes |
| `situation` | None cross-domain (Registration-internal) | No | No | Yes |
| `need` | None cross-domain (Registration-internal) | No | No | Yes |
| `claim` | Verification Operations, Needs Assessment | No | No | Yes |
| `evidence` | Verification Operations | No | No | Yes |
| `support_intervention` | None cross-domain (Registration-internal) | No | No | Yes |
| `case` | Beneficiary Lifecycle, Verification Operations | **No — see §7, open violation** | **No — see §7, open violation** | **Contested — see §7** |
| `lead` | None cross-domain | No | No | Yes |
| `volunteer_review` | None cross-domain | No | No | Yes |

### Case Management (`case-management/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `case` | Impact, Verification Operations, Support Delivery (×2) | **No — see §7, open violation** | **No — see §7, open violation** | **Contested — see §7** |
| `case_plan` | Support Delivery, Needs Assessment (via `case_plan_references_need_assertion`, reverse direction) | No | No | Yes |
| `referral` | None inbound cross-domain (Referral is the *from* side of its own outbound cross-domain edges to Organisation and Consent) | No | No | Yes |
| `follow_up` | None cross-domain | No | No | Yes |

### Verification Operations (`verification-operations/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `verification_subject` | None inbound cross-domain | No | No | Yes |
| `verification_activity` | Programs (`offering_verified_by`), Support Delivery (`observation_escalates_to_verification`) | No | No | Yes |
| `field_observation` | None inbound cross-domain | No | No | Yes |
| `verification_finding` | Beneficiary Lifecycle, Needs Assessment | No | No | Yes |
| `human_review` | None inbound cross-domain | No | No | Yes |
| `reverification_trigger` | None inbound cross-domain | No | No | Yes |
| `verification_assignment` | None inbound cross-domain | No | No | Yes |

### Needs Assessment

**Canonical (`needs-assessment/ontology/entities.yaml`):**

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `assessment_instrument` | None inbound cross-domain (specializes `shared:assessment_tool`) | No | No | Yes |
| `assessment_indicator` | None inbound cross-domain | No | No | Yes |
| `assessment_session` | Impact, Support Delivery | No | No | Yes |
| `observation` | None inbound cross-domain | No | No | Yes |
| `need_assertion` | Case Management | No | No | Yes |
| `finding_consensus` | None inbound cross-domain | No | No | Yes |
| `supervisor_review` | None inbound cross-domain | No | No | Yes |
| `assessor_calibration` | None inbound cross-domain | No | No | Yes |
| `reassessment_trigger` | None inbound cross-domain | No | No | Yes |

**Non-canonical (`needs-assessment/ontology.yaml`, legacy):**

| Concept | Status |
|---|---|
| `Assessment`, `AssessmentFinding`, `IdentifiedNeed` | **Not canonical — see §7, ownership violation.** Superseded in substance by `assessment_session`, `finding_consensus`/`verification_finding`, and `need_assertion` respectively, but not formally retired. |

### Beneficiary Lifecycle (`beneficiary-lifecycle/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `beneficiary_lifecycle` | None inbound cross-domain | No | No | Yes |
| `lifecycle_transition` | None inbound cross-domain | No | No | Yes |

### Community Context (`community-context/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `community` | None inbound cross-domain | No | No | Yes |
| `geographic_area` | Needs Assessment, Programs, Support Delivery | No | No | Yes |
| `built_infrastructure` | None inbound cross-domain | No | No | Yes |
| `natural_resource` | None inbound cross-domain | No | No | Yes |
| `transportation_network_asset` | None inbound cross-domain | No | No | Yes |
| `local_collective` | None inbound cross-domain | No | No | Yes |

### Volunteer Operations (`volunteer-operations/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `volunteer_profile` | Impact, Support Delivery | No | No | Yes |
| `volunteer_team` | None inbound cross-domain | No | No | Yes |

### Programs (`programs/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `program`, `program_version`, `program_variant`, `eligibility_rule`, `intervention_offering`, `enrollment`, `humanitarian_override`, `appeal`, `compliance_checkpoint` | None inbound cross-domain for any of these nine | No | No | Yes |

### Support Delivery (`support-delivery/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `delivery_event`, `delivery_window`, `delivery_attempt`, `proof_of_delivery`, `operational_observation`, `accountability_record`, `custody_transfer`, `community_representative`, `custodian` | None inbound cross-domain for any of these nine | No | No | Yes |

### Impact (`impact/ontology/entities.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `impact_evaluation`, `measurement` | None inbound cross-domain | No | No | Yes |

### Consent & Privacy (`consent-and-privacy/ontology.yaml`)

| Concept | Reference Domains | Extension Allowed? | Redefinition Allowed? | Canonical? |
|---|---|---|---|---|
| `consent` | Case Management | No | No | Yes (as a Phase 1 placeholder — Blueprint §16 marks the domain planned, not delivered; canonical within its declared boundary) |

---

## 3. Relationship Ownership Matrix

Every relationship is owned by the domain whose file declares it (the `from`-side domain, by
this repository's established convention — no relationship is declared jointly or by the
`to`-side domain). 51 cross-domain edges were found; all 51 have exactly one declaring file. No
relationship id is duplicated anywhere in the repository (verified in the prior implementation
pass and re-confirmed for this document).

| Owner Domain | Relationship | Allowed Reference | Illegal Ownership? | Duplicate Ownership? |
|---|---|---|---|---|
| Beneficiary Lifecycle | `beneficiary_lifecycle_tracks_journey_of_subject` | → `shared:subject` | No | No |
| Beneficiary Lifecycle | `lifecycle_transition_triggered_by_registration_case_case` (×2, incl. `..._case_decision_case`) | → `registration:case` | No — but targets the contested `case` id, see §7 | No |
| Beneficiary Lifecycle | `lifecycle_transition_triggered_by_verification_finding_verification_finding` | → `verification_operations:verification_finding` | No | No |
| Beneficiary Lifecycle | `lifecycle_transition_triggered_by_risk_characterization_risk_characterization` | → `shared_risk:risk_characterization` | No | No |
| Case Management | `case_informed_by_family` | → `shared_human_model:family` | No | No |
| Case Management | `follow_up_assigned_to_actor` | → `shared:actor` | No | No |
| Case Management | `referral_targets_organisation` | → `shared:organisation` | No | No |
| Case Management | `case_has_primary_subject` | → `shared:subject` | No | No |
| Case Management | `case_plan_references_need_assertion` | → `needs_assessment:need_assertion` | No | No |
| Case Management | `referral_references_consent` | → `consent_and_privacy:consent` | No | No |
| Case Management | `case_has_lead_coordinator`, `case_has_statutory_owner` | → `shared:actor` | No | No |
| Community Context | `built_infrastructure_operated_by_organization` | → `shared_org:organisation` | No | No |
| Community Context | `local_collective_composed_of_members` | → `shared_human:person` | No | No |
| Impact | `impact_evaluates_case` | → `case_management:case` | No | No |
| Impact | `measurement_baseline_derived_from` | → `needs_assessment:assessment_session` | No | No |
| Impact | `measurement_evaluated_by` | → `volunteer_operations:volunteer_profile` | No | No |
| Needs Assessment | `session_evaluates_person`, `session_conducted_by_person`, `calibration_audits_assessor` | → `shared:person` | No | No |
| Needs Assessment | `session_evaluates_household` | → `shared:household` | No | No |
| Needs Assessment | `session_evaluates_community`, (Programs' `variant_located_in`) | → `community_ctx:geographic_area` | No | No |
| Needs Assessment | `session_conducted_by_actor` | → `shared:actor` | No | No |
| Needs Assessment | `observation_based_on_claim` | → `registration:claim` | No | No |
| Needs Assessment | `need_assertion_based_on_verified_fact` | → `verification_operations:verification_finding` | No | No |
| Programs | `program_funded_by`, `program_implemented_by` | → `shared_org:organisation` | No | No |
| Programs | `program_managed_by`, `enrollment_for_beneficiary` | → `shared_human:person` | No | No |
| Programs | `enrollment_for_household` | → `shared_human:household` | No | No |
| Programs | `offering_verified_by` | → `verif_ops:verification_activity` | No | No |
| Registration | `beneficiary_observes_person` | → `shared:person` | No | No |
| Registration | `household_snapshot_observes_household` | → `shared:household` | No | No |
| Support Delivery | `delivery_fulfills_case_plan` | → `case_management:case_plan` | No | No |
| Support Delivery | `delivery_executed_by_agent` | → `volunteer_operations:volunteer_profile` | No | No |
| Support Delivery | `delivery_received_by_beneficiary` | → `registration:beneficiary` | No | No |
| Support Delivery | `delivery_received_by_proxy` | → `registration:registrant` | No | No |
| Support Delivery | `delivery_occurs_at_location` | → `community_context:geographic_area` | No | No |
| Support Delivery | `observation_escalates_to_assessment` | → `needs_assessment:assessment_session` | No | No |
| Support Delivery | `observation_escalates_to_case_management`, `accountability_escalates_to_case_management` | → `case_management:case` | No | No |
| Support Delivery | `observation_escalates_to_verification` | → `verification_operations:verification_activity` | No | No |
| Verification Operations | `verification_subject_derived_from_claim` | → `registration:claim` | No | No |
| Verification Operations | `field_observation_corroborated_by_evidence` | → `registration:evidence` | No | No |
| Verification Operations | `verification_assignment_verifies_case` | → `case_management:case` | No | No |
| Verification Operations | `verification_assignment_issued_from_brief_context_of_case` | → `registration:case` | No — but targets the contested `case` id, see §7 | No |
| Verification Operations | `verification_activity_conducted_by_actor`, `verification_assignment_assigned_to_actor`, `human_review_reviewed_by_actor` | → `shared:actor` | No | No |
| Verification Operations | `reverification_trigger_informed_by_risk_characterization` | → `shared_risk:risk_characterization` | No | No |
| Volunteer Operations | `volunteer_profile_profile_of_actor` | → `shared_core:actor` | No | No |
| Volunteer Operations | `volunteer_profile_affiliated_with_organisation` | → `shared_org:organisation` | No | No |

**No relationship was found to be illegally owned** (i.e., declared by a domain that does not
own its `from`-side entity) **and no relationship id is duplicated.** The only irregularity is
that two relationship owners (Beneficiary Lifecycle, Verification Operations) target the
contested `registration:case` id — this is a consequence of the open Case question in §7, not a
defect in the relationships themselves.

---

## 4. Aggregate Ownership Matrix

An aggregate root is an entity that owns child entities through a `has`-type relationship
within its own domain.

| Aggregate Root | Owner Domain | Child Entities Owned |
|---|---|---|
| `case` (Case Management sense) | Case Management | `case_plan`, `referral`, `follow_up` |
| `case` (Registration sense) | Registration | `registrant`, `beneficiary`, `household_snapshot`, `situation`, `need`, `claim`, `evidence`, `support_intervention` (all via `case_has_*`) — **contested, see §7** |
| `household_snapshot` | Registration | `household_member` |
| `need` | Registration | (no owned children; participates as child of `case`) |
| `assessment_session` | Needs Assessment | `observation` (via `session_yields_observation`) |
| `verification_activity` | Verification Operations | `field_observation` |
| `verification_finding` | Verification Operations | `human_review` |
| `verification_assignment` | Verification Operations | `verification_activity` |
| `community` | Community Context | none owned directly (peer relationships to `built_infrastructure`/`natural_resource`/`transportation_network_asset`/`local_collective`, not ownership) |
| `program` | Programs | `program_version`, `program_variant` |
| `program_version` | Programs | `eligibility_rule`, `intervention_offering` |
| `delivery_event` | Support Delivery | `delivery_window`, `delivery_attempt`, `accountability_record`, `custody_transfer` |
| `delivery_attempt` | Support Delivery | `proof_of_delivery`, `operational_observation` |
| `impact_evaluation` | Impact | `measurement` |
| `volunteer_profile` | Volunteer Operations | (no owned children; is itself owned indirectly by no one — a root) |
| `beneficiary_lifecycle` | Beneficiary Lifecycle | `lifecycle_transition` |
| `subject`, `person`, `household`, `actor`, `organisation` | Shared Core | none — these are referenced, not owned as children, by every consuming domain |
| `family` | Shared Human Model | `family_member` (per the domain's own prose model; not yet expressed as a canonical relationship, since only the `family`/`family_member` ids themselves were made addressable this Phase — the ownership relationship between them exists in prose, not yet as a declared `relationships:` row) |

No aggregate root was found with ambiguous ownership. The one aggregate-level irregularity is
the same Case duplication already logged in §7 — two aggregate roots currently share the id
`case` with different child sets.

---

## 5. Identity Ownership Matrix

Identity concepts are entities with a durable identifier (per the Phase 1.1A Canonical Semantic
Foundation) intended to persist and be recognized across cases/time, as distinct from
case-scoped snapshots.

| Identity Concept | Identifier Property | Owner Domain | Snapshot(s) That Observe It |
|---|---|---|---|
| `person` | `person_id` | Shared Core | Registration's `beneficiary` (via `beneficiary_observes_person`) |
| `household` | `household_id` | Shared Core | Registration's `household_snapshot` (via `household_snapshot_observes_household`) |
| `organisation` | `organisation_id` | Shared Core | None — referenced directly, not snapshotted, by Community Context, Programs, Volunteer Operations, Case Management |
| `case` (Case Management sense) | `case_id` (declared in Registration's entity; not yet independently declared for Case Management's `case`) | Case Management (per ADR-021's reconciled model) | N/A — **the identity question itself is what remains open, see §7** |
| `actor` | none declared (forward-declared placeholder; identity is inherited by specializations) | Shared Core | `volunteer_profile` (via `volunteer_profile_profile_of_actor`) |
| `family` | none declared (entity added this Phase without an explicit identifier property) | Shared Human Model | None yet |

**Observation:** `family` was made addressable this Phase but was not given an explicit
identifier property (e.g. `family_id`) the way Person, Household, and Organisation were in the
Phase 1.1A/1.2 passes. This is not a violation — no relationship currently requires resolving
"is this the same family as an earlier one," so no identifier was mandated — but it is worth
recording here as a known asymmetry in the identity model, should a future need for
family-level longitudinal tracking arise. Recording this observation is within this
governance phase's remit; adding the property would not be, and is not proposed here.

---

## 6. Cross-Domain Dependency Matrix

Derived directly from the 51 relationship edges in §3, collapsed to domain-pairs.

| Consuming Domain | Depends On | Via |
|---|---|---|
| Beneficiary Lifecycle | Shared Core, Registration, Verification Operations, Shared Risk | 5 relationships |
| Case Management | Shared Core, Shared Human Model, Needs Assessment, Consent & Privacy | 7 relationships |
| Community Context | Shared Core | 2 relationships |
| Impact | Case Management, Needs Assessment, Volunteer Operations | 3 relationships |
| Needs Assessment | Shared Core, Community Context, Registration, Verification Operations | 8 relationships |
| Programs | Shared Core, Community Context, Verification Operations | 7 relationships |
| Registration | Shared Core | 2 relationships |
| Support Delivery | Case Management, Volunteer Operations, Registration, Community Context, Needs Assessment, Verification Operations | 9 relationships |
| Verification Operations | Registration, Case Management, Shared Core, Shared Risk | 8 relationships |
| Volunteer Operations | Shared Core | 2 relationships |

**No circular dependency was found.** Tracing the graph: Shared Core sits at the root with zero
outbound dependencies; Registration, Community Context, Volunteer Operations depend only on
Shared Core; Needs Assessment and Verification Operations depend on Registration and each other
in one direction only (Needs Assessment → Verification Operations via
`need_assertion_based_on_verified_fact`, with no reverse edge); Case Management depends on
Needs Assessment and Shared Human Model; Beneficiary Lifecycle, Impact, Programs, and Support
Delivery sit downstream of Case Management and/or Verification Operations with no relationship
in the reverse direction found anywhere in the 51 edges reviewed.

**Every cross-domain dependency found is intentional** — each corresponds to a relationship
whose `notes:` field (where present) or business meaning was verified against the Blueprint in
prior passes. None was found to reference a concept its target domain does not own.

---

## 7. Ownership Violations

Two genuine violations, both already on record from prior passes and not newly discovered
here — this governance phase's contribution is formalizing them as ownership violations rather
than leaving them as implementation notes.

### Violation 1 — `case` duplicate ownership

`case-management/ontology/entities.yaml` and `registration/ontology/entities.yaml` both declare
an entity with `id: case`. Each has its own aggregate children (§4) and its own inbound
cross-domain relationships (§3: 4 relationships target `case_management:case`; 2 target
`registration:case`). This is a live violation of the single-ownership principle this freeze
phase exists to enforce.

**Status:** Not resolved by this document. `ADR_RECONCILIATION_CASE.md` (produced in a prior
governance pass) determined that ADR-021's single-canonical-Case model should stand over the
Phase 1.1A split proposal, but that determination's own implementation step — repointing
Beneficiary Lifecycle's two relationships to `case_management:case` and clarifying
Registration's `case` entity description — was never carried out. The duplication therefore
persists in the committed ontology exactly as it did before the reconciliation report was
written. **This is the one entity this ownership freeze cannot certify as having a single
owner.**

### Violation 2 — Needs Assessment legacy monolith

`needs-assessment/ontology.yaml` declares `Assessment`, `AssessmentFinding`, and `IdentifiedNeed`
as a non-canonical dict-shaped `entities:` block, parallel to and unretired alongside the
canonical `needs-assessment/ontology/entities.yaml`, which declares `assessment_session`,
`finding_consensus`/`need_assertion` as their canonical successors. No relationship in the
repository currently references the legacy monolith's ids, so this violation does not manifest
as a broken reference — but it is a duplicate, contradictory declaration of the same domain's
concepts under different names and different schemas, which is exactly the condition
single-ownership governance exists to prevent.

**Status:** Flagged, not resolved. Retiring the legacy files was identified as out of scope for
the ontology-completion implementation pass (it reads as repository cleanup); this governance
phase records it as a formal ownership violation so that its resolution is tracked as
governance debt rather than lost.

No other entity, relationship, aggregate, or identity concept reviewed in §§2–6 was found in
violation.

---

## 8. Recommended Authority Matrix Updates

The following are recommendations only, per instruction — nothing below has been applied to
`ontology_authority_matrix.md`.

1. **Add a row for `organisation`, `family`, `family_member`, `risk`, `risk_characterization`,
   and `follow_up`** to their respective domain sections, if not already present from the prior
   implementation pass's own authority-matrix updates (the prior pass added `organisation` and
   `follow_up`; `family`, `family_member`, `risk`, and `risk_characterization` were made
   addressable in the same pass but were not yet given their own authority-matrix rows).
2. **Add a row for `consent`** under a new "Consent & Privacy Domain" section (none currently
   exists in `ontology_authority_matrix.md`), reflecting its Phase 1 placeholder boundary.
3. **Update the existing FLAG entries** (the matrix's own "Flagged Boundary Cases" section) to
   add a new flag for the `case` duplicate — the matrix currently resolves FLAG-005 (Household)
   as closed but has no equivalent flag tracking the still-open Case duplication documented in
   §7 of this report.
4. **Add a new flag for the Needs Assessment legacy monolith** (§7, Violation 2), since no
   existing flag in the matrix currently tracks it.
5. **No change is recommended to any existing "must not be redefined" constraint** — every one
   reviewed in §2 remains correctly stated and was not found violated except by the two items
   already flagged.

---

## 9. Final Ownership Decision

# B.

## OWNERSHIP MODEL NOT APPROVED

The ownership model cannot be certified as permanently frozen while one entity (`case`) has two
live, differently-shaped owners with different aggregate children and different inbound
relationships, and one domain (Needs Assessment) has a formally undeclared duplicate
representation of three of its own concepts. Freezing ownership now would mean certifying, as
permanent governance, an entity whose owner this repository's own reconciliation report has
already found to be unresolved.

**Ownership conflicts preventing freeze:**

1. **`case`** — duplicate ownership between Case Management (`case-management/ontology/entities.yaml`)
   and Registration (`registration/ontology/entities.yaml`), each with distinct aggregate
   children and distinct inbound cross-domain relationships. Blocking until
   `ADR_RECONCILIATION_CASE.md`'s determination (ADR-021 stands) is actually implemented —
   specifically, Beneficiary Lifecycle's two relationships repointed from `registration:case` to
   `case_management:case`, and Registration's `case` entity description clarified as the
   pre-operational-phase view of the single canonical Case, per that report's own §4.

2. **`Assessment` / `AssessmentFinding` / `IdentifiedNeed`** — undeclared duplicate ownership
   between the legacy `needs-assessment/ontology.yaml` monolith and the canonical
   `needs-assessment/ontology/entities.yaml`. Blocking until the legacy monolith is formally
   retired or its concepts are explicitly reconciled with their canonical successors.

Every other entity, relationship, aggregate root, and identity concept in the Phase 1 ontology
— all 76 remaining entities and all 51 cross-domain relationships — has exactly one owner, no
illegal ownership, and no unintentional cross-domain dependency, and would be approvable for
freeze in isolation. The freeze is withheld in full rather than partially, since a "frozen
except for two named exceptions" state is not a stable governance posture — both items should
be resolved and this phase re-run for a clean approval.
