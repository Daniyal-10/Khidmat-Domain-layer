# Domain Discovery

> **FROZEN 2026-07-29. Superseded in role. Do not edit, do not extend.**
>
> Ontology design reads `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md`,
> not this document. This is the **traceability record** for external evidence: what the
> humanitarian sector's own standards and literature establish, and how each bears on the
> eleven gaps left by the two authoritative sources. Its content stands and is correct.
>
> Its most consequential finding — the programme/case altitude split (§1) — is carried into
> reference model §11.4. Corrections enter by amending an authoritative source and
> re-deriving, never by editing here.

**Addressed to the eleven gaps recorded in `MERGED_BUSINESS_UNDERSTANDING.md` §11.**

---

## 0. Method and discipline

**Inputs, and only these:**

| Tag | Source |
|---|---|
| `[MBU §n]` | `docs/02-understanding/MERGED_BUSINESS_UNDERSTANDING.md`, section n |
| `[TD-0n / BD-TD0n-00m]` | The six evidence dossiers in `docs/01-evidence/`, by finding ID |

**A material constraint on the evidence base, stated before any finding is used.**

The six dossiers were authored under the previous process. Each collected evidence in tiers:
Tier A (practitioner), Tier B (sector standards), Tier C (project-internal artifacts), Tier D
(secondary literature).

- **Tier C is void.** Every internal artifact the dossiers compared against — the business
  architecture blueprint, the project overview, the glossary, the contradiction log — was
  deleted in the reset. Any dossier claim of the form *"this reinforces our internal
  document X"* has lost its referent and **carries no weight here**.
- **Tier A was never executed.** Not deferred — structurally unavailable. No dossier contains
  a single word from a humanitarian practitioner. TD-01 records this as *"not merely unanswered
  but currently unanswerable by this process alone."*
- **Tier B and Tier D survive.** These are external: OCHA, UNHCR, IASC, ICRC, Sphere/CHS,
  interagency case-management standards, and peer-reviewed literature. They are evidence about
  the humanitarian sector, independent of anything this project ever wrote.

**Therefore:** only Tier B/D findings are used below. Where a dossier claimed corroboration of
a deleted internal document, that claim is **re-tested against the merged understanding** and
reported as it comes out — sometimes it holds against Business Logic V1 directly, sometimes it
does not.

**What this document does not do.** It does not name domains, draw boundaries, or decide what
belongs where. That is the next phase. It also does not invent: where evidence is absent, the
gap is reported as still open, and §5 is as important as §3.

---

## 1. Headline: the two sources describe one altitude; the sector operates at two

This is the largest finding of the phase, and neither authoritative source contains it.

**Business Logic V1 and the Client First Draft are both case-altitude documents.** BL's seven
actors are all internal to a single organisation acting on a single case `[MBU §5]`. Its
lifecycle is one person's journey `[MBU §6]`. Its nine models describe one person, one family,
one household, and the community around them `[MBU §4]`.

**External evidence says humanitarian reality runs two structurally distinct rhythms
concurrently.** This appears five times, in five dossiers, from independent evidence:

| # | Finding | Source strength |
|---|---|---|
| 1 | The IASC Humanitarian Programme Cycle (needs analysis → response planning → resource mobilisation → implementation & monitoring → review) is an organisation/sector-level cycle on an annual or crisis-length cadence. It *"is not a description of what happens to one specific person."* `[TD-03: BD-TD03-001]` | High — 4 independent institutional sources (IASC, UNHCR, IOM, WHO Health Cluster) |
| 2 | "Needs assessment," "coordination" and "planning" exist as named capabilities at sector/programme level, **distinct from and prerequisite to** case-level capabilities *of the same name* `[TD-04: BD-TD04-003]` | High — 4 independent sources |
| 3 | Area-level and community-wide responses are distinct programmatic value streams that *"do not cleanly decompose into sequential, individual case-level capabilities"* — they trigger on aggregated area-level signals, not individual registrations `[TD-05: BD-TD05-002]` | Medium-High |
| 4 | Intervention **Sector** is set at programme altitude; intervention **Modality** is decided at case altitude on local market feasibility and household appropriateness `[TD-06: BD-TD06-002]` | Medium-High |
| 5 | The IASC cluster system names lead and co-lead **organisations** per sector; it *"does not define individual operational roles such as a registrant, proxy, or field verifier"* `[TD-01: BD-TD01-002]` | High — OCHA + UNHCR |

TD-04 explicitly notes this is the altitude split observed *"a third, independent time."* It is
now five.

**Why this matters.** `[TD-04: BD-TD04-003]` states the consequence precisely: a capability
catalogue *"cannot name 'Needs Assessment' once without specifying which altitude it operates
at, or it will silently conflate two genuinely different activities that happen to share a
label."*

The same hazard applies to every shared term: assessment, planning, monitoring, coordination,
needs. **Business Logic V1 uses several of these without altitude qualification**, because at
case altitude no qualification is needed. The moment programme altitude enters, every one
becomes ambiguous.

**What it does not mean.** It is not a finding that Khidmat must model programme altitude.
`[MBU §8.3]` excludes resource allocation at scale, and `[MBU §8.2]` records programmes as
declared but unspecified. **The finding is that the boundary is real and must be drawn
deliberately, not discovered by accident later.** Carried to the boundary-freeze phase as its
primary input.

---

## 2. The two authoritative sources, tested against external evidence

Six statements in the merged understanding now have independent external corroboration. This
is the first time anything in this project has been checked against reality outside itself.

| Merged understanding | External corroboration | Strength |
|---|---|---|
| §6 — the journey is non-linear; feedback reopens earlier stages | Two interagency case-management standards (GBV; Child Protection) describe the six-stage cycle explicitly as *"a loop rather than a straight line — monitoring routinely sends a case back into reassessment"* `[TD-03: BD-TD03-002]` | **High**, ≥4 independent source families |
| §3.1, §7 — claims are converted to findings by verification | The speed-vs-verification conflict is documented sector-wide, and the literature resolves it through *accelerated-but-present* verification controls rather than a binary choice. The claim/finding split is *"a documented real-world response pattern to this tension, not an arbitrary design choice"* `[TD-02: BD-TD02-002]` | Medium-High |
| §3.2 — consent, bounded by necessity | ICRC *Handbook on Data Protection in Humanitarian Action* resolves consent-infeasibility in emergencies via a **bounded necessity exception**, and warns explicitly against consent becoming a box-ticking exercise `[TD-02: BD-TD02-004]` | **High** — primary Tier B + 3 secondary |
| §3.4 — accountability runs in both directions | Donor accountability and affected-population accountability are documented as structurally pulling in different directions, attributed to unequal power relations `[TD-02: BD-TD02-001]` | **High**, ≥4 source families |
| §6 — engagement stage is decoupled from how aid is delivered | Graduation Approach practice (BRAC-originated, used at scale by USAID's Bureau for Humanitarian Assistance for displaced populations) tracks a household's underlying trajectory **separately** from its status in any specific programme — *"two separately tracked concepts in mature practice, not one combined status field"* `[TD-03: BD-TD03-004]` | Medium-High, ≥4 source families |
| §8.3 — the knowledge layer is separable from delivery | Humanitarian value chains comprise two concurrent flows — an information/knowledge flow (registration, verification, needs assessment) and a material/resource flow (procurement, logistics, delivery) — which practice *"decouple[s]"* `[TD-05: BD-TD05-001]` | Medium-High |

**Reading of this table.** Business Logic V1 is holding up. Its most distinctive commitments —
epistemic humility, the non-linear journey, bounded consent, two-directional accountability,
and separating the knowledge layer from delivery — are not idiosyncratic. Each matches
documented sector practice arrived at independently.

That is a meaningful result. It is also the first genuine external validation this foundation
has ever had, and it applies to the source document, not to anything derived from it.

---

## 3. Where evidence bears on the eleven gaps

### 11.5 Consent mechanism — **substantially addressed**

`[MBU §11.5]` recorded consent as foundational in principle and a placeholder in specification.

Evidence supplies the sector's own resolution `[TD-02: BD-TD02-004]`: genuine informed consent
is *frequently infeasible* in emergency contexts for reasons of vulnerability, security and
logistics. Sector guidance — the ICRC Handbook, which is primary standard-setting material —
does not respond by abandoning consent or by blocking action. It uses a **bounded necessity
exception**, and warns that consent must not degrade into box-ticking.

**What this gives the next phase:** consent is not a binary attached to a registration. It is a
condition with a lawful-basis dimension, where "necessity" is a bounded alternative to consent
rather than a replacement for it. **What it still does not give:** what consent is obtained
for, from whom in a household, how it is withdrawn, and what withdrawal obliges. Those remain
open.

### 11.6 Grievance mechanism — **substantially addressed, and upgraded in significance**

`[MBU §11.6]` recorded beneficiary voice as foundational with no mechanism.

Evidence `[TD-04: BD-TD04-002]`, corroborated across **five independent major humanitarian
actors** maintaining their own doctrine (IOM, UNHCR, CARE, DRC, and referenced NRC guidance):
Complaints and Feedback Mechanisms are a **distinct, named, standing capability, structurally
separate from case management**, connected to it by explicit referral pathways —
*"two different systems that hand off to each other, not one system."*

**This changes the shape of the gap.** `[MBU §8.2]` inherits BL V1's framing of grievance
handling as a planned feature. The evidence says it is a standard capability in its own right
across the sector's largest actors. A foundation that treats beneficiary voice as a principle
`[MBU §3.4]` and grievance as a feature has a structural mismatch — and `[MBU §3.4]` already
requires that feedback be able to **reopen the journey**, which is exactly the referral pathway
the evidence describes.

### 11.9 Outcome measurement — **reframed, and a real conflict surfaced**

`[MBU §11.9]` recorded that the outcome-indicator vocabulary does not exist and V1 can record
that assistance occurred but not whether it worked.

Two findings bear on this, and together they **challenge Business Logic V1 directly**:

- Interagency case-management stage sets *end at closure*. BL V1's lifecycle continues past the
  equivalent point into Outcome Measurement, Impact Measurement and Knowledge Graph Learning as
  **further stages of the same lifecycle** `[MBU §6]`. Sector sources treat *"did the case
  close"* and *"did it work"* as related but organisationally distinct — typically a separate
  function, on a different cadence, sometimes a different team `[TD-03: BD-TD03-003]`.
- MEAL (Monitoring, Evaluation, Accountability and Learning) is a **named, bundled,
  semi-independent capability** — often a dedicated team — operating on its own cadence across
  whatever work it observes, *"not as the final stage of any one case's journey"*
  `[TD-04: BD-TD04-001]`, High confidence, ≥4 institutional source families.

**This is a genuine open question, and it is left open.** Either BL V1's single-lifecycle
framing is right and the sector's separation is an organisational convention rather than a fact
about reality, or outcome and impact belong to a separate discipline that *consumes* the case
lifecycle rather than continuing it. The evidence leans toward the second; it does not settle
it. Recorded as the most consequential unresolved question this phase produces.

### 11.10 Government schemes, and the support-taxonomy conflict — **dissolved**

`[MBU §10.5]` recorded that BL V1 lists five support pathways (financial, material, medical,
educational, livelihood) and the Client Draft lists seven intervention types (employment,
education, healthcare, government schemes, business support, skills development, emergency
relief), with *government schemes* mapping to nothing.

Evidence dissolves the framing rather than resolving the lists `[TD-06: BD-TD06-001]`,
High confidence, aligned with IASC clusters, CVA standards and Triple Nexus frameworks:

> Humanitarian interventions are categorised along **three fundamentally distinct** dimensions:
> **Sector** (what need is addressed), **Modality** (how it is delivered), and
> **Temporal/Objective Phase** (why and when). An intervention exists at the *intersection* —
> an Emergency [phase] In-kind [modality] Shelter [sector] intervention.

The dossier names the exact error: BL V1's list *"mixes modalities ('Financial', 'Material')
with sectors ('Medical', 'Educational') in a single list."*

**So the two lists were never in conflict.** BL V1's five conflate two dimensions; the Client
Draft's seven are mostly sector-flavoured. Neither is a taxonomy. Two further findings follow:

- **Intervention-to-need is many-to-many, not one-to-one.** Multipurpose Cash is a single
  modality intended to cover food, shelter and WASH needs concurrently `[TD-06: BD-TD06-003]`.
  A single intervention must be able to satisfy multiple needs across domains.
- **The dimensions are stable; the catalogue is volatile.** *"Jerry cans," "school fees,"
  "hygiene kits"* vary by region, organisation and emergency type `[TD-06: BD-TD06-004]`.

That last point corroborates `[MBU §8.2]`'s record that the intervention catalogue is blocked
on programme-staff input — and reframes it. **The catalogue is not missing. It is correctly
absent**, because it does not belong at this layer at all.

### 11.11 Coordination — **addressed by §1**

`[MBU §11.11]` recorded that the Client Draft names coordination as foundational, BL V1's actors
are all internal to one organisation, and neither states whether coordination is in scope.

The altitude split of §1 is the answer to *where* coordination lives: at programme altitude,
which is precisely where Business Logic V1 is silent. Whether Khidmat models that altitude
remains a scope decision, not a discovery finding.

### 11.1 Values inside every dimension — **not resolved, and possibly not a gap**

`[MBU §11.1]` recorded that both sources name dimensions (capability types, health categories,
need categories, shelter conditions) and never their values.

No evidence retrieved supplies values. But `[TD-06: BD-TD06-004]` supplies a reason to doubt
the framing: for interventions at least, the dimensions are enduring business concepts while
the concrete items are *"inherently volatile and context-dependent"* operational
implementations that belong to downstream configuration.

**If that generalises, the absence of values is correct rather than incomplete** — and the
previous foundation's enumerated value sets were the error, not the omission. Whether it
generalises from interventions to health, capability and need dimensions is **not evidenced**.
Flagged as a hypothesis to test, not a conclusion.

### 11.3 Basic standard of wellbeing — **not resolved; source identified, not retrieved**

`[MBU §11.3]` recorded that a need is defined as a gap against a basic standard of wellbeing
that neither source defines.

The Sphere Handbook's minimum humanitarian standards are the obvious candidate. TD-01's
collection log lists Sphere among sources retrieved, but only its Core Humanitarian Standard
**definitional page** — no dossier retrieved the minimum standards themselves. This is a
**named, actionable next step**, not an answered question.

### 11.2, 11.7, 11.8, 11.4 — **not resolved, no evidence retrieved**

- **11.2 How vulnerability composes.** BL V1 gives two illustrative sums and no rule. Nothing
  retrieved addresses composition. Still open.
- **11.7 Household and family boundaries.** How membership is determined, how the two relate,
  and what happens when they diverge under displacement, polygamy, fostering or
  multi-generational co-residence. Nothing retrieved. Still open.
- **11.8 Identity resolution.** How sameness of person is determined across engagements, and
  what happens when recognition is uncertain. Nothing retrieved. Still open — and this one
  carries the most weight, since `[MBU §3.5]` and `[MBU §4.1]` both rest on it and
  `[MBU §2]` names duplicate registration as a problem to be solved.
- **11.4 Deployment context.** Independently confirmed as a gap by the evidence base itself:
  *"No source retrieved was specific to this project's actual likely deployment geography"*
  `[TD-01: Open Gap 3]`, a standing limitation on **every** finding in **every** dossier. Every
  applicability scope in §1–§3 above is general/cross-context by necessity. Blocked on the
  `direct-relief-architecture.html` question in `CLIENT_CONTEXT_UNVERIFIED.md`.

---

## 4. Knowledge neither source anticipated

Beyond the altitude split (§1) and the intervention dimensions (§3, gap 11.10):

**4.1 Informal and emergent actors are a real, independent actor category.**
*"Emergent groups," "spontaneous volunteers"* and *"mutual aid/self-help groups"* are documented
as a real, independent and **frequently first-responding** category with proximity, speed and
local-trust advantages over formal organisations. The literature argues explicitly that they
should be recognised as legitimate actors in their own right, *"not merely absorbed or
supplanted by formal actors"* `[TD-01: BD-TD01-005]` — High confidence, ≥3 independent source
families spanning pandemic, conflict and urban disaster response.

**Business Logic V1's actor set `[MBU §5]` has no place for them.** Its seven roles are all
formal positions within an organisation. This is a genuine omission relative to evidence, not a
scope exclusion — nothing in `[MBU §8.3]` excludes informal actors.

**4.2 Two structural tensions the sources do not name.**

- **Donor-driven standardisation versus locally-led legitimacy.** Compliance requirements —
  standardised eligibility, beneficiary lists, financial controls — conflict with the
  flexibility and informal-network legitimacy that make locally-led response effective. Local
  actors are simultaneously required to meet donor standards and to leverage the informal
  legitimacy those standards undermine `[TD-02: BD-TD02-003]`, High confidence.
- **Speed versus verification**, managed rather than resolved `[TD-02: BD-TD02-002]`.

Both bear on `[MBU §3.5]` fairness and `[MBU §7]` epistemics. Neither source names either.

**4.3 A service handoff is a governance boundary.**
Business services are the tangible outputs of capabilities — a verified claim, an assessed
need, an approved support plan — and a value stream is built by **chaining the outputs of
discrete capabilities, not by merging the capabilities** `[TD-05: BD-TD05-003]`. The handoff
point is where ownership changes.

This is the most directly structural finding in the evidence base and is carried to the
boundary-freeze phase alongside §1.

**4.4 Donors are actors in reality; sector standards say so explicitly.**
The Core Humanitarian Standard defines humanitarian actors to **include** organisations
providing financial, material or technical support without directly delivering assistance
`[TD-01: BD-TD01-004]`.

This does not disturb `[MBU §10.4]`. It confirms both halves of it: donors are real, and
`[MBU §8.3]` excludes them from V1 scope. **Reality-membership does not imply
scope-membership** — the resolution already recorded, now with external support for its first
half. The previous foundation collapsed exactly this and opened a domain the source excluded.

**4.5 Programme and Organisation are probably distinct.**
Every Tier B source retrieved names implementing organisations separately from the programmes
and clusters they lead; none describes them as the same kind of thing `[TD-01: BD-TD01-003]`,
Medium-High. Business Logic V1 collapses them into a single actor row `[MBU §5]`.

Evidence leans toward distinct. **This is a decision, not a discovery** — recorded for the
boundary-freeze phase.

---

## 5. What cannot be discovered by this process

Stated plainly, because the previous foundation's central failure was filling gaps like these
with plausible content.

**5.1 Nothing here has been checked with a humanitarian practitioner.** Tier A was never
executed in any dossier. TD-01's disposition is unambiguous: the question is *"not merely
unanswered but currently unanswerable by this process alone"* — closing it requires a human
interviewer and named practitioners, arranged outside the discovery process.

**5.2 The gaps most in need of Tier A are precisely those §3 left open.** Vulnerability
composition, household and family boundaries, identity resolution, and the values inside every
dimension are all facts about how humanitarian work is actually done with real families. They
do not live in institutional standards documents, which is why five dossiers of Tier B/D
searching did not surface them.

**5.3 Operational role granularity has zero external validation.** TD-01 searched
specifically and found that sector standards *"operate at the organizational/coordination
level, not this granularity."* Business Logic V1's Registrant, Proxy, Field Verifier, Human
Reviewer and Case Manager `[MBU §5]` are **currently validated by nothing outside this
project.** TD-01 states closing this *"most plausibly requires Tier A evidence specifically,
not further literature search."*

That is not evidence the roles are wrong. It is a precise statement of what is not yet known
about them.

**5.4 Every finding is general/cross-context.** No source in any dossier was specific to a
deployment geography, because none was stated. This qualifies everything above.

---

## 6. Status

**Discovered and evidenced:** the altitude split (§1, five independent occurrences); six
external corroborations of the merged understanding (§2); substantive resolution of gaps 11.5,
11.6 and 11.11; dissolution of the support-taxonomy conflict and gap 11.10 (§3); five items of
knowledge neither source anticipated (§4).

**Surfaced and deliberately unresolved:** whether outcome, impact and learning belong inside
the case lifecycle or to a separate discipline (gap 11.9) — the most consequential open
question of this phase; whether Programme and Organisation are one concept or two (§4.5);
whether the absence of values inside dimensions is a defect or correct (§3, gap 11.1).

**Still open, no evidence:** vulnerability composition (11.2), basic standard of wellbeing
(11.3 — Sphere minimum standards identified but not retrieved), deployment context (11.4),
household and family boundaries (11.7), identity resolution (11.8).

**Requires action outside this process:** Tier A practitioner elicitation. Without it, gaps
11.2, 11.7 and 11.8 will not close, and the operational role vocabulary stays unvalidated.

**What became of this document.** Its findings were carried into the Domain Reference Model,
which is what ontology design reads. Two carry forward as structural inputs to boundary
setting: **§1**, the programme/case altitude split — five independent occurrences, now
reference model §11.4 — and **§4.3**, a service handoff is where ownership changes, now
reference model §12.3. Its open questions are consolidated in reference model §16.5.

**Superseded, not withdrawn.** Nothing here is retracted. It is no longer an input.
