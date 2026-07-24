# Humanitarian Business Reference Model Blueprint — Resolution

**Type:** Governance resolution
**Resolves:** Every Required Change and Open Question raised in `HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT_ARCHITECTURE_REVIEW.md`
**Subject blueprint:** `HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT.md` (unmodified by this document)
**Date:** 2026-07-22

---

## 1. Executive Summary

Every one of the review's seven Required Changes identifies a real problem — none is dismissed outright. But the review is not treated as infallible here, and three of its seven proposed *remedies* are rejected or narrowed in favor of lighter, more precisely-scoped fixes, on the grounds that following the review's literal suggestion in those three cases would itself introduce the kind of governance overbuilding the review separately warns against. In one case (Chapter 0's inclusion criterion), a materially better fix than either option the review offered is derived independently. In one case (the "resilience" versus "capacity to cope" example), direct re-reading of the BMP text produces an even sharper diagnosis than the review's own — confirming its conclusion (do not presume synonymy) while improving the reasoning behind it.

Net result: all seven Required Changes are resolved (five accepted, one accepted with modification, one accepted with modification following independent re-derivation); all three of the review's own Open Questions are closed, none deferred; and one of the review's Recommended Changes is explicitly declined as scope creep belonging to a different document's future blueprint, not this one.

**Final status: Ready for Amendment.** The blueprint itself is not amended by this document — per this task's constraint — but every required decision needed before amendment is now made and recorded.

---

## 2. Resolution for Every Required Change

### RC1 — Concept-vs-Relationship promotion test

**Review's claim:** Chapter 2 (Tensions) and Chapter 5 (Business Services) catalog inherently relational BMP concepts as standalone entries, with no test analogous to ADR-023's Entity/Value-Object promotion test to guard against inconsistent treatment.

**Independent assessment:** The underlying diagnosis is correct — a tension is definitionally a pull between two interests, a service is definitionally a handoff between two capabilities, and the current template gives both the same standalone-entry treatment as an unambiguous noun like "Household." That risk is real and would compound at scale.

However, the review's implicit remedy — a formal promotion test in the style of ADR-023 — is disproportionate, and adopting it literally would reproduce exactly the "ontology creep" risk the review itself separately warns about (§8 of the review): building a formal decision-procedure apparatus, one layer up, that looks and functions like the ontology layer's own governance machinery. The blueprint's existing template already has the beginning of a correct, lighter answer: a closed **Concept Type** vocabulary and a **Type-Specific Handoff** field already designed for Business Service. The gap is not the absence of a heavyweight test — it is that neither field is currently *mandatory* or *structurally enforced* for relational concept types.

**Decision: Accepted with modification.** Tensions and Business Services remain first-class Concept Types (nodes) — not relationships — because the BMP itself already treats each as independently citable (Chapter 2 gives each tension its own named heading and reasoning; Chapter 5 gives each service its own bullet), and downstream documents need to cite "the dignity-versus-accountability tension" precisely, which is easier with a stable Concept ID than as an inferred edge between two other entries. The fix is narrower than a new promotion test: **Tension entries must mandatorily populate Related Concepts with exactly the two (or more) Interest/Objective entries in tension, using an explicit relationship label ("in tension with"); Business Service entries must mandatorily populate the Type-Specific Handoff field (already designed for this).** No new field, no new test document, no new governance apparatus — the ambiguity is closed by making two already-existing fields mandatory for two already-named Concept Types.

**Blueprint changes:** §2 (Scope) and §6 (Template) — add the mandatory-field rule above under the Concept Type definitions.
**Effect on future authoring:** Direct — Chapter 2 and Chapter 5 authors must populate these fields from the first entry drafted, not as an afterthought.

---

### RC2 — Terminology reconciliation verification (the "resilience" / "capacity to cope" example)

**Review's claim:** The blueprint's flagship reconciliation example may not survive close reading; terminology reconciliation should not be presumed uniformly safe.

**Independent assessment, going further than the review:** Re-reading Chapter 1 §1.1 ("may absorb a need for a period") against Chapter 7 §7.7 ("copes with it more effectively, *or requires less external assistance than it did before*") confirms the review's suspicion, but the review's own framing — "these may simply be two distinct concepts" — is not quite the sharpest available diagnosis. A closer read suggests neither "one concept, two labels" (the blueprint's original assumption) nor "two unrelated concepts" (the review's tentative alternative) is exactly right. Chapter 7's "resilience" is best read as a **related but distinct concept built on top of** Chapter 1's "capacity to cope": the base concept is a household's coping ability *at a point in time*; "resilience" as Chapter 7 uses it additionally commits to an *improvement trajectory across repeated shocks* that Chapter 1 never asserts. This is not two unconnected ideas — it is a base concept and a narrower, more specific concept built from it, which argues for a **Broader/Narrower relationship**, not a flat Alias, and not two disconnected entries either.

This distinction matters operationally: an Alias would silently erase the improvement-trajectory dimension; two disconnected entries would fail to show that Chapter 7's objective is *about* the same underlying household property Chapter 1 describes.

**Decision: Accepted, with the general rule strengthened beyond what the review requested.** The general Required Change — verify every Research Backlog Workstream F candidate individually against actual BMP text before merging — is adopted in full, with an added refinement: **verification must produce one of three outcomes (Alias, Broader/Narrower, or genuinely unrelated — not merely a binary "merge or don't"),** since this case demonstrates that "not a synonym" does not mean "unrelated."

**Blueprint changes:** §2 (Relationship to the Research Backlog subsection) and §3 (Responsibility 2, Deduplication) — replace the "resilience"/"capacity to cope" pairing as a *confirmed-safe* illustration with the three-outcome verification rule above, using this same pairing as the illustrative *example of why verification matters*, not an example of a safe merge.
**Effect on future authoring:** Direct — every Workstream F candidate (not only this one) now requires this three-way check before an Aliases field or a Broader/Narrower field is populated.

---

### RC3 — Concept ID uniqueness and namespacing rule

**Independent assessment:** No serious counter-argument exists here. The review is correct, the gap is real, and the fix is uncontroversial. The only judgment call is calibration: the ontology layer's own solution (`Canonical_Ontology_Schema.md` §3, CURIE-based, manifest-resolved) is heavier machinery than the business-reference layer needs, since the HBRM has no cross-domain CURIE resolution problem to solve — that begins at Ontology Design, not here.

**Decision: Accepted, calibrated down from the ontology layer's own solution.** Every Concept ID must be globally unique across the entire HBRM (not merely within its chapter), checked continuously against a running ID registry maintained during authoring — not caught only in a post-hoc pass. No CURIE, prefix, or namespace-resolution mechanism is needed at this layer; a flat global-uniqueness rule is sufficient and proportionate.

**Blueprint changes:** §6 (add the global-uniqueness rule) and §12 (add "maintain a running ID registry during authoring, checked at the moment each new ID is minted, not only in the end-of-document pass").
**Effect on future authoring:** Direct, from Chapter 0's first entry onward.

---

### RC4 — V1 Blueprint dependency

**Review's claim:** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` should be added as a mandatory cross-reference dependency, since its vocabulary (e.g., "Capabilities" in its Human Model, §5.3) could collide in label with BMP-derived HBRM entries (e.g., Chapter 4's organizational "Capabilities").

**Independent assessment — the review's remedy is rejected, though its underlying concern is not:** Checking the specific example cited: V1 Blueprint §5.3's "Capabilities" (Physical, Cognitive, Educational, Economic, Caregiving) are not merely *named* in V1 Blueprint — per that document's own §16, they are **already fully implemented in the ontology layer** as `shared/human-model/taxonomy/capabilities.yaml`. This is not a business-layer concept awaiting HBRM cataloging at all; it is already-formalized ontology content, several pipeline stages downstream of where the HBRM operates. The "collision" is therefore not a structural dependency the HBRM needs on V1 Blueprint as a *source of concepts* — it is a narrower, real, but much smaller risk: an English-language homonym between two documents using the same word ("capability") for two different things, one of which (V1's) is already fully resolved elsewhere in the repository.

Elevating this to a formal pipeline "dependency" (as the review's exact wording proposes) risks a second, subtler problem: `BUSINESS_MASTER_PLAN_RESOLUTION.md`'s Decision 2 carefully established the BMP and V1 Blueprint as "separate and complementary, neither superseding the other." Adding V1 Blueprint as an HBRM *dependency* — a term with real structural weight in this document stack (§8 of the blueprint uses it for BMP → HBRM, HBRM → Business Architecture, etc.) — risks quietly contradicting that carefully-drawn boundary by implying V1 Blueprint sits *in the pipeline* the same way the BMP does.

**Decision: Accepted with modification — the concern is real, the remedy is rescoped.** Not a pipeline dependency. Instead: add a **one-time label-collision check** to the Definition of Done (§9): every finalized HBRM Canonical Name is checked against V1 Blueprint's named vocabulary (Human/Family/Household/Needs/Risk/Support/Outcome Models) for homonym collision; where a collision exists, the HBRM entry is disambiguated (a more specific Canonical Name, or an explicit Notes-field cross-reference clarifying the distinction) — but V1 Blueprint is never treated as a source from which the HBRM derives *new* concepts, preserving the Resolution's "separate, complementary" framing intact.

**Blueprint changes:** §9 (Definition of Done) — add the label-collision check as a new item. §4 and §8 (dependency chain) are explicitly **not** changed — see §5 of this document.
**Effect on future authoring:** A final-pass check, not an ongoing authoring dependency.

---

### RC5 — Resolve Open Question 4 (mid-authoring concept invention) before authoring begins

**Independent assessment:** The review is correct that this cannot remain open once authoring starts — it is precisely the moment invention is most tempting. This one has a clean, binary answer.

**Decision: Accepted in full.** The HBRM may never contain an entry lacking a traceable, *already-ratified* BMP origin. If a future author (most plausibly, Business Architecture's) identifies a concept the BMP implies but never names — the exact situation that produced Research Backlog items RB-F2 ("Consent") and RB-F3 ("Voluntary Withdrawal") — the correct path is: confirm it is tracked in the Research Backlog; route it to a future BMP amendment; only once that amendment is itself governance-approved does the concept become eligible for an HBRM entry. No "Provisional, pending amendment" entry is permitted as a workaround. This closes Open Question 4 outright rather than leaving it open.

**Blueprint changes:** §10 (Open Questions) — remove Open Question 4 from the open list; state the resolution above directly in §2 (Scope) and §9 (Definition of Done, tightening "Origin" to mean an already-ratified BMP citation, never a placeholder).
**Effect on future authoring:** Direct and immediate — closes the exact loophole the traceability guarantee depended on remaining shut.

---

### RC6 — Chapter 0's inclusion criterion

**Review's claim:** The "referenced by three or more later HBRM chapters" test is retrospective and contradicts Architectural Principle 6 (no reorganization). The review offered two remedies: fix the criterion, or accept and document an explicit exception to Principle 6.

**Independent assessment — a third, better option exists and is adopted instead of either offered remedy:** The retrospection problem exists only because the criterion points at the *as-yet-unwritten HBRM's* future chapters. But the **BMP itself is already frozen and complete** — all nine chapters exist, in final form, right now. A criterion that instead points at the BMP's own, already-fixed cross-chapter reference pattern is knowable immediately and completely, with zero hindsight risk, because the source document being measured is not still being written.

**Decision: Accepted diagnosis; both of the review's own offered remedies rejected in favor of this independently-derived third option.** Chapter 0's inclusion criterion becomes: *a concept belongs in Chapter 0 if the frozen BMP itself already references it by name across three or more of its own nine chapters* (a fact checkable today, in full, by rereading the BMP once) — not "three or more later HBRM chapters" (a fact that cannot be known until the HBRM is mostly finished). This fully resolves the contradiction with Principle 6 without requiring any documented exception to it, and it means Chapter 0's full membership can be decided *before* any other HBRM chapter is drafted — an improvement over the original design, not merely a fix to it.

**Blueprint changes:** §7 (Chapter 0 row) — replace the inclusion criterion text as above.
**Effect on future authoring:** Chapter 0 can now be authored to completion first, exactly as §12's authoring strategy already intended, but without the "wait and see if a later chapter turns out to need it" ambiguity the original criterion introduced.

---

### RC7 — Backward reconciliation pass in the Authoring Strategy

**Review's claim:** No scheduled pass exists to catch cross-chapter duplication (the Chapter 2 "Dignity" interest versus Chapter 7 "Preservation of Dignity" objective) visible only once a later chapter is drafted.

**Independent assessment — the review is checked against the blueprint's actual text and found to have partially overstated the gap:** §12 of the blueprint already specifies, verbatim: *"After all ten chapters are drafted: run a document-wide duplication check (searching for near-duplicate definitions across chapters, not just within one)."* This already is a backward reconciliation pass — it is simply scheduled once, at the end, rather than incrementally. The review did not credit this existing provision. That said, an end-only check has a real cost the review's underlying instinct correctly identifies: later chapters may already be *built on top of* an undetected duplicate by the time the end-of-document check runs, requiring more rework to fix than an earlier catch would have.

**Decision: Accepted with modification.** The existing end-of-document check is retained as the authoritative final gate — it is not removed or replaced. A second, lightweight addition is made alongside it: after each new chapter's entries are drafted, before that chapter is considered closed, the author performs a quick name-search of each new entry against the running Concept Index built so far (not a full formal audit — a cheap, incremental check) to catch obvious cases early. This is proportionate: it adds a low-cost habit, not a new governance layer, and does not duplicate the heavier final check's job.

**Blueprint changes:** §12 (Authoring Strategy) — add the incremental per-chapter name-search step, explicitly retaining (not replacing) the existing end-of-document duplication check.
**Effect on future authoring:** A lightweight added habit per chapter; the final check remains the authoritative safety net.

---

## 3. Resolution for Every Open Question (from the Architecture Review)

**Review's Open Question 1** — "Should every Workstream F item now be presumed *not* synonymous, reversing the default?"
**Resolution: Closed.** Neither presumption is adopted. RC2's three-outcome verification rule (Alias / Broader-Narrower / unrelated) replaces any blanket default in either direction — every candidate is checked individually, with no presumption either way.

**Review's Open Question 2** — "Should the Concept-vs-Relationship promotion test live inside this blueprint or as a separate freestanding document, mirroring how the ontology layer's own promotion test has its own dedicated section?"
**Resolution: Closed.** Per RC1's resolution, no separate promotion-test document is needed at all — the fix is two mandatory field-population rules on two already-named Concept Types, recorded within the existing blueprint's §2/§6. The question is moot once the heavier remedy it presupposed is declined.

**Review's Open Question 3** — "If the backward-reconciliation pass finds two already-closed chapters' entries are genuine duplicates, what is the correction mechanism — retroactive merge or forward pointer?"
**Resolution: Closed, not deferred.** Architectural Principle 1 ("define exactly once") and the ontology layer's own precedent (`Canonical_Ontology_Schema.md` §3: "an id is frozen the moment it is written... renaming an id is a breaking change") together settle this. **An already-published Concept ID is never retroactively deleted or merged away.** Where genuine duplication is found between two closed chapters, correction is always a **forward Alias pointer** from the later-discovered entry to the earlier, established one — preserving ID stability for anything that may already cite it.

---

## 4. Blueprint Amendments Required

To be applied the next time `HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT.md` is opened for amendment (not performed by this document):

1. §2 / §6 — Mandatory field-population rules for Tension and Business Service Concept Types (RC1).
2. §2 / §3 — Three-outcome terminology-verification rule, replacing the "resilience"/"capacity to cope" pairing as a confirmed-safe example with its correct role as a cautionary illustration (RC2).
3. §6 / §12 — Global Concept ID uniqueness rule and a running ID registry maintained during authoring (RC3).
4. §9 — Label-collision check against `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`'s named vocabulary, added to the Definition of Done (RC4).
5. §2 / §9 / §10 — Firm resolution of the mid-authoring-invention question: no BMP-untraceable entries, ever; Open Question 4 removed from the open list (RC5).
6. §7 — Chapter 0's inclusion criterion rewritten to point at the frozen BMP's own cross-chapter reference pattern, not at future HBRM chapters (RC6).
7. §12 — Incremental per-chapter name-search step added alongside (not replacing) the existing end-of-document duplication check (RC7).
8. §10 — All three of the review's Open Questions removed, each closed per §3 of this document.

---

## 5. Amendments Explicitly Rejected

1. **A formal, ADR-023-style Concept-vs-Relationship promotion test as a new blueprint section or freestanding document.** Rejected as disproportionate; the lighter mandatory-field-population fix (RC1) achieves the same discipline without adding governance apparatus that would itself risk the "ontology creep" the review separately warns against.
2. **Adding `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` as a formal pipeline dependency in §4/§8's dependency-chain diagram.** Rejected; this would risk contradicting `BUSINESS_MASTER_PLAN_RESOLUTION.md`'s deliberate "separate, complementary, neither superseding" framing. The real underlying risk (label collision) is fully addressed by the narrower Definition-of-Done check adopted under RC4 instead.
3. **Both of the review's own offered remedies for Chapter 0 (fix the criterion in place, or document an exception to Principle 6).** Rejected in favor of the independently-derived third option (RC6): anchoring the criterion to the already-frozen BMP rather than to the as-yet-unwritten HBRM. This resolves the contradiction outright rather than accommodating it.
4. **The review's Recommended Change 6 — architecting, within this blueprint, the specific mechanism by which Domain Discovery would test a new domain proposal against HBRM concept boundaries.** Rejected as scope creep. Designing that mechanism is Domain Discovery's own future blueprint's responsibility, exactly as this blueprint does not (and should not) design Business Architecture's internal assignment mechanism, only the contract at the boundary. Asserting the relationship, as the current blueprint does, is sufficient at this stage; designing the other document's internal method is not this blueprint's job to pre-empt.

---

## 6. Final Blueprint Status

**Ready for Amendment.**

Every Required Change has a resolved, reasoned decision (§2). Every Open Question the review raised is closed, not deferred (§3). A complete, itemized list of the specific text amendments needed is recorded (§4), alongside an explicit record of what was considered and declined (§5), so the next author opening the blueprint for amendment has no ambiguity about what to change or why.

The blueprint document itself has not been touched by this resolution, per this task's constraint. Once the eight amendments in §4 are applied to `HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT.md`, the blueprint is positioned to move directly to a freeze decision, with no further open architectural questions outstanding from this review cycle.
