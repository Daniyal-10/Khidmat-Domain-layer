# 5 — Ground Truth Review Record: GT-OQ8-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ8-R1 |
| **Review ID (from matrix)** | GT-OQ8 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Funding restrictions |
| **Ontology layer(s)** | Constraints |
| **Ontology pillar(s)** | N/A |
| **Current structural position** | Constraint/Norm (P5); restriction taxonomy absent |
| **Open question reference, if any** | GT-OQ8 / Q8 |
| **Upstream citation chain** | `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "What specific kinds of restrictions have you seen donors attach to funding? (For instance, restrictions based on geography, specific sectors, types of populations, or time limits?)" |
| **Reviewer role** | Programme Management & Coordination Practitioner |
| **Humanitarian context** | Broad programme coordination and context assessment |
| **Evidence / response** | "Donor funding can have restrictions on how support is used. These can include geographic restrictions, target-population restrictions, specific sectors or types of assistance, eligible activities or expenses, funding periods or deadlines, and reporting requirements. For example, a donor may fund assistance for a particular population or location and only for specific types of support during a defined funding period. A beneficiary may have a genuine need outside those restrictions, but that does not automatically mean the donor-funded programme can provide that support. In that situation, the need still exists and should not be confused with programme eligibility. The practitioner may need to identify another appropriate programme, funding source, or referral rather than treating the person as having no need." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | REFINED |
| **Reviewer reasoning** | The practitioner confirmed that funding restrictions act as independent bounding rules (`Norms`) and provided the specific operational taxonomy that was previously absent (geography, target population, sector, eligible activities, time periods). They also reinforced that these constraints do not negate the underlying empirical need. |
| **Implication for ontology** | Funding restrictions should be modeled using the `Norm` primitive, parameterized by the provided taxonomy (geography, population, sector, time). |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Funding restrictions tightly bound assistance eligibility independently of the existence of a human need. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The constraint taxonomy must explicitly support geographic, demographic, sectoral, and temporal bounding rules. |

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
