# FINAL ONTOLOGY CLOSURE PLAN

## 1. Current Ontology Map Reconstruction

### Primitives
The seven primitive categories and boundaries are confirmed (closed set):
1. **Condition**: That which is true across a span and can change.
2. **Context**: The frame relative to which a statement holds.
3. **Epistemic Stance**: The warrant the system holds for what it asserts.
4. **Entity**: That which exists and persists as a distinct whole.
5. **Norm**: That which bounds what is permitted, required, or valid.
6. **Occurrence**: That which happened at a point in time.
7. **Relation**: A connection between things that persist.

### Layers
The eight structural layers derived from primitives are confirmed:
1. **Facets**: Dimensions of variation (Condition + Context).
2. **Entities**: Persisting tracking subjects (Entity).
3. **Relationships**: Connections (Relation).
4. **Constraints**: Permitted/required bounds (Norm + Context).
5. **States**: Values of condition across a span (Condition).
6. **Events**: Point-in-time happenings (Occurrence).
7. **Cognition**: Assertions, claims, confidence (Epistemic Stance).
8. **Coordination Patterns**: Recurring multi-party shapes (Composite).

### Pillars
The seven semantic domains slicing through the layers are confirmed:
I. Human & Social Subject
II. Context & Environment
III. Vulnerability & Need
IV. Epistemics & Knowledge
V. Actors & Ecosystem
VI. Action & Coordination
VII. Resources & Support

### Architecture Rules
- **CCR-1 (Altitude)**: Mandatory
- **CCR-2 (Algorithmic humility)**: Mandatory
- **CCR-5 (Human-oversight trigger)**: Mandatory
- **CCR-6 (Non-linearity)**: Mandatory
- **CCR-7 (Dual-clock)**: Currently Unresolved (G2)
- **CCR-8 (Dignity-as-constraint)**: Mandatory

---

## 2. Open-Item Closure Analysis

### Item 1: CCR-7 — Dual-clock rule

**Current status**: UNRESOLVED per Stage 7 G2. Not enforced as a mandatory constraint. Retained as a documented hypothesis pending further evidence.

**What the ontology currently says**: CCR-7 requires that a person's life-trajectory state and their engagement/administrative state are two separate State tracks and may never collapse into one combined status field.

**Evidence supporting the current model**: Medium-High — BD-TD03-004, >=4 source families (Graduation Approach / BRAC / USAID practice). Stage 5 GT-AR3 supported separating Person from administrative record.

**What is actually unresolved**: Whether architecture MUST enforce two distinct physical clocks / temporal tables for all implementations.

**Is this an ontological uncertainty or an architectural uncertainty?**: It is an architectural uncertainty.

**Can the ontology resolve it now?**: YES.

* **proposed final ontological statement**: A Person's real-world condition and their programmatic engagement state are ontologically distinct and classify under different layers (Condition/States vs Coordination/Events). Implementation mechanics (e.g., temporal databases, dual clocks, event sourcing) are delegated to architecture.
* **exact primitive/layer/pillar/rule affected**: `04-ARCHITECTURE-RULES.md` §4.4 (CCR-7).
* **whether this changes an existing boundary**: No, it clarifies the boundary between ontology (semantic truth) and architecture (technical implementation).
* **whether this introduces a new entity/relation/concept**: No.
* **why it is justified**: It removes an architectural implementation constraint from the ontology layer while preserving the core semantic truth that the Person and the Case are distinct entities with distinct states.

**Closure classification**: CLOSED

### Item 2: Need-to-Need interactions

**Current status**: GENUINELY OPEN (Q16).

**What the ontology currently says**: The general model of how needs relate remains open (`04-ARCHITECTURE-RULES.md` §7.1, `02-ONTOLOGY-LAYERS.md` §12.2). Stage 5 evidence (GT-OQ16) notes interactions are real but should not be a computable Relation.

**Evidence supporting the current model**: RM §7.5 notes needs cascade; GT-OQ16 confirms interactions are captured via case narrative/judgement, not as a structural Relation.

**What is actually unresolved**: Whether to formally add a relation type for Needs.

**Is this an ontological uncertainty or an architectural uncertainty?**: Ontological uncertainty.

**Can the ontology resolve it now?**: YES.

* **proposed final ontological statement**: Need-to-Need interaction is recognized as possible domain reasoning/context (Cognition layer) but is intentionally excluded as a canonical structural Relation in the ontology.
* **exact primitive/layer/pillar/rule affected**: `02-ONTOLOGY-LAYERS.md` §12.2, `04-ARCHITECTURE-RULES.md` §7.1.
* **whether this changes an existing boundary**: Closes a previously open boundary by formally excluding the relationship.
* **whether this introduces a new entity/relation/concept**: No, explicitly prevents introducing one.
* **why it is justified**: Needs are Conditions (P1). Relations (P7) connect persisting Entities (P4). A formal relationship between Needs violates structural boundaries and GT-OQ16 advises against it.

**Closure classification**: CLOSED

### Item 3: Service Providers as Actors

**Current status**: Provisionally REFINED - single-source; retained open pending broader corroboration (Q15).

**What the ontology currently says**: They exist in reality, but whether they act with agency is kept pending (`02-ONTOLOGY-LAYERS.md` L2, `03-ONTOLOGY-PILLARS.md` Pillar V).

**Evidence supporting the current model**: RM §11.3 identifies them. GT-OQ15 states they make independent capacity/eligibility decisions and act with agency.

**What is actually unresolved**: Whether to fully recognize them as active Entities (P4) with agency given limited empirical proof.

**Is this an ontological uncertainty or an architectural uncertainty?**: Ontological uncertainty.

**Can the ontology resolve it now?**: YES.

* **proposed final ontological statement**: Service Providers (clinics, schools, employers) are structurally classified as active Entities (P4) capable of participating in coordination, imposing capacity constraints, and making decisions. This semantic categorization is established, while acknowledging that empirical field evidence remains limited (single-source caveat).
* **exact primitive/layer/pillar/rule affected**: `02-ONTOLOGY-LAYERS.md` §3.1, `04-ARCHITECTURE-RULES.md` §7.1.
* **whether this changes an existing boundary**: Confirms their placement in Entities (L2) and Actors (Pillar V).
* **whether this introduces a new entity/relation/concept**: Confirms an existing tentative entity.
* **why it is justified**: An actor that accepts referrals and manages capacity is an Entity by definition. Semantic categorization does not require exhaustive empirical field evidence to be structurally sound.

**Closure classification**: CLOSED

### Item 4: Outcome / Impact Ownership

**Current status**: `ownership: pending` in L5/L6 and Pillar VI (Q5).

**What the ontology currently says**: Outcome and Impact are States (L5) belonging to the Human Subject. However, the operational ownership of Outcome/Impact Measurement (MEAL vs Case Journey) remains a structural tension.

**Evidence supporting the current model**: RM §12.5 leaves MEAL ownership open. BL V1 §14 implies it is part of Beneficiary Lifecycle.

**What is actually unresolved**: Whether MEAL is a separate workflow capability or part of Case Journey.

**Is this an ontological uncertainty or an architectural uncertainty?**: Architectural uncertainty.

**Can the ontology resolve it now?**: YES.

* **proposed final ontological statement**: Outcome and Impact structurally belong to the Human Subject (Person/Household) as States (L5). The operational responsibility for measuring them (Case Journey workflow vs MEAL team workflow) is an organizational and architectural concern, not an ontological one.
* **exact primitive/layer/pillar/rule affected**: `02-ONTOLOGY-LAYERS.md` §7.3, §9.3; `04-ARCHITECTURE-RULES.md` §7.1 (UHR-3).
* **whether this changes an existing boundary**: Clarifies the boundary between ontology (State ownership) and architecture (Workflow responsibility).
* **whether this introduces a new entity/relation/concept**: No.
* **why it is justified**: It resolves the tension by separating what exists (Outcome) from how an organization operates (MEAL).

**Closure classification**: CLOSED

### Item 5: Funder Altitude

**Current status**: GENUINELY OPEN (Q17). Shape defined by Stage 5 (GT-OQ17); detailed operational rules remain UHR-1 stub.

**What the ontology currently says**: An implied but unevidenced third altitude.

**Evidence supporting the current model**: RM §11.4 implies funders exist and impose constraints. GT-OQ17 provides high-level shape.

**What is actually unresolved**: Whether Funder Coordination requires a new primitive, layer, or altitude mechanism.

**Is this an ontological uncertainty or an architectural uncertainty?**: Ontological and Architectural.

**Can the ontology resolve it now?**: YES.

* **proposed final ontological statement**: Funder Coordination is fully represented using existing layers: Funders are Entities (L2), funding restrictions are Constraints (L4), and ecosystem-level coordination is a Coordination Pattern (L8). No distinct "Funder Altitude" layer or primitive exists.
* **exact primitive/layer/pillar/rule affected**: `04-ARCHITECTURE-RULES.md` §7.1, `02-ONTOLOGY-LAYERS.md` §9.1.
* **whether this changes an existing boundary**: Removes the ambiguity of a potential missing layer.
* **whether this introduces a new entity/relation/concept**: No.
* **why it is justified**: Existing primitives (Entity, Norm) and patterns fully capture the donor ecosystem without necessitating structural additions to the ontology.

**Closure classification**: CLOSED

### Item 6: Case Orchestration

**Current status**: GENUINELY OPEN (Q19). Shape defined by Stage 5 evidence; detailed operational rules remain UHR-1 stub.

**What the ontology currently says**: Whether it represents a standalone capability distinct from Case Management remains open.

**Evidence supporting the current model**: GT-OQ19 defines it as a cross-organisational coordination function.

**What is actually unresolved**: Whether Case Orchestration is a new kind of entity or just a coordination pattern.

**Is this an ontological uncertainty or an architectural uncertainty?**: Ontological/Architectural.

**Can the ontology resolve it now?**: YES.

* **proposed final ontological statement**: Case Orchestration is formally classified as a Coordination Pattern (L8) involving cross-organizational handoffs and gap tracking. It is not a distinct domain primitive or independent entity type. Technical workflow implementation is deferred to architecture.
* **exact primitive/layer/pillar/rule affected**: `04-ARCHITECTURE-RULES.md` §7.1, `02-ONTOLOGY-LAYERS.md` §9.1.
* **whether this changes an existing boundary**: No.
* **whether this introduces a new entity/relation/concept**: No.
* **why it is justified**: Case Orchestration fits perfectly within L8 (Coordination Patterns). Execution routing (who performs it and how) is strictly governed by LCR-7 as an architectural detail.

**Closure classification**: CLOSED

---

## 3. Final Closure Matrix

| Item | Current Status | Ontological Question | Resolution | Final Status | Architecture Impact |
| --- | --- | --- | --- | --- | --- |
| CCR-7 Dual-clock | UNRESOLVED | Is dual-clock an ontology or architecture rule? | Ontological distinction (State vs Event) retained. Implementation mechanism relegated to architecture. | CLOSED | Architecture is free to implement temporal tracking without strictly needing dual databases/clocks. |
| Need-to-Need | STILL OPEN | Should needs relate structurally? | Formally excluded. Need interaction is cognition/documentation, not a structural relation. | CLOSED | No structural recursive need relations require modeling. |
| Service Providers | Provisionally REFINED | Do they have agency (Entity)? | Yes, they are active Entities (L2) with capacity and decision-making ability. | CLOSED | Modeled as Entities (P4) with agency and constraints. |
| Outcome Ownership | ownership: pending | Does Outcome belong to Case Journey or MEAL? | Outcome belongs structurally to Human Subject (States L5). Operational workflow is architectural. | CLOSED | Workflow routing is separated from the domain state definition. |
| Funder Altitude | STILL OPEN | Does funding require a new altitude/layer? | No. Represented via Entities (L2), Norms (L4), and Coordination Patterns (L8). | CLOSED | No third architectural altitude is required. |
| Case Orchestration | STILL OPEN | Is this a new actor/capability? | No. It is a Coordination Pattern (L8). Workflow implementation left to architecture. | CLOSED | Orchestration is implemented via workflow, not domain extensions. |

## 4. FINAL VERDICT

**OPTION A — ONTOLOGY COMPLETE**
All ontological decisions are closed and architecture can begin. The existing ambiguities have been successfully disentangled into solid structural semantics and deferred technical implementation. No unresolved domain question remains that architecture would have to answer.

---

## 5. Precise Implementation Plan

### Change 1: Resolve CCR-7 Dual-Clock Rule
* **File**: `docs/05-ontology/04-ARCHITECTURE-RULES.md`
* **Section**: §4.4 Cross-Cutting Structural Rules (CCR)
* **Current wording**: "Status: UNRESOLVED per Stage 7 G2 (2026-09-01). Not enforced as a mandatory constraint. Retained as a documented hypothesis pending further evidence."
* **Proposed wording**: "Status: RESOLVED (Option A Closure). A person's real-world circumstances (States) and programmatic engagement (Events) are ontologically distinct. The architectural implementation mechanics (e.g., dual physical clocks, temporal tables, event sourcing) are explicitly delegated to architecture rather than mandated by the ontology."
* **Reason**: Separates semantic truth from technical implementation.
* **Source evidence**: GT-AR3 / Stage 7 G2
* **Governance basis**: Option A Handoff
* **Semantics**: Clarifies existing semantics.

### Change 2: Resolve Need-to-Need Interactions
* **File**: `docs/05-ontology/04-ARCHITECTURE-RULES.md`
* **Section**: §7.1 Open Tensions Carried Forward
* **Current wording**: "Need-interaction model ... Stage 5 evidence (GT-OQ16) indicates formal Need?Need Relation should NOT be built; interactions are Cognition/documentation content, not structural Relations"
* **Proposed wording**: Remove from Open Tensions table. Add to §7.2 Structurally Resolved Domain Concept. Concept: Need-interaction model. Structural Classification: Intentional Exclusion. Parameter: Need-to-Need interactions are formally excluded as structural Relations. They exist solely as Cognition/documentation content.
* **Reason**: Need does not meet P7 requirements.
* **Source evidence**: GT-OQ16, RM §7.5
* **Governance basis**: Option A Handoff
* **Semantics**: Clarifies existing semantics.

### Change 3: Resolve Service Providers as Actors
* **File**: `docs/05-ontology/04-ARCHITECTURE-RULES.md`
* **Section**: §7.1 Open Tensions Carried Forward
* **Current wording**: "Service Providers as Actors ... Provisionally REFINED — single-source; retained open pending broader corroboration or explicit Stage 7 ratification"
* **Proposed wording**: Remove from Open Tensions table. Add to §7.2 Structurally Resolved Domain Concept. Concept: Service Providers as Actors. Structural Classification: Entities (P4). Parameter: Structurally modeled as active Entities capable of participating in coordination and making capacity decisions, while retaining a single-source evidence caveat.
* **Reason**: Fits P4 perfectly.
* **Source evidence**: GT-OQ15, RM §11.3
* **Governance basis**: Option A Handoff
* **Semantics**: Clarifies existing semantics.

### Change 4: Resolve Outcome / Impact Ownership
* **File**: `docs/05-ontology/04-ARCHITECTURE-RULES.md`
* **Section**: §7.1 Open Tensions Carried Forward
* **Current wording**: "Outcome/Impact operational ownership (Case journey vs MEAL) ... UHR-3"
* **Proposed wording**: Remove from Open Tensions table. Add to §7.2 Structurally Resolved Domain Concept. Concept: Outcome / Impact Ownership. Structural Classification: States (L5) belonging to Human Subject. Parameter: Operational responsibility for measurement (Case Journey vs MEAL) is explicitly delegated to architecture/workflow design.
* **Reason**: Separates structural domain reality from organizational workflow.
* **Source evidence**: RM §12.5, BL V1 §14, GT-PL6, GT-OQ5
* **Governance basis**: Option A Handoff
* **Semantics**: Clarifies existing semantics.

### Change 5: Resolve Funder Altitude
* **File**: `docs/05-ontology/04-ARCHITECTURE-RULES.md`
* **Section**: §7.1 Open Tensions Carried Forward
* **Current wording**: "Funder Altitude ... shape defined by Stage 5 evidence; detailed operational rules remain UHR-1 stub"
* **Proposed wording**: Remove from Open Tensions table. Add to §7.2 Structurally Resolved Domain Concept. Concept: Funder Altitude. Structural Classification: Modeled via existing layers: Entities (L2), Norms (L4), and Coordination Patterns (L8). Parameter: No distinct third altitude layer or primitive exists.
* **Reason**: Avoids unnecessary structural bloat by mapping to existing primitives.
* **Source evidence**: GT-OQ17, RM §11.4
* **Governance basis**: Option A Handoff
* **Semantics**: Clarifies existing semantics.

### Change 6: Resolve Case Orchestration
* **File**: `docs/05-ontology/04-ARCHITECTURE-RULES.md`
* **Section**: §7.1 Open Tensions Carried Forward
* **Current wording**: "Case Coordination/Orchestration capability status ... shape defined by Stage 5 evidence; detailed operational rules remain UHR-1 stub"
* **Proposed wording**: Remove from Open Tensions table. Add to §7.2 Structurally Resolved Domain Concept. Concept: Case Orchestration. Structural Classification: Coordination Pattern (L8). Parameter: It is not a distinct domain primitive. Technical workflow implementation is deferred to architecture.
* **Reason**: Perfect fit for Coordination Pattern. Workflow is architectural per LCR-7.
* **Source evidence**: GT-OQ19, Stage 4
* **Governance basis**: Option A Handoff
* **Semantics**: Clarifies existing semantics.

## 6. Traceability and Verification
* **Closure Decision**: Proceed to OPTION A.
* **Dependencies**: None.
* **Risks**: By delegating implementation details to architecture, we ensure the ontology is clean, but the architecture team must now make explicit technical choices regarding MEAL workflows and temporal tracking.
* **Verification Criteria**: Validate that the resulting ontology specifies *what exists and what it means* strictly, leaving exactly 0 structural questions forcing architecture to invent domain semantics.
