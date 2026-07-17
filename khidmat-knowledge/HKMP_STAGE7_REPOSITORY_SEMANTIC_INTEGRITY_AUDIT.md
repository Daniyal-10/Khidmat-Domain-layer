# HKMP Stage 7 — Repository Semantic Integrity Audit

**Posture:** Independent governance board review. The repository is treated as one ontology; folder and domain boundaries are ignored except as evidence of where drift becomes possible. Every prior implementation, including this program's own Stage 6 additions, is assumed wrong until the file evidence proves otherwise. No new humanitarian knowledge is proposed anywhere in this document — every finding below is either a structural defect (missing/duplicated/ambiguous wiring) or a documentation-governance gap in what already exists.

---

## 1. Executive Summary

The repository's *concept-level* discipline is genuinely strong: qualitative composition (never a numeric score), open-world assumption (unassessed ≠ absent), concept-vs-instance separation, and boundary-note documentation are applied with unusual consistency across Shared Human Model, Shared Risk, Verification Operations, and Programs. Read one domain at a time, the repository is well-built.

Read as a single graph — which is the actual test this stage sets — it is not yet coherent. Two **critical** structural gaps sit exactly at the seams the program's own stated lifecycle depends on: **Case Plan has no relationship to any intervention entity**, despite its own description explicitly claiming to coordinate interventions, and **Impact has no relationship to Beneficiary Lifecycle**, so nothing connects a measured outcome back to a household's engagement or human-development stage. Several further **major** findings show the same pattern at smaller scale: independently authored, overlapping vocabularies with no cross-reference (Support Delivery's `delivery_modality` vs. Programs' `intervention_modality`/`thematic_sectors`; `graduated` defined twice, once in Programs and once in Beneficiary Lifecycle, with no link between them); an orphaned taxonomy with no consumer anywhere (`objective_status.yaml`); and a governance ledger (`GLOSSARY.md`, `ontology_authority_matrix.md`) that is current for some domains and silent for others of equal size and maturity.

None of this requires new humanitarian knowledge to fix — every finding is a missing edge, a missing cross-reference, or a missing ledger entry, not a missing concept.

---

## 2. Repository Health Score

**68 / 100**

Scoring rationale: strong deductions for the two critical lifecycle-chain gaps (each independently disqualifying from "Certified"), moderate deductions for the recurring pattern of undocumented cross-domain overlap and inconsistent governance-ledger coverage, offset by genuinely high marks for internal domain discipline, terminological precision within each domain, and an unusually honest self-documentation culture (most gaps found here were *already* flagged in-repo as open items — this audit's contribution is mainly connecting those flags into a repository-wide picture, plus surfacing two gaps that were not previously flagged anywhere).

---

## 3. Cross-Domain Semantic Integrity

Verified strong: Shared Human Model → Shared Risk (capability/dependency/family-structure/health-condition references, all by `*_ref`, never redefinition); Registration → Needs Assessment (`need_severity`, `need_relationship_type`, both explicitly reconciled rather than duplicated); Registration → Verification Operations (claim/evidence referenced, not redefined); Risk → Registration (hazard categories reference `situations.yaml` trigger events and `health-conditions.yaml` by ref).

Verified broken or undocumented: Case Management → Programs/Registration (no intervention linkage — Finding C-1); Impact → Beneficiary Lifecycle (no relationship at all — Finding C-2); Support Delivery ↔ Programs (overlapping modality vocabulary, no cross-reference — Finding M-1); Programs ↔ Beneficiary Lifecycle (`graduated` collision — Finding M-3).

---

## 4. Entity Review

No duplicate entity `id` was found across the domains inspected (Registration, Needs Assessment, Case Management, Programs, Beneficiary Lifecycle, Impact, Shared Human Model, Shared Risk, Verification Operations, Community Context, Volunteer Operations, Support Delivery, Consent & Privacy). Entity ownership is unambiguous everywhere it was checked — every domain's `entities.yaml` carries an explicit "does not own" section and the `case` entity's dual appearance (Registration's pre-handoff view vs. Case Management's canonical record) is the one case that looks like duplication but is in fact resolved and documented (ADR-021, `ADR_RECONCILIATION_CASE.md`).

**No hidden ownership drift found at the entity level.** The drift in this repository, where it exists, is at the *relationship and taxonomy* level (see below), not entities.

---

## 5. Relationship Review

**Finding C-1 (Critical): `case_plan` has no relationship to any intervention entity.**
`case-management/ontology/entities.yaml` describes `case_plan` as "the structured, approved operational strategy guiding the coordination of interventions for a Case." `case-management/ontology/relationships.yaml` contains exactly one outbound relationship from `case_plan`: `case_plan_references_need_assertion` (to Needs Assessment). There is no relationship from `case_plan` to Programs' `intervention_offering` or to Registration's `support_intervention`. A Case Plan, as currently modeled, can reference the needs it addresses but cannot represent which interventions it has actually selected to address them — the single most load-bearing missing edge in the repository, since it is the literal junction the Stage 6 work (`offering_prerequisite_for` and its siblings) assumed would eventually be reachable from a real case.

**Finding C-2 (Critical): `impact_evaluation` has no relationship to Beneficiary Lifecycle.**
`impact/ontology/relationships.yaml` links `impact_evaluation` only to `case_management:case`. Nothing connects an impact evaluation to `beneficiary_lifecycle`'s `current_stage` (engagement) or `human_development_stage` (added Stage 6). A household can be measured as having reached `self_reliance` in an impact evaluation with no structural path for that finding to ever touch the concept that is supposed to represent it.

**Predicate reuse:** correctly applied in the one place checked in depth (Programs' `prerequisite_for`/`mutually_exclusive_with`, reused across `program`↔`program` and `intervention_offering`↔`intervention_offering`). No duplicated predicate name was found carrying two different meanings anywhere reviewed.

**Future shared-predicate candidates:** `prerequisite_for` and `mutually_exclusive_with` (currently domain-local to Programs, used across two entity pairs within that one domain) are reasonable future candidates for shared promotion if any other domain ever needs the same relationship shape — already logged as an open governance item this session; restated here as still open, not newly discovered.

---

## 6. Predicate Review

No duplicate predicate name was found bound to conflicting semantics. The repository's predicate vocabulary is small and its reuse is deliberate where it exists (Programs). The interim registry (`shared/ontology/relationships.yaml`) contains exactly one entry (`succeeded_by`) and is not yet the authoritative checkpoint §11 of `Canonical_Ontology_Schema.md` describes — this is a known, explicitly-labeled proposed-not-ratified gap (§10–§11 are marked `[PROPOSED]`), not a new finding, but it means predicate-collision checking is currently manual and undocumented per addition (see Finding M-5 below for the one place this manual check appears not to have been performed and recorded).

---

## 7. Taxonomy Review

**Finding M-1 (Major): `support-delivery/taxonomy/delivery-modalities.yaml#delivery_modality` overlaps, undocumented, with two Programs schemes.**
Its seven values mix genuine delivery-form concepts (`physical_goods`, `digital_cash_voucher`, `physical_cash_voucher`) with what are actually sector concepts (`medical_service`, `education_service`, `livelihood_service`, `protection_legal_psychosocial_service`) that duplicate the *purpose* already carried by `programs/taxonomy/structure.yaml#thematic_sectors` (`health_and_nutrition`, `education`, `livelihood`, `protection`) and overlap with `programs/taxonomy/interventions.yaml#intervention_modality`'s `service_delivery` value. Unlike nearly every other cross-domain touch in this repository, this file carries no `references:` block, no boundary note, and no acknowledgment that Programs already owns adjacent vocabulary. A senior humanitarian expert reading both files side by side would reasonably ask whether a "medical_service" delivery and a "health_and_nutrition" thematic-sector, service-modality intervention are the same fact recorded twice.

**Finding M-3 (Major): `graduated` is independently defined in two schemes with no cross-reference.**
`programs/taxonomy/eligibility-and-enrollment.yaml#enrollment_outcome.graduated` ("successfully completed the program and achieved its objectives") and `beneficiary-lifecycle/taxonomy/exit-reasons.yaml#exit_reason.graduated` ("subject achieved self-sufficiency and no longer requires support") are conceptually adjacent but not identical — one is program-completion-scoped, the other is whole-ecosystem-scoped — and that distinction is defensible. What is not defensible is that neither file mentions the other's existence. This is the exact "silent naming collision" pattern ADR-008 exists to prevent, occurring at the taxonomy-value level rather than the concept-id level, which is why it survived prior single-file reviews.

**No overlapping hierarchy or naming-convention problems** were found beyond the above. Naming style (snake_case ids, Title Case labels) is consistently applied across every taxonomy file inspected.

**Finding M-2 (Major): `case-management/taxonomy/objective_status.yaml` is an orphaned taxonomy.**
The scheme (`not_started` / `in_progress` / `achieved` / `abandoned`) exists, is well-formed, and is listed in the domain's file inventory — but no entity named `objective` exists in `case-management/ontology/entities.yaml`, and no data property anywhere in the repository declares `taxonomy_ref: objective_status`. A repository-wide search confirms zero consumers. This is not a duplicate-concept problem; it is a dangling, unreachable one — a taxonomy authored for a concept (`case_plan` objectives) that was never given an entity or property to attach to.

---

## 8. Data Properties Review

Ownership and placement were checked against domain boundaries for every property added or touched across all six stages of this program plus a sample of pre-existing properties; all resolve to their declared owning domain correctly. The one placement judgment worth re-flagging under this stricter audit: `readiness_level` (Stage 6, on Programs' `enrollment`) and `human_development_stage` (Stage 6, on Beneficiary Lifecycle's `beneficiary_lifecycle`) are each correctly scoped to the entity that represents the right level of granularity (per-enrollment for readiness; per-lifecycle for developmental stage) — reviewed again here under adversarial assumption and found sound, not merely asserted sound by their own implementation report.

**No semantic duplication** was found among data properties — every apparent near-duplicate (`need_severity` in two domains, `functional_capacity` vs. `capability_levels`, `case.status` vs. `case_plan.plan_status`) is a documented, deliberate reconciliation rather than an accidental duplicate.

---

## 9. Lifecycle Integrity

The intended chain — Registration → Needs → Case → Intervention → Impact → Beneficiary Lifecycle → Human Development — **does not currently form one traceable path.** It breaks at two points, both already identified above:

- **Case → Intervention** (Finding C-1): a Case Plan cannot reference the interventions it coordinates.
- **Impact → Beneficiary Lifecycle → Human Development** (Finding C-2): an impact measurement cannot reach the developmental-stage concept it is meant to inform.

The remaining links in the chain are intact and well-formed: Registration → Needs Assessment (`observation_based_on_claim`, `need_assertion_based_on_verified_fact`), Needs Assessment → Case (`case_plan_references_need_assertion`), Case → Support Delivery (`delivery_event fulfills case_plan` — a genuinely well-built link, correctly typed and cross-domain-referenced), and Impact → Case (`impact_evaluates_case`). The chain is therefore intact from Registration through Delivery, and separately intact from Delivery through Impact-of-a-Case — but the two critical gaps mean the chain cannot currently be walked end-to-end from a registered need through to a certified change in human development stage without a manual, out-of-band join.

---

## 10. Risk Integrity

Hazards, vulnerability, protection, and (to a lesser, correctly-scoped extent) livelihood and community compose coherently. `vulnerability.yaml`'s cascade/interaction-amplification/single-point-of-failure model, `protective-factors.yaml`'s symmetric-not-inverse design, `hazard-categories.yaml`'s category ownership, and `protection-indicators.yaml`'s deliberate placement as a sibling file (Stage 3B) rather than a bolt-on to hazard categories all hold up under adversarial re-reading. The Stage 6 rejection of a separate "Intervention Risk Category" (in favor of `hazard-categories.yaml`'s existing extensibility) is re-confirmed correct on this pass: no gap was found here on renewed scrutiny.

**One residual concern, previously flagged and still open:** `impact/ontology/relationships.yaml` contains its own author's inline comment — *"Requires promotion to Shared Vocabulary before repository freeze"* — on `impact_contains_measurement`, and a second comment noting an external-shock reference to Community Context was removed pending upstream activation. Both are honestly self-disclosed, not hidden, but both are still open at the time of this audit and belong on the record here rather than only in a code comment.

---

## 11. Readiness Integrity

This axis is a **strength**, re-verified under adversarial assumption rather than accepted on the strength of its own design rationale. Eligibility (categorical, rule-based), capability (general, intervention-independent ability), vulnerability (latent susceptibility to harm), verification confidence (trust in a specific verification conclusion), and readiness (contextual fit for a specific intervention right now) were each re-examined for whether they could collapse into one another under a skeptical reading. They cannot: each answers a genuinely different question, each is documented with an explicit boundary note distinguishing it from its nearest neighbors, and none was found to silently duplicate another. Human development stage (also reviewed here as a sixth, newer member of this family) is likewise distinct from all five, provided the heavy cross-referencing documentation added in Stage 6 is not later trimmed — which this audit flags as the one condition on which this "strength" finding depends.

---

## 12. Impact Integrity

**Does not yet form one coherent model.** Outcomes (`impact/taxonomy/outcomes.yaml`), indicators (`impact/taxonomy/indicators.yaml`), human development stage (`beneficiary-lifecycle`), graduation (independently in both Programs and Beneficiary Lifecycle — Finding M-3), resilience, and community contribution are each well-modeled in isolation but are not wired together. Impact measures a Case; nothing propagates an impact finding into a change of human development stage, and nothing distinguishes, at the taxonomy level, whether "graduated" (Programs) and "resilience"/"community_contribution" (human_development_stage) are meant to correspond to specific `outcome_type`/`persistence_horizon` combinations in Impact's own vocabulary or are entirely independent judgments. This is the same underlying defect as Finding C-2, restated at the taxonomy-composition level rather than the relationship level.

---

## 13. Governance Review

**ADR compliance:** no ADR is contradicted by anything found in this audit. ADR-008 (Single Ownership) is the standard most directly implicated by Findings M-1 and M-3 — neither is a redefinition of an owned concept, so neither is a strict ADR-008 violation, but both are the kind of silent, undocumented overlap ADR-008's spirit exists to prevent, and both would fail a promotion review if one were ever conducted against them.

**Authority Matrix:** internally consistent for the domains it covers, but its coverage itself is inconsistent — see Section 15.

**Cross-references:** the repository's general discipline of documenting *why* a reference exists (seen throughout Shared Human Model, Shared Risk, and this program's own Stage 2A/3B/5B/6 additions) is excellent where it is applied, which makes its *absence* in Support Delivery's `delivery_modality` and Beneficiary Lifecycle's `graduated` value stand out as clear deviations from an otherwise well-established norm, rather than the norm itself being weak.

---

## 14. Glossary Review

**Finding M-4 (Major): `GLOSSARY.md` has no section for Needs Assessment, Case Management, Beneficiary Lifecycle, Programs, Community Context, Support Delivery, or Volunteer Operations**, despite each of these being a substantially built-out, canonical, active domain with its own rich vocabulary (`assessment_session`, `need_assertion`, `case_plan`, `engagement_stage`, `intervention_offering`, `enrollment`, `settlement_types`, `delivery_event`, `volunteer_profile`, and dozens more). Existing sections cover only Core Terms (Registration), Human Model Terms, Risk and Vulnerability Terms, Verification Operations Terms, Outcome Terms (Impact, partially), and Governance Terms. This is not an oversight isolated to one domain; it is a repository-wide pattern in which the Glossary was evidently maintained faithfully during some phases of this program's history and not others.

---

## 15. Authority Matrix Review

**Finding M-6 (Major): Registration and Programs — two of the largest, most mature, canonical domains in the repository — have no dedicated section in `ontology_authority_matrix.md`.** Every other domain reviewed (Shared Ontology, Shared Human Model, Risk, Verification Operations, Beneficiary Lifecycle, Needs Assessment, Case Management, Volunteer Operations, Shared Time, Consent & Privacy) has one. Registration's and Programs' concepts appear in the matrix only incidentally, as targets referenced *from* other domains' sections (e.g., `need_severity`, `claim`, `need_relationship_type` under Needs Assessment's "Explicit References Only"). This means there is no single place to check "who owns `case`, `need`, `situation`, `program`, `intervention_offering`, `enrollment`" the way the matrix promises to be for every other concept in the repository — an internal inconsistency in the governance ledger itself, not merely an omission.

---

## 16. README Review

Every README inspected accurately describes its own domain's current state, including honest "Does Not Own" sections — this is a genuine, repeatedly-verified strength. The one class of README inconsistency found: domain READMEs updated during this program's six stages (Registration, Needs Assessment, Beneficiary Lifecycle, Programs, Support-affiliated Risk) now reflect their new concepts, but no README anywhere documents the two critical cross-domain gaps found in this audit (Case Management's README does not mention that `case_plan` cannot yet reference an intervention; Impact's README does not mention its missing link to Beneficiary Lifecycle) — an expected consequence of those gaps existing, not an independent finding.

---

## 17. ADR Review

No ADR requires amendment as a result of this audit. ADR-008 (Single Ownership), ADR-013 (Concept vs. Instance Separation), and ADR-021 (Case Lifecycle Handoff) were the three most load-bearing for this review's findings and all three remain correctly applied wherever they govern a decision actually reviewed here. No ADR was found to conflict with another.

---

## 18. Architectural Debt

Consolidated list of items already known and open (not new findings, restated here for a single point of reference per this audit's own requirement):
- Predicate-modeling harmonization (C-2 / Shared Predicate Manifest) — logged this session, still open.
- `humanitarian_sector` (Shared Ontology) reserved but unpromoted; `need_assertion.thematic_sector` still sources from `programs_tax:thematic_sectors` instead.
- `functional_capacity` in `shared/taxonomy/persons.yaml` not yet retired in favor of `capabilities.yaml`'s scale, despite FLAG-001 calling for it.
- `impact_contains_measurement`'s self-flagged "requires promotion to Shared Vocabulary before repository freeze."
- Community Context's `external_shock` reference from Impact, deferred pending that domain's own activation.

---

## 19. Minor Issues

- `functional_capacity` retirement still pending (Section 18).
- `humanitarian_sector` promotion still pending (Section 18).
- README/glossary lag behind the newest concepts in a small number of files not touched by this program's own six stages (general staleness risk, not a specific defect located).

## 20. Major Issues

- **M-1:** Support Delivery's `delivery_modality` overlaps Programs' `intervention_modality`/`thematic_sectors` with no cross-reference.
- **M-2:** `objective_status.yaml` is an orphaned taxonomy with no entity or property anywhere consuming it.
- **M-3:** `graduated` independently defined in Programs and Beneficiary Lifecycle with no cross-reference.
- **M-4:** `GLOSSARY.md` has no coverage for seven active, canonical domains.
- **M-6:** `ontology_authority_matrix.md` has no dedicated section for Registration or Programs.

## 21. Critical Issues

- **C-1:** `case_plan` has no relationship to any intervention entity, despite its own description claiming to coordinate interventions.
- **C-2:** `impact_evaluation` has no relationship to Beneficiary Lifecycle; no structural path exists from a measured outcome to a household's engagement or human-development stage.

---

## 22. Repository Strengths

- Qualitative-composition discipline (no numeric scoring anywhere a judgment is recorded) applied with genuine, verified consistency across Risk, Verification Operations, and Programs.
- Open-world assumption applied uniformly and correctly — "not assessed" is never conflated with a negative value anywhere this was checked.
- Concept-vs-instance separation (ADR-013) correctly maintained in every domain reviewed.
- Boundary-note and "Does Not Own" documentation culture is exceptional by ontology-engineering standards and is what made most of this audit's findings *discoverable* rather than hidden — the repository's own honesty is why this review could be this specific.
- The readiness/eligibility/vulnerability/capability/human-development-stage family is, on adversarial re-examination, genuinely well-differentiated — a real strength, not merely an assertion carried over from prior stages.
- Predicate reuse (Programs' `prerequisite_for`/`mutually_exclusive_with`) is a correct, ratified-schema-conformant pattern, independently re-verified in this audit.

---

## 23. Certification Decision

**Repository Requires Remediation.**

The two critical findings (C-1, C-2) sit at exactly the junctions this program's own stated lifecycle model depends on — a Case Plan that cannot reference an intervention, and an Impact evaluation that cannot reach Beneficiary Lifecycle, mean the repository cannot currently support the single most basic humanitarian question the entire six-stage program was built toward: tracing one household from registered need through to a certified change in human development stage, as one connected graph. This disqualifies "Certified" and "Certified with Minor Findings" outright, regardless of the genuine strength of the domain-internal modeling. The findings are not, however, severe enough to warrant "Not Ready" — every gap identified is a missing edge or a missing cross-reference against already-existing, well-modeled concepts, not a missing or incoherent concept requiring redesign. Remediation here is edge-adding and ledger-updating work, not re-architecture.
