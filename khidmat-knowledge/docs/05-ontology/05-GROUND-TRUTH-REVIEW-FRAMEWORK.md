# 5 — Ground Truth Review Framework

**Ontology Design, step 5 of 7.** Status: **Framework established — zero reviews conducted.**

Derived from `01-DOMAIN-PRIMITIVES.md`, `02-ONTOLOGY-LAYERS.md`, `03-ONTOLOGY-PILLARS.md`,
`04-ARCHITECTURE-RULES.md`, and `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md`.

---

## 0. What this document is

This document defines **how** Ground Truth Reviews are conducted. It contains no review
results. As of this writing, **zero practitioner reviews have been performed.** Every
`Status` field in `05-GROUND-TRUTH-REVIEW-MATRIX.md` reads `NOT YET REVIEWED`, and every
`05-GROUND-TRUTH-REVIEW-RECORD-TEMPLATE.md` instance is blank until a real practitioner
completes one.

**Why this distinction matters.** README's Standing Rule 1 states that no document becomes
authoritative by being written. A review *template* is not a *finding*. A *question* is not
an *answer*. This framework exists to make genuine ground-truth collection possible; it does
not simulate, anticipate, or pre-populate what that collection will show.

---

## 1. Purpose

Stages 1–4 produced the current ontology structure, subsequently formalized and governed through Stage 7 rulings G1, G2, and G3 (see `docs/05-ontology/07-STAGE-7-GOVERNANCE-DECISIONS.md`). The ontology is baselined and architecture-ready; CCR-7 remains explicitly unresolved and non-blocking under G2. This structure was built entirely from two authoritative
business documents and six evidence dossiers whose Tier B/D sources describe *sector
institutions*, not *lived humanitarian casework*. `01-DOMAIN-PRIMITIVES.md` §7.1 records this
asymmetry directly: the primitives carrying the human side of the domain — Condition and
Relation — rest on Business Logic V1 alone, with zero external corroboration.

Stage 5 exists to close that gap **honestly** — by collecting real practitioner ground truth
against the ontology as it currently stands, not by inventing an approximation of what that
ground truth might say.

Stage 5 is a **validation layer**. It tests the existing seven primitives, eight layers, seven
pillars, and architecture rules against real humanitarian practice, and it prioritizes the
already-named `[OPEN]` questions in `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md`. It does not
redesign the foundation, and it does not close an open question merely because one practitioner
answered it once.

---

## 2. Authority position of Stage 5 evidence

| Tier | Role |
|---|---|
| **Tier 1** — `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, `KHIDMAT_AI_BUSINESS_OVERVIEW.html`, `docs/01-evidence/` | Sources of fact. Unchanged by Stage 5. |
| **Tier 2** — `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | Source of derivation. Unchanged by Stage 5. |
| **Ground-truth evidence (this stage)** | Real, but **not Tier 1**. A completed review record is evidence to be weighed, cited, and carried into Stage 6 (Evidence) and Stage 7 (Governance) — it does not silently amend Tier 1 or Tier 2, and it does not overwrite `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md` on its own authority. |

A finding that contradicts the Reference Model is not "wrong by definition" — it is exactly the
kind of signal Stage 5 exists to surface. But per README's Standing Rule 1, only an explicit
amendment to a Tier 1 source, followed by re-derivation, changes what the ontology asserts. A
Ground Truth Review record documents the contradiction; it does not resolve it.

---

## 3. Two-dimensional review structure

### 3.1 Structural ontology review

Tests whether the seven primitives, eight layers, seven pillars, and architecture rules hold up
against real cases, independent of any specific open question:

- **Primitives** — does every humanitarian concept a practitioner describes classify without
  forced fit into Condition, Context, Epistemic Stance, Entity, Norm, Occurrence, or Relation?
- **Layers** — does real casework produce content that fits Facets, Entities, Relationships,
  Constraints, States, Events, Cognition, and Coordination without contorting the concept?
- **Pillars** — do the seven pillars (Human & Social Subject; Context & Environment;
  Vulnerability & Need; Epistemics & Knowledge; Actors & Ecosystem; Action & Coordination;
  Resources & Support) cover what a practitioner actually encounters, without becoming an
  organizational-process map (README Standing Rule 4)?
- **Architecture Rules** — do the CCR/PIR/LCR/PBR/UHR rules in `04-ARCHITECTURE-RULES.md`
  produce sensible outcomes when applied to a real situation, or does a real case break one?

### 3.2 Targeted open-question review

Prioritizes the specific `[OPEN]` items already named in `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md`
and `03-ONTOLOGY-PILLARS.md` §8.2 / `04-ARCHITECTURE-RULES.md` §7.1. These are listed with their
existing identifiers in `05-GROUND-TRUTH-REVIEW-MATRIX.md` §2. No new open question is invented
here merely to enlarge Stage 5's scope; if a genuinely new gap surfaces during review, it is
logged as a new item with its own ID, not folded into an existing one.

---

## 4. Rules for question design

**R-1 — Reality before ontology.** Every question asks the practitioner to describe how
something actually works, before any ontology term is introduced. The mapping to a primitive,
layer, or pillar happens afterward, by the reviewer, not by the practitioner.

**R-2 — No leading questions.** A question must not disclose or imply the ontology's current
answer. "In humanitarian operations, how do X actually participate?" is admissible. "Do you
agree X should be classified as Y?" is not.

**R-3 — Answer space includes disagreement and non-resolution.** Every question's response
options must include, at minimum: Yes / No / Partially / Context-dependent / Different
distinction needed / Missing concept / Cannot determine. A binary-only question is a defect in
the instrument, not a defect in the practitioner's answer.

**R-4 — One question, one concept.** A question that bundles two ontology tensions (e.g., Risk
placement and Need placement together) is split before use, so a finding can be traced to
exactly one Review ID.

**R-5 — Context is captured, not assumed.** Every response records the practitioner's
operating context (geography, mandate, organization type, sector) alongside the answer, because
`CCR-1` (altitude qualification) and multiple Reference Model findings establish that
humanitarian practice varies structurally by scope.

---

## 5. Rules for recording findings

**F-1 — Domain reality vs. organizational practice vs. local practice vs. ontology implication.**
Every record separates these four explicitly (see `05-GROUND-TRUTH-REVIEW-RECORD-TEMPLATE.md`
§4). A single organization's convention is not, by itself, evidence of universal humanitarian
reality.

**F-2 — Disagreement is preserved, not averaged.** Where two practitioners answer the same
Review ID differently, both responses are recorded as separate entries against the same Review
ID, with their contexts intact. No entry synthesizes a "consensus" unless the practitioners
themselves converged.

**F-3 — A single response does not close an open question.** `UNRESOLVED` is not a failure
state; it is the correct classification whenever the accumulated evidence for a Review ID is
insufficient to support `CONFIRMED`, `CHALLENGED`, `REFINED`, or `MISSING`. Closing an
open question (per `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md`) requires an explicit governance
decision at Stage 7, informed by — but not automatically triggered by — Stage 5 findings.

**F-4 — Finding classification is fixed vocabulary.** Reviewers select from exactly the seven
values defined in §6 below. No ad hoc classification is introduced.

**F-5 — No later-phase content.** A Ground Truth Review record never proposes a database
schema, an API, a data model, a taxonomy value set, or an implementation detail. If a
practitioner volunteers one, it is recorded verbatim in the `Evidence / response` field as
color, not adopted into the `Finding` or `Implication for ontology` fields.

---

## 6. Finding classification vocabulary

| Value | Definition |
|---|---|
| `CONFIRMED` | The practitioner evidence supports the current structural interpretation as stated in Stages 1–4. |
| `CHALLENGED` | The practitioner evidence conflicts materially with the current structural interpretation. |
| `REFINED` | The structural interpretation is broadly valid but requires a stated qualification, boundary, or exception. |
| `MISSING` | A meaningful humanitarian concept, distinction, or relationship appears absent from the current ontology. |
| `CONTEXT_DEPENDENT` | The correct representation legitimately varies by geography, mandate, or operating context, and no single answer generalizes. |
| `UNRESOLVED` | Available practitioner evidence is insufficient — in volume, consistency, or specificity — to support any of the above. |
| `NOT_ASSESSABLE` | The selected practitioner or context cannot meaningfully answer this particular question (e.g., outside their domain of practice). |

A record may carry only one classification. Where a single reviewer's evidence plausibly
supports two classifications (e.g., `REFINED` and `CONTEXT_DEPENDENT`), the reviewer states
both readings in `Reviewer reasoning` and selects the classification that dominates, flagging
the ambiguity in `Follow-up requirement`.

---

## 7. Traceability chain

Every review question must be traceable in both directions:

```
Stage 5 Review ID
      ↓ / ↑
Ontology element (primitive / layer / pillar / architecture rule)
      ↓ / ↑
Stage 1–4 artifact (with section citation)
      ↓ / ↑
Reference Model section
      ↓ / ↑
Tier 1 source (Business Logic V1 §n, Client Draft section, or TD-0n finding)
```

Where the review targets a named open question (e.g., Q1–Q19 in
`PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md`, or an item in `03-ONTOLOGY-PILLARS.md` §8.2), the
existing identifier is carried forward unchanged, never re-numbered.

---

## 8. What Stage 5 does not do

- It does not modify `01-DOMAIN-PRIMITIVES.md`, `02-ONTOLOGY-LAYERS.md`,
  `03-ONTOLOGY-PILLARS.md`, `04-ARCHITECTURE-RULES.md`, or
  `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md`, unless a review surfaces an outright logical
  contradiction that makes the existing foundation internally impossible to apply — in which
  case the contradiction is documented separately (per the parent task's §19) and reported, not
  silently patched.
- It does not modify any Tier 1 or Tier 2 source.
- It does not introduce an eighth primitive, a ninth layer, or an eighth pillar. A candidate for
  any of these is escalated per `PIR-5` (`04-ARCHITECTURE-RULES.md` §4.1), not adopted here.
- It does not produce schemas, APIs, data models, or any implementation artifact.
- It does not fabricate practitioner evidence, findings, consensus, or field observations of any
  kind.

---

## 9. Status

**Framework: established.** Review matrix: populated with review items, all `NOT YET REVIEWED`.
Record template: defined, blank. **Zero Ground Truth Reviews have been conducted.** This
document, the matrix, and the template together constitute a **review system ready to receive
genuine ground-truth evidence** — not a review result.
