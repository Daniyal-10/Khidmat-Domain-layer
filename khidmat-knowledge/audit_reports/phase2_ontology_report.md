# Phase 2: Ontology Certification Report

## Finding 1: Semantic Leakage in Structural Constraints
- **Title**: Value Constraints Masquerading as Cardinality Constraints
- **Severity**: High
- **Evidence**: `registration/ontology/semantic-constraints.yaml` uses `type: cardinality` with `expression: age >= 0` (and `size >= 1`) instead of the required `{min, max}` structure.
- **Impact**: Breaks downstream generators that expect cardinality constraints to define structural limits (min/max instances) rather than evaluating property values. Causes semantic leakage between structure and validation.
- **Recommendation**: Move value validation rules out of structural `semantic-constraints.yaml` into domain reasoning/validation files, or define a distinct `type: value_validation` in the schema if it must be represented here.
- **Release Impact**: Blocks generator implementation. Must be fixed before final artifact generation.

## Finding 2: Unresolved Ownership Conflict for Household Entity
- **Title**: Dual-Definition of Household Entity
- **Severity**: Critical
- **Evidence**: `shared/ontology/entities.yaml` defines the canonical `household` entity, while `registration/ontology/entities.yaml` defines `household_snapshot` observing it. The `ontology_completion_checklist.md` explicitly flags an unresolved ownership dual-definition risk because the boundaries and attribute ownership are duplicated rather than strictly delegated.
- **Impact**: Violates ADR-008 (Single Ownership). Can lead to split-brain data models where different domains query different household representations.
- **Recommendation**: Consolidate household composition attributes into `shared/ontology/entities.yaml` and strictly define `household_snapshot` as a pure reference projection in Registration.
- **Release Impact**: Blocker for cross-domain case management and longitudinal household resilience tracking.

## Finding 3: Missing Integration Seam for Person Entity
- **Title**: Persistent Person Entity Lacks Attributes and Integration
- **Severity**: High
- **Evidence**: `shared/ontology/entities.yaml` declares a `person` entity but it remains a bare label with no attribute model. Crucially, there is no structural relationship in `registration` migrating the `beneficiary` snapshot to this persistent `person`.
- **Impact**: Prevents tracking beneficiaries across multiple cases or domains. The system will treat a returning beneficiary as a new, unconnected case.
- **Recommendation**: Flesh out the `person` entity attributes in `shared` and formalize the promotion/linkage seam in `registration/ontology/relationships.yaml` between `beneficiary` and `person`.
- **Release Impact**: Blocks Beneficiary Lifecycle domain activation and longitudinal outcome tracking.

## Finding 4: Taxonomic Misclassifications and Gaps
- **Title**: Misaligned Concepts in Shared and Registration Taxonomies
- **Severity**: Medium
- **Evidence**: 
  - `shared/taxonomy/organisations.yaml` conflates `mosque_or_religious_institution`, which have different accountability/service models. 
  - `registration/taxonomy/needs.yaml` classifies `therapeutic_nutrition` as a food subtype rather than a medical/clinical pathway.
- **Impact**: AI reasoning models will misclassify interventions and fail to trigger necessary medical pathways for severe acute malnutrition (SAM/MAM).
- **Recommendation**: Decouple the religious and educational organization types in the shared taxonomy. Move `therapeutic_nutrition` to the medical need category or establish a cross-reference.
- **Release Impact**: Required before Programs and Support Delivery domains are activated.
