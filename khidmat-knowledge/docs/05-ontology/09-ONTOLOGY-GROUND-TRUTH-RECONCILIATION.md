# ONTOLOGY ↔ GROUND-TRUTH RECONCILIATION

## PHASE 2 — SEMANTIC MAP OF CURRENT ONTOLOGY

### 1. DOMAIN PRIMITIVES
* **Condition (P1):** That which is true across a span and can change.
* **Context (P2):** The frame relative to which a statement holds.
* **Epistemic Stance (P3):** The warrant the system holds for what it asserts.
* **Entity (P4):** That which exists and persists as a distinct whole.
* **Norm (P5):** That which bounds what is permitted/required.
* **Occurrence (P6):** That which happens.
* **Relation (P7):** Connection between independent domain concepts.

### 2. ONTOLOGY LAYERS
* **Facets:** Independently variable axes.
* **Entities:** Distinct things.
* **Relationships:** Social/domain connections.
* **Constraints:** Rules/Norms.
* **States:** Longitudinal tracking of Conditions.
* **Events:** Dateable sequence of Occurrences.
* **Cognition:** Open-world commitment and Epistemic Stances.
* **Coordination Patterns:** Distinct workflow models (e.g. handoffs).

### 3. ONTOLOGY PILLARS
* I. Human & Social Subject
* II. Context & Environment
* III. Vulnerability & Need
* IV. Epistemics & Knowledge
* V. Actors & Ecosystem
* VI. Action & Coordination
* VII. Resources & Support

### 4. ARCHITECTURE RULES
* CCR-1: Altitude qualification
* CCR-2: Algorithmic humility
* CCR-5: Human-oversight trigger
* CCR-6: Non-linearity
* CCR-7: Dual-clock rule
* CCR-8: Dignity-as-constraint

---

## PHASE 3 & 4 — TEST GOVERNED REFINEMENT SIGNALS

### R1 — Reported requirement vs ground-reality review
* **GROUND-TRUTH ISSUE:** Initial survey yields claimed needs; ground check corrects, verifies, or rejects them.
* **SOURCE EVIDENCE:** "Volunteer goes to the ground and checks the requirement... reject false, correct, or proceed." (Khidmat Session 01)
* **SEMANTIC INTERPRETATION:** The system must distinguish between what is reported by a beneficiary and what is verified by the organization.
* **CURRENT ONTOLOGY COVERAGE:** The `Cognition` layer and `Epistemic Stance` primitive exist specifically to capture the "warrant" the system holds for an assertion. `Events` capture the verification Occurrence.
* **COVERAGE TEST:** Can we represent a reported claim vs verified reality? Yes. An initial need is created as a `State` with an `Epistemic Stance` of "Claimed". The ground check is an `Event` that updates the `Epistemic Stance` to "Verified" or "Rejected" and potentially alters the `State`.
* **SEMANTIC GAP?:** No semantic gap. The existing Epistemic Stance mechanism handles this distinction natively.
* **DECISION:** FULLY REPRESENTED — NO CHANGE.

### R2 — Epistemic status / verification
* **GROUND-TRUTH ISSUE:** Recording the state of "checked and false" vs "not checked yet" vs "uncertain".
* **SOURCE EVIDENCE:** Khidmat explicitly verifies genuine needs and rejects false ones, but notes "unknown... is not much required" in their specific workflow.
* **SEMANTIC INTERPRETATION:** While the local workflow doesn't heavily use an explicit "unknown" state, the ontology must support standard epistemic separation of absence-of-evidence vs evidence-of-absence to be domain-complete.
* **CURRENT ONTOLOGY COVERAGE:** `Epistemic Stance` (P3) is defined as "the warrant the system holds... including what it does not know."
* **COVERAGE TEST:** Can it express information assessed, rejected, or uncertain? Yes, via explicit `Epistemic Stance` attribution on `States`.
* **SEMANTIC GAP?:** No semantic gap.
* **DECISION:** FULLY REPRESENTED — NO CHANGE.

### R3 — Recurring vs one-off needs
* **GROUND-TRUTH ISSUE:** Differentiating short-term (e.g., medical bill) vs long-term (e.g., monthly rations) support, which affects closure and reassessment.
* **SOURCE EVIDENCE:** "medical needs are of one time and long also soo they can be if one time then help via the donors and then closed if recusisng like medicens they can conitnue" (Khidmat Session 01)
* **SEMANTIC INTERPRETATION:** A Need `State` has a temporal dimension (recurrence pattern) that governs its lifecycle and continuation.
* **CURRENT ONTOLOGY COVERAGE:** `Condition` (P1) and `States` (L5) govern things true across a span. 
* **COVERAGE TEST:** Can a State represent recurrence? A State's dimensions (Facets) can model temporal recurrence without inventing a new Entity.
* **SEMANTIC GAP?:** Minor descriptive gap in explicit temporal facets for Needs, but structurally fully supported.
* **DECISION:** PARTIALLY REPRESENTED — CLARIFICATION ONLY (Needs carry temporal facets).

### R4 — Organisation vs Programme
* **GROUND-TRUTH ISSUE:** Do Programmes universally exist beneath Organisations?
* **SOURCE EVIDENCE:** "NO organisations and programs are involved in this just the khidmat grp doing the root work" (Khidmat Session 01)
* **SEMANTIC INTERPRETATION:** Grassroots organizations may operate at a flat altitude without nested programmes. The ontology Tier 1 authority collapses them, but previous (now unverified) evidence challenged this.
* **CURRENT ONTOLOGY COVERAGE:** Structurally distinct entities per G1.
* **COVERAGE TEST:** The Khidmat evidence shows a case where there is no nested programme.
* **SEMANTIC GAP?:** No semantic gap. The concepts are structurally distinct (G1), and Khidmat simply instantiates only the Organisation.
* **DECISION:** RESOLVED — SCOPE NOTE APPLIED (G1).

### R5 — Micro-donor coordination
* **GROUND-TRUTH ISSUE:** Direct peer-to-peer or micro-donor matching.
* **SOURCE EVIDENCE:** "donors adopt the beneifcary... donors can combine or split." (Khidmat Session 01)
* **SEMANTIC INTERPRETATION:** Coordination involves direct matchmaking where funding allocation connects micro-donors directly to cases, not just top-down institutional funding.
* **CURRENT ONTOLOGY COVERAGE:** `Coordination Patterns` (L8) and `Actors` (Pillar V) support diverse giving entities.
* **COVERAGE TEST:** Can we represent a Donor Entity connected via a Coordination Pattern to a Case/Need State? Yes.
* **SEMANTIC GAP?:** No new entity required, just an instantiation of the existing Coordination pattern.
* **DECISION:** FULLY REPRESENTED — NO CHANGE.

### R6 — Person vs Family need
* **GROUND-TRUTH ISSUE:** Needs attaching to individuals vs heads of households.
* **SOURCE EVIDENCE:** "head of the family (zimmedar) is noted in the beneficary for the family and for the spefic needs the members which are beneficary their ids are also taken" (Khidmat Session 01)
* **SEMANTIC INTERPRETATION:** Need states must attach flexibly to either the Family/Household Entity or the individual Person Entity.
* **CURRENT ONTOLOGY COVERAGE:** `Entity` (P4) models Person and Household as distinct. `Relationships` (L3) connect them. `States` (L5) can apply to any Entity.
* **COVERAGE TEST:** The ontology allows a `State` (Need) to characterize a Person, or a `State` to characterize a Household natively.
* **SEMANTIC GAP?:** No structural gap. 
* **DECISION:** FULLY REPRESENTED — NO CHANGE.

### R7 — Evidence/source trust
* **GROUND-TRUTH ISSUE:** Institutional vs. reported evidence carrying different weight (e.g., Govt hospital proofs).
* **SOURCE EVIDENCE:** "The medicals proofs of government hospital are considered true only so no double verification"
* **SEMANTIC INTERPRETATION:** Some evidentiary sources carry automatic epistemic trust, bypassing standard verification loops.
* **CURRENT ONTOLOGY COVERAGE:** `Epistemic Stance` (P3) captures the "warrant" for an assertion. 
* **COVERAGE TEST:** Can the system record that a State's Epistemic Stance is anchored by a highly trusted source (Govt document), thus establishing it as "Verified"? Yes. No "TrustScore" primitive is needed; the source `Relation` and `Epistemic Stance` handle this.
* **SEMANTIC GAP?:** No semantic gap.
* **DECISION:** FULLY REPRESENTED — NO CHANGE.

---

## PHASE 5 — SEMANTIC GAP TEST

**Question 1:** Can the current ontology express the practitioner reality?
Yes. The existing structural ontology provides the exact semantic primitives (Epistemic Stance, Condition, Entity, Occurrence) needed to express Khidmat's ground reality.

**Question 2-7:** (N/A — No genuine semantic gap exists). The gaps identified in the Stage 6 Evidence report were explicitly classified as *Refinement Signals* and *Governance Candidates*, not broken primitives. The reconciliation confirms that the current primitives natively absorb these signals. 

## PHASE 6 — MINIMUM-CHANGE RULE

Applying the Minimum-Change Rule:
* **No change** is required to the structural ontology (Primitives, Layers, Pillars, Architecture Rules).
* The definitions of Epistemic Stance and States are confirmed by this evidence.
* We deliberately do NOT invent new entities (e.g., `Claim`, `TrustLevel`, `Verification`) because the existing primitive architecture natively supports the semantic distinctions required by the practitioner.
