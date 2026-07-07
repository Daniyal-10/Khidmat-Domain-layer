# Khidmat Health Conditions Ontology — Governance and Documentation

**Authority:** Knowledge Layer Architect
**Source:** Extracted from `shared/human-model/taxonomy/health-conditions.yaml`
**Purpose:** Governance documentation, boundary notes, cross-domain patterns, and alignment contracts for the Health Conditions Ontology.

---

## Boundary Enforcement Rules

These rules govern what the Health Conditions Ontology may and may not define.

1. **No capability definitions.** This file references `capabilities.yaml` by `domain_ref`. It does not define what physical mobility or cognitive functioning means.
2. **No dependency definitions.** This file references `dependency.yaml` by `dependency_ref`. It does not define what caregiving or physical_support dependency means.
3. **No lifecycle definitions.** This file references `lifecycle-stages.yaml` by `stage_ref`. It does not define what an infant or an elderly person is.
4. **No family role definitions.** This file references `family-structure.yaml` by `role_ref`. It does not define what a primary caregiver or primary earner is.
5. **No risk scores.** This file defines clinical properties (severity, progression, treatability). It does not define vulnerability, risk, or danger.
6. **No need severity.** This file defines clinical staging (SAM vs. MAM). It does not define operational need severity (critical, high, medium, low).
7. **No interventions.** This file defines conditions. It does not define what Khidmat should do about them.
8. **No treatment protocols.** This file defines whether a condition is treatable. It does not define the treatment.
9. **No diagnostic criteria.** This file defines conditions for humanitarian reasoning. It does not define clinical diagnostic thresholds.
10. **No outcome indicators.** This file defines the baseline. Outcome measurement belongs to Stage 6.

---

## Cross-Domain Relationship Patterns

These patterns formalise how conditions reference other domain files.

### Pattern: Capability Impact

**Description:** How a condition affects a capability domain. This file references `capabilities.yaml` by `domain_ref`. The `impact_mechanism` describes how the condition affects the capability, not what the capability is.

**Required Fields:**
- `domain_ref`: "capabilities.yaml#{domain_id}"
- `typical_impact_level`: One of `full`, `functional`, `partial`, `minimal` (from capabilities.yaml)
- `impact_mechanism`: Text describing the mechanism of impact
- `reversible_with_treatment`: boolean or partial

**Boundary Note:** This file does not define capability levels or domains. It only describes how the condition affects the capability as defined in `capabilities.yaml`. No capability definition text belongs here.

### Pattern: Dependency Trigger

**Description:** How a condition creates or intensifies a dependency relationship. This file references `dependency.yaml` by `dependency_ref`. The `trigger_condition` describes when the dependency is activated by the condition.

**Required Fields:**
- `dependency_ref`: "dependency.yaml#{dependency_type_id}"
- `trigger_condition`: Text describing when the dependency is triggered
- `typically_temporary`: boolean

**Boundary Note:** This file does not define dependency types. It only describes the conditions under which a condition triggers a dependency as defined in `dependency.yaml`.

### Pattern: Lifecycle Manifestation

**Description:** How a condition manifests differently at different lifecycle stages. This file references `lifecycle-stages.yaml` by `stage_ref`. The `manifestation` describes the stage-specific presentation, not the stage itself.

**Required Fields:**
- `stage_ref`: "lifecycle-stages.yaml#{stage_id}"
- `manifestation`: Text describing the stage-specific presentation

**Boundary Note:** This file does not define lifecycle stages. It only describes how the condition presents at a stage as defined in `lifecycle-stages.yaml`. No age boundaries or stage definitions belong here.

### Pattern: Family Role Impact

**Description:** How a condition affects a person's capacity to fulfil a family support role. This file references `family-structure.yaml` by `role_ref`. The `impact_description` describes the effect on the role, not the role.

**Required Fields:**
- `role_ref`: "family-structure.yaml#support_roles.{role_id}"
- `impact_description`: Text describing the impact on the role

**Boundary Note:** This file does not define family support roles. It only describes how a condition affects a person's capacity to fulfil a role as defined in `family-structure.yaml`.

### Pattern: Comorbidity

**Description:** How a condition interacts with another condition. This file references other conditions in this file by `condition_ref`.

**Required Fields:**
- `condition_ref`: "health-conditions.yaml#{condition_id}"
- `comorbidity_pattern`: One of `frequent`, `occasional`, `rare`
- `compounding_effect`: Text describing the interaction effect

**Boundary Note:** Comorbidity patterns are clinical observations, not risk scores. The Risk Domain uses these patterns to assess composite risk.

### Pattern: Environmental Interaction

**Description:** How environmental factors affect the condition. This file defines condition-context interactions that inform risk reasoning.

**Required Fields:**
- `factor`: Environmental factor name
- `effect`: Text describing the interaction effect

**Boundary Note:** Environmental interactions are condition properties. The Risk Domain uses these to assess environmental risk amplification. This file does not define environmental risk scores.

---

## Boundary Notes and Anti-Patterns

### What This File Does NOT Own

- This file does not own capability definitions. It references `capabilities.yaml` by `domain_ref`. No capability level scale, no capability domain description, and no capability assessment guidance belongs in this file. If a paragraph could be copied into `capabilities.yaml`, it does not belong here.
- This file does not own dependency definitions. It references `dependency.yaml` by `dependency_ref`. No dependency type description, no dependency directionality, and no dependency characteristic belongs in this file.
- This file does not own lifecycle stage definitions. It references `lifecycle-stages.yaml` by `stage_ref`. No age boundaries, no stage descriptions, and no developmental milestone definitions belong in this file.
- This file does not own family role definitions. It references `family-structure.yaml` by `role_ref`. No kinship role, no support role, and no family relationship definition belongs in this file.
- This file does not define risk scores, vulnerability indices, or danger classifications. Clinical properties (severity, progression, treatability) are defined here. Risk composition is computed by the Risk Domain using these properties as inputs.
- This file does not define operational need severity. Clinical staging (SAM vs. MAM, mild vs. severe dementia) is a condition attribute. Operational need severity (critical, high, medium, low) belongs to the registration and case management domains.
- This file does not define interventions, treatments, or care protocols. Treatability describes whether a condition is amenable to intervention in principle. The specific intervention type, eligibility, and protocol belong to operational domains.
- This file does not define diagnostic criteria. It models conditions for humanitarian reasoning, not clinical diagnosis. No diagnostic thresholds, no test results, and no examination findings belong here.
- This file does not define outcome indicators. It defines the baseline condition. Measuring improvement, deterioration, or change belongs to the outcome indicator vocabulary and impact domain.
- This file does not include ICD-10 codes, DSM-5 criteria, or other formal medical classification systems. These are too granular and change too frequently for a humanitarian reasoning layer. The condition definitions are stable, general, and focused on humanitarian consequences.
- This file does not include medication names, dosages, or regimens. Medication information is operational, individualized, and changes with clinical guidelines. It belongs to case management and clinical records, not the shared human model.
- This file does not include surgical procedures, treatment protocols, or rehabilitation programs. These are operational details that belong to program and case management domains.
- Condition count is intentionally limited to approximately 40 conditions covering the most common and consequential conditions in humanitarian contexts. The taxonomy is extensible — new conditions can be added using the same schema without restructuring. Rare or esoteric conditions should be handled as "other_condition" with free text rather than expanding the taxonomy indefinitely.
- The `condition_caregiver_intensity` attribute is intentionally named to distinguish it from the situational `caregiver_burden_level` in `family-structure.yaml`. The condition attribute describes intrinsic demand; the family attribute describes actual experienced burden. Both are needed for complete reasoning but must not be conflated.
- Future extensions to this file should follow the same schema and boundary rules. Any new condition must justify its inclusion by registration relevance, capability impact, or family cascade significance. Conditions that are purely clinical without humanitarian reasoning consequence should be excluded.
- When the Risk Domain activates (Stage 3), it will consume this file as an input. The Risk Domain must not modify this file. If risk reasoning requires new condition attributes, those attributes should be added to the Risk Domain's own models, not to this file. This file remains the authoritative source for condition definitions; the Risk Domain is the authoritative source for risk composition.
- When the Beneficiary Lifecycle Domain activates (Stage 7), it will model condition trajectories over time. This file defines conditions at a point in time. The lifecycle domain will track how a person's condition instance changes across registrations. The condition definition remains stable; the instance changes.
- When the Community Context Domain activates (Stage 8), it will model environmental risk factors at the area level. This file defines condition-environment interactions at the individual level. The community domain will aggregate these interactions to assess area-level risk profiles. The condition definition remains the same; the community domain adds the aggregate layer.

---

## Alignment with Existing Shared Human Model Files

### Capabilities YAML Contract

**Contract Source:** `capabilities.yaml` future extensions

**Resolution:** This file defines clinical conditions (dementia, intellectual disability, traumatic brain injury, severe acute malnutrition, chronic illness, physical disability, cognitive disability, mental health conditions) and maps them to capability domains using the `affected_capability_domains` pattern. The capability domains themselves are defined in `capabilities.yaml` and referenced here by `domain_ref`. The capability level scale (`full`, `functional`, `partial`, `minimal`) is owned by `capabilities.yaml` and used here for `typical_impact_level`. No capability definitions are duplicated.

**Status:** Resolved

### Dependency YAML Contract

**Contract Source:** `dependency.yaml` cross-references and `family-structure.yaml` future opportunity

**Resolution:** This file defines `triggered_dependency_types` for each condition, referencing dependency types from `dependency.yaml` by `dependency_ref`. The `condition_caregiver_intensity` attribute is distinguished from the situational `caregiver_burden_level` in `family-structure.yaml`. No dependency types are redefined.

**Status:** Resolved

### Lifecycle Stages YAML Contract

**Contract Source:** `lifecycle-stages.yaml` characteristic_vulnerabilities and FLAG-003

**Resolution:** This file provides authoritative definitions for SAM, MAM, chronic illness, cognitive decline, frailty, and polypharmacy (as conditions or condition-related concepts). The `lifecycle-stages.yaml` file uses descriptive references to these concepts. Future alignment work should add `condition_ref` cross-references in `lifecycle-stages.yaml` where appropriate. No lifecycle stage definitions are redefined here.

**Status:** Resolved — pending `lifecycle-stages.yaml` cross-reference update

### Family Structure YAML Contract

**Contract Source:** `family-structure.yaml` future opportunity (line 1557)

**Resolution:** This file defines `family_role_impact` for each condition, referencing support roles from `family-structure.yaml` by `role_ref`. The `structural_significance` attribute (now removed from the ontology) indicated how a condition in a specific role affects household structure. No family roles are redefined here.

**Status:** Resolved — `structural_significance` removed from ontology per governance audit

### Persons YAML Functional Capacity

**Contract Source:** FLAG-001 in `ontology_authority_matrix.md`

**Resolution:** This file does not reference `functional_capacity` from `persons.yaml`. The `functional_capacity` enum (`full`, `partial`, `dependent`) is superseded by the capability level scale in `capabilities.yaml` and the `independent_living` capability domain. This file uses the four-level capability scale (`full`, `functional`, `partial`, `minimal`) from `capabilities.yaml` for all capability impact descriptions. The retirement of `functional_capacity` from `persons.yaml` is a separate governance task tracked in the integration checklist.

**Status:** Resolved — this file does not reference `functional_capacity`

---

## Future Extensions

### Concept: Condition Trajectory Over Time

**Belongs In:** Beneficiary Lifecycle Domain (Stage 7)

A person's condition instance changes over time — improving, worsening, resolving, or recurring. This file defines conditions at a point in time. The trajectory of change across time must be modelled by the beneficiary lifecycle domain. The capability profile at each registration is the point-in-time snapshot that the lifecycle domain tracks.

### Concept: Condition-Specific Risk Factor Derivation

**Belongs In:** `shared/risk/` (Stage 3, not yet active)

Capability gaps are not themselves risk factors, but they are inputs to risk factor assessment. A person with minimal physical mobility in a flood zone has a compounded risk that the capability model by itself cannot express. Risk factor derivation logic belongs in the risk domain and must reference this file's condition vocabulary.

### Concept: Intervention Eligibility Based on Condition

**Belongs In:** `registration/taxonomy/support-interventions.yaml` (Stage 1) and Case Management Domain (Stage 5)

Intervention types have condition-related eligibility conditions. A therapeutic nutrition intervention is appropriate for SAM but not for stunting. A rehabilitation intervention is appropriate for TBI but not for dementia. These conditions belong in the support intervention taxonomy and case management domain, not in the condition model.

### Concept: Geographic Condition Prevalence

**Belongs In:** Community Context Domain (Stage 8, not yet active)

The prevalence of specific conditions varies by geographic area due to environmental, genetic, and healthcare access factors. Area-level condition prevalence is a community context attribute, not a condition definition attribute. The condition definition is universal; the prevalence is local.

### Concept: Condition Instance Entity

**Belongs In:** `shared/ontology/entities.yaml` or Beneficiary Lifecycle Domain

A person's actual condition at a point in time (with severity, onset date, treatment status, current impact) is an instance entity, not a definition. This file provides the vocabulary for the `condition_ref`. The instance entity belongs in the shared ontology or the beneficiary lifecycle domain, depending on where persistent health records are modelled.

---

*Governance document extracted from `health-conditions.yaml` during Phase 2.4 remediation.*
*Remediation date: 2026-01-19*
*Authority: Knowledge Layer Architect*
