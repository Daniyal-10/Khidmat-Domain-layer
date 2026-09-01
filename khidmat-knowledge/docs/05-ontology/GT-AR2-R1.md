# 5 — Ground Truth Review Record: GT-AR2-R1

**Ontology Design, step 5 of 7.**

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-AR2-R1 |
| **Review ID (from matrix)** | GT-AR2 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | Antigravity AI |

---

## 1. Traceability

| Field | Value |
|---|---|
| **Ontology element under review** | Non-linearity |
| **Ontology layer(s)** | N/A (Architecture Rule) |
| **Ontology pillar(s)** | N/A |
| **Current structural position** | CCR-6 (Non-linearity) |
| **Open question reference, if any** | N/A |
| **Upstream citation chain** | Stage 1–4 artifact → Reference Model section → Tier 1 source |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | In your actual work, can a case move backward or return to an earlier situation? How often does this happen in practice? When it happens, do you create a new case, reopen the previous case, or handle it in some other way? |
| **Reviewer role** | Humanitarian practitioner |
| **Humanitarian context** | Unspecified |
| **Evidence / response** | "Cases are not always completely linear... A person's need can be resolved and later return. A beneficiary can become inactive... and later become active again... A referral may also fail... The case therefore does not necessarily progress through one fixed sequence... the same person can have multiple periods of assistance or multiple engagements over time... In some situations, the existing beneficiary history is retained and the person's administrative status is updated... In other situations, a programme may create a new case or intervention record." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | CONFIRMED |
| **Reviewer reasoning** | The practitioner explicitly described cases as non-linear (needs recur, beneficiaries become active/inactive, referrals fail, no fixed forward-only sequence). The same person can have multiple engagement periods. Crucially, they noted organizations handle returning needs differently (reopen old case vs. create new case). |
| **Implication for ontology** | Validates the architectural requirement for non-linear case journeys. The stronger evidence-backed invariant is: The Person persists across engagement cycles and their relevant historical information remains accessible, regardless of whether an organization reopens an existing case or creates a new case record. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Human needs and interventions do not follow strictly linear, forward-only paths. |
| **Organizational practice** | Managing non-linear cases and ensuring the person and their history persists across multiple engagements, though the specific administrative mechanism (new case vs reopened case) varies by organization. |
| **Local/contextual practice** | |
| **Ontology implication** | Non-linearity (CCR-6) is validated; Entity persistence decoupled from case status is validated. |

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
