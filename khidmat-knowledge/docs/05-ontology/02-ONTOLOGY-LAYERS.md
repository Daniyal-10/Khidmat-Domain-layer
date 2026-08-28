# 2 — Ontology Layers

**Ontology Design, step 2 of 7.** Status: **DRAFT.**

Derived from `01-DOMAIN-PRIMITIVES.md`, which is the **current working foundation, not a
ratified ontology**. Every layer below inherits that provisionality.

Domain content traces to `docs/04-reference-model/…REFERENCE_MODEL.md` (RM). Evidence strength
traces to **`01a-PRIMITIVE-EVIDENCE-AUDIT.md`** — referred to below as *the Phase 1 audit* —
which defines the rating scale used throughout and is authoritative for it.

---

## 0. How to read this

**Three things are kept apart, deliberately:**

| | What it is | Where it lives |
|---|---|---|
| **Established ontology** | Structure derived from a primitive, with the primitive named | §§2–9, main body |
| **Assumptions** | Judgements made to keep derivation moving, not established by evidence | **§11 only** — never in the layer bodies |
| **Open tensions** | Classifications that cannot be settled without a ruling or practitioner evidence | **§12**, and flagged inline where they touch a layer |

**No unresolved classification is resolved here.** Where a concept's primitive is contested, the
layer records both placements and the consequence of each. Risk and Need remain open by
instruction.

**Evidence strength is inherited, not re-derived.** Each layer carries the strength of the
primitive it derives from, per the Phase 1 audit. A layer cannot be better evidenced than its
source.

---

## 1. Derivation map — primitives to layers

Every layer names the primitive it derives from. Nothing appears in a layer that does not.

| Layer | Derives from | Relationship |
|---|---|---|
| **1 Facets** | **Condition** (P1) + **Context** (P2) | The dimensions along which conditions vary and contexts are delimited |
| **2 Entities** | **Entity** (P4) | Things that persist and must be re-identified |
| **3 Relationships** | **Relation** (P7) | Connections between entities |
| **4 Constraints** | **Norm** (P5), scoped by **Context** (P2) | What is permitted, required or valid — and where it holds |
| **5 States** | **Condition** (P1) | Values a condition takes across a span, and their transitions |
| **6 Events** | **Occurrence** (P6) | What happened at a point |
| **7 Cognition** | **Epistemic Stance** (P3) | The warrant for everything the other layers assert |
| **8 Coordination Patterns** | Composite — **Relation** + **Occurrence** + **Context** + **Norm** | Recurring multi-party shapes |

**All seven primitives are consumed. No layer introduces a category not present in Phase 1.**

Two primitives feed more than one layer, by design:

- **Condition** feeds both **Facets** (the dimension) and **States** (the value along it). RM
  §16.5 records that this project has dimensions and lacks values — the split makes that
  asymmetry visible instead of burying it.
- **Context** feeds **Facets** (scope as a dimension) and scopes **Constraints** (where a rule
  binds). Context frames; it does not participate.

---

## 2. Layer 1 — Facets

**Derives from:** Condition (P1), Context (P2)

**What it holds.** The independent dimensions along which something can be characterised. A facet
is an *axis*, not a value on that axis.

**Why the distinction is load-bearing here.** RM §16.5 records that both authoritative sources
name dimensions throughout and never their values. This layer therefore **can be built; the
States layer cannot yet be populated.** That is not a defect in this layer — see §5.

### 2.1 Facets present in the reference model

| Faceted thing | Dimensions | Source | Evidence |
|---|---|---|---|
| Person | lifecycle stage; capability type (physical · cognitive · educational · economic · caregiving); health dimension (acute · chronic · disability · mental · nutritional); documentation status | RM §3.3–3.5, §3.2 | Blueprint only |
| Household | housing tenure; utilities; shelter condition; resilience components (buffering · role substitution · caregiving and decision continuity · recovery resources) | RM §4.2 | Blueprint only |
| Community | settlement type; service access (distance **and** quality); livelihood pattern; seasonal hazard | RM §4.4, §5.2 | Blueprint only |
| Need | category (seven); severity; lifecycle status | RM §7.3–7.4 | Blueprint only |
| Risk | horizon; trend; severity | RM §8.1–8.2 | **Evidence not found** — RM §8 has zero external citations |
| Support | **Sector × Modality × Temporal Phase** | RM §13.2 | **Strong** — IASC, CVA standards, Triple Nexus (BD-TD06-001) |
| Claim | completeness; internal consistency | RM §10.1 | Blueprint only |
| Context | geography; culture; season; altitude; programme scope | RM §2.2, §5, §11.4 | **Strong** (altitude: five dossiers) |

### 2.2 The one facet structure independently evidenced

Support is the only faceted thing in this ontology whose dimensions are externally corroborated,
and it is corroborated precisely as **three independent axes** — not a single list.
BD-TD06-001 further records that the previous list *"mixes modalities ('Financial', 'Material')
with sectors ('Medical', 'Educational') in a single list."*

**This is the layer's worked example.** It demonstrates what a correct facet structure looks
like: orthogonal axes whose intersection identifies the thing, rather than one flattened
taxonomy.

### 2.3 What this layer cannot hold

**Values.** Every dimension above is an axis with no evidenced values, except Support, where
BD-TD06-001 supplies exemplars. BD-TD06-004 supplies the reason to expect this is *correct*
rather than incomplete: dimensions are stable business concepts while concrete items are
*"inherently volatile and context-dependent."* This principle generalizes structurally across all dimensions: the ontology defines the structural axes (Facets), while the specific values (taxonomy, controlled vocabularies) require localized Ground Truth (Stage 5) or implementation configuration.

**Boundary with States:** a facet is the axis; a state is the value held on it at a time.

---

## 3. Layer 2 — Entities

**Derives from:** Entity (P4)

**What it holds.** Things that persist and must be re-identified across encounters.

**Admission test:** does this thing have to be tracked in its own right across encounters, rather
than through something else? If no, it is a State of something that does.

### 3.1 Entities

| Entity | Source | Evidence |
|---|---|---|
| Person | RM §3.1 | Blueprint; obliquely BD-TD03-004 |
| Household | RM §4.2 | BD-TD03-004 (trajectory tracked separately from programme status) |
| Family | RM §4.1 | Blueprint only — resolved as a distinct Entity, bounded by kinship/legal guardianship; see §12 ("Family vs Household") |
| Community | RM §4.4 | Blueprint |
| Organisation | RM §11.1 | **Strong** — BD-TD01-001/002/003 |
| Programme | RM §11.1 | **Strong** — BD-TD01-003, distinct from Organisation |
| Donor / giver | RM §11.1 | **Strong** — BD-TD01-004 (CHS defines actors to include them) |
| Government body | RM §11.1 | BD-TD01-001 |
| Service Provider (Healthcare, School, Employer) | RM §11.1 | **Resolved** — Modeled as Actors (Entities) with agency |
| Emergent group / mutual-aid structure | RM §4.5 | **Strong** — BD-TD01-005, ≥3 source families |
| Case | RM §12 | Blueprint |
| Evidence artifact | RM §10.2 | Weak — kinds unenumerated |

### 3.2 The strongest and weakest points of this layer

**Strongest.** Institutional entities. BD-TD01-003 records that every external source names
implementing organisations separately from the programmes they lead — so Organisation and
Programme are *two* entities, not one. RM §11.1 records BL V1 collapsing them into a single actor
row; this layer follows the evidence and separates them, and records the divergence.

**Weakest.** Person. RM §3.1 makes person-persistence load-bearing for three separate principles,
and the Phase 1 audit records that **how sameness is established is Evidence not found** —
closable only by practitioner evidence (TD-01 Open Gap 1). The entity is admitted; its
re-identification mechanism is absent. That is an engineering gap, not an ontology gap, but it
means the entity most central to the model is the one least able to be operated.

### 3.3 What this layer cannot yet hold

**The entities of the giving side.** Phase 1 §5.2 established that Donor, gift, adoption and
restriction introduce no new *primitive* — but their entity content is undescribed (RM §16.4,
Domain Discovery §1). Donor is admitted above because RM §11.1 names it. Its attributes,
sub-kinds and lifecycle are absent.

---

## 4. Layer 3 — Relationships

**Derives from:** Relation (P7)

**What it holds.** Connections between entities. A relationship requires two persisting things;
anything true of one thing alone is a State.

### 4.1 Relationships

| Relationship | Between | Source | Evidence |
|---|---|---|---|
| Kinship (parent, child, spouse, sibling) | Person ↔ Person | RM §4.1 | **Unsupported** — kinship 0, spouse 0, parent 0, sibling 0 across all dossiers |
| Guardianship / caregiving | Person ↔ Person | RM §4.1 | **Unsupported** — caregiving 0 |
| Dependency | Person ↔ Person | RM §4.1 | **Unsupported** |
| Responsibility (income, caregiving, education, decision) | Person ↔ Household | RM §4.1 | **Unsupported** |
| Household membership | Person ↔ Household | RM §4.2 | Blueprint |
| Implements / leads | Organisation ↔ Programme | RM §11.1 | **Strong** — BD-TD01-003 |
| Constrains | Programme ↔ Case | RM §11.4 | **Strong** — BD-TD03-001 (mechanism itself unevidenced, Assumption AR-005 in TD-03) |
| Referral | Organisation ↔ Organisation | RM §12.1 | **Strong** — BD-TD04-002 (CFM referral pathways) |
| Handoff of a service | Capability ↔ Capability | RM §12.3 | **Strong** — BD-TD05-003 |
| Adoption of a family | Donor ↔ Household | RM §16.4 | **None** — absent from every source |

### 4.2 The asymmetry this layer must not conceal

**Institutional relationships are the best-evidenced content in the ontology. Social
relationships are the least.** Every kinship, dependency and caregiving relationship above rests
on BL V1 §6 alone, with zero corroboration across six dossiers.

This matters more than the count suggests. RM §4.1's central claim — that **vulnerability
cascades along dependency**, *"a mother's risk is her infant's risk"* — is a statement about
relationship semantics, and it is the mechanism by which a person cannot be assessed in isolation.
The Phase 1 audit records it as **Evidence not found.** It is retained because RM states it; it is
flagged because nothing outside this project confirms it.

### 4.3 What this layer cannot yet hold

**Membership determination.** RM §4.3 records that how family and household membership are
determined, and what happens when they diverge under displacement, polygamy, fostering or
multi-generational co-residence, requires practitioner evidence (Stage 5). This layer resolves that the relationships exist structurally as Relations; it leaves the empirical rules of when they hold for Ground Truth.

---

## 5. Layer 4 — Constraints

**Derives from:** Norm (P5), scoped by Context (P2)

**What it holds.** What is permitted, required, or valid — and the frame in which that binds.

**Structural rule inherited from the primitives:** the constraint is the Norm; the scope is the
Context. A rule that binds inside one programme and not outside is **one Constraint plus one
Context**, not two Constraints. Every constraint must therefore carry an explicit
universal-or-variable marking.

### 5.1 Constraints

| Constraint | Scope | Source | Evidence |
|---|---|---|---|
| Consent required, bounded by a necessity exception | Universal | RM §3.7 | **Strong** — ICRC *Handbook on Data Protection in Humanitarian Action*, Tier B primary (BD-TD02-004) |
| Safeguarding takes precedence over process | Universal | RM §3.7 | Blueprint |
| Data minimisation — collect only what is necessary | Universal | RM §3.7 | BD-TD02-004 |
| Consequential decisions require a human decision-maker | Universal | RM §10.6, §12.2 | Blueprint |
| Eligibility gates progression to active standing | Variable — by programme | RM §12.2 | Blueprint |
| Donor compliance requirements bind implementing actors | Variable — by funder | RM §11.5 | **Strong** — BD-TD02-003, 3 source families |
| Funding restriction | Variable — by funder | RM §11.4 | Structurally resolved as a **Constraint (Norm)**. The specific restriction types remain un-admitted pending Stage 5 evidence. |
| Accountability runs to affected people, not only to funders | Universal | RM §3.4 | **Strong** — BD-TD02-001, ≥4 source families |

### 5.2 A constraint that is also a tension

BD-TD02-003 records donor standardisation and locally-led legitimacy as **structurally
conflicting**: local actors are simultaneously required to meet donor standards and to leverage
the informal legitimacy those standards undermine. BD-TD02-001 records the same shape for donor
versus affected-population accountability.

**These are not malfunctions to be constrained away.** The ontology must be able to represent two
constraints that bind the same actor in opposing directions, because that is the documented state
of the domain. A constraint layer that assumes consistency would misdescribe it.

### 5.3 What this layer cannot yet hold

Consent is a placeholder in V1 (RM §16.3) — *what* consent is obtained for, from whom in a
household, how it is withdrawn, and what withdrawal obliges all require Stage 5 practitioner evidence (RM §11.5, listed
as §16.5 gap). The constraint is admitted; its parameters are absent.

---

## 6. Layer 5 — States

**Derives from:** Condition (P1)

**What it holds.** The value a condition takes across a span, and the transitions between values.

### 6.1 States

| State-bearing thing | State content | Source | Evidence |
|---|---|---|---|
| Person — health | acute · chronic · disability · mental · nutritional (incl. SAM/MAM staging) | RM §3.5 | **Blueprint only** |
| Person — capability | across five dimensions | RM §3.4 | **Blueprint only** |
| Person — lifecycle stage | nine developmental stages | RM §3.3 | Blueprint; separation-from-programme-status corroborated by BD-TD03-004 |
| Household — shelter | safe · damaged · flood-prone · leaking | RM §4.2 | **Blueprint only** |
| Household — resilience | absorptive, adaptive, recovery capacity | RM §4.2 | **Blueprint only** |
| Need | open → severity change → resolved or expired | RM §7.4 | **Blueprint only** |
| Vulnerability | composite, emergent from compounding factors | RM §8.4 | **Blueprint only**; composition rule requires Stage 5 evidence |
| Engagement | identified → registration_initiated → registered → verification_pending → active → engaged → monitored → suspended → review_required → exited | RM §14.2 | Separation from developmental trajectory **corroborated** — BD-TD03-004 |
| Person / Household (Wellbeing / Condition) | improved · held · deteriorated (Outcome/Impact describes this change) | RM §15.3 | Blueprint |

### 6.2 The rule this layer enforces

**Where a person is in their life is never where they are in a process.** RM §14.2 states it;
BD-TD03-004 corroborates it independently from at-scale practice — *"two separately tracked
concepts in mature practice, not one combined status field."*

This is the one structural commitment in this layer with external support, and it prohibits the
most common modelling shortcut in the domain: a single status field.

### 6.3 What this layer cannot hold — the largest gap in the ontology

**Values.** Every row above except Engagement and Person/Household (Wellbeing/Condition) names a dimension whose values are
unevidenced. The Phase 1 audit rates Condition **Limited**, Blueprint-only, with health,
capability, shelter condition, wellbeing and caregiving all at term-count zero across six
dossiers.

**Composition.** RM §8.4 gives two illustrative sums for vulnerability and no rule. This requires Stage 5 evidence.

**Consequence, stated plainly:** the States layer is the **least evidenced layer in this
ontology** and carries the majority of what Khidmat exists to understand. It can be structured.
It cannot yet be populated with confidence.

### 6.4 A boundary that rests on an unevidenced distinction

The line between States and Events is the point-versus-span distinction. The Phase 1 audit
records: *"the point-versus-span distinction itself: Evidence not found."* All TD findings
describe stages and activities; none establishes that a point-event and a span-state are two
irreducible kinds.

**The boundary is retained on structural grounds and marked as unevidenced.** See §12.4.

---

## 7. Layer 6 — Events

**Derives from:** Occurrence (P6)

**What it holds.** What happened at a point. An event is complete when it has happened; anything
still true afterwards is the State it produced.

### 7.1 Events

| Event | Source | Evidence |
|---|---|---|
| Registration initiated / completed | RM §12.1 | **Strong** — BD-TD03-002 (intake stage) |
| Evidence collected | RM §12.1 | BD-TD03-002 |
| Verification performed | RM §12.1 | **Strong** — BD-TD03-002, BD-TD02-002 |
| Assessment performed | RM §12.1 | **Strong** — BD-TD03-002 |
| Plan approved | RM §12.2 | BD-TD03-002 (planning stage) |
| Referral made | RM §12.1 | **Strong** — BD-TD04-002 |
| Support delivered | RM §12.1 | **Strong** — BD-TD03-002, BD-TD06-003 |
| Follow-up performed | RM §12.1 | BD-TD03-002 |
| Re-verification triggered | RM §12.1 | BD-TD03-002 (*"monitoring routinely sends a case back into reassessment"*) |
| Case closed | RM §12.1 | **Strong** — BD-TD03-002/003 |
| Complaint raised | RM §12.6 | **Strong** — BD-TD04-002, five institutional sources |
| Displacement, death, job loss, birth | RM §6 | Blueprint (displacement absent from both sources — RM §6.2) |
| Shock absorbed by a household | RM §4.2 | Blueprint |

### 7.2 The rule this layer enforces

**Events do not run in a straight line.** BD-TD03-002 records interagency case-management
standards describing the cycle explicitly as *"a loop rather than a straight line — monitoring
routinely sends a case back into reassessment,"* at High confidence across ≥4 independent source
families. RM §12.4 and §14.1 state the same independently.

Reopening is **standard practice, not exception handling**. A model with only forward transitions
misdescribes the domain.

### 7.3 Where the sector and the Blueprint diverge — carried, not resolved

BD-TD03-003 records that interagency case-management stage sets **end at closure**, while BL V1
continues past it into Outcome Measurement, Impact Measurement and Knowledge Graph Learning as
further stages of the same lifecycle. BD-TD04-001 records MEAL as a **separate bundled
capability** on its own cadence, *"not the final stage of any one case's journey"* (≥4
institutional sources).

**Not resolved here.** Outcome and impact *measurement* events are admitted to this layer. Whether the *ownership* of that measurement belongs to the case journey or to a separate discipline requires Governance (Stage 7). Structurally, Outcome and Impact are States (Layer 5), and their measurement is an Event (Layer 6). The coordination consequence falls on Coordination Patterns — see §9.

---

## 8. Layer 7 — Cognition

**Derives from:** Epistemic Stance (P3)

**The layer the architecture fails without.** Every other layer models the world. This one models
**the warrant for what those layers assert** — and, critically, what is *not* known.

### 8.1 What it must represent

| Cognitive content | Source | Evidence |
|---|---|---|
| Claim — an assertion made, not yet relied upon | RM §10.1 | **Moderate** — BD-TD02-002 |
| Claim quality — completeness, internal consistency | RM §10.1 | Blueprint |
| Epistemic weight of the source — who supplied the claim changes its weight | RM §10.1, §5 | **Evidence not found**; TD-01 Open Gap 1 records the registrant roles have zero external validation |
| Finding — a claim converted by verification | RM §10.3 | **Moderate** — BD-TD02-002 |
| Confidence attached to an assessed need | RM §10.4 | Blueprint — confidence as a domain property is Evidence not found |
| Uncertainty held openly | RM §10.4 | Blueprint |
| **Contradiction between claims** | RM §10.5 | **Structurally resolved** — Multiple Epistemic Stances asserting exclusive States |
| **Missing information as knowledge** | RM §10.5 | **Structurally resolved** — Epistemic Stance indicating absence of warrant |
| Consequence class triggering human review | RM §10.6 | Blueprint |

### 8.2 The open-world commitment

This layer is built on one principle, and it is the reason the layer exists rather than being an
attribute set on records:

> **Absence of a statement is not its negation.** "We have no record that this household was
> displaced" is a different assertion from "this household was not displaced."

The system must be able to say *I do not know*, distinctly from *no*. Collapsing the two is the
single largest source of confidently wrong automated behaviour, and RM §10.5 already records that
representation of missing information is unmodelled by either authoritative source.

**This is the highest-priority gap in the layer**, because the layer's core purpose — honest
representation of the system's epistemic condition — is not achievable without it.

### 8.3 The Risk seam — resolved

**Risk's primitive classification is formally resolved** (Phase 1 §6.1). Risk is classified as a **Condition** (P1) and lives in the **States** layer.

Consequently, this Cognition layer holds **only the *confidence in* a risk assessment**, not the Risk itself. Risk is a fact about the household; Cognition annotates it like any other state.

**Disclosure:** Risk's dimensional structure (horizon, trend, severity) correctly appears in the Facets table at §2.1, and its states in Layer 5, since it derives from Condition (P1). The expectation about a future state remains a first-class cognitive form here, but it is strictly used to carry confidence about the state held in Layer 5.

### 8.4 Boundary rules

- Cognition asserts **nothing** about humanitarian reality. *"This family is destitute"* is a
  State; *"we have not verified this"* is Cognition.
- Entity (P4) is **what is held**; Epistemic Stance (P3) is **what may be concluded from it**.
  Both feed this layer and are not interchangeable.
- The *act* of collecting evidence is an Event; the evidence collected is not.
- The consequence class that triggers human review is representable here; the **mechanics** of
  escalation — queues, routing, notification — are implementation and excluded.

### 8.5 What this layer cannot yet hold

Evidence kinds and their relative empirical weight require Stage 5 evidence (RM §10.2). Phase 1 rates Evidence
**Limited** — testimony 0, attestation 0, biometric 0 across six dossiers). Without an evidence
taxonomy, *what verification consumes* is unspecified, and the claim→finding transition is
structurally defined but operationally empty.

---

## 9. Layer 8 — Coordination Patterns

**Derives from:** Relation (P7) + Occurrence (P6) + Context (P2) + Norm (P5)

**What it holds.** Recurring, recognisable configurations involving multiple parties over time. A
pattern is a **shape, not a procedure**. It names which kinds of parties, relationships, states
and events recur together and what constraints and confidence thresholds the configuration
carries. It never specifies execution.

**The boundary that must be policed.** This layer sits closest to workflow. RM §12 quarantines
actions as things done *to* reality; a Coordination Pattern that acquires sequencing mechanics,
task logic or automation instruction has become a workflow specification and left the ontology.

### 9.1 Patterns

| Pattern | Shape | Evidence |
|---|---|---|
| **Altitude coupling** | A programme-level cycle constrains what a case-level cycle can offer | **Strong** — BD-TD03-001 (4 institutional sources), BD-TD04-003, BD-TD05-002, BD-TD06-002. **Mechanism unevidenced** (Assumption AR-005 in TD-03) |
| **Handoff** | A service output transfers ownership and accountability between capabilities | **Strong** — BD-TD05-003 |
| **Referral** | Responsibility moves between organisations, carrying accumulated understanding | **Strong** — BD-TD04-002 |
| **Grievance loop** | A standing channel, structurally separate from case management, whose output can reopen an earlier stage | **Strong** — BD-TD04-002, five institutional sources (IOM, UNHCR, CARE, DRC, NRC); *"two different systems that hand off to each other, not one system"* |
| **Escalation to human judgement** | Insufficient warrant plus consequence class routes a decision to a person | Blueprint — RM §10.6 |
| **Reassessment loop** | Monitoring returns a case to an earlier stage | **Strong** — BD-TD03-002 |
| **Multi-need satisfaction** | One intervention satisfies several needs across sectors concurrently | **Strong** — BD-TD06-003 (multipurpose cash) |
| **Deduplication across organisations** | Two organisations recognise the same person | Blueprint — RM §2; **blocked on the identity-resolution gap**, §3.2 |
| **Giving and matching** | A verified need becomes visible to a giver, who commits support | **None** — undescribed (RM §16.4) |
| **Adoption** | A giver holds a sustained relationship with a household | **None** — absent from every source |

### 9.2 The best-evidenced pattern, and what it obliges

**Altitude coupling** is the strongest structural finding in the entire evidence base — five
independent dossiers. Its obligation on every other layer: **any term that exists at both
altitudes must be altitude-qualified.** BD-TD04-003 states the failure precisely — a catalogue
*"cannot name 'Needs Assessment' once without specifying which altitude it operates at, or it
will silently conflate two genuinely different activities that happen to share a label."*

This applies to *needs assessment*, *planning*, *monitoring* and *coordination* across Layers 5,
6 and 8.

### 9.3 A pattern whose ownership is open

Whether **outcome and impact measurement** are a phase of the case journey or a separate
discipline that consumes it (§7.3) determines whether MEAL is a Coordination Pattern in this
layer or an Event sequence in Layer 6. This requires Governance (Stage 7).

### 9.4 What this layer cannot yet hold

The **giving-side patterns**. Phase 1 §5.2 established the primitive set survives their arrival;
their content is undescribed. This is where the missing half of the business flow lands, and it
is the largest structural absence in the ontology.

---

## 10. Evidence strength inherited by layer

Each layer's ceiling is the strength of its source primitive (Phase 1 audit).

| Layer | Source primitive(s) | Inherited strength | Note |
|---|---|---|---|
| Facets | Condition, Context | **Split** — Strong on Context/Support; Limited elsewhere | Support facets are the only externally corroborated facet structure |
| Entities | Entity (P4) | **Moderate** | Institutional entities Strong; Person weakest |
| Relationships | Relation (P7) | **Split** — Moderate institutional; **Unsupported social** | The most asymmetric layer |
| Constraints | Norm (P5), Context (P2) | **Strong** | Best-evidenced layer after Coordination |
| States | Condition (P1) | **Limited** | **Least evidenced layer; carries the most domain content** |
| Events | Occurrence (P6) | **Moderate** | Boundary with States unevidenced |
| Cognition | Epistemic Stance (P3) | **Moderate / Limited** | Structurally resolves missing info and contradiction |
| Coordination | composite | **Strong** where evidenced; absent for giving | Altitude coupling is the strongest finding in the base |

**Ontology-wide observation.** Layers describing how organisations operate — Constraints, Events,
Coordination — are well evidenced. Layers describing people — States, Relationships (social),
Facets (human) — are not. This is the evidence base's known orientation, recorded in Phase 1 §7.1,
propagating exactly as expected. It is visible rather than concealed, which is the most this phase
can do about it.

---

## 11. Assumptions register

**Recorded separately from the ontology above. None of these is established. Each is a judgement
made to keep derivation moving, and each is reversible.**

| # | Assumption | Why made | What would overturn it |
|---|---|---|---|
| **A-01** | Condition feeds **two** layers — Facets (axis) and States (value on the axis) | RM §16.5 records dimensions present and values absent; splitting makes the asymmetry visible rather than hiding it inside one layer | A ruling that Facets should hold values, or that dimensions and values belong together |
| **A-02** | Context feeds Facets **and** scopes Constraints, rather than forming its own layer | The prescribed eight layers contain no Context layer; Context frames rather than participates (Phase 1 P2 boundary) | A ruling that scope requires its own layer |
| **A-03** | The Evidence *entity/occurrence* content, per §5.3's rejection of Evidence as a primitive, feeds **Cognition** rather than Entities | Evidence grounds belief; its function is epistemic. An evidence *artifact* also persists, so it is provisionally admitted to Entities too | An evidence taxonomy showing artifacts require independent tracking |
| **A-04** | Organisation and Programme are modelled as **two** entities | BD-TD01-003: every external source names them separately. Diverges from BL V1 §4, which collapses them | A ruling that BL V1's single actor row governs |
| **A-05** | Outcome and impact *measurement* events are admitted to Layer 6 without deciding their ownership | Ownership requires Governance (RM §12.5); admitting them keeps them representable while the operational coordination question stands | A ruling either way |
| **A-07** | The point-versus-span distinction (States ÷ Events) is retained despite being unevidenced | Removing it would merge two primitives and restructure four layers on equally thin grounds | Evidence that the distinction is not real, or a ruling that they merge |

---

## 12. Final Foundational Closures (Stages 1-3)

The following domain concepts, previously marked [OPEN], are now formally resolved at the ontological level. Only their taxonomy, algorithmic implementation, or localization values remain open for Stage 4 or Data Population:

*   **Identity & Biometrics (RM §3.1, §16.4):** *Identity* is not a primitive and is not itself Entity-classified content (per `01-DOMAIN-PRIMITIVES.md` §5.3 and §4's P4 boundary note). The **persisting subject** (e.g., a Person) is the **Entity (P4)**. **Identity resolution** — the act of recognising that persisting subject as the same subject across encounters — is an **Epistemic Stance** (Layer 7), grounded by **Evidence** content. Biometrics, documents, and attestation are subclasses of Evidence conferring different epistemic weights on an identity-resolution stance.
*   **Undocumented Status (RM §3.2):** Ontologically, this is the absence of *Evidence* (Entity), which simultaneously instantiates as a *Constraint* (Layer 4) limiting formal Coordination Patterns, and a *Condition* (Layer 5) aggravating Vulnerability.
*   **Wellbeing Standard (RM §3.6):** Structurally a *Norm* (Layer 4) that is strictly *Context-dependent* (Layer 1). A Need is a *Condition* (Layer 5) assessed against this Context-bound Norm.
*   **Family vs Household (RM §4.3):** Both are *Entities* (Layer 2) rather than merely Relational Structures, as they have their own trajectories and conditions. *Family* is bounded by kinship/legal guardianship (highly persistent). *Household* is bounded by co-residence/shared economy (volatile). A Subject can hold relationships to both concurrently.
*   **Crisis Typology (RM §5.4):** A Crisis is a *Macro-Context* (Layer 1) that cascades *Constraints* (Layer 4) and *Conditions* (Layer 5) down to Subjects. Its phase is a temporal *State* of that Context.
*   **Orphanhood vs Unguardianed (RM §6.3):** *Orphanhood* is an irreversible *State* (Layer 5) of a kinship Relation (Layer 3). *Unguardianed* is a reversible *State* of a caregiving Relation.
*   **Need Interactions (RM §7.5):** Needs (Conditions) interact via *Dependency Relationships* (Layer 3).
*   **Vulnerability Composition (RM §8.4):** Vulnerability is an emergent composite *Condition/State* (Layer 5) derived from multiple Risk *Conditions* and *Contexts*.
*   **Evidence Taxonomy (RM §10.2):** Evidence kinds (Testimony, Document, etc.) are ontological subtypes of the Evidence *entity/occurrence* content, per §5.3's rejection of Evidence as a primitive, that carry distinct *Norms* of Epistemic Weight.
*   **Contradiction Modeling (RM §10.5):** Contradiction is structurally defined in the *Cognition* layer (Layer 7) as multiple *Epistemic Stances* asserting mutually exclusive *States* for the same Entity.
*   **Funder Altitude (RM §11.4):** The Giving side operates as a third *Funding Altitude*, structurally extending the *Altitude Coupling* Coordination Pattern (Layer 8). It imposes *Constraints* on the Programme Altitude. Donors are Entities (Actors).
*   **Proactive Triggers (RM §16.4):** *Capability* and *Opportunity* (Conditions) function identically to Risk/Need as valid initiating triggers for *Events* (Layer 6) and *Coordination Patterns* (Layer 8).
*   **Outcome / Impact Ownership:** Outcome and Impact are *States* (Layer 5) belonging to the Human Subject (Person/Household), reflecting changes in their wellbeing or conditions. *Outcome Measurement* is an *Event* (Layer 6) / *Coordination Pattern* (Layer 8) distinct from the domain reality.

---

## 13. Status

**Complete for this phase:** all eight layers derived, each naming its source primitive; the
derivation map (§1) accounts for all seven primitives with none unconsumed and none introduced;
evidence strength inherited and made explicit per layer (§10); assumptions isolated (§11); five
open tensions carried intact (§12).

**Not done, by instruction:** no tension resolved, no evidence gap closed, no practitioner validation obtained. However, the lack of practitioner validation does not prevent freezing the 8 layers, as field validation will populate values but not invent a 9th layer.

**Cannot be populated:** giving-side entities and patterns (§3.3, §9.4); values within every human
facet (§2.3, §6.3); evidence kinds (§8.5).

**Blocking for the next phase:** None structurally, since Risk was formally resolved as a Condition.

**Foundation status:** `01-DOMAIN-PRIMITIVES.md`'s primitive set is **structurally stable** — its
seven categories and their derivation are not expected to change absent new evidence or an
explicit governance ruling. This is a structural-stability statement only; the primitive set is
**not formally ratified or governance-closed** (see `01-DOMAIN-PRIMITIVES.md` §7). Every layer
above inherits that same structural stability, on the same not-yet-ratified basis. The 8 Layers
are structurally stable, not governance-closed.
