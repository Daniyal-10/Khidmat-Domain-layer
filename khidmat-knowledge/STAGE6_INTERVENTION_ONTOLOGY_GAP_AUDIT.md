# STAGE 6 — Intervention Ontology & Taxonomy Gap Audit

**Source of truth audited:** the Humanitarian Intervention Intelligence Report (Stage 6, Research Pass 2), checked against the full repository — `registration/` (including the `support-interventions.yaml` placeholder), `needs-assessment/`, `case-management/` (entities, relationships, taxonomy: case_origin, case_plan_status, case_status, closure_reason, delegation_status, follow_up_status, objective_status, priority_level, referral_status, referral_type, suspension_reason), `programs/` (entities, relationships, taxonomy: interventions, eligibility-and-enrollment, structure, lifecycle-and-status, funding-and-compliance, governance-and-exceptions), `impact/` (taxonomy: indicators, outcomes, evaluation, measurement, attribution), `beneficiary-lifecycle/` (taxonomy: engagement-stage, exit-reasons, review-triggers, suspension-reasons), `shared/human-model/`, `shared/risk/`, `community-context/`, `volunteer-operations/`, and `consent-and-privacy/`.

**Scope discipline applied throughout:** every candidate below was checked against the golden rule (stable, reusable, universally true, humanitarian knowledge, decades-durable) before being listed. Operational reasoning ("cash should only be given if markets function," "business grants fail when skills are absent") is explicitly excluded per instruction — those statements are reasoning-system material, not ontology, and do not appear as gaps here even though the source report is built almost entirely from statements of that shape. Only the *permanent conceptual scaffolding* those statements presuppose — a place to record that a prerequisite relationship, a readiness state, or a risk category exists at all — is in scope.

---

## Already Represented (no gap)

Before listing gaps, it is necessary to record what the repository already covers, to keep the burden of proof honest:

- **Intervention delivery modality** (cash, voucher, in-kind, service, asset transfer) — `programs/taxonomy/interventions.yaml#intervention_modality`.
- **Conditionality** (unconditional, health/school attendance, public works) — `programs/taxonomy/interventions.yaml#conditionality_types`.
- **Graduation/milestone phasing** (intake-consumption, asset transfer, skill certification, graduation readiness) — `programs/taxonomy/interventions.yaml#milestone_types`.
- **Eligibility category and logic** (demographic, means-tested, geographic, vulnerability-scored; operators) — `programs/taxonomy/eligibility-and-enrollment.yaml`.
- **Enrollment state and outcome** (applied, waitlisted, active, suspended, exited; graduated, terminated, transitioned) — same file.
- **Waitlist prioritization method** — same file.
- **Program-to-program prerequisite and mutual exclusivity** — `programs/ontology/relationships.yaml#program_prerequisite_for`, `#program_mutually_exclusive_with`.
- **Thematic sector classification** (WASH, food security, health, shelter, education, livelihood, protection, social protection) — `programs/taxonomy/structure.yaml#thematic_sectors`.
- **Case-level objective progress** (not_started, in_progress, achieved, abandoned) — `case-management/taxonomy/objective_status.yaml`.
- **Case-level closure and suspension reasons, referral type/status, follow-up** — `case-management/taxonomy/*`.
- **Beneficiary ecosystem exit reasons** (graduated, deceased, relocated, requested removal, code-of-conduct violation) — `beneficiary-lifecycle/taxonomy/exit-reasons.yaml`.
- **Impact indicator typing** (objective/subjective/proxy/composite; category; hierarchy) — `impact/taxonomy/indicators.yaml`.
- **Outcome durability and relapse** (temporary/sustained/irreversible; rapid/gradual/no decay; full/partial/prevented relapse) — `impact/taxonomy/outcomes.yaml`. This is a materially strong match to the Report's "success indicator / failure indicator / stopping condition" language, deliberately generic across all intervention types rather than duplicated per type — consistent with this repository's established preference (seen already in `capabilities.yaml`, `protective-factors.yaml`) for one generic, cross-cutting concept over per-instance proliferation.
- **Household earner/caregiver/skill capacity, financial buffer, livelihood diversity** — `shared/human-model/`, `shared/risk/taxonomy/protective-factors.yaml` (audited in Stage 5A).
- **Community-level macro-economic base and market pattern** — `community-context/taxonomy/livelihood-patterns.yaml` (audited in Stage 5A).

The gaps below are the residue after this substantial existing coverage is accounted for.

---

## Gap 1 — Intervention Objective Category

**Gap title:** No taxonomy distinguishes the underlying humanitarian *purpose* of an intervention from its delivery modality or thematic sector.

**Humanitarian justification:** The Report's entire per-intervention analysis is organized around "what problem does it solve" — and that problem is neither the delivery modality (cash vs. voucher vs. asset) nor the thematic sector (livelihood vs. health vs. shelter). It is a third, distinct axis: is this intervention meant to preserve survival, restore a prior baseline, build a new capacity, protect from harm, connect to an existing opportunity, or build resilience against a future shock? A cash transfer and a business grant are both `intervention_modality` values, but one is typically survival/stabilization-oriented and the other is capacity-building-oriented — a distinction the current taxonomy has no way to express.

**Why it is permanent knowledge:** These purpose categories (survival/stabilization, restoration, capacity-building, protective, connective/market-linkage, resilience-building) are not tied to any specific programme, funding cycle, or country context — they describe the enduring shape of humanitarian purpose itself, the same today as they will be in decades, independent of which specific interventions exist in a catalogue at any given time.

**Recommended ontology artifact:** New taxonomy scheme (e.g., `intervention_objective_category`), most naturally owned alongside `programs/taxonomy/interventions.yaml#intervention_modality` as a sibling scheme, with `intervention_offering` gaining a corresponding data property referencing it.

**Priority:** High.

**Expected humanitarian impact:** Enables any future reasoning layer to distinguish "this intervention is solving the stated need" from "this intervention is solving a different, adjacent need," which is the exact diagnostic discipline the Report treats as the foundation of all correct intervention selection.

---

## Gap 2 — Intervention-Level Prerequisite and Incompatibility (Instance-Level, Not Program-Level)

**Gap title:** Prerequisite and mutual-exclusivity relationships exist only between whole Programs, not between individual Interventions (or between a Need and an Intervention).

**Humanitarian justification:** The Report is emphatic and specific that individual interventions — not whole programs — depend on and preclude one another: vocational training depends on a confirmed market opportunity; a business grant depends on confirmed skill; cash assistance and business support "should never be combined without a clear rationale" in some configurations. `program_prerequisite_for` and `program_mutually_exclusive_with` (`programs/ontology/relationships.yaml`) capture this only at the level of "Program A must precede Program B" — an institutional-initiative-level fact. There is no equivalent at the level of `intervention_offering`, which is the entity actually delivered to a specific household.

**Why it is permanent knowledge:** That some interventions structurally depend on others, and some are structurally incompatible, is a fact about the nature of the interventions themselves — true regardless of which specific programme catalogue is active in a given country or year, and directly mirrors a pattern this repository has already adopted once before, at the Registration/Needs Assessment layer (`need_influences_need`, added Stage 2A), for the identical underlying problem: two things of the same kind that can causally depend on, block, or compound one another.

**Recommended ontology artifact:** A relationship on `intervention_offering` (self-referential), analogous in shape to the existing `program_prerequisite_for`/`program_mutually_exclusive_with` pair — most consistent with this repository's own established precedent (`need_influences_need`) to use one generic relationship with a controlled qualifier rather than several separately-named relationships.

**Priority:** Critical — this is the single most load-bearing gap in the audit, since nearly every "prerequisite," "dependency," "sequencing," and "incompatibility" theme in the source report reduces to this one missing structural relationship.

**Expected humanitarian impact:** Allows a case plan to represent, durably and queryably, that this household's business grant is contingent on their vocational training completing first — the exact structural fact the Report treats as the difference between a livelihood pathway that succeeds and one that fails.

---

## Gap 3 — Readiness (Distinct from Eligibility)

**Gap title:** No concept represents a household's or enterprise's qualitative readiness for a specific intervention, as distinct from formal eligibility.

**Humanitarian justification:** Eligibility (`programs/taxonomy/eligibility-and-enrollment.yaml`) answers "does this household qualify under the programme's rules" — a categorical, rule-based determination (demographic, means-tested, geographic, vulnerability-scored). The Report's "Livelihood Readiness," "Market Readiness," and "Enterprise Readiness" answer a different question entirely: given that a household qualifies, is the *context and capacity* actually present for this specific intervention to succeed right now (skill present, market not saturated, household support secured, logistics feasible)? A household can be fully eligible and completely unready, or occasionally ready without yet being formally eligible.

**Why it is permanent knowledge:** This distinction — formal qualification versus actual contextual readiness — is a stable, universal humanitarian concept independent of any specific programme's rules, and follows the same qualitative-composition pattern already established and governed for `vulnerability_level` and `capability_level` (a structured, named judgment, never a computed score) in `shared/risk/ontology/vulnerability.yaml` and `shared/human-model/taxonomy/capabilities.yaml`.

**Recommended ontology artifact:** A new taxonomy scheme (e.g., `intervention_readiness_level`, mirroring the existing four-level qualitative pattern already used elsewhere in this repository) and a corresponding data property, most naturally scoped at the point where a specific need or capability is being matched to a specific `intervention_offering` — likely Case Management or Programs, not Registration.

**Priority:** High.

**Expected humanitarian impact:** Gives a durable, structured home to the exact judgment the Report's sewing-machine example walks through in such granular detail — currently, none of those fifteen questions has anywhere permanent to be recorded as a conclusion.

---

## Gap 4 — Intervention Risk Category

**Gap title:** No controlled vocabulary exists for the *kind* of risk a specific intervention carries.

**Humanitarian justification:** The Report insists that every intervention be assessed for "what risks exist" — market saturation, dependency creation, diversion, asset loss, relational strain within the household, exploitation of a vulnerable recipient. These are recurring, nameable categories of risk specific to intervention delivery, distinct from the household-level hazard categories already owned by the Risk Domain (environmental, economic, health, social protection, legal/administrative), which describe risk *to the household from its environment*, not risk *introduced by the intervention itself*.

**Why it is permanent knowledge:** These risk categories recur across every kind of intervention and every country context — market saturation risk applies whether the intervention is a sewing machine in one country or a livestock transfer in another — and are stable, nameable categories independent of any specific programme design.

**Recommended ontology artifact:** A new, small, closed taxonomy scheme (e.g., `intervention_risk_category`), most naturally owned by Programs or Case Management as a qualifier on `intervention_offering`, following the same "closed, small, illustrative-not-exhaustive" design discipline already established for `shared/risk/taxonomy/hazard-categories.yaml` and `protection-indicators.yaml`.

**Priority:** Medium.

**Expected humanitarian impact:** Allows risk to be recorded as a structured fact about a specific intervention rather than only existing as prose guidance for a case worker to remember unaided.

---

## Gap 5 — Human Development / Recovery Trajectory Stage

**Gap title:** No concept represents a household's own developmental trajectory (crisis → recovery → stability → self-reliance → resilience → community contribution), as distinct from the beneficiary's administrative relationship to Khidmat's ecosystem.

**Humanitarian justification:** `beneficiary-lifecycle/taxonomy/engagement-stage.yaml`'s `engagement_stage` (identified → registration_initiated → registered → verification_pending → active → engaged → monitored → suspended → review_required → exited) is a rigorous and complete model of the beneficiary's *administrative and operational relationship* to Khidmat. It is not, and was never intended to be, a model of the household's own *humanitarian developmental trajectory* — a person can be "engaged" in the ecosystem for years while remaining in crisis, or can be administratively "exited" while genuinely at the resilience or community-contribution stage the Report treats as the actual measure of success. These are two independent axes that the current taxonomy conflates by having only one of them.

**Why it is permanent knowledge:** The crisis-to-community-contribution arc is the central organizing frame of the entire Report and, more broadly, of humanitarian practice generally — a universal, decades-stable concept entirely independent of any organization's specific case-management workflow.

**Recommended ontology artifact:** A new taxonomy scheme (e.g., `human_development_stage`), most naturally owned alongside or cross-referenced from `beneficiary-lifecycle/taxonomy/engagement-stage.yaml`, explicitly documented as a distinct, non-overlapping axis from `engagement_stage` — mirroring the existing, already-successful precedent of keeping `need_severity` (Registration's claimed severity) and `need_assertion.need_severity` (Needs Assessment's synthesized severity) as deliberately separate, cross-referenced concepts rather than one conflated field.

**Priority:** Critical — this is the second most load-bearing gap in the audit, because it underlies the entire "Human Potential" / "Long-Term Outcomes" section of the source report and has no existing conceptual home anywhere in the repository, including Impact, which measures outcomes but does not classify the household's own developmental stage.

**Expected humanitarian impact:** Allows the organization to track and reason about the actual measure of humanitarian success the Report insists on — movement along this trajectory — rather than only the administrative status of the case.

---

## Gap 6 — Intervention Combination Relationship (Reinforces / Substitutes)

**Gap title:** No relationship represents that two interventions reinforce each other's effect (as distinct from one being a strict prerequisite for the other) or that two interventions are substitutes for the same underlying need.

**Humanitarian justification:** The Report is explicit that some interventions "naturally work together" and reinforce each other without either being a hard prerequisite (mentoring alongside a business grant), while others are outright substitutes for the same underlying need (employment placement versus business support) rather than either a dependency or an incompatibility. Gap 2 above captures prerequisite and incompatibility; it does not capture this third, softer relationship pattern of mutual reinforcement or substitution, which the Report treats as equally important to correct sequencing.

**Why it is permanent knowledge:** Which interventions reinforce each other and which are substitutes for the same gap is a stable fact about the interventions' own nature, not a policy choice specific to any programme.

**Recommended ontology artifact:** Extension of the same relationship/qualifier structure recommended in Gap 2 with two additional qualifier values (e.g., `reinforces`, `substitutes_for`) rather than a wholly separate relationship — consistent with the "single generic relationship, controlled qualifier" design principle this repository has already committed to.

**Priority:** Medium — naturally bundled with Gap 2's implementation rather than a separate structural addition.

**Expected humanitarian impact:** Completes the relationship vocabulary needed to represent the Report's full combination logic, not just its sequencing logic.

---

## Summary Table

| Gap | Artifact Type | Priority |
|---|---|---|
| 1. Intervention Objective Category | Taxonomy (new scheme) | High |
| 2. Intervention-Level Prerequisite/Incompatibility | Relationship (instance-level, mirroring existing program-level and need-level precedent) | Critical |
| 3. Readiness (distinct from Eligibility) | Taxonomy (new scheme) + Data Property | High |
| 4. Intervention Risk Category | Taxonomy (new, small, closed scheme) | Medium |
| 5. Human Development / Recovery Trajectory Stage | Taxonomy (new scheme, cross-referenced against engagement_stage) | Critical |
| 6. Intervention Combination (reinforces/substitutes) | Relationship qualifier extension (bundled with Gap 2) | Medium |

---

## Final Decision

**Moderate canonical enrichment recommended.**

The repository's existing coverage of intervention modality, eligibility, enrollment, graduation phasing, case-level objective tracking, and generic impact/outcome measurement is extensive and requires no further work. The gaps identified are real, permanent, and well-bounded — two of them (instance-level intervention dependency, and the human development trajectory distinct from ecosystem engagement status) are structurally significant enough to warrant "Critical" priority, since large parts of the source report's reasoning have no conceptual home to attach to without them. None of the six gaps requires a new entity, a new domain, or any architectural redesign — each extends an existing, already-owned file using patterns this repository has already established and validated for structurally identical problems elsewhere.
