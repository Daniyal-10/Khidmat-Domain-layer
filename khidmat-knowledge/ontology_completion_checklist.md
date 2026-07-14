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
✓ Registration Data Properties Ontology (`registration/ontology/data-properties.yaml`) — supersedes retired `attributes.yaml` (Registration Migration Phase 4)
✓ Registration Relationships Ontology (`registration/ontology/relationships.yaml`)
✓ Registration Semantic Constraints (`registration/ontology/semantic-constraints.yaml`)
□ Registration Lifecycle Constraints (`registration/ontology/lifecycle-constraints.yaml`) — canonical placeholder, no lifecycle semantics authored yet
✓ Registration Evidence Rules (`registration/reasoning/evidence-rules.yaml`) — claim-evidence matrix relocated from `evidence.yaml`
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
✓ Time Taxonomy (`shared/taxonomy/time.yaml`)

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
✓ Lifecycle Stages Ontology (`shared/human-model/taxonomy/lifecycle-stages.yaml`)
✓ Dependency Ontology (`shared/human-model/taxonomy/dependency.yaml`)
✓ Capability Ontology (`shared/human-model/taxonomy/capabilities.yaml`)
✓ Family Structure Ontology (`shared/human-model/ontology/family-structure.yaml`)
✓ Health Conditions Ontology (`shared/human-model/taxonomy/health-conditions.yaml`)

### Phase 3.0 — Risk Domain (Complete)

✓ Hazard Categories (`shared/risk/taxonomy/hazard-categories.yaml`)
✓ Exposure (`shared/risk/ontology/exposure.yaml`)
✓ Vulnerability (`shared/risk/ontology/vulnerability.yaml`)
✓ Protective Factors (`shared/risk/taxonomy/protective-factors.yaml`)
✓ Household Resilience (`shared/risk/ontology/household-resilience.yaml`)
✓ Risk (`shared/risk/ontology/risk.yaml`)
✓ Compound Risk Detection (`shared/risk/reasoning/compound-risk-detection.yaml`)

### Phase 4.0 — Verification Operations (Complete)

✓ Verification Operations Core Ontology (`verification-operations/verification-operations.yaml`)
✓ Verification Taxonomy (`verification-operations/taxonomy/*.yaml`)
✓ Verification Ontology Entities (`verification-operations/ontology/entities.yaml`)
✓ Verification Ontology Relationships (`verification-operations/ontology/relationships.yaml`)
✓ Verification Lifecycle Constraints (`verification-operations/ontology/lifecycle.yaml`)
✓ Verification Constraints (`verification-operations/ontology/constraints.yaml`)
✓ Verification Reasoning (`verification-operations/reasoning/*.yaml`)

### Phase 4.5 — Needs Assessment Domain (Complete)

✓ Discovery
✓ Taxonomy
✓ Ontology
✓ Independent Reviews
✓ Semantic Validation
✓ Foundation Review
✓ Governance Synchronization

### Phase 4.x — Beneficiary Lifecycle (Complete)

✓ Beneficiary Lifecycle Taxonomy (`beneficiary-lifecycle/taxonomy.yaml`)
✓ Beneficiary Lifecycle Ontology (`beneficiary-lifecycle/ontology.yaml`)

### Phase 5.0 — Case Management Domain (Complete)

✓ Case Management Taxonomy (`case-management/taxonomy/`)
✓ Case Management Ontology (`case-management/ontology/`)
✓ Consent Placeholder (`consent-and-privacy/ontology.yaml`)

### Repository Architecture Freeze (Complete — Registration Reference Implementation)

✓ Canonical Ontology Authoring Contract (`docs/architecture/Canonical_Ontology_Schema.md`)
✓ Canonical Taxonomy Authoring Contract (`docs/architecture/Canonical_Taxonomy_Schema.md`)
✓ Repository Migration Methodology (`docs/architecture/Repository_Migration_Methodology.md`)
✓ ADR-023 — Ontology Vocabulary Extension (Value Objects, Roles, Runtime/Reasoning Objects, Future Entity Candidate)
✓ Registration Migration Phases 1–4 (`docs/architecture/Registration_Migration_Plan.md`) — canonical to the CURIE boundary
□ Registration Migration Phase 5 (cross-domain CURIE layer) — blocked on repository-wide manifest and ratified base IRI
□ Registration Content Gap Log (19 records) — genuine content gaps requiring a domain-knowledgeable author; see `docs/architecture/Registration_Migration_Plan.md`

---

## IN PROGRESS

### Registration Domain — Incomplete Files

□ Support Intervention Taxonomy (`registration/taxonomy/support-interventions.yaml`)
  Status: Placeholder declared. Concepts listed. Implementation deferred pending operations staff input.
  Blocker: Requires operational intervention catalogue confirmed with programme staff.

□ Evidence Taxonomy (`registration/taxonomy/evidence.yaml`)
  Status: Structurally migrated to the canonical `schemes:`/`concepts:` shape and `status: active`;
  the Evidence entity's attributes are fully populated in `registration/ontology/data-properties.yaml`.
  Blocker: Two schemes (`evidence_types`, `availability_classifications`) still lack a
  domain-authored `description` — a genuine content gap, not a structural one (see the
  Registration Content Gap Log in `docs/architecture/Registration_Migration_Plan.md`).

### Community Context Domain — In Progress

□ Canonical Migration (`community-context/ontology/*.yaml`, `community-context/taxonomy/*.yaml`)
  Status: Domain content substantially built (12 taxonomy files, full ontology module) but
  authored against the pre-canonical structure.
  Blocker: None architectural — next in the migration queue after Registration's completed
  reference implementation. See `docs/architecture/Repository_Migration_Methodology.md`.

---

## MISSING

### Registration Domain — Known Gaps Not Yet Addressed

□ Compound Situation Inference Rules
  Gap: All inference rules are single-trigger. No rule models the compounding of multiple simultaneous triggers. A bereavement + displacement compound is qualitatively different from either alone.

□ Lifecycle-Stage-Aware Inference Rules
  Gap: Inference rules do not use lifecycle stage. An infant in a food-insecure household should trigger developmental malnutrition risk distinct from the household food need.

□ Medical Severity with Treatment Plan Absence
  Gap: A critical medical need with no care pathway does not escalate severity. The treatment_plan_gap is classified as medium regardless of need severity.

### Shared Layer — Missing Entities

□ Person Entity (Shared) — Integration Gap Remains
  Status: `shared/ontology/entities.yaml` is no longer a placeholder (`status: active`) and
  already declares a `person` entity (id: `person`, parent: `subject`).
  Remaining gap: the entity is a bare label with no attribute model, and no relationship
  wires it to registration's `Beneficiary` (a per-case snapshot). The promotion seam from
  Beneficiary snapshot to a persistent, cross-case Person still does not exist.

□ Community Entity — Now Exists, Pending Canonical Migration
  Status: `community-context/ontology/entities.yaml` already declares a `community` entity
  and related entities (`geographic_area`, `built_infrastructure`, `natural_resource`,
  `transportation_network_asset`, `local_collective`). This closes the "no community
  context model" gap. Remaining work is the domain's canonical migration (see the
  Community Context section above), which will also need to resolve a dangling
  `attributes_ref: ontology/attributes.yaml#community` reference — no such file exists
  in `community-context/ontology/` under the canonical (or legacy) structure.

□ Household Entity — Ownership Reconciliation Needed

Note: a first-class `household` entity now exists in **both**
`shared/ontology/entities.yaml` (declared authoritative, inherits from `subject`) and
`registration/ontology/entities.yaml` (an independent, fuller description, not
declared as a reference to the shared entity). This is a dual-definition that
`ontology_authority_matrix.md` and ADR-008's single-ownership rule are designed to
prevent. Flagged here for architectural review — not resolved by this documentation
pass, per this task's constraint against ontology/taxonomy content changes.

Remains required for: household vulnerability assessment, livelihood modelling,
family dependency chains, seasonal risk analysis, community-level planning.

### New Domains Required — Not Yet Placeholdered



□ Outcome Indicator Vocabulary
  No outcome model exists. The system ends at case closure. Outcome indicators must be in shared vocabulary before beneficiary lifecycle, programs, or impact domains can measure change.

Note: Health Condition Taxonomy and Seasonal/Environmental Risk Model, previously
listed here as missing, are now substantially built and have been moved to COMPLETED
and to the Community Context section above respectively:
`shared/human-model/taxonomy/health-conditions.yaml` (chronic disease, disability,
malnutrition staging including SAM/MAM, mental health conditions) and
`community-context/taxonomy/{seasonal-events,community-hazards,geographic-hierarchy}.yaml`.
Community Context's remaining work is canonical migration, not content authoring.

---

## FUTURE

### Domains to Activate (from Architecture.md Placeholders)

□ Volunteer Operations Domain
  Prerequisite: Volunteer profile requirements defined with operations staff.

□ Support Delivery Domain
  Prerequisite: Case Management Domain active + Intervention Taxonomy complete.

□ Programs Domain
  Prerequisite: Structured program distinct from ad-hoc assistance defined by client.

□ Impact Domain
  Prerequisite: Beneficiary Lifecycle Domain active + Outcome Indicator vocabulary.

### Future Knowledge Graph Domains (Not Yet Placeholdered)

Note: Community Context, previously listed here as not yet placeholdered, is now a
substantially built domain (`community-context/`) — see the Community Context section
above and the "In Progress" entry for its remaining canonical-migration work.

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
| Completed | 50+ files | Registration (canonical reference implementation), Shared Human Model, Risk Domain, Needs Assessment, Case Management, Beneficiary Lifecycle, and Verification Operations all complete; repository architecture frozen (Canonical Ontology/Taxonomy Schemas, ADR-023) |
| In Progress | 3 items | Support intervention taxonomy content (registration), evidence taxonomy content gaps (registration), Community Context canonical migration |
| Missing (registration) | 2 items | Compound/lifecycle-stage-aware inference rules, medical severity + treatment plan interaction |
| Missing (shared) | 2 items + 1 flagged conflict | Person entity lacks attributes and a Beneficiary integration seam; Outcome Indicator vocabulary does not yet exist; Household is defined in both `shared/` and `registration/` and needs an ownership decision (flagged, not resolved, by this pass) |
| Future (placeholder) | 5 domains | Volunteer Operations, Support Delivery, Programs, Impact, Consent & Privacy — all Level 2, inactive |
| Future (new) | 6 domains | Knowledge graph expansion domains |