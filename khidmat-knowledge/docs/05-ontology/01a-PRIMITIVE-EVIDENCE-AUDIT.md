# 1a — Domain Primitive Evidence Traceability Audit

**Independent review of the evidential support behind each accepted Domain Primitive.**
Conducted 2026-07-29, after `01-DOMAIN-PRIMITIVES.md` was drafted. Does not redesign the set.

> **Why this document exists.** This audit was performed and reported, but not committed.
> `02-ONTOLOGY-LAYERS.md` then cited it nine times as the authority for its Evidence columns —
> citing a document that was not in the repository. That was a package-integrity defect of
> exactly the kind Standing Rules 1 and 2 exist to prevent. This file closes it. The content is
> the audit as performed; nothing has been strengthened after the fact.

---

## 1. Evidence hierarchy applied

| Level | Source | Counts as independent evidence? |
|---|---|---|
| **1** | TD Evidence Dossiers (`docs/01-evidence/`) — **Tier B/D findings only** | **Yes** |
| 2 | `MERGED_BUSINESS_UNDERSTANDING.md` | No — derivative |
| 3 | `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | No — conceptual framework |
| 4 | `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` | No — conceptual blueprint |

**Two exclusions applied throughout.** The dossiers' **Tier C** content is void — every internal
artifact it compared against was deleted in the reset. **Tier A** was never executed in any
dossier. Only Tier B/D findings were counted.

**One further exclusion.** The dossiers' own confidence scoring and evidence tiering is the
*discovery method*, not domain evidence about epistemics. It was not counted toward Epistemic
Stance.

## 2. Rating scale

This scale is authoritative for both `01-DOMAIN-PRIMITIVES.md` and `02-ONTOLOGY-LAYERS.md`.

| Grade | Meaning |
|---|---|
| **Strong** | ≥2 independent Level-1 source families, Tier B institutional or high-confidence Tier D |
| **Moderate** | 1–2 Level-1 findings, corroborated but thin or at medium confidence |
| **Limited** | A single Level-1 finding, tangential or partial |
| **Blueprint-only** | No Level-1 support. Conceptually defined at Levels 3–4 only |
| **Evidence not found** | The specific claim was searched for across all six dossiers and is absent |

---

## 3. Evidence Traceability Matrix

> **Mapping Note (Stage 5 Correction):** This audit uses the term **Entity (P4)** to refer to what was originally assessed as "Identity". Similarly, "Evidence" was assessed but later rejected as a primitive and distributed across Entity, Occurrence, and Cognition. Its ratings are omitted from this primitive table but apply to the underlying concepts.

| Primitive | Supporting TD findings | Independent sources | Primary source | Strength | Evidence gaps | Practitioner validation |
|---|---|---|---|---|---|---|
| **Context** | BD-TD01-002, BD-TD01-006, BD-TD03-001, BD-TD04-003, BD-TD05-002, BD-TD06-002 | OCHA, UNHCR, IASC, IOM, WHO Health Cluster, fscluster, Springer, ReliefWeb | **TD Evidence** | **Strong** | No source specific to any deployment geography (TD-01 Open Gap 3) — category evidenced, instances not | Desirable |
| **Norm** | BD-TD01-004, BD-TD02-001, BD-TD02-003, BD-TD02-004 | ICRC (Tier B primary), Sphere/CHS, CSIS, ODI HPN, ScienceDirect, Emerald, *Disasters* (2025), IOM | **TD Evidence** | **Strong** | Content of specific giving restrictions: **Evidence not found** | Desirable |
| **Entity (P4)** | BD-TD01-001/002/003/004/005, BD-TD03-004 | OCHA, UNHCR, IASC, Sphere/CHS, WHO EMRO, Twigg & Mosel (2017), BRAC/USAID, PMC | **TD Evidence** | **Moderate** | How sameness of a person is established: **Evidence not found**. TD-01 Open Gap 1 — operational roles have zero external validation | **Yes** |
| **Occurrence (P6)** | BD-TD03-001, BD-TD03-002, BD-TD05-003, BD-TD06-003 | IASC, UNHCR, IOM, WHO, interagency GBV and Child Protection Guidelines, HVSM | **TD Evidence** | **Moderate** | **The point-versus-span distinction itself: Evidence not found.** All findings describe stages; none establishes point and span as two irreducible kinds | Desirable |
| **Epistemic Stance (P3)** | BD-TD02-002, BD-TD03-003, BD-TD04-001 | ResearchGate critical review, expert-framework commentary; Better Care Network, Sopact | TD Evidence (one direct finding) | **Moderate** | Confidence as an attached property of a humanitarian conclusion: **Evidence not found**. Representation of contradiction and of missing information: **Evidence not found** | **Yes** |
| **Condition (P1)** | BD-TD03-004, BD-TD06-001, BD-TD06-002 | BRAC/USAID Graduation literature, PMC systematic review, IASC, Triple Nexus | **Blueprint** | **Limited** | Health, capability, shelter condition, wellbeing, caregiving: **Evidence not found**. Vulnerability composition: **Evidence not found** | **Yes — critical** |
| **Relation (P7)** | BD-TD01-003, BD-TD03-001, BD-TD05-003 | IASC, UNHCR, OCHA, IOM, WHO, HVSM | **Split** — TD (institutional) / Blueprint (social) | **Moderate** institutional · **Evidence not found** social | Kinship 0, spouse 0, parent 0, sibling 0, family-member 0. RM §4.1's cascade claim — *"a mother's risk is her infant's risk"* — **Evidence not found** | **Yes — critical** |

**All 22 `BD-TD` finding IDs cited above resolve to real findings in the six dossiers.**

---

## 4. Coverage summary

**Strongest** — Context (five dossiers converging on the altitude split) and Norm (ICRC Tier B
primary plus three corroborated tension findings).

**Weakest** — Relation and Condition, both Limited-to-absent for exactly the content they exist
to classify.

**Supported only by conceptual documents** — the social half of Relation; the human-condition
half of Condition.

**Structural observation.** The six dossiers are topic-organised as *ecosystem actors ·
stakeholder tensions · lifecycle · business capabilities · services and value streams ·
intervention categories.* All six examine how humanitarian **organisations operate**. None
examines people, families, households, situations, needs or risk. The primitives classifying
organisational reality are well evidenced; those classifying human reality are not. The evidence
base carries the same operational-first orientation the foundation reset was undertaken to
correct.

Discovery was additionally chapter-driven and terminated at six topics; dossiers reference
Chapters 8 and 9 as requiring evidence, and no dossier for them exists.

---

## 5. Confidence bands

- **High confidence:** Context, Norm
- **Medium confidence:** Entity, Occurrence, Epistemic Stance
- **Low confidence:** Relation, Condition

## 6. Risks

1. **Relation (social) and Condition (human) are uncorroborated.** These carry the person,
   family, household, health, capability and vulnerability content. If Business Logic V1 is wrong
   about any of it, nothing in this repository would detect the error.
2. **The point-versus-span distinction is unevidenced.** Condition and Occurrence are separated
   on structural grounds alone. If they collapse, two of eight primitives merge.
3. **RM §8 (Risk) has zero external citations.** The Condition-versus-Epistemic-Stance tension in
   `01-DOMAIN-PRIMITIVES.md` §6.1 **cannot be settled by evidence review** — no independent
   material exists to adjudicate it. It is a ruling, not a research question.
4. **Entity's mechanism gap.** Person-persistence is load-bearing for three principles; how
   sameness is established has no evidence, and TD-01 states literature search will not close it.

## 7. Verdict

**Sufficient to proceed to Ontology Layers, with two boundaries:**

- **The primitive set must not be closed or ratified on this evidence.** Closure asserts
  completeness across the whole domain; Relation and Condition do not support that claim.
- **Cognition is affected.** It derives from Epistemic Stance (Moderate at best) and its scope
  depends on the unresolvable Risk classification, which must be ruled on before Cognition is
  finalised.

Delaying layer design would not help: these are Tier A gaps, and no further document review will
close them.
