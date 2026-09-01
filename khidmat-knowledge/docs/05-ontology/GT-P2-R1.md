# 5 — Ground Truth Review Record: GT-P2-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-P2-R1 |
| **Review ID (from matrix)** | GT-P2 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Context |
| **Ontology layer(s)** | Facets, scopes, Constraints |
| **Ontology pillar(s)** | II — Context & Environment |
| **Current structural position** | "The frame relative to which a statement holds" — RM §2.2, §5, §11.4 |
| **Open question reference, if any** | |
| **Upstream citation chain** | `01-DOMAIN-PRIMITIVES.md` -> `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "When you assess that a certain condition is true for a household (for example, that they have a specific need or a damaged roof), can you give a real example of where that exact same physical condition meant something completely different depending on the location, the season, or the specific programme evaluating it?" |
| **Reviewer role** | Programme Management & Coordination Practitioner |
| **Humanitarian context** | Broad programme coordination and context assessment |
| **Evidence / response** | "Yes. In actual humanitarian work, the same physical or observed condition can have different meanings depending on the location, season, household circumstances, and programme context... A damaged roof in an area experiencing heavy monsoon rainfall may create an immediate shelter and safety need. The same degree of roof damage in a dry season or a different climate may represent a less urgent need. Similarly, the same household condition can be assessed differently by different programmes because their eligibility criteria, objectives, available support, and thresholds may differ. Context therefore affects the meaning, severity, urgency, relevance, and response associated with a condition. The underlying physical observation should not be silently changed simply because the context changes... A condition can remain factually the same while its practical significance changes because the surrounding context changes." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | CONFIRMED |
| **Reviewer reasoning** | The practitioner confirmed that the factual condition (e.g., damaged roof) exists independently, but its operational meaning, severity, and resulting need are strictly determined by the context (season, geography, programme). This exactly matches the primitive definition of Context as the frame relative to which a statement holds. |
| **Implication for ontology** | Confirms the structural separation of `Condition` and `Context`. The system must permit multiple different needs or assessments to be derived from a single condition based on varying contexts. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | The meaning, urgency, and programmatic relevance of an observed condition are relative to the context in which it occurs. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | Factual condition observations must not be silently overwritten or altered when a new programme assesses them; instead, a new contextual assessment should be linked to the same underlying condition. |

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
