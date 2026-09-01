# 5 — Ground Truth Review Record: GT-OQ5-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ5-R1 |
| **Review ID (from matrix)** | GT-OQ5 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Outcome / Impact ownership |
| **Ontology layer(s)** | States (L5) + Events (L6) |
| **Ontology pillar(s)** | VI — Action & Coordination |
| **Current structural position** | States (L5) + Events (L6); operational ownership `pending` |
| **Open question reference, if any** | GT-OQ5 / Q5 |
| **Upstream citation chain** | `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "Describe a case where the administrative step of 'closing the case' and the actual measurement of 'did the assistance work' were tracked differently. Are these always handled by the same person on the same timeline, or do you have a separate process for measuring the actual outcome/impact?" |
| **Reviewer role** | MEAL / Information Management Practitioner |
| **Humanitarian context** | Broad field operations and casework |
| **Evidence / response** | "Yes. In actual casework, closing a case and determining whether the assistance achieved its intended outcome are separate activities... Outcome measurement can happen separately through follow-up, monitoring, reassessment, beneficiary feedback, verification, or MEAL activities. The person responsible for the case may be different from the person or team responsible for monitoring the outcome... The outcome should therefore be represented separately from the administrative state of the case, including information about what was intended, what was observed or measured, when it was assessed, and who or what source provided the assessment." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | REFINED |
| **Reviewer reasoning** | The open question regarding who "owns" outcomes and how they relate to the case timeline is resolved by separating them. The practitioner clarified that outcomes are separate assessments owned by different roles (often MEAL) on different timelines, independent of the administrative "case closed" event. |
| **Implication for ontology** | Outcome ownership should be explicitly assigned to the States layer (L5) rather than the case Events layer (L6), requiring its own distinct Epistemic Stance and source attribution (e.g., who measured the outcome and when). |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Outcome assessment is a distinct operational process from case management, often requiring post-assistance verification. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | Outcomes must be modeled as empirical states assessed independently of the case administrative lifecycle. |

---

## 5. Disagreement handling

| Field | Value |
|---|---|
| **Prior Record ID(s) on the same Review ID** | None |
| **Where they agree** | |
| **Where they disagree** | |
| **Is the disagreement contextual?** | |
| **Further evidence needed?** | |

---

## 6. Follow-up

| Field | Value |
|---|---|
| **Follow-up requirement** | sufficient — no further evidence needed for this Review ID |
| **Carried to** | Stage 6 (Evidence) |
