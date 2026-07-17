# Khidmat Knowledge Layer — File Inventory

**Authority:** Knowledge Layer Architect
**Scope:** All files in khidmat-knowledge/ as of Phase 3.0 entry
**Purpose:** Single source of truth for what every file is, what it owns, and what it owes

---

## SHARED DOMAIN

---

### shared/taxonomy/persons.yaml

**Purpose:** Generic person vocabulary shared across all domains. Declares person roles and base attributes that every domain references when talking about a human being.

**Concepts Owned:**
- Person role labels (beneficiary, registrant, proxy, volunteer, case_manager, programme_officer, organisation_staff, donor)
- Age classification (minor / adult boundary and consequences)
- Gender vocabulary (male, female, not_disclosed)
- Functional capacity (reference to capabilities.yaml)

**Relationships Owned:** None. Taxonomy only — no structural relationships declared.

**Maturity:** Partial. Roles are declared but not defined. Functional capacity references the Shared Human Model capabilities.

**Known Gaps:**
- No lifecycle stage model. Age is a boundary (minor/adult), not a developmental context.
- Functional capacity is inert — no domain file derives behaviour from it.
- No capability vocabulary (what a person can do, not only their capacity for daily tasks).
- No health condition vocabulary.
- Future domain roles (case_manager, programme_officer) are declared here but their detailed definitions belong in their respective domains. The declaration is correct; the future detail is absent.

**Overlap / Conflicts:**
- `functional_capacity` is referenced by both `registration/ontology/attributes.yaml#beneficiary` and `registration/ontology/attributes.yaml#household_member`. Authority is now deferred to `capabilities.yaml`. No conflict.

---

### shared/taxonomy/organisations.yaml

**Purpose:** Organisation type vocabulary shared across domains. Registration uses it for referral source classification. Future domains (programs, support delivery) will use it for partner management.

**Concepts Owned:**
- Organisation type labels (flat list of 8 types: hospital_or_clinic, school_or_madrasa, mosque_or_religious_institution, ngo_or_charity, government_office, community_organisation, employer, court_or_legal_authority)

**Relationships Owned:** None.

**Maturity:** Minimal. A flat list. Not an organisation model.

**Known Gaps:**
- No accountability structure (who is this organisation answerable to).
- No capacity model (what can this organisation provide, and to whom).
- No relationship model (does this organisation have a partnership with Khidmat, a referral agreement, a service contract).
- No contact or geographic reach attributes.
- `mosque_or_religious_institution` conflates two distinct organisational types. A mosque has a different accountability and service model from a school that happens to be a madrasa.

**Overlap / Conflicts:** None currently. Future programs and support-delivery domains will need to extend this significantly without creating a second authority.

---

### shared/taxonomy/locations.yaml

**Purpose:** Location vocabulary for volunteer dispatch and geographic reasoning. Registration uses it to classify how precisely a beneficiary can be found.

**Concepts Owned:**
- Location precision (exact_address, area_with_landmark, area_only, unknown)
- Location stability (permanent, temporary, transient, unknown)

**Relationships Owned:** None.

**Maturity:** Adequate for volunteer dispatch. Insufficient for geographic reasoning.

**Known Gaps:**
- No geographic hierarchy (district, block, village, ward). Cannot aggregate cases by area.
- No environmental risk profile (flood zone, drought zone, remote access). Cannot reason about seasonal or environmental vulnerability.
- No urban/rural classification. These carry different service access assumptions.
- No distance-to-services attribute. Cannot reason about healthcare or school access without knowing how far they are.
- No seasonal accessibility attribute. A location may be reachable in dry season and cut off in monsoon.

**Overlap / Conflicts:** None.

---

### shared/taxonomy/document-types.yaml

**Purpose:** Shared document type vocabulary. Registration uses it for evidence classification. Future domains will use it for document management and audit trails.

**Concepts Owned:**
- Identity documents (national_id, passport, birth_certificate, voter_registration_card, ration_card, refugee_documentation, no_document)
- Medical documents (doctors_letter, diagnosis_report, prescription, discharge_summary, referral_letter, medical_test_result)
- Financial documents (salary_slip, bank_statement, termination_letter, tax_document)
- Legal documents (court_order, eviction_notice, tenancy_agreement, death_certificate, police_report)
- Institutional documents (school_fee_statement, enrollment_certificate, ngo_referral_letter, government_benefit_letter)

**Relationships Owned:** None.

**Maturity:** Adequate for intake evidence identification. Insufficient for document lifecycle management.

**Known Gaps:**
- No validity model (documents expire, are revoked, are disputed, are fraudulent).
- No provenance model (who issued it, when, under what authority).
- No verification status (has this document been confirmed as genuine).
- `ration_card` is India-specific and carries specific entitlements. This should be noted or the file should acknowledge regional specificity.

**Overlap / Conflicts:** Registration/taxonomy/evidence.yaml is a placeholder that will eventually extend this file. The authority boundary is correctly declared there.

---

### shared/taxonomy/time.yaml

**Purpose:** Defines the authoritative temporal vocabulary for the Khidmat Knowledge Layer. Every domain that reasons about duration, recurrence, validity, freshness, or time-bounded status draws from this file.

**Concepts Owned:**
- duration_bands
- onset_recency
- recurrence_patterns
- temporal_status
- observation_windows
- temporal_granularity
- waiting_and_grace_periods
- evidence_freshness

**Relationships Owned:** None.

**Maturity:** Complete (Phase 4.0).

**Known Gaps:** None.

**Overlap / Conflicts:** None.

---

### shared/ontology/entities.yaml

**Purpose:** Will contain entity definitions shared across two or more active domains.

**Concepts Owned:** None currently. Placeholder only.

**Maturity:** Placeholder.

**Known Gaps:** The Person entity as a cross-domain persistent concept does not yet exist. This is the most significant structural gap in the shared layer. The beneficiary entity in registration is a snapshot. A persistent Person entity that survives across cases, registrations, and domains needs to live here.

**Overlap / Conflicts:** None currently. Risk of future drift if domains begin defining their own person sub-entities without promoting to shared.

---

### shared/ontology/relationships.yaml

**Purpose:** Will contain relationships shared across two or more active domains.

**Concepts Owned:** None currently. Placeholder only.

**Maturity:** Placeholder.

**Known Gaps:** Family relationships that span domains (parent-child, caregiver-dependent) need to be here. Currently absent.

**Overlap / Conflicts:** None.

---

### shared/vocabulary/controlled-terms.yaml

**Purpose:** Will contain controlled terms used as field values across multiple domains.

**Concepts Owned:** None currently. Placeholder only.

**Maturity:** Placeholder.

**Known Gaps:** Contact method types (phone, whatsapp, in_person), currency codes, language codes. None formalised.

**Overlap / Conflicts:** None.

---

## SHARED HUMAN MODEL

---

### shared/human-model/README.md

**Purpose:** Architecture definition for the Shared Human Model layer.
Declares scope, design principles, planned files with ownership and
reasoning opportunities, ownership boundaries, and activation criteria.
This is an architecture document, not an ontology file.

**Concepts Owned:** None directly. This file declares ownership boundaries
for the five planned YAML files that will follow.

**Completed files declared here:**
- `lifecycle-stages.yaml` — lifecycle stage concepts ✓ Complete
- `capabilities.yaml` — capability concepts ✓ Complete
- `dependency.yaml` — dependency relationship concepts ✓ Complete
- `family-structure.yaml` — family structure concepts ✓ Complete
- `health-conditions.yaml` — health condition vocabulary ✓ Complete

**Maturity:** Complete.

**Known Gaps:** None for the architecture document itself.

**Overlap / Conflicts:** None. Ownership boundaries explicitly declared.
Risk factors, vulnerability scoring, interventions, outcomes, and program
classifications are explicitly excluded from this model's scope.

---

### shared/human-model/taxonomy/lifecycle-stages.yaml

**Purpose:** Authoritative lifecycle stages ontology for the Shared Human
Model. Defines nine developmental stages as reasoning contexts — each with
characteristic dependencies, capabilities, vulnerabilities, reasoning
implications, and ontology notes. This is not an age-band classification
file; each stage represents a qualitatively distinct developmental reality.

**Concepts Owned:**
- Lifecycle stage identifiers and names (infant, toddler, early_childhood,
  school_age_child, adolescent, young_adult, adult, older_adult, elderly)
- Stage boundary definitions and boundary rationale
- Characteristic dependency types per stage
- Characteristic capability profiles per stage
- Characteristic vulnerability profiles per stage
- Reasoning implications at the ontology level (relationships and
  developmental consequences only — no workflow or intervention logic)
- Ontology notes for future domain interpretation

**Relationships Owned:** None structural. Relationships to capability and
dependency models are referenced by note pending those files' creation.

**Maturity:** Complete. Version 1.0.

**Known Gaps:**
- References to health conditions (SAM, MAM, chronic illness) are
  descriptive placeholders requiring alignment with `health-conditions.yaml`
- References to capability concepts are descriptive placeholders requiring
  alignment with `capabilities.yaml`
- References to dependency relationships are descriptive placeholders
  requiring alignment with `dependency.yaml`

**Overlap / Conflicts:**
- `shared/taxonomy/persons.yaml` declares `functional_capacity` as a
  three-value enum (full, partial, dependent). This is a proto-capability
  concept. Now that `capabilities.yaml` is created, `functional_capacity`
  should reference that file as its authority. No conflict currently;
  alignment task flagged for Phase 3.0 completion.

---

## RISK DOMAIN

---

### shared/risk/README.md

**Purpose:** Scope declaration, design principles, file structure mapping, and activation criteria for the Risk Domain.
**Concepts Owned:** None directly. Declares boundaries and maps the transition from conceptual layout to active implementation.
**Relationships Owned:** None.
**Maturity:** Complete (Phase 3.0).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### shared/risk/governance.md

**Purpose:** Boundary enforcement rules, cross-domain reference patterns, anti-patterns, and alignment contracts for the Risk Domain. Ensures ontology files stay free of documentation bloat.
**Concepts Owned:** None directly. Declares reference constraints and patterns for capabilities, dependency, family structure, health conditions, and registration.
**Relationships Owned:** None.
**Maturity:** Complete (Phase 3.0).
**Known Gaps:** None.
**Overlap / Conflicts:** Resolves descriptive alignment with lifecycle stages (FLAG-005) and family structure.

---

### shared/risk/taxonomy/hazard-categories.yaml

**Purpose:** Qualitative classification of the types of harm under consideration.
**Concepts Owned:** 
- `hazard_category`
**Relationships Owned:** None.
**Maturity:** Complete (Phase 3.0).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### shared/risk/ontology/exposure.yaml

**Purpose:** Defines the relationship between a person, family, or household and a hazard category describing the degree to which they may encounter it.
**Concepts Owned:**
- `exposure`
**Relationships Owned:** None.
**Maturity:** Complete (Phase 3.0).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### shared/risk/ontology/vulnerability.yaml

**Purpose:** Defines standing susceptibility to harm resulting from vulnerability conditions and capacity limitations.
**Concepts Owned:**
- `vulnerability`
**Relationships Owned:** None.
**Maturity:** Complete (Phase 3.0).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### shared/risk/taxonomy/protective-factors.yaml

**Purpose:** Defines observable protective factors that moderate hazard-specific risk.
**Concepts Owned:** 
- The 12 protective factors
- financial_buffer
- livelihood_diversity
- treatment_continuity_active
**Relationships Owned:** Moderation relationships to hazard categories.
**Maturity:** Complete (Phase 3.2).
**Known Gaps:** None.
**Overlap / Conflicts:** Excludes Khidmat-provided interventions to prevent circular dependency.

---

### shared/risk/ontology/household-resilience.yaml

**Purpose:** Defines Household Resilience as a first-class composite capacity to absorb, adapt to, and recover from adversity.
**Concepts Owned:** 
- household_resilience
- absorptive_capacity
- adaptive_capacity
- recovery_capacity
- support_redundancy
- role_substitution_capacity
- buffering_capacity
- recovery_resources
- caregiving_continuity
- decision_continuity
**Relationships Owned:** `supports` relationships (mechanisms to capacities) and `component_of` relationships (capacities to resilience).
**Maturity:** Complete (Phase 3.0).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### shared/risk/ontology/risk.yaml

**Purpose:** Defines Risk as a first-class Risk Domain concept. Models how contributors (hazard categories, exposure, vulnerability, and household resilience) are composed, interpreted, represented, and expressed as a qualitative risk assessment.
**Concepts Owned:**
- `risk`
- `risk_composition`
- `risk_characterization`
- `risk_profile`
- `risk_horizon`
- `risk_trend`
- `risk_state`
- `risk_severity`
**Relationships Owned:**
- `contributes_to` (hazard_category, exposure, vulnerability, household_resilience to risk_composition)
- `informs` (risk_composition to risk_characterization, risk_characterization to risk_profile)
- `represents` (risk_profile to risk)
- `attribute_of` (risk_horizon, risk_trend, risk_state, risk_severity to risk)
**Maturity:** Complete (Phase 3.0).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

## REGISTRATION DOMAIN

---

### registration/taxonomy/actors.yaml

**Purpose:** Defines who participates in a registration conversation, their epistemic role, and how that role affects claim weight and questioning approach.

**Concepts Owned:**
- Registrant types (beneficiary, proxy, volunteer) with subtypes under proxy (family_member, community_member, professional_advocate)
- Claim basis (first_hand, second_hand, observational, inferred)
- Proxy consent values (confirmed, unable_to_obtain, not_yet_obtained, not_applicable)

**Relationships Owned:** None structural. Derives default_claim_basis from registrant_type.

**Maturity:** Mature. Well-designed.

**Known Gaps:**
- The volunteer-as-proxy edge case is unmodelled. When a volunteer cannot locate the beneficiary directly and registers based on community testimony, they are acting as a proxy but are not classified as one. The registrant_type is `volunteer` but the claim basis is `observational` — this conflation hides a case where claim_basis should be `second_hand` for specific claims.
- No model of registrant fatigue or registrant credibility across repeat interactions.

**Overlap / Conflicts:** Registrant roles are declared in `shared/taxonomy/persons.yaml` and detailed here. Authority is correctly split — shared owns the label, registration owns the definition. No conflict.

---

### registration/taxonomy/needs.yaml

**Purpose:** Classification of needs identified during registration. Defines need categories, subtypes, severity levels, and duration values.

**Concepts Owned:**
- Need categories (food, medical, shelter, education, livelihood, psychosocial)
- Need subtypes per category
- Need source (expressed, assessed, both)
- Need severity (reference to needs-assessment/taxonomy.yaml)
- Need duration (one_time, short_term, recurring, long_term)

**Relationships Owned:** None. Subtypes are nested classification, not relationships.

**Maturity:** Adequate for intake. Insufficient for case management or outcome tracking.

**Known Gaps:**
- No need interdependency model. A food need and a medical need may share a root cause and require coordinated response. Currently treated as independent line items.
- No need trajectory (is this need worsening, stable, or improving over time). All needs are assessed as a snapshot.
- Psychosocial subtypes describe the nature of the need correctly but do not reference a mental health condition vocabulary. This creates a gap when mental health reasoning is needed.
- `therapeutic_nutrition` is a subtype of food need. It is clinically a distinct pathway that belongs closer to the medical domain. The current placement is pragmatic but architecturally ambiguous.

**Overlap / Conflicts:** Need severity definitions have been consolidated into `needs-assessment/taxonomy.yaml`. Severity classification rules remain in `reasoning/severity-rules.yaml`. No conflict.

---

### registration/taxonomy/situations.yaml

**Purpose:** Classifies the circumstances that create or sustain vulnerability. Defines how situations develop (trajectory), what domain of life they affect (affected_domains), and what specific event triggered them (trigger_events).

**Concepts Owned:**
- Trajectory (structural, crisis_triggered, progressive, acute)
- Trigger events (bereavement, job_loss, accident_or_injury, illness_onset, displacement, domestic_violence, natural_disaster, legal_crisis)
- Affected domains (economic, health, social, environmental, dependent_load, legal_and_documentation)

**Relationships Owned:** None.

**Maturity:** Good for intake triggering. Insufficient for longitudinal reasoning.

**Known Gaps:**
- No compound situation model. Multiple simultaneous triggers (breadwinner died AND family was displaced) produce qualitatively different vulnerability than either alone. The taxonomy has no way to express compounding.
- The `structural` trajectory is the weakest classification. "Long-standing condition predating any specific event" covers everything from generational poverty to a 5-year-old disability. No texture within it.
- Seasonal and environmental triggers are absent. Pre-monsoon housing vulnerability is a situational context that the system cannot currently classify.
- Affected domains list is flat. There is no weighting or severity-within-domain concept. Economic domain affected at 10% income reduction is not the same as affected at total income loss.

**Overlap / Conflicts:** `safety_flag` is declared as a situation attribute in `ontology/attributes.yaml` but is also denormalised to case level. The canonical authority is on the situation; the case-level flag is a derived convenience. This is documented and intentional.

---

### registration/taxonomy/claims.yaml

**Purpose:** Classifies assertions made during registration and defines the two-dimensional quality model (sufficiency and consistency).

**Concepts Owned:**
- Claim types (identity_claim, situation_claim, need_claim, household_claim)
- Information sufficiency (complete, partial, missing)
- Information consistency (consistent, ambiguous, contradictory)

**Relationships Owned:** None. Cross-references verifiable and evidence_available as boolean attributes owned by `ontology/attributes.yaml`.

**Maturity:** Mature. The two-dimensional quality model is architecturally sound and one of the strongest design decisions in the current layer.

**Known Gaps:**
- No temporal dimension on claims. A claim made in January that is still open in March has aged. The system has no model of claim age or claim staleness.
- No claim revision model. If a registrant corrects a claim mid-conversation, the system records the new claim but there is no audit trail of what was previously stated.

**Overlap / Conflicts:** None.

---

### registration/taxonomy/case-outcomes.yaml

**Purpose:** Defines the status values a case can reach at registration closure.

**Concepts Owned:**
- Case statuses (in_progress, ready_for_verification, requires_review, unsafe_to_verify, duplicate_suspected, on_hold, referred_externally)

**Relationships Owned:** None. Transition rules are in `readiness/readiness-rules.yaml`.

**Maturity:** Mature.

**Known Gaps:**
- `referred_externally` is reserved for future use. The taxonomy declares it but it cannot be used without a referral network domain.
- No terminal "closed" status for cases that have completed the full lifecycle (verified, assisted, closed). This is appropriate for V1 (registration ends at closure) but will need to be added when the beneficiary lifecycle domain activates.

**Overlap / Conflicts:** None.

---

### registration/taxonomy/lead-statuses.yaml

**Purpose:** Defines the status values for the Lead entity during intake and review.

**Concepts Owned:**
- Lead statuses (draft, submitted, assigned_for_review, under_review, approved, needs_clarification, rejected, escalated)

**Relationships Owned:** None.

**Maturity:** Mature.

**Known Gaps:** None significant. Well-scoped for current operational need.

**Overlap / Conflicts:** None.

---

### registration/taxonomy/referral-sources.yaml

**Purpose:** Classifies how a beneficiary came to register, which affects what the AI can assume at conversation start.

**Concepts Owned:**
- Referral types (self_initiated, community_referral, institutional_referral, volunteer_identification, repeat_registration)
- Contextual prior per referral type

**Relationships Owned:** None.

**Maturity:** Mature.

**Known Gaps:** No model of referral quality or referral accuracy. An institutional referral from a hospital carries different epistemic weight than a community referral from a neighbour. Both are classified equivalently in terms of assumed prior knowledge.

**Overlap / Conflicts:** None.

---

### registration/taxonomy/support-interventions.yaml

**Purpose:** Will classify intervention types that can be requested during registration.

**Concepts Owned:** None currently. Placeholder only.

**Maturity:** Placeholder. This is the most operationally urgent gap in the registration domain.

**Known Gaps:** The entire file is a gap. Without an intervention taxonomy, the system cannot reason about what Khidmat can actually offer, intervention fit, intervention sequencing, or intervention outcome.

**Overlap / Conflicts:** None yet. Future risk: if intervention types are invented by the registration domain without coordination with operations staff, they will not map to what Khidmat can actually deliver.

---

### registration/taxonomy/evidence.yaml

**Purpose:** Will classify evidence types used during registration to support claims.

**Concepts Owned:** None currently. Placeholder only.

**Maturity:** Placeholder.

**Known Gaps:** The entire file is a gap. Evidence classification beyond the shared document-types vocabulary is absent. No availability model, no quality model, no link between evidence type and claim type.

**Overlap / Conflicts:** Correctly declared as extending `shared/taxonomy/document-types.yaml`. Authority boundary is clean.

---

### registration/ontology/entities.yaml

**Purpose:** Defines the entities that exist within the registration domain and their cardinality within a case.

**Concepts Owned:**
- Entity declarations: Registrant, Beneficiary, Household, HouseholdMember, Situation, Need, Claim, Evidence, SupportIntervention, Case, Lead, VolunteerReview

**Relationships Owned:** Entity cardinality within a case (exactly_one, one_or_more, zero_or_more).

**Maturity:** Mature. Well-structured.

**Known Gaps:**
- Evidence entity is declared but has no attribute detail (attributes_ref points to a section of data-properties.yaml that does not currently exist for evidence). This is a latent gap.
- VolunteerReview and Lead entities are declared here but their lifecycle is partially owned by lead-statuses.yaml. The authority boundary is not explicitly declared.

**Overlap / Conflicts:** None.

---

### registration/ontology/data-properties.yaml (supersedes retired `attributes.yaml`)

**Purpose:** The canonical home for all datatype/value properties (and Value Object
composite properties, per ADR-023 / `Canonical_Ontology_Schema.md` §17) for registration
domain entities. Replaces the former `attributes.yaml`, which was deleted in Registration
Migration Phase 4 (`docs/architecture/Registration_Migration_Plan.md`).

**Concepts Owned:**
- All scalar and Value Object properties of: Beneficiary, Household, HouseholdMember, Need, Claim, Registrant, Situation, SupportIntervention, Case, Lead, VolunteerReview
- Composite Value Object rows: `contact_point`, `location`, `income`, `treatment_plan` (flagged `future_entity_candidate`), `cost_estimate`, `requested_amount`, `non_resident_guardian`

**Relationships Owned:** None. Structural relationships (including the ADR-023 `guardian_of` role relationship) are in `relationships.yaml`.

**Maturity:** Mature and detailed. The most comprehensive file in the knowledge layer.

**Known Gaps:**
- `functional_capacity` on Beneficiary and HouseholdMember references shared taxonomy correctly but no inference rule operates on it. The attribute is fully defined but dormant.
- Need.treatment_plan has a `plan_known` field but no model of what to do when it is false beyond flagging a gap. The absence of a care pathway for a high-severity need should escalate severity classification, but no rule encodes this.

**Overlap / Conflicts:** None.

**Sibling canonical files (also part of this migration):** `registration/ontology/semantic-constraints.yaml`
(target-neutral structural constraints, e.g. `beneficiary_age_validation`) and
`registration/ontology/lifecycle-constraints.yaml` (placeholder — no lifecycle semantics
authored yet). `registration/reasoning/evidence-rules.yaml` now holds the claim-evidence
matrix relocated out of `evidence.yaml` per Migration Plan Decision D3.

---

### registration/ontology/relationships.yaml

**Purpose:** Defines the structural relationships between registration domain entities with cardinality and closure rules.

**Concepts Owned:**
- All relationships between: Registrant, Case, Beneficiary, Household, HouseholdMember, Situation, Need, Claim, Evidence, SupportIntervention, VerificationBrief, Lead, VolunteerReview

**Maturity:** Mature. The one-to-one registrant-to-case cardinality is intentional and correct.

**Known Gaps:**
- The `need_concerns_member` relationship is declared as `zero_to_one` with `required: false` and a note that it becomes required for medical, education, and therapeutic nutrition needs. This conditional requirement is not enforced in the relationships file itself — it is declared as a note. The enforcement lives in data-properties.yaml (required_when) and gap-detection-rules.yaml. This cross-file dependency should be explicitly documented.

**Overlap / Conflicts:** VerificationBrief appears in this file's relationships but is explicitly a projection, not an entity. The file correctly notes this. No conflict.

---

### registration/reasoning/inference-rules.yaml

**Purpose:** Forward-chaining inference rules allowing the AI to anticipate likely gaps and needs before they are explicitly stated.

**Concepts Owned:**
- Inference rules by trigger: bereavement → economic, injury → livelihood, displacement → shelter and documentation, displacement → psychosocial, economic crisis + children → education, minor without guardian → safeguarding, domestic violence → safety, illness onset → medical, high dependent load → multi-need

**Maturity:** Good for single-trigger inference. Insufficient for compound situations.

**Known Gaps:**
- No compound inference rules. When bereavement AND displacement co-occur, the compounded vulnerability is not modelled.
- `functional_capacity: dependent` on a beneficiary produces no inference. An inference rule connecting dependent functional capacity to caregiver-burden need and household resilience reduction is absent.
- Gender-specific risk inference is absent. An adolescent female in a financially distressed household should trigger an early marriage risk flag. No such rule exists.
- Lifecycle-stage-aware inference is absent. An infant in a food-insecure household should trigger a developmental malnutrition risk flag distinct from the household food need. No such rule exists.
- All rules are reactive (when X is stated, infer Y). No proactive rules exist (given profile attributes, flag Z before stated).

**Overlap / Conflicts:** Inference rules operate on the same entities and attributes defined in ontology/data-properties.yaml. No ownership conflict. Reasoning does not own the concepts it reasons about — correct.

---

### registration/reasoning/severity-rules.yaml

**Purpose:** Deterministic rules for classifying need severity by category. Provides a consistent basis for severity assessment that volunteers can trust.

**Concepts Owned:**
- Severity classification conditions per need category (food, medical, shelter, education, livelihood, psychosocial)

**Maturity:** Adequate. Creates consistency where severity would otherwise be arbitrary.

**Known Gaps:**
- Medical severity relies on registrant-reported information. There is no flag for "severity classification based on registrant report only — requires clinical review." This creates false precision.
- Treatment plan absence is not incorporated into medical severity rules. A critical-presenting medical need with no care pathway should amplify severity, not be assessed as a separate medium-priority gap.
- Education severity has no model of examination year proximity. Dropout risk in a terminal examination year is categorically more severe than dropout in a non-examination year.

**Overlap / Conflicts:** None.

---

### registration/reasoning/case-coherence-rules.yaml

**Purpose:** Rules for assessing whether a case is internally consistent beyond gap detection. A case can have no blocking gaps and still fail coherence.

**Concepts Owned:**
- Coherence rules: situation_need_alignment, severity_timeline_alignment, household_size_member_count_alignment, minor_guardian_coherence, proxy_claim_basis_coherence, support_intervention_need_alignment

**Maturity:** Mature.

**Known Gaps:**
- No coherence rule for compound situations. Two situations with overlapping affected_domains but incompatible trajectories (one structural, one acute) should trigger a review to confirm they are genuinely independent.

**Overlap / Conflicts:** None.

---

### registration/reasoning/gap-detection-rules.yaml

**Purpose:** Inference rules for detecting gaps during registration. Detection conditions — when true, the corresponding gap type is present.

**Concepts Owned:**
- Detection conditions for all gap types declared in gaps/gap-types.yaml

**Maturity:** Mature.

**Known Gaps:**
- `treatment_plan_gap` is classified as `blocking: false` with `severity: medium` regardless of the severity of the underlying medical need. A medical need classified as critical with no treatment plan should produce a blocking gap or escalate to critical severity. The current rule is too coarse.
- No gap type for compound situation severity (multiple simultaneous high-severity situations). This is a detection void.

**Overlap / Conflicts:** Correctly references gap-types.yaml for type definitions. Gap types are owned there; detection logic is owned here. Clean separation.

---

### registration/gaps/gap-types.yaml

**Purpose:** Defines the gap type vocabulary with severity classification.

**Concepts Owned:**
- Gap type definitions: safety_gap, guardian_gap, entity_gap, situation_need_traceability_gap, household_gap, severity_gap, duration_gap, contact_gap, location_gap, consistency_gap, evidence_gap, treatment_plan_gap, claim_gap, support_intervention_gap

**Maturity:** Mature.

**Known Gaps:** None significant. Well-scoped.

**Overlap / Conflicts:** None.

---

### registration/questioning/questioning-strategy.yaml

**Purpose:** Defines the principles and sequencing rules governing how the AI conducts the registration conversation.

**Concepts Owned:**
- Core questioning principles (trust_before_disclosure, one_gap_at_a_time, do_not_repeat_verbatim, inference_before_question, challenge_gently, sensitive_topic_protocol)
- Conversation phases 1–8
- Sensitive topic rules (domestic_violence, minor_without_guardian, psychosocial_risk_to_self, legal_status)

**Maturity:** Mature.

**Known Gaps:**
- Phase sequencing assumes a relatively cooperative registrant with a single primary situation. No alternative sequencing for crisis situations (registrant is in acute distress and cannot follow structured conversation), for very low-literacy registrants, or for situations where the registrant reveals information out of phase order.
- Sensitive topic rules do not include elder abuse or child exploitation beyond the guardian gap. Protection domain sensitivity handling is absent.

**Overlap / Conflicts:** None.

---

### registration/questioning/question-templates.yaml

**Purpose:** Reusable question templates for common registration scenarios, organised by gap type.

**Concepts Owned:**
- Question templates for gap types: household_gap, entity_gap, severity_gap, contact_gap, location_gap, safety_gap, guardian_gap, treatment_plan_gap, support_intervention_gap, registrant_relationship_gap, proxy_consent_gap, need_subtype_gap, referral_source_gap

**Maturity:** Mature.

**Known Gaps:** No templates for compound situations. No templates for lifecycle-stage-specific questioning (e.g., an infant in the household triggers different follow-up questions than a school-age child). Templates are need-category-neutral beyond the medical/food/shelter variants shown.

**Overlap / Conflicts:** None.

---

### registration/verification/verification-brief-projection.yaml

**Purpose:** Defines the structure of the document produced at case closure for volunteer field verification. A projection of the Case entity — not a stored entity.

**Concepts Owned:**
- Snapshot semantics and rationale
- Projection field mapping (all fields map to Case or its contained entities)
- Re-issuance responsibility declaration

**Maturity:** Mature. The projection model is architecturally correct.

**Known Gaps:** None at current maturity level. Re-issuance is accepted as a V1 gap.

**Overlap / Conflicts:** None.

---

### registration/verification/verification-requirements.yaml

**Purpose:** Defines how verification requirements are derived from claims at case closure. Derivation logic, not stored entities.

**Concepts Owned:**
- Derivation rules per claim type
- Priority classification (priority_1, priority_2, priority_3)
- Unverifiable claim handling

**Maturity:** Mature.

**Known Gaps:** None significant at current scope.

**Overlap / Conflicts:** None.

---

### registration/readiness/readiness-rules.yaml

**Purpose:** Defines the conditions that must be satisfied before a case can transition to ready_for_verification. The integration point of the registration domain.

**Concepts Owned:**
- Layer 1: Blocking gap clearance conditions
- Layer 2: Coherence clearance (by reference to case-coherence-rules.yaml)
- Layer 3: Minimum entity quality conditions
- Status transition table
- On-hold conditions
- Lead submission readiness conditions

**Maturity:** Mature.

**Known Gaps:** None significant at current scope.

**Overlap / Conflicts:** None.

---

## NEEDS ASSESSMENT DOMAIN

---

### needs-assessment/needs_assessment_discovery_report.md

**Purpose:** Discovery architectural mapping for the Needs Assessment bounded context. Defines boundaries, semantic invariant rules, and justification.
**Concepts Owned:** N/A (Architecture document)
**Relationships Owned:** N/A
**Maturity:** Complete.

---

### needs-assessment/taxonomy.yaml

**Purpose:** Authoritative vocabulary for the Needs Assessment domain.
**Concepts Owned:** 
- assessment_depth
- assessment_urgency
- assessment_scope
- assessment_status
- assessment_methodology
- finding_confidence
- need_severity
**Relationships Owned:** None.
**Maturity:** Complete.
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### needs-assessment/ontology.yaml

**Purpose:** First-class semantic model of the Needs Assessment domain.
**Concepts Owned:** 
- Assessment
- AssessmentFinding
- IdentifiedNeed
**Relationships Owned:** 
- assesses, produces, belongs_to, synthesizes_into, synthesized_from, based_on_claim, based_on_verified_fact, affects, superseded_by
**Referenced Concepts:** Subject (Shared), HumanitarianSector (Shared), AssessmentTool (Shared), RegistrationClaim (Registration), VerificationFinding (Verification)
**Maturity:** Complete.
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### needs-assessment/needs_assessment_taxonomy_review.md

**Purpose:** Justification and architectural validation for the taxonomy decisions.
**Concepts Owned:** N/A
**Relationships Owned:** N/A
**Maturity:** Complete.

---

### needs-assessment/needs_assessment_ontology_review.md

**Purpose:** Justification and architectural validation for the ontology decisions.
**Concepts Owned:** N/A
**Relationships Owned:** N/A
**Maturity:** Complete.

---

## VERIFICATION OPERATIONS DOMAIN

---

### verification-operations/ontology/entities.yaml

**Purpose:** Defines the first-class entities owned by the Verification Operations domain. Verification Operations is responsible for producing verification knowledge from verification activities performed against registration outputs. Canonically migrated (Canonical_Ontology_Schema.md) — consolidates what was previously split between a pre-canonical core-ontology monolith (`verification-operations/verification-operations.yaml`, now retired) and this folder.

**Concepts Owned:**
- `verification_subject`
- `verification_activity`
- `field_observation`
- `verification_finding`
- `reverification_trigger`
- `human_review`
- `verification_assignment`

**Maturity:** Complete (Phase 4.0, canonical).

**Known Gaps / Notes:** None.

---

### verification-operations/ontology/data-properties.yaml

**Purpose:** Datatype and coded properties for each Verification Operations entity.
**Maturity:** Complete.

---

### verification-operations/ontology/relationships.yaml

**Purpose:** Structural relationships between verification entities, and semantic references to Registration, Case Management, Shared Ontology, Shared Risk, and Shared Time.
**Maturity:** Complete.

---

### verification-operations/ontology/semantic-constraints.yaml

**Purpose:** Target-neutral structural constraints (conditional-requirement facts already stated in the taxonomy layer's prose, e.g. could_not_complete_reason required when verification_status is could_not_complete).
**Maturity:** Complete.

---

### verification-operations/ontology/lifecycle-constraints.yaml

**Purpose:** Descriptive lifecycle semantics for verification_activity, verification_finding, human_review, and verification_assignment (status transition notes, indeterminate-confidence resolution, review-decision immutability).
**Maturity:** Complete.

---

### verification-operations/taxonomy/*.yaml

**Purpose:** Authoritative vocabularies for verification operations (escalation reasons, review decisions, verification confidence, findings, methods, status, triggers). Canonically migrated to the `schemes:`/`concepts:` shape (Canonical_Taxonomy_Schema.md).
**Maturity:** Complete.

---

### verification-operations/reasoning/*.yaml

**Purpose:** Rules for verification findings, confidence composition, contradictions, escalation, reverification, and completeness.
**Maturity:** Complete.

---

## COMMUNITY CONTEXT DOMAIN

---

**Purpose:** Models the geographic, infrastructural, environmental, and social fabric
a household sits inside — settlement type, accessibility, hazards, seasonal events,
essential services, local organisations, livelihood patterns.

**Files:** `community-context/taxonomy/*.yaml` (12 files: accessibility, community-assets,
community-hazards, essential-services, geographic-hierarchy, infrastructure-types,
livelihood-patterns, local-organizations, physical-environment, seasonal-events,
settlement-types, transportation), plus a full `ontology/` module (`entities.yaml`,
`relationships.yaml`, `lifecycle-constraints.yaml`, `semantic-constraints.yaml`), a
governance document (`community-context-governance.md`), and a discovery report.

**Maturity:** Canonical — Phases 1–4 of `docs/architecture/Community_Context_Migration_Plan.md`
are complete (canonical four-key headers, full `ontology/` module including
`data-properties.yaml`, `schemes:`/`concepts:` taxonomy shape). Phase 5 (cross-domain CURIE
linking) remains blocked on a repository-wide manifest, same as Registration.

**Known Gaps:** Phase 5 cross-domain CURIE linking pending the repository-wide manifest.

**Overlap / Conflicts:** None identified against other domains; internal boundary
rules between its own taxonomy files are documented in
`community-context-governance.md`.

---

## OTHER DOMAINS

---

### case-management/taxonomy/

**Purpose:** Authoritative vocabulary for the Case Management domain.
**Concepts Owned:**
- `case_status`, `priority_level`, `referral_status`, `case_origin`, `closure_reason`, `case_plan_status`, `delegation_status`, `objective_status`, `referral_type`, `suspension_reason`
**Relationships Owned:** None.
**Maturity:** Complete (Level 1).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### case-management/ontology/

**Purpose:** Semantic model of Case Management orchestration concepts and their relationships.
**Concepts Owned:**
- `case`, `case_plan`, `referral` (entities); `follow_up`, `case_note` (nested Value Object fields on `case`)
**Relationships Owned:**
- `case_has_case_plan`, `case_has_referral`, `case_superseded_by_case`, `case_has_primary_subject`, `case_plan_references_need_assertion`, `referral_references_consent`, `case_has_lead_coordinator`, `case_has_statutory_owner`
**Maturity:** Complete (Level 1).
**Known Gaps:** `case_assignment` is named in discovery documents but not yet an authored entity.
**Overlap / Conflicts:** Correctly references Subject, BeneficiaryLifecycle, NeedsAssessment without redefining them.

---

### beneficiary-lifecycle/taxonomy/

**Purpose:** Classifies the concepts governing the macro-state of a beneficiary's engagement (lifecycle stages, transition reasons, exit and suspension reasons, and review triggers).
**Concepts Owned:** 
- `engagement_stage`
- `exit_reason`
- `suspension_reason`
- `review_trigger`
**Relationships Owned:** None.
**Maturity:** Complete (Level 1).
**Known Gaps:** None.
**Overlap / Conflicts:** None.

---

### beneficiary-lifecycle/ontology/

**Purpose:** Models the authoritative lifecycle record (`beneficiary_lifecycle`) and its event-sourced transitions (`lifecycle_transition`) for a Person or Household over time.
**Concepts Owned:**
- `beneficiary_lifecycle`
- `lifecycle_transition`
**Relationships Owned:**
- `tracks_journey_of`
- `has_transition_history`
- `followed_by`
- `triggered_by_registration_case`
- `triggered_by_verification_finding`
- `triggered_by_risk_characterization`
- `triggered_by_case_decision`
- `part_of_lifecycle`
**Maturity:** Complete (Level 1).
**Known Gaps:** None.
**Overlap / Conflicts:** References Registration, Shared Risk, Verification Operations, and Shared Human Model without redefining their concepts.

---

### volunteer-operations/ontology/, volunteer-operations/taxonomy/

**Status:** Foundational (Tier 1) canonical structure complete, per ADR-024. Operational/runtime layer (scheduling, dispatch, trust/performance scoring) deferred to Stage 9.
**Assessment:** Well-scoped. Correctly notes that volunteer full profile lives here, not in registration. `volunteer-operations/_placeholder.yaml` remains present alongside the canonical folders as a leftover from the pre-migration state.

---

### support-delivery/ontology/, support-delivery/taxonomy/

**Status:** Canonical `ontology/`+`taxonomy/` structure complete.
**Assessment:** Clean boundary between what is needed (registration) and how it is delivered (this domain).

---

### programs/ontology/, programs/taxonomy/

**Status:** Canonical `ontology/`+`taxonomy/` structure complete.
**Assessment:** Well-scoped. `programs/_placeholder.yaml` remains present alongside the canonical folders as a leftover from the pre-migration state.

---

### impact/ontology/, impact/taxonomy/

**Status:** Canonical `ontology/`+`taxonomy/` structure complete.
**Assessment:** Correctly notes that impact measurement requires longitudinal data from beneficiary lifecycle. `impact/_placeholder.yaml` remains present alongside the canonical folders as a leftover from the pre-migration state.

---

### consent-and-privacy/ontology.yaml

**Status:** Level 2 placeholder.
**Assessment:** Minimal placeholder declaration for Consent, required for Case Management to reference.

---

## ARCHITECTURE DOCUMENTS

---

### ARCHITECTURE.md

**Purpose:** Domain inventory, dependency rules, and maturity level definitions.
**Assessment:** Accurate and correctly maintained.
**Gap:** None. Shared human model domains (lifecycle, capability, dependency, family structure) introduced in Phase 2.4 are now listed.

---

### DECISIONS.md

**Purpose:** Architectural decision log. Records what was decided, why, and what was rejected.
**Assessment:** Well-maintained. 21 decisions recorded (including ADR-021 Case Lifecycle Handoff).
**Gap:** Does not yet record the decision to defer functional_capacity from reasoning rules, which is effectively an undocumented ADR (the attribute exists but is inert).

---

### GLOSSARY.md

**Purpose:** Ubiquitous language for the Khidmat domain.
**Assessment:** Accurate and useful. Covers core terms well. Reorganised in Phase 2.0 to include Human Model Terms, Risk and Vulnerability Terms, Outcome Terms, and Governance Terms sections aligned to ownership boundaries.
**Gap:** None at current phase. To be extended as new domains activate.

---

### AI_WORKFLOW.md

**Purpose:** Authoritative governance document describing how AI systems collaborate on the Khidmat Knowledge Layer. Defines AI roles, mandatory workflow, governance file responsibilities, governance update checklist, repository authority order, concept ownership rules, domain activation rules, current priority, and architectural principle.
**Assessment:** Complete. Produced in Phase 2.0.
**Gap:** None at current phase.

---

### AGENT_HANDOFF.md

**Purpose:** Quick-start onboarding briefing for any AI agent entering the project. Summarises current state, current phase, immediate objective, what must not be done, governance references, AI roles, and the current next step. Target read time under 2 minutes.
**Assessment:** Complete. Produced in Phase 2.0.
**Gap:** Must be updated when the current phase changes or a new agent handoff point is reached.

---

### ontology_authority_matrix.md

**Purpose:** Declares the authoritative owner for every concept in the
knowledge layer. Enforces single ownership per ADR-008. Each entry
records the concept ID, concept name, authoritative file, owner domain,
and reference constraint. Also records flagged boundary cases where
ownership alignment is pending.
**Assessment:** Structure established in Phase 2.0. Populated with nine
lifecycle stage concept ownership declarations. Four boundary cases
flagged for future alignment (functional_capacity, dependency types,
health condition labels, capability profile descriptions).
**Gap:** Must be populated as each new concept is introduced. Currently
covers only Shared Human Model — Lifecycle Stage concepts. All concepts
from future files must be declared here at time of creation.

---

### knowledge_layer_inventory.md

**Purpose:** Single source of truth for every file in the repository —
what it owns, what it owes, its maturity, and its known gaps.
**Assessment:** Complete as of Phase 3.0 entry. Covers all shared domain files,
registration domain files, placeholder domains, and architecture documents.
Shared Human Model section completed in Phase 2.4.
**Gap:** Must be updated when new files are created. Self-referential —
this file must include its own entry.

---

### ontology_completion_checklist.md

**Purpose:** Tracks progress across all taxonomy, ontology, reasoning,
and governance files. The single source of truth for what is done,
in progress, missing, and future.
**Assessment:** Complete as a tracking document. Updated throughout
Phase 2.4 as files were completed and stale entries were corrected.
**Gap:** Must be updated as items complete or move between states.
Status summary table at the bottom requires periodic reconciliation.

---

### knowledge_layer_roadmap.md

**Purpose:** Defines the dependency order for all stages of knowledge
layer development. Governs domain activation sequencing.
**Assessment:** Complete. Defines ten stages from Registration Completion
through Full Humanitarian Knowledge Graph. Dependency graph summary
and recommended file structure included.
**Gap:** Must be updated when a stage is marked substantially complete
or when a new domain is added to the planned sequence.

---

### docs/architecture/

**Purpose:** Houses the frozen, ratified structural contracts every domain's
`ontology/`+`taxonomy/` module must conform to (`Canonical_Ontology_Schema.md`,
`Canonical_Taxonomy_Schema.md`), the reusable migration process
(`Repository_Migration_Methodology.md`), the domain-specific migration plan for
registration (`Registration_Migration_Plan.md`) and its companion conformance
audit (`Registration_Domain_Audit.md`), and the architecture review documents that
motivated the freeze (`Repository_Architecture_Report.md`,
`Repository_Architecture_Improvement_Program.md`, `Registration_Content_Completion_Review.md`).
**Assessment:** Complete and in effect for the two schema contracts and the migration
methodology. Registration is the completed reference implementation under this
contract; Community Context is the next domain to migrate.
**Gap:** A repository-wide manifest (Finding R-1) and a ratified base IRI (Finding
C-2) — both preconditions for Phase 5 of any domain's migration — do not yet exist.