# 5 — Ground Truth Review Record: GT-OQ1-R1

**Ontology Design, step 5 of 7.**

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ1-R1 |
| **Review ID (from matrix)** | GT-OQ1 |
| **Date recorded** | 2026-08-28 |
| **Recorded by** | Antigravity AI |

---

## 1. Traceability

| Field | Value |
|---|---|
| **Ontology element under review** | Person-sameness / identity resolution |
| **Ontology layer(s)** | Entities (P4) + Epistemic Stance (P3) |
| **Ontology pillar(s)** | IV — Epistemics & Knowledge |
| **Current structural position** | Entity (P4) + Epistemic Stance (P3); deterministic matching rule unspecified, biometrics excluded |
| **Open question reference, if any** | Q1 / GT-OQ1 |
| **Upstream citation chain** | Stage 1–4 artifact → Reference Model section → Tier 1 source |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | How do you currently determine, without biometrics, that a new registration is the same person as an existing record? [Follow-up: What happens if a phone number is shared by multiple people in a family, or if a beneficiary loses or changes their phone number?] |
| **Reviewer role** | Humanitarian practitioner (role unspecified) |
| **Humanitarian context** | Unspecified; references Aadhaar/Voter ID in India. |
| **Evidence / response** | "We primarily identify and link beneficiaries using their phone number... We will also collect identity documents for the person and bind each person to an individual ID. For example, documents such as an Aadhaar card or Voter ID in India can be used. This makes identifying and distinguishing the same person much easier than relying only on the phone number." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | REFINED |
| **Reviewer reasoning** | The practitioner stated that while phone numbers are primarily used for linking, they also collect identity documents (e.g., Aadhaar/Voter ID) to bind to an internal "individual ID", which makes identification "much easier" than phone numbers alone. This refines the deterministic matching mechanism by demonstrating a multi-layered approach (phone, government ID, internal ID) in this organization. The evidence does not establish government ID as a universal identity-resolution mechanism across the domain. |
| **Implication for ontology** | The ontology may need to structurally distinguish between a Person (Entity), a contact method (phone), a government ID, and an internal administrative ID, rather than collapsing them. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | |
| **Organizational practice** | Using phone numbers primarily, but binding each person to an internal "individual ID" supported by collected identity documents. |
| **Local/contextual practice** | Use of Aadhaar or Voter ID specifically (India context). |
| **Ontology implication** | The ontology might consider separating the Entity (Person) from its various identifiers (phone, state ID, internal ID). |

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
| **Follow-up requirement** | Further evidence needed. We must determine if this multi-layered ID approach (phone + state ID + internal ID) is common across other humanitarian contexts, or if some contexts rely solely on contact methods or biometrics. |
| **Carried to** | Stage 6 (Evidence) |
