# 5 — Ground Truth Review Record: GT-OQ19-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ19-R1 |
| **Review ID (from matrix)** | GT-OQ19 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Case Coordination/Orchestration capability status |
| **Ontology layer(s)** | Coordination Pattern (L8) |
| **Ontology pillar(s)** | N/A |
| **Current structural position** | Genuinely open — Coordination Pattern (L8), stub extension point |
| **Open question reference, if any** | GT-OQ19 / Q19 |
| **Upstream citation chain** | `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "Is there a distinct role or function in your operating environment that exists solely to coordinate a complex case across multiple different organizations, separate from the case manager who is delivering direct support?" |
| **Reviewer role** | Programme Management & Coordination Practitioner |
| **Humanitarian context** | Broad programme coordination and ecosystem |
| **Evidence / response** | "Yes. Complex cases can require coordination across multiple organisations and services... coordination can also involve a separate function or role when several organisations, referrals, services, or support streams are involved. The coordination function is responsible for helping the different parties work together, tracking referrals or handoffs, identifying gaps or duplication, and following up on actions across organisations. This coordination function is distinct from the actual service delivery performed by each organisation. However, the exact staffing arrangement can vary. In a smaller operation, the same person may perform both case-management and coordination responsibilities. What is distinct is the coordination function, not necessarily a universally separate job title or employee." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | REFINED |
| **Reviewer reasoning** | The practitioner answered the open question regarding the validity of a "Case Orchestration" stub extension. They confirmed that cross-organizational case coordination is an operationally distinct function (tracking handoffs, gaps, duplication) fundamentally separate from direct service delivery, even if the same employee occasionally performs both. |
| **Implication for ontology** | The stub extension point for Case Orchestration is valid and necessary. It should be modeled as a distinct Coordination Pattern managing the broader case timeline across multiple organizational boundaries. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Complex cases require an orchestration function to track multi-org referrals and prevent service gaps, functioning distinctly from direct assistance provision. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The ontology must architecturally separate the tracking/orchestration of a case from the individual action/service events within that case. |

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
