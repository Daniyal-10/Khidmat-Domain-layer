# STAGE 6 — EVIDENCE INTEGRATION REPORT (GTR SESSION 01)

## 1. Purpose
This document formally integrates real practitioner evidence from Khidmat (GTR Session 01) into the humanitarian ontology process. It evaluates what the evidence establishes about existing ontology assumptions, separating raw practitioner statements (Level 1) from semantic interpretation (Level 2) and potential ontology implications (Level 3). It does not perform ontology refinement or governance.

## 2. Evidence Sources
**Highest Priority (Real Practitioner Evidence):**
* `DOMAIN Gathering/all_answers.md`
* `DOMAIN Gathering/ORGANIZED-GTR-SESSION-01.md`

**Baseline Models (for comparison):**
* `01-DOMAIN-PRIMITIVES.md`, `02-ONTOLOGY-LAYERS.md`, `03-ONTOLOGY-PILLARS.md`, `04-ARCHITECTURE-RULES.md`

## 3. Evidence Method
This analysis maintains strict evidentiary boundaries:
1. **Level 1 — Practitioner Evidence:** What the expert explicitly stated.
2. **Level 2 — Semantic Interpretation:** What can be reasonably inferred from the evidence.
3. **Level 3 — Ontology Implication:** Potential refinement signals for the ontology (subject to governance).

## 4. Session 01 Context
The practitioner operates within a specific, grassroots, volunteer-based organization in the Bhopal area. The organization uses a direct volunteer-to-donor matchmaking model. It explicitly excludes seasonal or pandemic disaster situations from its core workflow. **Findings are localized to this context and are not automatically universalized.**

## 5. Review-ID Disposition

| Review ID | Disposition | What is Established | What Remains Unknown |
|---|---|---|---|
| GT-L1, GT-P1, GT-L5 | ANSWERED | Ground verification process exists and corrects survey claims. | N/A |
| GT-OQ3, GT-L2 | ANSWERED | Zimmedar (head) acts for family; distinct entities for Donor/Provider. | N/A |
| GT-OQ15, GT-OQ7 | ANSWERED | Specific eligibility rules (zakat, govt hospital provision) apply. | N/A |
| GT-OQ8, GT-OQ11 | ANSWERED | Needs attach to individuals or families contextually. | N/A |
| GT-L8, GT-OQ19, GT-PL7 | ANSWERED | Direct donor adoption and vendor fulfillment mechanisms. | N/A |
| GT-L6, GT-P6, GT-AR2 | ANSWERED | Tracking cards with signatures used as delivery evidence. | N/A |
| GT-OQ4, GT-PL1 | ANSWERED | Needs have varying temporal spans (recurring vs one-time). | N/A |
| GT-PL5, GT-OQ6 | ANSWERED | Khidmat operates without nested programmes. | Universality across domain. |
| GT-OQ17 | ANSWERED | Micro-donor matchmaking environment is active. | Universality across domain. |
| GT-OQ1 | PARTIALLY_ANSWERED | Reverification for recurring needs occurs. | Seasonal handling (excluded from context). |
| GT-P4 | PARTIALLY_ANSWERED | Unique Beneficiary IDs resolve identity mismatch. | Full person vs admin case separation. |
| GT-AR6 | PARTIALLY_ANSWERED | Volunteers provide human check over initial survey. | Algorithmic intervention handling. |
| GT-P2, GT-PL2 | PARTIALLY_ANSWERED | Context modulates support rules. | Exact facet definitions. |
| GT-OQ2, GT-PL3, GT-OQ9 | PARTIALLY_ANSWERED | Vulnerability based on compound factors (widow, no income). | Exact risk formulas. |
| GT-P7, GT-L3 | PARTIALLY_ANSWERED | Family/household relations are recorded. | Complex cascading dependencies. |
| GT-L7, GT-P3, GT-OQ10 | PARTIALLY_ANSWERED | Volunteer check & govt proofs separate claim from verified fact. | Exact handling of "Unknown/Unable to determine". |
| GT-OQ12 | PARTIALLY_ANSWERED | False claims rejected; genuine ones proceed. | "Unknown" handling (expert says not much required). |
| GT-OQ5, GT-PL6 | PARTIALLY_ANSWERED | One-time needs are closed after help; recurring ones continue. | Complex outcome timelines. |
| GT-OQ14 | PARTIALLY_ANSWERED | Donor limits applied so beneficiary doesn't become dependent. | Safeguarding vs Score formulas. |
| GT-P5 | PARTIALLY_ANSWERED | Norms (zakat eligibility) restrict action. | Full constraint resolution mechanics. |
| GT-OQ16, GT-OQ18 | UNANSWERED | N/A | Interaction between explicitly blocked needs. |
| GT-PL4, GT-OQ13, GT-AR4 | UNANSWERED | N/A | Conflicting source resolution. |
| GT-AR3 | UNANSWERED | N/A | Status vs Reality (Dual-clock) mismatch. |
| GT-L4 | UNANSWERED | N/A | Conflicting rule resolution. |
| GT-AR5 | UNANSWERED | N/A | Dignity vs Score. |
| GT-AR1 | NOT_ASSESSABLE | Khidmat operates at a single altitude. | Altitude qualification. |

## 6. Major Practitioner Findings

1. **Identity:** Beneficiaries require unique IDs to solve identity mismatches; government proofs (Aadhar, Ayushman) are collected.
2. **Family vs. Individual:** General needs (food) attach to the family head (Zimmedar); specific needs (medical, orphans) attach to individuals.
3. **Vulnerability:** Poverty, widowhood, lack of income, and accidental injuries compound to raise priority.
4. **Evidence/Verification:** Initial surveys are treated as claims. Experienced volunteers do physical ground-reality checks. Government hospital docs are trusted (no double verification). Totally false claims are rejected, genuine requirements proceed, and surveyed needs that differ from actual needs can be corrected based on ground reality. Multiple needs can have different genuine/non-genuine outcomes. No second survey is performed. Unknown/unable-to-determine remains unresolved.
5. **Needs:** Reported requirements can be corrected, partially approved, or totally rejected based on ground checks.
6. **Fulfillment:** Delivery uses physical tracking cards with signatures. Donors directly adopt cases, combine, or split support. Vendors provide direct fulfillment.
7. **Recurrence:** Distinction between one-time needs (medical bills) which close, and recurring needs (monthly rations) which require reverification.
8. **Coordination:** First-come-first-serve donor matching via messaging groups; lead verification by volunteers.
9. **Programme:** Khidmat explicitly does not use nested programmes.
10. **Constraints:** Donor limits are enforced to prevent over-dependence; seasonal/pandemic issues are out of scope.

## 7. Evidence vs Semantic Interpretation

| Level 1: Observed Reality | Level 2: Semantic Interpretation | Level 3: Potential Ontology Impact |
|---|---|---|
| "Volunteer goes to the ground and checks the requirement... reject false, correct, or proceed." | A candidate semantic interpretation is that the workflow distinguishes reported information from information supported by verification. | Refinement signal: The ontology may require Epistemic Stance mechanisms on States to distinguish claims from verified findings (Requires Stage 7 consideration). |
| "General needs head of family, specific needs individual members." | A possible semantic interpretation is that Need entities may attach flexibly to either Person or Family entities. | Refinement signal: Support for non-linear Relation and Entity mappings may be a candidate ontology implication. |
| "Government hospital reports considered true only." | Some evidentiary sources are intrinsically trusted without secondary ground checks. | Refinement signal: Source-trust properties on Epistemic claims may be a candidate ontology implication. |
| "No organisations and programs are involved... just Khidmat grp doing the root work." | The specific operating context lacks a distinct Programme layer above the case. | Context-specific observation; this may challenge the applicability of the Tier 1 Organisation/Programme collapse and requires Stage 7 consideration. |
| "Donors adopt the beneficiary... can combine or split." | Financial coordination happens at the direct case level in this context. | Refinement signal: A Coordination pattern for direct micro-funders may be a candidate ontology implication. |

## 8. Session 01 vs Existing Ontology
The Session 01 evidence provides support for the ontology's proposed distinct Epistemic Stances, flexible Entity attachment, and distinct Coordination patterns. However, it raises questions about the generalization of nested Programmes and highlights remaining evidence gaps in handling true "Unknown" states and conflicting sources (which the practitioner simply avoids or resolves manually on the ground).

## 9. Eight-Layer Evidence Analysis

| Layer | Session 01 Evidence | Existing Coverage | Evidence Assessment | Potential Impact |
|---|---|---|---|---|
| 1. Facets | Context limits to non-seasonal, local poverty. | Context modules meaning. | ALREADY REPRESENTED | NO MATERIAL IMPACT |
| 2. Entities | Uses Person, Family, Vendor, Donor. | Supports these entities. | ALREADY REPRESENTED | NO MATERIAL IMPACT |
| 3. Relationships | Zimmedar represents family. | Relations handle kinship. | ALREADY REPRESENTED | NO MATERIAL IMPACT |
| 4. Constraints | Donor limits, Zakat rules. | Norms bound operations. | REFINEMENT SIGNAL | Refinement signal: Potential need to formalize rule-based capacity constraints. |
| 5. States | Needs are recurring vs one-time. | Persistent vs Occurrence. | REFINEMENT SIGNAL | Refinement signal: Potential need to represent temporal recurrence patterns. |
| 6. Events | Ground verification, tracking card signature. | Events alter States. | REFINEMENT SIGNAL | Refinement signal: Verification events may need to distinctly alter Epistemic Stance. |
| 7. Cognition | Correcting a survey claim via ground check. | Open-world stance. | REFINEMENT SIGNAL | Refinement signal: A potential mechanism to distinguish a claim from a verified finding may be required. |
| 8. Coordination | Direct donor matching, vendor fulfillment. | Funder/Orchestration. | REFINEMENT SIGNAL | Refinement signal: Potential formalization of Micro-donor coordination pattern. |

## 10. Ontology Refinement Signals

| Refinement Signal (NOT AN ONTOLOGY DECISION) | Evidence | Review IDs | Relevant Layer(s) | Why It Matters | Confidence | Governance Required? |
|---|---|---|---|---|---|---|
| Verification Epistemics | Volunteer corrects/rejects initial survey. | GT-L1, GT-P1, GT-L7 | L7 (Cognition), L6 (Events) | Separation of reported claim from verified finding may be crucial for data integrity. | High | No |
| Entity Need Attachment | General needs to family, specific to individual. | GT-OQ8, GT-OQ11 | L2 (Entities), L3 (Relationships) | May prevent rigid single-entity need modeling. | High | No |
| Recurring vs One-time | Monthly rations vs medical bill. | GT-OQ4, GT-PL1 | L5 (States) | May dictate reverification cycles and closure rules. | High | No |
| Trusted Source Evidence | Govt hospital proof accepted as true. | GT-OQ10 | L7 (Cognition) | May prevent redundant verification; may introduce source-trust weighting. | Medium | No |
| Direct Coordination | Donor adoption, vendor fulfillment. | GT-L8, GT-OQ19 | L8 (Coordination) | Provides evidence for the existence of decentralized micro-coordination in humanitarian work. | High | No |

## 11. Context-Specific Findings
* **No nested programmes:** The lack of programmes is specific to grassroots Khidmat; it does not establish that Programme does not exist across the humanitarian ontology.
* **Scope exclusions:** Ignoring seasonal/pandemic disasters is a localized policy.
* **WhatsApp/Messaging matching:** The specific use of messaging apps is an implementation detail, not a universal Coordination pattern (though the pattern of "Direct Matchmaking" is).

## 12. Contradictions / Challenges
* **Programme Altitude:** Khidmat's grassroots reality (no programmes) contradicts the Tier 1 Business Logic assumption that everything sits under a Programme. This is a governance candidate: Stage 7 must determine how to reconcile the Tier 1 baseline with this organizational context without prematurely forcing an architectural choice.

## 13. Remaining Evidence Gaps

| Review ID | What Session 01 Established | What Remains Unknown | Why It Matters | Session 02 Question |
|---|---|---|---|---|
| GT-OQ12 | False claims rejected. | "Unknown" handling. | System needs state for unverified claims. | "When a volunteer is absolutely unsure if a claim is true or false, how is it recorded?" |
| GT-AR3 | Needs are verified. | Status vs Reality mismatch. | Dual-clock validation. | "Have you ever had a case where the tracking card said 'delivered' but the beneficiary claimed they didn't receive it?" |
| GT-PL4 | Verification checks survey. | Conflicting source resolution. | Conflict algorithms. | "What happens when two different volunteers disagree on a family's needs?" |

## 14. Session 02 Follow-up Requirements
1. Further investigate "unknown" state handling.
2. Investigate conflicting sources and manual overrides.
3. Clarify boundary constraints (Dignity vs Score).

## 15. Required / Desired Artifacts
* Khidmat Form = E1 practitioner testimony / description (unless actual artifact evidence is inspected).
* Blank Tracking Card = E1 practitioner testimony / description (unless actual artifact evidence is inspected).
* Anonymized Case Summary example = E1 practitioner testimony / description (unless actual artifact evidence is inspected).

## 16. Governance-Required Items
* **Organisation vs. Programme Structure:** Stage 7 must consider how to address the structural tension between the Tier 1 collapsed model and grassroots realities like Khidmat's, without prematurely forcing an architectural choice.

## 17. Stage 6 Conclusions
Session 01 provides robust Level 1 evidence that supports the exploration of distinct Epistemic Stance separation, flexible temporal states, and direct coordination patterns. It answers 20 Review IDs and partially answers 18 others, leaving 8 unanswered and 1 not assessable (Total 47). Critical gaps remain regarding conflicting sources and "unknown" states. The major structural tension regarding the absence of "Programmes" is isolated as a context-specific finding that triggers a formal Stage 7 Governance requirement.

## 18. Explicit Boundary: No Ontology Refinement Performed
**No ontology semantics, primitives, layers, pillars, or architecture rules have been modified during this integration task.** The findings above are Refinement Signals and Governance Candidates only.

---

# APPENDIX: PRE-GTR-SESSION-01 HISTORICAL STAGE 6 REPORT

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
