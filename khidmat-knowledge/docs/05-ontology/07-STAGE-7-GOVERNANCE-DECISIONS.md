# Stage 7 — Governance Decisions

## 1. Purpose
Execute Stage 7 Governance Decisions for the Khidmat Humanitarian Ontology using the completed and committed Stage 6 Evidence Integration from GTR Session 01. This task determines what practitioner evidence is authorized to influence ontology refinement, what is deferred, and what is context-specific. It does NOT modify the ontology.

## 2. Governance Principles
Every governance decision traces from Evidence → Semantic interpretation → Potential ontology impact → Governance decision → Rationale. No decision is based on intuition, software convenience, or unsupported generic assumptions. The Minimum-Change Principle applies.

## 3. Inputs
* `docs/05-ontology/06-STAGE-6-EVIDENCE-INTEGRATION-REPORT.md` (Primary)
* Practitioner evidence (`all_answers.md`, `ORGANIZED-GTR-SESSION-01.md`)
* Existing ontology baseline (`01-DOMAIN-PRIMITIVES.md`, `02-ONTOLOGY-LAYERS.md`, etc.)

## 4. Decision Framework
**Governance Authorization Boundary:** "Accept for Refinement" authorizes an issue for evaluation during the subsequent Ontology ↔ Ground Truth Reconciliation phase. It does not authorize a specific ontology construct, ontology modification, architectural change, or implementation mechanism. Any actual ontology change requires a subsequent reconciliation decision supported by evidence and governed under the project's minimum-change principle.

* **ACCEPT FOR REFINEMENT**: Authorized for consideration during the subsequent Ontology ↔ Ground Truth Reconciliation phase. Does NOT mean modify ontology now.
* **DEFER — MORE PRACTITIONER EVIDENCE REQUIRED**: Evidence insufficient.
* **CONTEXT-SPECIFIC**: Finding valid for observed context but not generalizable without broader evidence.
* **RETAIN AS EXISTING MODEL**: Existing ontology suffices.
* **REJECT AS ONTOLOGY CHANGE**: Evidence does not justify ontology change.
* **ESCALATE FOR GOVERNANCE**: Requires explicit structural resolution.

## 5. Session 01 Governance Decisions

### 5.1 Verification / Reported Information
* **Issue**: Reported requirement vs ground-reality verification.
* **Evidence**: Initial survey claims are checked by volunteers. Claims can be totally false (rejected), genuine (proceed), or differ from reality (corrected).
* **Disposition**: **ACCEPT FOR REFINEMENT**
* **Rationale**: The workflow establishes a genuine semantic distinction between reported information and verified information, raising the question of whether the existing ontology is sufficient.
* **Action**: Authorized for consideration during the subsequent Ontology ↔ Ground Truth Reconciliation phase.

### 5.2 Epistemic Status
* **Issue**: Epistemic status / verification.
* **Evidence**: Ground-reality checking or trusted sources (government hospitals) separate claims from verified facts.
* **Disposition**: **ACCEPT FOR REFINEMENT**
* **Rationale**: Candidate representations, including epistemic distinctions, may be evaluated during reconciliation if the existing ontology is insufficient.
* **Action**: Authorized for consideration during the subsequent Ontology ↔ Ground Truth Reconciliation phase.

### 5.3 Unknown Verification
* **Issue**: Unknown / unable-to-determine state handling.
* **Evidence**: Practitioner noted this is rare and remains unresolved.
* **Disposition**: **DEFER — MORE PRACTITIONER EVIDENCE REQUIRED**
* **Rationale**: Practitioner evidence does not establish operational handling.
* **Action**: Meeting 2+ must ask: "How is a claim recorded when a volunteer is absolutely unsure if it is true or false?"

### 5.4 Need-Level Acceptance
* **Issue**: Need-level partial acceptance.
* **Evidence**: When multiple needs exist, genuine ones proceed and non-genuine ones are rejected independently.
* **Disposition**: **RETAIN AS EXISTING MODEL**
* **Rationale**: This is an operational workflow fully representable by treating Needs as independent Entities/Conditions with distinct states. No new ontology structure is required.

### 5.5 Recurring Needs
* **Issue**: Recurring vs one-off needs.
* **Evidence**: One-time medical bills vs recurring monthly rations requiring reverification.
* **Disposition**: **ACCEPT FOR REFINEMENT**
* **Rationale**: The evidence establishes recurrence/reverification behavior; it does not establish the ontology representation required to model it. The reconciliation phase must first test whether existing temporal/state semantics are sufficient.
* **Action**: Authorized for consideration during the subsequent Ontology ↔ Ground Truth Reconciliation phase.

### 5.6 Organisation / Programme
* **Issue**: Organisation vs Programme distinction.
* **Evidence**: Khidmat operates without nested programmes, interacting directly with donors and beneficiaries.
* **Disposition**: **CONTEXT-SPECIFIC**
* **Rationale**: Session 01:
Khidmat operates without nested programmes.

Broader domain:
Insufficient evidence from Session 01 alone to generalize this structure.

Governance:
Context-specific; broader practitioner validation required.
* **Action**: Retain as context-specific evidence. The prior governance decision (G1) splitting Organisation and Programme remains standing pending broader practitioner validation.

### 5.7 Micro-Donor Coordination
* **Issue**: Micro-donor coordination.
* **Evidence**: Direct donor adoption, first-come-first-serve matching, splitting donations via messaging groups.
* **Disposition**: **ACCEPT FOR REFINEMENT**
* **Rationale**: Session 01 establishes a recurring coordination pattern in the observed Khidmat context involving direct donor-beneficiary matching, donor adoption, and messaging-group coordination. The governance question is whether this pattern is sufficiently generalizable to warrant domain-level ontology consideration.
* **Action**: Authorized for consideration during the subsequent Ontology ↔ Ground Truth Reconciliation phase.

### 5.8 Delivery / Outcome
* **Issue**: Delivery vs outcome.
* **Evidence**: Case closure is tied to donor delivery and tracking-card signatures.
* **Disposition**: **DEFER — MORE PRACTITIONER EVIDENCE REQUIRED**
* **Rationale**: Delivery of support does not necessarily equate to achieving the desired humanitarian outcome. The evidence raises an important semantic distinction between delivery of support and resolution of the underlying vulnerability. Further practitioner evidence is required before determining whether additional ontology representation is justified.
* **Action**: Meeting 2+ must ask: "How is it recorded if support is delivered but the underlying vulnerability remains?"

### 5.9 Conflicting Sources
* **Issue**: Conflicting sources.
* **Evidence**: Unresolved handling of situations where volunteers disagree.
* **Disposition**: **DEFER — MORE PRACTITIONER EVIDENCE REQUIRED**
* **Rationale**: The current practitioner workflow is linear and avoids conflicting sources. No evidence exists to justify a specific conflict-resolution algorithm.
* **Action**: Meeting 2+ must ask: "What happens when two different volunteers or sources disagree on a family's needs?"

### 5.10 Dual-Clock Mismatch
* **Issue**: Dual-clock mismatch (Status vs Reality).
* **Evidence**: Unresolved case of tracking card saying "delivered" while beneficiary says "not delivered".
* **Disposition**: **DEFER — MORE PRACTITIONER EVIDENCE REQUIRED**
* **Rationale**: No evidence exists to determine the semantic treatment of administrative status mismatching with field reality.
* **Action**: Meeting 2+ must ask: "Have you ever had a case where the tracking card said 'delivered' but the beneficiary claimed they didn't receive it?"

## 6. Complete Refinement-Signal Governance Register

| Gov ID | Review ID | Issue | Evidence | Semantic Question | Disposition | Rationale | Further Evidence | Eligible for Ontology ↔ Ground-Truth Reconciliation? |
|---|---|---|---|---|---|---|---|---|
| SG-01 | GT-L1, GT-P1, GT-L7 | Verification Epistemics | Volunteer corrects/rejects initial survey based on ground check. | Does the current ontology adequately represent the distinction between initially reported information and information subsequently supported or corrected through ground-reality verification? | **ACCEPT FOR REFINEMENT** | Separation of reported claim from verified finding is crucial for data integrity. | None | YES — FOR RECONCILIATION |
| SG-02 | GT-OQ8, GT-OQ11 | Entity Need Attachment | General needs attach to family; specific needs attach to individual. | Does the existing ontology adequately represent the observed fact that some needs are associated with a family while other needs are associated with an individual member? | **ACCEPT FOR REFINEMENT** | Support for non-linear Relation and Entity mappings prevents rigid single-entity modeling. | None | YES — FOR RECONCILIATION |
| SG-03 | GT-OQ4, GT-PL1 | Recurring vs One-time | Monthly rations vs medical bill. | The evidence establishes recurrence/reverification behavior; it does not establish the ontology representation required to model it. The reconciliation phase must first test whether existing temporal/state semantics are sufficient. | **ACCEPT FOR REFINEMENT** | Dictates reverification cycles and closure rules. | None | YES — FOR RECONCILIATION |
| SG-04 | GT-OQ10 | Trusted Source Evidence | Govt hospital proof accepted as true without secondary check. | Does the existing ontology adequately represent the practitioner distinction between information requiring ground-reality verification and information accepted from a source treated as sufficiently authoritative in the observed context? | **ACCEPT FOR REFINEMENT** | May prevent redundant verification and introduces source-trust weighting. | None | YES — FOR RECONCILIATION |
| SG-05 | GT-L8, GT-OQ19 | Direct Coordination | Donor adoption, vendor fulfillment. | Is this micro-donor coordination pattern sufficiently generalizable to warrant domain-level ontology consideration? | **ACCEPT FOR REFINEMENT** | Provides context-specific evidence for decentralized micro-coordination that must be evaluated for domain generalization. | None | YES — FOR RECONCILIATION |

## 7. Unresolved / Deferred Evidence
* **Unknown / Unable-to-determine:** Practitioner rarely encounters this; operational handling remains untested.
* **Conflicting Sources:** No operational evidence for resolving volunteer disagreements.
* **Dual-Clock Mismatch:** No evidence for administrative record conflicting with field reality.
* **Delivery vs Outcome:** Evidence only covers delivery closure, not necessarily outcome resolution.

## 8. Meeting 2+ Evidence Requirements
1. "How is a claim recorded when a volunteer is absolutely unsure if it is true or false?"
2. "What happens when two different volunteers or sources disagree on a family's needs?"
3. "Have you ever had a case where the tracking card said 'delivered' but the beneficiary claimed they didn't receive it?"
4. "How is it recorded if support is delivered but the underlying vulnerability remains?"
5. "How do organizations that use nested programmes interact with grassroots layers like Khidmat?" (Broader domain validation)

## 9. Governance Summary

* **ACCEPT FOR REFINEMENT**: 7 (Verification/Reported Info, Epistemic Status, Recurring Needs, Micro-Donor Coordination, Entity Need Attachment, Trusted Source Evidence, Direct Coordination - grouped logically as 7 distinct accepted signals)
* **DEFER — MORE EVIDENCE**: 4 (Unknown Verification, Delivery/Outcome, Conflicting Sources, Dual-Clock Mismatch)
* **CONTEXT-SPECIFIC**: 1 (Organisation/Programme)
* **RETAIN AS EXISTING MODEL**: 1 (Need-Level Acceptance)
* **REJECT AS ONTOLOGY CHANGE**: 0
* **ESCALATE FOR GOVERNANCE**: 0

*(Note: The 7 Accepted items are authorized for the reconciliation phase; this does not alter the ontology directly.)*

## 10. Explicit Non-Decisions
Stage 7 explicitly did NOT:
* Stage 7 authorizes only consideration of the identified semantic questions during reconciliation; it does not authorize their implementation.
* Create new ontology concepts.
* Remove ontology concepts.
* Merge concepts or split concepts.
* Redesign ontology layers or pillars.
* Modify architecture rules.
* Collapse Organisation and Programme (treated strictly as context-specific observation).
* Establish `Claim` → `Fact` as a finalized ontology mechanism.
* Establish a formal epistemic mechanism.
* Equate delivery with outcome.
* Invent conflict-resolution algorithms.
* Resolve Unknown / Unable-to-determine handling.
* Modify the frozen reference-model baseline.

## 11. Stage 7 Closure
Session 01 governance analysis is complete. The authorized refinement signals may now proceed to the Ontology ↔ Ground Truth Reconciliation phase.

---

## 12. Appendix: Historical Governance Decisions

# STAGE 7 — GOVERNANCE DECISIONS

This register records formal governance rulings on structural conflicts and unresolved items identified during Stage 6 Evidence Integration, following the resolution conventions of the domain.

---

### G1 — Organisation vs Programme (Resolution of Q6 / C2)
| Field | Value |
| --- | --- |
| ID | G1 (Supersedes Q6) |
| Domain Question | Are Organisation and Programme distinct entities? |
| Source Evidence | `BL V1 §4`, `GT-OQ6`, `GT-PL5` |
| Established Domain Facts | Practitioner evidence overwhelmingly requires tracking distinct programmatic constraints. |
| Existing Authoritative Position | `BL V1 §4` explicitly collapses Organisation and Programme into a single Entity (P4). Reference Model resolved earlier tensions by adopting this collapse (`Q6`). |
| Exact Conflict | Tier 1 authority explicitly collapses them. Grounded field practice explicitly requires separating them to track distinct programmatic constraints. |
| Options Evaluated | **Opt 1**: Preserve Tier 1 (Collapsed).<br>**Opt 2**: Split into two distinct Entities. |
| Ontological Consequences | Opt 1 fails to model distinct programmatic bounds on constraints/eligibility. Opt 2 adds a new Entity (`Programme`), requires `Relation` between Org and Prog. |
| Architectural Consequences | Opt 1 conflates Org and Prog IDs. Opt 2 requires tracking two distinct IDs and APIs. |
| Breakage | Opt 1 breaks the ability to properly model "Funding Restrictions" (Q8) and "Context" (P2), which depend on Programme rules. Opt 2 formally amends Tier 1 authority. |
| Formal Ruling | **Opt 2 is SELECTED.** Organisation and Programme ARE distinct entities. |
| Tier 1 Authority Status | The prior rule collapsing them (`BL V1 §4`, `Q6`) has been amended directly at source in `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 (dated 2026-09-02), per this document's own XCR-2 requirement. This Stage 7 entry records the ruling; the source document itself now reflects it. Field evidence demonstrates that Context, Norms, and Need derivation cannot function structurally if the Organisation is the only boundary. |
| Downstream Ontology Changes | L2 (Entities) must explicitly list Programme as a distinct Entity. P4 (Entity) description updated. |
| Architecture Rule Changes | None fundamentally, but schema representations must split them. |
| Status | **RESOLVED** |

---

### G2 — CCR-7 Temporal Perspectives (Resolution of C8)
| Field | Value |
| --- | --- |
| ID | G2 |
| Original Domain Question | Whether human/life-trajectory temporality and organisational/programme engagement temporality require two formally independent temporal clocks. |
| Source Evidence | `GT-AR3`; subsequent Stage 7 ontological analysis comparing a unified temporal model, two independent clocks, and one temporal foundation with multiple temporal perspectives. |
| Established Domain Facts | The Reference Model and Ground Truth establish that a person's human/life/situation trajectory exists and persists independently of organisational engagement. Case closure does not imply need resolution. The evidence does not establish a universal requirement for two independent mechanical temporal systems. |
| Exact Conflict | Ground Truth supported separation between the person and administrative engagement but did not justify a universal mandatory dual-clock architecture, originally leaving this parameter UNRESOLVED. |
| Formal Ruling | They are semantically distinct temporal perspectives, but the ontology does not require two formally independent clocks.<br><br>A person's life/situation states and organisational/programme engagement states MUST NOT collapse into a single combined status or be treated as semantically equivalent. Therefore: Case Closed ≠ Need Resolved; Programme Ended ≠ Vulnerability Ended; No Active Case ≠ No Humanitarian Need; Support Delivered ≠ Outcome Achieved.<br><br>The distinction is represented through existing ontology semantics: temporally valid States and Occurrences interpreted relative to their relevant semantic Context (which can provide the frame/perspective relative to which a temporal state or occurrence is understood).<br><br>Both kinds of temporal facts share the same underlying temporal foundation.<br><br>The ontology does not prescribe a fixed number of temporal perspectives (e.g., Life/situation, Programme/engagement, Legal, Funder, or other legitimate future contexts) and does NOT introduce a Clock entity, Timeline primitive, or Process primitive, nor any new primitive, layer, or pillar. |
| Rationale | The existing ontology (`Condition` + `Context`) is sufficient to preserve the distinction without semantic loss. This resolves the semantic problem without requiring independent clocks. |
| Architectural Consequences | CCR-7 is no longer an unresolved foundational question. Architecture MUST preserve the semantic distinction and prevent conflation, while remaining free to determine the appropriate technical representation. |
| Future Evolution | Additional temporal perspectives may be supported if later domain evidence or scope requires them. Such evolution does not imply the existence of independent clocks or require reopening the foundational ontology unless genuine semantic loss is demonstrated. |
| Status | **RESOLVED — ONE TEMPORAL FOUNDATION WITH MULTIPLE TEMPORAL PERSPECTIVES** |

---

### G3 — Domain Primitive Definition (Resolution of R-1)
| Field | Value |
| --- | --- |
| ID | G3 |
| Domain Question | Is a Domain Primitive a category of concept (Identity, Relation, Condition) or a concrete irreducible of reality (Person, Household, Need)? |
| Source Evidence | - `01-DOMAIN-PRIMITIVES.md` §1 — circularity argument: Person cannot be both source and member of the Entities layer.<br>- `01-DOMAIN-PRIMITIVES.md` §5.2 — giving-side coverage test.<br>- `docs/06-review-package/02-ontology-design-review-phase-1.html` — R-1. |
| Established Domain Facts | The category reading is the only reading under which Stage 2's eight layers, including the Entities layer, can be derived without circularity. The concrete reading was tested and produces an unbounded/non-converging candidate list. |
| Options Evaluated | - **Opt 1** — Ratify category-of-concept reading as already implemented in Stages 1–2.<br>- **Opt 2** — Reject it and require concrete-irreducible re-derivation of the entire primitive/layer stack. |
| Formal Ruling | **Opt 1 is SELECTED.**<br><br>Domain Primitive = category of concept.<br><br>This is the governing definition project-wide. |
| Tier 1 Authority Status | No Tier 1 conflict. This is a methodological/design-primitive definition, not a business fact. |
| Downstream Ontology Changes | None. Stages 1–2 already reflect this interpretation. This ruling makes the interpretation formally authoritative. |
| Status | **RESOLVED** |

---

### G4 — Option A Closure Ratification (Need-Interactions, Service Providers, Outcome/Impact Ownership, Funder Altitude, Case Orchestration)
| Field | Value |
| --- | --- |
| ID | G4 |
| Domain Question | Are the single-source "Option A Closure" resolutions for these five items formally adopted? |
| Source Evidence | `GT-OQ16`, `GT-OQ15`, `GT-OQ5`, `GT-OQ17`, `GT-OQ19` |
| Established Domain Facts | Each item rests on exactly one practitioner record (Finding classification REFINED, not CONFIRMED) and has not been independently corroborated. |
| Formal Ruling | **Governance decision**: The project adopts "Option A" (the treatment described for each item in `06-STAGE-6-EVIDENCE-INTEGRATION-REPORT.md` §9 / the closure reports) for current modeling purposes.<br><br>**Ontological status**: UNRESOLVED. The underlying domain propositions are NOT ontologically closed. For example, regarding Need-Interactions, the current evidence is insufficient to justify introducing a formal ontology-level relation type, but this does not mean such a relation does not exist in humanitarian reality.<br><br>**Evidence status**: Weak/Single-source. Each item rests on exactly one practitioner record and lacks independent corroboration.<br><br>Reopening requires new practitioner evidence or an explicit superseding governance ruling. |
| Status | **GOVERNED PROVISIONAL — single-source evidence acknowledged** |

---

### G5 — Risk and Need Primitive Classification
| Field | Value |
| --- | --- |
| ID | G5 |
| Domain Question | Are Risk and Need classified as Condition (P1) or some other primitive? |
| Source Evidence | `01-DOMAIN-PRIMITIVES.md` §6.1 (Risk), §6.2 (Need); `04-ARCHITECTURE-RULES.md` §1 (Need synchronization correction). |
| Established Domain Facts | Risk is a dispositional-future-oriented Condition; Need is a Condition with a lifecycle, not a Relation, because its Norm-based comparator forecloses the Relation reading. |
| Formal Ruling | Risk = Condition (P1); confidence about Risk = Epistemic Stance (P3). Need = Condition (P1); the wellbeing standard it is measured against = Norm (P5). |
| Status | **RESOLVED** |
