# ADR Reconciliation Report — Case / Registration Record

**Status:** Governance review only. Not an implementation. No ontology YAML for `case` has
been modified as a result of this report; `registration/ontology/entities.yaml`'s `case`
entity and every relationship targeting `registration:case` remain exactly as they were before
Phase 1.1–1.1A.

**Trigger:** During Phase 1.2 implementation, `verification-operations/ontology/relationships.yaml`
was found to explicitly cite and depend on **ADR-021 (Accepted)**, which had already reasoned
through — and rejected — the same entity split that the Phase 1.1A Canonical Semantic
Foundation ratified as its Case decision. Implementation was paused on this concept pending
reconciliation, per instruction.

---

## 1. The Two Decisions, Side by Side

| | ADR-021 (existing, Accepted) | Phase 1.1A Case Decision (this session's ratification) |
|---|---|---|
| **Model** | One entity, `Case`, canonical to Case Management. Registration's status vocabulary (`in_progress`, `ready_for_verification`, …) describes *pre-operational phases of the same Case*. On completing registration, the Case undergoes a phase transition into the Case Management lifecycle (typically starting at `opened`). No new entity. | Two entities: Case Management's `Case` (long-lived coordination container) and a renamed `Registration Record` (bounded intake artifact), joined by an explicit `case_opened_from_registration_record` relationship. |
| **Explicit alternative considered** | "Declaring the Registration Case as a distinct entity `RegistrationRecord` that promotes to a Case Management `Case` at a handoff event: **Rejected** because it introduces unnecessary entity duplication for the same real-world object." | This *is* that rejected alternative. |
| **Stated reasoning** | Avoids "unnecessary entity duplication for the same real-world object." Treats registration-phase and case-management-phase statuses as two vocabularies describing sequential phases of one lifecycle. | Treats the bounded, closed-at-intake artifact and the long-lived, mutable coordination container as two different real-world things that happen to share a name today — citing that three downstream domains already reference them inconsistently (see §2). |
| **What already depends on it** | `verification-operations/ontology/relationships.yaml`: `verification_assignment_verifies_case` and `verification_assignment_issued_from_brief_context_of_case` both cite ADR-021 by name and describe "the single canonical Case regardless of which phase it currently occupies." `ontology_authority_matrix.md` and `registration/ontology/entities.yaml`'s own inline note both reference the Case/Verification-Brief relationship in terms consistent with a single persisting Case. | Nothing yet — it is a fresh ratification with no downstream implementation. |

---

## 2. What the Phase 1.1/1.1A Passes Did Not Have Visibility Into

The Phase 1.1 ontology review and Phase 1.1A ratification both correctly *observed* that
`registration:case` and `case_management:case` are declared with different descriptions and
that three domains split across them inconsistently:

- `beneficiary-lifecycle` → `registration:case` (×2 relationships)
- `impact` → `case_management:case`
- `verification-operations` → **both** `registration:case` and `case_management:case`

This observation is factually correct and remains true regardless of which model is chosen —
it is evidence of an *unresolved seam*, not evidence for either resolution. What Phase 1.1A did
not have was ADR-021's own resolution of that seam, or its reasoning for why the two
vocabularies are phases of one entity rather than two entities. Phase 1.1A treated the seam as
unaddressed; it was addressed, on record, by ADR-021.

Critically, verification-operations' inconsistency is *not* evidence that ADR-021 failed — it
is evidence that verification-operations' own relationship notes are self-aware of exactly this
ADR-021 phase-handoff model and use both references *intentionally*: 
`verification_assignment_issued_from_brief_context_of_case` explicitly targets
`registration:case` because "the Case entity is canonical and persists across the
Registration-to-Case-Management phase handoff; this reference targets that single canonical
Case regardless of which phase it currently occupies" (quoting the file directly). The two
references are two ways of naming *one* entity at two different points in its lifecycle, per
ADR-021's own design — not a split.

`beneficiary-lifecycle`'s two relationships to `registration:case` are less clearly justified
either way — they were not accompanied by a note invoking ADR-021 — but they are equally
consistent with "referencing the canonical Case, using its pre-handoff name" as they are with
"referencing a genuinely separate Registration Record."

---

## 3. Re-Examining Phase 1.1A's Stated Rationale for the Split

Phase 1.1A's Case decision (Section 5 of that pass) argued for the split on these grounds,
each re-examined against ADR-021 below:

1. **"Two different real-world things wearing the same name."**
   ADR-021 does not dispute that intake and coordination are different *activities* — it
   disputes that they require different *entities*. A Case's `status` moving from
   `ready_for_verification` (a registration-phase value) to `opened` (a case-management-phase
   value) is, under ADR-021, a state transition of one long-lived record, exactly analogous to
   an Evidence record moving from `provided_digitally` to `verified`, or a Need moving from
   `open` to `resolved`. Under this reading, Phase 1.1A's premise — that two real-world things
   exist — is itself the contested point, not a settled observation.

2. **"Preserves both: what was originally asked (Registration Record) and what is the current
   state (Case)."**
   ADR-021's model preserves this too, differently: the append-only, phase-tagged status
   history *on the single Case* is what preserves "what was originally asked" — the same
   pattern the knowledge layer already uses elsewhere for append-only history (e.g.
   `human_review_supersedes_human_review`, `case_note` in Case Timeline). No second entity is
   required to keep the intake-time snapshot legible; a phase-scoped status log on one entity
   does the same job.

3. **"No future breaking change needed — the seam is already explicit."**
   This is true of the split model. It is also true of ADR-021's model, which has *already
   been implemented* against by Verification Operations — meaning the split model, if adopted
   now, is the one that requires a breaking change (to Verification Operations' two
   ADR-021-citing relationships and their justifying notes), not the reverse.

None of this proves ADR-021 is correct and Phase 1.1A is wrong. It shows that Phase 1.1A's three
supporting arguments are each also satisfiable under ADR-021's model, which was not visible to
that pass. The two decisions are not making incompatible claims about the business domain; they
are making different modelling choices for representing the same, accurately-observed seam.

---

## 4. Determination

**C. Both decisions can be reconciled without changing the semantic model — by recognizing
that ADR-021's "phase handoff" and Phase 1.1A's "opened from" relationship describe the same
underlying structure with different entity granularity, and that ADR-021, being the earlier,
Accepted, and already-implemented decision, should stand.**

Reasoning:

- ADR-021 is **Accepted**, **already implemented** (Verification Operations depends on it by
  name), and its rejection of the split model was **deliberate and reasoned**, not an oversight.
- Phase 1.1A's Case decision was made **without visibility into ADR-021** and its three
  supporting arguments are each independently satisfiable under ADR-021's existing model (§3).
- Overturning an Accepted, implemented ADR requires the reversal to be *better justified* than
  the original decision, not merely *differently justified*. Phase 1.1A's case for the split is
  a legitimate reading of the same evidence ADR-021 already considered, not new evidence ADR-021
  failed to consider.
- The practical cost of adopting the split now is real and immediate: `verification-operations`
  would require both relationship rewrites and rewritten justifying notes, and every downstream
  reference in `beneficiary-lifecycle` would need re-adjudication as to which of the two new
  entities it actually means — reopening exactly the ambiguity this reconciliation exists to
  close.

**This is not "ADR-021 remains correct" in isolation (option A) — it is answer C**, because
Phase 1.1A's genuine contribution is preserved rather than discarded: the *inconsistency*
Phase 1.1A identified (three domains split across two names) is real and still needs closing.
Under this reconciliation, it closes by **standardizing every domain's reference on the single
canonical `Case` per ADR-021**, not by minting a second entity. Concretely, once implementation
resumes on this concept:

- `registration/ontology/entities.yaml`'s `case` entity is retained (not renamed to
  `Registration Record`) but its description is clarified to state explicitly, per ADR-021,
  that it is the pre-operational-phase view of the one canonical Case owned by Case Management —
  matching how `verification-operations` already treats it.
- `beneficiary-lifecycle`'s two relationships to `registration:case` should be re-pointed to
  `case_management:case` (or explicitly annotated, matching verification-operations' pattern,
  as referencing the canonical Case by its pre-handoff name) so that all three previously
  inconsistent domains converge on one documented pattern instead of two undocumented ones.
- No new `case_opened_from_registration_record` relationship is introduced, since no second
  entity exists to open one from.

## 5. What Remains Genuinely Open

ADR-021 itself flags its own limit: *"Review if/when additional domains introduce their own
intermediate statuses."* Case Management, Beneficiary Lifecycle, and Impact have all since been
built out beyond what existed when ADR-021 was accepted. Whether ADR-021's phase-handoff model
still holds cleanly across all of them — rather than specifically the Case/Registration decision
in isolation — is worth a dedicated review, but that review is a **scope question about
ADR-021's applicability going forward**, not a reason to adopt Phase 1.1A's split as a
workaround. That review, if wanted, should be scoped and requested separately.

---

*This report is a governance determination only. Implementation (re-pointing
beneficiary-lifecycle's two relationships and clarifying registration's `case` entity
description) has not been performed and awaits explicit authorization to resume.*
