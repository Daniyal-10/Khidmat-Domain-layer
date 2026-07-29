# Merged Business Understanding

> **FROZEN 2026-07-29. Superseded in role. Do not edit, do not extend.**
>
> Ontology design reads `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md`,
> not this document. This is the **traceability record** behind it: the two authoritative
> sources reconciled, six conflicts between them resolved (§10), eleven gaps recorded unfilled
> (§11). Its content stands and is correct. Consult it to audit where a statement in the
> reference model came from.
>
> Corrections enter by amending an authoritative source and re-deriving — never by editing here.

---

## 0. What this document is

This is the reconciliation of the two authoritative sources into one coherent statement of
what Khidmat is and what humanitarian reality it must understand.

**Sources, and only these:**

| Tag | Document |
|---|---|
| `[BL §n]` | `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, section n |
| `[CD: name]` | `KHIDMAT_AI_BUSINESS_OVERVIEW.html` (Client First Draft), named section |

**Rules observed in authoring this document:**

1. Every substantive statement carries a citation. A statement without one does not belong here.
2. Nothing is added because it is true of humanitarian work generally, or because it would
   make the model more complete. Where both sources are silent, §11 records the silence.
3. Where the sources conflict, Business Logic V1 wins, and the conflict is recorded in §10
   rather than resolved silently.
4. The organisation is by **model of reality**, following `[BL §§5–13]`, not by operational
   process. This is deliberate — see §10.1.
5. The six evidence dossiers in `docs/01-evidence/` were **not** used. They are external
   sector evidence and enter at domain discovery, the next phase. Phase 0 merges the two
   business sources and nothing else.

**What this document is not.** It is not ontology. It contains no primitives, entities,
facets, relationships as ontological constructs, states, events, or schema. Where it names a
concept it is reporting what the sources say exists, not deciding how it will be modelled.

---

## 1. What Khidmat is

Khidmat is **not a registration system** `[BL §1]`. It is not a software product, an AI
chatbot, a registration or donation platform, or an NGO CRM `[CD: What Khidmat AI Is]`.

Business Logic V1 names it a **Humanitarian Operating System** `[BL §1]`. The Client Draft
names it **a long-term effort to understand humanitarian reality itself** and an
**intelligence layer capable of understanding reality before attempting to automate it**
`[CD: The Vision, What Khidmat AI Is]`.

These are compatible. BL states the operational ambition; CD states the epistemic
precondition. Both agree software is downstream: *"Software is only one expression of that
understanding, not the goal of it"* `[CD: What Khidmat AI Is]`.

Its purpose is to understand people, families, households, communities, vulnerabilities,
capabilities, risks, and support pathways — **and to coordinate the people who act on that
understanding** — so assistance is delivered accurately, fairly, proactively and at scale,
while preserving human oversight, consent and accountability at every stage `[BL §1]`.

The long-term horizon is a **shared humanitarian intelligence foundation** supporting
organisations, communities, researchers and future AI systems working from a common
understanding of reality `[CD: Closing]`.

---

## 2. The problem

Humanitarian systems **store data but rarely understand it** `[CD: The Problem]`. Most
humanitarian software is built to register cases and track donations, not to understand the
people and circumstances behind them `[CD: The Problem]`.

Four named consequences `[CD: The Problem]`:

- duplicate registrations occur
- verification quality varies
- historical context is lost
- long-term outcomes are hard to measure

The Client Draft's diagnosis is explicit: *"The limitation is not simply software. It is the
absence of a structured understanding of humanitarian reality"* `[CD: The Problem]`.

Business Logic V1 states the same gap as a difference in question. Most systems answer
*what did the person ask for?* Khidmat must answer `[BL §2]`:

- What does this person need?
- Why do they need it?
- What will happen if the need is unmet?
- Who else is affected?
- What support pathway exists?
- What future risks are developing?

**These six questions are the functional specification of the understanding Khidmat must
hold.** Every model in §4 exists to make one or more of them answerable.

---

## 3. Governing principles

Business Logic V1 states five foundational principles `[BL §3]`. The Client Draft states six
beliefs `[CD: Core Philosophy]`. They overlap substantially. Merged, with the source of each:

**3.1 Epistemic humility — claims, not facts.**
Everything a registrant tells the system is a **claim**, not a confirmed fact. Claims carry
an explicit quality (how complete, how internally consistent). Verification converts claims
into **findings**. Assessed needs carry an explicit **confidence**. The system reasons openly
with uncertainty rather than pretending to certainty it has not earned. *"A registration is
merely a collection of claims"* until verification says otherwise `[BL §3.1]`.

Corroborated by CD: *"Evidence before conclusions"* and *"Verification before trust — nothing
is assumed true without checking"* `[CD: Core Philosophy]`.

> This principle is load-bearing beyond its section. See §7.

**3.2 Consent, dignity, do-no-harm.**
Khidmat collects deep information about vulnerable people including children, the ill, and
survivors of violence. Data is collected with consent, kept to what is necessary, and handled
so that **the act of seeking help never exposes a person to further harm**. Safety concerns —
safeguarding, domestic violence, minors without guardians — take precedence over process
`[BL §3.2]`. CD: *"Dignity at the center — every decision keeps the person first"*
`[CD: Core Philosophy]`.

**3.3 Human oversight and governance.**
The system supports human decisions; it does not replace them. Consequential decisions —
eligibility, escalation, exit — remain human decisions with a human accountable for them
`[BL §3.3]`. CD: AI *"is not expected to replace human judgment. It supports human decisions
while staying transparent about confidence, uncertainty, and what still needs verifying"*
`[CD: The AI Intelligence Layer]`.

**3.4 Accountability and beneficiary voice.**
Accountability runs in **both directions**. The system is accountable *to the people it
serves*, not only to the organisation. A beneficiary must be able to question, correct, or
complain about a decision, and that feedback must be able to **reopen the relevant part of
the journey** `[BL §3.4]`.

**3.5 Fairness and integrity.**
Assistance is allocated on the basis of understood need, applied consistently across people
in comparable situations. **The same person is recognised as one person across time**, so
support is neither duplicated nor lost between engagements `[BL §3.5]`.

**3.6 Understanding precedes automation.**
*"AI cannot make reliable humanitarian decisions unless it first understands humanitarian
reality"* `[CD: Core Philosophy]`. Stated as an ordering: knowledge before automation, reality
before implementation, business before technology `[CD: Core Philosophy]`; and as a sequence:
Reality → Knowledge → Understanding → Models → Reasoning → Intelligence → Applications
`[CD: Current Direction]`.

This principle has no direct BL counterpart in §3, but is not in tension with it — BL's entire
structure enacts it. Recorded as CD-originated.

---

## 4. The models of humanitarian reality

This is the substance of what must be understood. Nine models, per `[BL §§5–13]`.

### 4.1 Human Model — the foundation `[BL §5]`

**Persistent identity `[BL §5.1]`.** A person is a **persistent entity, not a per-case
record**. The same human being is recognised across multiple registrations, cases and
domains. This is what makes it possible to reason about a person over time — to see that a
household returning for the third time has not improved, or that a child in school at first
contact has dropped out by the second.

> BL states plainly: *"Every downstream promise about longitudinal reasoning rests on this
> principle"* `[BL §5.1]`. It is also the mechanism of fairness principle §3.5, and the answer
> to CD's named failure *"historical context is lost"* `[CD: The Problem]`. Three independent
> lines converge on it.

**Individual `[BL §5.2]`.** Every person has:

- **Identity** — name, age, gender, marital status, documentation.
- **Lifecycle stage** — infant, toddler, early childhood, school-age child, adolescent, young
  adult, adult, older adult, elderly. **A lifecycle stage is not merely an age band**; it is a
  distinct developmental reality carrying characteristic dependencies, capabilities and
  vulnerabilities. Different stages create different needs.

**Capabilities `[BL §5.3]`** — what a person *can* do, not only what they lack. Five
dimensions: physical (walk, travel, work physically); cognitive (learn, understand, decide);
educational (read, write, study); economic (earn, manage money, run a business); caregiving
(care for children, elderly, or disabled dependents).

**Health `[BL §5.4]`** — five dimensions: acute conditions (accident, surgery, injury);
chronic conditions (diabetes, kidney disease, hypertension); disabilities (visual, hearing,
mobility); mental health (depression, anxiety, trauma); nutritional conditions (malnutrition,
stunting, wasting, including clinical staging such as SAM/MAM).

### 4.2 Family Model `[BL §6]`

*"A family is not just a list of people."*

- **Relationships** — parent, child, guardian, caregiver, spouse.
- **Dependency** — who depends on whom. *Father earns → mother depends financially → children
  depend financially.* **A vulnerability in one member cascades to those who depend on them:
  a mother's risk is her infant's risk.**
- **Responsibility** — who is responsible for income, caregiving, education, decision-making.

### 4.3 Household Model `[BL §7]`

*"A household is a living unit."*

- **Housing** — ownership, rental, temporary shelter.
- **Utilities** — water, electricity, sanitation.
- **Shelter condition** — safe, damaged, flood-prone, roof leakage.
- **Household resilience** — composite capacity to absorb, adapt to and recover from shocks:
  buffering capacity, role substitution, caregiving and decision continuity, recovery
  resources. **Two households with the same need are not equally vulnerable if one can absorb
  the shock and the other cannot.**

### 4.4 Community Model `[BL §8]`

The household is understood in context, not in isolation.

- **Community context** — village, neighbourhood, district; settlement type and accessibility.
- **Available services** — schools, hospitals, markets, employment opportunities, **and the
  distance and quality of access to them**.
- **Local fabric** — local organisations, livelihood patterns, community assets, social capital.
- **Seasonal and environmental risk** — flooding, rainy season, heat waves, drought, and the
  seasonal calendar that turns *a damaged roof in a flood zone before monsoon into a preventive
  emergency rather than a routine repair*.

### 4.5 Needs Model `[BL §9]`

**A need is a gap between current state and a basic standard of wellbeing.**

Seven categories: **food** (daily food, nutrition, infant feeding, therapeutic nutrition);
**health** (treatment, surgery, medication, rehabilitation, assistive devices, diagnosis);
**education** (school fees, supplies, transport, re-enrollment); **housing** (roof repair,
shelter repair, rent support, emergency housing); **livelihood** (income support, employment,
skills development, tools and equipment); **psychosocial** (grief, trauma, chronic stress,
caregiver burden, domestic-violence aftermath); **protection** (widow support, child
protection, elder care, safeguarding of people at risk of harm).

**Needs are dynamic, not static.** A need opens, changes in severity, and resolves or expires
as circumstances change — a job restored may close a food need while a new medical need opens.
The system tracks needs across their lifetime, not as a single snapshot.

Khidmat must identify needs that are **explicitly requested**, **implied**, and **emerging**
`[BL §1]`.

### 4.6 Vulnerability Model `[BL §10]`

Vulnerability is **not a single condition**. It emerges from multiple **compounding** factors.
The system reasons about how factors combine, not only about each factor alone.

> Infant + malnutrition + low-income household = high vulnerability
> Elderly person + lives alone + mobility impairment = high vulnerability

### 4.7 Risk Model `[BL §11]`

- **Current risks** — hunger, medical deterioration, school dropout.
- **Future risks** — roof collapse during rainy season, loss of income after injury, child
  malnutrition.
- **Compound risks** — *widow + no income + disabled child = complex humanitarian risk.*

**Risk is a first-class concept** with a **horizon** (how soon), a **trend** (worsening,
stable, improving) and a **severity** — *not a byproduct of severity rules* `[BL §11]`.

**The risk domain produces signals; it does not decide what to do about them** `[BL §11]`.

### 4.8 Support Model `[BL §12]`

Support is not one thing. Different needs have different pathways: **financial** (cash,
grants); **material** (food, shelter materials); **medical** (treatment support, medication);
**educational** (scholarships, school support); **livelihood** (skills training, employment
linkage).

The Client Draft states the same principle more widely: donations are only one possible form
of help, and the range includes *employment, education, healthcare, government schemes,
business support, skills development, and emergency relief* `[CD: Beyond Donations]`. See
§10.5 on how the two lists relate.

### 4.9 Outcome Model `[BL §13]`

**The goal is not case closure. The goal is improved human wellbeing** `[BL §13]`.

Four outcome families: **health** (recovery, stability); **educational** (continued
schooling); **economic** (sustainable income); **family** (reduced dependency).

The Client Draft states the same measure independently and more sharply: *"Success is not
measured by the amount of aid distributed. Success is measured by sustainable improvement in
human well-being"* `[CD: Beyond Donations]`, with the goal *"reducing dependency through
sustainable improvement"*.

**Strong agreement between sources. Recorded as the success definition for the project.**

### 4.10 How the models compose

Business Logic V1 states the composed structure as its final vision `[BL §15]`:

```
Person → Family → Household → Community
      → Needs → Capabilities → Health → Dependencies
      → Risks → Support → Outcomes → Impact
```

BL is explicit that **this composed, cross-domain reasoning is the roadmap end-state, not a
V1 deliverable** `[BL §15]`.

---

## 5. Actors

Business Logic V1 recognises seven business roles `[BL §4]`. BL notes this is a conceptual map
of responsibilities, and that detailed operational profiles — availability, routing,
performance — are out of V1 scope.

| Role | Business responsibility |
|---|---|
| **Beneficiary / Subject** | The person or household whose needs the system exists to understand and serve. **Persists across cases and time.** |
| **Registrant** | Whoever supplies registration information — the beneficiary directly, a **proxy** (family member, community member, professional advocate), or a **volunteer**. **The registrant's role and relationship determine how much epistemic weight a claim carries.** |
| **Volunteer** | Conducts intake and field verification, later assists delivery. Appears in registration only as a registrant type. |
| **Field Verifier** | Confirms claims through field or desk activity; produces verification findings. |
| **Human Reviewer** | Adjudicates escalations, ambiguous cases, safety flags. |
| **Case Manager** | Owns the case: plans, referrals, follow-ups, assignments, and the eligibility/continuation decisions. |
| **Programme / Organisation** | Defines the assistance actually available, the eligibility criteria, and the accountability structure the case operates within. |

**Donors and the resource-supply side are explicitly not V1 actors** `[BL §4, §17]`.

The Client Draft lists *Organizations* and *Programs* among the dimensions of humanitarian
reality `[CD: What Khidmat AI Seeks to Understand]`, consistent with the Programme/Organisation
role above. See §10.4 on donors.

---

## 6. The beneficiary journey

Business Logic V1 states thirteen stages `[BL §14]`:

```
Awareness → Lead Creation → Registration (produces claims)
   → Verification (claims → findings)
   → Needs Assessment (claims + findings → identified needs, with confidence)
   → Eligibility / Approval (a human decision, gated by an approved case plan)
   → Support Planning → Volunteer Assignment → Support Delivery → Follow-up
   → Case Management (orchestrates plan, referrals, follow-ups, assignments)
   → Outcome Measurement → Impact Measurement → Knowledge Graph Learning
```

**On "Approval."** Eligibility is a human decision realised as a verification outcome **plus**
an approved case plan. A case progresses to active standing only after verification clears it
and a case plan is approved. **It is not an automatic status flip** `[BL §14]`.

**The accountability loop.** At every stage a beneficiary may question or correct a decision,
and new information — a changed circumstance, a grievance, a re-verification trigger — can send
the case **back** to the appropriate earlier stage. **The journey is not strictly
one-directional** `[BL §14]`.

The Client Draft states the same non-linearity independently: *"real humanitarian journeys are
rarely linear. People may revisit earlier stages, needs evolve, assessments change, and
recovery does not always move in a straight line"* `[CD: End-to-End Humanitarian Flow]`.

**Macro-state.** The journey is tracked as engagement stages — identified,
registration_initiated, registered, verification_pending, active, engaged, monitored,
suspended, review_required, exited — **decoupled from how any specific aid is delivered**
`[BL §14]`.

> **Note on status.** This journey is a statement of what happens in humanitarian reality, and
> is recorded here as such. It is **not** a licence to organise the ontology by these stages.
> See §10.1.

---

## 7. Epistemics: what the system is entitled to believe

This is not a section of either source. It is a cross-cutting concern that both sources state
in fragments, collected here because it governs every model in §4.

**The transformation chain** `[BL §3.1, §14]`:

```
claim  ──verification──►  finding  ──assessment──►  identified need (with confidence)
```

**What each source contributes:**

| Element | Source |
|---|---|
| Everything a registrant states is a claim, not a fact | `[BL §3.1]` |
| Claims carry explicit quality — completeness, internal consistency | `[BL §3.1]` |
| Verification converts claims into findings | `[BL §3.1, §14]` |
| Assessed needs carry explicit confidence | `[BL §3.1, §14]` |
| Who supplied a claim determines its epistemic weight | `[BL §4]` |
| The system reasons openly with uncertainty rather than feigning certainty | `[BL §3.1]` |
| Consequential decisions stay human | `[BL §3.3]` |
| Evidence before conclusions; verification before trust | `[CD: Core Philosophy]` |
| AI stays transparent about confidence, uncertainty, and what still needs verifying | `[CD: The AI Intelligence Layer]` |
| Evidence and Verification are dimensions of humanitarian reality in their own right | `[CD: What Khidmat AI Seeks to Understand]` |

**Why this is collected here.** Both sources treat the system's epistemic condition as part of
reality to be modelled, not as application behaviour. CD lists *Evidence* and *Verification*
alongside *Individuals* and *Communities* as things to be understood
`[CD: What Khidmat AI Seeks to Understand]`. BL makes claim-status and confidence structural
properties of needs and findings, not annotations on them `[BL §3.1, §14]`.

Every model in §4 is therefore held **at some epistemic status**. A household's shelter
condition is a claim until verified. A need's severity carries a confidence. This is not a
tenth model — it is a property of the other nine.

---

## 8. Scope

### 8.1 Understood and specified in V1 `[BL §16]`

> **Disclosed rewording, and a void claim in the source.**
>
> Business Logic V1 titles this list **"Delivered today (built in the repository)"** and states
> that the authoritative definitions live in `shared/`, `registration/`, `shared/risk/`,
> `verification-operations/`, `needs-assessment/`, `case-management/`, `beneficiary-lifecycle/`
> and `community-context/`, with sequencing in `knowledge_layer_roadmap.md`.
>
> **None of those exist in this repository and none ever did.** They refer to an earlier
> codebase outside this project. Nothing is built.
>
> This section therefore reports BL V1's list as **specified**, not as delivered — a
> deliberate weakening of the source's claim, disclosed here rather than made silently. The
> nine items are statements of what V1 *intends to understand*. Any reading of them as existing
> artifacts is false, and BL V1's pointer delegating concept definitions to those directories
> is **void**: the authoritative definition of every concept it names is the reference model,
> derived from BL V1's own prose and nothing else.

Human Model (lifecycle stages, capabilities, dependency, health conditions) · Family and
Household models, including household resilience · Community context · Needs and
confidence-weighted needs assessment · Vulnerability and Risk (composition, horizon, trend,
compound risk) · Verification · Case orchestration · Beneficiary lifecycle macro-state ·
Claim epistemics and temporal reasoning.

### 8.2 Declared but not specified `[BL §16]`

Support intervention taxonomy — **blocked on operational input from programme staff** ·
Support delivery (vendors, logistics, proof of delivery) · Outcome-indicator vocabulary and
impact measurement · Programmes (eligibility, cycles, enrollment, budget, reporting) ·
Volunteer operations (full profiles and dispatch) · Consent and privacy — **currently a
minimal placeholder** · Persistent Person entity promotion · Beneficiary feedback and
grievance handling — **principle stated, mechanism to follow**.

> Two of these are consequential for a foundation that claims dignity and accountability as
> principles: **consent and privacy is a placeholder** `[BL §16]` while §3.2 makes consent
> foundational, and **grievance handling has no mechanism** `[BL §16]` while §3.4 makes
> beneficiary voice foundational. Recorded here, not resolved.

### 8.3 Explicitly excluded from V1 `[BL §17]`

- **A predictive / preventive engine** that flags need before any signal exists — V2 horizon.
- **The donor / resource-supply side and donor–need matching.** *"Khidmat V1 understands
  beneficiaries; it is not a donation marketplace."*
- **Resource allocation and optimisation at scale.**
- **Trust-economy scoring, fraud/anomaly engines, biometric verification.** Light integrity
  such as duplicate suspicion is already handled.
- **Runtime and orchestration** — payment/escrow, offline-first field ops, ID-card/QR
  credentials, multi-tenant deployment, and any autonomous multi-agent execution layer.

**These exclusions are binding.** The previous foundation overrode two of them through internal
decisions and built discovery domains the source had excluded. An exclusion may be revisited
only by amending Business Logic V1 itself, never by a downstream document.

> **Subsequent decision (2026-07-29), recorded here so this section is not read as current.**
> The Project Lead exercised exactly the route this paragraph reserves: the exclusions were
> revisited at the level of the project's own scope definition rather than by a downstream
> override. The resolution — recorded in `docs/03-discovery/SCOPE_COVERAGE.md` §4 and enacted
> in reference model §16 — is that **these items are modelled as humanitarian reality, and
> their V1 exclusion is a build-sequence statement, not a claim that they are unreal.**
>
> The rule stated above still holds and was followed. What changed is the scope, not the rule.

### 8.4 The prediction boundary

Business Logic V1 makes a scope correction against its own vision, twice, and it governs.

Its §1 states the system exists to identify needs *"likely to occur in the future — before the
beneficiary has to ask."* Its scope-honesty note immediately qualifies this: **V1 delivers
structured understanding and reactive inference — it reasons from what is known and stated.
Forward prediction of need before any signal exists is the roadmap end-state.** *"V1 must not
be read as promising a prediction engine"* `[BL §1]`. Repeated for risk at `[BL §11]`.

The Client Draft's *"proactively"* framing `[CD: The Vision]` is read subject to this
qualification.

> A source that corrects its own ambition is more trustworthy than one that does not. This is
> part of why BL V1 is the senior authority.

---

## 9. What the sources agree on

Recorded because independent agreement across two documents is the strongest signal available
in Phase 0, and because these points should survive every later phase unchanged.

| Agreement | BL | CD |
|---|---|---|
| Khidmat is not a registration/donation platform or CRM | §1 | What Khidmat AI Is |
| Understanding must precede automation | §2 | Core Philosophy; Current Direction |
| Success is improved wellbeing, not aid delivered or cases closed | §13 | Beyond Donations |
| Nothing is trusted without verification | §3.1 | Core Philosophy |
| Human judgment is supported, never replaced | §3.3 | The AI Intelligence Layer |
| The person is understood in context — family, household, community | §§5–8 | The Vision |
| The journey is non-linear; people revisit earlier stages | §14 | End-to-End Flow |
| Uncertainty and confidence must be visible, not hidden | §3.1 | The AI Intelligence Layer |
| Dignity is central | §3.2 | Core Philosophy |
| Support extends far beyond donations | §12 | Beyond Donations |

---

## 10. Conflicts, and how each is resolved

### 10.1 Organising axis — reality or process

**The conflict.** Business Logic V1 organises humanitarian reality by **model**: Human,
Family, Household, Community, Needs, Vulnerability, Risk, Support, Outcome `[BL §§5–13]`.

The Client Draft contains **two lists that do not agree with each other**:

- *What Khidmat AI Seeks to Understand* — twelve **dimensions of reality**: human needs,
  individuals, households and families, communities, organizations, programs, interventions,
  evidence, verification, relationships, outcomes, decision making. CD states explicitly that
  this list is *"organized around reality — the entities, relationships, and outcomes that make
  up humanitarian work"* and **not** around software users `[CD: What Khidmat AI Seeks to Understand]`.
- *Foundational Understanding* — eleven areas: Registration, Identity, Household Understanding,
  Evidence, Verification, Assessment, Decision Support, Interventions, Coordination, Monitoring,
  Reporting. CD says these *"are not software features or modules"* `[CD: Foundational Understanding]`
  — but six of the eleven name **activities** (registration, verification, assessment, decision
  support, monitoring, reporting), not things that exist in the world.

**Resolution.** Business Logic V1's model-based organisation governs. CD's twelve dimensions
are **corroborating** — they map onto BL's models with no forced fit. CD's eleven foundational
areas are recorded as **statements of required capability, not as structure**. They describe
what the system must be able to do; they do not describe what exists.

**Why this matters more than any other item in this document.** The previous foundation took
the process-shaped list as its organising axis and built ten discovery domains around
operational function — registration, casework, programme management, logistics, evaluation,
coordination. The result, in that work's own words, was that *"Registration & Identity holds a
registry record; Case Management holds a workflow record. Neither holds a person."*

The process list is not wrong. It is a description of activity, and activity is real. But
**activity is not the axis along which reality decomposes**, and using it as one produces a
model of the organisation rather than a model of the people. `[BL §17]` excludes runtime and
orchestration from scope; making operational process the organising axis imports precisely
what that exclusion keeps out.

### 10.2 Epistemics — depth of specification

**The conflict.** CD is not silent on epistemics — it states *evidence before conclusions*,
*verification before trust*, and requires transparency about confidence and uncertainty
`[CD: Core Philosophy, The AI Intelligence Layer]`. But it specifies no mechanism.
BL specifies the full chain: claim → finding → confidence-weighted assessed need, with claim
quality and registrant-dependent epistemic weight `[BL §3.1, §4, §14]`.

**Resolution.** BL governs and supplies the mechanism; CD corroborates the requirement. No
contradiction — a difference in depth. Collected in §7.

### 10.3 Vulnerability and risk — absent from CD

**The conflict.** CD has no vulnerability model and no risk model. BL has both, and makes risk
first-class with horizon, trend and severity `[BL §10, §11]`.

**Resolution.** BL supplies both. This is a **gap in CD, not a disagreement** — CD is a vision
document and does not descend to this level. Recorded because it means §4.6 and §4.7 rest on a
single source, unlike most of §4.

### 10.4 The donor and resource-supply side

**The conflict.** CD lists *Organizations* among the dimensions of humanitarian reality
`[CD: What Khidmat AI Seeks to Understand]` and devotes a section to *Beyond Donations*
`[CD: Beyond Donations]`. BL excludes the donor and resource-supply side from V1 entirely, in
two places `[BL §4, §17]`.

**Resolution.** BL governs. **Giving and donors exist in humanitarian reality; they are out of
Khidmat V1's scope.** These are different statements and both are true. CD's *Beyond Donations*
section is in fact about the **breadth of support types**, not about donor management — read
correctly it supports `[BL §12]` rather than conflicting with `[BL §17]`.

> The previous foundation collapsed exactly this distinction. An internal decision reasoned
> that because donors are real, a donor domain was warranted — and opened one the source had
> excluded. **Reality-membership does not imply scope-membership.** This is the specific
> reasoning error to avoid.

### 10.5 Support taxonomy — two different lists

**The conflict.** BL §12 lists five support pathways: financial, material, medical,
educational, livelihood. CD lists seven intervention types: employment, education, healthcare,
government schemes, business support, skills development, emergency relief
`[CD: Beyond Donations]`.

**Resolution.** Neither list is authoritative as a taxonomy. BL is explicit that the concrete
intervention catalogue *"is defined operationally with programme staff"* and is **blocked on
input that does not yet exist** `[BL §12, §16]`.

Both lists are therefore **candidate material, not settled structure**. Note that CD's
*government schemes* has no BL counterpart — the only support type in either document that
does not map onto the other. Carried to §11.

### 10.6 Lifecycle granularity and endpoint

**The conflict.** CD gives ten steps ending at *Long-Term Independence*
`[CD: End-to-End Humanitarian Flow]`. BL gives thirteen ending at *Knowledge Graph Learning*
`[BL §14]`.

**Resolution.** BL governs on granularity and structure. The endpoints are not in conflict —
they answer different questions. CD's *Long-Term Independence* is an **outcome for the person**
and is corroborated by BL's family outcome *"reduced dependency"* `[BL §13]`. BL's *Knowledge
Graph Learning* is an **outcome for the system**. Both are real; they belong to different
subjects.

CD's step 9, *Recovery*, has no direct BL stage. It sits between BL's *Follow-up* and *Outcome
Measurement* and is best read as an outcome state rather than a process stage.

---

## 11. What neither source states

Recorded as gaps, deliberately unfilled. These are the questions domain discovery must answer,
and the places where invention would be easiest and most damaging.

**11.1 The values inside every dimension.** Both sources name the **dimensions** along which
reality varies — capability types, health categories, need categories, shelter conditions — and
neither states the **values** those dimensions take, or whether they are qualitative,
graded, or scored. `[BL §5.3, §5.4, §7, §9]` all name dimensions only.

**11.2 How vulnerability composes.** BL states that vulnerability emerges from compounding
factors and gives two illustrative sums `[BL §10]`. It does not state the composition rule.
The same gap exists for compound risk `[BL §11]`.

**11.3 What "basic standard of wellbeing" means.** The needs model defines a need as a gap
against this standard `[BL §9]`. Neither source defines the standard.

**11.4 Deployment context.** Neither source states a geography, population, language, currency,
partner set, or connectivity assumption. See `CLIENT_CONTEXT_UNVERIFIED.md` — content exists
claiming to answer this, sourced to a client file not present in the repository.

**11.5 Consent mechanism.** §3.2 makes consent foundational; `[BL §16]` records the treatment
as a minimal placeholder. What consent is obtained for, from whom, how it is withdrawn, and
what happens on withdrawal are unstated.

**11.6 Grievance mechanism.** §3.4 makes beneficiary voice foundational and requires that
feedback can reopen the journey; `[BL §16]` records the mechanism as absent.

**11.7 Household and family boundaries.** BL models family `[BL §6]` and household `[BL §7]`
separately without stating how membership is determined, how the two relate, or what happens
when they diverge — as they do under displacement, polygamy, fostering, or multi-generational
co-residence.

**11.8 Identity resolution.** §3.5 and §5.1 require that the same person be recognised across
time and engagements. Neither source states how sameness is determined, nor what happens when
recognition is uncertain — though CD names *"duplicate registrations occur"* as a problem to be
solved `[CD: The Problem]`.

**11.9 Outcome measurement.** `[BL §13]` names four outcome families; `[BL §16]` records that
the indicator vocabulary does not exist and that **V1 can record that assistance occurred but
cannot yet measure whether it worked** `[BL §13]`.

**11.10 Government schemes.** Present in CD's support list, absent from BL's `[CD: Beyond
Donations]` vs `[BL §12]`. Whether Khidmat models state provision as a support pathway is
unresolved.

**11.11 Coordination.** CD names coordination as a foundational area *"how people and
organizations work together"* `[CD: Foundational Understanding]`. BL's actors are all internal
to one organisation `[BL §4]`, and cross-organisational structure is not modelled. Whether
coordination is in V1 scope is unstated by both.

---

## 12. Status

**Phase 0 steps 1–3 complete:** Business Logic V1 understood; Client First Draft understood;
both merged into this document.

**What became of this document.** It fed domain discovery (`docs/03-discovery/`), and both then
fed the Domain Reference Model, which is what ontology design reads. Its eleven gaps were
carried forward and are now tracked in reference model §16.5.

**Its standing role is traceability.** Every statement in the reference model that originates
in Business Logic V1 or the Client First Draft can be audited back through here, including the
six source conflicts resolved in §10.

**Superseded, not withdrawn.** Nothing in this document is retracted. It is no longer an input.
