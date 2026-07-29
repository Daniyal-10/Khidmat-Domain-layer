# Scope Coverage — the described system vs. the authoritative source

> **FROZEN 2026-07-29. Decision taken — this finding is closed.**
>
> Raised as a blocking conflict: Business Logic V1 §17 excludes roughly half the end-to-end
> flow the Project Lead described. **Resolved by Option C of §4** — model humanitarian reality
> in full, sequence implementation separately — enacted by the Project Lead's instruction to
> author the Domain Reference Model, in which §16 separates humanitarian reality from ontology
> scope from V1 implementation scope from roadmap.
>
> Retained as the **traceability record** for that decision: what was excluded, by which
> clause, and why the resolution took the form it did. Do not edit or extend.

---

## 0. Why this document exists

The Project Lead's instruction is to produce **the entire project ontology, end to end**. The
end-to-end flow, as described, runs:

> registration of any person → any need, any evidence, details taken as per the need and the
> conversation → the AI understands the person, individual, household → verification →
> dispatch to a volunteer → volunteer visits the nearest beneficiary → facial recognition →
> evidence collection per the case and needs → need may be anything (health, shelter, medical,
> educational, financial, clothing) → verified need plus exact location appears on the donor
> side → anyone able to help can help → one-time needs fulfilled, or a donor adopts a family or
> case → re-verification that real needs were satisfied → environmental effects → long-term
> assessment (identify young people who are inactive, arrange work, set up businesses) → any
> case type can exist

**Business Logic V1 §17 explicitly excludes roughly half of that flow.** Not by omission — by
deliberate, stated design decision.

This is not a defect in the work completed. It is a **conflict between two authorities**: the
Lead's end-to-end mandate, and the source document the Lead's own reset instruction made
supreme. Both cannot be satisfied as written.

---

## 1. Coverage map

Each element of the described flow, tested against `MERGED_BUSINESS_UNDERSTANDING.md` (MBU) and
`DOMAIN_DISCOVERY.md` (DD).

### Covered — the source supports this fully

| Element described | Where it is covered |
|---|---|
| Registration of any person | `[MBU §6]` Registration stage, produces claims |
| Any need — health, shelter, medical, educational, financial, clothing | `[MBU §4.5]` seven need categories: food, health, education, housing, livelihood, psychosocial, protection. "Clothing" is a material modality against a housing/protection need `[DD §3, gap 11.10]` |
| Evidence collection | `[MBU §6, §7]` — evidence and verification are first-class |
| Verification converting claims to findings | `[MBU §3.1, §7]` — the strongest-evidenced part of the whole foundation |
| Understanding the person, individual, household | `[MBU §4.1–4.4]` — Human, Family, Household, Community models. **This is the most complete area of the source.** |
| Re-verification / needs change over time | `[MBU §4.5]` needs are dynamic; `[MBU §6]` re-verification triggers can reopen the journey |
| Environmental effects | `[MBU §4.4]` seasonal and environmental risk, including the seasonal calendar |
| Any case type can exist | `[MBU §4.5]` — though the seven need categories are a **closed** list; see §3.3 |

### Partially covered — real but under-specified

| Element described | Status |
|---|---|
| Details taken *"as per the need and the conversation"* — adaptive intake | Neither source describes how intake adapts to what is being said. `[MBU §11.1]` — dimensions named, values absent. **Not evidenced anywhere.** |
| Volunteer receives the case | Volunteer is a recognised actor `[MBU §5]`, but BL V1 states plainly that *"availability, routing, performance… are out of V1 scope"*, and Volunteer Operations is declared-not-specified `[MBU §8.2]` |
| *"Nearest"* beneficiary — dispatch by proximity | Requires operational geolocation and routing. Community context holds settlement type and accessibility `[MBU §4.4]`, not dispatch coordinates. Out of scope as runtime `[MBU §8.3]` |
| Confirming real needs were satisfied | `[MBU §4.9]` outcome model exists, but BL V1 states V1 *"can record that assistance occurred but cannot yet measure whether it worked"* `[MBU §8.2]`. Sector evidence puts this in MEAL, a separate capability `[DD §3, gap 11.9]` — **unresolved** |
| Long-term livelihood support — arrange work, set up businesses | Supported as *concepts*: economic capability `[MBU §4.3]`, livelihood needs `[MBU §4.5]`, livelihood support via skills training and employment linkage `[MBU §4.8]`. **The proactive identification half is excluded — see below.** |

### Excluded by Business Logic V1 §17 — verbatim

| Element described | The exclusion |
|---|---|
| **Verified need appears on the donor side; anyone able to help can help** | *"The donor / resource-supply side and donor–need matching (Khidmat V1 understands beneficiaries; **it is not a donation marketplace**)."* |
| **Matching needs to those who can fund them** | *"Resource allocation and optimisation at scale (future)."* |
| **Facial recognition at the point of visit** | *"Trust-economy scoring, fraud/anomaly engines, and **biometric verification**."* |
| **AI multi-agent system** | *"…any **autonomous multi-agent execution layer**. This repository deliberately stops at the knowledge layer; runtime is designed against it, later."* |
| **Identifying young people who are inactive and have not asked for help** | *"A **predictive/preventive engine** that flags need before any signal exists (V2 horizon)."* Reinforced by BL V1's own scope-honesty note: V1 *"reasons from what is known and stated"* `[MBU §8.4]` |
| **Exact location capture, offline field operation** | *"Runtime and orchestration — payment/escrow, **offline-first field ops**, ID-card/QR credentials…"* |

### Absent from both sources entirely

| Element described | Status |
|---|---|
| **A donor adopting a family or a case** — a sustained, named relationship between a giver and a specific household over time | Appears **nowhere** in Business Logic V1 or the Client First Draft. It is not excluded; it was never contemplated. This is a genuinely new business concept. |

---

## 2. What the pattern shows

The exclusions are not scattered. **They cluster at exactly one seam.**

```
    ┌──────────── Business Logic V1 scope ────────────┐
    registration → evidence → verification → understanding
    → needs → vulnerability → risk → support planning
                                                      │
                                    ═══ THE LINE ═════╡
                                                      │
    donor visibility → matching → giving → adoption → delivery
    → biometric identity → dispatch → multi-agent execution
    └──────── everything the described flow adds ─────┘
```

Business Logic V1 draws its boundary precisely where the described flow reaches its midpoint.
Everything **upstream** of "we now understand this household's verified need" is in scope and
well modelled. Everything **downstream** — who sees the need, who funds it, who delivers it,
how identity is proven biometrically, how agents execute — is excluded.

This is coherent on its own terms. BL V1 calls itself *"a first-generation understanding
layer"* and says so in the same sentence as the exclusions. **It is not an accident or an
oversight. It is the document's thesis.**

The described system is not an understanding layer. It is an **operating system spanning
understanding, matching, giving and delivery** — which is what BL V1 §1 calls Khidmat in its
opening line, and then spends §17 narrowing away from.

**Business Logic V1 contradicts itself on ambition.** §1 promises a Humanitarian Operating
System. §17 delivers a knowledge layer. The Lead's description is of the §1 system. The reset
instruction made §17 binding.

---

## 3. Three consequences that change the next phase

### 3.1 The previous foundation's "error" needs re-reading

The reset triage recorded that the previous work built `giving-resource-origin` and
`resource-logistics` domains **against** BL V1 §17, via an internal decision (CL-002) that
overrode the source. That was recorded as a process failure.

**The process failure was real. The judgement may not have been wrong.**

If the actual business scope includes the donor side — and the description above says it
plainly does — then the previous team was responding to a real requirement. Their error was the
**method**: overriding a supreme document through a downstream internal decision, instead of
saying "the source is out of date, amend the source." Doing it their way meant the contradiction
stayed buried and the foundation drifted.

The correct method is to amend Business Logic V1 at source, with the Lead's authority, and let
everything derive from the amended version. That is what this document exists to trigger.

### 3.2 Domain boundaries cannot be frozen until this is answered

Freezing boundaries **is** the scope decision. If the donor side is in scope, there is at
minimum a giving/resource-origin domain and a matching or allocation concern, and the altitude
split found in `[DD §1]` gets a third altitude — the **giver**, who sits outside both programme
and case altitude and yet constrains both. If it is out of scope, none of those exist.

Those are different ontologies. Not different levels of detail — different ontologies.

### 3.3 Two smaller items that also need a ruling

- **The need categories are a closed list of seven** `[MBU §4.5]`. The description says a need
  *"can be anything."* Either the seven are exhaustive categories that anything maps into, or
  the model needs an open-ended structure. The sources do not say which. This is a modelling
  decision that must be made deliberately, because it determines whether an unanticipated need
  is representable.
- **Facial recognition is excluded and is not a routine exclusion.** BL V1 groups biometric
  verification with fraud engines as *"operational tooling."* But biometric identification of
  vulnerable people — including children and survivors of violence, whom `[MBU §3.2]` names
  explicitly — engages the do-no-harm principle directly, and the ICRC *Handbook on Data
  Protection in Humanitarian Action* already in our evidence base `[DD §3, gap 11.5]` is the
  governing sector guidance. If facial recognition is in scope, it needs a deliberate decision
  with that guidance consulted, not a silent inclusion because it solves the duplicate-identity
  problem `[MBU §11.8]`. Flagging the requirement, not the answer.

---

## 4. The decision — taken

**Outcome: Option C.** The Project Lead directed that a Domain Reference Model be authored
describing humanitarian reality itself, with scope separated into four explicit layers. That
enacts Option C below.

**What it settles:** the donor side, matching, adoption, biometric identity, proactive
identification and multi-agent reasoning are **modelled as humanitarian reality** in the
reference model, and their V1 exclusion is recorded as a build-sequence statement rather than
a claim about the world. Reference model §16.4 tables each with the rulings still outstanding.

The options are retained below as the record of what was chosen over what.

---

**Original framing.** *Only the Project Lead can make this call. It is a scope decision, not a
discovery finding.*

| Option | What it means | Consequence |
|---|---|---|
| **A. Amend Business Logic V1** | The Lead's end-to-end description becomes the scope. §17 is rewritten to move the donor side, matching, adoption, biometric identity and multi-agent execution from "excluded" into scope or into a stated later phase. | The ontology covers the full flow. Larger, and honest about it. The amended BL V1 becomes the authority; everything derives from it. |
| **B. Keep §17 as written** | Khidmat is the understanding layer. The donor side, matching, delivery and execution are **separate systems** that consume Khidmat's output. | The ontology is smaller and sharper. But it does not answer the Lead's "entire project, end to end" instruction, and that gap must be stated to the Lead explicitly rather than discovered later. |
| **C. Amend with staging** | Full flow acknowledged in the ontology; §17 becomes a *sequencing* statement rather than an *exclusion* — donor side and delivery are modelled as reality, built later. | Closest to what the described system needs while preserving BL V1's discipline. The ontology models what is real; the roadmap decides what is built when. |

**Recommendation: C.**

It matches what the evidence already showed. `[DD §4.4]` established via the Core Humanitarian
Standard that donors **are** actors in humanitarian reality, and `[MBU §10.4]` resolved that
*reality-membership does not imply scope-membership*. Option C applies that resolution
correctly: model giving as real, sequence it as later. It is also the only option under which
the described adoption relationship — absent from every document — can be discovered properly
rather than invented.

**Whichever is chosen, it must be recorded as an amendment to Business Logic V1 itself**, not
as a decision in a downstream document. That is the specific failure mode this repository was
reset to escape.

---

## 5. Honest answer to "are we doing this well?"

**Method: yes.** The foundation is now traceable. Every statement cites a source. Six of BL V1's
commitments have external corroboration `[DD §2]`, which is more validation than this project
has ever had. Gaps are recorded as gaps rather than filled with plausible content.

**Coverage of the human-understanding half: strong.** Person, family, household, community,
needs, vulnerability, risk `[MBU §4]` — this is the deepest part of the source and it directly
serves *"the AI should understand the human, person, individual, household."*

**Progress toward an ontology: none yet, by design.** The phase sequence is twelve steps. Three
are complete — merge sources, discover domain knowledge, and now this scope finding. **No
primitive, entity, facet, relationship, state or event has been written**, and none should be
until boundaries are frozen, which this document blocks.

**Maturity: not yet, and two things stand between here and it.**

1. **This scope decision.** Without it, boundaries cannot be frozen, and everything downstream
   inherits the ambiguity.
2. **Tier A practitioner evidence** `[DD §5]`. Nothing in this repository has been checked with
   a humanitarian practitioner. Four gaps will not close without it — vulnerability composition,
   household and family boundaries, identity resolution, and the values inside every dimension.
   BL V1's own operational roles are validated by nothing outside this project.

An ontology built now would be structurally sound and empirically thin. It would look mature
and would not be. **Both blockers require action outside this process** — a ruling from the
Lead, and practitioner access from the client.
