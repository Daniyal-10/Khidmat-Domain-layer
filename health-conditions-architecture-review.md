# Khidmat AI — Health Conditions Ontology Architecture Review

**Review Phase:** Phase 2.4 Pre-Implementation Architecture Review
**Authority:** Knowledge Layer Architect
**Date:** 2026
**Status:** ARCHITECTURE REVIEW ONLY — Implementation Not Authorized
**Governing ADRs:** ADR-007, ADR-008
**Prerequisite Files Reviewed:**
- `shared/human-model/lifecycle-stages.yaml` (v1.0, Phase 2.0)
- `shared/human-model/dependency.yaml` (v1.0, Phase 2.0)
- `shared/human-model/capabilities.yaml` (v1.0, Phase 2.2)
- `shared/human-model/family-structure.yaml` (v1.0, Phase 2.3)
- `shared/human-model/README.md` (architecture declaration)
- `ontology_authority_matrix.md` (FLAG-003)
- `knowledge_layer_roadmap.md` (Stage 2.4, Stage 3 dependency)
- `knowledge_layer_inventory.md` (health condition taxonomy gap)
- `ontology_completion_checklist.md` (missing health condition vocabulary)
- `registration/taxonomy/needs.yaml` (medical and therapeutic nutrition needs)
- `registration/ontology/attributes.yaml` (functional_capacity, treatment_plan)
- `shared/taxonomy/persons.yaml` (functional_capacity enum)
- `ARCHITECTURE.md`, `DECISIONS.md`, `GLOSSARY.md`

---

## 1. Executive Summary

The `health-conditions.yaml` file is the final component of the Shared Human Model and the gateway to the Risk Domain (Stage 3). Its design quality will determine whether downstream domains can perform lifecycle-aware, capability-informed, family-structured risk reasoning — or whether they must invent competing health concepts.

**Verdict:** The architecture is well-prepared. The four existing Shared Human Model files contain explicit forward-references and future-extension notes that define exactly what `health-conditions.yaml` must do and what it must not do. The primary risks are not technical — they are boundary-control risks. The file must resist three strong temptations: (1) becoming a medical encyclopedia rather than a humanitarian reasoning vocabulary, (2) absorbing capability or dependency definitions that belong elsewhere, and (3) embedding operational concepts (treatment plans, severity scores, interventions) that belong to downstream domains.

**Critical finding:** Three existing files (`capabilities.yaml`, `family-structure.yaml`, `lifecycle-stages.yaml`) already contain explicit contractual expectations of what `health-conditions.yaml` will provide. The ontology must satisfy these contracts without exceeding them. The registration domain's `functional_capacity` attribute is a dormant proto-health concept that requires explicit resolution as part of this phase.

**Recommendation:** Proceed with implementation under strict boundary control. The recommended ontology structure is a four-layer hierarchy (condition categories → condition families → specific conditions → condition attributes) with cross-reference relationships to capabilities, dependencies, lifecycle stages, and family roles. No risk scoring, no intervention logic, no treatment protocols.

---

## 2. Architecture Review

### 2.1 Integration Contract Analysis

The existing files have established an implicit integration contract with `health-conditions.yaml`. These are not vague aspirations — they are explicit forward references that define what the file must deliver.

**From `capabilities.yaml` (line 287–288, line 1340–1350):**
> "Health-conditions.yaml (not yet created) will own clinical cognitive condition vocabulary (dementia, intellectual disability, traumatic brain injury). This file defines the capability concept; that file will own the conditions that affect it."

**Contractual obligation:** `health-conditions.yaml` must define clinical conditions that map to capability impacts. It must not define the capabilities themselves.

**From `capabilities.yaml` future_extensions:**
> "When health-conditions.yaml is created, it should define how conditions such as severe acute malnutrition, chronic illness, physical disability, cognitive disability, and mental health conditions affect capability profiles."

**Contractual obligation:** The file must model condition-to-capability impact relationships, not capability levels.

**From `family-structure.yaml` (line 1557–1563):**
> "When health-conditions.yaml is created, health conditions should be able to reference family support roles. A chronic illness in the primary earner has different structural significance than the same illness in a financial dependent."

**Contractual obligation:** The file must enable family-role-aware condition reasoning. It must not define family roles.

**From `lifecycle-stages.yaml` (characteristic_vulnerabilities throughout):**
Descriptive references to SAM, MAM, chronic illness, cognitive decline, frailty, polypharmacy appear as examples of stage-characteristic vulnerabilities. FLAG-003 in `ontology_authority_matrix.md` records these as pending alignment.

**Contractual obligation:** The file must provide authoritative definitions for these conditions so that lifecycle-stages.yaml can transition from descriptive references to formal cross-references. The lifecycle file must not be modified to define conditions.

### 2.2 Downstream Consumer Requirements (Risk Domain Stage 3)

The Risk Domain is the primary downstream consumer of `health-conditions.yaml`. Its requirements are knowable from the roadmap and the existing reasoning gaps.

**Required inputs from `health-conditions.yaml`:**
- Condition severity/staging vocabulary (clinical, not operational) — e.g., SAM vs. MAM, mild vs. moderate vs. severe dementia
- Condition progression trajectory — improving, stable, deteriorating, episodic, relapsing-remitting
- Condition treatability classification — curable, manageable with treatment, manageable without treatment, untreatable, terminal
- Condition reversibility — temporary, permanent, partially reversible
- Condition-to-capability impact mapping — which capability domains are affected and at what level
- Condition-to-dependency trigger mapping — which dependency types a condition creates or intensifies
- Lifecycle-stage prevalence and manifestation patterns — how the same condition presents differently across stages
- Comorbidity patterns — which conditions frequently co-occur
- Environmental interaction patterns — which conditions are exacerbated by heat, cold, flooding, displacement stress

**What the Risk Domain will do with these inputs (not owned by `health-conditions.yaml`):**
- Compose vulnerability scores from capability gaps + environmental factors + household structure
- Generate risk trajectories (improving, stable, deteriorating, imminent)
- Assess household resilience impact
- Determine intervention urgency and prioritization
- Model predictive risk (e.g., "this household is likely to enter crisis within three months")

### 2.3 Registration Domain Integration Requirements

The registration domain already handles medical needs but lacks health condition vocabulary. The integration must be clean.

**Current state:**
- `registration/taxonomy/needs.yaml` defines medical need subtypes (surgical_treatment, ongoing_medication, rehabilitation, assistive_device, diagnostic_assessment) and therapeutic_nutrition (RUTF for SAM, fortified supplement for MAM)
- `registration/ontology/attributes.yaml` defines `treatment_plan` as a conditional object on medical needs
- `shared/taxonomy/persons.yaml` defines `functional_capacity` as a three-level enum (full, partial, dependent) — a proto-health/disability concept

**Required resolution:**
- `health-conditions.yaml` must not own need types, treatment plans, or medical need subtypes. These are operational concepts owned by registration and case management.
- `health-conditions.yaml` should provide the condition vocabulary that registration needs can reference. For example, a medical need with subtype `ongoing_medication` should be able to reference the specific condition (e.g., diabetes, hypertension) from `health-conditions.yaml`.
- `functional_capacity` in `shared/taxonomy/persons.yaml` must be explicitly retired or redirected to the capabilities model, as planned in FLAG-001. The three-level enum (`full, partial, dependent`) is superseded by the capabilities.yaml four-level scale plus the `independent_living` capability domain. `health-conditions.yaml` must not revive or depend on `functional_capacity`.

---

## 3. Ownership Boundary Analysis

### 3.1 Concepts `health-conditions.yaml` MUST Own

These are the authoritative concepts that no other file currently owns and that the Risk Domain requires:

| Concept Area | Examples | Why It Belongs Here |
|---|---|---|
| **Condition taxonomy** | diabetes, hypertension, tuberculosis, SAM, MAM, dementia, depression, traumatic brain injury, congenital heart disease, epilepsy, hearing impairment, visual impairment | No other file defines these. Registration references them descriptively. |
| **Condition classification** | Communicable vs. non-communicable; acute vs. chronic; nutritional; mental/behavioral; injury/trauma; congenital/developmental; sensory | No other file owns this classification hierarchy. |
| **Condition severity/staging** | SAM (severe acute malnutrition), MAM (moderate acute malnutrition); mild/moderate/severe dementia; controlled/uncontrolled diabetes | Clinical staging is a health condition property, not a need severity or risk score. |
| **Condition progression trajectory** | Improving, stable, deteriorating, episodic, relapsing-remitting, progressive, terminal | The natural history of the condition. Risk Domain uses this for trajectory modeling. |
| **Condition treatability** | Curable, manageable with treatment, manageable without treatment, untreatable, terminal | Determines whether absence of treatment is a gap or a structural reality. |
| **Condition reversibility** | Temporary, permanent, partially reversible | Affects whether capability reduction is expected to recover. |
| **Condition-to-capability impact** | "Diabetes affects physical_mobility (partial through neuropathy)" | Owned here as a relationship; capability definitions are owned by capabilities.yaml. |
| **Condition-to-dependency trigger** | "Severe physical disability creates physical_support dependency" | Owned here as a relationship; dependency types are owned by dependency.yaml. |
| **Lifecycle-stage condition manifestation** | "SAM in infant has developmental consequences distinct from adult malnutrition" | Owned here as a condition property; lifecycle stages are owned by lifecycle-stages.yaml. |
| **Comorbidity patterns** | "Diabetes + hypertension frequently co-occur"; "elderly + multiple comorbidities" | Owned here as condition-to-condition relationships. |
| **Environmental interaction** | "Heat exacerbates cardiovascular conditions"; "Flooding increases infection risk for immunocompromised" | Owned here as condition-context interactions. |

### 3.2 Concepts `health-conditions.yaml` MUST NOT Own

These concepts are explicitly owned by other files or future domains. Their presence in `health-conditions.yaml` would constitute an ownership violation under ADR-008.

| Concept | Current Owner | Violation if Added to health-conditions.yaml |
|---|---|---|
| **Capability definitions** | `capabilities.yaml` | Defining "what a person can do" duplicates capability domains. |
| **Capability level scale** | `capabilities.yaml` (full, functional, partial, minimal) | Redefining the scale creates ontology drift. |
| **Dependency type definitions** | `dependency.yaml` | Defining "caregiving dependency" or "physical_support dependency" duplicates dependency types. |
| **Lifecycle stage definitions** | `lifecycle-stages.yaml` | Defining "infant" or "elderly" as health stages is a fundamental category error. |
| **Family roles** | `family-structure.yaml` | Defining "primary caregiver" or "primary earner" duplicates kinship/support roles. |
| **Risk factors** | Risk Domain (Stage 3) | Defining "what makes this person vulnerable" is the Risk Domain's job. |
| **Vulnerability scoring** | Risk Domain (Stage 3) | Any numeric score, composite index, or ranking belongs downstream. |
| **Need severity** | `registration/reasoning/severity-rules.yaml` | Operational severity classification for volunteer action is not a health condition property. |
| **Intervention types** | Case Management / Programs | Defining "surgery," "medication," "therapy" as interventions duplicates support-interventions taxonomy. |
| **Treatment plans** | Registration (treatment_plan attribute) / Case Management | Treatment protocols, provider relationships, and care pathways are operational. |
| **Outcome indicators** | Outcome Indicator vocabulary (Stage 6) | Defining "improved HbA1c" or "reduced stunting" is an outcome measurement concern. |
| **Program classifications** | Programs Domain (Stage 9) | Health program types (e.g., "TB program") are operational. |
| **Diagnostic criteria** | Not owned by any Khidmat domain | Clinical diagnostic criteria (ICD-10 codes, DSM-5 criteria) are too granular and change too frequently for a humanitarian reasoning layer. |
| **Medication regimens** | Not owned by any Khidmat domain | Specific drug names, dosages, and schedules are operational clinical details. |
| **Surgical procedures** | Not owned by any Khidmat domain | Procedure names and protocols are operational. |

### 3.3 Potential Authority Conflicts with Existing Files

**Conflict 1: `functional_capacity` in `shared/taxonomy/persons.yaml`**
- **Severity:** HIGH — Active conflict with FLAG-001 resolution
- **Current state:** `persons.yaml` defines `functional_capacity` as `full, partial, dependent`. `capabilities.yaml` defines a four-level scale `full, functional, partial, minimal` and `independent_living` capability domain. `health-conditions.yaml` cannot reference `functional_capacity` without creating a three-way dependency mess.
- **Resolution:** `functional_capacity` must be retired from `persons.yaml` as part of this phase. The registration attributes that reference it (`beneficiary.functional_capacity`, `household_member.functional_capacity`) must be updated to reference the capabilities model. `health-conditions.yaml` must not reference `functional_capacity` at all; it should reference capability domains and levels from `capabilities.yaml`.
- **Action required:** Update `shared/taxonomy/persons.yaml`, `registration/ontology/attributes.yaml`, and record in `DECISIONS.md`.

**Conflict 2: Therapeutic nutrition in `registration/taxonomy/needs.yaml`**
- **Severity:** MEDIUM — Boundary risk
- **Current state:** `needs.yaml` defines `therapeutic_nutrition` as a food need subtype, referencing SAM and MAM descriptively. `health-conditions.yaml` will own SAM and MAM as condition definitions.
- **Risk:** `needs.yaml` could be tempted to define malnutrition staging. `health-conditions.yaml` could be tempted to define need types.
- **Resolution:** `health-conditions.yaml` owns the condition definitions (SAM, MAM). `needs.yaml` owns the need subtype (therapeutic_nutrition). The need references the condition. The condition does not reference the need.

**Conflict 3: `treatment_plan` in `registration/ontology/attributes.yaml`**
- **Severity:** LOW — Clarity risk only
- **Current state:** `attributes.yaml` defines a `treatment_plan` object on medical needs, with fields for `provider_name`, `plan_description`, `plan_known`.
- **Risk:** `health-conditions.yaml` might be tempted to define treatment plan attributes or care pathways.
- **Resolution:** `health-conditions.yaml` defines whether a condition is treatable (treatability attribute). `attributes.yaml` defines whether a treatment plan exists for a specific need (operational fact). The two are related but distinct. No cross-reference is required; the treatability attribute informs reasoning about whether `plan_known: false` is a significant gap.

**Conflict 4: `characteristic_vulnerabilities` in `lifecycle-stages.yaml`**
- **Severity:** LOW — Alignment risk
- **Current state:** `lifecycle-stages.yaml` uses health condition names descriptively (SAM, MAM, chronic illness, cognitive decline, frailty, polypharmacy) as examples of stage-characteristic vulnerabilities.
- **Risk:** After `health-conditions.yaml` is created, these descriptive references might diverge from the authoritative definitions.
- **Resolution:** Verify that all health condition names in `lifecycle-stages.yaml` align with `health-conditions.yaml` definitions. Update `lifecycle-stages.yaml` to add `condition_ref` cross-references where appropriate. No redefinition — only cross-referencing.

**Conflict 5: Medical need subtypes vs. condition classification**
- **Severity:** MEDIUM — Taxonomy boundary risk
- **Current state:** `needs.yaml` defines `assistive_device` as a medical need subtype. `health-conditions.yaml` will define conditions that create physical disability, which may lead to assistive device need.
- **Risk:** The boundary between "condition" and "consequence of condition that generates need" is subtle. A person has a spinal cord injury (condition) which causes paraplegia (capability impact) which generates a need for a wheelchair (intervention/need).
- **Resolution:** `health-conditions.yaml` stops at the condition and its capability impact. The need for an assistive device is a downstream need generated by the capability gap. It belongs to the need taxonomy, not the condition taxonomy.

---

## 4. Recommended Ontology Structure

### 4.1 Top-Level Structure

```yaml
# =============================================================================
# Khidmat Shared Human Model — Health Conditions Ontology
# =============================================================================
ontology_version: "1.0"
authority: "shared/human-model/"
owner_domain: "Shared Human Model"
status: "Phase 2.4 — Implementation"
# ---------------------------------------------------------------------------
# Purpose: Defines a structured vocabulary of health conditions relevant to
#          humanitarian reasoning. Models conditions, their clinical properties,
#          their effects on human functioning, and their interaction with
#          lifecycle stages and family roles.
# Scope:   This file answers "what condition is this, what does it do to
#          a person, and how does it interact with their developmental stage
#          and family context?"
#          It does not answer "what should the system do about it?"
# Governing ADRs: ADR-007, ADR-008
# ---------------------------------------------------------------------------

health_conditions:

  # PART 1: CONDITION CATEGORIES
  # High-level classification of conditions by domain and nature
  
  # PART 2: CONDITION FAMILIES
  # Groupings of related conditions with shared characteristics
  
  # PART 3: SPECIFIC CONDITIONS
  # Individual condition definitions with attributes
  
  # PART 4: CONDITION ATTRIBUTES
  # Properties that describe a condition instance (severity, stage, trajectory)
  
  # PART 5: CROSS-DOMAIN RELATIONSHIPS
  # How conditions interact with capabilities, dependencies, lifecycle stages,
  # and family roles — all by reference, not by definition
  
  # PART 6: DESIGN DECISIONS AND BOUNDARY NOTES
```

### 4.2 Major Condition Categories

Recommended seven top-level categories. This is not an exhaustive medical taxonomy — it is a humanitarian reasoning taxonomy. The categories must cover the conditions referenced in the existing files plus the conditions required for risk reasoning.

| Category | Scope | Examples from Existing Files | Reasoning Purpose |
|---|---|---|---|
| **Nutritional Conditions** | Malnutrition and micronutrient deficiencies | SAM, MAM, stunting, micronutrient deficiency | Lifecycle-aware malnutrition reasoning |
| **Communicable Diseases** | Infectious and parasitic diseases | Tuberculosis, HIV/AIDS, malaria, respiratory infections | Contagion risk, treatment access, public health |
| **Non-Communicable Diseases (NCDs)** | Chronic physical conditions | Diabetes, hypertension, cardiovascular disease, chronic kidney disease, asthma, epilepsy | Chronic disease burden, treatment dependency |
| **Mental and Behavioral Health Conditions** | Psychological and psychiatric conditions | Depression, anxiety, PTSD, psychosis, substance use disorders | Caregiver impact, social participation, decision-making |
| **Injury and Trauma** | Acute and chronic physical damage | Traumatic brain injury, spinal cord injury, fractures, burns | Capability impact, rehabilitation trajectory |
| **Congenital and Developmental Conditions** | Conditions present from birth or early development | Congenital heart disease, intellectual disability, cerebral palsy, developmental delay | Lifecycle-stage-specific support needs |
| **Sensory and Physical Disabilities** | Permanent or long-term sensory and physical impairments | Visual impairment, hearing impairment, physical disability, amputation | Capability impact, assistive device need, accessibility |

**Note:** These categories are not mutually exclusive. A person may have both an NCD and a mental health condition. The category structure is a reasoning aid, not a strict partition.

### 4.3 Required Entities

**Condition Family**
A grouping of related conditions that share clinical characteristics, treatment approaches, or capability impact patterns.
- Examples: "cardiovascular diseases" (family containing hypertension, coronary artery disease, heart failure, stroke); "neurocognitive disorders" (family containing dementia, traumatic brain injury, intellectual disability)
- Purpose: Enables reasoning about comorbidity clusters and shared risk factors without enumerating every condition.

**Specific Condition**
An individual health condition with a defined clinical reality.
- Required fields: `id`, `name`, `category`, `description`, `typical_onset_pattern`, `typical_progression`, `treatability`, `reversibility`
- Optional fields: `body_systems_affected`, `common_comorbidities`, `lifecycle_stage_prevalence`, `environmental_interactions`
- Cross-reference fields: `affected_capability_domains` (references capabilities.yaml), `triggered_dependency_types` (references dependency.yaml), `characteristic_lifecycle_manifestations` (references lifecycle-stages.yaml)

**Condition Instance (not an entity, but a profile)**
A person's actual condition at a point in time. This is not owned by `health-conditions.yaml` — it is owned by the Beneficiary Lifecycle domain or the registration domain. `health-conditions.yaml` provides the vocabulary that describes it.
- The condition instance would have: `condition_ref` (to health-conditions.yaml), `severity/stage`, `onset_date`, `treatment_status`, `current_impact_on_capabilities` (derived from capabilities.yaml levels)

### 4.4 Required Attributes per Condition

| Attribute | Type | Purpose | Example |
|---|---|---|---|
| `id` | string | Canonical identifier | `diabetes_mellitus_type_2` |
| `name` | string | Human-readable name | "Diabetes Mellitus, Type 2" |
| `category` | enum | Top-level category | `non_communicable_disease` |
| `family` | string | Condition family | `metabolic_disorders` |
| `description` | text | Humanitarian-context description | "A chronic metabolic condition..." |
| `body_systems_affected` | list | Physiological domains | `[endocrine, cardiovascular, renal, neurological]` |
| `typical_onset_pattern` | enum | When it usually appears | `adulthood`, `older_adulthood`, `any_age` |
| `typical_progression` | enum | Natural history | `progressive`, `stable_if_managed`, `episodic`, `relapsing_remitting` |
| `treatability` | enum | Treatment potential | `manageable_with_treatment`, `manageable_without_treatment`, `curable`, `unpreventable`, `terminal` |
| `reversibility` | enum | Can it be undone? | `irreversible`, `partially_reversible`, `reversible_with_treatment`, `reversible_spontaneously` |
| `fatal_if_untreated` | boolean | Mortality risk without care | `true` for tuberculosis, `false` for controlled hypertension |
| `disability_potential` | enum | Likelihood of causing permanent disability | `high`, `moderate`, `low`, `none` |
| `caregiver_burden_level` | enum | Demand on family caregivers | `high` (dementia, quadriplegia), `moderate` (diabetes), `low` (controlled hypertension) |
| `affected_capability_domains` | list of references | Which capabilities it may reduce | `[physical_mobility, cognitive_functioning, independent_living]` |
| `capability_impact_mechanism` | text | How it affects capabilities | "Peripheral neuropathy reduces sensation and mobility..." |
| `triggered_dependency_types` | list of references | Which dependencies it may create | `[physical_support, caregiving, financial]` |
| `characteristic_lifecycle_manifestations` | list of objects | How it differs by stage | See section 4.5 |
| `common_comorbidities` | list of references | Conditions that frequently co-occur | `[hypertension, cardiovascular_disease, chronic_kidney_disease]` |
| `environmental_interactions` | list of objects | Context factors that worsen it | `[{factor: extreme_heat, effect: exacerbates}, {factor: flooding, effect: increases_infection_risk}]` |
| `underdisclosure_risk` | enum | Likelihood of being hidden | `high` (mental health, STIs), `moderate` (chronic disease), `low` (visible disability) |
| `registration_relevance` | enum | Why it matters for Khidmat | `direct_need`, `capability_impact`, `caregiver_burden`, `family_cascade`, `all` |

### 4.5 Relationship Patterns

**Pattern 1: Condition → Capability Impact**
```yaml
affected_capability_domains:
  - domain_ref: capabilities.yaml#physical_mobility
    typical_impact_level: partial        # Most people with this condition
    impact_mechanism: >
      Peripheral neuropathy and vascular disease reduce sensation,
      proprioception, and wound healing in lower limbs.
    reversible_with_treatment: partial
    note: >
      Impact is highly variable with glycemic control. Well-controlled
      diabetes may have minimal mobility impact; poorly controlled
      diabetes may lead to amputation.
```

**Pattern 2: Condition → Dependency Trigger**
```yaml
triggered_dependency_types:
  - dependency_ref: dependency.yaml#physical_support
    trigger_condition: >
      When peripheral neuropathy or visual impairment from diabetic
      retinopathy reduces safe independent mobility.
    typically_temporary: false
    note: >
      Physical support dependency may be partial (assistance with
      some outdoor tasks) or total (full mobility assistance).
```

**Pattern 3: Condition → Lifecycle Stage Manifestation**
```yaml
characteristic_lifecycle_manifestations:
  - stage_ref: lifecycle-stages.yaml#elderly
    manifestation: >
      Elderly persons with diabetes frequently have multiple comorbidities
      (hypertension, cardiovascular disease, chronic kidney disease) that
      compound the management burden. Polypharmacy is common. Cognitive
      decline may reduce medication adherence. The combination of diabetes,
      reduced mobility, and cognitive change creates a high-risk profile
      for acute complications (hypoglycemia, hyperglycemic crisis, foot ulcers).
    specific_vulnerability: polypharmacy_and_cognitive_decline_interaction
```

**Pattern 4: Condition → Family Role Impact**
```yaml
family_role_impact:
  - role_ref: family-structure.yaml#support_roles.primary_earner
    impact_description: >
      A primary earner with diabetes faces intermittent incapacity
      during hypoglycemic episodes or hospitalization for complications.
      The condition is usually compatible with continued employment but
      requires workplace accommodation and healthcare access.
    structural_significance: moderate    # Not immediately catastrophic but creates chronic pressure
  - role_ref: family-structure.yaml#support_roles.primary_caregiver
    impact_description: >
      A primary caregiver with diabetes must manage their own condition
      while caregiving. Hypoglycemia can incapacitate the caregiver
      suddenly, creating a safety risk for dependents. The dual burden
      of self-management and caregiving is a known stressor.
    structural_significance: high       # Directly affects dependent safety
```

**Pattern 5: Comorbidity → Compounding Effect**
```yaml
common_comorbidities:
  - condition_ref: health-conditions.yaml#hypertension
    comorbidity_pattern: frequent
    compounding_effect: >
      Diabetes and hypertension together accelerate cardiovascular
      and renal damage. The management burden is more than additive —
      each condition worsens the other. Medication interactions increase
      polypharmacy risk. The combination significantly increases the
      likelihood of stroke, heart attack, and kidney failure.
```

### 4.6 Classification Hierarchy

```
Health Condition
├── Category (7 top-level)
│   ├── Nutritional Conditions
│   │   ├── Acute Malnutrition
│   │   │   ├── SAM (severe acute malnutrition)
│   │   │   └── MAM (moderate acute malnutrition)
│   │   ├── Chronic Malnutrition / Stunting
│   │   └── Micronutrient Deficiencies
│   │       ├── Iron deficiency anemia
│   │       ├── Vitamin A deficiency
│   │       └── Iodine deficiency
│   ├── Communicable Diseases
│   │   ├── Respiratory Infections
│   │   ├── Tuberculosis
│   │   ├── HIV/AIDS
│   │   ├── Malaria
│   │   ├── Hepatitis
│   │   └── Diarrheal Diseases
│   ├── Non-Communicable Diseases
│   │   ├── Cardiovascular Diseases
│   │   │   ├── Hypertension
│   │   │   ├── Coronary Artery Disease
│   │   │   ├── Heart Failure
│   │   │   └── Stroke
│   │   ├── Metabolic Disorders
│   │   │   └── Diabetes Mellitus (Type 1 and Type 2)
│   │   ├── Respiratory Conditions
│   │   │   └── Asthma / COPD
│   │   ├── Renal Conditions
│   │   │   └── Chronic Kidney Disease
│   │   ├── Neurological Conditions
│   │   │   └── Epilepsy
│   │   └── Cancer (selected common types relevant to humanitarian contexts)
│   ├── Mental and Behavioral Health Conditions
│   │   ├── Depressive Disorders
│   │   ├── Anxiety Disorders
│   │   ├── Trauma-Related Disorders (PTSD, acute stress)
│   │   ├── Psychotic Disorders
│   │   ├── Substance Use Disorders
│   │   └── Developmental Behavioral Conditions
│   ├── Injury and Trauma
│   │   ├── Traumatic Brain Injury
│   │   ├── Spinal Cord Injury
│   │   ├── Fractures and Orthopedic Trauma
│   │   ├── Burns
│   │   └── Amputation
│   ├── Congenital and Developmental Conditions
│   │   ├── Congenital Heart Disease
│   │   ├── Intellectual Disability
│   │   ├── Cerebral Palsy
│   │   ├── Developmental Delay
│   │   └── Cleft Lip/Palate
│   └── Sensory and Physical Disabilities
│       ├── Visual Impairment
│       ├── Hearing Impairment
│       ├── Physical Disability (lower limb)
│       ├── Physical Disability (upper limb)
│       └── Multiple Disabilities
```

**Important constraint:** This hierarchy is not intended to be exhaustive. It is intended to cover the conditions explicitly referenced in existing files plus the conditions required for humanitarian risk reasoning. It should be extensible without restructuring.

---

## 5. Risks and Concerns

### 5.1 Ontology Drift Risks

**Risk 1: Medical Encyclopedia Drift**
- **Description:** The file could accumulate excessive clinical detail — ICD-10 codes, diagnostic criteria, medication lists, treatment protocols — in an attempt to be "comprehensive."
- **Impact:** Bloated file that is difficult to maintain, requires medical expertise to update, and drifts from humanitarian reasoning into clinical practice.
- **Mitigation:** Enforce the "humanitarian reasoning relevance" filter. Every condition must be justified by a registration need, a capability impact, a dependency trigger, or a family cascade. Purely clinical conditions with no humanitarian reasoning consequence should be excluded.
- **Warning sign:** If the file exceeds 2000 lines or contains medication names, it has drifted.

**Risk 2: Capability Redefinition Drift**
- **Description:** In describing how conditions affect people, the file might redefine capability concepts (e.g., "a person with this condition has reduced mobility") instead of referencing capability domains.
- **Impact:** Silent duplication of capability definitions, creating two sources of truth for what "physical mobility" means.
- **Mitigation:** Strict use of `domain_ref` and `level_ref` from capabilities.yaml. No capability descriptions in this file. The only text allowed is the *mechanism* of impact (how the condition affects the capability), not the capability definition itself.
- **Warning sign:** Any paragraph that could be copied into capabilities.yaml is a drift signal.

**Risk 3: Lifecycle Stage Re-definition Drift**
- **Description:** The file might define "childhood diabetes" or "geriatric diabetes" as distinct concepts, effectively redefining lifecycle boundaries within the health domain.
- **Impact:** Lifecycle stage definitions become fragmented across files. The lifecycle model loses its authority.
- **Mitigation:** Lifecycle associations must use `stage_ref` to lifecycle-stages.yaml. The file describes how a condition *manifests* at a stage, not what the stage *is*. No age boundaries in this file.
- **Warning sign:** Any condition definition that contains age ranges.

**Risk 4: Risk Factor Absorption Drift**
- **Description:** The file might define "high-risk diabetes" or "vulnerable diabetes profile" as condition attributes, effectively doing the Risk Domain's work.
- **Impact:** Risk factors are defined in the wrong place. The Risk Domain cannot compose its own models because condition definitions pre-judge the risk composition.
- **Mitigation:** The file defines clinical properties (severity, progression, treatability). The Risk Domain defines risk composition. No risk scores, no vulnerability labels, no "high risk" / "low risk" classification in this file.
- **Warning sign:** Any attribute that sounds like a risk assessment.

### 5.2 Ownership Violations

**Violation 1: Treatment Plan Ownership**
- **Likelihood:** HIGH
- **Trigger:** The registration domain already has a `treatment_plan` attribute. It is natural to extend condition definitions with "recommended treatment" or "typical treatment plan."
- **Consequence:** Treatment logic belongs to case management and clinical domains. Embedding it in the Shared Human Model creates an operational dependency on a model that should be stable.
- **Prevention:** Explicitly exclude treatment_plan, medication regimen, and clinical protocol concepts from the design. Record this exclusion in the file's boundary notes.

**Violation 2: Severity Score Ownership**
- **Likelihood:** MEDIUM
- **Trigger:** Need severity is already modeled in registration. It is tempting to define "condition severity" in a way that pre-computes need severity.
- **Consequence:** Need severity becomes coupled to condition definitions. A person with "severe diabetes" would automatically get a critical need, bypassing the reasoning layer.
- **Prevention:** Clinical severity/staging (e.g., SAM vs. MAM, mild vs. severe dementia) is a condition attribute. Operational need severity (critical, high, medium, low) is a registration/case-management concept. The two are not the same and must not be conflated. The file may define clinical staging; it must not define operational severity.

**Violation 3: Intervention Eligibility Ownership**
- **Likelihood:** MEDIUM
- **Trigger:** The file might define "this condition qualifies for X intervention" as a condition attribute.
- **Consequence:** Intervention eligibility belongs to case management. Embedding it in the human model makes the model operational and unstable.
- **Prevention:** The file may define condition properties that *inform* intervention eligibility (e.g., treatability, reversibility). It must not define eligibility rules.

### 5.3 Hidden Duplication

**Hidden Duplication 1: Disability vs. Condition**
- **Location:** `capabilities.yaml` defines capability domains including `physical_mobility`, `cognitive_functioning`. `health-conditions.yaml` will define conditions that cause disability. The registration domain has `functional_capacity` (full, partial, dependent).
- **Risk:** Three overlapping concepts: disability as capability reduction, disability as health condition, disability as functional capacity enum. The registrant might be described as having "physical disability" (condition), "minimal physical mobility" (capability), and "dependent functional capacity" (registration attribute) simultaneously.
- **Resolution:** The `functional_capacity` enum must be retired (FLAG-001). After that, the distinction is clear: `health-conditions.yaml` owns the condition (e.g., spinal cord injury), `capabilities.yaml` owns the capability level (minimal physical mobility), and the registration domain records the assessed capability level for the case.

**Hidden Duplication 2: Caregiver Burden vs. Dependency**
- **Location:** `dependency.yaml` defines `caregiving` dependency. `family-structure.yaml` defines `caregiver_burden_level` as a situational attribute. `health-conditions.yaml` will define `caregiver_burden_level` as a condition attribute.
- **Risk:** Caregiver burden is defined in two places: as a family structure attribute (current situation) and as a health condition property (intrinsic to the condition). These are different concepts but share a name.
- **Resolution:** Rename the condition attribute to `intrinsic_caregiver_demand` or `condition_caregiver_intensity` to distinguish it from the situational `caregiver_burden_level` in family-structure.yaml. The condition attribute describes the typical demand the condition places on caregivers. The family attribute describes the actual burden experienced by the current caregiver.

**Hidden Duplication 3: Malnutrition in Two Places**
- **Location:** `registration/taxonomy/needs.yaml` defines `therapeutic_nutrition` as a food need subtype. `health-conditions.yaml` will define SAM and MAM as nutritional conditions. `lifecycle-stages.yaml` references SAM and MAM in infant vulnerabilities.
- **Risk:** SAM might be treated as a need, a condition, and a vulnerability simultaneously.
- **Resolution:** SAM is a condition (health-conditions.yaml). A person with SAM has a need for therapeutic nutrition (needs.yaml). The infant stage is vulnerable to SAM (lifecycle-stages.yaml). Each file owns one aspect. No file owns more than one.

### 5.4 Future Maintenance Problems

**Problem 1: Clinical Knowledge Obsolescence**
- **Description:** Medical knowledge changes. Diabetes management in 2026 is different from 2015. If `health-conditions.yaml` contains detailed clinical descriptions, it will require expert medical review to maintain.
- **Mitigation:** Keep clinical descriptions at a level of generality that is stable across decades. Focus on the humanitarian consequences (capability impact, dependency creation, caregiver burden) rather than the clinical mechanisms. The clinical description should be accurate but not cutting-edge.

**Problem 2: Geographic Specificity**
- **Description:** Conditions have different prevalence, manifestation, and treatment access in different regions. A file that assumes South Asian epidemiology may not transfer to other contexts.
- **Mitigation:** Include geographic context notes where relevant (e.g., "TB is endemic in South Asia; screening and treatment access are public health priorities in this context"). But do not embed geographic assumptions into condition definitions. Keep definitions general enough for multi-context use.

**Problem 3: Condition Count Inflation**
- **Description:** As the system encounters new conditions in registration, there will be pressure to add every condition mentioned by registrants.
- **Mitigation:** Define a threshold for inclusion: a condition must be (a) referenced by an existing file, (b) required for risk reasoning, or (c) common enough in the target population to warrant formal modeling. Rare or esoteric conditions can be handled as "other_condition" with free text description, rather than expanding the taxonomy indefinitely.

### 5.5 Concepts That Appear Attractive but Should Not Be Added

| Concept | Why It Appears Attractive | Why It Must Not Be Added |
|---|---|---|
| **ICD-10 codes** | Standard medical classification; enables interoperability with health systems | Too granular; changes between revisions; humanitarian reasoning does not need this precision; adds maintenance burden |
| **Medication lists** | "A person with diabetes needs insulin"; medications are part of condition management | Medication regimens are operational and individualized. The file would have to track drug availability, generic vs. brand, dosing — all operational. |
| **Treatment protocols** | "First-line treatment for TB is DOTS" | Treatment protocols are owned by health programs and case management. They change with WHO guidelines. |
| **Diagnostic criteria** | "Diabetes is diagnosed by HbA1c ≥ 6.5%" | Diagnostic criteria are clinical tools for healthcare providers. Khidmat registrants are not diagnosed during registration. The file models conditions, not diagnostic thresholds. |
| **Condition-specific risk scores** | "Diabetes risk score = 7.3" | Any risk score belongs to the Risk Domain. The condition file provides the inputs; the Risk Domain computes the score. |
| **Prognosis predictions** | "Life expectancy with Stage 4 CKD is 3-5 years" | Prognosis is highly individual and context-dependent. The file may define progression trajectories; it must not predict individual outcomes. |
| **Intervention contraindications** | "Surgery is contraindicated for uncontrolled diabetes" | Contraindications belong to the intervention taxonomy and case management domain. |
| **Mental health severity scales** | PHQ-9, GAD-7, etc. | Clinical screening tools are operational instruments. The file defines the conditions (depression, anxiety); the registration or case management domain may use screening tools if needed. |
| **Nutrition intervention protocols** | "RUTF dosage for SAM is 150-220 kcal/kg/day" | Operational detail. The need taxonomy references RUTF; the condition taxonomy defines SAM. The dosage is a program operational detail. |
| **Disability certification criteria** | "Qualifies for disability benefits if..." | Legal and administrative criteria vary by jurisdiction. The file models the condition and its capability impact; certification is an operational/legal domain concern. |

---

## 6. Final Design Recommendation

### 6.1 Approved Ontology Design

**Structure:** Six-part YAML file

1. **Condition Categories** — Seven top-level categories with definitions and scope boundaries
2. **Condition Families** — Groupings of related conditions with shared characteristics (cardiovascular, neurocognitive, musculoskeletal, etc.)
3. **Specific Conditions** — Individual condition definitions with the attribute schema defined in section 4.4
4. **Condition Attributes Reference** — Formal definitions of the attribute vocabulary used in part 3 (treatability, reversibility, progression, etc.)
5. **Cross-Domain Relationship Patterns** — Templates for how conditions reference capabilities, dependencies, lifecycle stages, and family roles
6. **Boundary Notes and Anti-Patterns** — Explicit exclusions, warning signs, and future extension guidance

**Scope constraint:** Approximately 40–60 specific conditions should be defined in the initial version. This is sufficient to cover the conditions referenced in existing files and the most common conditions in humanitarian contexts. The taxonomy must be extensible — new conditions can be added without restructuring.

### 6.2 Integration Checklist for Implementation

Before `health-conditions.yaml` is considered complete, the following integration tasks must be performed:

- [ ] **FLAG-003 Resolution:** Verify all health condition names in `lifecycle-stages.yaml` align with `health-conditions.yaml` definitions. Update lifecycle-stages.yaml to add cross-references where appropriate.
- [ ] **FLAG-001 Resolution:** Retire `functional_capacity` from `shared/taxonomy/persons.yaml`. Update `registration/ontology/attributes.yaml` to reference capabilities.yaml instead. Record in `DECISIONS.md`.
- [ ] **Capabilities Integration:** Verify that `capabilities.yaml` future_extensions contract is satisfied. The condition-to-capability impact mappings must be present and must reference capabilities.yaml domains correctly.
- [ ] **Dependency Integration:** Verify that condition-to-dependency trigger mappings reference dependency.yaml types correctly.
- [ ] **Family Structure Integration:** Verify that `family-structure.yaml` future opportunity for health condition impact on family structure is satisfied. Condition-to-role impact mappings must be present.
- [ ] **Registration Integration:** Verify that `registration/taxonomy/needs.yaml` medical and therapeutic nutrition subtypes can reference `health-conditions.yaml` conditions. No redefinition in either file.
- [ ] **Ontology Authority Matrix Update:** Add all health condition concepts to `ontology_authority_matrix.md` with `health-conditions.yaml` as the authoritative file.
- [ ] **Glossary Update:** Add health condition terms to `GLOSSARY.md` under a new "Health Condition Terms" section.
- [ ] **Knowledge Layer Inventory Update:** Add the new file to `knowledge_layer_inventory.md` with full ownership declaration and gap assessment.
- [ ] **Completion Checklist Update:** Mark `health-conditions.yaml` as complete in `ontology_completion_checklist.md` and move the Capability Alignment Migration item to resolved.
- [ ] **Roadmap Update:** Mark Phase 2.4 as complete in `knowledge_layer_roadmap.md` and confirm Stage 3 (Risk Domain) prerequisites are satisfied.

### 6.3 Boundary Enforcement Rules

These rules must be included in the header comments of `health-conditions.yaml` and must be respected by all future editors:

1. **No capability definitions.** This file references `capabilities.yaml` by `domain_ref`. It does not define what physical mobility or cognitive functioning means.
2. **No dependency definitions.** This file references `dependency.yaml` by `dependency_type_ref`. It does not define what caregiving dependency or physical support dependency means.
3. **No lifecycle definitions.** This file references `lifecycle-stages.yaml` by `stage_ref`. It does not define what an infant or an elderly person is.
4. **No family role definitions.** This file references `family-structure.yaml` by `role_ref`. It does not define what a primary caregiver or primary earner is.
5. **No risk scores.** This file defines clinical properties (severity, progression, treatability). It does not define vulnerability, risk, or danger.
6. **No need severity.** This file defines clinical staging (SAM vs. MAM). It does not define operational need severity (critical, high, medium, low).
7. **No interventions.** This file defines conditions. It does not define what Khidmat should do about them.
8. **No treatment protocols.** This file defines whether a condition is treatable. It does not define the treatment.
9. **No diagnostic criteria.** This file defines conditions for humanitarian reasoning. It does not define clinical diagnostic thresholds.
10. **No outcome indicators.** This file defines the baseline. Outcome measurement belongs to Stage 6.

### 6.4 Risk Domain Readiness Confirmation

`health-conditions.yaml` will expose the following information to enable Risk Domain reasoning:

| Risk Domain Need | Information Exposed by health-conditions.yaml |
|---|---|
| Lifecycle-aware risk assessment | `characteristic_lifecycle_manifestations` — how conditions interact with developmental stages |
| Capability-informed risk assessment | `affected_capability_domains` — which capabilities are reduced and by what mechanism |
| Dependency chain risk assessment | `triggered_dependency_types` — which dependencies a condition creates |
| Family cascade risk assessment | `family_role_impact` — how conditions in key family roles propagate structurally |
| Household resilience assessment | `caregiver_burden_level` — intrinsic demand placed on family caregivers |
| Treatment access gap detection | `treatability` — whether absence of treatment is a manageable gap or a structural reality |
| Progressive deterioration flags | `typical_progression` — whether the condition is expected to worsen |
| Comorbidity compounding | `common_comorbidities` — which conditions frequently co-occur and compound |
| Environmental risk interaction | `environmental_interactions` — which conditions are worsened by environmental factors |
| Underdisclosure risk | `underdisclosure_risk` — which conditions are likely to be hidden at registration |

| Risk Domain Need | Information Deferred to Risk Domain |
|---|---|
| Vulnerability composite score | Computed from capability gaps + household structure + environmental factors |
| Risk trajectory prediction | Computed from condition progression + household events + community context |
| Intervention urgency | Computed from need severity + condition stage + treatment access + environmental timing |
| Household resilience score | Computed from family support network + financial reserves + capability distribution |
| Predictive risk flags | Computed from longitudinal data + seasonal calendar + aggregate patterns |
| Programmatic response triggers | Computed from case concentration + area vulnerability + resource availability |

### 6.5 Go/No-Go Decision

**GO — with boundary enforcement.**

The architecture is sound. The prerequisites are clear. The integration contracts from existing files are explicit and satisfiable. The primary risk is not technical failure but conceptual overreach. With the boundary enforcement rules in section 6.3, the file can be implemented safely.

The architecture review recommends proceeding to implementation under the following conditions:
1. The six-part structure defined in section 6.1 is followed.
2. The boundary enforcement rules in section 6.3 are included in the file header and respected.
3. The integration checklist in section 6.2 is completed before the file is marked final.
4. The `functional_capacity` retirement (FLAG-001) is completed as part of this phase.
5. The initial condition set is limited to 40–60 conditions, with a clear extensibility mechanism.

---

*End of Architecture Review*
