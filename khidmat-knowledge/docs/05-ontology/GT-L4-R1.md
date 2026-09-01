# 5 — Ground Truth Review Record: GT-L4-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-L4-R1 |
| **Review ID (from matrix)** | GT-L4 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Constraints |
| **Ontology layer(s)** | Constraints |
| **Ontology pillar(s)** | N/A |
| **Current structural position** | Structural feature that must represent conflicting rules without resolving them away |
| **Open question reference, if any** | |
| **Upstream citation chain** | `02-ONTOLOGY-LAYERS.md` -> `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "What kind of operational rules or constraints strictly bind your casework, regardless of what the individual beneficiary needs (e.g., eligibility cutoffs, safeguarding rules, reporting mandates)? Can you describe a real situation where two of these rules pulled you in opposite directions (like a donor reporting requirement clashing with a family's preference for privacy)? How did you handle that clash?" |
| **Reviewer role** | Programme Management & Coordination Practitioner |
| **Humanitarian context** | Broad programme coordination and context assessment |
| **Evidence / response** | "These rules can sometimes conflict with each other or with the beneficiary's preferences. For example, a programme may require certain information to be collected for eligibility or reporting, while the beneficiary may not want that information shared beyond the people directly handling the case. In such situations, the practitioner cannot simply ignore either requirement... If the conflict cannot be resolved within the applicable rules, the matter is escalated to the responsible supervisor or appropriate authority rather than allowing an individual worker or system to silently override the constraint." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | CONFIRMED |
| **Reviewer reasoning** | The practitioner confirmed that overlapping rules frequently clash in practice, and that these clashes must not be silently overridden by a system or worker. Instead, they must be recognized and escalated. This validates the design of the Constraints layer, which requires representing conflicting norms explicitly. |
| **Implication for ontology** | The Constraints layer must support concurrent, conflicting `Norm` entities and provide a mechanism to surface these conflicts for human resolution. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Competing operational rules are a fundamental reality of casework and require human judgement to resolve. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The system architecture must not attempt to automatically "solve" normative conflicts via arithmetic; it must intentionally preserve the clash. |

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
