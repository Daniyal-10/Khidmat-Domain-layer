# 5 — Ground Truth Review Record: GT-OQ12-R1

**Ontology Design, step 5 of 7.**

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ12-R1 |
| **Review ID (from matrix)** | GT-OQ12 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | Antigravity AI |

---

## 1. Traceability

| Field | Value |
|---|---|
| **Ontology element under review** | Missing information representation mechanism |
| **Ontology layer(s)** | Cognition |
| **Ontology pillar(s)** | IV — Epistemics & Knowledge |
| **Current structural position** | Open-world commitment established; representation mechanism `[OPEN]` |
| **Open question reference, if any** | Q12 / GT-OQ12 |
| **Upstream citation chain** | Stage 1–4 artifact → Reference Model section → Tier 1 source |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | What practical mechanism, field, or process do you use to show this distinction? What happens if a field is simply left blank? |
| **Reviewer role** | Humanitarian practitioner |
| **Humanitarian context** | Unspecified |
| **Evidence / response** | "the implementation should preferably use explicit epistemic values such as: Yes, No, Unknown, Not assessed, Not applicable... A blank field means that the information has not been recorded yet... an assessment/value should therefore be able to carry both the observed value and its information status rather than relying only on whether a field contains a value... the system should preserve the distinction between a recorded negative observation and absence of information rather than using the presence or absence of a value alone to determine truth." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | REFINED |
| **Reviewer reasoning** | The open question was "how to represent missing info." The practitioner resolved this by defining the mechanism: data structures must couple the value with an explicit categorical "information status" field (e.g., Unknown, Not Assessed, Yes, No) rather than inferring epistemic state from null or blank fields. |
| **Implication for ontology** | Resolves Q12 by explicitly mandating that data structures carry a dedicated epistemic status property. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | |
| **Organizational practice** | Using explicit status fields (Yes, No, Unknown) rather than interpreting empty database fields as negative facts. |
| **Local/contextual practice** | |
| **Ontology implication** | Resolves Q12 by defining the representation mechanism as explicit epistemic status flags. |

---

## 5. Disagreement handling

| Field | Value |
|---|---|
| **Prior Record ID(s) on the same Review ID** | |
| **Where they agree** | |
| **Where they disagree** | |
| **Is the disagreement contextual?** | |
| **Further evidence needed?** | |

---

## 6. Follow-up

| Field | Value |
|---|---|
| **Follow-up requirement** | sufficient — no further evidence needed for this Review ID. |
| **Carried to** | Stage 6 (Evidence) |
