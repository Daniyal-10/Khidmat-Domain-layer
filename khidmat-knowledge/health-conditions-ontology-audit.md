# PHASE 2.4 — HEALTH CONDITIONS ONTOLOGY GOVERNANCE AUDIT

**Authority:** Knowledge Layer Architect  
**Scope:** `shared/human-model/health-conditions.yaml`  
**Reference Files Audited:**
- `shared/human-model/lifecycle-stages.yaml`
- `shared/human-model/dependency.yaml`
- `shared/human-model/capabilities.yaml`
- `shared/human-model/family-structure.yaml`
- `ontology_authority_matrix.md`
- `ontology_completion_checklist.md`
- `knowledge_layer_roadmap.md`

**Date:** 2026-01-19

---

## 1. EXECUTIVE SUMMARY

The `health-conditions.yaml` file is **NOT READY for acceptance** into the Khidmat Knowledge Layer. It is **architecturally flawed but salvageable**.

| Metric | Value |
|---|---|
| Total Lines | 5,860 |
| Condition Count | 40 specific conditions |
| Condition Category Count | 7 |
| Condition Family Count | 15 |
| Documentation/Governance Lines | ~675 (Parts 4–8 + header) |
| Broken Cross-References | 6 |
| Duplicate Entries | 1 |
| Intervention Leakage Instances | 18+ |
| Risk-Domain Leakage Instances | 4 attribute types |

### Core Finding

The file has **scope confusion**. It attempts to be simultaneously:
- A **health condition vocabulary** (its legitimate purpose)
- A **clinical medical reference** (intervention leakage)
- A **reasoning rule engine** (risk-domain leakage)
- A **governance document** (documentation bloat)

The condition definitions are clinically verbose, encode downstream reasoning rules (`registration_relevance`, `structural_significance`, `underdisclosure_risk`, `specific_vulnerability`), and contain ~675 lines of documentation, boundary notes, and future-extension guidance that should live in a separate markdown file.

**Verdict: REJECT for acceptance. Require remediation per Section 8 before inclusion.**

---

## 2. OWNERSHIP VIOLATIONS

### 2.1 Lifecycle Ownership — NO VIOLATION

The file correctly references `lifecycle-stages.yaml` via `stage_ref` in `characteristic_lifecycle_manifestations`. It does not define lifecycle stages, age boundaries, or developmental milestones. The `typical_onset_pattern` attribute uses age-band descriptors (birth, infancy, early childhood, etc.) as **clinical onset values**, not as lifecycle stage definitions. This is a legitimate condition attribute.

**Status: Clean.**

### 2.2 Capability Ownership — NO VIOLATION

The file correctly references `capabilities.yaml` via `domain_ref` in `affected_capability_domains`. It does not define capability levels, scales, domains, or assessment guidance. The `typical_impact_level` uses the four-level scale from `capabilities.yaml` by reference.

**However**, three broken capability domain references exist (see Section 3.4).

**Status: Clean with broken references.**

### 2.3 Dependency Ownership — NO VIOLATION

The file correctly references `dependency.yaml` via `dependency_ref` in `triggered_dependency_types`. It does not define dependency types, directionality, or characteristics. The `trigger_condition` describes when a condition activates a dependency — this is legitimately a condition property.

**Status: Clean.**

### 2.4 Family Structure Ownership — NO VIOLATION

The file correctly references `family-structure.yaml` via `role_ref` in `family_role_impact`. It does not define kinship roles, support roles, family relationships, or caregiver classifications. The `impact_description` describes how a condition affects a family role — this is legitimately a condition property.

**However**, the file defines `structural_significance` (low/moderate/high) as a condition attribute. This is **a reasoning output**, not a condition property. The risk domain and family-structure reasoning should compute structural significance from condition + role + household context, not have it pre-declared in the condition file. (See Section 3.2.)

**Status: Clean with one reasoning-attribute leakage.**

### 2.5 Risk Domain Ownership — VIOLATION

The file encodes **four risk/reasoning attributes** that belong to downstream domains:

| Attribute | Belongs To | Location in File | Violation |
|---|---|---|---|
| `registration_relevance` | Registration Reasoning | Every condition (lines 515–555) | Condition declares its own registration relevance instead of registration reasoning referencing the condition. |
| `underdisclosure_risk` | Registration Questioning | Every condition (lines 5414–5430) | Questioning strategy should determine which conditions need active probing. |
| `structural_significance` | Risk Domain / Family Reasoning | Every `family_role_impact` (lines 5470–5487) | Risk domain should compute structural impact from condition + household context. |
| `specific_vulnerability` | Risk Domain | Every `characteristic_lifecycle_manifestation` (lines 555–556) | Risk domain should derive vulnerability labels from condition + lifecycle + context. |

These are not condition properties. They are **reasoning classifications** that the condition file has incorrectly claimed.

**Status: VIOLATION — 4 attributes must be removed.**

### 2.6 Case Management / Programs / Impact Ownership — NO DIRECT VIOLATION

The file does not explicitly define case management rules, program eligibility, or outcome indicators. However, the clinical treatment details embedded in condition descriptions (see Section 3.3) implicitly encode what interventions are appropriate. The `treatability` attribute is legitimately a clinical property, but the descriptions go beyond treatability into treatment specificity.

**Status: Indirect leakage through clinical description verbosity.**

---

## 3. CROSS-DOMAIN VIOLATIONS

### 3.1 Risk Domain Leakage

#### A. `specific_vulnerability` Labels (Risk Domain)

Every `characteristic_lifecycle_manifestation` includes a `specific_vulnerability` label. Examples:

- `developmental_irreversibility` (SAM, infant)
- `high_mortality_infant` (tuberculosis, infant)
- `delayed_diagnosis_and_transmission` (tuberculosis, adult)
- `polypharmacy_and_cognitive_decline_interaction` (diabetes, older adult)
- `stepwise_decline_from_minor_events` (heart failure, elderly)
- `underdisclosure_and_exploitation_risk` (dementia, elderly)

These are **vulnerability labels** — vocabulary owned by the Risk Domain. The Risk Domain must derive vulnerability from condition + lifecycle + capability + environment + household context. The condition file should not pre-declare vulnerability labels. This is a **vocabulary ownership violation**.

**Recommendation:** Remove `specific_vulnerability` entirely. Replace with a plain-text `stage_specific_note` if stage-specific narrative is needed.

#### B. `disability_potential` (Risk Domain Input)

`disability_potential` (none/low/moderate/high) is a clinical property but is explicitly designed as a **risk domain input**. The boundary notes state: "The Risk Domain uses this as an input to disability risk assessment."

This is acceptable as a condition attribute if it remains purely clinical. However, it must not evolve into a score.

**Recommendation:** Keep but monitor. If the Risk Domain needs a different scale, `disability_potential` must not block it.

#### C. `structural_significance` (Risk Domain Output)

`structural_significance` (low/moderate/high) is defined as "The impact of a condition in a specific family role on the household's structural stability." This is a **risk-domain output**. A condition in a primary earner may have different structural significance in a large, well-resourced family versus a small, impoverished one. The condition file cannot know the household context. Pre-computing this is architecturally wrong.

**Recommendation:** Remove entirely. Compute in Risk Domain or family-structure reasoning.

#### D. `registration_relevance` (Registration Reasoning)

`registration_relevance` (direct_need / capability_impact / caregiver_burden / family_cascade / all) tells the registration system which reasoning pathways to activate. This is a **registration reasoning rule**, not a condition property. The registration domain should have a mapping table: "These conditions trigger direct_need; these trigger family_cascade."

**Recommendation:** Remove entirely. Move to registration reasoning or a cross-domain mapping file.

#### E. `underdisclosure_risk` (Registration Questioning)

`underdisclosure_risk` (low/moderate/high) is defined as "The likelihood that the condition will be hidden or not reported during registration." While this is a property of the condition (e.g., HIV has high stigma → high underdisclosure), the **registration questioning strategy** should determine which conditions need active probing. The condition file should not tell registration how to question.

**Recommendation:** Remove or move to registration questioning strategy. If kept, it must be reframed as a pure clinical/epidemiological property with no registration-system implications.

### 3.2 Capability Ownership Violations — NONE (but broken references)

The file does not define capability levels, domains, or assessments. However, it references **three non-existent capability domains**:

| Broken Reference | Condition | Line |
|---|---|---|
| `capabilities.yaml#feeding` | `cleft_lip_palate` | ~4472 |
| `capabilities.yaml#emotional_regulation` | `traumatic_brain_injury` | ~3277 |
| `capabilities.yaml#decision_making` | `dementia` | ~2438 |

`feeding` and `emotional_regulation` are not defined in `capabilities.yaml`. `decision_making` is a dependency type (`dependency.yaml#decision_making`), not a capability domain. These are **cross-reference errors**, not ownership violations, but they indicate insufficient cross-file validation.

**Recommendation:** Fix all broken capability references. Map to actual capability domains or remove the mappings.

### 3.3 Dependency Ownership Violations — NONE

The file correctly references `dependency.yaml` and does not define dependency types. No violations.

### 3.4 Family Ownership Violations — NONE

The file correctly references `family-structure.yaml` and does not define family structures, roles, or caregiver classifications. No violations.

### 3.5 Intervention Leakage

The condition descriptions contain **clinical treatment and management details** that belong to clinical domains, not a humanitarian ontology. The boundary enforcement rules explicitly state: "No treatment protocols. This file defines whether a condition is treatable. It does not define the treatment." Yet the file repeatedly violates this.

#### Flagged Instances (representative, not exhaustive):

| Condition | Intervention Leakage | Line Range |
|---|---|---|
| `severe_acute_malnutrition` | "SAM requires **immediate therapeutic intervention**." | ~406 |
| `tuberculosis` | "requires **prolonged treatment (typically 6 months)**... **Treatment interruption** leads to drug resistance" | ~775–778 |
| `hiv_aids` | "With **antiretroviral therapy**, HIV is a manageable chronic condition" | ~889–891 |
| `diabetes_mellitus` | "Management requires **sustained blood glucose control through medication, diet, and monitoring**" | ~1304–1308 |
| `cancer` | "Cancer **treatment requires surgery, chemotherapy, radiation, or palliative care**" | ~2277–2279 |
| `cleft_lip_palate` | "**Lip repair is typically performed at 3–6 months; palate repair at 9–18 months**" | ~4449–4452 |
| `congenital_heart_disease` | "Many congenital heart defects can be **corrected or palliated with surgery**" | ~3876–3881 |
| `chronic_kidney_disease` | "Advanced CKD requires **dialysis or transplantation**" | ~2029–2032 |
| `epilepsy` | "Epilepsy is manageable with **antiseizure medication**" | ~2149–2151 |
| `hepatitis` | "Chronic hepatitis can progress to **cirrhosis and liver cancer**" | ~1157–1159 |
| `asthma` | "Asthma is typically manageable with **inhaled medication**" | ~1938–1941 |
| `psychotic_disorder` | "With **treatment**, many people achieve significant symptom control" | ~2942–2944 |
| `amputation` | "With **prosthetics and rehabilitation**, many people regain significant function" | ~3744–3746 |
| `traumatic_brain_injury` | "Recovery is variable and may be incomplete, particularly in severe cases. **Rehabilitation**..." | ~3225–3227 |
| `spinal_cord_injury` | "The condition is permanent because **the spinal cord does not regenerate**" | ~3368–3370 |
| `stroke` | "Stroke is a **medical emergency** with lasting consequences" | ~1800–1802 |
| `heart_failure` | "Heart failure requires **daily caregiving support for medication management, fluid monitoring, dietary restriction**" | ~1724–1729 |

These are **clinical management statements**, not humanitarian condition descriptions. A humanitarian ontology should describe what the condition does to a person's functioning, not what clinical treatment it requires. The `treatability` attribute (curable / manageable_with_treatment / etc.) is sufficient to capture whether the condition is amenable to intervention. The descriptions should focus on:
- What body functions are affected
- What capability impacts result
- What dependency types are triggered
- How the condition differs across lifecycle stages
- How the condition affects family roles

**Recommendation:** Remove all clinical treatment timelines, medication names, treatment protocols, and rehabilitation specifics from condition descriptions. Retain `treatability` as the sole clinical-intervention attribute.

### 3.6 Broken Cross-References and Quality Errors

| Error | Type | Location |
|---|---|---|
| `capabilities.yaml#feeding` | Broken reference | `cleft_lip_palate.affected_capability_domains` |
| `capabilities.yaml#emotional_regulation` | Broken reference | `traumatic_brain_injury.affected_capability_domains` |
| `capabilities.yaml#decision_making` | Broken reference (wrong file) | `dementia.affected_capability_domains` |
| `health-conditions.yaml#osteoporosis` | Dangling reference (condition not defined) | `fracture_orthopedic_trauma.common_comorbidities` |
| `health-conditions.yaml#pressure_injuries` | Dangling reference (condition not defined) | `spinal_cord_injury.common_comorbidities` and `lower_limb_physical_disability.common_comorbidities` |
| `health-conditions.yaml#malnutrition_unspecified` | Dangling reference (condition not defined) | `acute_respiratory_infection.common_comorbidities` |
| `health-conditions.yaml#tuberculosis` | Duplicate entry | `hiv_aids.common_comorbidities` (listed twice) |

---

## 4. RECOMMENDED REMOVALS

### 4.1 Documentation Bloat (Parts 5–8)

Remove the following sections entirely and move to a separate governance markdown file:

- **Part 5: Cross-Domain Relationship Patterns** (~124 lines)  
  This is developer documentation, not ontology content.
- **Part 6: Boundary Notes and Anti-Patterns** (~122 lines)  
  These are governance notes. They belong in a governance document.
- **Part 7: Alignment with Existing Shared Human Model Files** (~63 lines)  
  These are integration contracts. They belong in `DECISIONS.md` or a dedicated alignment document.
- **Part 8: Future Extensions** (~55 lines)  
  Future extension guidance belongs in the roadmap or governance document.
- **Header Boundary Enforcement Rules** (~22 lines, lines 36–57)  
  These are governance rules, not ontology content.
- **Condition category `reasoning_purpose` fields** (~21 lines)  
  These encode reasoning logic into the category definitions. Remove or simplify to pure description.

**Estimated removal: ~400 lines.**

### 4.2 Risk-Domain Leakage Attributes

Remove the following attributes from **all** conditions:

1. `registration_relevance` — move to registration reasoning
2. `underdisclosure_risk` — move to registration questioning strategy
3. `structural_significance` — move to risk domain / family reasoning
4. `specific_vulnerability` — replace with plain `note` or remove entirely

**Estimated removal: ~200 lines.**

### 4.3 Clinical Treatment Details from Descriptions

Remove or rewrite condition descriptions to eliminate:
- Medication names and timelines
- Surgery timelines and protocols
- Rehabilitation specifics
- Treatment duration specifics (e.g., "typically 6 months")
- Diagnostic criteria embedded in descriptions

**Estimated removal: ~300–400 lines of description verbosity.**

### 4.4 Broken Cross-References and Duplicates

Fix or remove:
- `capabilities.yaml#feeding` → remove or map to `independent_living`
- `capabilities.yaml#emotional_regulation` → remove or map to `cognitive_functioning`
- `capabilities.yaml#decision_making` → remove or map to `self_advocacy`
- `health-conditions.yaml#osteoporosis` → remove or define `osteoporosis` as a condition
- `health-conditions.yaml#pressure_injuries` → remove or define as a condition
- `health-conditions.yaml#malnutrition_unspecified` → remove or map to `stunting`
- Remove duplicate TB entry in HIV

---

## 5. RECOMMENDED REFACTORS

### 5.1 Reframe Condition Descriptions

Current descriptions are 3–8 sentence clinical paragraphs. Refactor to **2–3 sentence humanitarian descriptions**:

- Sentence 1: What the condition is (clinical essence, 1 sentence)
- Sentence 2: What it does to human functioning (humanitarian consequence, 1 sentence)
- Sentence 3 (optional): Why it matters in humanitarian contexts (1 sentence)

**Example — Current `diabetes_mellitus` description:**
> A chronic metabolic condition characterized by elevated blood glucose due to insufficient insulin production or impaired insulin action. Diabetes causes progressive damage to multiple organ systems including the eyes, kidneys, nerves, and cardiovascular system. Management requires sustained blood glucose control through medication, diet, and monitoring.

**Example — Refactored:**
> A chronic metabolic condition of elevated blood glucose that causes progressive damage to multiple organ systems. In humanitarian contexts, the primary concern is treatment access and adherence rather than the disease itself, as the condition requires sustained management that is frequently disrupted by displacement or resource constraints.

### 5.2 Simplify `impact_mechanism` Fields

Current `impact_mechanism` descriptions are 3–6 sentences. Reduce to **1–2 sentences** describing the mechanism of capability impact. The detail is excessive for reasoning purposes.

### 5.3 Reduce `environmental_interactions`

Current: 1–4 environmental factors per condition.  
**Recommended:** 1–2 factors per condition, keeping only the most relevant to humanitarian contexts (e.g., displacement, food insecurity, extreme heat, healthcare access gap). Remove factors like "high salt diet" or "allergen exposure" unless they are dominant in humanitarian settings.

### 5.4 Consider Condition Consolidation

The file has 40 conditions. While the boundary notes state this is "intentionally limited," the granularity is at the upper bound of what a humanitarian ontology needs. Consider consolidating:

- **Cardiovascular conditions:** `coronary_artery_disease`, `heart_failure`, `stroke` → could be merged into `cardiovascular_disease` with sub-type notation, OR kept separate but with reduced descriptions. The current separation is clinically precise but may not be necessary for humanitarian reasoning.
- **Mental health conditions:** `depression`, `anxiety_disorder`, `post_traumatic_stress_disorder`, `psychotic_disorder`, `substance_use_disorder` — these are distinct and should likely remain separate because they have different humanitarian consequences (caregiver impact, stigma, family cascade).
- **Injury conditions:** `traumatic_brain_injury`, `spinal_cord_injury`, `fracture_orthopedic_trauma`, `burns`, `amputation` — these have distinct capability impacts. Keeping them separate is justified.
- **Sensory/physical disabilities:** `visual_impairment`, `hearing_impairment`, `lower_limb_physical_disability`, `upper_limb_physical_disability`, `multiple_disabilities` — these are distinct and should remain separate.

**Recommendation:** Do not reduce the condition count at this stage. Reduce the **description verbosity** per condition instead. If the file remains too large after verbosity reduction, reconsider consolidation.

### 5.5 Make `family_role_impact` Optional

Not all conditions need `family_role_impact` for every role. Some conditions have minimal impact on certain roles. The schema should allow omission of `family_role_impact` for roles where the impact is negligible, rather than requiring an entry for every major role.

### 5.6 Refactor `condition_attributes_reference`

Part 4 (Condition Attributes Reference) is ~243 lines. It defines controlled values for condition properties. This is legitimate ontology content, but it could be simplified. Some values are overly verbose in their descriptions.

**Recommendation:** Keep Part 4 but reduce description verbosity by ~30%.

---

## 6. RECOMMENDED FILE STRUCTURE

### Current Structure (Problematic)

```
health-conditions.yaml (5,860 lines)
├── Header + boundary rules
├── Part 1: Condition Categories
├── Part 2: Condition Families
├── Part 3: Specific Conditions (~4,860 lines)
├── Part 4: Condition Attributes Reference
├── Part 5: Cross-Domain Relationship Patterns
├── Part 6: Boundary Notes and Anti-Patterns
├── Part 7: Alignment with Existing Files
└── Part 8: Future Extensions
```

### Recommended Structure

```
shared/human-model/
├── health-conditions.yaml (~3,500–4,000 lines target)
│   ├── Condition Categories
│   ├── Condition Families
│   ├── Specific Conditions (reduced verbosity)
│   └── Condition Attributes Reference
├── health-conditions-governance.md
│   ├── Boundary Enforcement Rules
│   ├── Cross-Domain Relationship Patterns
│   ├── Alignment Contracts with Existing Files
│   └── Future Extension Guidance
└── DECISIONS.md (append alignment resolutions)
```

### Rationale

The ontology file should contain **only the ontology**. All governance, documentation, boundary notes, alignment contracts, and future extension guidance should live in a separate markdown file. This follows the pattern established by the other Shared Human Model files:

- `lifecycle-stages.yaml`: 601 lines, no extensive governance sections
- `dependency.yaml`: 562 lines, no extensive governance sections
- `capabilities.yaml`: 1,400 lines, has design notes and future extensions but these are contained and proportionate
- `family-structure.yaml`: 1,573 lines, has design decisions and boundary notes but they are the final sections, not interleaved

`health-conditions.yaml` at 5,860 lines is **4× larger** than the next largest file. The disproportion is not justified by the ontology content alone. It is justified by the clinical verbosity and documentation bloat. Both must be reduced.

---

## 7. FINAL VERDICT

| Criterion | Assessment |
|---|---|
| **Ownership Compliance** | Partially non-compliant. Core references are clean, but 4 reasoning attributes (`registration_relevance`, `underdisclosure_risk`, `structural_significance`, `specific_vulnerability`) belong to downstream domains. |
| **Risk Domain Leakage** | **Present.** Vulnerability labels, structural significance, and registration relevance are risk-domain or registration-domain concepts encoded into the condition ontology. |
| **Intervention Leakage** | **Present.** Condition descriptions contain clinical treatment timelines, medication references, and treatment protocols. These violate the explicit "No treatment protocols" boundary rule. |
| **Capability/Dependency/Family Ownership** | Clean. No definitions stolen. Three broken cross-references require fixing. |
| **Documentation Bloat** | **Severe.** ~675 lines of documentation, governance, and alignment content should be extracted to a separate markdown file. |
| **Ontology Size** | **Over-modelled in verbosity, not in condition count.** 40 conditions is acceptable for a humanitarian ontology, but 5,860 lines is excessive. The file is clinically verbose and approaches medical reference territory. Target: ~3,500–4,000 lines. |
| **Cross-Reference Quality** | **Poor.** 6 broken references and 1 duplicate entry indicate insufficient validation against referenced files. |

### Overall Verdict: **REJECT — REMEDIATION REQUIRED**

The file is **not ready for acceptance**. It does not require a complete rewrite, but it requires:
1. **30% size reduction** through documentation extraction and description verbosity reduction
2. **Removal of 4 downstream-domain reasoning attributes**
3. **Stripping of clinical treatment details** from condition descriptions
4. **Fixing of all broken cross-references**
5. **Re-audit** before inclusion in the Knowledge Layer

After remediation, the file will be a **clean, authority-compliant ontology** that correctly references lifecycle, capability, dependency, and family structure domains without owning their concepts.

---

## 8. PRECISE REMEDIATION PLAN

### Phase A: Documentation Extraction (Priority: High)
1. Create `shared/human-model/health-conditions-governance.md`.
2. Move the following from `health-conditions.yaml` to the governance file:
   - Lines 36–57: Boundary Enforcement Rules
   - Lines 5497–5613: Part 5 — Cross-Domain Relationship Patterns
   - Lines 5614–5736: Part 6 — Boundary Notes and Anti-Patterns
   - Lines 5737–5800: Part 7 — Alignment with Existing Files
   - Lines 5801–5856: Part 8 — Future Extensions
   - All `reasoning_purpose` fields from condition categories
3. Append alignment contract resolutions to `DECISIONS.md`.

### Phase B: Downstream-Domain Attribute Removal (Priority: High)
4. Remove `registration_relevance` from every condition.
5. Remove `underdisclosure_risk` from every condition.
6. Remove `structural_significance` from every `family_role_impact`.
7. Remove `specific_vulnerability` from every `characteristic_lifecycle_manifestation`. Replace with optional plain-text `note` if needed.
8. Move the `registration_relevance` and `underdisclosure_risk` mappings to `registration/reasoning/` or `registration/questioning/` as appropriate.

### Phase C: Clinical Description Refactoring (Priority: High)
9. Rewrite every condition description to remove:
   - Medication names and regimens
   - Surgery timelines and protocols
   - Treatment duration specifics
   - Diagnostic procedure references
   - Rehabilitation program details
10. Retain `treatability` as the sole clinical-intervention attribute.
11. Ensure descriptions focus on humanitarian functioning impact, not clinical management.

### Phase D: Verbosity Reduction (Priority: Medium)
12. Reduce every `impact_mechanism` to 1–2 sentences.
13. Reduce every `environmental_interaction` to 1 factor per condition (2 maximum).
14. Reduce `compounding_effect` descriptions in `common_comorbidities` to 1–2 sentences.
15. Simplify descriptions in `condition_attributes_reference` by ~30%.

### Phase E: Cross-Reference Repair (Priority: High)
16. Fix `capabilities.yaml#feeding` → remove or map to `capabilities.yaml#independent_living`.
17. Fix `capabilities.yaml#emotional_regulation` → remove or map to `capabilities.yaml#cognitive_functioning`.
18. Fix `capabilities.yaml#decision_making` → remove or map to `capabilities.yaml#self_advocacy`.
19. Fix `health-conditions.yaml#osteoporosis` → remove or define `osteoporosis` as a condition.
20. Fix `health-conditions.yaml#pressure_injuries` → remove or define as a condition.
21. Fix `health-conditions.yaml#malnutrition_unspecified` → remove or map to `health-conditions.yaml#stunting`.
22. Remove duplicate TB entry in `hiv_aids.common_comorbidities`.

### Phase F: Validation (Priority: High)
23. Run a cross-reference validation script against:
    - `capabilities.yaml` (verify all `domain_ref` targets exist)
    - `dependency.yaml` (verify all `dependency_ref` targets exist)
    - `lifecycle-stages.yaml` (verify all `stage_ref` targets exist)
    - `family-structure.yaml` (verify all `role_ref` targets exist)
    - `health-conditions.yaml` itself (verify all `condition_ref` targets exist)
24. Target final file size: **3,500–4,000 lines**.
25. Re-audit before acceptance.

### Estimated Impact

| Remediation | Lines Removed | Lines Added |
|---|---|---|
| Documentation extraction | ~400 | ~400 (in .md file) |
| Attribute removal | ~200 | 0 |
| Description refactoring | ~300–400 | ~100 (rewritten text) |
| Verbosity reduction | ~500–700 | ~100 |
| Broken reference removal | ~50 | 0 |
| **Net reduction** | **~1,200–1,600 lines** | **~600 (in .md file)** |
| **Net YAML reduction** | **~1,200–1,600 lines** | — |

**Target YAML size: ~4,200–4,600 lines.**  
If further reduction is needed, consider merging cardiovascular conditions or reducing `environmental_interactions` further.

---

*Audit completed. Do not modify the ontology until the remediation plan is approved by the Human Owner.*
