# STAGE 6 — EVIDENCE INTEGRATION REPORT

## 1. Repository Understanding
The following authoritative files were inspected to establish the baseline ontology and review the Stage 5 evidence:
- **`docs/05-ontology/01-DOMAIN-PRIMITIVES.md`**: Defines the 7 fundamental building blocks (Condition, Context, Epistemic Stance, Entity, Norm, Occurrence, Relation).
- **`docs/05-ontology/02-ONTOLOGY-LAYERS.md`**: Defines the 8 structural layers combining primitives (Facets, Entities, Relationships, Constraints, States, Events, Cognition, Coordination Patterns).
- **`docs/05-ontology/03-ONTOLOGY-PILLARS.md`**: Defines the 7 semantic pillars that organize the ontology.
- **`docs/05-ontology/04-ARCHITECTURE-RULES.md`**: Outlines the governing architectural rules for implementation.
- **`docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md`**: Provides the structural index of all 47 open questions and structural reviews.
- **`docs/05-ontology/GT-*-R1.md`**: 47 individual Ground Truth Review records containing practitioner evidence.

## 2. Ontology Baseline

**Domain Primitives**
1. Condition: That which is true across a span and can change.
2. Context: The frame relative to which a statement holds.
3. Epistemic Stance: The warrant the system holds for what it asserts.
4. Entity: That which exists and persists as a distinct whole.
5. Norm: That which bounds what is permitted, required, or valid.
6. Occurrence: That which happened at a point in time.
7. Relation: A connection between things that persist.

**Layers**
1. Facets
2. Entities
3. Relationships
4. Constraints
5. States
6. Events
7. Cognition
8. Coordination Patterns

**Pillars**
I. Human & Social Subject
II. Context & Environment
III. Vulnerability & Need
IV. Epistemics & Knowledge
V. Actors & Ecosystem
VI. Action & Coordination
VII. Resources & Support

**Architecture Rules (Domain Content)**
- CCR-1: Altitude qualification
- CCR-2: Algorithmic humility
- CCR-5: Human-oversight trigger
- CCR-6: Non-linearity
- CCR-7: Dual-clock rule
- CCR-8: Dignity-as-constraint

## 3. Ground Truth Baseline
Summary of all 47 Review IDs by classification:
- **CONFIRMED**: 29
- **REFINED**: 15
- **CHALLENGED**: 2
- **UNRESOLVED**: 1

## 4. Domain Primitive Impact Map

| Primitive | Relevant GT IDs | Impact / Treatment | Governance Required? |
|---|---|---|---|
| P1: Condition | GT-P1, GT-OQ9, GT-OQ11, GT-OQ2 | Validates Condition as distinct from Occurrence. "Need" and "Risk" are emergent Conditions. **Treatment: KEEP/REFINE** | No |
| P2: Context | GT-P2, GT-OQ11, GT-OQ4 | Confirms Context modulates Condition meaning and Facet values. **Treatment: KEEP** | No |
| P3: Epistemic Stance | GT-P3, GT-OQ10, GT-OQ12, GT-OQ13 | Must support "unknown", source attribution, and conflict retention. **Treatment: REFINE** | No |
| P4: Entity | GT-P4, GT-OQ1, GT-OQ3, GT-OQ6, GT-OQ15 | Requires distinction between Person, ID, and administrative record. Tension around Org vs Programme. **Treatment: REFINE** | Yes (Org/Prog) |
| P5: Norm | GT-P5, GT-OQ8, GT-OQ14 | Confirms Norm bounds operations (consent, donor restrictions, safeguarding). **Treatment: KEEP** | No |
| P6: Occurrence | GT-P6, GT-OQ9 | Distinct from persistent conditions; captures events like referrals. **Treatment: KEEP** | No |
| P7: Relation | GT-P7, GT-OQ16, GT-OQ18 | Vital for kinship/dependency. Needs interact but don't strictly require formal Relations. **Treatment: KEEP/REFINE** | No |

## 5. Layer Impact Map

| Layer | Relevant GT IDs | Impact / Treatment | Governance Required? |
|---|---|---|---|
| L1: Facets | GT-L1, GT-OQ4 | Independently variable axes. Values defined by context/programmes. **Treatment: REFINE** | No |
| L2: Entities | GT-L2, GT-OQ3, GT-OQ6, GT-OQ15, GT-OQ7 | Distinct entities (Person, Family, Household, Provider, Donor). Conflict on Org/Programme. **Treatment: REFINE** | Yes (Org/Prog) |
| L3: Relationships | GT-L3, GT-OQ18 | Social relationships (kinship, guardian, household member) must remain distinct. **Treatment: KEEP** | No |
| L4: Constraints | GT-L4 | Must support concurrent, conflicting Norms and human resolution. **Treatment: KEEP** | No |
| L5: States | GT-L5, GT-OQ5 | Longitudinal tracking is crucial. Outcome ownership belongs here, not just Events. **Treatment: REFINE** | No |
| L6: Events | GT-L6 | Dateable sequence of programme-relevant occurrences. **Treatment: KEEP** | No |
| L7: Cognition | GT-L7, GT-OQ12 | Open-world commitment is strictly required. Blank != No. **Treatment: KEEP** | No |
| L8: Coordination | GT-L8, GT-OQ17, GT-OQ19 | Handoffs, referrals, funder coordination, case orchestration are distinct patterns. **Treatment: EXTEND** | No |

## 6. Pillar Impact Map

| Pillar | Relevant GT IDs | Impact / Treatment | Governance Required? |
|---|---|---|---|
| I: Human/Social Subject | GT-PL1 | Boundary separating identity from external environment is valid. **Treatment: KEEP** | No |
| II: Context/Environment | GT-PL2 | Context modulates interpretation of physical observations into programmatic needs. **Treatment: KEEP** | No |
| III: Vulnerability/Need | GT-PL3, GT-OQ2, GT-OQ11 | Vulnerability/Need are emergent combinations determined by local norms, not universal formulas. **Treatment: REFINE** | No |
| IV: Epistemics/Knowledge | GT-PL4, GT-OQ10, GT-OQ13 | Must retain multiple competing claims, sources, and verification status without deletion. **Treatment: REFINE** | No |
| V: Actors & Ecosystem | GT-PL5, GT-OQ6 | Field practice requires separating Organisation and Programme; Tier 1 collapsed them. **Treatment: CHALLENGED** | Yes |
| VI: Action/Coordination | GT-PL6, GT-OQ5 | Case closure does not equal outcome achievement. They operate on different timelines. **Treatment: KEEP** | No |
| VII: Resources/Support | GT-PL7 | Need addressed, delivery modality, and support phase are distinct dimensions. **Treatment: KEEP** | No |

## 7. Architecture Rule Impact Map

| Rule | Relevant GT IDs | Impact / Treatment | Governance Required? |
|---|---|---|---|
| CCR-1: Altitude | GT-AR1 | Confirmed. Activities typed by case vs. programme altitude to prevent conflation. **Treatment: KEEP** | No |
| CCR-2: Algorithmic Humility | GT-AR6 | Confirmed. Uncertain algorithmic conclusions need human verification states. **Treatment: KEEP** | No |
| CCR-5: Human Oversight | GT-AR4 | Confirmed. Must capture human attribution for consequential decisions. **Treatment: KEEP** | No |
| CCR-6: Non-linearity | GT-AR2 | Confirmed. Person persists across multiple non-linear case journeys. **Treatment: KEEP** | No |
| CCR-7: Dual-clock | GT-AR3 | Unresolved. Evidence suggests separation of Person from admin status, but lacks full proof. **Treatment: UNRESOLVED** | No |
| CCR-8: Dignity-as-constraint | GT-AR5 | Confirmed. Safeguarding modeled as Norm, not just numerical Condition. **Treatment: KEEP** | No |

## 8. Cross-Cutting Findings

1. **Epistemic Status & Humility**: Pervasive requirement across multiple primitives (Cognition, Epistemics, Events). "Unknown" vs "No", source attribution, retention of contradictory claims, and algorithmic uncertainty require structural support.
2. **Context Dependency**: A single objective condition (e.g., damaged roof) can yield multiple different assessments (Need/Risk) depending on the local Programme or seasonal context.
3. **Temporal Persistence**: Entities (Person) persist independently of administrative cases. Conditions persist across a span; Events happen at a point. History must be preserved for longitudinal reassessment.
4. **Organisation vs. Programme**: A major structural tension exists between Tier 1 authority (which collapses them) and field practice (which treats an Organisation operating multiple discrete Programmes).
5. **Outcome vs. Case Closure**: Administrative case closure does not imply an outcome was achieved. Outcome measurement operates on a separate timeline.
6. **Compound Vulnerability**: Vulnerability is an emergent property, computed locally by practitioner judgment and context rules, not a universal ontological equation.
7. **Actors as Service Providers**: Service providers are active Entities with their own capacity constraints and rules, not passive contextual attributes.

## 9. Stage 7 Governance Candidates

| Issue | Evidence / Conflict | Options & Architectural Consequences | Why Governance is Required |
|---|---|---|---|
| **Organisation vs. Programme** (GT-OQ6, GT-PL5) | Tier 1 authority collapses them (Business Logic V1). Practitioner evidence strongly requires separating an Organisation from its multiple Programmes. | **Opt 1**: Preserve Tier 1 (Collapsed). Consequence: Inability to track distinct eligibility criteria per programme. <br>**Opt 2**: Split into two Entities. Consequence: Breaks Tier 1 alignment, requires ontology restructure. | Direct conflict between formal Tier 1 authority and grounded practitioner reality. Stage 6 cannot unilaterally override Tier 1. |

## 10. Proposed Stage 6 Change Register

| ID | Ontology Component | Current State | Proposed Treatment | Reason | Governance Required? |
|---|---|---|---|---|---|
| C1 | Epistemic Stance (P3) / Cognition (L7) | Open-world commitment established; representation open. | **REFINE** | Mandate explicit epistemic property (Unknown, Not Assessed, Source ID) on relevant state records. | No |
| C2 | Entity (P4) / L2 | Organisation and Programme collapsed. | **CHALLENGE** | Practitioner evidence requires split; conflicts with Tier 1. | Yes |
| C3 | States (L5) | Outcome ownership open. | **REFINE** | Assign Outcome ownership to L5 (States) rather than L6 (Events) with distinct epistemic timelines. | No |
| C4 | Entities (L2) | Service Providers modeled loosely. | **REFINE** | Structurally model Service Providers as active Entities, not contextual locations. | No |
| C5 | Coordination (L8) | Funder/Orchestration patterns stubbed. | **EXTEND** | Formalize Funder coordination and Case Orchestration as distinct pattern types. | No |
| C6 | Constraint (L4) / Norm (P5) | Consent/Safeguarding open. | **REFINE** | Model Consent and Funding Restrictions explicitly as Norms that bound actions, not just conditions. | No |
| C7 | Need/Vulnerability | Open composition. | **REFINE** | Define Need as an emergent `State` shaped by `Context`, rejecting universal calculation models. | No |
| C8 | Architecture Rule CCR-7 | Unresolved by GT. | **UNRESOLVED** | Insufficient evidence to formally enshrine the Dual-clock rule from ground truth alone. | No |
