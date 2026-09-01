# 5 — Ground Truth Review Record: GT-OQ10-R1

**Ontology Design, step 5 of 7.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`.

---

## Record identity

| Field | Value |
|---|---|
| **Record ID** | GT-OQ10-R1 |
| **Review ID (from matrix)** | GT-OQ10 |
| **Date recorded** | 2026-09-01 |
| **Recorded by** | AI Assistant |

---

## 1. Traceability (fill before the review, from the matrix)

| Field | Value |
|---|---|
| **Ontology element under review** | Types and Weighting of Evidence |
| **Ontology layer(s)** | Cognition (Epistemic Stance) |
| **Ontology pillar(s)** | IV — Epistemics & Knowledge |
| **Current structural position** | Evidence = Entity/Occurrence grounding Epistemic Stance (P3); weighting/taxonomy absent |
| **Open question reference, if any** | GT-OQ10 / Q10 |
| **Upstream citation chain** | `05-GROUND-TRUTH-REVIEW-MATRIX.md` |

---

## 2. The review itself

| Field | Value |
|---|---|
| **Question as asked** | "When gathering facts about a person or household, what different types of evidence do you actually collect in the field? If different sources of evidence point to different conclusions, how do you decide which one to trust? Is there a formal rule for which type of evidence 'wins'?" |
| **Reviewer role** | MEAL / Information Management Practitioner |
| **Humanitarian context** | Broad field operations and casework |
| **Evidence / response** | "In actual casework, we may receive evidence from several sources, including the person's own statement, documents or records, direct observation by a practitioner, information from family or community members, and information from organisations or service providers. These sources do not necessarily have the same reliability for every situation. The appropriate level of trust depends on what is being verified and the context of the case. For example, an official document may be the strongest evidence for a person's identity or eligibility-related fact, while direct observation or practitioner assessment may be more useful for understanding a person's current living conditions or immediate needs. If different sources provide conflicting information, workers should not simply delete one source or silently overwrite the previous information. The different claims and their sources should remain available, and the conflict should be identified for verification. There should not necessarily be one universal rule saying that one evidence type always wins over every other type. The reliability or relevance of evidence can depend on the particular fact being assessed, the source, the circumstances, and the purpose of the assessment. Where the conflict cannot be resolved automatically or confidently, it should be referred to an appropriate human practitioner for review." |

---

## 3. Finding

| Field | Value |
|---|---|
| **Finding classification** | REFINED |
| **Reviewer reasoning** | The practitioner confirmed that evidence types are diverse and must be tracked with claims, but actively refuted the idea of a universal "epistemic hierarchy" where one evidence type always outweighs another. The weighting is context-dependent, which refines our understanding that the *absence* of a hardcoded hierarchy in the ontology is a feature, not a bug. It also reinforced the need to preserve conflicting claims without silent overwrites. |
| **Implication for ontology** | The Epistemic Stance primitive (P3) must support associating a source type with a claim, but the ontology should not build a structural hierarchy for automated conflict resolution based purely on those types. Conflict resolution requires human review or context-specific logic. |

---

## 4. Domain reality vs. practice

| Field | Value |
|---|---|
| **Humanitarian domain reality** | Evidence weight is context-dependent and domain-specific (e.g., identity vs. immediate needs). Conflicting claims must not be silently overwritten. |
| **Organizational practice** | |
| **Local/contextual practice** | |
| **Ontology implication** | The system must permit multiple conflicting claims with distinct sources to exist simultaneously, surfacing them for human resolution rather than resolving them automatically via a global hierarchy. |

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
