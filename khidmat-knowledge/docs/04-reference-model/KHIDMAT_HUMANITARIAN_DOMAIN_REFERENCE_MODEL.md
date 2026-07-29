# Khidmat Humanitarian Domain Reference Model

**The definitive conceptual reference for Khidmat AI.**

Every future ontology, taxonomy, knowledge graph, AI agent, database, workflow, API, interface
and reasoning engine is to be derived from this document.

It answers one question:

> **What exists in humanitarian reality that Khidmat must understand in order to help people
> correctly?**

---

## 0. How to read this document

### 0.1 What this is not

This is not ontology engineering, software architecture, database design, or business process
modelling. It contains no entity definitions, no schemas, no cardinalities, no enumerated value
sets, no process specifications. Where it names something that exists, it is reporting a feature
of the world — not deciding how that feature will be represented.

### 0.2 The discipline that governs every line

**Reality is separated from software.** A malnourished child is malnourished whether or not any
system records it. The record is not the child.

**Reality is separated from process.** A household's shelter condition exists. "Verification" is
something humanitarian actors *do* to learn about it. §12 treats actions as a distinct kind of
thing for this reason.

**Reality is separated from implementation limits.** Business Logic V1 states that V1 *"can
record that assistance occurred but cannot yet measure whether it worked"* `[BL §13]`. That is a
fact about a build, not about the world. Outcomes exist and change regardless. **No V1 limitation
is permitted to shrink the description of reality in §§3–15.** Limits live in §16 and nowhere
else.

**Reality is separated from scope.** Donors exist in humanitarian reality; the Core Humanitarian
Standard says so explicitly `[EXT: Sphere/CHS via TD-01: BD-TD01-004]`. Whether Khidmat V1
builds donor-facing capability is a different question, answered in §16. **Reality-membership
does not imply scope-membership**, and confusing the two is the specific error that derailed the
previous foundation.

### 0.3 Citation key

Every substantive statement traces to one of:

| Tag | Source |
|---|---|
| `[BL §n]` | Khidmat Business Logic Blueprint V1 — used as *a source of knowledge*, not as this document's structure |
| `[CD: name]` | Client First Draft (`KHIDMAT_AI_BUSINESS_OVERVIEW.html`) |
| `[EXT: source via TD-0n]` | External humanitarian standard or literature, retrieved and recorded in `docs/01-evidence/`. The chain is shown so it can be audited. |
| `[OPEN]` | **Not supported by any available source.** Stated as a question, never answered by invention. |

**On external evidence.** Only sources actually retrieved into `docs/01-evidence/` are cited:
OCHA, UNHCR, IASC, ICRC, Sphere/CHS, IOM, WHO, and named peer-reviewed literature. The Sphere
Handbook's *minimum standards* were **not** retrieved — only its Core Humanitarian Standard
definitional page. Where those standards would settle a question, that is marked `[OPEN]` with
the source named as a next action rather than assumed.

**No source in this repository has been validated with a humanitarian practitioner.** Tier A
elicitation was never executed. This qualifies everything below and is restated in §16.5.

### 0.4 The twenty-year test

Every statement was checked against one question: *would this still be true if the technology,
the organisation, and the funding model all changed?* Statements that failed were moved to §16
or removed. This document describes the world; it does not describe Khidmat's first release.

---

## 1. Vision — why Khidmat exists

Humanitarian systems **store data but rarely understand it** `[CD: The Problem]`. Most
humanitarian software is built to register cases and track donations, not to understand the
people and circumstances behind them `[CD: The Problem]`. Four consequences follow, each named
by the Client Draft: duplicate registrations occur, verification quality varies, historical
context is lost, and long-term outcomes are hard to measure.

The diagnosis is explicit: *"The limitation is not simply software. It is the absence of a
structured understanding of humanitarian reality"* `[CD: The Problem]`.

Business Logic V1 states the same gap as a difference in the question asked. Most systems answer
*what did the person ask for?* Khidmat must answer `[BL §2]`:

> What does this person need? Why do they need it? What will happen if the need is unmet? Who
> else is affected? What support pathway exists? What future risks are developing?

**These six questions are the functional specification of this entire document.** Every section
below exists because one or more of them cannot be answered without it.

Khidmat is therefore **not a registration system** `[BL §1]`, not a software product, not a
chatbot, not a donation platform, and not an NGO CRM `[CD: What Khidmat AI Is]`. It is a
**Humanitarian Operating System** `[BL §1]` — a structured understanding of humanitarian reality,
from which help can be reasoned about rather than merely recorded.

The long-term horizon is a **shared humanitarian intelligence foundation** serving organisations,
communities, researchers and future AI systems working from a common understanding of reality
`[CD: Closing]`.

---

## 2. Humanitarian reality — what is being modelled

### 2.1 Two kinds of real

Humanitarian reality contains two categories of thing, and conflating them is the most common
modelling failure in this domain.

**Reality that exists independently of humanitarian response.** People, families, households,
communities, geography, seasons, illness, poverty, displacement, capability, need, risk. These
exist whether or not any organisation is present, any system is deployed, or any help is offered.
A roof leaks in the absence of a shelter assessment. A child is malnourished whether or not
anyone measures them.

**Reality that exists because humanitarian response exists.** Registration, verification,
assessment, case plans, referrals, findings, programmes, deliveries. These are real events
performed by real people — but they exist *only because* a humanitarian system is operating on
the first category.

Sections 3–11 and 13–15 describe the first. **Section 12 describes the second, and is
deliberately quarantined there.** Building an ontology whose primary structure is the second
category produces a model of the organisation rather than a model of the people it serves — the
failure this project has already made once and reset to escape.

### 2.2 Reality is local

Humanitarian reality does not hold uniformly. A household means different things in different
cultures `[BL §8]`. A season turns a damaged roof into an emergency `[BL §8]`. What is true
within one context is not thereby true outside it.

This is not a caveat appended to the model. It is a structural property of the domain: **every
statement about humanitarian reality carries an implicit scope, and a statement whose scope is
unstated is a claim about all contexts** — usually a false one. The evidence base records this
as a standing limitation: no source retrieved in any dossier was specific to a deployment
geography `[TD-01: Open Gap 3]`.

### 2.3 Reality changes

Nothing in §§3–9 is static. People age through developmental stages `[BL §5.2]`. Needs open,
change severity, and resolve or expire `[BL §9]`. Risks have trends — worsening, stable,
improving `[BL §11]`. Households absorb shocks or fail to `[BL §7]`.

A model that captures a person as a point in time misdescribes them. The Client Draft names this
directly: most systems lose historical context `[CD: The Problem]`. **Time is not an attribute
added to this model; it is the medium the whole model exists in.**

---

## 3. Human reality

The foundation of everything else `[BL §5]`.

### 3.1 The person persists

A person is a **persistent entity, not a per-case record** `[BL §5.1]`. The same human being is
recognised across registrations, cases, organisations and years.

This single statement carries more weight than any other in this document. It is what makes it
possible to see that a household returning for the third time has not improved, or that a child
in school at first contact has dropped out by the second `[BL §5.1]`. Business Logic V1 states
that *"every downstream promise about longitudinal reasoning rests on this principle"*
`[BL §5.1]`. It is also the mechanism of fairness — the same person recognised as one person, so
support is neither duplicated nor lost `[BL §3.5]` — and the answer to the Client Draft's named
failures of duplicate registration and lost history `[CD: The Problem]`.

**`[OPEN]` — How sameness of person is established.** No source states how a person is
recognised as the same person across encounters, nor what happens when recognition is uncertain.
This is the single most consequential open question in this document, because three separate
principles rest on it. Biometric approaches exist in the sector; Business Logic V1 excludes them
from V1 `[BL §17]`, which is a scope decision and not an answer to the underlying question. See
§16.4.

### 3.2 Identity

Every person has identity: name, age, gender, marital status, documentation `[BL §5.2]`.

Documentation status is itself a humanitarian condition, not merely an administrative fact —
undocumented people face barriers to assistance, employment and services. `[OPEN]` — no source
in this repository elaborates the consequences of undocumented status.

### 3.3 Lifecycle stage

Every person occupies a developmental stage: infant, toddler, early childhood, school-age child,
adolescent, young adult, adult, older adult, elderly `[BL §5.2]`.

**A lifecycle stage is not an age band.** It is a *distinct developmental reality* carrying
characteristic dependencies, capabilities and vulnerabilities. Different stages create different
needs `[BL §5.2]`.

This matters because it means age is not a number to be filtered on but a claim about what a
person can do, what they require, and who they depend on.

**A person's developmental trajectory is distinct from their status in any programme.**
Graduation Approach practice — originated by BRAC, used at scale including by USAID's Bureau for
Humanitarian Assistance for displaced populations — tracks these as *"two separately tracked
concepts in mature practice, not one combined status field"*
`[EXT: BRAC/USAID Graduation literature via TD-03: BD-TD03-004]`. Corroborates `[BL §14]`.

### 3.4 Capabilities — what a person can do

Humanitarian understanding that records only deficits is incomplete. Every person has
capabilities `[BL §5.3]`:

- **Physical** — walk, travel, work physically
- **Cognitive** — learn, understand, make decisions
- **Educational** — read, write, study
- **Economic** — earn, manage money, run a business
- **Caregiving** — care for children, elderly, or disabled dependents

Capability is not the inverse of need. A person may have severe need and substantial capability
simultaneously, and the combination determines what help is appropriate — the difference between
relief and a pathway out. See §9.

### 3.5 Health and bodily condition

Five dimensions `[BL §5.4]`:

- **Acute conditions** — accident, surgery, injury
- **Chronic conditions** — diabetes, kidney disease, hypertension
- **Disabilities** — visual, hearing, mobility impairment
- **Mental health** — depression, anxiety, trauma
- **Nutritional conditions** — malnutrition, stunting, wasting, including clinical staging such
  as SAM/MAM

### 3.6 Wellbeing

Wellbeing is the state the whole system exists to improve `[BL §13]`, `[CD: Beyond Donations]`.
A need is defined as a gap against *a basic standard of wellbeing* `[BL §9]`.

**`[OPEN]` — What the basic standard of wellbeing is.** Neither source defines it. The Sphere
Handbook's minimum humanitarian standards are the sector's canonical statement of this and are
the obvious source; **they were not retrieved** into this repository — only Sphere's Core
Humanitarian Standard definitional page was `[TD-01 collection log]`. Retrieving them is a named
next action, not an answered question. Until then, "basic standard of wellbeing" is a placeholder
carrying real weight.

### 3.7 Dignity

Dignity is not a measurable condition alongside health and capability. It is a **standing
constraint on how every other part of this model may be used**.

Khidmat collects deep information about vulnerable people including children, the ill, and
survivors of violence. Data is collected with consent, kept to what is necessary, and handled so
that **the act of seeking help never exposes a person to further harm** `[BL §3.2]`. Safety
concerns — safeguarding, domestic violence, minors without guardians — take precedence over
process `[BL §3.2]`. The Client Draft states it as *"dignity at the center — every decision keeps
the person first"* `[CD: Core Philosophy]`.

Consent in humanitarian settings is genuinely difficult, and the sector has a considered
position: genuine informed consent is *frequently infeasible* in emergencies for reasons of
vulnerability, security and logistics. The ICRC *Handbook on Data Protection in Humanitarian
Action* resolves this through a **bounded necessity exception** rather than abandoning consent or
blocking action, and warns explicitly against consent becoming a box-ticking exercise
`[EXT: ICRC via TD-02: BD-TD02-004]`.

**A person is not their record, and understanding a person deeply is a responsibility before it
is a capability.**

---

## 4. Social reality

People do not exist alone, and modelling them alone misdescribes them.

### 4.1 Family

*"A family is not just a list of people"* `[BL §6]`. Three dimensions:

- **Relationships** — parent, child, guardian, caregiver, spouse `[BL §6]`
- **Dependency** — who depends on whom. *Father earns → mother depends financially → children
  depend financially* `[BL §6]`
- **Responsibility** — who is responsible for income, caregiving, education, decision-making
  `[BL §6]`

**Vulnerability cascades along dependency.** A vulnerability in one member propagates to those
who depend on them: *a mother's risk is her infant's risk* `[BL §6]`. This is a structural
feature of social reality, not an inference rule — it is why a person cannot be assessed in
isolation from those who depend on them.

### 4.2 Household

*"A household is a living unit"* `[BL §7]`:

- **Housing** — ownership, rental, temporary shelter
- **Utilities** — water, electricity, sanitation
- **Shelter condition** — safe, damaged, flood-prone, roof leakage
- **Household resilience** — composite capacity to absorb, adapt to and recover from shocks:
  buffering capacity, role substitution, caregiving and decision continuity, recovery resources

**Two households with the same need are not equally vulnerable if one can absorb the shock and
the other cannot** `[BL §7]`. Resilience is therefore not a summary of need; it is an independent
property that changes what a given need means.

### 4.3 Family and household are not the same thing

Business Logic V1 models them in separate sections with different content `[BL §6, §7]` — family
is a structure of relationship and obligation; household is a unit of shared living.

**`[OPEN]` — How family and household membership are determined, and what happens when they
diverge.** They routinely diverge under displacement, polygamy, fostering, labour migration and
multi-generational co-residence. No source in this repository addresses membership determination,
the relationship between the two, or divergence. Business Logic V1 acknowledges that the meaning
of household varies culturally `[BL §8]` without stating how that variation is handled.

### 4.4 Community

The household is understood in its context, not in isolation `[BL §8]`:

- **Community context** — village, neighbourhood, district; settlement type and accessibility
- **Available services** — schools, hospitals, markets, employment opportunities, **and the
  distance and quality of access to them**
- **Local fabric** — local organisations, livelihood patterns, community assets, social capital
- **Seasonal and environmental risk** — see §5

Access is not binary. A hospital that exists but cannot be reached is, for the household in
question, closer to absent than present — which is why `[BL §8]` names distance and quality of
access rather than mere presence.

### 4.5 Community as actor, not only as context

Communities are not passive settings. *"Emergent groups," "spontaneous volunteers"* and *"mutual
aid/self-help groups"* are documented as a real, independent and **frequently first-responding**
category of humanitarian actor, with proximity, speed and local-trust advantages over formal
organisations. The literature argues explicitly that they should be recognised as legitimate
actors in their own right, *"not merely absorbed or supplanted by formal actors"*
`[EXT: Twigg & Mosel (Disasters, 2017), COVID-19 mutual-aid studies, Sudan localisation study,
via TD-01: BD-TD01-005]` — High confidence, ≥3 independent source families spanning pandemic,
conflict and urban disaster response.

Neither authoritative source contains this. It is recorded here as reality established by
external evidence. See §11.

---

## 5. Environmental reality

The physical and economic world a household lives in, which changes what any given condition
means.

### 5.1 Geography, settlement and infrastructure

Settlement type and accessibility `[BL §8]`; utilities — water, electricity, sanitation — at
household level `[BL §7]`; services and the distance and quality of access to them `[BL §8]`.

### 5.2 Seasonality and hazard

Flooding, rainy season, heat waves, drought, and **the seasonal calendar** `[BL §8]`.

Business Logic V1 states the consequence exactly: the seasonal calendar *"turns a damaged roof in
a flood zone before monsoon into a preventive emergency rather than a routine repair"* `[BL §8]`.

**This is one of the most important sentences in either source.** It establishes that the
severity of a condition is not a property of the condition alone — it is a function of the
condition, its environmental context, and time. The same damaged roof is a routine repair in one
month and an emergency in another. Any model that assigns severity to a condition in isolation
will be wrong for reasons it cannot detect.

### 5.3 Economy and livelihood context

Livelihood patterns, markets, employment opportunities, community assets `[BL §8]`.

Economic context determines whether a given form of help is even possible. Modality selection —
cash versus in-kind — is decided on **local market feasibility** and household appropriateness
`[EXT: IASC coordination guidance and CVA feasibility literature via TD-06: BD-TD06-002]`. A cash
transfer where no market functions is not help.

### 5.4 Disaster and crisis

`[BL §11]` names roof collapse during rainy season as a future risk; `[BL §8]` names flooding,
heat waves and drought.

**`[OPEN]` — Crisis typology and phase.** Neither source characterises crises as entities with
onset, phase and duration. External evidence establishes that a **Temporal/Objective Phase**
dimension exists and is universally recognised — Emergency Relief, Rehabilitation, Development
`[EXT: IASC, Triple Nexus frameworks via TD-06: BD-TD06-001]`. Whether Khidmat models crises
themselves, or only their effects on households, is unresolved.

---

## 6. Humanitarian situations

A **situation** is a circumstance of a person, family or household that changes wellbeing and
therefore generates needs and risks. Situations are not needs; they are the circumstances from
which needs arise.

### 6.1 Situations named by the authoritative sources

| Situation | Source |
|---|---|
| Illness — acute, chronic | `[BL §5.4]` |
| Disability — visual, hearing, mobility | `[BL §5.4]` |
| Malnutrition, stunting, wasting (incl. SAM/MAM) | `[BL §5.4]` |
| Mental-health conditions, trauma | `[BL §5.4]` |
| Widowhood | `[BL §9]` protection; `[BL §11]` compound risk |
| Children without adequate protection; minors without guardians | `[BL §3.2, §9]` |
| Domestic violence, and its aftermath | `[BL §3.2, §9]` |
| Loss of income; unemployment | `[BL §11, §9]` |
| Elderly people without support | `[BL §9, §10]` |
| Housing insecurity — damaged, flood-prone, temporary shelter | `[BL §7]` |
| Food insecurity | `[BL §9]` |
| Education interruption — including re-enrolment need | `[BL §9]` |
| Caregiver burden | `[BL §9]` |
| Grief; chronic stress | `[BL §9]` |
| Environmental hazard exposure | `[BL §8]` |

### 6.2 Situations supported by external evidence but absent from both sources

**Displacement.** Not named anywhere in Business Logic V1 or the Client First Draft. It is
central to the humanitarian sector — UNHCR exists for it, and the evidence base includes
displaced-population programming literature `[EXT: PMC systematic review on displaced populations
via TD-03: BD-TD03-004]`. Recorded here as **reality that both authoritative sources omit.**

**Poverty as a structural condition**, distinct from any acute episode. Business Logic V1 treats
economic circumstance through capability `[BL §5.3]` and livelihood need `[BL §9]` but does not
name chronic poverty as a situation in its own right. Graduation Approach literature treats a
household's poverty trajectory as a first-class tracked concept
`[EXT: via TD-03: BD-TD03-004]`.

### 6.3 Situations requested but not evidenced

**Orphanhood.** Named in the project direction. Business Logic V1 names *child protection* and
*minors without guardians* `[BL §3.2, §9]`, which overlap but are not identical — a child may be
orphaned yet well-guardianed, or unguardianed yet not orphaned. `[OPEN]` — no source distinguishes
them.

### 6.4 The open-endedness problem

The instruction is that a situation can be *anything* that changes human wellbeing, and that any
case type can exist.

**`[OPEN]` — Whether the set of situations is open or closed.** This is a genuine and consequential
modelling question that no source answers. Business Logic V1's seven need categories `[BL §9]` are
presented as a closed list. If situations are open-ended but needs are closed, then an
unanticipated situation must still resolve into one of seven need categories — which may be
correct, or may be a silent truncation of reality.

**This must be decided deliberately, because it determines whether a situation nobody
anticipated is representable at all.** It is recorded here as a question, not resolved.

---

## 7. Needs

### 7.1 What a need is

**A need is a gap between current state and a basic standard of wellbeing** `[BL §9]`.

This definition is doing real work: a need is *relational*, not absolute. It exists between where
someone is and where they ought to be. It follows that the same condition constitutes a need in
one context and not another, and that the standard — §3.6, currently `[OPEN]` — is load-bearing.

### 7.2 How needs are known

Khidmat must identify needs that are `[BL §1]`:

- **explicitly requested** — the person asks
- **implied** — inferable from what is known and stated
- **emerging** — developing but not yet acute

and, as long-term horizon, needs **likely to occur in the future, before the beneficiary has to
ask** `[BL §1]`.

**Business Logic V1 immediately qualifies the fourth.** V1 delivers structured understanding and
*reactive* inference — it reasons from what is known and stated. Forward prediction before any
signal exists is the roadmap end-state, not a V1 capability: *"V1 must not be read as promising a
prediction engine"* `[BL §1]`.

**The distinction being drawn is about implementation, not reality.** Emerging needs genuinely
emerge in the world before anyone asks about them. That is a fact about humanitarian reality and
belongs in this document. Whether Khidmat can detect them is a §16 question.

### 7.3 Need categories

Seven `[BL §9]`:

| Category | Content |
|---|---|
| **Food** | daily food, nutrition, infant feeding, therapeutic nutrition |
| **Health** | treatment, surgery, medication, rehabilitation, assistive devices, diagnosis |
| **Education** | school fees, supplies, transport, re-enrolment |
| **Housing** | roof repair, shelter repair, rent support, emergency housing |
| **Livelihood** | income support, employment, skills development, tools and equipment |
| **Psychosocial** | grief, trauma, chronic stress, caregiver burden, domestic-violence aftermath |
| **Protection** | widow support, child protection, elder care, safeguarding of people at risk of harm |

Clothing, named in the project direction, is a **material modality** against a housing or
protection need rather than a category of its own — see §13.2 on why this distinction matters.

### 7.4 Needs are dynamic

**Needs are not static.** A need opens, changes in severity, and resolves or expires as
circumstances change — *a job restored may close a food need while a new medical need opens*
`[BL §9]`. Needs are tracked across their lifetime, not as a single snapshot.

### 7.5 Needs interact

Business Logic V1 does not state a general theory of need interaction, but three interaction
patterns are evidenced:

- **Needs cascade through dependency.** A vulnerability in one family member creates need in
  those who depend on them `[BL §6]`.
- **Resolving one need can open another** `[BL §9]`.
- **One intervention can satisfy several needs at once.** The mapping between a delivered
  intervention and a need is **many-to-many**, not one-to-one — Multipurpose Cash is a single
  modality intended to cover food, shelter and WASH needs concurrently
  `[EXT: CVA standards and humanitarian policy literature via TD-06: BD-TD06-003]`.

**`[OPEN]` — A general model of how needs relate to one another** (prerequisite, aggravating,
substituting, mutually exclusive) is not stated by any source.

---

## 8. Risk

### 8.1 Risk is first-class

Risk is **a first-class concept with a horizon (how soon), a trend (worsening, stable, improving)
and a severity — not a byproduct of severity rules** `[BL §11]`.

This is a deliberate and unusual commitment. It means risk is not computed from need; it is its
own kind of thing, about what has not happened yet.

### 8.2 Kinds of risk

- **Current risk** — hunger, medical deterioration, school dropout `[BL §11]`
- **Future risk** — roof collapse during rainy season, loss of income after injury, child
  malnutrition `[BL §11]`
- **Compound risk** — *widow + no income + disabled child = complex humanitarian risk* `[BL §11]`
- **Long-term risk** — the trajectory across years that determines whether a household recovers
  or entrenches. Implied by `[BL §13]`'s reduced-dependency outcome and by
  `[CD: End-to-End Flow]`'s long-term independence endpoint.

### 8.3 Risk produces signals; it does not decide

*"The risk domain produces signals; it does not decide what to do about them"* `[BL §11]`.

A clean separation: identifying that a household is at risk is a different act from deciding what
to do about it, and the second is a human decision `[BL §3.3]`.

### 8.4 Vulnerability

Vulnerability is **not a single condition. It emerges from multiple compounding factors**
`[BL §10]`. The system reasons about how factors combine, not only about each factor alone.

> Infant + malnutrition + low-income household = high vulnerability
> Elderly person + lives alone + mobility impairment = high vulnerability `[BL §10]`

**`[OPEN]` — How vulnerability composes.** Business Logic V1 gives two illustrative sums and no
rule. Whether composition is additive, threshold-based, multiplicative, or qualitative is
unstated, and no external source retrieved addresses it. This is a genuine gap at the centre of
the model — the same gap applies to compound risk `[BL §11]`.

---

## 9. Capabilities, strengths and resources

A humanitarian model that sees only deficits will offer only relief.

### 9.1 What exists on the strength side

- **Individual capability** — physical, cognitive, educational, economic, caregiving `[BL §5.3]`
- **Household resilience** — buffering capacity, role substitution, caregiving and decision
  continuity, recovery resources `[BL §7]`
- **Community assets and social capital** — local organisations, livelihood patterns, community
  assets `[BL §8]`
- **Community response capacity** — emergent groups and mutual-aid structures as first responders
  `[EXT: via TD-01: BD-TD01-005]`
- **Opportunity in the environment** — markets, employment opportunities, services `[BL §8]`

### 9.2 Why this side of the model is not optional

Business Logic V1 frames capability explicitly as *"what a person can do, not only what they
lack"* `[BL §5.3]`. The Client Draft frames the goal as *"reducing dependency through sustainable
improvement"* and states that *"success is not measured by the amount of aid distributed"*
`[CD: Beyond Donations]`.

**Dependency reduction is only possible if capability is modelled.** A system that records only
need can allocate relief; it cannot identify that a young adult has economic capability, no
current livelihood, and an accessible market — the combination that makes a pathway out possible
rather than another distribution. This is the structural reason §9 exists as a peer of §7 and §8
rather than as an afterthought.

**Note on scope, not reality.** *Proactively identifying* capable people who have not asked for
help is exactly the forward-looking capability `[BL §1]` qualifies and `[BL §17]` excludes from
V1. **The capability and opportunity exist in reality regardless.** See §16.

---

## 10. Evidence and knowledge

Humanitarian reality includes not only how things are, but **what is known about how things are,
and how well it is known**. This is not a software concern. Two organisations looking at the same
household hold genuinely different states of knowledge about it.

### 10.1 Claims

Everything a person tells the system is a **claim, not a confirmed fact** `[BL §3.1]`. Claims
carry an explicit quality — how complete, how internally consistent `[BL §3.1]`.

*"A registration is merely a collection of claims"* until verification says otherwise `[BL §3.1]`.

**Who supplies a claim changes its weight.** The registrant's role and relationship determine how
much epistemic weight a claim carries `[BL §4]` — a beneficiary speaking for themselves, a family
member speaking for them, and a trained volunteer observing are not equivalent.

### 10.2 Evidence

Evidence is what grounds a claim in fact `[CD: Foundational Understanding]`. The Client Draft
treats **Evidence** and **Verification** as dimensions of humanitarian reality in their own right,
alongside Individuals and Communities `[CD: What Khidmat AI Seeks to Understand]`.

**`[OPEN]` — The kinds of evidence and their relative weight.** Neither source enumerates evidence
types (document, observation, testimony, community attestation, measurement) or states how they
compare.

### 10.3 Findings

Verification converts claims into **findings** `[BL §3.1, §14]`.

This transformation is externally corroborated as real practice, not a design invention. The
speed-versus-verification conflict is documented sector-wide, and the literature resolves it
through *accelerated-but-present* verification controls — minimum checks, community validation —
rather than a binary choice; the claim/finding split is *"a documented real-world response pattern
to this tension, not an arbitrary design choice"*
`[EXT: humanitarian critical-review literature via TD-02: BD-TD02-002]`.

### 10.4 Confidence

Assessed needs carry an explicit **confidence** `[BL §3.1]`. The system reasons openly with
uncertainty rather than pretending to certainty it has not earned `[BL §3.1]`. AI must stay
*"transparent about confidence, uncertainty, and what still needs verifying"*
`[CD: The AI Intelligence Layer]`.

### 10.5 Uncertainty, contradiction and absence

Three further states, each of which is knowledge:

- **Uncertainty** — a conclusion held provisionally `[BL §3.1]`
- **Contradiction** — two claims that cannot both be true. `[OPEN]` — no source states how
  contradictions between claims are represented or handled.
- **Missing information** — a gap in understanding is itself a thing to be known. Implied by
  `[BL §3.1]`'s requirement to reason openly with uncertainty; **not explicitly modelled by
  either source.** `[OPEN]`

### 10.6 Why this section is not a software concern

The temptation is to treat claim-status and confidence as metadata on records. They are not.
**They are facts about the relationship between the world and what anyone knows of it**, and they
exist whether that relationship is recorded in a database, a paper file, or a case worker's
memory.

This is also what makes human oversight enforceable: consequential decisions — eligibility,
escalation, exit — remain human decisions with a human accountable `[BL §3.3]`, and that rule can
only be applied if the system can represent *how well* something is known.

---

## 11. Humanitarian actors

Following the instruction, three categories are distinguished explicitly.

### 11.1 Actors that exist in humanitarian reality

| Actor | Basis |
|---|---|
| **Person / beneficiary** | `[BL §4]` — persists across cases and time |
| **Family and household** | `[BL §6, §7]` |
| **Community** | `[BL §8]`; as actor `[EXT: via TD-01: BD-TD01-005]` |
| **Emergent groups, spontaneous volunteers, mutual-aid structures** | `[EXT: Twigg & Mosel; COVID mutual-aid; Sudan localisation, via TD-01: BD-TD01-005]` — frequently first-responding |
| **Volunteer** | `[BL §4]` |
| **Field verifier** | `[BL §4]` |
| **Human reviewer** | `[BL §4]` |
| **Case manager** | `[BL §4]` |
| **Organisation** (NGO, INGO, community organisation) | `[BL §4]`; `[EXT: OCHA, UNHCR, IASC via TD-01: BD-TD01-001/003]` |
| **Programme** | `[BL §4]`; distinct from organisation — see below |
| **Donor** | `[EXT: Sphere/CHS via TD-01: BD-TD01-004]` — the Core Humanitarian Standard **explicitly defines** humanitarian actors to include those providing financial, material or technical support without directly delivering assistance |
| **Host government** | `[EXT: WHO EMRO actor guide, Sphere/CHS via TD-01: BD-TD01-001]` — bearing primary responsibility for protecting its population |
| **UN agencies and coordination bodies** | `[EXT: OCHA, UNHCR, IASC via TD-01: BD-TD01-002]` |
| **Healthcare provider, school, employer, market** | `[BL §8]` — as services and opportunities; **not modelled as actors by either source.** `[OPEN]` |

**Programme and Organisation are probably distinct.** Business Logic V1 collapses them into a
single actor row `[BL §4]`. Every external source retrieved names implementing organisations
separately from the programmes and clusters they lead, and none describes them as the same kind of
thing `[EXT: IASC/UNHCR/OCHA via TD-01: BD-TD01-003]`. **Recorded as evidence favouring
separation; the decision is not made here.**

### 11.2 Actors Khidmat V1 interacts with

Business Logic V1's operational set `[BL §4]`: Beneficiary/Subject · Registrant (beneficiary,
proxy, or volunteer) · Volunteer · Field Verifier · Human Reviewer · Case Manager ·
Programme/Organisation.

**Warning, recorded because it matters more than it appears.** These specific operational roles
have **zero external validation**. TD-01 searched for them specifically and found that sector
standards *"operate at the organizational/coordination level, not this granularity"*
`[TD-01: Open Gap 1]`. They are currently supported by nothing outside this project, and closing
that gap *"most plausibly requires Tier A evidence specifically, not further literature search."*

This is not evidence the roles are wrong. It is a precise statement of what is not yet known
about them — and they sit at the centre of the epistemic-weight rule of §10.1.

### 11.3 Actors outside first implementation scope

**Donors and the resource-supply side** are excluded from Khidmat V1 `[BL §4, §17]`.

**This is a scope decision, not a claim about reality.** Donors are actors — the Core Humanitarian
Standard says so `[EXT: via TD-01: BD-TD01-004]`. Business Logic V1's exclusion reads as a
delivery-scope decision, not a denial that donors exist. See §16.

**Government, healthcare providers, schools and employers** appear in both sources only as
*services* and *opportunities* in the community `[BL §8]`, `[CD: Beyond Donations]` — never as
actors with their own interests and behaviours. `[OPEN]` — whether they are modelled as actors is
undecided.

### 11.4 Actors operate at different altitudes

The strongest structural finding in the evidence base, appearing **five times across five
independent dossiers**: humanitarian reality runs two distinct rhythms concurrently.

- A **programme/coordination altitude** — the IASC Humanitarian Programme Cycle, on an annual or
  crisis-length cadence, which *"is not a description of what happens to one specific person"*
  `[EXT: IASC/UNHCR/IOM/WHO via TD-03: BD-TD03-001]`
- A **case/individual altitude** — event-driven, governing how one person's situation unfolds

The same word means different things at each. *"Needs assessment," "coordination"* and *"planning"*
exist as named capabilities at both altitudes and are **genuinely different activities that share
a label** `[EXT: OCHA, fscluster via TD-04: BD-TD04-003]`. Value streams split along the same axis
`[EXT: via TD-05: BD-TD05-002]`, as does intervention categorisation — Sector set at programme
altitude, Modality at case altitude `[EXT: via TD-06: BD-TD06-002]`.

**Both authoritative sources describe only the case altitude.** This is the largest structural
gap between the sources and evidenced reality, and any term shared across altitudes must be
altitude-qualified or it will silently conflate two things.

**A third altitude is implied but unevidenced.** `[OPEN]` — givers (donors, adopters,
institutional funders) sit outside both altitudes yet constrain both, since funding restrictions
determine who may receive what. No source in this repository models this.

### 11.5 Tensions between actors are structural

Three documented tensions, none of which is a malfunction to be fixed:

- **Donor accountability versus affected-population accountability** pull in different directions,
  attributed to unequal power relations `[EXT: Emerald, ODI HPN, Disasters (2025), IOM, via
  TD-02: BD-TD02-001]` — High confidence, ≥4 source families
- **Donor-driven standardisation versus locally-led legitimacy** — local actors are simultaneously
  required to meet donor standards and to leverage the informal legitimacy those standards
  undermine `[EXT: CSIS, ODI HPN, ScienceDirect Syria case study, via TD-02: BD-TD02-003]`
- **Speed versus verification** — managed, not resolved `[EXT: via TD-02: BD-TD02-002]`

Business Logic V1 states the corresponding principle: accountability runs **in both directions**,
and the system is accountable *to the people it serves*, not only to the organisation `[BL §3.4]`.

---

## 12. Humanitarian actions

**These are activities that operate on reality. They are not reality in the sense of §§3–9.**

They are real — a verification visit genuinely happens — but they exist only because humanitarian
response exists. §2.1 draws this line; this section is where it is enforced.

**Why the quarantine matters.** The previous foundation organised its entire discovery around
these activities. The result, in that work's own words, was that *"Registration & Identity holds a
registry record; Case Management holds a workflow record. Neither holds a person."* Actions must
appear in the model — they are how understanding is acquired — but they must never be its
organising axis.

### 12.1 The actions

| Action | What it does to reality | Source |
|---|---|---|
| **Registration** | Makes a person and their situation known; produces claims | `[BL §14]`, `[CD: Flow]` |
| **Evidence collection** | Gathers what grounds claims | `[CD: Flow]` |
| **Verification** | Converts claims into findings | `[BL §3.1, §14]` |
| **Assessment** | Converts claims and findings into identified needs, with confidence | `[BL §14]` |
| **Planning** | Determines what support is appropriate | `[BL §14]` |
| **Referral** | Moves responsibility to another actor or organisation | `[BL §14]` |
| **Delivery** | Provides the support | `[BL §14]` |
| **Monitoring** | Observes what happens after | `[BL §14]`, `[CD: Flow]` |
| **Follow-up** | Re-contacts; may trigger re-verification | `[BL §14]` |
| **Re-verification** | Re-establishes findings as circumstances change | `[BL §14]` |
| **Outcome measurement** | Determines whether wellbeing improved | `[BL §14]` |

### 12.2 Eligibility is a human decision

Eligibility is realised as a verification outcome **plus** an approved case plan. A case
progresses to active standing only after verification clears it and a plan is approved. **It is
not an automatic status flip** `[BL §14]`.

### 12.3 A handoff is where ownership changes

Business services are the tangible outputs of capabilities — a verified claim, an assessed need,
an approved support plan — and a value stream is built by **chaining the outputs of discrete
capabilities, not by merging the capabilities** `[EXT: HVSM methodology via TD-05: BD-TD05-003]`.
The handoff point is where ownership and accountability change hands.

### 12.4 Actions do not run in a straight line

Sector-standard case management describes its stage cycle explicitly as *"a loop rather than a
straight line — monitoring routinely sends a case back into reassessment"*
`[EXT: interagency GBV and Child Protection Case Management Guidelines, via TD-03: BD-TD03-002]` —
High confidence, ≥4 independent source families. Corroborates `[BL §14]` and
`[CD: End-to-End Flow]`, which both state non-linearity independently.

### 12.5 Where the sector stops and Business Logic V1 continues

Interagency case-management stage sets **end at closure**. Business Logic V1 continues past the
equivalent point into Outcome Measurement, Impact Measurement and Knowledge Graph Learning as
further stages of the *same* lifecycle `[BL §14]`. Sector practice treats *"did the case close"*
and *"did it work"* as related but organisationally distinct — a separate function, on a different
cadence, sometimes a different team `[EXT: via TD-03: BD-TD03-003]`. MEAL is documented as a
**named, bundled, semi-independent capability** operating across whatever it observes, *"not as
the final stage of any one case's journey"* `[EXT: ≥4 institutional sources via TD-04:
BD-TD04-001]`.

**`[OPEN]` — Whether outcome, impact and learning belong inside the case journey or to a separate
discipline that consumes it.** Evidence leans toward separation; it does not settle it. This is
the most consequential unresolved question in this document after §3.1 identity.

### 12.6 Accountability action

**Complaints and Feedback Mechanisms are a distinct, named, standing capability, structurally
separate from case management**, connected by explicit referral pathways — *"two different systems
that hand off to each other, not one system"* `[EXT: IOM, UNHCR, CARE, DRC, NRC, via TD-04:
BD-TD04-002]`, five independent institutional sources.

This is the mechanism by which `[BL §3.4]`'s requirement is met: a beneficiary must be able to
question, correct or complain about a decision, and that feedback must be able to **reopen the
relevant part of the journey** `[BL §3.4]`.

---

## 13. Support

### 13.1 Support pathways

Five, by the form help takes `[BL §12]`: **financial** (cash, grants) · **material** (food,
shelter materials) · **medical** (treatment support, medication) · **educational** (scholarships,
school support) · **livelihood** (skills training, employment linkage).

The Client Draft states the breadth more widely: donations are only one possible form of help, and
the range includes *employment, education, healthcare, government schemes, business support, skills
development, and emergency relief* `[CD: Beyond Donations]`.

### 13.2 Support is categorised on three independent dimensions

The two lists above were never in conflict — they are **different dimensions of the same thing**.

Humanitarian interventions are categorised along three fundamentally distinct, universally
recognised dimensions `[EXT: IASC clusters, CVA standards, Triple Nexus frameworks, via TD-06:
BD-TD06-001]` — High confidence:

| Dimension | Question it answers | Examples |
|---|---|---|
| **Sector / Domain** | *What need is addressed?* | Health, Shelter, Education, Food, Protection |
| **Modality** | *How is it delivered?* | Cash, In-kind, Service, Voucher |
| **Temporal / Objective Phase** | *Why and when?* | Emergency Relief, Rehabilitation, Development |

An intervention exists at the **intersection** — an Emergency [phase] In-kind [modality] Shelter
[sector] intervention.

The evidence names the error in Business Logic V1's list precisely: it *"mixes modalities
('Financial', 'Material') with sectors ('Medical', 'Educational') in a single list"*
`[EXT: via TD-06: BD-TD06-001]`. **Clothing** — named in the project direction — resolves cleanly
here as an in-kind modality against a housing or protection sector need, which is why it needs no
category of its own.

### 13.3 The catalogue is not part of this model

The three dimensions are **stable, enduring business concepts**. The specific items delivered —
*"jerry cans," "school fees," "hygiene kits"* — are operational implementations that vary
significantly by region, organisation and emergency type, and are *"inherently volatile and
context-dependent"* `[EXT: via TD-06: BD-TD06-004]`.

Business Logic V1 says the same: the concrete intervention catalogue is *"defined operationally
with programme staff"* and is blocked on input that does not yet exist `[BL §12, §16]`.

**Therefore the catalogue is not missing from this document. It is correctly absent** — it does
not belong at this layer. Enumerating it here is precisely the error the previous foundation made.

### 13.4 Sources of support beyond the organisation

`[CD: Beyond Donations]` names **government schemes** among the range of help. Business Logic V1
has no counterpart. Government bears primary responsibility for protecting its population
`[EXT: WHO EMRO, Sphere/CHS via TD-01: BD-TD01-001]`.

**`[OPEN]` — Whether state provision, community support and informal giving are modelled as
support pathways alongside organisational assistance.** Community mutual aid is documented as real
and frequently first `[EXT: via TD-01: BD-TD01-005]`; Islamic charitable giving is documented as
operating in both formal/institutional ("vertical") and informal/community ("horizontal") forms
`[EXT: Springer Nature (2020), ReliefWeb, via TD-01: BD-TD01-006]`. Neither authoritative source
models any of these as a support pathway.

---

## 14. The humanitarian journey

**This is not a workflow. It is the evolution of humanitarian reality over time.**

The distinction is exact: §12 lists what humanitarian actors *do*. This section describes what
*happens to a person* — which continues whether or not anyone is acting.

```
Human exists
   ↓          a person, in a family, in a household, in a community      §§3–5
Situation changes
   ↓          illness, loss, displacement, disaster, season turning      §§5–6
Need emerges
   ↓          a gap opens between current state and basic wellbeing      §7
Need communicated
   ↓          requested, implied, or observed — or not communicated      §7.2
Understanding
   ↓          claims gathered, context assembled                        §10
Verification
   ↓          claims become findings                                     §10.3
Assessment
   ↓          findings become identified needs, with confidence          §10.4
Planning
   ↓          appropriate support determined; a human decides            §12.2
Support
   ↓          pathway selected across sector, modality, phase            §13
Delivery
   ↓          support reaches the person                                 §12
Follow-up
   ↓          circumstances re-examined; may reopen anything above       §12.4
Outcome
   ↓          wellbeing improved, held, or deteriorated                  §15
Recovery
   ↓          the situation that generated the need resolves             §15
Resilience
   ↓          capacity to absorb the next shock without falling again    §4.2
Long-term wellbeing
              sustained independence, or continued dependency            §15
```

### 14.1 Four properties of the journey

**It is not linear.** People revisit earlier stages, needs evolve, assessments change, and
*"recovery does not always move in a straight line"* `[CD: End-to-End Flow]`. New information — a
changed circumstance, a grievance, a re-verification trigger — sends the situation back to an
earlier point `[BL §14]`. Externally corroborated as standard practice, not exception handling
`[EXT: via TD-03: BD-TD03-002]`.

**It does not require the system.** A person's situation changes, a need emerges, and it may
resolve, persist, or worsen without any humanitarian actor ever knowing. **The journey is the
person's, not the organisation's.** This is why it is described here rather than in §12.

**A person may be at many points at once.** Needs are dynamic and independent — a job restored may
close a food need while a new medical need opens `[BL §9]`. A household can be in recovery on one
need and acute crisis on another. **The journey is not a single position.**

**It can end without recovery.** Nothing guarantees that needs are met or that wellbeing improves.
A model that treats the endpoint as inevitable will misdescribe every case that does not reach it.

### 14.2 Engagement is tracked separately from what happens

Business Logic V1 tracks macro-state as engagement stages — identified, registration_initiated,
registered, verification_pending, active, engaged, monitored, suspended, review_required, exited —
**decoupled from how any specific aid is delivered** `[BL §14]`.

Corroborated by mature practice: Graduation Approach programming tracks a household's underlying
trajectory separately from its status in any specific programme, as *"two separately tracked
concepts… not one combined status field"* `[EXT: BRAC/USAID via TD-03: BD-TD03-004]`.

**Where a person is in their life is not where they are in your process.** Conflating them is a
documented failure mode, and the two must never collapse into one status.

---

## 15. Outcomes

### 15.1 What success means

**The goal is not case closure. The goal is improved human wellbeing** `[BL §13]`.

The Client Draft states it independently and more sharply: *"Success is not measured by the amount
of aid distributed. Success is measured by sustainable improvement in human well-being"*
`[CD: Beyond Donations]`, with the aim of *"reducing dependency through sustainable improvement."*

**Both authoritative sources agree on this without qualification.** It is the strongest agreement
between them and the definition of success for the whole project.

### 15.2 Levels of outcome

| Level | Content | Source |
|---|---|---|
| **Individual wellbeing** | Health recovery and stability; continued schooling; sustainable income | `[BL §13]` |
| **Family wellbeing** | Reduced dependency | `[BL §13]` |
| **Household resilience** | Restored capacity to absorb, adapt and recover | `[BL §7]` |
| **Community resilience** | Local capacity, assets, social capital | `[BL §8]` — as context; **as outcome, `[OPEN]`** |
| **Independence** | Long-term independence as journey endpoint | `[CD: End-to-End Flow]` |
| **Sustainable livelihood** | Employment, skills, business capacity | `[BL §12]`, `[CD: Beyond Donations]` |
| **Recovery** | The generating situation resolves | `[CD: End-to-End Flow]` |
| **Development** | Movement beyond relief toward durable improvement | `[EXT: Triple Nexus phase dimension via TD-06: BD-TD06-001]` |

### 15.3 Outcomes can be negative

A situation can improve, hold, or **deteriorate**. Business Logic V1 frames outcome measurement as
determining *"whether a situation improved, held, or deteriorated"* `[BL §13]`.

A model that represents only successful outcomes cannot learn, and cannot detect that a household
returning for the third time has not improved `[BL §5.1]`.

### 15.4 The measurement gap is an implementation fact, not a reality fact

Business Logic V1 records that the outcome-indicator vocabulary does not exist and that V1 *"can
record that assistance occurred but cannot yet measure whether it worked"* `[BL §13, §16]`.

**Outcomes exist and change regardless.** The gap belongs to §16.

**`[OPEN]` — What indicates each outcome.** No source supplies an indicator vocabulary. Sphere's
minimum standards are the obvious sector reference and were not retrieved (§0.3).

---

## 16. Scope — four concentric layers

The single most important structural section of this document. Confusing these four layers is
what caused the previous foundation's failure, and keeping them apart is what keeps this one
honest.

```
┌─────────────────────────────────────────────────────────────┐
│ 16.1  HUMANITARIAN REALITY                                  │
│       Everything that exists, whether Khidmat models it      │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ 16.2  ONTOLOGY SCOPE                                   │ │
│  │       What Khidmat's ontology represents                │ │
│  │  ┌───────────────────────────────────────────────────┐ │ │
│  │  │ 16.3  V1 IMPLEMENTATION SCOPE                     │ │ │
│  │  │       What the first build delivers                │ │ │
│  │  └───────────────────────────────────────────────────┘ │ │
│  │        16.4  ROADMAP — modelled, built later           │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 16.1 Humanitarian reality

Everything in §§3–15. It includes things Khidmat will never build: donors and giving
`[EXT: Sphere/CHS via TD-01: BD-TD01-004]`, government responsibility
`[EXT: via TD-01: BD-TD01-001]`, informal mutual aid `[EXT: via TD-01: BD-TD01-005]`,
programme-altitude coordination `[EXT: via TD-03: BD-TD03-001]`, crisis phase
`[EXT: via TD-06: BD-TD06-001]`.

**Reality is not narrowed by scope.** Whatever Khidmat builds, these exist.

### 16.2 Ontology scope

What the Khidmat ontology represents. **This document is the candidate boundary.** Deciding
which of §§3–15 falls inside it is the **first act of ontology design**, performed as ontology
work — not as a further narrative document.

The governing rule, established by evidence and now settled: **reality-membership does not imply
scope-membership, and scope-exclusion does not imply unreality.** Donors are actors in reality and
outside V1 delivery; both statements are true and neither cancels the other.

The correct test for ontology scope is not *"is it real?"* — everything in §§3–15 is real. It is
*"must Khidmat understand this to help people correctly?"*

### 16.3 Khidmat V1 implementation scope

Business Logic V1 §16 records what V1 specifies: Human Model · Family and Household · household
resilience · Community context · Needs and confidence-weighted assessment · Vulnerability and Risk
· Verification · Case orchestration · engagement macro-state · claim epistemics and temporal
reasoning.

> **Two claims in the source are void, and must not be inherited.**
>
> BL V1 titles the list above *"Delivered today (built in the repository)"*, and its header
> delegates the authoritative definition of every concept it names to directories — `shared/`,
> `registration/`, `verification-operations/`, `needs-assessment/`, `case-management/`,
> `beneficiary-lifecycle/`, `community-context/` — plus a `knowledge_layer_roadmap.md`.
>
> **None of these exist in this repository and none ever did.** They refer to an earlier
> codebase outside this project. **Nothing is built, and no concept definition lives anywhere
> but here.**
>
> The list is therefore read as *specified*, never as *delivered*. This is the one place where
> this document knowingly weakens a statement in an authoritative source; it is disclosed
> rather than silent, because a stale claim about a vanished codebase is not a fact about
> humanitarian reality and §0.2 forbids implementation state from entering §§3–15 in either
> direction.

Declared but unspecified `[BL §16]`: intervention taxonomy (blocked on programme-staff input) ·
support delivery · outcome-indicator vocabulary and impact measurement · programmes · volunteer
operations · consent and privacy (**a minimal placeholder**) · persistent-person promotion ·
beneficiary feedback and grievance handling (**principle stated, mechanism absent**).

> Two of these sit badly with §3.7 and §11.5: **consent is a placeholder** while dignity is
> foundational, and **grievance has no mechanism** while beneficiary voice is foundational and
> the sector treats CFM as a standard standing capability across five major actors
> `[EXT: via TD-04: BD-TD04-002]`. Recorded, not resolved.

Excluded from V1 `[BL §17]`, verbatim: a **predictive/preventive engine** flagging need before any
signal exists · the **donor/resource-supply side and donor–need matching** · **resource allocation
and optimisation at scale** · **trust-economy scoring, fraud/anomaly engines, and biometric
verification** · **runtime and orchestration** including payment/escrow, offline-first field ops,
ID-card/QR credentials, multi-tenant deployment, and any **autonomous multi-agent execution
layer**.

### 16.4 Roadmap — real, modelled, built later

Everything in §16.3's exclusion list **exists in humanitarian reality** and is described in this
document. The exclusions are statements about build sequence, not about the world.

Five items require an explicit ruling before boundaries are frozen, because each was named in the
project direction and each collides with §16.3:

| Item | Reality status | V1 status | Ruling needed |
|---|---|---|---|
| **Donor visibility of verified need; giving** | Real `[EXT: CHS via TD-01: BD-TD01-004]` | Excluded `[BL §17]` | In ontology scope? |
| **Donor adopting a family or case** | **Absent from every source** — genuinely new | — | Requires discovery, not assumption |
| **Matching need to giver** | Real | Excluded `[BL §17]` | In ontology scope? |
| **Biometric / facial identity** | Real; bears on §3.1 `[OPEN]` | Excluded `[BL §17]` | See below |
| **Proactive identification of the inactive but capable** | Real — capability and opportunity exist `[BL §5.3, §8]` | Excluded `[BL §17]` | In ontology scope? |
| **Multi-agent reasoning over this model** | Implementation, not reality | Excluded `[BL §17]` | Sequencing only |

**On biometric identity specifically.** Business Logic V1 groups it with fraud engines as
*"operational tooling"* `[BL §17]`. But biometric identification of vulnerable people — including
children and survivors of violence, whom `[BL §3.2]` names explicitly — engages the do-no-harm
principle of §3.7 directly. The ICRC *Handbook on Data Protection in Humanitarian Action* is the
governing sector guidance and is already in this repository's evidence base
`[EXT: via TD-02: BD-TD02-004]`. If biometric identity enters scope, it should do so through a
deliberate decision consulting that guidance — **not silently, because it happens to solve the
open identity-resolution question of §3.1.**

### 16.5 What is not known, at any layer

Stated plainly, because the previous foundation's central failure was filling gaps like these with
plausible content.

**No statement in this repository has been validated by a humanitarian practitioner.** Tier A
elicitation was never executed in any evidence dossier — not deferred, structurally unavailable.
TD-01 records the question as *"not merely unanswered but currently unanswerable by this process
alone"*, closable only by a human interviewer with named practitioners, arranged outside this
process.

**The open questions most needing it are the ones at the centre of this model:**

| `[OPEN]` | Section |
|---|---|
| How sameness of person is established across encounters | §3.1 |
| What the basic standard of wellbeing is (Sphere minimum standards not retrieved) | §3.6 |
| How family and household membership are determined, and what happens when they diverge | §4.3 |
| Whether the set of situations is open or closed, and whether seven need categories can absorb anything | §6.4 |
| How vulnerability and compound risk compose | §8.4 |
| How needs relate to one another | §7.5 |
| The kinds of evidence and their relative weight | §10.2 |
| How contradictions between claims are represented | §10.5 |
| How missing information is represented | §10.5 |
| Whether outcome, impact and learning sit inside the journey or beside it | §12.5 |
| Whether Programme and Organisation are one concept or two | §11.1 |
| Whether government, schools, employers and healthcare providers are actors or context | §11.3 |
| Whether a giver altitude exists alongside programme and case | §11.4 |
| Whether state, community and informal giving are support pathways | §13.4 |
| What indicates each outcome | §15.4 |
| Deployment context — geography, population, language, currency, partners | `CLIENT_CONTEXT_UNVERIFIED.md` |

**Every finding in this document is general/cross-context.** No source retrieved in any dossier
was specific to a deployment geography, because none was stated `[TD-01: Open Gap 3]`.

**The values inside every dimension are absent throughout** — capability types, health categories,
need categories, shelter conditions are named as *dimensions*, never as *values*. This may be
correct rather than incomplete: for interventions at least, dimensions are enduring while concrete
items are *"inherently volatile and context-dependent"* `[EXT: via TD-06: BD-TD06-004]`. Whether
that generalises is itself `[OPEN]` — and the previous foundation's enumerated value sets were
plausibly the error, not the omission.

---

## 17. Status and derivation

**This document is the conceptual reference from which the ontology, taxonomy, knowledge graph,
AI reasoning and implementation are to be derived.** Nothing downstream may introduce a concept
absent here without either tracing it to the two authoritative sources or to external humanitarian
standards, or opening it as a question.

**Status: FROZEN 2026-07-29.** The foundation phase is closed. This document does not change
except by amending an authoritative source and re-deriving. No further foundation documents are
to be authored.

**It does not draw domain boundaries.** Doing so is the first act of ontology design, and its
two structural inputs are the altitude split of §11.4 and the handoff-as-ownership-boundary of
§12.3.

**Nothing about ontology has been decided.** No primitive, entity, facet, relationship,
constraint, state, event, cognition or coordination structure appears above, by design.

**Ontology design reads this document and the two authoritative sources.** It does not read
`docs/02-understanding/` or `docs/03-discovery/` — those are frozen traceability records
behind what is stated here.

**One ruling is still required before primitive discovery can begin:** whether a Domain Primitive
means a concrete irreducible of reality (*Person*, *Household*, *Need*) or a category of concept
(*Identity*, *Relation*, *Condition*). The entire ontology derives from the answer.
