# 5 — Ground Truth Review Record Template

**Ontology Design, step 5 of 7.** Status: **Template only — contains no completed records.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`. Every field below is blank or holds an
instruction in *italics*. Copy this template once per completed practitioner review and fill it
in with real evidence. **Do not fill in a copy of this file with invented, hypothetical, or
"illustrative" content.** An empty, honestly-blank record is worth more to this project than a
plausible-looking fabricated one — see `README.md` Standing Rule 1 and 2.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | *e.g., GT-P7-R1 — the Review ID from the matrix, plus a sequence number if more than one practitioner responds to the same Review ID* |
| **Review ID (from matrix)** | *copy exactly from `05-GROUND-TRUTH-REVIEW-MATRIX.md`* |
| **Date recorded** | *ISO date* |
| **Recorded by** | *the person who conducted/transcribed the review, not the practitioner* |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | *primitive / layer / pillar / architecture rule name* |
| **Ontology layer(s)** | |
| **Ontology pillar(s)** | |
| **Current structural position** | *copy from the matrix — the ontology's existing answer, so the practitioner's answer can be compared against it afterward, never shown to the practitioner beforehand (Framework R-2)* |
| **Open question reference, if any** | *e.g., Q2 / GT-OQ2* |
| **Upstream citation chain** | *Stage 1–4 artifact → Reference Model section → Tier 1 source, per Framework §7* |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | *verbatim, in the practitioner's language if translated* |
| **Reviewer role** | *e.g., field case worker, programme manager, community liaison — role only, not identifying detail unless the practitioner has consented to attribution* |
| **Humanitarian context** | *geography, sector/mandate, organization type, scale of operation, urban/rural, acute/chronic setting — per Framework R-5* |
| **Evidence / response** | *the practitioner's answer, as given. Direct quotation where useful; paraphrase where lengthy. Include anything volunteered beyond the question — do not trim color that might matter later (Framework F-5 governs where volunteered implementation detail goes: recorded here, never promoted into Finding or Implication).* |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | *exactly one of: CONFIRMED / CHALLENGED / REFINED / MISSING / CONTEXT_DEPENDENT / UNRESOLVED / NOT_ASSESSABLE — see Framework §6 for definitions* |
| **Reviewer reasoning** | *why this classification was chosen, referencing the specific evidence above. If more than one classification was plausible, say so explicitly.* |
| **Implication for ontology** | *what, if anything, this suggests for the primitive/layer/pillar/rule under review — stated as a possibility to weigh at Stage 6/7, never as an enacted change* |

---

## 4. Domain reality vs. practice (Framework F-1 — fill in whichever apply; leave the rest blank rather than guessing)

| Field | Value |
|---|---|
| **Humanitarian domain reality** (what appears to be true of humanitarian work generally, beyond this practitioner's organization) | |
| **Organizational practice** (specific to this practitioner's organization's own conventions) | |
| **Local/contextual practice** (specific to this country, programme, or operating environment) | |
| **Ontology implication** (what the evidence, once separated into the above, means for the ontology — may be much narrower than the raw response suggested) | |

---

## 5. Disagreement handling (only if this Record responds to a Review ID with an existing, differing Record)

| Field | Value |
|---|---|
| **Prior Record ID(s) on the same Review ID** | |
| **Where they agree** | |
| **Where they disagree** | |
| **Is the disagreement contextual?** (i.e., explainable by different operating contexts, per Framework R-5) | Yes / No / Unclear |
| **Further evidence needed?** | Yes / No — and what kind |

*Per Framework F-2, do not average or synthesize a single answer across disagreeing records.
Both stand.*

---

## 6. Follow-up

| Field | Value |
|---|---|
| **Follow-up requirement** | *e.g., "needs a second independent practitioner in a different geography," "needs Stage 7 governance ruling," "sufficient — no further evidence needed for this Review ID"* |
| **Carried to** | *Stage 6 (Evidence) / Stage 7 (Governance) / left open pending further Stage 5 collection* |

---

## Usage notes

1. One completed copy of this template = one Record. Multiple practitioners answering the same
   Review ID = multiple Records, cross-referenced via §5, never merged into one.
2. A Record with an empty §2 "Evidence / response" field is not a Record — it is an unused
   template and should not be checked in as if it were evidence.
3. When a Record is completed, update the corresponding row's `Status` in
   `05-GROUND-TRUTH-REVIEW-MATRIX.md` from `NOT YET REVIEWED` to the Finding classification
   reached (or, if evidence is still accumulating for that Review ID, leave it at
   `NOT YET REVIEWED` until at least one full Record exists, then move to the classification).
4. No Record may be used to directly edit `01-DOMAIN-PRIMITIVES.md`, `02-ONTOLOGY-LAYERS.md`,
   `03-ONTOLOGY-PILLARS.md`, `04-ARCHITECTURE-RULES.md`, or
   `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md`. Findings are carried forward into Stage 6
   (Evidence) and resolved, if at all, at Stage 7 (Governance).
