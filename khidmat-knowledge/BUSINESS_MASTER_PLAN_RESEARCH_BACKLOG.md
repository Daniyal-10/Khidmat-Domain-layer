# Business Master Plan — Consolidated Research Backlog

**Type:** Backlog / traceability register
**Supersedes as the single reference point (not deletes):** The individual "Flagged Open Items" sections at the end of `BUSINESS_MASTER_PLAN.md` Chapters 1–9, and §5/§9 of `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md`
**Purpose:** One place for the Humanitarian Business Reference Model's author, and every subsequent methodology document's author, to check open items once instead of re-deriving them from nine chapters' worth of footnotes.
**Status of items below:** Registered and prioritized only. None are resolved here, per this task's explicit constraint.

---

## How to Read This Backlog

Each item carries:
- **ID** — stable reference (`RB-##`) for citation from future documents and ADRs.
- **Workstream** — the thematic cluster from `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md` §9 (A–F).
- **Origin** — the originating chapter(s)/section(s), for traceability back to the source.
- **Priority** — Critical / High / Medium / Low, assigned by blocking effect on the Humanitarian Business Reference Model, not by general importance.
- **Disposition** — the recommended next home for this item (future research, an ADR, a later methodology document, or "carry forward as a deferred boundary — no action needed").

---

## Workstream A — Domain-Expert Validation Program

Items requiring the same underlying action: structured domain-expert / field input, ideally gathered once across all of them rather than chapter by chapter.

| ID | Item | Origin | Priority | Disposition |
|---|---|---|---|---|
| RB-A1 | Actor-map completeness — additional actor categories may exist in specific operating contexts | Ch1, Flagged Item 1 | Medium | Domain-expert validation program |
| RB-A2 | Depth of community-structure description (informal credit, self-help groups, informal leadership) in specific communities | Ch1, Flagged Item 2 | Medium | Domain-expert validation program |
| RB-A3 | Context-specific stakeholder tensions beyond the eight named | Ch2, Flagged Item 2 | Medium | Domain-expert validation program |
| RB-A4 | Lifecycle stage boundaries not defined (when is "understanding" sufficient to move to "assessment") | Ch3, Flagged Item 1 | Low | Domain-expert validation program (see also RB-E, process-trigger cluster) |
| RB-A5 | Typical stage durations, and variation by need type/urgency | Ch3, Flagged Item 2 | Low | Domain-expert validation program |
| RB-A6 | Capability-list exhaustiveness — additional capabilities may exist in specific contexts | Ch4, Flagged Item 1 | Medium | Domain-expert validation program |
| RB-A7 | Capability boundary cases needing validation (Verification vs. Monitoring, Referral vs. Coordination) | Ch4, Flagged Item 4 | Low | Domain-expert validation program |
| RB-A8 | Value-stream exhaustiveness — additional patterns may exist | Ch5, Flagged Item 1 | Medium | Domain-expert validation program |
| RB-A9 | Intervention-category exhaustiveness and subdivision | Ch6, Flagged Item 3 | Medium | Domain-expert validation program |
| RB-A10 | Intervention-category overlap boundaries not validated against real programme practice | Ch6, Flagged Item 4 | Medium | Domain-expert validation program |
| RB-A11 | Operational-objective exhaustiveness and relative weighting by context | Ch7, Flagged Item 3 | Medium | Domain-expert validation program |
| RB-A12 | Household-vs-program governance boundary may not hold for very small organizations | Ch8, Flagged Item 3 | Low | Domain-expert validation program |
| RB-A13 | Variation-dimension exhaustiveness (Ch9's eight dimensions may not be complete) | Ch9, Flagged Item 1 | Medium | Domain-expert validation program |
| RB-A14 | Ch9's universal/variable discipline (§9.1) has never been tested against a real, specific regional case | Ch9, Flagged Item 4 | High | Domain-expert validation program — should be one of the first tests run, since it validates the *method*, not just one chapter's content |

**Recommended handling:** Run as a single structured interview/validation program in parallel with early Reference Model drafting, not sequentially before it. Fourteen items, one program.

---

## Workstream B — Religiously-Obligated Giving Mechanics

Recurring across four independent chapters — a signal this is a standing discovery topic, not a minor caveat.

| ID | Item | Origin | Priority | Disposition |
|---|---|---|---|---|
| RB-B1 | Specific doctrine, eligible-recipient categories, and conditions of religiously-obligated giving are never described, only acknowledged as existing | Ch1 Flagged Item 3, Ch2 Flagged Item 3 | High | Dedicated research workstream |
| RB-B2 | Relationship between funding authority (Ch8 §8.5) and religiously-obligated giving's own eligibility framework not elaborated | Ch8, Flagged Item 4 | High | Dedicated research workstream — same underlying question as RB-B1 |
| RB-B3 | Only one religious giving framework has been named (by inheritance from earlier chapters); other frameworks may be equally significant and are not addressed | Ch9, Flagged Item 2 | Medium | Dedicated research workstream — scope-widening question, resolve after RB-B1/B2 |

**Cross-reference:** This workstream directly affects already-authored ontology content — `donor-resource/taxonomy/islamic-giving.yaml` and `extensions/humanitarian/islamic/` — which `KHIDMAT_ARCHITECTURE_REVIEW.md` separately flagged as having undeclared ownership in `ontology_authority_matrix.md`. Resolving RB-B1/B2 at the business level and resolving that ontology-ownership gap should be coordinated, not run as two unrelated efforts.

**Recommended handling:** Escalate to the same priority tier as Workstream C below — both are recurring, both block multiple downstream documents.

---

## Workstream C — Programme-Validated Intervention Catalogue

| ID | Item | Origin | Priority | Disposition |
|---|---|---|---|---|
| RB-C1 | The concrete, programme-validated catalogue of what is actually provided within each of Chapter 6's eight intervention categories does not exist and cannot be authored without programme staff input | Ch6, Flagged Item 1 | **Critical** | Top-priority discovery item; independently corroborated by `knowledge_layer_roadmap.md`'s own long-standing blocker on the support-intervention taxonomy |
| RB-C2 | No eligibility conditions are stated for any intervention category (by design — see Workstream D) | Ch6, Flagged Item 2 | N/A | Not a gap — correctly deferred; see RB-D3 |

**Why Critical:** This is the single item that blocks the Reference Model, Business Architecture, *and* the existing ontology layer simultaneously. Recommend a dedicated decision record once resolved, given its cross-cutting blocking effect.

---

## Workstream D — Deliberately Deferred (Not Gaps)

These are correctly-held boundary lines, not omissions. Registered here so no future author mistakes the BMP's restraint for an oversight.

| ID | Item | Origin | Disposition |
|---|---|---|---|
| RB-D1 | No priority ordering among the eight stakeholder tensions | Ch2, Flagged Item 1 | Carry forward as explicit input requirement for Business Architecture |
| RB-D2 | No priority ordering among the ten operational objectives | Ch7, Flagged Item 1 | Carry forward as explicit input requirement for Business Architecture |
| RB-D3 | No eligibility rules for any intervention category | Ch6, Flagged Item 2 | Carry forward as explicit input requirement for Business Architecture / Programs domain |
| RB-D4 | No decision-rights assigned to any role, title, or named actor | Ch8, Flagged Item 1 | Carry forward as explicit input requirement for Business Architecture |
| RB-D5 | No capability assigned to any actor named in Chapter 1 | Ch4, Flagged Item 2 | Carry forward as explicit input requirement for Business Architecture |
| RB-D6 | No relative-frequency claim for any value stream | Ch5, Flagged Item 4 | Informational only — no downstream document currently requires this |

**Recommended handling:** Label these explicitly as "intentionally deferred to you" in the handoff brief to whoever authors Business Architecture, rather than leaving them to be rediscovered as apparent gaps.

---

## Workstream E — Process-Trigger Mechanisms Not Defined

Four items sharing one underlying question — what specific event or judgment moves a case from one state to another — better resolved together than four times separately.

| ID | Item | Origin | Priority | Disposition |
|---|---|---|---|---|
| RB-E1 | What determines whether a case reaches closure vs. continued support | Ch3, Flagged Item 3 | Medium | Single combined research topic with RB-E2–E4 |
| RB-E2 | Reassessment triggers not enumerated | Ch3, Flagged Item 4 | Medium | Single combined research topic |
| RB-E3 | Transition conditions between value-stream patterns not defined | Ch5, Flagged Item 3 | Medium | Single combined research topic |
| RB-E4 | Governance escalation triggers not defined | Ch8, closing discussion | Medium | Single combined research topic |

**Recommended handling:** Resolve as one "trigger mechanisms" research topic rather than four independent ones — the answer to "what marks stage/state transitions in humanitarian case work" is likely a single, reusable finding across all four.

---

## Workstream F — Newly Identified Gaps (This Review's Own Findings)

These did not appear in any chapter's own Flagged Open Items and were surfaced only by the independent architecture review and the subsequent governance resolution. Registered here for the first time.

| ID | Item | Origin | Priority | Disposition |
|---|---|---|---|---|
| RB-F1 (= RB-01 in Resolution doc) | Anticipatory / predictive need detection has no home in Chapter 3's lifecycle or Chapter 4's capability list | Architecture Review §5, item 1 | **High** | Note: `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §1/§17 already names this as the project's stated long-term vision *and* explicitly out of scope for the current version — the project has not overlooked this, but the BMP's own timeless business description still does not name the concept anywhere. Recommend as a future BMP amendment topic (new capability and/or lifecycle stage), not urgent for the Reference Model's first pass since V1 does not need it delivered. |
| RB-F2 | Consent as an explicit business concept, distinct from the general "dignity" and "control over one's story" language already present | Architecture Review §5, item 2 | Medium | `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3.2 already elevates consent to a foundational principle. Recommend the BMP eventually name consent explicitly (likely a Chapter 2 or Chapter 8 amendment) so the two documents use consistent vocabulary. |
| RB-F3 | Voluntary withdrawal or declined assistance has no place in Chapter 3's lifecycle, which assumes engagement continues once begun | Architecture Review §5, item 3 | Medium | `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §14 names a related but distinct "accountability loop" (grievance reopens the journey) — not the same as withdrawal. Recommend as a future Chapter 3 amendment topic. |
| RB-F4 (= RB-04 in Resolution doc) | The possibility of inaccurate or fraudulent claims is never named, only the possibility of claims requiring confirmation | Architecture Review §5, item 4 | Low | `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §17 already scopes fraud/anomaly engines as out-of-scope operational tooling for V1, noting light integrity checking already exists. Business-level naming of this possibility (without operational mechanism) could still strengthen Chapter 4/Chapter 7, but is not blocking. |
| RB-F5 | Chapter 9's universal/variable discipline was never applied to Chapter 7's own claim that "Fair and Equitable Access" is a universal objective — whether the *conception* of equity itself varies by culture is untested | Architecture Review §4.4 | Medium | Recommend as a Chapter 9 amendment topic, or as an early test case for RB-A14 |
| RB-F6 | Chapter 2 and Chapter 8 ground the same standardization-versus-flexibility tension in two different, uncross-referenced rationales (funder comparability vs. beneficiary equity) | Architecture Review §4.3 | Low | Cosmetic/clarity issue; resolve opportunistically during any future BMP touch-up, not urgent |
| RB-F7 | Terminology reconciliation: "capacity" is overloaded (household coping capacity / organizational capacity / the intervention category "Capacity Building"); "resilience" (Ch7) is introduced without being explicitly anchored to "capacity to cope" (Ch1, Ch3); lifecycle-stage names (Ch3) and capability names (Ch4) are deliberately not identical with no cross-reference table provided | Architecture Review §4.2 | Medium | Recommend a dedicated glossary/terminology pass before or alongside Reference Model authoring — explicitly out of scope for the BMP itself, but should not be inherited uncorrected |
| RB-F8 | Governance chapter (Ch8) is thinly connected to Value Streams (Ch5) — only one citation, versus dense connections to every other chapter | Architecture Review §4.5 | Low | Note for future Business Architecture author; not a defect requiring BMP amendment |

---

## Priority Summary (Cross-Workstream)

**Critical:** RB-C1 (intervention catalogue).

**High:** RB-B1, RB-B2 (religiously-obligated giving mechanics), RB-A14 (untested universal/variable discipline), RB-F1 (anticipatory need detection, context-noted as non-urgent for V1).

**Medium:** the majority of Workstream A, RB-B3, most of Workstream E, RB-F2, RB-F5, RB-F7.

**Low:** RB-A5, RB-A7, RB-A12, RB-F4, RB-F6, RB-F8.

**Not a gap (Workstream D):** RB-D1–D6, carried forward as explicit Business Architecture inputs, not backlog debt.

---

## Traceability Statement

Every item in this backlog traces to a named chapter, section, or flagged item in `BUSINESS_MASTER_PLAN.md`, or to a named finding in `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md`. No item was introduced without a cited origin. This backlog does not delete or supersede the source Flagged Open Items sections in the BMP itself — those remain in place as the chapter-level record; this document is the cross-chapter index over them.
