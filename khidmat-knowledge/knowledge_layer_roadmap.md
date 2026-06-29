# Khidmat Knowledge Layer — Dependency Roadmap

**Authority:** Knowledge Layer Architect
**Purpose:** Shows what depends on what, in what order work must proceed, and what the knowledge graph looks like at each stage. This is a knowledge design roadmap, not an implementation plan.

---

## How to Read This Document

Each stage must be substantially complete before the next stage begins. "Substantially complete" means the concepts that downstream stages depend on are stable — not that every edge case is resolved. Prerequisites are hard dependencies. A domain that activates before its prerequisites are in place will invent concepts it shouldn't own, producing ontology drift.

Estimated maturity at each stage describes the reasoning capability the knowledge layer gains, not feature delivery.

---

## Current State: Entry Point

```
Registration Domain [COMPLETE]
    ├── Intake actors taxonomy
    ├── Need taxonomy
    ├── Situation taxonomy
    ├── Claims taxonomy and quality model
    ├── Case readiness rules
    ├── Verification brief projection
    └── Gap detection rules

Shared Layer [PARTIAL]
    ├── Person base taxonomy [minimal]
    ├── Organisation types [minimal]
    ├── Location vocabulary [dispatch-only]
    └── Document types [adequate]

Placeholder Domains [DECLARED, NOT ACTIVE]
    ├── verification-operations
    ├── case-management
    ├── beneficiary-lifecycle
    ├── volunteer-operations
    ├── support-delivery
    ├── programs
    └── impact

Missing Entirely

├── Community context
└── Outcome indicators

Current Active Phase

└── Phase 4.0 — Verification Operations (Active / In Progress)

Already Created

├── Lifecycle model
├── Dependency model
├── Capability model
├── Family structure model
├── Health conditions model
├── Risk Domain (Complete)
└── Verification Operations (Core Ontology Complete)
```

**Reasoning capability at current state:** The system can conduct a structured intake conversation, identify needs and claims, detect gaps, assess case readiness, and produce a verification brief. It cannot reason about a person across time, cannot model household resilience, cannot generate preventive signals, and cannot evaluate whether interventions work.

---

## Stage 1 — Complete Registration Domain Foundation

**What this stage completes:**
- Support Intervention Taxonomy (`registration/taxonomy/support-interventions.yaml`)
- Evidence Entity Attributes (`registration/ontology/attributes.yaml` — evidence section)
- Evidence Taxonomy (`registration/taxonomy/evidence.yaml`)
- Compound Inference Rules (extension of `registration/reasoning/inference-rules.yaml`)
- Functional Capacity Inference Rules (extension of `registration/reasoning/inference-rules.yaml`)
- Medical Severity + Treatment Plan interaction (fix in `registration/reasoning/severity-rules.yaml`)

**Prerequisites:** None. These are completions of the current domain.

**Blocker:** Support intervention types require operational input from programme staff. This cannot be invented by the knowledge layer alone.

**What this enables downstream:** Verification Operations domain can activate. Without the intervention taxonomy, the verification brief cannot tell a volunteer what specific assistance is being requested in structured form.

**Reasoning capability gained:** The system can now specify what it is asking for (not just that it needs help) and can classify evidence in a structured way. Verification volunteers receive a richer brief.

---

Stage 2 — Shared Human Model

STATUS: COMPLETED

Completed:
✓ lifecycle-stages.yaml
✓ dependency.yaml
✓ capabilities.yaml
✓ family-structure.yaml
✓ health-conditions.yaml

Current Active Deliverable:

Phase 4.0 — Verification Operations (Active / In Progress)

Future Shared Ontology Work:
□ shared human entity promotion model

Current Active Phase:
Phase 4.0 — Verification Operations (Active / In Progress)

The Shared Human Model prerequisite is now fully satisfied:

✓ lifecycle-stages.yaml
✓ dependency.yaml
✓ capabilities.yaml
✓ family-structure.yaml
✓ health-conditions.yaml

Risk Domain may now be activated.

**Prerequisites:** Stage 1 should be in progress but need not be complete. The shared human model does not depend on the intervention taxonomy. It does depend on the person base taxonomy in `shared/taxonomy/persons.yaml` which is already mature enough to extend.

**What this enables downstream:** Every subsequent domain that reasons about people, families, households, or life stages depends on this model existing. Without it, each domain invents its own person model, producing incompatible representations of the same human being.

**Reasoning capability gained:** The system can now differentiate a 6-month-old from a 16-year-old not merely by age integer but by lifecycle stage and the developmental expectations, risks, and needs associated with that stage. It can model what a person is capable of (not only what they lack). It can represent that a mother's vulnerability is an infant's vulnerability without requiring a separate registration for the infant.

---
### Current Shared Human Model Status

Completed

* shared/human-model/README.md
* shared/human-model/lifecycle-stages.yaml
* shared/human-model/dependency.yaml
* shared/human-model/capabilities.yaml
* shared/human-model/family-structure.yaml
* shared/human-model/health-conditions.yaml

Next Active Deliverable

Phase 4.0 — Verification Operations (Active / In Progress) (Core ontology complete; operational models pending)

After Completion

Stage 4 — Activate Verification Operations Domain (requires Stage 1 completion)

Architecture Rule

Risk Domain must not begin until:

* Family Structure Ontology
* Health Conditions Ontology

are complete and stable.


## Stage 3 — Risk Domain

**STATUS: COMPLETED**

**Completed:**
- ✓ Protective Factors Model (`shared/risk/protective-factors.yaml`)
- ✓ Hazard Categories (`shared/risk/hazard-categories.yaml`)
- ✓ Exposure Model (`shared/risk/exposure.yaml`)
- ✓ Vulnerability Composite Model (`shared/risk/vulnerability.yaml`)
- ✓ Household Resilience Model (`shared/risk/household-resilience.yaml`)
- ✓ Risk Model (`shared/risk/risk.yaml` — folded Risk Trajectory / Trend Model here)
- ✓ Compound Risk Detection (`shared/risk/reasoning/compound-risk-detection.yaml`)

**Prerequisites:**
- Stage 2 complete (Shared Human Model). ✓ Satisfied.
- `shared/taxonomy/locations.yaml` must be extended with geographic hierarchy and environmental risk profile classification. (Deferred to Stage 8 Community Context).

**What this enables downstream:** Case Management domain can reason about intervention urgency. Beneficiary Lifecycle domain can track risk trajectory over time. The Community Context domain depends on the seasonal risk calendar. Predictive flagging becomes possible.

**Reasoning capability gained:** The system can now distinguish "this household is currently in crisis" from "this household is likely to enter crisis within three months." A damaged roof in a flood-zone community before monsoon season becomes a detectable risk. An elderly person living alone with no caregiver during extreme heat becomes a proactive outreach signal. Risk is a first-class concept, not a byproduct of severity rules.

**Important boundary note:** The risk domain produces signals. It does not decide what to do about them. Intervention logic belongs in Stage 5.

---

## Stage 4 — Activate Verification Operations Domain

**STATUS: ACTIVE / IN PROGRESS** (Core Ontology Complete; Operational models pending; Stage 1 Dependency Anomaly Noted)

**What this stage produces:**
- ✓ Verification Operations core ontology (`verification-operations/verification-operations.yaml`) [Complete]
- □ Volunteer assignment model [Pending]
- □ Field visit outcome model [Pending]
- □ Claim confirmation model (result of a verification requirement) [Pending]
- □ Evidence collection model [Pending]
- □ Re-verification trigger model [Pending]

**Prerequisites:**
- Stage 1 complete (support interventions and evidence taxonomies)
- Registration domain stable in production (per existing placeholder declaration)
- Volunteer field workflow defined with operations staff

**What this enables downstream:** Case Management domain depends on verification operations completing. Without verification outcomes, there is nothing for case management to act on.

**Reasoning capability gained:** The system can now track what happens after case closure. The verification brief produces outcomes. Claims are confirmed or refuted. Cases move beyond the "awaiting verification" state.

---

## Stage 5 — Intervention Taxonomy and Case Management Domain

**What this stage produces:**
- Completed Support Intervention Taxonomy (operationally validated by programme staff)
  - Intervention type hierarchy
  - Eligibility conditions per intervention type
  - Typical duration norms
  - Contraindications (circumstances where an intervention type is inappropriate)
- Case Management domain — full Level 1 implementation
  - Case decision model
  - Intervention approval model
  - Case assignment model
  - Case escalation model
  - Intervention record

**Prerequisites:**
- Stage 3 complete (Risk Domain) — case management needs to reason about risk when prioritising interventions
- Stage 4 complete (Verification Operations active) — case management acts on verified cases

**Reasoning capability gained:** The system can now reason about what to do in response to a verified need. Intervention fit can be assessed: does this person's profile and situation match the eligibility conditions for this intervention type? Does the household's resilience suggest a time-limited intervention or a sustained one? The right intervention becomes a reasoned recommendation, not a manual decision.

---

## Stage 6 — Outcome Indicator Vocabulary

**What this stage produces:**
- Shared outcome indicator vocabulary (`shared/vocabulary/outcome-indicators.yaml`)
  - Outcome indicators per need category (what improvement looks like)
  - Measurement method per indicator (observable, self-reported, documented)
  - Baseline and endline concepts
  - Change classification (improved, unchanged, deteriorated, exited)

**Prerequisites:**
- Stage 5 complete (Intervention Taxonomy). Outcome indicators must align with what interventions are intended to produce.
- Must be co-designed across case management, programs, and impact domains to ensure consistency.

**Why this must precede Stage 7:** The Beneficiary Lifecycle domain tracks change over time. Without outcome indicators, it can track that a case occurred but cannot measure whether the person's situation changed. Lifecycle tracking without outcome measurement is a record system, not a knowledge system.

**Reasoning capability gained:** The system can now close the loop: Need → Intervention → Outcome. It can distinguish a household that received food assistance and achieved food security from one that received food assistance and remained food insecure. This distinction is the foundation of learning and improvement.

---

## Stage 7 — Beneficiary Lifecycle Domain

**What this stage produces:**
- Persistent Person entity in `shared/ontology/entities.yaml` (promoted from beneficiary snapshot)
- Beneficiary Lifecycle domain — full Level 1 implementation
  - Beneficiary record (persistent identity across cases)
  - Registration history
  - Intervention history
  - Status change tracking (improvement, deterioration, exit, re-entry)
  - Periodic review triggers
  - Re-registration triggers

**Prerequisites:**
- Stage 2 complete (Shared Human Model — lifecycle stages, capability)
- Stage 6 complete (Outcome Indicator vocabulary)
- At least two complete registrations for returning beneficiaries must exist in production (per existing placeholder declaration)

**What this enables downstream:** Impact domain depends on longitudinal data. Community Context domain uses aggregate lifecycle data for area-level vulnerability mapping.

**Reasoning capability gained:** The system can now reason about a person across time. It can identify that a household receiving assistance for the third time has not improved, suggesting the intervention type is wrong. It can flag that a child who was in school at first registration has dropped out by second registration. The person has a history, not just a snapshot.

---

## Stage 8 — Community Context Domain

**What this stage produces:**
- Geographic area profiles (district, block, village with environmental and service access attributes)
- Service access model (distance and quality of healthcare, schools, markets, water)
- Seasonal risk calendar (flood season, drought season, agricultural cycle, school examination periods)
- Community social capital indicators
- Aggregate vulnerability mapping (concentration of vulnerable households in an area)

**Prerequisites:**
- Stage 3 complete (Risk Domain — the seasonal risk calendar extends from the risk domain)
- Stage 7 complete (Beneficiary Lifecycle — aggregate data requires longitudinal records)
- `shared/taxonomy/locations.yaml` must be extended with geographic hierarchy

**Reasoning capability gained:** The system can now reason about a household in its context, not in isolation. A household with a damaged roof is a shelter repair case. The same household in a flood-zone community with monsoon approaching is a preventive emergency. The community layer makes that distinction expressible.

The system can also reason at the programme level: which geographic areas have concentrations of vulnerable households that warrant a programmatic response rather than case-by-case intervention?

---

## Stage 9 — Activate Remaining Placeholder Domains

At this stage, Volunteer Operations, Support Delivery, Programs, and Impact can activate in sequence. Each has its prerequisites met.

**Volunteer Operations:** Activates when a volunteer management workflow is defined with operations staff. Depends on volunteer profile requirements emerging from operational experience.

**Support Delivery:** Activates after Case Management is active and an intervention approval workflow exists. Depends on vendor relationships and payment mechanisms being defined.

**Programs:** Activates when a structured program distinct from ad-hoc case-by-case assistance is defined by the client.

**Impact:** Activates after Beneficiary Lifecycle domain is active and sufficient longitudinal data exists to measure change.

---

## Stage 10 — Full Humanitarian Knowledge Graph

When Stages 1–9 are complete, the knowledge layer can reason simultaneously at:

```
Person
    → Lifecycle Stage
    → Capability
    → Risk Trajectory
    → Dependency Chain (caregiver/dependent relationships)

Family
    → Decision-Making Structure
    → Internal Support Capacity
    → Vulnerability Cascade (mother's risk → infant's risk)

Household
    → Composite Vulnerability Score
    → Resilience Factors (assets, social capital, buffering capacity)
    → Need History
    → Intervention History
    → Outcome Record

Community
    → Environmental Risk Profile
    → Service Access Model
    → Seasonal Risk Calendar
    → Aggregate Vulnerability Map

Case
    → Needs (with lifecycle-aware severity)
    → Interventions (with eligibility and fit reasoning)
    → Outcomes (with improvement measurement)
    → Predictive Flags (risk before stated need)
```

**Reasoning capability at this stage:**
- A family presents for food assistance. The system identifies not only food insecurity but that the 6-month-old faces developmental malnutrition risk requiring therapeutic nutrition, distinct from the adults' nutritional hardship.
- An elderly person registers for shelter repair. The system recognises pre-monsoon timing, flood zone location, and single-occupant status, and escalates to emergency preventive response.
- A young adult registers for income support after a father's accident. The system identifies not only the immediate livelihood need but a self-sufficiency pathway based on the person's education level, vocational skills, and the rehabilitation timeline for the injury.
- A community with six households registering in the same month with similar displacement-related needs triggers a programmatic flag for area-level response rather than six separate case-by-case interventions.

---

## Dependency Graph Summary

```
Stage 1: Registration Completion
    (no external prerequisites)
    ↓ enables: Stage 4

Stage 2: Shared Human Model

Completed:
✓ lifecycle-stages.yaml
✓ dependency.yaml
✓ capabilities.yaml
✓ family-structure.yaml
✓ health-conditions.yaml

Stage 2 is considered complete.


Stage 3: Risk Domain
    (requires: Stage 2)
    ↓ enables: Stages 5, 8

Stage 4: Verification Operations
    (requires: Stage 1)
    ↓ enables: Stage 5

Stage 5: Intervention Taxonomy + Case Management
    (requires: Stages 3 + 4)
    ↓ enables: Stage 6

Stage 6: Outcome Indicator Vocabulary
    (requires: Stage 5)
    ↓ enables: Stage 7

Stage 7: Beneficiary Lifecycle
    (requires: Stages 2 + 6)
    ↓ enables: Stage 8

Stage 8: Community Context
    (requires: Stages 3 + 7)
    ↓ enables: Stage 9

Stage 9: Remaining Domain Activations
    (requires: Stage 8 + operational triggers per domain)
    ↓ enables: Stage 10

Stage 10: Full Humanitarian Knowledge Graph
    (requires: Stages 1–9)
```

---

## File Structure Recommendation

The current structure is adequate for the registration domain. It will become unmaintainable at scale without restructuring. The following is the recommended structure for a 10-year knowledge layer.

### Current structure (adequate for now, insufficient for scale)

```
khidmat-knowledge/
├── shared/
│   ├── taxonomy/
│   └── ontology/
├── registration/
│   ├── taxonomy/
│   ├── ontology/
│   ├── reasoning/
│   ├── questioning/
│   ├── verification/
│   ├── gaps/
│   └── readiness/
└── [placeholder domains]
```

### Recommended structure (designed for 10-year scale)

```
khidmat-knowledge/
│
├── shared/
│   ├── taxonomy/
│   │   ├── persons.yaml              [exists — extend]
│   │   ├── organisations.yaml        [exists — extend later]
│   │   ├── locations.yaml            [exists — extend in Stage 3]
│   │   ├── document-types.yaml       [exists]
│   │   └── time.yaml                 [placeholder — complete in Stage 5]
│   │
│   ├── human-model/                  [NEW in Stage 2]
│   │   ├── README.md
│   │   ├── lifecycle-stages.yaml
│   │   ├── capabilities.yaml
│   │   ├── dependency.yaml
│   │   ├── family-structure.yaml
│   │   └── health-conditions.yaml
│   │
│   ├── risk/                         [NEW in Stage 3]
│   │   ├── protective-factors.yaml
│   │   ├── risk-trajectory.yaml
│   │   ├── vulnerability.yaml
│   │   ├── household-resilience.yaml
│   │   └── seasonal-risk.yaml
│   │
│   ├── vocabulary/
│   │   ├── controlled-terms.yaml     [placeholder]
│   │   └── outcome-indicators.yaml   [NEW in Stage 6]
│   │
│   └── ontology/
│       ├── entities.yaml             [placeholder — Person entity in Stage 7]
│       └── relationships.yaml        [placeholder — family relationships in Stage 2]
│
├── registration/                     [complete — maintain as-is]
│   ├── taxonomy/
│   ├── ontology/
│   ├── reasoning/
│   │   ├── detection/                [SPLIT from reasoning/ — Stage 1]
│   │   └── inference/                [SPLIT from reasoning/ — Stage 1]
│   ├── questioning/
│   ├── verification/
│   ├── gaps/
│   └── readiness/
│
├── verification-operations/          [activate in Stage 4]
├── case-management/                  [activate in Stage 5]
├── beneficiary-lifecycle/            [activate in Stage 7]
├── volunteer-operations/             [activate in Stage 9]
├── support-delivery/                 [activate in Stage 9]
├── programs/                         [activate in Stage 9]
├── impact/                           [activate in Stage 9]
│
├── ARCHITECTURE.md                   [update at each stage]
├── DECISIONS.md                      [living document]
└── GLOSSARY.md                       [update at each stage]
```

### Justification for structural changes

**Split `registration/reasoning/` into `detection/` and `inference/`:** These are fundamentally different types of reasoning. Detection rules evaluate what is already known. Inference rules project forward. As the reasoning layer grows, mixing them creates maintenance confusion and makes it harder for agents to know which rules to apply in which context.

**New `shared/human-model/` folder:** The lifecycle, capability, dependency, family, and health condition models are not taxonomy (they are not classification hierarchies) and not ontology (they are not entities or relationships). They are domain models — rich descriptions of how the human domain works. A dedicated folder prevents these from being scattered across taxonomy and ontology files.

**New `shared/risk/` folder:** Risk is a domain of its own, not a subdirectory of shared taxonomy. It has its own reasoning layer, its own vocabulary, and its own output (risk signals). Treating it as a flat YAML file in taxonomy would underrepresent it.

**`shared/vocabulary/outcome-indicators.yaml`:** Outcome indicators must be consistent across case management, programs, and impact domains. They do not belong in any single domain. The shared vocabulary folder is the right home, but it currently has only a placeholder. The outcome indicators file must be a first-class document, not an afterthought.