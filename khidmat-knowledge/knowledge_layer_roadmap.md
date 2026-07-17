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
    ├── volunteer-operations
    ├── support-delivery
    ├── programs
    ├── consent-and-privacy
    └── impact

Missing Entirely

└── Outcome indicators

Canonical (Content Pending)

└── Community Context (12 taxonomy files, full ontology module — migrated onto the
    frozen ontology/taxonomy contract, Phases 1–4 complete; 1 of 18 data properties
    remains an open content gap, see docs/architecture/Community_Context_Migration_Plan.md)

Current Active Phase

└── Phase 4.5 — Needs Assessment Domain (Complete) / Ready for next stage

Already Created

├── Lifecycle model
├── Dependency model
├── Capability model
├── Family structure model
├── Health conditions model
├── Risk Domain (Complete)
├── Verification Operations (Complete)
├── Needs Assessment (Complete)
├── Beneficiary Lifecycle (Complete)
└── Case Management (Complete)
```

**Reasoning capability at current state:** The system can conduct a structured intake conversation, identify needs and claims, detect gaps, assess case readiness, and produce a verification brief. It cannot reason about a person across time, cannot model household resilience, cannot generate preventive signals, and cannot evaluate whether interventions work.

---

## Stage 1 — Complete Registration Domain Foundation

**What this stage completes:**
- Support Intervention Taxonomy (`registration/taxonomy/support-interventions.yaml`)
- Evidence Entity Attributes (`registration/ontology/data-properties.yaml` — evidence section)
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

Phase 4.5 — Needs Assessment Domain (Complete) / Phase 5.0 — Case Management Domain (Complete)

Future Shared Ontology Work:
□ shared human entity promotion model

Current Active Phase:
Ready for next stage

The Shared Human Model prerequisite is now fully satisfied:

✓ lifecycle-stages.yaml
✓ dependency.yaml
✓ capabilities.yaml
✓ family-structure.yaml
✓ health-conditions.yaml

Risk Domain is complete.

**Prerequisites:** Stage 1 should be in progress but need not be complete. The shared human model does not depend on the intervention taxonomy. It does depend on the person base taxonomy in `shared/taxonomy/persons.yaml` which is already mature enough to extend.

**What this enables downstream:** Every subsequent domain that reasons about people, families, households, or life stages depends on this model existing. Without it, each domain invents its own person model, producing incompatible representations of the same human being.

**Reasoning capability gained:** The system can now differentiate a 6-month-old from a 16-year-old not merely by age integer but by lifecycle stage and the developmental expectations, risks, and needs associated with that stage. It can model what a person is capable of (not only what they lack). It can represent that a mother's vulnerability is an infant's vulnerability without requiring a separate registration for the infant.

---
### Current Shared Human Model Status

Completed

* shared/human-model/README.md
* shared/human-model/taxonomy/lifecycle-stages.yaml
* shared/human-model/taxonomy/dependency.yaml
* shared/human-model/taxonomy/capabilities.yaml
* shared/human-model/ontology/family-structure.yaml
* shared/human-model/taxonomy/health-conditions.yaml

Next Active Deliverable

Phase 5.0 — Case Management Domain (Partially Complete)

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
- ✓ Protective Factors Model (`shared/risk/taxonomy/protective-factors.yaml`)
- ✓ Hazard Categories (`shared/risk/taxonomy/hazard-categories.yaml`)
- ✓ Exposure Model (`shared/risk/ontology/exposure.yaml`)
- ✓ Vulnerability Composite Model (`shared/risk/ontology/vulnerability.yaml`)
- ✓ Household Resilience Model (`shared/risk/ontology/household-resilience.yaml`)
- ✓ Risk Model (`shared/risk/ontology/risk.yaml` — folded Risk Trajectory / Trend Model here)
- ✓ Compound Risk Detection (`shared/risk/reasoning/compound-risk-detection.yaml`)

**Prerequisites:**
- Stage 2 complete (Shared Human Model). ✓ Satisfied.
- `shared/taxonomy/locations.yaml` must be extended with geographic hierarchy and environmental risk profile classification. (Deferred to Stage 8 Community Context).

**What this enables downstream:** Case Management domain can reason about intervention urgency. Beneficiary Lifecycle domain can track risk trajectory over time. The Community Context domain depends on the seasonal risk calendar. Predictive flagging becomes possible.

**Reasoning capability gained:** The system can now distinguish "this household is currently in crisis" from "this household is likely to enter crisis within three months." A damaged roof in a flood-zone community before monsoon season becomes a detectable risk. An elderly person living alone with no caregiver during extreme heat becomes a proactive outreach signal. Risk is a first-class concept, not a byproduct of severity rules.

**Important boundary note:** The risk domain produces signals. It does not decide what to do about them. Intervention logic belongs in Stage 5.

---

## Stage 4 — Activate Verification Operations Domain

**STATUS: COMPLETED** (Stage 1 Dependency Anomaly Noted)

**What this stage produces:**
- ✓ Verification Operations core ontology (`verification-operations/ontology/`) [Complete, canonical]
- ✓ Volunteer assignment model [Complete]
- ✓ Field visit outcome model [Complete]
- ✓ Claim confirmation model (result of a verification requirement) [Complete]
- ✓ Evidence collection model [Complete]
- ✓ Re-verification trigger model [Complete]

**Prerequisites:**
- Stage 1 complete (support interventions and evidence taxonomies)
- Registration domain stable in production (per existing placeholder declaration)
- Volunteer field workflow defined with operations staff

**What this enables downstream:** Case Management domain depends on verification operations completing. Without verification outcomes, there is nothing for case management to act on.

**Reasoning capability gained:** The system can now track what happens after case closure. The verification brief produces outcomes. Claims are confirmed or refuted. Cases move beyond the "awaiting verification" state.

---

## Stage 4.5 — Needs Assessment Domain

**STATUS: COMPLETED**

**What this stage produces:**
- ✓ Needs Assessment taxonomy (`needs-assessment/taxonomy.yaml`) [Complete]
- ✓ Needs Assessment ontology (`needs-assessment/ontology.yaml`) [Complete]

**Prerequisites:**
- Stage 4 complete (Verification Operations active) — assessment synthesizes facts and claims.

**What this enables downstream:** Case Management, Support Delivery, Program Management, and Monitoring & Evaluation can now safely reference Needs Assessment.

**Reasoning capability gained:** The system can evaluate what assessments occurred, what findings were produced with explicit epistemic confidence, and what needs were synthesized, decoupling them from operational case management.

---

## Stage 5 — Intervention Taxonomy and Case Management Domain

**STATUS: PARTIALLY COMPLETED** (Case Management domain complete; Intervention taxonomy pending operational input)

**What this stage produces:**
- [Pending] Completed Support Intervention Taxonomy (operationally validated by programme staff)
  - Intervention type hierarchy
  - Eligibility conditions per intervention type
  - Typical duration norms
  - Contraindications (circumstances where an intervention type is inappropriate)
- [Complete] Case Management domain — full Level 1 implementation
  - Case taxonomy and ontology (Complete)

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

**STATUS: COMPLETED**

**Completed:**
- ✓ Beneficiary Lifecycle taxonomy (`beneficiary-lifecycle/taxonomy/`)
- ✓ Beneficiary Lifecycle ontology (`beneficiary-lifecycle/ontology/`)
- □ Persistent Person entity in `shared/ontology/entities.yaml` (promoted from beneficiary snapshot) [Pending]

**Prerequisites:**
- Stage 2 complete (Shared Human Model — lifecycle stages, capability)
- Stage 6 complete (Outcome Indicator vocabulary)
- At least two complete registrations for returning beneficiaries must exist in production (per existing placeholder declaration)

**What this enables downstream:** Impact domain depends on longitudinal data. Community Context domain uses aggregate lifecycle data for area-level vulnerability mapping.

**Reasoning capability gained:** The system can now reason about a person across time. It can identify that a household receiving assistance for the third time has not improved, suggesting the intervention type is wrong. It can flag that a child who was in school at first registration has dropped out by second registration. The person has a history, not just a snapshot.

---

## Stage 8 — Community Context Domain

**Note:** Substantial Community Context content already exists (`community-context/taxonomy/*`,
12 files, and a full `ontology/` module). Migration to the frozen
`Canonical_Ontology_Schema.md` / `Canonical_Taxonomy_Schema.md` contract is
complete through Phase 4 (`docs/architecture/Community_Context_Migration_Plan.md`)
— Community Context is the second domain, after Registration, migrated onto both
contracts, and the second to reach **Canonical (Content Pending)** status. All
entities, relationships, constraints, and taxonomy schemes are canonical; 17 of 18
implied data properties are authored. One property
(`transportation_network_asset.surface_condition`) awaits a domain-knowledgeable
author to define a new taxonomy scheme. Phase 5 CURIE linking is blocked on the
repository-wide manifest like every domain.

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

**Volunteer Operations:** Its **foundational** (organization-invariant) ontology and taxonomy are **already authored** under ADR-024 — maturity *Canonical (Foundational) — Operational Deferred*. The Stage-9 trigger now gates **only the operational/runtime layer** (Tier 2): scheduling, dispatch, routing, workload balancing, optimization, trust/performance scoring, the assignment act, and per-instance assignment/training history. That layer activates when a volunteer management workflow is defined with operations staff and volunteer profile requirements emerge from operational experience.

**Support Delivery:** Activates after Case Management is active and an intervention approval workflow exists. Depends on vendor relationships and payment mechanisms being defined.

**Programs:** Activates when a structured program distinct from ad-hoc case-by-case assistance is defined by the client.

**Impact:** Activates after Beneficiary Lifecycle domain is active and sufficient longitudinal data exists to measure change.

---

## HKMP Stage 8 — Donor & Resource Domain (Distinct Numbering Track)

**Numbering disambiguation:** this entry uses the "HKMP Stage N" numbering established during
subsequent phases of development — a separate, later-established numbering track from this document's own
"Stage 8: Community Context" / "Stage 9: Activate Remaining Placeholder Domains" above, which are
unrelated and already complete. The two numbering tracks happen to collide at the digit 8 while
referring to different work.

**HKMP Stage 8B — Donor & Funding Intelligence** (requires: Programs, Shared Ontology — both
already active). Produces `donor_profile`, `grant`, `contribution`, the Islamic Giving taxonomy
(zakat, sadaqah, sadaqah_jariyah, waqf, fidya, kaffarah, qurbani, and the eight zakat-eligible
asnaf categories), and funding lifecycle vocabulary (grant status, contribution status, renewal,
funding window, restriction reference).
↓ enables: HKMP Stage 8C

**HKMP Stage 8C — Material Resource & Logistics Intelligence** (requires: HKMP Stage 8B, Programs,
Case Management, Shared Ontology — all already active; boundary held with Support Delivery at the
custody/dispatch line). Produces `resource` (abstract) → `financial_resource`/`material_resource`,
`inventory_item`, `storage_location`, `resource_allocation`, and their supporting taxonomies
(resource classification, stock movement, storage, allocation).
↓ enables: Support Delivery's `delivery_event_fulfilled_from_resource_allocation` reference row

**HKMP Stage 8D — Governance Integration** (requires: HKMP Stage 8B + 8C complete). Ratifies
ADR-025 through ADR-028, integrates the domain into `ontology_authority_matrix.md` and
`GLOSSARY.md`, and authors the one Support Delivery-side reference row anticipated since Stage 8A's
architecture design. **Complete** — see `donor-resource/` and ADR-025 through ADR-028.

**Reasoning capability gained:** The system can now reason about who funds Khidmat's operations and
under what restriction (including Islamic-giving-specific restrictions), and about what material
and financial resources exist in stock and are committed to a program or case plan before delivery
executes. A zakat-restricted grant's eligible-recipient categories are expressible and
distinguishable from a Program's general eligibility rules; a delivery event can be traced back to
the specific pre-delivery allocation decision that reserved the stock it fulfils.

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
    ↓ enables: Stage 4.5

Stage 4.5: Needs Assessment
    (requires: Stage 4)
    ↓ enables: Stage 5

Stage 5: Intervention Taxonomy + Case Management
    (requires: Stages 3 + 4.5)
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
│   │   └── time.yaml                 [complete]
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
├── needs-assessment/                 [complete]
├── case-management/                  [activate in Stage 5]
├── beneficiary-lifecycle/            [activate in Stage 7]
├── volunteer-operations/             [foundational authored (ADR-024); operational layer activates in Stage 9]
├── support-delivery/                 [activate in Stage 9]
├── programs/                         [activate in Stage 9]
├── consent-and-privacy/              [activate in Stage 9]
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