# 4 — Architecture Rules

**Ontology Design, step 4 of 7.** Status: **COMPLETE / BASELINED.**

Derived from `01-DOMAIN-PRIMITIVES.md`, `02-ONTOLOGY-LAYERS.md`, `03-ONTOLOGY-PILLARS.md`,
`README.md` (Standing Rules), and
`docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` (RM).

Intended location in the repository: `docs/05-ontology/04-ARCHITECTURE-RULES.md`.

---

## 0. How to read this

Same discipline as Stage 2 and Stage 3, applied to rules rather than domain content:

| | What it is | Where it lives |
|---|---|---|
| **Established rules** | A rule with a named source in a frozen document or an explicit ruling below | §4, main body |
| **Rulings** | A tension closed by this document, stated once, propagating everywhere | §1 |
| **Open tensions** | Acknowledged unknowns the architecture must accommodate without resolving | §7, and the UHR rules in §4.8 |

**No rule below is invented.** Each traces to a Standing Rule (README), a Reference Model
section, or an explicit decision already taken in Stages 1–3. Where a rule encodes a domain
finding rather than a purely methodological constraint, both the design source and the
underlying TD evidence tier are cited (§4.5, ECR-5).

**This document does not re-open Stages 1–3.** It assumes their completion (per the prior
completion audit) and states the rules under which their content may be composed, extended,
and corrected going forward.

---

## 1. Synchronization Correction — Need Classification (Stage 1-origin decision, propagated to Stage 3)

**Finding.** Three answers exist for the same question across the frozen documents:

| Document | Says |
|---|---|
| `01-DOMAIN-PRIMITIVES.md` §6.2 | Need is a **Condition** |
| `02-ONTOLOGY-LAYERS.md` §2.1, §6.1 | Follows Condition (Facets + States tables) |
| `03-ONTOLOGY-PILLARS.md` §8, item 2 | Need is a **Relation** |
| `03-ONTOLOGY-PILLARS.md` §3 (Pillar III body) | Calls the placement "structurally open" — contradicting §8's own header, "Resolved decisions and final ontological closures" |

Stage 3 disagrees with Stage 1/2 in one place and with itself in another.

**Confirmed classification (originating in `01-DOMAIN-PRIMITIVES.md` §6.2 — not newly decided
here): Need is classified as a Condition (P1).** Stage 4's role in this section is limited to
identifying that `03-ONTOLOGY-PILLARS.md` had drifted from Stage 1's already-established
classification, and correcting Stage 3 to match Stage 1 — not to originate the classification.
This is now the single stated answer for architecture purposes, per Stage 1's authority.

**Reasoning, restated and strengthened.** Need's *definition* — a gap between current state and
a basic standard of wellbeing (RM §7.1) — is relational language, which is what motivated the
Relation reading. But two structural facts foreclose it:

1. **Need behaves like a Condition, not a Relation.** It opens, changes severity, and resolves
   or expires (RM §7.4) — a lifecycle over a span, which is exactly P1's definition ("true of
   something across a span of time, and which can change while what it is true of persists").
   A Relation has no such lifecycle of its own; it holds or it doesn't.
2. **Need's own primitive boundary rule forecloses Relation.** P7 (Relation) requires "a
   connection between independent domain concepts" (`01-DOMAIN-PRIMITIVES.md` §4, P7). The counterpart
   Need is measured against — "a basic standard of wellbeing" — is a **Norm** (RM §3.6;
   `03-ONTOLOGY-PILLARS.md` §8 item 10 itself classifies the wellbeing standard as a
   Context-scoped Norm), not a persisting Entity. A Norm is not the kind of thing Relation
   connects to. Need therefore cannot satisfy Relation's own admission test.

Need's *definition* describes what a Need **means**; its ontological classification describes
what **kind of tracked object** it is. Stage 1 already drew this exact distinction for Risk
(RM §8.1's "first-class" language vs. the confidence held *about* it) — the same distinction now
closes Need consistently.

**Propagation status: CONFIRMED APPLIED (verified against current repository text at time of
this remediation).**

*Historical finding (recorded for traceability):* `03-ONTOLOGY-PILLARS.md` originally contained
two locations that had drifted from Stage 1's Need classification — §8 item 2 originally read
*"Need is fundamentally a Relation..."* and §3 Pillar III's "Unresolved tensions" line originally
called both Risk and Need "structurally open."

*Corrective action:* Both locations were corrected to state Need as a Condition, consistent with
`01-DOMAIN-PRIMITIVES.md` §6.2, with the reasoning that the wellbeing standard Need is measured
against is a Norm rather than a persisting Entity, which forecloses the Relation reading.

*Current status:* `03-ONTOLOGY-PILLARS.md` §8 item 2 now reads *"Need Placement: Need is
fundamentally a Condition (RESOLVED — see `01-DOMAIN-PRIMITIVES.md` §6.2 and
`04-ARCHITECTURE-RULES.md` §1)..."* and §3 Pillar III now reads *"Both Risk and Need placements
are resolved (see §8, items 1–2, and `04-ARCHITECTURE-RULES.md` §1). No structural tension
remains for this pillar's definition..."* — both confirmed present verbatim as of this
remediation. No further action is required on this item.


This ruling is binding per **CTR-2 / CTR-3** (§4.7): it applies wherever Need appears, and may be
reopened only by new evidence or an explicit governance ruling, never by a later document
silently reverting to the Relation reading.

## 1A. Synchronization Correction — Organisation/Programme Split (Stage 7 G1-origin decision)

**Finding.** Business Logic V1 §4 originally collapsed implementing organisations and the programmes they lead into a single actor row ("Programme / Organisation").

**Confirmed classification (originating in Stage 7 `07-STAGE-7-GOVERNANCE-DECISIONS.md` G1):** `Organisation` and `Programme` are split into two distinct Entities connected by a new `operates` Relation.

**Reasoning.** Stage 6 identified this as a tension between Tier-1 sources and external practitioner evidence (GT-PL5, GT-OQ6). Stage 7 G1 formally amended the Blueprint, splitting the entities so that programme-specific eligibility, funding, and activity rules attach to the Programme rather than the Organisation.

**Propagation status: APPLIED.** `02-ONTOLOGY-LAYERS.md` and `03-ONTOLOGY-PILLARS.md` have been updated to reflect the two distinct Entities and the new relationship, overwriting the earlier unified Entity.

---

## 2. Purpose and scope

Architecture Rules are the **grammar of the ontology** — the rules that must hold for any
concept to be validly represented in it, and the rules governing how the ontology itself may
grow or be corrected. They are not:

- implementation, schema, or database design;
- API design;
- a taxonomy or value-set specification;
- a workflow or process specification.

They govern the space between "the ontology map exists" (Stages 1–3) and "the ontology is
engineered into something buildable" (Stages 5–7 and beyond).

---

## 3. Derivation method

Each rule below is sourced to one of:

1. A **Standing Rule** in `README.md` (five rules, each tied to a named prior-foundation
   failure);
2. An explicit **structural boundary** stated in Stage 1, 2, or 3 (a primitive boundary, a
   layer admission test, a pillar's "what remains outside");
3. A **Reference Model** section, where the rule operationalizes a domain finding rather than a
   pure design constraint.

No rule is admitted on the strength of this document alone (per ECR-3, §4.5).

---

## 4. Architecture Rules

### 4.1 Primitive Integrity Rules (PIR)

**PIR-1 — Closed-set discipline.** The seven primitives (Condition, Context, Epistemic Stance,
Entity, Norm, Occurrence, Relation) are treated as complete for architecture purposes. No rule,
layer, or pillar may introduce an eighth without going through PIR-5.
*Source:* `01-DOMAIN-PRIMITIVES.md` §1 ("the set is closed once ratified"), §7.

**PIR-2 — One primary classification per concept.** Every domain concept is assigned exactly one
primitive as its primary classification. A concept appearing to need two is escalated as a
tension (§4.7), never silently dual-classified.
*Source:* `01-DOMAIN-PRIMITIVES.md` §1, "Rules governing the set."

**PIR-3 — Primitive-to-layer fan-out is not concept-to-primitive fan-out.** A single primitive
*may* feed more than one layer (Condition → Facets + States; Context → Facets + scoping of
Constraints). This is fan-out at the primitive→layer edge and does not violate PIR-2, which
governs the concept→primitive edge only.
*Source:* `02-ONTOLOGY-LAYERS.md` §1, Assumptions A-01/A-02. This rule formally closes open
review item **R-5** from `02-ontology-design-review-phase-1.html` §5 by stating explicitly what
PIR-2 does and does not restrict.

**PIR-4 — Escalation over accommodation.** A concept failing any of tests T1–T5 is escalated for
a ruling; it is never accommodated by stretching a primitive's boundary.
*Source:* `01-DOMAIN-PRIMITIVES.md` §1.

**PIR-5 — Admission gate for extension.** A candidate eighth primitive must pass all five
qualification tests (T1 abstract, T2 universal, T3 necessary, T4 evidence-grounded, T5
organisation/technology-independent) and must be run against the giving-side-style coverage
test method before admission.
*Source:* `01-DOMAIN-PRIMITIVES.md` §1, §5.2.

### 4.2 Layer Composition Rules (LCR)

**LCR-1 — Named source primitive required.** No layer content is valid without tracing to a
named primitive.
*Source:* `02-ONTOLOGY-LAYERS.md` §1.

**LCR-2 — Facet/State split.** An axis along which something varies is a Facet; the value held
on that axis at a point in time is a State. The two are never merged into one entry.
*Source:* `02-ONTOLOGY-LAYERS.md` §2 vs §6; RM §16.5.

**LCR-3 — Context framing rule.** Context primarily frames and scopes concepts and rules, and should not be modeled as an ordinary P7 Relation merely to express that scoping. A frame that is itself tracked, funded, and reported on has become an Entity.
*Source:* `01-DOMAIN-PRIMITIVES.md` P2 boundary.

**LCR-4 — Norm/Context pairing rule.** A rule binding in one scope and not another is one
Constraint (Norm) plus one Context — never two Constraints.
*Source:* `01-DOMAIN-PRIMITIVES.md` P5 boundary; `02-ONTOLOGY-LAYERS.md` §5.

**LCR-5 — Event completion rule.** An Event is complete once it has finished happening. Anything still true afterward is the State it established, changed, or ended, not a property of the Event.
*Source:* `01-DOMAIN-PRIMITIVES.md` P6 boundary; `02-ONTOLOGY-LAYERS.md` §7.

**LCR-6 — Cognition non-assertion rule.** Cognition never asserts a fact about the world. "This
household is destitute" is a State; "we have not verified this" is Cognition. No Cognition entry
may be phrased as a first-order claim about reality.
*Source:* `02-ONTOLOGY-LAYERS.md` §8.4.

**LCR-7 — Coordination Pattern shape-only rule.** A pattern names which party types,
relationships, states, and events recur together, and which constraints and confidence
thresholds apply. It never specifies execution order, task routing, automation instruction, or hidden inference / causal derivation.
*Source:* `02-ONTOLOGY-LAYERS.md` §9; RM §12 (action quarantine); README Standing Rule 4.

**LCR-8 — Open-world default.** Where a State's value is unknown, the correct representation is
an explicit "unknown" Cognition entry referencing that State — never a default value or an
omitted field treated as negative.
*Source:* `02-ONTOLOGY-LAYERS.md` §8.2; RM §10.5.

**LCR-9 — Inherence of Condition.** When a Condition characterizes a bearer, that characterization is structural inherence, not a Relation (P7). A Relation connects two independent concepts, whereas a Condition cannot exist independently of what it characterizes.
- *Entity Dependency:* Represented via a P7 Relation (e.g., Person A depends on Person B).
- *Condition Cascade:* The domain's dependency-based cascade (e.g., "a mother's risk is her infant's risk") is represented by each entity structurally bearing its own inherent Condition, with a P7 Relation between the entities. The ontology provides the structural capacity to record both risks, but the automated inference of one from the other belongs to downstream reasoning/business logic, not embedded in the ontology or Coordination Patterns.
- *Condition Influence:* Causal or influence assertions (e.g., Condition A caused Condition B) are represented as Claims (Layer 7 Cognition) evaluated by an Epistemic Stance, or deferred to downstream reasoning. They are not modeled as first-order P7 Relations, nor embedded in Coordination Patterns (which only describe recurring non-inferential shapes).
*Source:* `01-DOMAIN-PRIMITIVES.md` P1 boundary, P7 boundary; RM §4.1.

### 4.3 Pillar Boundary Rules (PBR)

**PBR-1 — Pillars are vertical slices, not a ninth category.** A pillar may never be cited as
the source of a primitive or a layer. Citation runs primitives → layers → pillars only.
*Source:* `03-ONTOLOGY-PILLARS.md` §2.

**PBR-2 — Explicit negative boundary required.** A pillar definition is incomplete without a
stated "what remains outside it."
*Source:* `03-ONTOLOGY-PILLARS.md` §3 (every pillar's boundary field).

**PBR-3 — Universal core / Level-2 localization split.** Every pillar's foundational concepts
are jurisdiction-independent. Jurisdiction-specific content specializes a pillar at Level 2 and
never redefines it.
*Source:* `03-ONTOLOGY-PILLARS.md` §7.

**PBR-4 — Cross-pillar connections are explicit, not duplicated.** Where a concept touches two
pillars (e.g., Outcome in Pillar I and Pillar III), the connection is a named Relation or
Coordination Pattern — not a re-stated definition in both places.
*Source:* `03-ONTOLOGY-PILLARS.md` §3 (Outcome/Impact ownership note), §8 item 3.

**PBR-5 — Coverage re-test on pillar change.** Any pillar addition or restructuring requires
re-running both the full-domain coverage test and the Cognition coverage test before acceptance.
*Source:* `03-ONTOLOGY-PILLARS.md` §5–§6.

### 4.4 Cross-Cutting Structural Rules (CCR)

**CCR-1 — Altitude qualification rule.** Any term existing at both programme and case altitude
(needs assessment, planning, monitoring, coordination) must carry an explicit altitude tag
wherever it appears. An unqualified use is a defect.
*Source:* RM §11.4. *Underlying evidence:* **Strong** — five independent dossiers
(BD-TD01-002, BD-TD03-001, BD-TD04-003, BD-TD05-002, BD-TD06-002).

**CCR-2 — Action quarantine rule.** Registration, verification, assessment, planning, referral,
delivery, monitoring, follow-up, and re-verification may never become the ontology's organizing
axis. They are represented because understanding is acquired through them, not as a model of an
organization's workflow.
*Source:* README Standing Rule 4; RM §12; `02-ONTOLOGY-LAYERS.md` §9.

**CCR-3 — Reality/scope separation rule.** Reality-membership does not imply scope-membership,
and scope-exclusion does not imply unreality. No rule may infer one from the other.
*Source:* README Standing Rule 5; RM §16.2, §0.2.

**CCR-4 — Open-world commitment rule.** Absence of a recorded statement is never the negation of
that statement. Any pattern that could encounter missing information must have an explicit "not
known" path through Cognition.
*Source:* RM §10.5, §16.5; `02-ONTOLOGY-LAYERS.md` §8.2.

**CCR-5 — Human-oversight trigger rule.** Any Constraint whose decision could materially affect
a person's rights, safety, dignity, legal status, eligibility, access to services, or long-term
wellbeing must route to a human-review Coordination Pattern; no pattern may resolve such a
decision automatically.
*Source:* RM §10.6, §12.2; BL §3.3.

**CCR-6 — Non-linearity rule.** Every multi-stage Coordination Pattern must support re-entry to
an earlier stage as a first-class, non-exceptional transition.
*Source:* RM §12.4, §14.1. *Underlying evidence:* **High** — BD-TD03-002, ≥4 independent source
families (interagency GBV and Child Protection case-management standards).

**CCR-7 — Temporal Perspectives rule.** The ontology assumes one underlying temporal foundation. A person's or household's human/life/situation trajectory and their organisational/programme/administrative engagement are semantically distinct and may never collapse into one combined status field or equivalent semantic representation (i.e., Case Closed does not imply Need Resolved; Programme Ended does not imply Vulnerability Ended; No Active Case does not imply No Humanitarian Need; Support Delivered does not imply Outcome Achieved). Temporal facts may be interpreted within different semantic perspectives (e.g., human/life/situation, programme/engagement, legal, funder, or other legitimate domain contexts, without freezing this into exactly two perspectives). `Context` distinguishes the semantic perspective/frame in which a temporal `State` or `Occurrence` is interpreted. This relies strictly on existing ontology semantics (`Condition`, `Context`, `Entity`, `Occurrence`, `Relation`, State semantics). It does NOT mandate two independent mechanical clocks, nor introduce a Clock, Timeline, Temporal, or Process primitive, nor a new layer, pillar, or ontology category. Architecture must preserve this semantic separation but remains technology-neutral (it does not prescribe database tables, columns, schemas, event sourcing, workflow engines, APIs, classes, queues, storage models, or implementation-specific timeline mechanisms). Status: RESOLVED per Stage 7 G2 (Historically, Ground Truth did not establish a universal requirement for two independent clocks, originally leaving G2 unresolved; later ontological analysis proved the semantic problem is resolved without independent clocks).
*Source:* RM §14.2. *Underlying evidence:* **Medium-High** — BD-TD03-004, ≥4 source families (Graduation Approach / BRAC / USAID practice), and subsequent CCR-7 ontological resolution.

**CCR-8 — Dignity-as-constraint rule.** Dignity is represented only as a standing Constraint
governing how other layers' content may be used or disclosed — never as a State, score, or
measurable Condition.
*Source:* RM §3.7; `01-DOMAIN-PRIMITIVES.md` §5.3 (Dignity rejected as a primitive, fails T1).

### 4.5 Evidence & Citation Rules (ECR)

**ECR-0 — Evidence Rating Scale.** The following scale is authoritative for all evidence strength references in the ontology foundation. (Level-1 sources are TD Evidence Dossier Tier B/D findings; Tier C findings are excluded).
| Grade | Meaning |
|---|---|
| **Strong** | ≥2 independent Level-1 source families, Tier B institutional or high-confidence Tier D |
| **Moderate** | 1–2 Level-1 findings, corroborated but thin or at medium confidence |
| **Limited** | A single Level-1 finding, tangential or partial |
| **Blueprint-only** | No Level-1 support. Conceptually defined at Levels 3–4 only |
| **Evidence not found** | The specific claim was searched for across all dossiers and is absent |

**ECR-1 — RM citation required.** Every ontology element must cite the Reference Model section
it derives from. An element with no RM citation is a proposal, not part of the ontology.
*Source:* README Standing Rules 1–2.

**ECR-2 — Evidence strength inherits downward, never upgrades.** A layer entry cannot exceed the
strength recorded for its primitive; a pillar cannot exceed its
constituent layers'. Restating a Blueprint-only claim elsewhere does not make it Tier B/D
evidence.
*Source:* Pre-Stage-5 Phase 1 ratings; `02-ONTOLOGY-LAYERS.md` §0, §10.

**ECR-3 — No self-citation.** A document may not cite itself, or a document derived from it, as
independent support for a claim.
*Source:* README Standing Rule 2.

**ECR-4 — Assumptions stay out of body text.** A judgment made to keep derivation moving is
recorded only in a dedicated Assumptions section, never asserted inline in a rule, layer, or
pillar body.
*Source:* `02-ONTOLOGY-LAYERS.md` §0, §11.

**ECR-5 — Architecture rules are methodological, not domain-empirical.** A rule here is sourced
to a Standing Rule, an RM section, or a prior design decision — not to a TD dossier finding —
unless it directly operationalizes a domain finding (e.g., CCR-1, CCR-6, CCR-7), in which case
both the design source and the underlying TD evidence tier are cited. This mirrors the Tier-C
exclusion already applied in the evidence rating scale (ECR-0), extended by analogy to
rule-provenance.

**Citation defects — CONFIRMED CORRECTED (historical record retained per XCR-3):**
- *Historical finding:* `02-ONTOLOGY-LAYERS.md` §11 (assumption A-03) previously labeled
  Evidence as "(P4)"; P4 is Entity (`01-DOMAIN-PRIMITIVES.md` §4), and Evidence was examined and
  rejected as a primitive (`01-DOMAIN-PRIMITIVES.md` §5.3), so the label was incorrect.
- *Historical finding:* `02-ONTOLOGY-LAYERS.md` §12 ("Evidence Taxonomy" item) previously
  referred to "the Evidence primitive," which does not exist as a primitive for the same reason.
- *Corrective action:* Both locations were rewritten to read "the Evidence *entity/occurrence*
  content, per §5.3's rejection of Evidence as a primitive."
- *Current status:* Confirmed present verbatim in `02-ONTOLOGY-LAYERS.md` §11 and §12 as of this
  remediation. No further action required on this item.

### 4.6 Extension & Change-Control Rules (XCR)

**XCR-1 — No phase anticipation.** Content belonging to Stage 5, 6, or 7 may not be authored
inside any Stage 1–4 document.
*Source:* README Standing Rule 3.

**XCR-2 — Amend-at-source rule.** To change a business fact this architecture depends on, the
correction is made in Business Logic V1 or the Reference Model, and every downstream document is
re-derived. No architecture rule may itself declare a new business fact.
*Source:* README "Authority" section; Standing Rule 1.

**XCR-3 — Single-ruling propagation rule.** When a tension is closed, the ruling is recorded
once, in the stage where the tension first arose, and every document that stated the tension is
corrected to match.
*Source:* This document, §1 — the Need closure is the first enactment of this rule, directly
answering the defect the completion audit found (Need answered three different ways across three
documents).

**XCR-4 — Re-test on structural change.** Adding, merging, or removing a primitive, layer, or
pillar requires re-running the primitive coverage test, the layer derivation map, and the pillar
coverage tests, in that order, before acceptance.
*Source:* `01-DOMAIN-PRIMITIVES.md` §5.2; `03-ONTOLOGY-PILLARS.md` §5–§6.

### 4.7 Contradiction & Tension Resolution Rules (CTR)

**CTR-1 — Scoped blocking.** An open tension blocks only the specific downstream work
depending on it — not unrelated stages or concepts. (Risk's unresolved placement blocked only
Risk-dependent pillar work per R-3 in the Phase 1 review; it never blocked, e.g., the Human &
Social Subject pillar.)
*Source:* `02-ontology-design-review-phase-1.html` §5, R-3; `03-ONTOLOGY-PILLARS.md` §8, items 1–2.

**CTR-2 — Single-answer requirement.** A ruling closes a tension with exactly one stated answer,
applied identically everywhere the concept appears. A tension is not resolved while any document
still records the pre-ruling alternative as live.
*Source:* This document, §1 (generalizing the Need correction).

**CTR-3 — Rulings are reversible only by re-derivation.** A closed tension may be reopened only
by new evidence or an explicit governance ruling overriding the prior one — never by a later
document silently reintroducing the old alternative.
*Source:* README, "Two things blocked outside this repository," item 1 (the primitive
definition itself is "open to reversal," but only via an explicit Lead ruling, never silent
drift) — generalized here to all rulings.

### 4.8 Unknown-Handling Rules (UHR)

These rules let acknowledged open items proceed into architecture without being resolved or
allowed to block Stage 4 — the same anti-loop discipline applied to the Stage 1–3 audit.

**UHR-1 — Stub extension points.** Where content is real but undescribed (giving-side entities
and patterns, evidence-kind taxonomy, human-facet value sets), the architecture reserves a
named, empty extension point in the relevant layer/pillar. The stub carries no invented content.
*Source:* `01-DOMAIN-PRIMITIVES.md` §5.2 (giving side introduces no new primitive);
`02-ONTOLOGY-LAYERS.md` §3.3, §8.5, §9.4.

**UHR-2 — Composition-function parameterization.** Where a composition rule is domain-real but unevidenced (vulnerability composition, compound risk composition), the architecture represents it as a named, versioned function attached to the relevant State, parameterized for Stage 5. It is NOT hard-coded as additive, multiplicative, or threshold-based because the sources do not provide a math formula.
*Source:* RM §8.4; `02-ONTOLOGY-LAYERS.md` §6.3.

**UHR-3 — Disputed ownership tagging.** (Historical). This rule previously tagged Coordination Patterns whose ownership was genuinely undecided (e.g., outcome/impact measurement) as `ownership: pending`. This tension has been structurally resolved (delegated to architecture); the tag is no longer active.
*Source:* RM §12.5; `02-ONTOLOGY-LAYERS.md` §7.3, §9.3.

**UHR-4 — Identity-resolution uncertainty routing.** Because the mechanism for establishing
person-sameness is unevidenced, any pattern depending on person-identity (deduplication,
longitudinal reasoning) must route low-confidence matches through Cognition's human-review
trigger (CCR-5) rather than resolving them silently.
*Source:* RM §3.1, §16.5; TD-01 Open Gap 1.

**UHR-5 — Unadmitted constraint content stays unadmitted.** Where the Reference Model itself records a candidate constraint with unknown empirical content (e.g., specific funding restriction types — RM §11.4), the architecture treats the structural classification as resolved (Norm/Constraint) but leaves the specific values unadmitted. A stub extension point (UHR-1) is reserved for the content, bounded as a Source-Absent Parameter.
*Source:* RM §11.4; `02-ONTOLOGY-LAYERS.md` §5.1.

---

## 5. Rule-to-stage traceability

| Rule group | Protects | Primary stage dependency |
|---|---|---|
| PIR (4.1) | Primitive set integrity | Stage 1 |
| LCR (4.2) | Layer derivation integrity | Stage 2 |
| PBR (4.3) | Pillar derivation integrity | Stage 3 |
| CCR (4.4) | Domain-critical invariants that cut across all stages | RM directly |
| ECR (4.5) | Evidentiary honesty across all stages | ECR-0 Rating Scale |
| XCR (4.6) | Change discipline | README Standing Rules |
| CTR (4.7) | Tension-resolution discipline | Review package + this document |
| UHR (4.8) | Non-blocking treatment of source-absent parameters | RM source-gap items, Stage 2 §3.3/§6.3/§8.5/§9.4 |

---

## 6. Compliance check — Stages 1–3 against these rules

A pass through existing Stage 1–3 content against the rules above, to confirm no other
undisclosed violation exists:

| Check | Result |
|---|---|
| PIR-2 (one primary classification) | **Pass**, once the Need ruling (§1) is applied. Risk was already consistent. |
| PIR-3 (primitive→layer fan-out ≠ concept→primitive fan-out) | **Pass** — Condition and Context fan-out is disclosed as assumptions (A-01/A-02), not silent. |
| LCR-2 (Facet/State split) | **Pass** — enforced consistently across §2/§6 of Stage 2. |
| LCR-6 (Cognition non-assertion) | **Pass** — Stage 2 §8.4 states this rule explicitly and no layer entry violates it. |
| CCR-1 (altitude qualification) | **Pass** — RM §11.4 and Stage 2 §9.2 state the obligation; no ontology element currently uses an altitude-ambiguous term unqualified. |
| CCR-2 (action quarantine) | **Pass** — Stage 2 §9 and Stage 3 §3 (Pillar VI) both cite the RM §12 quarantine explicitly. |
| ECR-1/ECR-5 (citation integrity) | **Defect found and confirmed corrected at source** — Evidence was mislabeled as "(P4)" in Stage 2 §11/§12; both locations now read correctly per §4.5's historical record. Never misclassified any domain concept. |
| CTR-2 (single-answer requirement) | **Defect found and closed by §1** — Need was answered three ways; now one. |
| PBR-1 (pillars introduce no new primitive) | **Pass** — Stage 3 §2 states derivation direction explicitly; no pillar in §3 is cited as a primitive source. |

**Net result:** one substantive defect (Need) and one cosmetic defect (Evidence mislabel), both
now confirmed corrected at source. No other rule is violated by existing content.

---

## 7. Open Tensions and Parameter Gaps

### 7.1 Open Tensions Carried Forward

These represent genuine structural ambiguities or governance gaps that remain unresolved, tracked here to prevent them from blocking Stage 5.

All items in this category have now been formally resolved. The final previously unresolved item (CCR-7) was closed by subsequent governance:

| Rule | Status | Why it is not blocking |
|---|---|---|
| CCR-7 — Temporal Perspectives rule | **RESOLVED per Stage 7 G2** (see §4.4) | Governance formally resolved this item via a dedicated ontological analysis, establishing one temporal foundation with multiple temporal perspectives. It is no longer an open tension. |

Every other tension named in the pre-Stage-5 review package (§7.2 below) has been structurally resolved and is not repeated here.
### 7.2 Structurally Resolved but Parameter-Absent

There are no unresolved structural questions for the items below. What remains missing is strictly the **empirical value/rule** which the current authoritative project sources do not specify. These are formally classified as Source-Absent Parameters.

None of the following prevents Stage 5 (Ground Truth Reviews) from beginning. Each has an explicit UHR treatment (§4.8) that lets the architecture proceed.

| Structurally Resolved Domain Concept | Structural Classification (Established) | Source-Absent Parameter (Not defined in sources) | UHR treatment |
|---|---|---|---|
| **Family Structure vs Household** | Entities (P4) bounded by kinship vs shared economy. | The ontology establishes the entities, but no authoritative project source specifies the membership determination rules or parameters. | UHR-2 equivalent |
| **Person-sameness / Identity** | Persisting subject is an Entity (P4); Sameness assertion is a Claim evaluated by an Epistemic Stance (P3). | The ontology establishes the identity-sameness mechanism class, but no authoritative project source specifies the operational attestation rules or conflict procedures. | UHR-4 |
| **Vulnerability / Risk Composition** | Emergent composite State (Layer 5) derived from compounding Conditions (P1). | The ontology establishes the composition boundary, but no authoritative project source specifies the qualitative/quantitative composition rules. | UHR-2 |
| **Evidence Taxonomy** | Evidence artifacts are Entities/Occurrences that ground an Epistemic Stance (P3). | The ontology establishes the grounding role, but no authoritative project source specifies an exhaustive evidence taxonomy or numerical epistemic weights. | UHR-1 |
| **Giving-side Content** | Actors are Entities; Restrictions are Constraints; Interactions are Coordination Patterns. | BL V1 explicitly excludes donor scope. Therefore, no authoritative project source specifies the donor kinds, pattern steps, or funding restriction types. | UHR-1, UHR-5 |
| **Human-facet Value Sets** | Structurally axes/dimensions (Facets) separated from values (States). | The ontology sets the dimensions, but no authoritative project source specifies the exhaustive controlled vocabularies. | UHR-1 |
| **Need-interaction model** | Scope accommodation. | The current evidence is insufficient to justify introducing a formal ontology-level relation type for this interaction. Provisionally treated as Cognition/documentation content. | Governed provisional — single-source practitioner evidence acknowledged by Stage 7 G4; retained as a governance decision pending broader corroboration. |
| **Service Providers as Actors** | Entities (P4). | Structurally modeled as active Entities capable of participating in coordination and making capacity decisions, while retaining a single-source evidence caveat. | Governed provisional — single-source practitioner evidence acknowledged by Stage 7 G4; retained as a governance decision pending broader corroboration. |
| **Outcome / Impact Ownership** | Distinct from measurement representations. | The ontology does not impose a universal ownership assignment to the Human Subject. Operational responsibility for measurement is explicitly delegated to architecture/workflow design. | Governed provisional — single-source practitioner evidence acknowledged by Stage 7 G4; retained as a governance decision pending broader corroboration. |
| **Funder Altitude** | Modeled via existing layers: Entities (L2), Norms (L4), and Coordination Patterns (L8). | No distinct third altitude layer or primitive exists based on current evidence. | Governed provisional — single-source practitioner evidence acknowledged by Stage 7 G4; retained as a governance decision pending broader corroboration. |
| **Case Orchestration** | Coordination Pattern (L8). | It is not a distinct domain primitive. Technical workflow implementation is deferred to architecture. | Governed provisional — single-source practitioner evidence acknowledged by Stage 7 G4; retained as a governance decision pending broader corroboration. |
| **Contradiction-representation** | Cognition (Layer 7). | Retains all conflicting claims with source attribution rather than overwriting. Resolution algorithms are deferred to architecture. | Option A Closure (CONFIRMED evidence — not a G4 item; no single-source caveat applies) |
| **Missing-information-representation** | Cognition (Layer 7). | The system preserves explicit epistemic information so that unknown or uncertain claims are not collapsed. | Option A Closure (CONFIRMED evidence — not a G4 item; no single-source caveat applies) |


---

## 8. Status

**Complete for this phase:** all eight rule categories defined and sourced; the Need
contradiction identified during the Stage 1–3 completion audit is ruled and closed (§1); a
compliance pass against existing Stage 1–3 content found one substantive defect (now closed) and
one cosmetic defect (flagged); all structural tensions are resolved explicitly (§7). All structural governance dependencies are now closed against authoritative Tier 1 sources.

**Not done, by design:** no practitioner validation of the domain content the rules govern; no taxonomy or value-set population.

**Blocking for Stage 5:** None. The rules in §4 are sufficient to begin Ground Truth Reviews —
which test the ontology's content against real cases — without further Stage 1–4 rework.

**Propagation — CONFIRMED COMPLETE.** The two patch cells specified in §1 and the two citation
cleanups specified in §4.5 have been verified as applied at source, verbatim, in
`03-ONTOLOGY-PILLARS.md` and `02-ONTOLOGY-LAYERS.md` respectively, as of this remediation. This
section (§8) and §1/§4.5 remain the historical record of what was found and corrected, per
XCR-3; no further propagation action is required.


