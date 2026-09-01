# 5 — Ground Truth Review Record: GT-OQ14-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ14-R1 |
| **Review ID (from matrix)** | GT-OQ14 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Consent rules and parameters |
| **Ontology layer(s)** | Constraints |
| **Ontology pillar(s)** | N/A |
| **Current structural position** | Constraint/Norm (P5); operational policy is a "minimal placeholder" |
| **Open question reference, if any** | GT-OQ14 / Q14 |
| **Upstream citation chain** | `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "In practice, what exactly do you ask a beneficiary for consent to do? And operationally, what happens to the case or the data if they withdraw their consent partway through receiving assistance?" |
| **Reviewer role** | Programme Management & Coordination Practitioner |
| **Humanitarian context** | Broad programme coordination and context assessment |
| **Evidence / response** | "In practice, consent is required when we need to collect, use, store, or share a beneficiary's personal information... or when participation in a particular activity requires the person's agreement... If a beneficiary withdraws consent during an ongoing case, the withdrawal must be respected for activities that depend on that consent. We do not treat withdrawal of consent as meaning that the person no longer exists or that their underlying need has disappeared. The caseworker determines what assistance or processing can continue under the applicable rules and what activities must stop, and records the change appropriately. Where another lawful or mandatory basis exists for retaining particular records or taking a required safeguarding action, that is handled according to the applicable rules rather than assuming that withdrawal automatically deletes all historical information." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | REFINED |
| **Reviewer reasoning** | The practitioner confirmed consent operates as a `Norm`, and fleshed out the "minimal placeholder" by explaining the operational mechanics: consent dictates data sharing and activity participation. Most importantly, consent withdrawal does *not* equate to automated cascading retroactive deletion of the record, as other lawful bases may apply. |
| **Implication for ontology** | Consent must be modeled as an ongoing validation rule (`Norm`) on actions (collection, sharing, participation) rather than a master cascading-delete toggle. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Consent withdrawal halts future dependent action and data sharing, but does not invalidate the historical existence of the person or their needs. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The system must evaluate consent as a constraint preceding specific Actions/Events, rather than tying it to the existence of Entity or Condition records directly. |

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
