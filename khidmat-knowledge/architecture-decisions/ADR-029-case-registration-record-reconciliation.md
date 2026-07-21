# ADR-029

## Title
Case / Registration Record Reconciliation — One Canonical Case Stands (ADR-021 Upheld)

## Status
Proposed (Pending Owner Ratification). The technical determination below is complete, but
acceptance is a governance action reserved to the project owner; ADR-029 is to be ratified to
**Accepted** once the documentation cleanup and Business Discovery review are complete. The
ontology implementation of the convergence described under Consequences is separately pending
explicit authorization to resume.

## Context
During Phase 1.2 implementation, `verification-operations/ontology/relationships.yaml`
was found to cite and depend on **ADR-021 (Accepted)**, which had already reasoned through —
and deliberately rejected — the same entity split that the Phase 1.1A "Canonical Semantic
Foundation" pass ratified as its Case decision:

- **ADR-021 (existing, Accepted, already implemented against):** one entity, `Case`, canonical
  to Case Management. Registration's status vocabulary (`in_progress`, `ready_for_verification`, …)
  describes *pre-operational phases of that same Case*. On completing registration the Case
  undergoes a phase transition into the Case Management lifecycle (typically `opened`). No new
  entity.
- **Phase 1.1A Case decision (later, made without visibility into ADR-021):** two entities — a
  long-lived `Case` and a renamed bounded `Registration Record` — joined by a
  `case_opened_from_registration_record` relationship.

Phase 1.1A correctly *observed* an unresolved seam: three domains reference the two case names
inconsistently — `beneficiary-lifecycle` → `registration:case` (×2), `impact` →
`case_management:case`, `verification-operations` → **both**. That observation is real and
remains true regardless of which model is chosen; it is evidence of an unresolved seam, not
evidence for either resolution. What Phase 1.1A lacked was ADR-021's prior, reasoned resolution
of that seam.

Each of Phase 1.1A's three supporting arguments for the split ("two real-world things sharing a
name," "preserves both original ask and current state," "no future breaking change needed") is
independently satisfiable under ADR-021's single-entity model: a phase-tagged, append-only
status history on the one `Case` preserves the intake-time snapshot the same way the layer
already handles append-only history elsewhere (e.g. `human_review_supersedes_human_review`,
`case_note`). And `verification-operations`' dual reference is not a failure of ADR-021 — its own
relationship notes invoke ADR-021's phase-handoff model intentionally, naming one entity at two
lifecycle points.

## Decision
The two decisions are reconciled **without changing the semantic model**: ADR-021's "phase
handoff" and Phase 1.1A's "opened from" describe the same underlying structure at different
entity granularity, and **ADR-021 — the earlier, Accepted, and already-implemented decision —
stands.** There is one canonical `Case`, owned by Case Management; there is no separate
`Registration Record` entity.

Reasoning:
- ADR-021 is Accepted, already implemented (Verification Operations depends on it by name), and
  its rejection of the split was deliberate and reasoned, not an oversight.
- Overturning an Accepted, implemented ADR requires the reversal to be *better* justified than
  the original, not merely *differently* justified. Phase 1.1A's case for the split is a
  legitimate reading of the same evidence ADR-021 already weighed — not new evidence.
- The practical cost of adopting the split now is real and immediate: Verification Operations
  would need both relationship rewrites and rewritten justifying notes, and every downstream
  `beneficiary-lifecycle` reference would need re-adjudication — reopening exactly the ambiguity
  this reconciliation exists to close.

This is not "ADR-021 in isolation": Phase 1.1A's genuine contribution — the identified
inconsistency — is preserved and closed, by **standardizing every domain on the single canonical
`Case`**, not by minting a second entity.

## Alternatives Considered
- **Adopt Phase 1.1A's two-entity split** (`Case` + `Registration Record`): rejected — it
  overturns an Accepted, already-implemented ADR without better justification and forces
  breaking changes on Verification Operations.
- **Declare ADR-021 correct in isolation and discard Phase 1.1A entirely:** rejected — it would
  leave the real cross-domain inconsistency Phase 1.1A found unaddressed.

## Consequences
The semantic model is unchanged and no entity is renamed by this determination. When
implementation on this concept is authorized to resume, convergence proceeds as follows:
- `registration/ontology/entities.yaml`'s `case` entity is retained (not renamed) and its
  description clarified to state, per ADR-021, that it is the pre-operational-phase view of the
  one canonical Case owned by Case Management — matching how `verification-operations` already
  treats it.
- `beneficiary-lifecycle`'s two relationships to `registration:case` are re-pointed to
  `case_management:case` (or annotated, matching `verification-operations`' pattern, as
  referencing the canonical Case by its pre-handoff name), so all three previously inconsistent
  domains converge on one documented pattern.
- No `case_opened_from_registration_record` relationship is introduced — no second entity exists
  to open one from.

*These ontology edits are deliberately NOT performed by this ADR; they await explicit
authorization, per the governance determination this ADR formalizes.*

## Future Review Considerations
ADR-021 flags its own limit: "Review if/when additional domains introduce their own intermediate
statuses." Case Management, Beneficiary Lifecycle, and Impact have since been built out beyond
what existed when ADR-021 was accepted. Whether ADR-021's phase-handoff model still holds cleanly
across all of them is worth a dedicated, separately-scoped review — but that is a forward-looking
scope question about ADR-021's applicability, not a reason to adopt the split as a workaround.

## Related Documents
- `architecture-decisions/ADR-021-case-lifecycle-handoff.md` (the decision this upholds)
- `ontology_authority_matrix.md`

## History
Formalized from the standalone `ADR_RECONCILIATION_CASE.md` governance report (Phase A
documentation consolidation), preserving that report's Section 4 determination verbatim in
substance. The canonical YAML files that previously cited `ADR_RECONCILIATION_CASE.md`
(`registration/ontology/entities.yaml`, `registration/ontology/lifecycle-constraints.yaml`,
`case-management/ontology/entities.yaml`, `case-management/ontology/relationships.yaml`,
`beneficiary-lifecycle/ontology/relationships.yaml`, `shared/ontology/data-properties.yaml`)
now reference this ADR.
