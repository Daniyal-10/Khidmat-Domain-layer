# 8 — Final Ontology Change Register

**Status: READ-ONLY AUDIT OUTPUT. No ontology file has been modified.**
Produced per the Ontology Finalization Handoff, prior to any edit pass.
Awaiting explicit approval before Step 1 (Primitives) editing begins.

---

## 0. Audit method and governing constraint

Every proposed change below was tested against one question before inclusion:

> **Does this change require Stage 7 governance, and if so, does a Stage 7 ruling exist for it?**

Per `06-STAGE-6-EVIDENCE-INTEGRATION-REPORT.md` §4–§7, **only one item** was flagged
`Governance Required: Yes` — Organisation/Programme (P4/L2/Pillar V). Stage 7 (`07-STAGE-7-...md`)
resolved it as **G1**. Every other Stage 6 change candidate (C1, C3–C7) was flagged
`Governance Required: No`, meaning it may proceed to ontology text as an ordinary refinement
**without** a numbered Stage 7 ruling, provided it does not amend a Tier 1 fact, invent a
formula, or close a question on single-source evidence alone (Ground Truth Review Framework F-3).

**CCR-7 (C8)** is the one exception in the other direction: Stage 7 explicitly ruled (**G2**) to
formally *leave it unresolved and unenforced*, which is itself a governance act and is treated as
approved — the approved change is to annotate the rule as governed-unresolved, not to strengthen it.

No new primitive, layer, or pillar is proposed anywhere below. All changes are text-level
refinements of existing structure, or (for G1 alone) a single approved entity split.

---

## 1. Final Ontology Change Register

| ID | Component | Current Definition | Evidence (GT-IDs) | Stage 6 Impact | Stage 7 Decision | Approved Change | Exact File | Exact Section | Risk | Dependencies |
|---|---|---|---|---|---|---|---|---|---|---|
| **OCR-01** | Entity (P4) / L2 / Pillar V — **Organisation vs Programme** | Collapsed into one Entity per Tier 1 (BL V1 §4) | GT-PL5, GT-OQ6 (both CHALLENGED) | C2 — CHALLENGE, Governance Required: Yes | **G1 — SELECTED: split into two Entities; Tier 1 BL V1 §4 formally amended** | Split `Organisation` and `Programme` into two Entities connected by a new `operates` Relation. Programme-specific eligibility/funding/activity rules attach to Programme, not Organisation. | `02-ONTOLOGY-LAYERS.md` | §3.1 Entities table row; §3.2 "strongest/weakest" para; §4.1 Relationships table (new row); §11 Assumption A-04; §12.1 closure list | **Highest** — only Tier-1-amending change in this pass | `03-ONTOLOGY-PILLARS.md` Pillar V; `04-ARCHITECTURE-RULES.md` (new synchronization-correction entry, mirroring §1's Need pattern); `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md` Q6 status |
| **OCR-02** | Pillar V boundary text | "Organisation and Programme are collapsed into one Entity per Tier 1 authority precedence... closing the previous evidence-based divergence" | GT-PL5, GT-OQ6 | (same as C2) | G1 | Rewrite boundary sentence to state the split and cite G1 as the amending authority, per PBR-2/PBR-3 | `03-ONTOLOGY-PILLARS.md` | §3, Pillar V body; §5 coverage-test bullet listing "Organisations, Programmes" | Medium | OCR-01 |
| **OCR-03** | `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md` Q6 | Status: RESOLVED (collapsed) | — | — | G1 supersedes | Update status field to "SUPERSEDED BY STAGE 7 G1 — split, not collapsed" without altering the historical record's own wording (append, don't rewrite) | `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md` | Q6 row, "Status" field only | Low | OCR-01 |
| **OCR-04** | Epistemic Stance (P3) / Cognition (L7) — missing-info & contradiction representation | "Structurally resolved" placeholder language; open-world commitment stated but mechanism unspecified | GT-P3, GT-L7, GT-OQ12 (REFINED), GT-OQ13 (REFINED) | C1 — REFINE, Governance: No | N/A (no governance needed) | Specify the mechanism now evidenced: every State/Claim carries a paired **(value, epistemic-status)** tuple, with epistemic-status ∈ {Known-True, Known-False, Unknown, Not-Assessed, Not-Applicable}; contradictions retain **all** conflicting claims with source attribution rather than overwriting | `02-ONTOLOGY-LAYERS.md` | §8.1 Cognition table (two rows); §8.2 open-world commitment paragraph | Low — refines an already-open stub, no closure of anything Tier 1 | None |
| **OCR-05** | Norm (P5) evidence rating | "Evidence not found" / Blueprint-only in places | GT-P5, GT-L4, GT-OQ8 (REFINED), GT-OQ14 (REFINED) | C6 — REFINE, Governance: No | N/A | (a) Upgrade evidence annotation to Moderate (practitioner-corroborated). (b) Populate funding-restriction taxonomy as a **non-exhaustive, named** Source-Absent Parameter (geography, target population, sector, eligible activity, time period, reporting) rather than fully unadmitted. (c) State consent explicitly as an ongoing per-action validation Norm, and that withdrawal halts dependent actions but does **not** cascade-delete history where another lawful basis applies | `02-ONTOLOGY-LAYERS.md` | §5.1 Constraints table (Funding restriction row); §5.3 "what this layer cannot yet hold" (consent) | Low-Medium — must not present the taxonomy as exhaustive (UHR-5 still applies) | None |
| **OCR-06** | States (L5) — Outcome/Impact ownership | Already states "ownership: pending", Outcome=State/measurement=Event | GT-PL6 (CONFIRMED), GT-OQ5 (REFINED) | C3 — REFINE, Governance: No | N/A | **No structural change** — current text already matches the evidence. Add citation annotations only (GT-PL6, GT-OQ5) to the existing §7.3/§12.2 entries | `02-ONTOLOGY-LAYERS.md` | §7.3; §12.2 item "Outcome/Impact Ownership" | None | None |
| **OCR-07** | Entities (L2) / Pillar V — Service Providers | Tagged `[OPEN]` — agency undecided | GT-OQ15 (REFINED, single practitioner) | C4 — REFINE, Governance: No | N/A | Update default reading toward "active Entity with independent capacity/eligibility decisions" **but retain an explicit single-source caveat** per Framework F-3 — do not fully close | `02-ONTOLOGY-LAYERS.md` | §3.1 Entities table (Service Provider row) | `03-ONTOLOGY-PILLARS.md` §3 Pillar V body | Low-Medium — F-3 forbids treating one response as closure | None |
| **OCR-08** | Architecture Rules §7.1 — "Service Providers as Actors" open item | Listed as fully `[OPEN]` | GT-OQ15 | (same) | N/A | Change status marker to "Provisionally REFINED — single-source; retained open pending broader corroboration or explicit Stage 7 ratification" | `04-ARCHITECTURE-RULES.md` | §7.1 Open Tensions table | Low | OCR-07 |
| **OCR-09** | Coordination Patterns (L8) — Funder coordination / Case orchestration | Stub extension points, "genuinely open" | GT-OQ17 (REFINED), GT-OQ19 (REFINED), both single-source | C5 — EXTEND, Governance: No | N/A | Add two named pattern rows (shape only, per LCR-7): **Funder Coordination** (funders set priorities/restrictions/reporting across programmes, distinct from programme casework) and **Case Orchestration** (cross-organisational coordination function — handoffs, gap/duplication tracking — distinct from direct service delivery, may or may not be a separate role) | `02-ONTOLOGY-LAYERS.md` | §9.1 Coordination Patterns table (two new rows); §9.4 "what this layer cannot yet hold" (narrow, don't remove entirely) | Low-Medium — shape-only, no execution/routing detail (LCR-7 boundary) | None |
| **OCR-10** | Architecture Rules §7.1 — Funder Altitude / Case Coordination open items | Listed as fully `[OPEN]`, UHR-1 stub | GT-OQ17, GT-OQ19 | (same as C5) | N/A | Downgrade from "genuinely open, no shape" to "shape defined by Stage 5 evidence; detailed operational rules remain UHR-1 stub" | `04-ARCHITECTURE-RULES.md` | §7.1 Open Tensions table (two rows) | Low | OCR-09 |
| **OCR-11** | Condition (P1) — Need vs Eligibility | Need defined RM §7.1; Eligibility a separate Constraint already exists (§5.1 "Eligibility gates progression") | GT-OQ11 (REFINED) — "need should not be treated as simply another fixed condition value... independent of programme eligibility" | C7 — REFINE, Governance: No | N/A | Add explicit cross-reference note: **Need (Condition, L5)** and **Eligibility (Norm, L4)** are structurally distinct and must never be conflated — a person can have a Need with no matching Programme eligibility, and the Need still exists | `02-ONTOLOGY-LAYERS.md` | §6.1 States table (Need row, add note); §5.1 Constraints table (Eligibility row, add cross-reference) | Low | None |
| **OCR-12** | States (L5) — Vulnerability composition | UHR-2 parameterized, versioned function; no hardcoded formula | GT-OQ2 / GT-PL3 (both CONFIRMED — no universal formula, context/professional-judgement driven) | C7 — REFINE, Governance: No | N/A | **No structural change** — confirms UHR-2 was the correct treatment. Add citation only | `02-ONTOLOGY-LAYERS.md` | §6.3 | None | None |
| **OCR-13** | Cognition (L7) — evidence-type weighting | Evidence kinds/weighting Source-Absent (UHR-1) | GT-OQ10 (REFINED — no universal evidence-precedence hierarchy; weighting is purpose/context-dependent) | (folds into C1) | N/A | Add an explicit **prohibition** note: do not hardcode a global evidence-type precedence order; weighting is Context-scoped (P2) and case-purpose-dependent | `02-ONTOLOGY-LAYERS.md` | §8.5 "what this layer cannot yet hold" | Low — this is a negative/preventive clarification, no new content invented | None |
| **OCR-14** | States (L5) / Relationships (L3) — Orphanhood vs Unguardianed | RM §6.3 does not distinguish; listed `[OPEN]` | GT-OQ18 (CONFIRMED — biologically/legally distinct from active-caregiving status) | Not a numbered C-item; folds into general findings | N/A | Confirm as two independent tracked facts: **Orphanhood** (a Condition, P1 — biographical/legal fact) and **presence of an active guardian/caregiver** (a Relation, P7, or its absence). Update `[OPEN]` marker to CONFIRMED-distinct | `02-ONTOLOGY-LAYERS.md` | §6.1 (add Person-condition row: Orphanhood); §4.1 (Guardianship relation, already listed — cross-reference) | Low | None |
| **OCR-15** | Coordination Patterns (L8) — Need-to-Need interaction | Not modelled as a formal Relation; RM §7.5 open | GT-OQ16 (REFINED — interactions are real but captured via case narrative/judgement, **not** a formal computable Relation) | Not a numbered C-item | N/A | Add a **preventive** note to the open-tensions entry: Stage 5 evidence indicates a formal Need↔Need Relation type should **not** be built; interactions are Cognition/documentation content, not structural Relations | `04-ARCHITECTURE-RULES.md` | §7.1 Open Tensions table ("Need-interaction model" row) | Low | None |
| **OCR-16** | CCR-7 — Dual-clock rule | Stated as a firm architecture rule, no caveat | GT-AR3 (**UNRESOLVED**) | C8 — UNRESOLVED, Governance: No (but Stage 7 ruled anyway) | **G2 — Retain as unresolved/optional; do not force universal enforcement** | Annotate CCR-7's definition with its governance status: "Status: UNRESOLVED per Stage 7 G2 (2026-09-01). Not enforced as a mandatory constraint. Retained as a documented hypothesis pending further evidence." | `04-ARCHITECTURE-RULES.md` | §4.4, CCR-7 definition | Low — this is a downgrade to honesty, not a strengthening | None |
| **OCR-17** | Entity (P4) — Person vs administrative record | Person and Case already listed as separate Entities | GT-P4 (REFINED), GT-OQ1 (REFINED), GT-AR3 (UNRESOLVED) | Folds into general findings | N/A | **No new entity.** Add a clarifying citation confirming the existing Person/Case separation already satisfies the practitioner's "beneficiary card ≠ person" distinction; note that identifiers (phone, national ID, internal ID) are attributes/Relations grounding identity evidence, not the Person Entity itself | `01-DOMAIN-PRIMITIVES.md` | P4 boundary note (§4, P4) | `02-ONTOLOGY-LAYERS.md` §3.1/§3.2 | Low | None |
| **OCR-18** | Evidence-strength annotations — Condition (P1), Norm (P5), general | Rated "Blueprint only" / "Evidence not found" in several places | GT-P1, GT-OQ2, GT-OQ9, GT-OQ11, GT-P5, GT-OQ8, GT-OQ14, GT-L3, GT-P7 (all CONFIRMED/REFINED) | Cross-cutting | N/A | Upgrade evidence-rating annotations in the pre-Stage-5 tables from "Blueprint only"/"Evidence not found" to "Moderate — Stage 5 practitioner-corroborated" wherever a corresponding CONFIRMED/REFINED GT record exists. **Does not change ECR-0's rating *scale*, only re-scores specific rows now that Ground Truth evidence exists as a source class alongside Tier B/D.** | `01-DOMAIN-PRIMITIVES.md` | §7.1 evidence table | `02-ONTOLOGY-LAYERS.md` §10 evidence-strength table | Low-Medium — must not silently claim Tier B/D-equivalent strength; Ground Truth evidence is its own tier per the Framework §2, not Tier 1 | None |

---

## 2. Primitive changes (P1–P7)

| Primitive | Change? | Basis |
|---|---|---|
| P1 — Condition | **Annotation only.** Evidence rating upgraded (OCR-18); Need/Eligibility cross-reference (OCR-11); Orphanhood as a Condition instance (OCR-14). No definition or boundary change. | GT-P1, GT-OQ2, GT-OQ9, GT-OQ11, GT-OQ18 |
| P2 — Context | **No change.** Strongly confirmed as-is (GT-P2, GT-PL2). | — |
| P3 — Epistemic Stance | **Refined.** Explicit epistemic-status value set and multi-claim retention rule made concrete (OCR-04); evidence-weighting prohibition (OCR-13). Definition/boundary unchanged. | GT-P3, GT-L7, GT-OQ10, GT-OQ12, GT-OQ13 |
| P4 — Entity | **One structural change (OCR-01, via G1).** Organisation/Programme split. Person/Case separation confirmed, not altered (OCR-17). Service Provider default updated with caveat (OCR-07). | GT-PL5, GT-OQ6, GT-P4, GT-OQ1, GT-OQ15 |
| P5 — Norm | **Annotation + parameter population (OCR-05).** No definition change; funding-restriction and consent parameters populated as non-exhaustive named categories. | GT-P5, GT-L4, GT-OQ8, GT-OQ14 |
| P6 — Occurrence | **No change.** Confirmed as-is (GT-P6, GT-L6). | — |
| P7 — Relation | **One addition.** New `operates` relation (Organisation→Programme) as a direct consequence of OCR-01. Kinship/dependency/guardianship confirmed unchanged (GT-P7, GT-L3). Need↔Need relation explicitly **not** added (OCR-15). | GT-P7, GT-L3, GT-OQ16 |

---

## 3. Layer changes (L1–L8)

| Layer | Change? | Register IDs |
|---|---|---|
| L1 — Facets | No structural change. GT-L1, GT-OQ4 confirm/refine that values remain programme/context-specific and out of ontology scope — this **confirms** the existing design, no edit required beyond an optional citation. | — |
| L2 — Entities | Organisation/Programme split (OCR-01); Service Provider default updated with caveat (OCR-07); Person/Case separation confirmed (OCR-17). | OCR-01, OCR-07, OCR-17 |
| L3 — Relationships | New `operates` relation row (OCR-01 dependency). No other change — GT-L3, GT-P7 confirm existing set. | OCR-01 |
| L4 — Constraints | Funding-restriction taxonomy populated (non-exhaustive); consent mechanics clarified; Need/Eligibility cross-reference added. | OCR-05, OCR-11 |
| L5 — States | Outcome ownership citation-only (already correct); Orphanhood condition added; Vulnerability composition confirmed unchanged. | OCR-06, OCR-11, OCR-12, OCR-14 |
| L6 — Events | No change. GT-L6, GT-P6 confirm as-is. | — |
| L7 — Cognition | Explicit epistemic-status mechanism (OCR-04); evidence-weighting prohibition (OCR-13). | OCR-04, OCR-13 |
| L8 — Coordination Patterns | Two new named pattern rows: Funder Coordination, Case Orchestration (shape only). Need↔Need relation explicitly excluded. | OCR-09, OCR-15 |

---

## 4. Pillar changes (I–VII)

| Pillar | Change? | Basis |
|---|---|---|
| I — Human & Social Subject | No change. Confirmed (GT-PL1). | — |
| II — Context & Environment | No change. Confirmed (GT-PL2). | — |
| III — Vulnerability & Need | No structural change; §8 items 1–2 (Risk/Need resolved) reconfirmed by GT-OQ2/9/11, cite only. | OCR-11, OCR-12 |
| IV — Epistemics & Knowledge | No structural change; cognition coverage test (§6) reconfirmed and its mechanism concretised via L7 changes. | OCR-04, OCR-13 |
| V — Actors & Ecosystem | **Two changes.** Organisation/Programme boundary text rewritten to reflect the split (OCR-02); Service Provider agency note updated with caveat (OCR-07/08). | OCR-01, OCR-02, OCR-07 |
| VI — Action & Coordination | No structural change; outcome-ownership language already correct, cite only. New coordination patterns (Funder/Orchestration) sit here without altering the pillar boundary. | OCR-06, OCR-09 |
| VII — Resources & Support | No change. Confirmed (GT-PL7) — the one facet structure with genuine external corroboration is unaffected. | — |

**Full-domain coverage test (03-ONTOLOGY-PILLARS.md §5) must be re-run once OCR-01/02 are applied**, per PBR-5 (coverage re-test on pillar change) — this is a required verification step, not itself a content change.

---

## 5. Architecture rule changes

| Rule / Item | Change? | Basis |
|---|---|---|
| CCR-1 (Altitude) | No change. Confirmed (GT-AR1). | — |
| CCR-2 (Algorithmic humility) | No change. Confirmed (GT-AR6). | — |
| CCR-5 (Human-oversight trigger) | No change. Confirmed (GT-AR4). | — |
| CCR-6 (Non-linearity) | No change. Confirmed (GT-AR2). | — |
| **CCR-7 (Dual-clock)** | **Annotated as governed-unresolved, per G2.** Not strengthened, not removed. | OCR-16 |
| CCR-8 (Dignity-as-constraint) | No change. Confirmed (GT-AR5). | — |
| §7.1 Open Tensions table | Four rows re-annotated (Service Providers, Funder Altitude, Case Coordination, Need-interaction) to reflect Stage 5 shape-level evidence while explicitly **not** closing them per Framework F-3. | OCR-08, OCR-10, OCR-15 |
| §1 (Need synchronization correction) | Unchanged — historical record stands. A **parallel new entry** is added for the Organisation/Programme correction, following the same XCR-3 single-ruling-propagation pattern. | OCR-01 |
| ECR-0 (Evidence Rating Scale) | **No change to the scale itself.** Ground Truth evidence is a new evidentiary input alongside Tier B/D per the Ground Truth Review Framework §2 — it does not retroactively become Tier 1, but individual row-level ratings are refreshed (OCR-18). | OCR-18 |

---

## 6. Explicitly unchanged items

The following were reviewed and confirmed to require **no edit**, because Stage 5 evidence either
matched the existing structure exactly or corroborated an already-correct open/stub treatment:

- All 7 primitive **definitions and boundary rules** (only annotations change, per §2 above)
- The 8-layer **derivation map** (§1 of `02-ONTOLOGY-LAYERS.md`) — no primitive gains or loses a layer
- The 7-pillar **set and derivation direction** (PBR-1 unaffected)
- Risk and Need **primitive classification** (both Condition) — reconfirmed, not reopened
- Family vs Household as **two distinct Entities** — reconfirmed (GT-OQ3)
- Kinship / dependency / guardianship / responsibility **relationship types** — reconfirmed (GT-L3, GT-P7)
- The **Facet/State split** (LCR-2) and the decision not to invent value sets — reconfirmed (GT-L1, GT-OQ4)
- **Vulnerability composition** as a parameterized, non-formulaic function (UHR-2) — reconfirmed (GT-OQ2, GT-PL3)
- **Handoff / Referral / Reassessment / Grievance loop** coordination patterns — reconfirmed (GT-L8)
- **Consent as a bounded-necessity Norm** — structure reconfirmed; only its operational parameters were populated (OCR-05), not its classification
- CCR-1, CCR-2, CCR-5, CCR-6, CCR-8 — all reconfirmed verbatim

---

## 7. Governance-locked items

These must **not** be altered by this finalization pass without a new, explicit Stage 7 ruling:

1. **GT-AR3 / CCR-7 (Dual-clock rule).** Locked at UNRESOLVED per **G2**. May be annotated (OCR-16) but not upgraded to a mandatory constraint, and no implementation strategy may be inferred from it.
2. **Organisation / Programme split.** Locked at "split" per **G1** — this is now the governed state; reverting to the collapsed reading would itself require a new Stage 7 ruling, not a downstream edit (CTR-3).
3. **Any item on the §7.1 Open Tensions table not listed in this register as re-annotated** (e.g., Contradiction-representation and Missing-information-representation structural mechanisms beyond OCR-04, which remain UHR-1 stubs) — these stay open; Stage 5 gave partial shape (OCR-04) but not full closure.
4. **Tier 1 sources** (`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, `KHIDMAT_AI_BUSINESS_OVERVIEW.html`) — Tier 1 source amendment: `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 was amended at source on 2026-09-02 pursuant to Stage 7 governance ruling G1 and the repository's XCR-2 amend-at-source requirement. The original collapsed Programme / Organisation row was replaced with distinct Organisation and Programme rows, with a dated amendment note documenting the correction. The Reference Model remained unchanged.
5. **The Reference Model** (`docs/04-reference-model/...md`) — untouched. No edit in this register touches it; every change traces to Stage 5/6/7 artifacts layered *on top of* the frozen reference model, consistent with README's "ontology derives from this document and nothing else."

---

## 8. Traceability summary

```
GT-PL5 / GT-OQ6  ──▶  Stage 6 C2 (Governance: Yes)  ──▶  Stage 7 G1  ──▶  OCR-01, 02, 03
GT-P3 / GT-L7 / GT-OQ12 / GT-OQ13  ──▶  Stage 6 C1  ──▶  (no governance needed)  ──▶  OCR-04
GT-PL6 / GT-OQ5  ──▶  Stage 6 C3  ──▶  (already applied)  ──▶  OCR-06 (citation only)
GT-OQ15  ──▶  Stage 6 C4  ──▶  (no governance needed, single-source caveat)  ──▶  OCR-07, 08
GT-OQ17 / GT-OQ19  ──▶  Stage 6 C5  ──▶  (no governance needed)  ──▶  OCR-09, 10
GT-P5 / GT-L4 / GT-OQ8 / GT-OQ14  ──▶  Stage 6 C6  ──▶  (no governance needed)  ──▶  OCR-05
GT-OQ2 / GT-PL3 / GT-OQ11  ──▶  Stage 6 C7  ──▶  (no governance needed)  ──▶  OCR-11, 12
GT-AR3  ──▶  Stage 6 C8 (UNRESOLVED)  ──▶  Stage 7 G2  ──▶  OCR-16
GT-OQ10 / GT-OQ16 / GT-OQ18 / GT-P4 / GT-OQ1  ──▶  (cross-cutting, not a numbered C-item)  ──▶  OCR-13, 15, 14, 17
(all evidence-rating rows)  ──▶  §7.1 impact maps  ──▶  OCR-18
```

Every register row above traces backward to a named GT record and forward to an exact file and
section. No row invents content beyond what its cited GT record, Stage 6 impact map entry, or
Stage 7 governance decision states.

---

## 9. What happens next

This document makes **no edits**. Per the handoff instructions:

- If approved as-is, I will apply OCR-01 through OCR-18 in the order Primitives → Layers →
  Pillars → Architecture Rules, re-running the pillar coverage test (§4 above) after OCR-01/02,
  and will present the full diff before considering the pass complete.
- If any row should be dropped, narrowed, or deferred, flag it by ID and I will revise the
  register before touching any file.
- Stage 5 GT records, the Stage 6 report, and the Stage 7 governance record will not be edited
  by this pass under any circumstance — they are the evidentiary record this register derives
  from, not its output.
