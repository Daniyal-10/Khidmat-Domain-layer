# 5 — Ground Truth Review Record: GT-P5-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-P5-R1 |
| **Review ID (from matrix)** | GT-P5 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Norm |
| **Ontology layer(s)** | Constraints |
| **Ontology pillar(s)** | N/A |
| **Current structural position** | "That which bounds what is permitted, required, or valid" — RM §3.7, §10.6, §12.2, §13.4, §16.4 |
| **Open question reference, if any** | |
| **Upstream citation chain** | `01-DOMAIN-PRIMITIVES.md` -> `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "What kind of operational rules or constraints strictly bind your casework, regardless of what the individual beneficiary needs (e.g., eligibility cutoffs, safeguarding rules, reporting mandates)? Can you describe a real situation where two of these rules pulled you in opposite directions (like a donor reporting requirement clashing with a family's preference for privacy)? How did you handle that clash?" |
| **Reviewer role** | Programme Management & Coordination Practitioner |
| **Humanitarian context** | Broad programme coordination and context assessment |
| **Evidence / response** | "Yes. Our casework is subject to operational rules and constraints that apply independently of what a beneficiary needs. These can include programme eligibility criteria, donor restrictions, safeguarding requirements, consent and privacy requirements, geographic or population restrictions, documentation requirements, and reporting requirements. These rules can sometimes conflict with each other or with the beneficiary's preferences... the practitioner cannot simply ignore either requirement. We follow the applicable safeguarding, consent, privacy, programme, and reporting requirements and use practitioner judgement to determine what can legitimately be done. If the conflict cannot be resolved within the applicable rules, the matter is escalated to the responsible supervisor or appropriate authority rather than allowing an individual worker or system to silently override the constraint." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | CONFIRMED |
| **Reviewer reasoning** | The practitioner explicitly confirmed that casework is governed by independent operational rules (eligibility, safeguarding, donor restrictions) that bound action regardless of beneficiary need. This perfectly validates the primitive definition of `Norm`. |
| **Implication for ontology** | Confirms the structural validity of the `Norm` primitive as an independent entity bounding operations. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Practice is constrained by overlapping, independent rule sets that dictate what actions are valid. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The ontology must explicitly model `Norm` independent of `Condition`, ensuring rules are evaluated separately from empirical facts. |

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
