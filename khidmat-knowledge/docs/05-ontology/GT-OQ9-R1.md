# 5 — Ground Truth Review Record: GT-OQ9-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ9-R1 |
| **Review ID (from matrix)** | GT-OQ9 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Risk classification |
| **Ontology layer(s)** | Condition (P1) |
| **Ontology pillar(s)** | III — Vulnerability & Need |
| **Current structural position** | Condition (P1) — structurally resolved |
| **Open question reference, if any** | GT-OQ9 / Q9 |
| **Upstream citation chain** | `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "When a household is identified as being 'at risk', how is that actually recorded in your data? Does treating 'at risk' as an ongoing, continuing fact about the household (similar to a health condition) match how you use the term in practice, or is it treated differently?" |
| **Reviewer role** | MEAL / Information Management Practitioner |
| **Humanitarian context** | Broad field operations and casework |
| **Evidence / response** | "Yes. When a household is identified as being at risk, that risk can represent an ongoing condition rather than only a single event... A household can therefore move from at risk → reduced risk → no longer identified as at risk, or a different risk can emerge later. The original assessment or identification should remain available where historical tracking is required... The exact risk categories, thresholds, and assessment methods may vary by programme or context. 'At risk' should therefore not automatically be interpreted as a universal numerical classification across all programmes." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | CONFIRMED |
| **Reviewer reasoning** | The practitioner used the exact phrasing of the primitive ("ongoing condition") to describe risk. They explicitly confirmed that risk persists, changes over time, and requires both a current state and a history of previous assessments, perfectly validating the proposed structural resolution mapping Risk to the Condition primitive (P1). |
| **Implication for ontology** | Confirms that Risk should remain structurally modeled as a `Condition` (P1) shaped by `Context` (P2), rather than as an Occurrence/Event. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Risk is a persistent, changeable condition whose thresholds vary by programme and context. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | Risk must be implemented using the Condition primitive, preserving history and context, not as a universal scalar value or an instantaneous event. |

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
