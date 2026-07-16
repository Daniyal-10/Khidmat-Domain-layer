# Khidmat Knowledge Layer — Ontology Authority Matrix

**Authority:** Knowledge Layer Architect
**Governing ADR:** ADR-008: Single Ownership of Concepts (See `architecture-decisions/` directory for full ADR texts)
**Purpose:** Declares the authoritative owner for every concept in the
knowledge layer. This is the governance record of concept ownership.

---

## How to Use This Matrix

**Defining vs. referencing:**
A concept may be referenced by many files but may only be defined by one
owner. The owner file is listed in the `Authoritative File` column. All
other files that use the concept must reference it — they must not
redefine it.

**Adding a new concept:**
When a new concept is introduced to the knowledge layer, its owner must be
declared in this matrix before or at the time the concept is written.
No concept may be used in a reasoning rule if its ownership is undeclared.

**Changing ownership:**
If a concept is promoted from a domain file to shared ownership, the
`Authoritative File` and `Owner Domain` columns must be updated. The
change must be accompanied by a new ADR if it affects an established
design decision.

**Flagged boundary cases:**
Concepts with known overlap risks or pending alignment requirements are
listed separately in the Flagged Boundary Cases section at the end of
this file.

---

## Shared Ontology

**Owner domain:** Shared Ontology
**Introduced:** Phase 1 (Foundation Remediation Sprint)
**Governing ADRs:** ADR-018

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `subject` | Subject | `shared/ontology/entities.yaml` | Shared Ontology | Semantic parent for Person/Household. Owns no demographic data. Must not be redefined. |
| `person` | Person | `shared/ontology/entities.yaml` | Shared Ontology | Authoritative concept for individuals. Must not be redefined. |
| `household` | Household | `shared/ontology/entities.yaml` | Shared Ontology | Authoritative concept for households. Must not be redefined. |
| `assessment_tool` | AssessmentTool | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for Needs Assessment — resolved via `needs_assessment:assessment_instrument` (`parent: shared:assessment_tool`). Must not be redefined. |
| `humanitarian_sector` | HumanitarianSector | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for Needs Assessment. Still unresolved: `needs_assessment:thematic_sector` currently sources its vocabulary from `programs_tax:thematic_sectors` instead. Reassignment to this placeholder is pending a Shared-promotion ADR (see `needs-assessment/Needs_Assessment_Canonical_Migration_Plan.md` §10.1) — not implemented. Must not be redefined. |
| `intervention_type` | InterventionType | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for Case Management. Must not be redefined. |
| `actor` | Actor | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for an operational participant. Must not be redefined. |
| `organisation` | Organisation | `shared/ontology/entities.yaml` | Shared Ontology | Introduced per the Phase 1.1A Canonical Semantic Foundation. Authoritative concept for any government body, NGO, institution, or partner that funds, implements, operates infrastructure for, affiliates volunteers with, or receives a Referral. Referenced by Community Context (`built_infrastructure_operated_by_organization`), Programs (`program_funded_by`, `program_implemented_by`), Volunteer Operations (`volunteer_profile_affiliated_with_organisation`), and Case Management (`referral_targets_organisation`). Distinct from `shared/taxonomy/organisations.yaml`, which classifies organisation *types* and remains a separate, non-conflicting scheme. Must not be redefined. |

---

## Shared Human Model

### Lifecycle Stage Concepts

**Authoritative file:** `shared/human-model/taxonomy/lifecycle-stages.yaml`
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-007, ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `infant` | Infant | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `toddler` | Toddler | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `early_childhood` | Early Childhood | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `school_age_child` | School-Age Child | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `adolescent` | Adolescent | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `young_adult` | Young Adult | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `adult` | Adult | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `older_adult` | Older Adult | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `elderly` | Elderly | `shared/human-model/taxonomy/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

**What these concepts cover:**
Each lifecycle stage concept owns its complete definition including:
stage boundaries, characteristic dependencies, characteristic capabilities,
characteristic vulnerabilities, reasoning implications, and ontology notes.

**What these concepts do not cover:**
Risk factors associated with each stage are not owned here. Vulnerability
scoring, intervention recommendations, and outcome indicators associated
with stages are not owned here. These belong to the Risk Domain (Stage 3),
Case Management (Stage 5), and Outcome Measurement (Stage 6) respectively.

### Capability Concepts

**Authoritative file:** shared/human-model/taxonomy/capabilities.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| capability | Capability | shared/human-model/taxonomy/capabilities.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

### Dependency Concepts

**Authoritative file:** shared/human-model/taxonomy/dependency.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| dependency | Dependency | shared/human-model/taxonomy/dependency.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

### Family Structure Concepts

**Authoritative file:** shared/human-model/ontology/family-structure.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `family_structure` | Family Structure | shared/human-model/ontology/family-structure.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

### Health Condition Concepts

**Authoritative file:** shared/human-model/taxonomy/health-conditions.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| health_condition | Health Condition | shared/human-model/taxonomy/health-conditions.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

---

## Risk Domain

**Owner domain:** Risk Domain
**Introduced:** Phase 3.0
**Governing ADRs:** ADR-010, ADR-011, ADR-012, ADR-013, ADR-014

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `hazard_category` | Hazard Category | `shared/risk/taxonomy/hazard-categories.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `exposure` | Exposure | `shared/risk/ontology/exposure.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `vulnerability` | Vulnerability | `shared/risk/ontology/vulnerability.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `financial_buffer` | Financial Buffer | `shared/risk/taxonomy/protective-factors.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `livelihood_diversity` | Livelihood Diversity | `shared/risk/taxonomy/protective-factors.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `treatment_continuity_active` | Treatment Continuity Active | `shared/risk/taxonomy/protective-factors.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `household_resilience` | Household Resilience | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `absorptive_capacity` | Absorptive Capacity | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `adaptive_capacity` | Adaptive Capacity | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `recovery_capacity` | Recovery Capacity | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `support_redundancy` | Support Redundancy | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `role_substitution_capacity` | Role Substitution Capacity | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `buffering_capacity` | Buffering Capacity | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `recovery_resources` | Recovery Resources | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `caregiving_continuity` | Caregiving Continuity | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `decision_continuity` | Decision Continuity | `shared/risk/ontology/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk` | Risk | `shared/risk/ontology/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_composition` | Risk Composition | `shared/risk/ontology/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_characterization` | Risk Characterization | `shared/risk/ontology/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_profile` | Risk Profile | `shared/risk/ontology/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_horizon` | Risk Horizon | `shared/risk/ontology/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_trend` | Risk Trend | `shared/risk/ontology/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_state` | Risk State | `shared/risk/ontology/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `exploitation_and_coercion_indicators` | Exploitation and Coercion Indicators | `shared/risk/taxonomy/protection-indicators.yaml` | Risk Domain | Added Stage 3B. May be referenced by any domain; must not be redefined. Referenced cross-domain as `shared_risk:exploitation_and_coercion_indicators` by Registration's `situation.protection_indicators_observed` (`registration/ontology/data-properties.yaml`) — the same reconciliation pattern as `need_severity`/`need_relationship_type` above: no parallel vocabulary authored in Registration. |
## Verification Operations Domain

**Authoritative files:** `verification-operations/ontology/`, `verification-operations/taxonomy/`
**Owner domain:** Verification Operations
**Introduced:** Phase 4.0 (canonically migrated)
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `verification_subject` | Verification Subject | `verification-operations/ontology/entities.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `verification_activity` | Verification Activity | `verification-operations/ontology/entities.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `field_observation` | Field Observation | `verification-operations/ontology/entities.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `verification_finding` | Verification Finding | `verification-operations/ontology/entities.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `reverification_trigger` | Reverification Trigger | `verification-operations/ontology/entities.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `human_review` | Human Review | `verification-operations/ontology/entities.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `verification_assignment` | Verification Assignment | `verification-operations/ontology/entities.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |

---

## Beneficiary Lifecycle Domain

**Authoritative files:** `beneficiary-lifecycle/taxonomy/`, `beneficiary-lifecycle/ontology/`
**Owner domain:** Beneficiary Lifecycle
**Introduced:** Phase 4.x
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `engagement_stage` | Engagement Stage | `beneficiary-lifecycle/taxonomy/engagement-stage.yaml` | Beneficiary Lifecycle | May be referenced by any domain; must not be redefined |
| `exit_reason` | Exit Reason | `beneficiary-lifecycle/taxonomy/exit-reasons.yaml` | Beneficiary Lifecycle | May be referenced by any domain; must not be redefined |

## Needs Assessment Domain

**Authoritative files (canonical):** `needs-assessment/ontology/entities.yaml`,
`needs-assessment/ontology/relationships.yaml`,
`needs-assessment/ontology/data-properties.yaml`,
`needs-assessment/ontology/lifecycle-constraints.yaml`,
`needs-assessment/ontology/semantic-constraints.yaml`,
`needs-assessment/taxonomy/evidence.yaml`, `needs-assessment/taxonomy/finding.yaml`,
`needs-assessment/taxonomy/session.yaml`, `needs-assessment/taxonomy/governance.yaml`
**Owner domain:** Needs Assessment
**Introduced:** Phase 4.5
**Governing ADRs:** ADR-008

**Note — legacy monolith retired (Phase 1.3A):** `needs-assessment/ontology.yaml` and
`needs-assessment/taxonomy.yaml` have been deleted. Their one piece of unique content not
already superseded by the canonical files above — `need_severity` — was migrated to
`needs-assessment/ontology/data-properties.yaml` (`need_assertion.need_severity`,
referencing the existing `registration_tax:need_severity` scheme rather than duplicating
it). Every other legacy concept (`Assessment`, `AssessmentFinding`, `IdentifiedNeed`,
`assessment_scope`, `assessment_status`, `finding_confidence`) was confirmed already
superseded in substance by the canonical concepts below and required no migration. See
`needs-assessment/Needs_Assessment_Legacy_Migration_Dependency_Report.md` for the
dependency analysis this retirement was conditioned on, and
`PHASE1_3A_OWNERSHIP_CONFLICT_RESOLUTION.md` for the full determination.

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `assessment_instrument` | Assessment Instrument | `needs-assessment/ontology/entities.yaml` | Needs Assessment | Specializes `shared:assessment_tool` (`parent`). May be referenced by any domain; must not be redefined |
| `assessment_indicator` | Assessment Indicator | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_session` | Assessment Session | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `observation` | Observation | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `need_assertion` | Need Assertion (Finding) | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `finding_consensus` | Finding Consensus | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `supervisor_review` | Supervisor Review | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessor_calibration` | Assessor Calibration | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `reassessment_trigger` | Reassessment Trigger | `needs-assessment/ontology/entities.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `session_status` | Session Status | `needs-assessment/taxonomy/session.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_modality` | Assessment Modality | `needs-assessment/taxonomy/session.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `missing_data_reason` | Missing Data Reason | `needs-assessment/taxonomy/session.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_depth` | Assessment Depth | `needs-assessment/taxonomy/session.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_urgency` | Assessment Urgency | `needs-assessment/taxonomy/session.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_methodology` | Assessment Methodology | `needs-assessment/taxonomy/session.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `evidence_type` | Evidence Type | `needs-assessment/taxonomy/evidence.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `confidence_level` | Confidence Level | `needs-assessment/taxonomy/evidence.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `conflict_status` | Conflict Status | `needs-assessment/taxonomy/evidence.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `finding_status` | Finding Status | `needs-assessment/taxonomy/finding.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `invalidation_reason` | Invalidation Reason | `needs-assessment/taxonomy/finding.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `need_urgency` | Need Urgency | `needs-assessment/taxonomy/finding.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `review_status` | Review Status | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `rejection_reason` | Rejection Reason | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `calibration_status` | Calibration Status | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `calibration_outcome` | Calibration Outcome | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `consensus_status` | Consensus Status | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `consensus_outcome` | Consensus Outcome | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `trigger_status` | Trigger Status | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `trigger_type` | Trigger Type | `needs-assessment/taxonomy/governance.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |

**Formerly-legacy concepts, now retired (Phase 1.3A):** `Assessment` → superseded by
`assessment_session`; `AssessmentFinding` → superseded by `observation` + `need_assertion`;
`IdentifiedNeed` → superseded by `need_assertion`; `assessment_scope` → superseded by the
`session_evaluates_person`/`_household`/`_community` relationship trio;
`assessment_status` → superseded by `session_status` and the `assessment_session`
lifecycle-constraints state machine; `finding_confidence` → superseded by
`confidence_level`. `need_severity` had no canonical successor and was migrated (see the
note above) rather than superseded — it is not owned by Needs Assessment; see "Explicit
References Only" below.

**Relationships Owned:**
- `session_uses_instrument`
- `instrument_contains_indicator`
- `session_evaluates_person`
- `session_evaluates_household`
- `session_evaluates_community`
- `session_conducted_by_person`
- `session_conducted_by_actor`
- `session_yields_observation`
- `observation_evaluates_indicator`
- `observation_synthesizes_into`
- `observation_based_on_claim`
- `need_assertion_based_on_verified_fact`
- `consensus_resolves_finding`
- `consensus_reviews_observation`
- `session_supersedes_assertion`
- `review_audits_session`
- `calibration_audits_assessor`
- `trigger_initiates_session`
- `assertion_influences_assertion` (added Stage 2A Canonical Needs Assessment
  Enrichment — mirrors Registration's `need_influences_need` at the
  synthesized-finding level; see `need_relationship_type` below for the
  cross-domain taxonomy this relationship's qualifying property references)

**Explicit References Only (Owned Elsewhere):**
- `person`, `household`, `actor`, `assessment_tool` (Shared)
- `geographic_area` (Community Context)
- `claim` (Registration)
- `need_severity` (Registration — `registration/taxonomy/needs.yaml`, referenced cross-domain
  as `registration_tax:need_severity` by `need_assertion.need_severity`; added Phase 1.3A)
- `need_relationship_type` (Registration — `registration/taxonomy/needs.yaml`, referenced
  cross-domain as `registration_tax:need_relationship_type` by
  `need_assertion_relationship_type`, the qualifying property of
  `assertion_influences_assertion`; added Stage 2A Canonical Needs Assessment
  Enrichment, same reconciliation pattern as `need_severity` immediately above —
  no parallel scheme authored)
- `verification_finding` (Verification Operations)
- `thematic_sectors` (Programs) — **open item, not a ratified ownership assignment.**
  `thematic_sector` currently draws its vocabulary from `programs_tax:thematic_sectors`.
  The reserved long-term owner is `shared:humanitarian_sector` (see Shared Ontology
  section above); reassignment is pending a Shared-promotion ADR and is documented,
  not implemented, in this pass.

---

## Case Management Domain

**Authoritative files:** `case-management/taxonomy/`, `case-management/ontology/`
**Owner domain:** Case Management
**Introduced:** Phase 5.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `case_status` | Case Status | `case-management/taxonomy/case_status.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `priority_level` | Priority Level | `case-management/taxonomy/priority_level.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `referral_status` | Referral Status | `case-management/taxonomy/referral_status.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `case_origin` | Case Origin | `case-management/taxonomy/case_origin.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `closure_reason` | Closure Reason | `case-management/taxonomy/closure_reason.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `case` | Case | `case-management/ontology/entities.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `case_plan` | Case Plan | `case-management/ontology/entities.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `referral` | Referral | `case-management/ontology/entities.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `follow_up` | Follow Up | `case-management/ontology/entities.yaml` | Case Management | Introduced per the Phase 1.1A Canonical Semantic Foundation, promoted from a nested string field of the `case_timeline` Value Object to its own entity (status, due date, assignee, outcome). May be referenced by any domain; must not be redefined. |
| `case_note` | Case Note | `case-management/ontology/data-properties.yaml` (nested field of the `case_timeline` Value Object) | Case Management | May be referenced by any domain; must not be redefined |
| `case_assignment` | Case Assignment | Not yet implemented — named in discovery docs and README only; no `entities.yaml` row exists | Case Management | Reserved; declare an authoritative file here once authored |

---

## Volunteer Operations Domain

**Authoritative files:** `volunteer-operations/ontology/*.yaml`, `volunteer-operations/taxonomy/*.yaml`
**Owner domain:** Volunteer Operations
**Introduced:** Foundational authoring (ADR-024 — *Canonical (Foundational) — Operational Deferred*)
**Governing ADRs:** ADR-024, ADR-004, ADR-008, ADR-018, ADR-023

Foundational (Tier 1) concepts only. The operational/runtime layer (Tier 2 —
scheduling, dispatch, workload, trust/performance scoring, the assignment act,
per-instance assignment/training history) is deferred to the Stage-9 activation
trigger and is intentionally absent from this table until authored.

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `volunteer_profile` | Volunteer Profile | `volunteer-operations/ontology/entities.yaml` | Volunteer Operations | Attaches behind `shared:actor`; must not redefine the actor or the `volunteer` role. Must not be redefined elsewhere. |
| `volunteer_team` | Volunteer Team | `volunteer-operations/ontology/entities.yaml` | Volunteer Operations | Structural grouping only; must not be redefined |
| `volunteer_status` | Volunteer Status | `volunteer-operations/taxonomy/volunteer-classification.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |
| `volunteer_type` | Volunteer Type | `volunteer-operations/taxonomy/volunteer-classification.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |
| `skill_category` | Skill Category | `volunteer-operations/taxonomy/skills.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |
| `certification_type` | Certification Type | `volunteer-operations/taxonomy/certifications.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |
| `availability_type` | Availability Type | `volunteer-operations/taxonomy/availability.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |
| `assignment_type` | Assignment Type | `volunteer-operations/taxonomy/assignment-types.yaml` | Volunteer Operations | Eligibility classification only; must not be conflated with the assignment act (FLAG-006). Must not be redefined |
| `coverage_type` | Coverage Type | `volunteer-operations/taxonomy/coverage.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |
| `language_proficiency` | Language Proficiency | `volunteer-operations/taxonomy/languages.yaml` | Volunteer Operations | Promotion candidate to Shared if a second domain needs it (VO-FLAG-B); must not be redefined |
| `affiliation_type` | Affiliation Type | `volunteer-operations/taxonomy/affiliation.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |
| `training_status` | Training Status | `volunteer-operations/taxonomy/training.yaml` | Volunteer Operations | May be referenced by any domain; must not be redefined |

**Relationships Owned (domain-local):**
- `profile_of` (`volunteer_profile` → `shared:actor`)
- `member_of` / `has_member` (`volunteer_profile` ↔ `volunteer_team`)
- `affiliated_with` (`volunteer_profile` → `shared_org:organisation`)

**Explicit References Only (Owned Elsewhere):**
- `actor` (Shared Ontology)
- `organisation` (Shared Taxonomy)
- `volunteer` role label (Shared — `persons.yaml`)
- `verification_assignment` (Verification Operations), `CaseAssignment` (Case Management) — the assignment act (FLAG-006)

---

## Shared Time Domain

**Authoritative files:** `shared/taxonomy/time.yaml`
**Owner domain:** Shared Domain
**Introduced:** Phase 4.0
**Governing ADRs:** ADR-007, ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `duration_bands` | Duration Bands | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |
| `onset_recency` | Onset Recency | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |
| `recurrence_patterns` | Recurrence Patterns | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |
| `temporal_status` | Temporal Status | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |
| `observation_windows` | Observation Windows | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |
| `temporal_granularity` | Temporal Granularity | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |
| `waiting_and_grace_periods` | Waiting and Grace Periods | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |
| `evidence_freshness` | Evidence Freshness | `shared/taxonomy/time.yaml` | Shared Domain | May be referenced by any domain; must not be redefined |

---

## Consent & Privacy Domain

**Authoritative file:** `consent-and-privacy/ontology.yaml`
**Owner domain:** Consent & Privacy
**Introduced:** Phase 5.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `Consent` | Consent | `consent-and-privacy/ontology.yaml` | Consent & Privacy | May be referenced by any domain; must not be redefined |

---

## Flagged Boundary Cases

The following are known areas where concept ownership requires future
alignment. They are not current conflicts but are recorded here so that
future domain designers do not create silent drift.

### FLAG-001: functional_capacity and capabilities.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/taxonomy/persons.yaml` |
| Concept | `functional_capacity` (enum: full, partial, dependent) |
| Situation | This is a proto-capability concept declared before the Shared Human Model existed. It functions as a placeholder for a capability model. |
| Risk | When `capabilities.yaml` is created in Phase 2.0, `functional_capacity` in persons.yaml must reference that file as its authority rather than defining its own capability vocabulary. |
| Resolution required | Update `shared/taxonomy/persons.yaml` to reference `capabilities.yaml`. No silent modification — record in DECISIONS.md if the change is architectural. |
| Status | Resolved |

### FLAG-002: Dependency type names and dependency.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/taxonomy/lifecycle-stages.yaml` |
| Concept | Dependency type labels (physiological, developmental, medical, safety, nutritional, protective, educational, situational, health, economic, physical, social, legal) |
| Situation | These type labels appear in `characteristic_dependencies` entries throughout lifecycle-stages.yaml. They are descriptive, not definitional — they describe the nature of each stage's dependencies without formally owning the dependency type vocabulary. |
| Risk | When `dependency.yaml` is created, it will formally own the dependency type taxonomy. The labels used in lifecycle-stages.yaml must align with that taxonomy. |
| Resolution required | Verify that all dependency type labels in lifecycle-stages.yaml are consistent with the authoritative vocabulary in `dependency.yaml`. Update lifecycle-stages.yaml if any labels require standardisation. |
| Status | Resolved |

### FLAG-003: Health condition references and health-conditions.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/taxonomy/lifecycle-stages.yaml` |
| Concept | Health condition labels used descriptively (SAM, MAM, chronic illness, cognitive decline, frailty, polypharmacy) |
| Situation | These appear in `characteristic_vulnerabilities` entries as descriptive references. They are not defined here — they are named as examples of vulnerabilities characteristic to each stage. |
| Risk | When `health-conditions.yaml` is created, it will own the authoritative vocabulary for these conditions. The descriptive references in lifecycle-stages.yaml should remain consistent with that vocabulary. |
| Resolution required | Verify descriptive references in lifecycle-stages.yaml align with authoritative terminology in `health-conditions.yaml`. |
| Status | Resolved |

### FLAG-004: Capability profile descriptions and capabilities.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/taxonomy/lifecycle-stages.yaml` |
| Concept | Capability descriptions in `characteristic_capabilities` entries (e.g., independent mobility, emergent language, literacy, full economic productive capacity) |
| Situation | These are descriptive profiles of what each stage can do. They anticipate the capability vocabulary that `capabilities.yaml` will formally define. |
| Risk | When `capabilities.yaml` is created, the capability vocabulary it establishes must be consistent with the capability descriptions already recorded in lifecycle-stages.yaml. |
| Resolution required | Cross-check capability vocabulary in `capabilities.yaml` against lifecycle-stages.yaml descriptive entries. Align terminology. |
| Status | Resolved |

### FLAG-005: household entity defined independently in two domains — RESOLVED

| Item | Detail |
|---|---|
| Prior location | `shared/ontology/entities.yaml` (`id: household`, `parent: subject`) **and** `registration/ontology/entities.yaml` (`id: household`, its own fuller description, `cardinality_in_case: exactly_one`) |
| Concept | `household` |
| Situation (prior) | Both files declared a full `household` entity independently. Neither declared the other as canonical; registration's definition was not expressed as a reference to the shared entity. |
| Risk (prior) | This was a live single-ownership conflict under ADR-008 — two authoritative-looking definitions of the same concept coexisted. |
| Resolution implemented | Per the Phase 1.1A Canonical Semantic Foundation ratification: `shared/ontology/entities.yaml` remains the **sole owner** of `household` (now with an `household_id` identifier, added in `shared/ontology/data-properties.yaml`). `registration/ontology/entities.yaml`'s conflicting `id: household` entity was renamed to `household_snapshot` — the intake-time view of a household's composition and attributes for one case — and a new relationship `household_snapshot_observes_household` (`registration/ontology/relationships.yaml`) links every snapshot to exactly one canonical Household. All registration relationships, data properties, semantic constraints, and reasoning-rule field-path references (`readiness-rules.yaml`, `questioning-strategy.yaml`, `case-coherence-rules.yaml`, `gap-detection-rules.yaml`, `inference-rules.yaml`) were updated to `household_snapshot`. |
| Status | **Resolved and implemented.** No further conformance migration pending. |

### FLAG-006: actor qualification vs. the assignment act (Volunteer Operations boundary)

| Item | Detail |
|---|---|
| Existing locations | `shared/ontology/entities.yaml` (`id: actor`, "Placeholder for an operational participant"); `shared/taxonomy/persons.yaml` (`person_roles.volunteer`); `verification-operations/ontology/entities.yaml` (`verification_assignment`) and `relationships.yaml` (`verification_activity_conducted_by_actor`); `case-management/ontology/` (`CaseAssignment`) |
| Concept | The boundary between a volunteer's **qualification / fitness to be assigned** (skills, certifications, availability, geographic coverage, trust, training) and the **assignment act** itself |
| Situation | `verification-operations/ontology/relationships.yaml` already states, one-directionally: *"Verification Operations does not define actor qualification, roles, or types — that remains a Volunteer Operations concern (Level 2 placeholder)."* `review-decisions.yaml` echoes it. `verification_assignment` and `CaseAssignment` own the *assignment event*; the `Actor` entity and the `volunteer` role are single-owned in Shared. Volunteer Operations (Stage 9 placeholder) will own the *profile behind the actor* — never the assignment act, the actor entity, or the role label. |
| Risk | On Volunteer Operations activation, the domain must attach its profile *behind* the shared `Actor` reference (via a `references`/relationship link), not mint a second actor entity or redefine `verification_assignment`/`CaseAssignment`. Silent drift would produce a duplicate actor/assignment model. |
| Resolution required | On activation: add a Volunteer Operations owned-concepts section here; author the profile-to-`shared:Actor` link; leave the assignment acts owned by their operational domains. See `docs/architecture/Volunteer_Operations_Migration_Plan.md` (Phase 4) and `Volunteer_Operations_Domain_Audit.md` (VO-6). |
| Status | **Foundational side authored** (ADR-024). The Volunteer Operations owned-concepts section is added above; `volunteer_profile` attaches behind `shared:actor` via `profile_of` (`volunteer-operations/ontology/relationships.yaml`); eligibility is modeled as `eligible_assignment_type` (a data property), and the assignment **act** remains owned by `verification-operations` (`verification_assignment`) and `case-management` (`CaseAssignment`) — not duplicated. The boundary is now held reciprocally in authored YAML, not only in prose. The operational layer (trust/performance scoring, assignment history) stays deferred to Stage 9. |
