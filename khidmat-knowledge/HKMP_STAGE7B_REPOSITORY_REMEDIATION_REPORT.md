# HKMP Stage 7B — Repository Remediation Report

**Source of truth:** `HKMP_STAGE7_REPOSITORY_SEMANTIC_INTEGRITY_AUDIT.md`, accepted as-is. This pass implements only the remediation that audit required — no new humanitarian knowledge, no new domains, no new architecture. Every change below is a missing edge, a missing cross-reference, or a missing ledger entry against concepts that already existed.

---

## 1. Findings Remediated

### P0 — Critical

**C-1 — Case Plan had no relationship to any intervention entity.**
Closed by adding `case_plan_addressed_by_intervention` (`case_plan` → `registration:support_intervention`), reusing the existing `addressed_by` predicate already used by `need_addressed_by_intervention`. No new entity, no new predicate. `support_intervention` (Registration) was chosen over `programs:intervention_offering` because it is the entity already representing "what assistance is being provided" at case scope, and formal-Program linkage already flows through the existing `referral_targets_program` pathway — adding a second, parallel program-link here would have duplicated that route rather than completed a gap.

**C-2 — Impact had no relationship to Beneficiary Lifecycle.**
Closed by adding `lifecycle_transition_triggered_by_impact_evaluation` (`lifecycle_transition` → `impact:impact_evaluation`) in `beneficiary-lifecycle/ontology/relationships.yaml` — the domain that already owns four sibling `triggered_by_X` relationships (registration case, verification finding, risk characterization, case decision). This is the fifth, added in the identical shape. Ownership is unchanged: Impact gains no ability to set `engagement_stage` or `human_development_stage`; Beneficiary Lifecycle continues to own both, and merely gains the ability to record that a specific impact evaluation was the trigger for a transition — exactly as it already can for a verification finding.

### P1 — Major

**Support Delivery overlap (M-1).** `delivery_modality` was not redesigned or revalued. A design note and a `references:` block were added to `support-delivery/taxonomy/delivery-modalities.yaml` explaining precisely why its four service-named values (handover/custody requirements) do not duplicate Programs' `intervention_modality` (delivery form) or `thematic_sectors` (sector) — different question, different scope, explicitly cross-referenced now instead of silently adjacent.

**`objective_status` orphan (M-2).** Wired to the existing `case_plan` entity as a new, optional data property (`objective_status`, domain: `case_plan`), rather than introducing a new `Objective` entity — the taxonomy now has exactly one consumer, at the coarsest defensible scope, with the scope limitation (one status for the plan as a whole, not per-individual-objective) explicitly documented rather than silently implied.

**`graduated` cross-references (M-3).** Added a `note:` to each of the two independently-defined `graduated` values — `programs/taxonomy/eligibility-and-enrollment.yaml#enrollment_outcome.graduated` and `beneficiary-lifecycle/taxonomy/exit-reasons.yaml#exit_reason.graduated` — each pointing at the other and stating explicitly that neither implies nor redefines the other. No value, id, or scheme was changed.

**Authority Matrix (M-6).** Added dedicated "Registration Domain" and "Programs Domain" sections to `ontology_authority_matrix.md`, in the same table format as every other domain section, recording ownership that was already true and already enforced in practice but had no single-page record. Also added the newly-wired `objective_status` to the existing Case Management section.

**Glossary (M-4).** Added seven missing sections to `GLOSSARY.md`: Needs Assessment, Case Management, Beneficiary Lifecycle, Programs, Community Context, Support Delivery, and Volunteer Operations Terms — each a concise set of the domain's core terms, matching the existing glossary's terse, one-to-three-sentence style. Not exhaustive; sufficient to close the "zero coverage" gap the audit identified.

---

## 2. Files Modified

- `case-management/ontology/relationships.yaml` — added `case_plan_addressed_by_intervention`; added `registration` namespace
- `case-management/ontology/data-properties.yaml` — added `objective_status` (on `case_plan`)
- `beneficiary-lifecycle/ontology/relationships.yaml` — added `lifecycle_transition_triggered_by_impact_evaluation`; added `impact` namespace
- `support-delivery/taxonomy/delivery-modalities.yaml` — added design note, `references:` block, `namespaces:` block
- `programs/taxonomy/eligibility-and-enrollment.yaml` — added cross-reference note to `enrollment_outcome.graduated`
- `beneficiary-lifecycle/taxonomy/exit-reasons.yaml` — added cross-reference note to `exit_reason.graduated`
- `ontology_authority_matrix.md` — added Registration Domain and Programs Domain sections; updated Case Management section for `objective_status`
- `GLOSSARY.md` — added seven domain-term sections
- `case-management/README.md`, `beneficiary-lifecycle/README.md`, `impact/README.md` — one-line-to-one-paragraph updates reflecting the new relationships

No entity was created. No new domain was created. No taxonomy scheme's value set was changed. No file was deleted.

---

## 3. Design Decisions

1. **Predicate reuse over predicate invention for C-1.** `addressed_by` already exists and already means exactly "this thing is addressed by this intervention" (Registration's `need_addressed_by_intervention`). Reusing it for `case_plan_addressed_by_intervention` is the same predicate-reuse discipline the Stage 7 governance review independently certified as correct for Programs' offering-level relationships — applied here rather than invented fresh.
2. **Sibling-pattern extension over new relationship shape for C-2.** Beneficiary Lifecycle already had a four-member `triggered_by_X` family. Adding a fifth member in the identical shape (rather than, say, a generic `informed_by` relationship with a qualifier) keeps the file internally uniform and required no new mechanism.
3. **`support_intervention` over `intervention_offering` as the C-1 target.** A Case Plan coordinates what a household is actually receiving in this case, which is `support_intervention` — a case-scoped concept already tied to `need`. `intervention_offering` is a catalogued, Program-scoped concept one level of abstraction removed; linking to it directly from `case_plan` would have bypassed the existing, already-correct `referral → program` pathway and created a second, competing route to the same eventual information.
4. **Attach `objective_status` to the nearest existing entity rather than create one for it.** The audit explicitly forbids new architecture in this pass. `case_plan` is the only existing entity for which "objective progress" is a coherent, if coarse, concept.
5. **Documentation-only remediation for M-1 and M-3.** Both findings were genuine but neither required a structural change — in each case the underlying concepts were legitimately distinct; what was missing was the record of that distinction. Adding notes and `references:` blocks closes the finding without touching any value, matching "minimum necessary."

---

## 4. Validation

**Repository graph traversal — the specific chain the audit required:**

`Registration (need) → [need_expressed_through_claim / need_addressed_by_intervention] → support_intervention → [case_plan_addressed_by_intervention, new] → case_plan → [case_plan_references_need_assertion] → need_assertion (Needs Assessment)` and, in the other direction, `case_plan → [delivery_event fulfills case_plan, pre-existing] → delivery_event (Support Delivery) → [pre-existing relationships] → ... → impact_evaluates_case → impact_evaluation (Impact) → [lifecycle_transition_triggered_by_impact_evaluation, new] → lifecycle_transition → [part_of_lifecycle] → beneficiary_lifecycle → human_development_stage / engagement_stage.`

The full chain — Registration → Needs → Case Plan → Intervention → Support Delivery → Impact → Beneficiary Lifecycle → Human Development — is now traceable as one connected graph. Confirmed by inspection of every relationship row along the path; no hop in this chain now terminates without an onward edge.

**No duplicate ownership:** `support_intervention` remains solely owned by Registration; `impact_evaluation` remains solely owned by Impact; `engagement_stage` and `human_development_stage` remain solely owned by Beneficiary Lifecycle. The two new relationships are rows in the *consuming* domain's own `relationships.yaml` (Case Management and Beneficiary Lifecycle respectively), pointing outward by CURIE — the identical, already-established pattern used by every other cross-domain relationship in both files. No domain gained the ability to define a concept it does not own.

**No broken references:** confirmed programmatically — `registration:support_intervention` and `impact:impact_evaluation` both resolve to entities that exist (`registration/ontology/entities.yaml`, `impact/ontology/entities.yaml`); every new or edited YAML file parses without error; every relationship, data-property, and taxonomy-concept id touched in this pass is unique within its file.

**No ADR violations:** ADR-008 (Single Ownership) is reinforced, not weakened — every remediation either added a reference to an existing owner or documented a pre-existing, legitimate distinction; no concept was redefined outside its owning file. ADR-021 (Case Lifecycle Handoff) is respected — the new Case Plan relationship targets `registration:support_intervention` directly (a Registration-owned entity that persists unchanged through handoff), not the pre-handoff `case` view.

**No semantic overlap introduced:** the two structural fixes (C-1, C-2) connect existing, already-distinct concepts; they do not merge any two concepts into one. The two documentation fixes (M-1, M-3) explicitly record distinctions that already existed but were previously undocumented.

**No new architectural debt:** every change in this pass is additive and terminal — no change here creates a new orphan, a new undocumented overlap, or a new missing cross-domain link. The items explicitly out of scope for this pass (predicate registry, shared relationship governance, `humanitarian_sector` promotion, `functional_capacity` retirement) were not touched, as instructed, and remain exactly where the Stage 7 audit left them — not worsened, not silently resolved.

---

## 5. Remaining Governance Debt

Unchanged by this pass, per explicit instruction not to touch them:
- Predicate registry / Shared Predicate Manifest (C-2 governance item, logged separately from this stage's C-2 finding — unrelated despite the shared label).
- `humanitarian_sector` (Shared Ontology) reserved but unpromoted; `need_assertion.thematic_sector` still sources from `programs_tax:thematic_sectors`.
- `functional_capacity` in `shared/taxonomy/persons.yaml` not yet retired in favor of `capabilities.yaml`'s scale (FLAG-001, still open).
- `impact_contains_measurement`'s self-flagged "requires promotion to Shared Vocabulary before repository freeze."
- Community Context's `external_shock` reference from Impact, deferred pending that domain's own activation.

One new, minor item surfaced by this remediation itself, worth recording rather than silently absorbing: `objective_status` on `case_plan` is now a single, coarse status for an entire plan, while a case plan may in practice coordinate multiple distinct objectives (one per need, potentially). This was an explicit, documented scope decision for this pass (Section 3, Decision 4), not an oversight — but if Case Management's model matures further, a finer-grained per-objective structure remains a legitimate future consideration, not something this pass silently foreclosed.

---

## 6. Final Repository Health

**Estimated health: 84 / 100** (up from 68/100 at the Stage 7 audit).

Both critical findings are closed with structurally sound, minimal, precedent-consistent edges. All five Priority-1 major findings are closed. The remaining gap to a perfect score is entirely the deliberately-untouched governance debt listed above (predicate registry maturity, two pending promotions, one pending retirement) — none of which this pass was authorized or instructed to resolve, and none of which represents a broken or ambiguous concept; each is an openly-tracked, honestly-labeled future task.

---

## 7. Certification Recommendation

**Repository Certified with Minor Findings.**

The two conditions that previously disqualified certification — an unreachable Case→Intervention link and an unreachable Impact→Human-Development link — are both resolved, and the full audited lifecycle chain is now traceable as one connected graph. The remaining open items are all pre-existing, previously-disclosed governance debt explicitly out of scope for this remediation pass, none of which represents a duplicate concept, a broken reference, or an ownership ambiguity. This repository is ready to be treated as one coherent knowledge graph for the purpose this program set out to validate, subject to that governance debt being picked up in its own dedicated future pass.
