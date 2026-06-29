# Khidmat Knowledge Layer — Ontology Completion Checklist

**Authority:** Knowledge Layer Architect
**Purpose:** Single source of truth for ontology progress. Updated as work completes.
**Scope:** All taxonomy, ontology, reasoning, verification, questioning, and governance files

---

## COMPLETED

### Registration Domain — Core

✓ Actors Taxonomy (`registration/taxonomy/actors.yaml`)
✓ Needs Taxonomy (`registration/taxonomy/needs.yaml`)
✓ Situations Taxonomy (`registration/taxonomy/situations.yaml`)
✓ Claims Taxonomy (`registration/taxonomy/claims.yaml`)
✓ Case Outcomes Taxonomy (`registration/taxonomy/case-outcomes.yaml`)
✓ Lead Statuses Taxonomy (`registration/taxonomy/lead-statuses.yaml`)
✓ Referral Sources Taxonomy (`registration/taxonomy/referral-sources.yaml`)
✓ Registration Entities Ontology (`registration/ontology/entities.yaml`)
✓ Registration Attributes Ontology (`registration/ontology/attributes.yaml`)
✓ Registration Relationships Ontology (`registration/ontology/relationships.yaml`)
✓ Inference Rules (`registration/reasoning/inference-rules.yaml`)
✓ Severity Rules (`registration/reasoning/severity-rules.yaml`)
✓ Case Coherence Rules (`registration/reasoning/case-coherence-rules.yaml`)
✓ Gap Detection Rules (`registration/reasoning/gap-detection-rules.yaml`)
✓ Gap Types (`registration/gaps/gap-types.yaml`)
✓ Questioning Strategy (`registration/questioning/questioning-strategy.yaml`)
✓ Question Templates (`registration/questioning/question-templates.yaml`)
✓ Verification Brief Projection (`registration/verification/verification-brief-projection.yaml`)
✓ Verification Requirements (`registration/verification/verification-requirements.yaml`)
✓ Readiness Rules (`registration/readiness/readiness-rules.yaml`)

### Shared Domain — Core

✓ Person Base Taxonomy (`shared/taxonomy/persons.yaml`)
✓ Organisation Types Taxonomy (`shared/taxonomy/organisations.yaml`)
✓ Location Taxonomy (`shared/taxonomy/locations.yaml`)
✓ Document Types Taxonomy (`shared/taxonomy/document-types.yaml`)

### Architecture and Governance

✓ Architecture Declaration (`ARCHITECTURE.md`)
✓ Architectural Decision Log (`DECISIONS.md`)
✓ Ubiquitous Language Glossary (`GLOSSARY.md`)
✓ AI Collaboration Workflow (`AI_WORKFLOW.md`)
✓ Agent Handoff Briefing (`AGENT_HANDOFF.md`)

### Phase 2.0 Governance (Produced This Phase)

✓ Knowledge Layer Inventory (`knowledge_layer_inventory.md`)
✓ Ontology Completion Checklist (`ontology_completion_checklist.md`) ← this file
✓ Ontology Authority Matrix (`ontology_authority_matrix.md`)
✓ Knowledge Layer Roadmap (`knowledge_layer_roadmap.md`)

### Phase 2.0 — Shared Human Model (Foundational Ontologies)

✓ Shared Human Model Architecture (`shared/human-model/README.md`)
✓ Lifecycle Stages Ontology (`shared/human-model/lifecycle-stages.yaml`)
✓ Dependency Ontology (`shared/human-model/dependency.yaml`)
✓ Capability Ontology (`shared/human-model/capabilities.yaml`)
✓ Family Structure Ontology (`shared/human-model/family-structure.yaml`)
✓ Health Conditions Ontology (`shared/human-model/health-conditions.yaml`)

### Phase 3.0 — Risk Domain (Complete)

✓ Hazard Categories (`shared/risk/hazard-categories.yaml`)
✓ Exposure (`shared/risk/exposure.yaml`)
✓ Vulnerability (`shared/risk/vulnerability.yaml`)
✓ Protective Factors (`shared/risk/protective-factors.yaml`)
✓ Household Resilience (`shared/risk/household-resilience.yaml`)
✓ Risk (`shared/risk/risk.yaml`)
✓ Compound Risk Detection (`shared/risk/reasoning/compound-risk-detection.yaml`)

### Phase 4.0 — Verification Operations (Active / In Progress)

✓ Verification Operations Core Ontology (`verification-operations/verification-operations.yaml`)
□ Operational Verification Models (assignment, field visit, claim confirmation, etc.) [Pending]

### Phase 4.x — Beneficiary Lifecycle (Complete)

✓ Beneficiary Lifecycle Taxonomy (`beneficiary-lifecycle/taxonomy.yaml`)
✓ Beneficiary Lifecycle Ontology (`beneficiary-lifecycle/ontology.yaml`)

---

## IN PROGRESS

### Registration Domain — Incomplete Files

□ Support Intervention Taxonomy (`registration/taxonomy/support-interventions.yaml`)
  Status: Placeholder declared. Concepts listed. Implementation deferred pending operations staff input.
  Blocker: Requires operational intervention catalogue confirmed with programme staff.

□ Evidence Taxonomy (`registration/taxonomy/evidence.yaml`)
  Status: Placeholder declared. Dependency on shared/taxonomy/document-types.yaml declared.
  Blocker: Requires registration domain to need structured evidence classification beyond document type labels.

### Shared Domain — In Progress

□ Time Taxonomy (`shared/taxonomy/time.yaml`)
  Status: Placeholder declared. Will formalise duration bands and onset recency vocabulary.
  Blocker: Requires cross-domain reporting to make consistent time vocabulary necessary.

---

## MISSING

### Registration Domain — Known Gaps Not Yet Addressed

□ Evidence Entity Attributes
  Gap: `registration/ontology/attributes.yaml` declares an evidence entity in entities.yaml but has no attribute block for it. Evidence entity attributes must be added before verification operations can function.

□ Compound Situation Inference Rules
  Gap: All inference rules are single-trigger. No rule models the compounding of multiple simultaneous triggers. A bereavement + displacement compound is qualitatively different from either alone.

□ Lifecycle-Stage-Aware Inference Rules
  Gap: Inference rules do not use lifecycle stage. An infant in a food-insecure household should trigger developmental malnutrition risk distinct from the household food need.

□ Capability Alignment Migration

Gap:
`functional_capacity` currently exists inside the registration domain while the emerging Shared Human Model introduces a dedicated capability ontology.

Required Future Work:

- align registration functional_capacity
- map lifecycle capability expectations
- migrate reasoning ownership to capability ontology
- prevent duplicate capability definitions across domains

□ Medical Severity with Treatment Plan Absence
  Gap: A critical medical need with no care pathway does not escalate severity. The treatment_plan_gap is classified as medium regardless of need severity.

### Shared Layer — Missing Entities

□ Person Entity (Shared, Persistent)
  Gap: No cross-domain persistent Person entity exists. `shared/ontology/entities.yaml` is a placeholder. The promotion from registration Beneficiary (snapshot) to Person (persistent) has no structural seam.

□ Community Entity
  Gap: No community context model. Location is for volunteer dispatch only.

□ Household Entity

Gap:
The system currently models beneficiaries and family members but does not yet define a first-class household entity.

Required for:

- household vulnerability assessment
- livelihood modelling
- family dependency chains
- seasonal risk analysis
- community-level planning

### New Domains Required — Not Yet Placeholdered



□ Outcome Indicator Vocabulary
  No outcome model exists. The system ends at case closure. Outcome indicators must be in shared vocabulary before beneficiary lifecycle, programs, or impact domains can measure change.

□ Health Condition Taxonomy
  Medical needs reference no health condition vocabulary. There is no chronic disease classification, no disability model beyond the three-value functional capacity enum, no malnutrition staging (SAM/MAM), no mental health condition vocabulary.

□ Seasonal and Environmental Risk Model
  No seasonal calendar. No environmental risk profile per geographic area. The damaged-roof-before-rainy-season reasoning scenario is entirely unsupported.

---

## FUTURE

### Domains to Activate (from Architecture.md Placeholders)

□ Case Management Domain
  Prerequisite: Verification Operations Domain active.

□ Volunteer Operations Domain
  Prerequisite: Volunteer profile requirements defined with operations staff.

□ Support Delivery Domain
  Prerequisite: Case Management Domain active + Intervention Taxonomy complete.

□ Programs Domain
  Prerequisite: Structured program distinct from ad-hoc assistance defined by client.

□ Impact Domain
  Prerequisite: Beneficiary Lifecycle Domain active + Outcome Indicator vocabulary.

### Future Knowledge Graph Domains (Not Yet Placeholdered)

□ Community Context Domain
  Owner: Shared or dedicated domain. Covers geographic area profiles, service access maps, seasonal risk calendars, community social capital indicators.

□ Donor Matching Domain
  Future. Requires: Intervention taxonomy, program taxonomy, donor profile model.

□ Resource Optimisation Domain
  Future. Requires: Intervention taxonomy, geographic data, volunteer capacity model.

□ Predictive Risk Domain
  Future. Requires: Risk domain, seasonal model, community context, household resilience model, longitudinal case data.

□ Programme Impact Ontology
  Future. Requires: Outcome indicators, impact measurement methodology, longitudinal data model.

□ Household Resilience Domain

Future.

Requires:

- Family Structure Ontology
- Capability Ontology
- Risk Domain
- Community Context Domain

Purpose:

Model the household's ability to absorb shocks, recover from crises, and maintain basic wellbeing over time.

---

## STATUS SUMMARY

| Category | Count | Notes |
|----------|-------|-------|
| Completed | 44+ files | Registration, Shared Human Model, Risk Domain, Beneficiary Lifecycle, and Verification Operations core established |
| In Progress | 2 items | Evidence taxonomy, time taxonomy |
| Missing (registration) | 4 items | Advanced reasoning and evidence modelling gaps |
| Missing (shared) | 6 items | Person, Household, Community and governance entities |
| Future (placeholder) | 5 domains | Planned operational domains (Stage 1 dependency anomaly noted; Verification Operations core complete but operational models pending) |
| Future (new) | 6 domains | Knowledge graph expansion domains |