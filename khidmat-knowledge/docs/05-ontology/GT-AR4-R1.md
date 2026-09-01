# 5 — Ground Truth Review Record: GT-AR4-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-AR4-R1 |
| **Review ID (from matrix)** | GT-AR4 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | CCR-5 — Human-oversight trigger |
| **Ontology layer(s)** | Events / Architecture Rules |
| **Ontology pillar(s)** | VI — Action & Coordination |
| **Current structural position** | Architecture rule that consequential decisions require human oversight and cannot be fully automated. |
| **Open question reference, if any** | |
| **Upstream citation chain** | `04-ARCHITECTURE-RULES.md` (CCR-5) -> `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "In your casework, which specific decisions or actions strictly require a human practitioner to review and approve them? Are there scenarios where a system calculation, formula, or junior assessment is explicitly not trusted to make the final determination?" |
| **Reviewer role** | MEAL / Information Management Practitioner |
| **Humanitarian context** | Broad field operations and casework |
| **Evidence / response** | "Certain decisions in humanitarian casework require human judgement and should not be left entirely to an automated calculation or system rule. This is particularly important when a decision can materially affect a person's access to assistance, eligibility, protection, safety, dignity, or case status. A system may calculate scores, identify possible matches, apply programme rules, or highlight cases for attention, but these outputs should support the practitioner rather than automatically replace the practitioner's judgement where the situation is uncertain, sensitive, exceptional, or consequential. Examples include: deciding whether a person genuinely requires assistance; interpreting conflicting or incomplete evidence; assessing unusual or exceptional circumstances; making sensitive protection or safeguarding decisions; determining an appropriate intervention when several needs interact; reviewing an uncertain automated match or classification; approving a consequential case decision. When the available information is uncertain or contradictory, the system should surface the issue to a human rather than silently making an irreversible decision. The final decision should remain attributable to the responsible practitioner or authorised decision-maker where human judgement is required." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | CONFIRMED |
| **Reviewer reasoning** | The practitioner exactly described the premise of CCR-5, detailing that automated systems should only support the practitioner and must not replace human judgement for consequential, sensitive, or uncertain decisions. The requirement to attribute the final decision to a human was explicitly validated. |
| **Implication for ontology** | Confirms CCR-5 (Human-oversight trigger) as a structural requirement. The ontology must support capturing human attribution for consequential case events. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | High-consequence decisions involving eligibility, protection, and uncertainty inherently require human judgement and attribution. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The architecture must distinguish between automated system calculations/beliefs and human-authorized decisions. |

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
