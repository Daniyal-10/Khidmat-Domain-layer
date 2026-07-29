# 1 — Domain Primitives

**Ontology Design, step 1 of 7.** Status: **DRAFT — set not closed.** See §7.

---

> ## ⚠ GATE QUESTION — read before anything else
>
> **`REFERENCE_MODEL.md` §17, which is FROZEN, states:**
>
> > *"One ruling is still required before primitive discovery can begin: whether a Domain
> > Primitive means a concrete irreducible of reality (Person, Household, Need) or a category of
> > concept (Identity, Relation, Condition). The entire ontology derives from the answer."*
>
> **That ruling was not obtained. This work proceeded under a ruling the authors made.**
>
> **Ruling taken:** a Domain Primitive is a **category of concept**.
>
> **Argument, in three sentences.** The prescribed step 2 builds a layer named *Entities*, and
> layers derive from primitives. If *Person* were a primitive it would be both the source of the
> Entities layer and a member of it, and the derivation would be circular. Only a category can
> stand above eight layers that themselves include Entities and Relationships.
>
> **Consequence of a contrary ruling: Phase 1 is void and Phase 2 with it.** Both documents
> would require rebuilding from the primitive definition upward. Nothing downstream survives.
>
> **This is the first thing the Project Lead should ratify or reverse.** It is not presented as
> settled. Full reasoning at §1; the strongest independent support for it is the falsification
> test at §5.2.

---

Derived from `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` (RM).
No concept enters from the methodology teaching documents.

---

## 1. What a Domain Primitive is

**A Domain Primitive is one of a small, closed set of categories of concept — the *kind of thing*
a humanitarian concept can be.**

A primitive is not a humanitarian concept. It is the classification axis under which every
humanitarian concept falls.

### Why this reading, and not the concrete one

Two readings have been in circulation: a primitive as a *concrete irreducible of reality*
(Person, Household, Need), or as a *category of concept* (Identity, Relation, Condition).

**The prescribed sequence settles it.** Step 2 builds layers, and one layer is named
**Entities**. Layers derive from primitives. If *Person* were a primitive, *Person* would be
both the source of the Entities layer and a member of it — the derivation would be circular and
step 2 would produce nothing. Only a category can stand above eight layers that themselves
include Entities and Relationships.

Three further confirmations from our own material:

1. **Concrete concepts fail irreducibility against our evidence.** RM §7.1 defines a need
   *relationally* — a gap between current state and a basic standard of wellbeing. A gap between
   two things is not irreducible. Household decomposes into people, dwelling and shared living.
   Risk decomposes into horizon, trend and severity (RM §8.1).
2. **The concrete set does not converge.** Working through RM §§3–15, the concrete reading
   yields Person, Family, Household, Community, Situation, Need, Risk, Capability, Evidence,
   Claim, Support, Outcome, Actor, Action, Context — fifteen and still counting. A primitive set
   that grows with the domain is not a primitive set.
3. **The methodology documents do not contradict this.** Their base unit is a *Class* — "the
   nouns of your domain." That corresponds to our **Entities** layer, not to a primitive layer;
   their methodology has no layer above entities at all. They are silent here, not opposed.

### Qualification tests

A candidate is a Domain Primitive only if it satisfies all five:

| # | Test |
|---|---|
| T1 | **Abstract.** A category, not a concept a humanitarian glossary would define. If a glossary could sensibly hold an entry for it, it is too concrete. |
| T2 | **Universal.** Required whether the domain is health, shelter, education, livelihood, protection or a domain not yet encountered. |
| T3 | **Necessary.** Removing it leaves some class of humanitarian knowledge unclassifiable — not merely awkward. |
| T4 | **Evidence-grounded.** At least one concept in the reference model already requires it. No primitive exists speculatively. |
| T5 | **Independent of organisation and technology.** Makes sense regardless of who operates the system or how it is built. |

### Rules governing the set

- **One primary classification per concept.** Where a concept appears to need two, that is
  treated as information — evidence the concept should be decomposed, or that the set needs
  review — and escalated, not resolved by permitting dual classification. Two such cases are
  open; see §6.
- **The set is closed once ratified.** An author meeting a concept that seems to need a new
  primitive escalates; they do not extend.
- **The set is not yet ratified.** See §7.

---

## 2. Method

For each concept in RM §§3–15, ask *what kind of thing is this?* — then ask the same question of
the answer, until answers stop multiplying and begin repeating. The recurring answers are the
candidate set.

Primitives are **discovered by abstraction from the reference model, never invented in the
abstract**, and never adopted because a modelling tradition or teaching document contains them.

---

## 3. Derivation trace

Every row is a concept from the reference model, with the kind-answer reached. This is the
audit trail: each answer can be checked against its source.

| Reference-model concepts | Kind-answer reached |
|---|---|
| Person (§3.1) · Family (§4.1) · Household (§4.2) · Community (§4.4) · Organisation, Programme, Donor, Government (§11.1) · Emergent groups (§4.5) | that which persists and must be re-identified |
| Parent, child, guardian, spouse, caregiver (§4.1) · dependency (§4.1) · responsibility (§4.1) · household membership (§4.3) · referral (§12.1) · adoption of a family (§16.4) | a connection between things that persist |
| Lifecycle stage (§3.3) · capabilities (§3.4) · health, disability, malnutrition (§3.5) · wellbeing (§3.6) · shelter condition, utilities (§4.2) · household resilience (§4.2) · need (§7.1) · vulnerability (§8.4) · engagement stage (§14.2) · outcome (§15.2) · documentation status (§3.2) | that which is true across a span, and can change |
| Registration, verification visit, delivery, referral, follow-up (§12.1) · displacement, death, job loss (§6) · a shock absorbed (§4.2) · complaint raised (§12.6) | that which happened at a point |
| Document, testimony, field observation, community attestation, measurement (§10.2) · proof of delivery (§12.1) | that which grounds a belief |
| Claim vs finding (§10.1, §10.3) · confidence (§10.4) · uncertainty, contradiction, missing information (§10.5) · epistemic weight of a registrant (§10.1) | the warrant the system holds for what it asserts |
| Consent and its bounded necessity exception (§3.7) · dignity as standing constraint (§3.7) · eligibility (§12.2) · safeguarding precedence (§3.7) · funding restriction (§11.4, stated there inside an `[OPEN]`) · human-review requirement (§10.6) | that which bounds what is permitted or valid |
| Geography, settlement type (§5.1) · seasonal calendar (§5.2) · cultural framing of household (§4.3) · crisis phase (§5.4) · programme vs case altitude (§11.4) · applicability scope (§2.2) | the frame relative to which a statement holds |

**Eight answers. Each recurs across multiple independent sections of the reference model. No
ninth answer survived a second pass** — except two contested classifications recorded in §6.

---

## 4. The eight Domain Primitives

Presented alphabetically. Order carries no meaning.

### P1 — Condition
**That which is true of something across a span of time, and which can change while what it is
true of persists.**

Irreducible because a condition cannot be decomposed into occurrences without loss: a chronic
illness is not the sum of the moments it was observed, and a household's absorptive capacity is
not the sum of the shocks it has absorbed. Removing Condition leaves no category for anything
that *is the case* rather than something that *happened*.

*Evidence:* RM §3.3–3.6, §4.2, §7.1, §8.4, §14.2, §15.2.
*Boundary:* ends where independent re-identification begins. The moment something must be
tracked in its own right across encounters rather than through what it qualifies, it is an
Identity. An *observation of* a condition is an Occurrence; the condition observed is not.

### P2 — Context
**The frame relative to which a statement holds — geographic, cultural, temporal, institutional
or programmatic — such that what is true within it is not thereby true outside it.**

Irreducible because nothing else carries scope. Remove it and every regularity observed in one
setting becomes a claim about all settings — the failure RM §2.2 names as structural to this
domain.

*Evidence:* RM §2.2, §5.1–5.4, §4.3, §11.4.
*Boundary:* Context frames; it does not participate. A geographic area that is itself tracked,
funded and reported on has crossed into Identity. Context stops short of the rule it scopes —
the scope is Context, the rule is a Norm.

*Load-bearing note:* RM §11.4's programme/case altitude split classifies here. This is what
prevents "needs assessment" meaning two things under one name.

### P3 — Epistemic Stance
**The warrant the system holds for what it asserts — including what it does not know.**

Irreducible because it is *about* the other categories rather than about the world. Every other
primitive models reality; this one models the relationship between reality and what anyone knows
of it. Remove it and claim-status, confidence, contradiction and absence-of-information become
untrackable, and RM §10.6's human-oversight rule becomes unenforceable.

*Evidence:* RM §10.1, §10.3–10.6, §3.1.
*Boundary:* a stance is never a fact about a household. "This family is destitute" is a
Condition; "we have not verified this" is an Epistemic Stance.

*Load-bearing note:* this is the primitive the Cognition layer (step 2) derives from. The
methodology's open-world principle — *absence of a statement is not its negation* — is
representable only because this category exists.

### P4 — Evidence
**That which grounds a belief.**

Irreducible because evidence is neither the claim it supports nor the confidence it produces. A
photograph of a damaged roof is not the damage, not the assertion of damage, and not the
confidence in that assertion.

*Evidence:* RM §10.2, §12.1.
*Boundary:* the *act of collecting* evidence is an Occurrence; the evidence collected is not.
Distinct from Epistemic Stance: evidence is what is held; stance is what may be concluded from it.

### P5 — Identity
**That which persists and must be re-identified across encounters.**

Irreducible because persistence-with-re-identification cannot be produced from the others. RM
§3.1 states that every promise about longitudinal reasoning rests on it, and RM §3.5's fairness
principle and RM §2's duplicate-registration problem both reduce to it.

*Evidence:* RM §3.1, §4.1–4.5, §11.1.
*Boundary:* something that is never tracked in its own right across encounters is not an
Identity — it is a Condition of something that is.

*Open:* RM §3.1 records that *how* sameness is established is unknown. That is a mechanism gap,
not an obstacle to the category — the category asserts only that re-identification is required
and may fail.

### P6 — Norm
**That which bounds what is permitted, required, or valid.**

Irreducible because a norm binds rather than describes. Consent, safeguarding precedence,
eligibility, funding restriction and the human-review threshold are not conditions of the world
and not stances about it; they constrain what may be done.

*Evidence:* RM §3.7, §10.6, §12.2, §13.4, §16.4.
*Boundary:* the Norm is the rule; the Context is the scope in which it holds. A norm that binds
inside one programme and not outside it is one Norm plus one Context, not two Norms.

*Load-bearing note:* the methodology's *"regulation lives inside the ontology — they ARE the
model"* is this primitive. Consent is not a compliance wrapper.

### P7 — Occurrence
**That which happened at a point in time.**

Irreducible because point and span do not derive from one another. RM distinguishes them
consequentially throughout — a displacement, a verification visit, a death, a delivery.

*Evidence:* RM §6, §12.1, §14.
*Boundary:* an occurrence is complete when it has happened. Anything that continues to be true
afterwards is the Condition it produced, not the occurrence itself.

### P8 — Relation
**A connection between things that persist.**

Irreducible because a relation holds *between* identities and cannot be reduced to a property of
either. RM §4.1's central finding — that vulnerability cascades along dependency, *"a mother's
risk is her infant's risk"* — is a statement that can only be made if connection is a category.

*Evidence:* RM §4.1, §4.3, §12.1, §16.4.
*Boundary:* a relation requires two persisting things. Something true of one thing alone is a
Condition.

---

## 5. Coverage test

The set is falsified if any concept in the reference model fails to classify without forced fit.

### 5.1 Against the described domain

Every concept in the derivation trace (§3) classified. No concept in RM §§3–15 was left
structurally homeless except the two in §6.

### 5.2 Against the undescribed giving side — the decisive test

Domain Discovery recorded that the giving and resourcing side of the business flow has no domain
description, and that primitives cannot be *closed* over a half-described domain. Testing the set
against the giving side as the Project Lead described it:

| Giving-side concept | Classifies as | Forced? |
|---|---|---|
| Donor, institutional funder | Identity | No — persists, must be re-identified |
| A gift or contribution | Occurrence | No — happened at a point |
| Donor adopting a family | Relation | No — connects two persisting things |
| Funding restriction on who may receive | Norm | No — bounds who may receive |
| Restricted funding chain | Norm scoped by Context | No |
| Verified need visible to a giver | Epistemic Stance + Norm | No — what may be disclosed, and on what warrant |
| Matching a need to a giver | Occurrence, under Norm | No |

**The giving side introduces no new primitive.** This is a substantive result: it converts the
"cannot close primitives over a half-described domain" blocker from structural to
content-only. The **entities** of the giving side remain undescribed and step 2 cannot populate
them — but the **primitive set survives their arrival**.

This is the strongest available evidence that the category reading is correct. Under the
concrete reading, Donor, Gift, Adoption and Restriction would each be candidate primitives and
the set would break.

### 5.3 Candidates examined and rejected

| Candidate | Rejected because |
|---|---|
| **Person** | Fails T1. A concept a glossary defines. Classifies under Identity. |
| **Time** | Fails T1, T3. Time is the medium in which Condition and Occurrence are distinguished, not a category anything classifies under. Nothing in RM is "a Time." |
| **Place** | Fails T3. Decomposes — a settlement tracked in its own right is an Identity; an applicability frame is a Context. |
| **Role** | Fails T3. A responsibility held by an identity across a span: Identity + Condition, or Identity + Relation. Decomposes without loss. |
| **Capability** | Fails T1, T3. A Condition of a person (RM §3.4). |
| **Dignity** | Fails T1 as a category. RM §3.7 makes it a standing constraint — a Norm — not a kind of thing concepts can be. Nothing classifies as "a Dignity." |
| **Action / Process** | Fails T3. RM §12 quarantines actions as things done *to* reality. Each is an Occurrence. |
| **Quantity** | Fails T1. A dimension of a Condition. RM records no evidenced value sets (§16.5). |

---

## 5A. Ontology scope decision

`REFERENCE_MODEL.md` §16.2 names this **"the first act of ontology design, performed as ontology
work."** It was not performed before the primitive derivation above, and content was instead
admitted by default. This section performs it and offers it for ratification.

**The test, stated by RM §16.2:** not *"is it real?"* — everything in RM §§3–15 is real — but
**"must Khidmat understand this to help people correctly?"**

**The governing rule, from the same section:** reality-membership does not imply
scope-membership, and scope-exclusion does not imply unreality.

| RM section | In ontology scope? | Basis |
|---|---|---|
| §3 Human reality | **In** | The six questions of RM §1 cannot be answered without it |
| §4 Social reality | **In** | RM §4.1 — vulnerability cascades along dependency; a person cannot be assessed in isolation |
| §5 Environmental reality | **In** | RM §5.2 — the same shelter damage is routine or emergency depending on season |
| §6 Humanitarian situations | **In** | The circumstances from which needs arise; needs are unintelligible without them |
| §7 Needs | **In** | The system's central object |
| §8 Risk | **In** | RM §1's sixth question — *what future risks are developing?* |
| §9 Capabilities and strengths | **In** | RM §9.2 — dependency reduction is impossible if only deficits are modelled |
| §10 Evidence and knowledge | **In** | RM §10.6 — human oversight is unenforceable without it |
| §11 Actors | **In** | Including givers, per the Option C decision recorded in `SCOPE_COVERAGE.md` §4 |
| §12 Actions | **In, constrained** | Admitted because understanding is acquired through them. **May never be the organising axis** (Standing Rule 4; RM §12 quarantine) |
| §13 Support | **In — dimensions only** | Sector × Modality × Phase are stable; the concrete catalogue is excluded as volatile per BD-TD06-004 |
| §14 Journey | **In** | The person's evolution, distinct from engagement state |
| §15 Outcomes | **In** | RM §15.1 — the definition of success for the project |

**Result: all of RM §§3–15 is in ontology scope**, with two qualifications — §12 admitted under
constraint, and §13 admitted at dimension level only.

**Why this is the right answer rather than a convenient one.** The narrower alternative would
exclude the giving side. `SCOPE_COVERAGE.md` §4 records that the Project Lead already chose
Option C — model reality fully, sequence implementation separately — and RM §16 was authored to
enact it. Excluding givers here would reverse a decision already taken, one layer further down.

**What this does not decide.** Ontology scope is not V1 implementation scope. RM §16.3's
exclusions stand unchanged: the ontology may *represent* givers, matching, biometric identity and
proactive identification; whether V1 *builds* them is a separate question RM §16.4 tables for
ruling.

**Status: offered for ratification.** If the Lead narrows this, the affected layers in Phase 2
contract accordingly; the primitive set is unaffected, since §5.2 established it survives the
giving side either way.

---

## 6. Two unresolved classification tensions

Both are central concepts that do not classify cleanly. Recorded as information, not resolved —
per the one-primary-classification rule.

### 6.1 Risk

RM §8.1 insists risk is **first-class**, with horizon, trend and severity, *"not a byproduct of
severity rules."* But a risk concerns something that has **not happened**.

- As **Condition**: being-at-risk is currently true of a household.
- As **Epistemic Stance**: a risk is a warranted expectation about a future Condition, which is
  what "horizon, trend, severity" describe.

The second reading is more faithful to RM §8.3 — *"the risk domain produces signals; it does not
decide"* — which is stance language. But it makes risk a fact about our knowledge rather than
about the family, and RM §8.1 explicitly resists demoting it.

**Consequence if wrong:** risk is one of the nine models. Misclassifying it misplaces an entire
branch of the ontology. **Must be resolved before step 2 builds the Cognition layer**, because
Cognition derives from Epistemic Stance and would either absorb risk or exclude it.

### 6.2 Need

RM §7.1 defines a need as **a gap between current state and a basic standard of wellbeing**.

- As **Condition**: a need is true of a household across a span and changes (RM §7.4).
- As **Relation**: a gap holds *between* a current state and a standard — and a relation between
  two things is precisely what Relation is for.

The Relation reading is more literal. The Condition reading matches how RM §7.4 describes needs
behaving — opening, changing severity, resolving.

**This tension is aggravated by an open question:** RM §3.6 records that the *basic standard of
wellbeing is undefined*. If a need is a Relation, the standard is one of its two ends and must
exist as something. If a need is a Condition, the standard can remain implicit. **Classification
here is partly blocked on a gap in the reference model.**

---

## 7. Status — why this set is not closed

**Ratifiable now:** the definition of a Domain Primitive (§1), the method (§2), the derivation
trace (§3), and the coverage result that the giving side introduces no new primitive (§5.2).

**Not closed, for three reasons:**

1. **Two classification tensions are open** (§6). Risk must be settled before the Cognition
   layer is built.
2. **Provenance disclosure.** These eight match the primitive set in the deleted
   `DOMAIN_PRIMITIVES.md` from the pre-reset repository. The derivation in §3 was performed
   against the reference model, but that file was read earlier in this session and independence
   cannot be certified. **The mitigation is that §3 is auditable** — each row can be checked
   against its reference-model source, so the set can be validated on its merits regardless of
   where the idea originated. It should be independently re-derived by someone who has not seen
   the deleted file before ratification.
3. **No practitioner validation exists** (RM §16.5). The set is structurally tested and
   empirically unvalidated.

### 7.1 The evidence base is asymmetric — measured

The six evidence dossiers cover the **organisational** side of humanitarian work and almost
none of the **human** side. Term counts across all six:

`widow 0 · orphan 0 · malnutrition 0 · disability 0 · displacement 0 · shelter condition 0 ·
caregiving 0 · family 1 · vulnerability 2 · household 6`

External citations in the reference model land the same way: ~34 of 49 fall in Actors, Scope,
Support and Actions; ~6 fall across Human Reality, Social Reality, Needs, Capabilities,
Evidence and Outcomes combined. **Business Logic V1 states nine models of humanitarian reality;
the evidence base covers one of them** (Support, via TD-06).

Consequence for this set — each primitive carries a different evidential weight:

| Primitive | Support |
|---|---|
| **Context** (P2) | Strong — altitude split, five independent dossiers |
| **Norm** (P6) | Moderate — ICRC consent guidance, funding restrictions |
| **Epistemic Stance** (P3) | Moderate — claim/finding split corroborated via TD-02 |
| **Occurrence** (P7) | Moderate — lifecycle and verification practice via TD-03 |
| **Evidence** (P4) | **Limited** — evidence kinds absent entirely: testimony 0, attestation 0, biometric 0 across six dossiers |
| **Identity** (P5) | Partial — trajectory/enrolment separation via TD-03 |
| **Condition** (P1) | **Business Logic V1 alone** — health, capability, shelter, vulnerability, resilience have no external corroboration |
| **Relation** (P8) | **Business Logic V1 alone** — family, dependency and caregiving are effectively absent from the dossiers |

**The two primitives carrying most of the human side rest on a single unvalidated source.**
This does not invalidate them — categories classify regardless of evidence density — but it is
where the set is weakest and where practitioner evidence would change the most.

### 7.2 Why the Risk tension (§6.1) cannot be resolved from evidence

RM §8 (Risk) has **zero external citations**. The claim that risk is first-class with horizon,
trend and severity rests entirely on Business Logic V1's assertion. There is no independent
material against which to adjudicate Condition versus Epistemic Stance. §6.1 is therefore a
judgement call for the Project Lead or a practitioner, not a question further evidence review
can settle.

**What step 2 inherits:** eight classification axes. Cognition derives principally from Epistemic
Stance (P3); Constraints from Norm (P6); Entities from Identity (P5); States from Condition (P1);
Events from Occurrence (P7); Relationships from Relation (P8); Facets from Condition and Context.

**What step 2 cannot yet populate:** the entities of the giving side, which remain undescribed.
The primitive set survives them; the Entities layer will not be complete without them.
