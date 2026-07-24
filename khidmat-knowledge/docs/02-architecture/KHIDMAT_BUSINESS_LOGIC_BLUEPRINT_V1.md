# KHIDMAT AI — BUSINESS LOGIC BLUEPRINT V1

**Status:** Completion-ready. This edition incorporates the improvements approved by the
Blueprint V1 Audit and the Blueprint V1 Decision Review. It is the authoritative
first-generation *business specification* for the Khidmat Knowledge Layer and is ready to be
frozen.

**What this document is:** a statement of the business architecture — the actors, principles,
models, lifecycle, and vision the system serves. It is not ontology, taxonomy, reasoning, or
runtime design. Where it names a concept, the authoritative definition lives in the
repository (`shared/`, `registration/`, `shared/risk/`, `verification-operations/`,
`needs-assessment/`, `case-management/`, `beneficiary-lifecycle/`, `community-context/`) and
its sequencing lives in `knowledge_layer_roadmap.md`. This document describes the *target*
business architecture; Section 16 states plainly what is delivered today versus planned.

---

## 1. Vision

Khidmat AI is not a registration system.

Khidmat AI is a **Humanitarian Operating System**.

Its purpose is to understand people, families, households, communities, vulnerabilities,
capabilities, risks, and support pathways — and to coordinate the people who act on that
understanding — so that assistance can be delivered accurately, fairly, proactively, and at
scale, while preserving human oversight, consent, and accountability at every stage.

The system exists to identify:

- needs that are explicitly requested
- needs that are implied
- needs that are emerging

and, as its long-term horizon, needs that are **likely to occur in the future** — before the
beneficiary has to ask.

> **Scope honesty (approved improvement).** Proactive, *predictive* identification of future
> need is the direction of the architecture, not a capability V1 guarantees today. V1 delivers
> structured understanding and reactive inference (it reasons from what is known and stated).
> Forward prediction of need before any signal exists is the roadmap's end-state
> (see Section 15 and Section 17). V1 must not be read as promising a prediction engine.

---

## 2. Core Philosophy

Most systems answer:

> What did the person ask for?

Khidmat answers:

> What does this person need?
> Why do they need it?
> What will happen if the need is unmet?
> Who else is affected?
> What support pathway exists?
> What future risks are developing?

To answer those questions responsibly, Khidmat operates under a small set of foundational
principles. These are not implementation details — they are the stance the whole system takes
toward the people it serves.

---

## 3. Foundational Principles

**3.1 Epistemic humility — claims, not facts.**
Everything a registrant tells the system is a *claim*, not a confirmed fact. Claims carry an
explicit quality (how complete, how internally consistent). Verification converts claims into
findings. Assessed needs carry an explicit confidence. The system reasons openly with
uncertainty rather than pretending to certainty it has not earned. *"A registration is merely a
collection of claims"* until verification says otherwise.

**3.2 Consent, dignity, and do-no-harm.**
Khidmat collects deep information about vulnerable people — including children, the ill, and
survivors of violence. Data is collected with consent, kept to what is necessary, and handled
so that the act of seeking help never exposes a person to further harm. Safety concerns
(safeguarding, domestic violence, minors without guardians) take precedence over process.

**3.3 Human oversight and governance.**
The system supports human decisions; it does not replace them. Consequential
decisions — eligibility, escalation, exit — remain human decisions with a human accountable
for them. Every concept has a single authoritative owner, and the knowledge layer stays
internally consistent by governance, not by convention.

**3.4 Accountability and beneficiary voice.**
Accountability runs in both directions. The system is accountable *to* the people it serves,
not only to the organisation. A beneficiary must be able to question, correct, or complain
about a decision, and that feedback must be able to reopen the relevant part of the journey.

**3.5 Fairness and integrity.**
Assistance is allocated on the basis of understood need, applied consistently across people in
comparable situations. The same person is recognised as one person across time, so that
support is neither duplicated nor lost between engagements.

---

## 4. Actors and Operational Roles

A humanitarian operating system is defined not only by whom it serves but by whom it
coordinates. V1 recognises the following business roles. (This is a conceptual map of
responsibilities; detailed operational profiles — availability, routing, performance — belong
to the Volunteer Operations domain and are out of V1 scope.)

| Role | Business responsibility |
|---|---|
| **Beneficiary / Subject** | The person or household whose needs the system exists to understand and serve. Persists across cases and time. |
| **Registrant** | Whoever supplies registration information — the beneficiary directly, or a **proxy** (family member, community member, professional advocate), or a **volunteer**. The registrant's role and relationship determine how much epistemic weight a claim carries. |
| **Volunteer** | Conducts intake and field verification, and later assists delivery. Appears in registration only as a registrant type; the full volunteer profile lives in the Volunteer Operations domain. |
| **Field Verifier** | Confirms claims through field or desk activity and produces verification findings. |
| **Human Reviewer** | Adjudicates escalations, ambiguous cases, and safety flags. |
| **Case Manager** | Owns the case: plans, referrals, follow-ups, assignments, and the eligibility/continuation decisions. |
| **Programme / Organisation** | Defines the assistance actually available, the eligibility criteria, and the accountability structure the case operates within. |

*Donors and the resource-supply side are intentionally not V1 actors — see Section 17.*

---

## 5. Human Model

The foundation of the system is the Human Model.

**5.1 Persistent identity.**
A person is a *persistent entity*, not a per-case record. The same human being recognised
across multiple registrations, cases, and domains is what makes it possible to reason about a
person over time — to see that a household returning for the third time has not improved, or
that a child in school at first contact has dropped out by the second. Every downstream
promise about longitudinal reasoning rests on this principle.

**5.2 Individual.**

Every person has:

- **Identity** — name, age, gender, marital status, documentation.
- **Lifecycle stage** — infant, toddler, early childhood, school-age child, adolescent, young
  adult, adult, older adult, elderly. A lifecycle stage is not merely an age band; it is a
  *distinct developmental reality* carrying characteristic dependencies, capabilities, and
  vulnerabilities. Different stages create different needs.

**5.3 Capabilities** — what a person *can* do, not only what they lack:

- **Physical** — walk, travel, work physically.
- **Cognitive** — learn, understand, make decisions.
- **Educational** — read, write, study.
- **Economic** — earn, manage money, run a business.
- **Caregiving** — care for children, elderly, or disabled dependents.

**5.4 Health** — the system understands:

- **Acute conditions** — accident, surgery, injury.
- **Chronic conditions** — diabetes, kidney disease, hypertension.
- **Disabilities** — visual, hearing, mobility impairment.
- **Mental health** — depression, anxiety, trauma.
- **Nutritional conditions** — malnutrition, stunting, wasting (including clinical staging such
  as SAM/MAM).

---

## 6. Family Model

A family is not just a list of people.

The system understands:

- **Relationships** — parent, child, guardian, caregiver, spouse.
- **Dependency** — who depends on whom. *(Father earns → mother depends financially →
  children depend financially.)* A vulnerability in one member cascades to those who depend on
  them: a mother's risk is her infant's risk.
- **Responsibility** — who is responsible for income, caregiving, education, decision-making.

---

## 7. Household Model

A household is a living unit.

The system understands:

- **Housing** — ownership, rental, temporary shelter.
- **Utilities** — water, electricity, sanitation.
- **Shelter condition** — safe, damaged, flood-prone, roof leakage.
- **Household resilience** — the household's composite capacity to absorb, adapt to, and
  recover from shocks: buffering capacity, role substitution, caregiving and decision
  continuity, recovery resources. Two households with the same need are not equally
  vulnerable if one can absorb the shock and the other cannot.

---

## 8. Community Model

The system understands the household in its context, not in isolation:

- **Community context** — village, neighborhood, district; settlement type and accessibility.
- **Available services** — schools, hospitals, markets, employment opportunities, and the
  distance and quality of access to them.
- **Local fabric** — local organisations, livelihood patterns, community assets, and social
  capital.
- **Seasonal and environmental risk** — flooding, rainy season, heat waves, drought, and the
  seasonal calendar that turns a damaged roof in a flood zone before monsoon into a preventive
  emergency rather than a routine repair.

---

## 9. Needs Model

A need is a gap between current state and a basic standard of wellbeing.

Need categories:

- **Food** — daily food, nutrition, infant feeding, therapeutic nutrition.
- **Health** — treatment, surgery, medication, rehabilitation, assistive devices, diagnosis.
- **Education** — school fees, supplies, transport, re-enrollment.
- **Housing** — roof repair, shelter repair, rent support, emergency housing.
- **Livelihood** — income support, employment, skills development, tools and equipment.
- **Psychosocial** — grief, trauma, chronic stress, caregiver burden, domestic-violence
  aftermath.
- **Protection** — widow support, child protection, elder care, and safeguarding of people at
  risk of harm.

**Needs are dynamic, not static.** A need opens, changes in severity, and resolves or expires
as circumstances change — a job restored may close a food need while a new medical need opens.
The system tracks needs across their lifetime, not as a single snapshot.

---

## 10. Vulnerability Model

Vulnerability is not a single condition. It emerges from multiple compounding factors.

> Infant + malnutrition + low-income household = high vulnerability
>
> Elderly person + lives alone + mobility impairment = high vulnerability

The system reasons about how factors combine, not only about each factor alone.

---

## 11. Risk Model

The system reasons about:

- **Current risks** — hunger, medical deterioration, school dropout.
- **Future risks** — roof collapse during rainy season, loss of income after injury, child
  malnutrition.
- **Compound risks** — *widow + no income + disabled child = complex humanitarian risk.*

Risk is a first-class concept with a horizon (how soon), a trend (worsening, stable,
improving), and a severity — not a byproduct of severity rules.

> **Scope note (approved improvement).** V1 reasons about risk from what is currently known
> and stated. Generating *predictive* risk signals — flagging a crisis before any stated
> need or observed signal exists — depends on longitudinal, seasonal, and community data and
> is the roadmap horizon (Section 15), not a V1 guarantee. The risk domain produces signals;
> it does not decide what to do about them.

---

## 12. Support Model

Support is not one thing. Different needs have different support pathways:

- **Financial** — cash, grants.
- **Material** — food, shelter materials.
- **Medical** — treatment support, medication.
- **Educational** — scholarships, school support.
- **Livelihood** — skills training, employment linkage.

What Khidmat can *actually* offer — the concrete intervention catalogue, eligibility per
intervention, and how support is physically delivered (vendors, logistics, proof of
delivery) — is defined operationally with programme staff and belongs to the intervention
taxonomy and the Support Delivery domain (planned; see Section 16).

---

## 13. Outcome Model

The goal is not case closure. The goal is improved human wellbeing.

- **Health outcomes** — recovery, stability.
- **Educational outcomes** — continued schooling.
- **Economic outcomes** — sustainable income.
- **Family outcomes** — reduced dependency.

Measuring outcomes — baseline, endline, and whether a situation improved, held, or
deteriorated — requires an outcome-indicator vocabulary that is planned but not yet delivered
(Section 16). Until then, V1 can record that assistance occurred but cannot yet measure whether
it worked.

---

## 14. Beneficiary Lifecycle — The Humanitarian Operating Flow

A beneficiary moves through a validated end-to-end journey. Each stage has an owning domain;
transitions carry information forward under single ownership.

```
Awareness
   ↓
Lead Creation
   ↓
Registration                (produces claims)
   ↓
Verification                (claims → findings)
   ↓
Needs Assessment            (claims + findings → identified needs, with confidence)
   ↓
Eligibility / Approval      (a human decision, gated by an approved case plan)
   ↓
Support Planning
   ↓
Volunteer Assignment
   ↓
Support Delivery
   ↓
Follow-up
   ↓
Case Management             (orchestrates plan, referrals, follow-ups, assignments)
   ↓
Outcome Measurement
   ↓
Impact Measurement
   ↓
Knowledge Graph Learning
```

**On "Approval."** Eligibility is a human decision realised as a verification outcome plus an
approved case plan: a case progresses to active standing only after verification clears it and
a case plan is approved. It is not an automatic status flip. Programme-level eligibility
criteria are owned by the Programs domain (planned).

**Accountability loop.** At every stage a beneficiary may question or correct a decision, and
new information (a changed circumstance, a grievance, a re-verification trigger) can send the
case back to the appropriate earlier stage. The journey is not strictly one-directional.

The macro-state of this journey is tracked as engagement stages (identified →
registration_initiated → registered → verification_pending → active → engaged → monitored →
suspended → review_required → exited), decoupled from how any specific aid is delivered.

---

## 15. Humanitarian Knowledge Graph (Final Vision)

```
Person → Family → Household → Community
      → Needs → Capabilities → Health → Dependencies
      → Risks → Support → Outcomes → Impact
```

The ultimate objective of Khidmat AI is a system that understands humanitarian reality deeply
enough to identify needs, risks, and support pathways — eventually before they become
crises — while preserving human oversight, consent, and accountability at every stage. This
composed, cross-domain reasoning is the roadmap's end-state, not a V1 deliverable.

---

## 16. Scope — Delivered Now vs. Planned

V1 describes the target business architecture. Maturity and sequencing are governed by
`knowledge_layer_roadmap.md`. To prevent this frozen specification from over-claiming:

**Delivered today (built in the repository):**
- Human Model (lifecycle stages, capabilities, dependency, health conditions)
- Family and Household models; household resilience
- Community context (built; pending canonical migration)
- Needs (registration) and confidence-weighted Needs Assessment
- Vulnerability and Risk (composition, horizon, trend, compound risk)
- Verification Operations
- Case Management orchestration
- Beneficiary Lifecycle (macro-state tracking)
- Claim epistemics and temporal reasoning

**Planned (declared and sequenced, not yet delivered):**
- Support intervention taxonomy (blocked on operational input from programme staff)
- Support Delivery (vendors, logistics, proof of delivery)
- Outcome-indicator vocabulary; Impact measurement
- Programs (eligibility, cycles, enrollment, budget, reporting)
- Volunteer Operations (full volunteer profiles and dispatch)
- Consent & Privacy (currently a minimal placeholder)
- Persistent Person entity promotion (the Beneficiary-snapshot → cross-case Person seam)
- Beneficiary feedback / grievance handling (principle stated here; mechanism to follow)

---

## 17. Explicitly Out of Scope for V1

The following are intentionally excluded so V1 stays a first-generation *understanding*
layer. Some are inspired by mature systems such as Direct Relief; they are not adopted merely
because they exist elsewhere, and none is a V1 commitment:

- **A predictive/preventive engine** that flags need before any signal exists (V2 horizon).
- **The donor / resource-supply side and donor–need matching** (Khidmat V1 understands
  beneficiaries; it is not a donation marketplace).
- **Resource allocation and optimisation** at scale (future).
- **Trust-economy scoring, fraud/anomaly engines, and biometric verification** (operational
  tooling; light integrity such as duplicate suspicion is already handled).
- **Runtime and orchestration** — payment/escrow, offline-first field ops, ID-card/QR
  credentials, multi-tenant deployment, and any autonomous multi-agent execution layer. This
  repository deliberately stops at the knowledge layer; runtime is designed against it, later.

---

*End of Business Logic Blueprint V1.*
