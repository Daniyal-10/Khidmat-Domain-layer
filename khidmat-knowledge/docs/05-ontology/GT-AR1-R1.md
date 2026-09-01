# 5 — Ground Truth Review Record: GT-AR1-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-AR1-R1 |
| **Review ID (from matrix)** | GT-AR1 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | CCR-1 — Altitude qualification |
| **Ontology layer(s)** | Architecture Rules |
| **Ontology pillar(s)** | N/A |
| **Current structural position** | Architecture rule prohibiting the conflation of case-level and programme-level activities sharing the same name. |
| **Open question reference, if any** | |
| **Upstream citation chain** | `04-ARCHITECTURE-RULES.md` (CCR-1) -> `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "In your work, have you ever seen terms like 'needs assessment', 'planning', or 'coordination' used to mean two genuinely different things depending on whether the speaker was talking about an individual person's case versus talking about a broader population-level programme? Can you describe how the activities actually differ?" |
| **Reviewer role** | Programme Management & Coordination Practitioner |
| **Humanitarian context** | Broad programme coordination and context assessment |
| **Evidence / response** | "Yes. In practice, terms such as needs assessment, planning, monitoring, and coordination can refer to different activities depending on whether they concern an individual case or a broader programme/population. At the individual case level, a needs assessment is concerned with understanding the circumstances and needs of a particular person... At a programme or population level, assessment is broader... identifying patterns of need across many households... planning at programme level concerns things such as programme objectives, eligibility criteria... rather than the action plan for one individual household... Therefore, the same word does not necessarily represent the same operational activity. The scope and subject of the activity matter. The system should not assume that a case-level assessment and a programme-level assessment are the same record simply because both are called an 'assessment.'" |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | CONFIRMED |
| **Reviewer reasoning** | The practitioner explicitly confirmed that identical terms (assessment, planning, coordination, monitoring) represent fundamentally different operational activities depending on whether their scope is an individual case or a population/programme. This exactly validates the premise of CCR-1. |
| **Implication for ontology** | Confirms CCR-1 (Altitude qualification) as a critical structural requirement. The ontology must explicitly type activities by their altitude to prevent conflation. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Operational activities are strongly segregated by altitude (case-level vs population/programme-level), despite sharing terminology. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The data architecture must not merge case-level and programme-level actions into universal generic entities. |

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
