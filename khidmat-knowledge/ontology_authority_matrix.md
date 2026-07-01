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
| `assessment_tool` | AssessmentTool | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for Needs Assessment. Must not be redefined. |
| `humanitarian_sector` | HumanitarianSector | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for Needs Assessment. Must not be redefined. |
| `intervention_type` | InterventionType | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for Case Management. Must not be redefined. |
| `actor` | Actor | `shared/ontology/entities.yaml` | Shared Ontology | Placeholder for an operational participant. Must not be redefined. |

---

## Shared Human Model

### Lifecycle Stage Concepts

**Authoritative file:** `shared/human-model/lifecycle-stages.yaml`
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-007, ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `infant` | Infant | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `toddler` | Toddler | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `early_childhood` | Early Childhood | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `school_age_child` | School-Age Child | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `adolescent` | Adolescent | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `young_adult` | Young Adult | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `adult` | Adult | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `older_adult` | Older Adult | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `elderly` | Elderly | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

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

**Authoritative file:** shared/human-model/capabilities.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| capability | Capability | shared/human-model/capabilities.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

### Dependency Concepts

**Authoritative file:** shared/human-model/dependency.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| dependency | Dependency | shared/human-model/dependency.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

### Family Structure Concepts

**Authoritative file:** shared/human-model/family-structure.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| amily_structure | Family Structure | shared/human-model/family-structure.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

### Health Condition Concepts

**Authoritative file:** shared/human-model/health-conditions.yaml
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| health_condition | Health Condition | shared/human-model/health-conditions.yaml | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

---

## Risk Domain

**Owner domain:** Risk Domain
**Introduced:** Phase 3.0
**Governing ADRs:** ADR-010, ADR-011, ADR-012, ADR-013, ADR-014

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `hazard_category` | Hazard Category | `shared/risk/hazard-categories.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `exposure` | Exposure | `shared/risk/exposure.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `vulnerability` | Vulnerability | `shared/risk/vulnerability.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `financial_buffer` | Financial Buffer | `shared/risk/protective-factors.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `livelihood_diversity` | Livelihood Diversity | `shared/risk/protective-factors.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `treatment_continuity_active` | Treatment Continuity Active | `shared/risk/protective-factors.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `household_resilience` | Household Resilience | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `absorptive_capacity` | Absorptive Capacity | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `adaptive_capacity` | Adaptive Capacity | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `recovery_capacity` | Recovery Capacity | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `support_redundancy` | Support Redundancy | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `role_substitution_capacity` | Role Substitution Capacity | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `buffering_capacity` | Buffering Capacity | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `recovery_resources` | Recovery Resources | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `caregiving_continuity` | Caregiving Continuity | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `decision_continuity` | Decision Continuity | `shared/risk/household-resilience.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk` | Risk | `shared/risk/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_composition` | Risk Composition | `shared/risk/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_characterization` | Risk Characterization | `shared/risk/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_profile` | Risk Profile | `shared/risk/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_horizon` | Risk Horizon | `shared/risk/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_trend` | Risk Trend | `shared/risk/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
| `risk_state` | Risk State | `shared/risk/risk.yaml` | Risk Domain | May be referenced by any domain; must not be redefined |
## Verification Operations Domain

**Authoritative file:** `verification-operations/verification-operations.yaml`
**Owner domain:** Verification Operations
**Introduced:** Phase 4.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `verification_subject` | Verification Subject | `verification-operations/verification-operations.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `verification_activity` | Verification Activity | `verification-operations/verification-operations.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `field_observation` | Field Observation | `verification-operations/verification-operations.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `verification_finding` | Verification Finding | `verification-operations/verification-operations.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `reverification_trigger` | Reverification Trigger | `verification-operations/verification-operations.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `human_review` | Human Review | `verification-operations/verification-operations.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |
| `verification_assignment` | Verification Assignment | `verification-operations/verification-operations.yaml` | Verification Operations | May be referenced by any domain; must not be redefined |

---

## Beneficiary Lifecycle Domain

**Authoritative files:** `beneficiary-lifecycle/taxonomy.yaml`, `beneficiary-lifecycle/ontology.yaml`
**Owner domain:** Beneficiary Lifecycle
**Introduced:** Phase 4.x
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `engagement_stage` | Engagement Stage | `beneficiary-lifecycle/taxonomy.yaml` | Beneficiary Lifecycle | May be referenced by any domain; must not be redefined |
| `exit_reason` | Exit Reason | `beneficiary-lifecycle/taxonomy.yaml` | Beneficiary Lifecycle | May be referenced by any domain; must not be redefined |
**Authoritative files:** `needs-assessment/taxonomy.yaml`, `needs-assessment/ontology.yaml`
**Owner domain:** Needs Assessment
**Introduced:** Phase 4.5
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `assessment_depth` | Assessment Depth | `needs-assessment/taxonomy.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_urgency` | Assessment Urgency | `needs-assessment/taxonomy.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_scope` | Assessment Scope | `needs-assessment/taxonomy.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_status` | Assessment Status | `needs-assessment/taxonomy.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `assessment_methodology` | Assessment Methodology | `needs-assessment/taxonomy.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `finding_confidence` | Finding Confidence | `needs-assessment/taxonomy.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `need_severity` | Need Severity | `needs-assessment/taxonomy.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `Assessment` | Assessment | `needs-assessment/ontology.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `AssessmentFinding` | Assessment Finding | `needs-assessment/ontology.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |
| `IdentifiedNeed` | Identified Need | `needs-assessment/ontology.yaml` | Needs Assessment | May be referenced by any domain; must not be redefined |

**Relationships Owned:**
- `assesses`
- `produces`
- `belongs_to`
- `synthesizes_into`
- `synthesized_from`
- `based_on_claim`
- `based_on_verified_fact`
- `affects`
- `superseded_by`

**Explicit References Only (Owned Elsewhere):**
- `Subject` (Shared)
- `HumanitarianSector` (Shared)
- `AssessmentTool` (Shared)
- `RegistrationClaim` (Registration)
- `VerificationFinding` (Verification)

---

## Case Management Domain

**Authoritative files:** `case-management/taxonomy.yaml`, `case-management/ontology.yaml`
**Owner domain:** Case Management
**Introduced:** Phase 5.0
**Governing ADRs:** ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `case_status` | Case Status | `case-management/taxonomy.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `priority_level` | Priority Level | `case-management/taxonomy.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `referral_status` | Referral Status | `case-management/taxonomy.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `case_origin` | Case Origin | `case-management/taxonomy.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `case_outcome` | Case Outcome | `case-management/taxonomy.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `administrative_closure_reason` | Administrative Closure Reason | `case-management/taxonomy.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `Case` | Case | `case-management/ontology.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `CasePlan` | Case Plan | `case-management/ontology.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `Referral` | Referral | `case-management/ontology.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `FollowUp` | Follow Up | `case-management/ontology.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `CaseAssignment` | Case Assignment | `case-management/ontology.yaml` | Case Management | May be referenced by any domain; must not be redefined |
| `CaseNote` | Case Note | `case-management/ontology.yaml` | Case Management | May be referenced by any domain; must not be redefined |

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
| Existing location | `shared/human-model/lifecycle-stages.yaml` |
| Concept | Dependency type labels (physiological, developmental, medical, safety, nutritional, protective, educational, situational, health, economic, physical, social, legal) |
| Situation | These type labels appear in `characteristic_dependencies` entries throughout lifecycle-stages.yaml. They are descriptive, not definitional — they describe the nature of each stage's dependencies without formally owning the dependency type vocabulary. |
| Risk | When `dependency.yaml` is created, it will formally own the dependency type taxonomy. The labels used in lifecycle-stages.yaml must align with that taxonomy. |
| Resolution required | Verify that all dependency type labels in lifecycle-stages.yaml are consistent with the authoritative vocabulary in `dependency.yaml`. Update lifecycle-stages.yaml if any labels require standardisation. |
| Status | Resolved |

### FLAG-003: Health condition references and health-conditions.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/lifecycle-stages.yaml` |
| Concept | Health condition labels used descriptively (SAM, MAM, chronic illness, cognitive decline, frailty, polypharmacy) |
| Situation | These appear in `characteristic_vulnerabilities` entries as descriptive references. They are not defined here — they are named as examples of vulnerabilities characteristic to each stage. |
| Risk | When `health-conditions.yaml` is created, it will own the authoritative vocabulary for these conditions. The descriptive references in lifecycle-stages.yaml should remain consistent with that vocabulary. |
| Resolution required | Verify descriptive references in lifecycle-stages.yaml align with authoritative terminology in `health-conditions.yaml`. |
| Status | Resolved |

### FLAG-004: Capability profile descriptions and capabilities.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/lifecycle-stages.yaml` |
| Concept | Capability descriptions in `characteristic_capabilities` entries (e.g., independent mobility, emergent language, literacy, full economic productive capacity) |
| Situation | These are descriptive profiles of what each stage can do. They anticipate the capability vocabulary that `capabilities.yaml` will formally define. |
| Risk | When `capabilities.yaml` is created, the capability vocabulary it establishes must be consistent with the capability descriptions already recorded in lifecycle-stages.yaml. |
| Resolution required | Cross-check capability vocabulary in `capabilities.yaml` against lifecycle-stages.yaml descriptive entries. Align terminology. |
| Status | Resolved |
