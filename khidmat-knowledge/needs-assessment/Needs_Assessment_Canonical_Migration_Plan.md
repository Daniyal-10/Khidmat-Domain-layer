# Needs Assessment — Canonical Migration Audit & Plan

## Purpose

Full repository audit comparing the legacy monolith
(`needs-assessment/ontology.yaml`, `needs-assessment/taxonomy.yaml`) against
the canonical structure (`needs-assessment/ontology/*.yaml`,
`needs-assessment/taxonomy/*.yaml`), a complete concept mapping, every live
downstream dependency, and a phased migration plan that reaches 100%
semantic coverage without breaking any existing reference. **No files are
modified in this pass** — analysis and planning only, per instruction.

This supersedes nothing in `Needs_Assessment_Legacy_Migration_Dependency_Report.md`;
it broadens that file's dependency table into a full entity/taxonomy/
relationship/constraint mapping and adds the concepts that already point at
the canonical folder.

---

## 1. Headline Finding

Both concept sets are simultaneously "live" today, in different roles:

- The **canonical folder** (`ontology/`, `taxonomy/`) is already the
  integration contract that other migrated domains code against —
  `case-management`, `impact`, `support-delivery`, and
  `verification-operations` all hold live CURIEs like
  `needs_assessment:need_assertion` and `needs_assessment:assessment_session`.
  None of these would break if the legacy monolith were deleted today.
- The **legacy monolith** is still the file of record for governance —
  `ontology_authority_matrix.md`, `knowledge_layer_inventory.md`,
  `knowledge_layer_roadmap.md`, and `needs-assessment/README.md` all describe
  only the legacy concept set, and one real dependent
  (`registration/taxonomy/needs.yaml`'s `need_severity` placeholder,
  Registration decision D5) is explicitly deferred pending this domain's
  migration.

So retiring the monolith is not blocked by breakage risk to consumers (they
already moved on) — it is blocked by (a) three legacy concepts with **no
canonical equivalent at all**, (b) two legacy relationships with no canonical
equivalent, (c) one real structural divergence in how supersession is
modeled, and (d) stale governance documents that need to be resynced.

---

## 2. Entity Mapping

| Legacy (`ontology.yaml`) | Canonical (`ontology/entities.yaml`) | Relationship |
|---|---|---|
| `Assessment` | `assessment_session` | Narrowed match — session lacks legacy's depth/urgency/methodology axes (see §3). Legacy's `uses → AssessmentTool` also fragments into two canonical entities: `assessment_instrument` + `assessment_indicator`. |
| `AssessmentFinding` | **split** across `observation` + `need_assertion` | Legacy conflates raw evidence and synthesized conclusion into one entity ("objective observations and conclusions"). Canonical deliberately separates them: `observation` is raw/uninterpreted, `need_assertion` is the synthesized output. This is the central structural divergence between the two models. |
| `IdentifiedNeed` | `need_assertion` | Direct match — canonical's own label is "Need Assertion (Finding)". |
| — | `assessment_indicator` | **Canonical-only.** No legacy analogue; legacy's `AssessmentTool` reference was monolithic (one opaque tool), canonical decomposes it into instrument + measured indicator. |
| — | `finding_consensus` | **Canonical-only.** Governance record resolving conflicting findings. Legacy has no consensus/dispute-resolution entity at all — `finding_confidence` is a scalar property, not a governance process. |
| — | `supervisor_review` | **Canonical-only.** QA gate entity. No legacy analogue. |
| — | `assessor_calibration` | **Canonical-only.** Bias-correction governance process. No legacy analogue. |
| — | `reassessment_trigger` | **Canonical-only.** Legacy's `superseded_by` captures the *result* of a reassessment but has no entity for what *mandates* one. |

Canonical adds 5 wholly new governance/QA entities the legacy monolith never
modeled (consensus, review, calibration, reassessment triggers) — this is
real semantic growth, not just a rename exercise.

---

## 3. Taxonomy (Scheme) Mapping

| Legacy (`taxonomy.yaml`) | Canonical | Status |
|---|---|---|
| `assessment_status` (planned / in_progress / completed / discontinued) | `session_status` (scheduled / in_progress / completed / partially_completed / interrupted / abandoned) | Renamed + expanded. `planned→scheduled`, `discontinued→abandoned`; canonical adds `partially_completed` and `interrupted` as distinct terminal/recoverable states, backed by `ontology/lifecycle-constraints.yaml`. |
| `assessment_scope` (individual / household / community) | *(not a taxonomy)* — realized as relationships `session_evaluates_person` / `session_evaluates_household` / `session_evaluates_community` | Converted from an enum property to structural relationships. Semantically equivalent, mechanically different — matters for any consumer that expects a scalar field. |
| `finding_confidence` (very_high / high / medium / low) | `confidence_level` (high / medium / low / highly_uncertain) | Renamed. **Value sets are not identical**: legacy has a `very_high` tier with no canonical counterpart; canonical's `highly_uncertain` reads as lower than legacy's `low`. Also scope changed: legacy restricts this to `AssessmentFinding`; canonical applies `confidence_level` to **both** `observation` and `need_assertion` (`data-properties.yaml` domain: `[observation, need_assertion]`) — canonical explicitly widens what legacy's own constraint #4 forbade ("`finding_confidence` applies exclusively to AssessmentFindings"). |
| `need_severity` (critical / high / medium / low) | `need_urgency` (critical / severe / moderate / mild / none) | Renamed. Value crosswalk is not 1:1: canonical relabels `high→severe`, `medium→moderate`, `low→mild`, and adds a `none` tier legacy has no equivalent for. |
| `assessment_depth` (rapid / detailed) | **none** | **Gap.** No canonical scheme carries this axis (rapid vs. detailed triage-depth). Not the same axis as `assessment_modality` (channel) or `session_status` (lifecycle). |
| `assessment_urgency` (routine / emergency — triage pressure on the *assessment event*) | **none** | **Gap.** Distinct from canonical `need_urgency`, which describes the severity of the *outcome*, not the triage pressure driving the *assessment itself*. No canonical equivalent exists. |
| `assessment_methodology` (structured / semi_structured / observational / participatory / clinical / mixed_method) | **none** | **Gap.** Canonical `assessment_modality` (in_person_interview / remote_phone / direct_observation / digital_self_service) is a different axis — delivery channel, not methodological class. No canonical scheme covers this. |
| — | `evidence_type` (declared / proxy_reported / observed / verified / inferred) | **Canonical-only.** No legacy analogue — legacy had no epistemological-source classification for evidence. |
| — | `conflict_status` (consistent / internal_conflict / external_conflict) | **Canonical-only.** No legacy analogue. |
| — | `missing_data_reason` (beneficiary_refusal / safety_risk / language_barrier / session_interrupted / not_applicable) | **Canonical-only.** No legacy analogue. |
| — | `invalidation_reason` (mass_disaster / superseded / fraud_detected) | **Canonical-only.** Legacy has an `invalidated` concept only implicitly, via prose constraint #3; canonical formalizes *why*. |
| — | `session_status`, `assessment_modality` | Already covered above / canonical-only respectively. |

Three legacy taxonomy schemes (`assessment_depth`, `assessment_urgency`,
`assessment_methodology`) have **zero canonical equivalent** — these are the
concrete gaps blocking 100% coverage, not merely renames.

---

## 4. Relationship Mapping

| Legacy (`ontology.yaml`) | Canonical (`ontology/relationships.yaml`) | Status |
|---|---|---|
| `assesses` (Assessment → Subject) | `session_evaluates_person` / `_household` / `_community` | Matches, split by scope per §3. |
| `uses` (Assessment → AssessmentTool) | `session_uses_instrument` (→ `assessment_instrument`) | Matches, narrower target type. |
| `produces` (Assessment → AssessmentFinding) | `session_yields_observation` (→ `observation`) | Matches in shape but not in target semantics — canonical session produces raw *observations*, not synthesized findings directly (see §2 split). |
| `synthesizes_into` / `synthesized_from` (AssessmentFinding ↔ IdentifiedNeed) | `observation_synthesizes_into` / `assertion_synthesized_from` (observation ↔ need_assertion) | Same relationship name and cardinality shape; source-side entity changed per the AssessmentFinding split. |
| `belongs_to` (AssessmentFinding → Assessment) | implicit inverse of `session_yields_observation` (`observation_from_session`) | Matches. |
| `based_on_claim` (AssessmentFinding → registration:RegistrationClaim) | **none** | **Gap.** No canonical relationship links `observation` or `need_assertion` to a Registration claim. |
| `based_on_verified_fact` (AssessmentFinding → verification:VerificationFinding) | **none in `needs-assessment/ontology/`** | **Gap** on this side. The link exists only as prose on the *other* domain (`verification-operations/taxonomy/verification-findings.yaml:165-170`, `scheme: needs_assessment:need_assertion, relation: supplies_values_for`) — there is no formal relationship edge declared from the needs-assessment side. |
| `affects` (IdentifiedNeed → Subject) | **none** | **Gap.** Canonical `need_assertion` has no direct edge to the evaluated subject; the subject is only reachable transitively via `assessment_session → observation → need_assertion`. May be intentional (avoid duplicate edges) but needs a content-owner call. |
| `belongs_to_sector` (IdentifiedNeed → shared:HumanitarianSector) | `thematic_sector` data-property (`taxonomy_ref: programs_tax:thematic_sectors`) | Matches conceptually, but changed **type** (relationship → data property) and **owning domain** (Shared → Programs). |
| `superseded_by` / `supersedes` (IdentifiedNeed ↔ IdentifiedNeed, self-referential) | `session_supersedes_assertion` / `assertion_superseded_by_session` (assessment_session → need_assertion) | **Structural divergence, not a rename.** Legacy models supersession as one need replacing another directly. Canonical models it as a new *assessment session* superseding a prior *assertion*. Different actors, different cardinality implications — needs an explicit content-owner ratification (see D6 below). |
| — | `session_conducted_by_person`, `session_conducted_by_org` | **Canonical-only.** Legacy never modeled who/what organization conducted the assessment. |
| — | `observation_evaluates_indicator` | **Canonical-only**, supports the new `assessment_indicator` entity. |
| — | `consensus_resolves_finding`, `consensus_reviews_observation` | **Canonical-only**, supports `finding_consensus`. |
| — | `review_audits_session` | **Canonical-only**, supports `supervisor_review`. |
| — | `calibration_audits_assessor` | **Canonical-only**, supports `assessor_calibration`. |
| — | `trigger_initiates_session` | **Canonical-only**, supports `reassessment_trigger`. |

---

## 5. Constraint Mapping

| Legacy (`ontology.yaml` constraints, prose) | Canonical equivalent | Status |
|---|---|---|
| "Every AssessmentFinding belongs to exactly one Assessment." | Enforced structurally via `session_yields_observation` cardinality + single `from` on observation-side relationships. | Matches, now structural instead of prose. |
| "An IdentifiedNeed must be synthesized from at least one AssessmentFinding." | `observation_synthesizes_into` cardinality `{min:1, max:unbounded}`. | Matches, now structural. |
| "IdentifiedNeeds remain authoritative until superseded..." | `taxonomy/finding.yaml#finding_status` (`authoritative` state) + `ontology/lifecycle-constraints.yaml` (`need_assertion` lifecycle: `authoritative → expired/invalidated`) + `invalidation_reason` scheme. | Matches — canonical is *more* richly modeled here (explicit state machine + reasons vocabulary vs. one sentence). |
| "finding_confidence applies exclusively to AssessmentFindings..." | Contradicted — canonical `confidence_level` domain is `[observation, need_assertion]`, i.e. both. | **Divergence**, not a gap — a deliberate canonical broadening that should be called out explicitly rather than silently inherited. |
| "The Needs Assessment domain consumes evidence by reference but never creates new evidence records outside of its own synthesized findings." | Arguably **inverted** — canonical's `observation` entity, populated via `session_yields_observation`, *is* an evidence record created and owned within this domain, not merely a reference. | **Divergence.** This is an architectural stance change worth a content-owner sign-off, not a mechanical carry-forward. |
| — | `ontology/semantic-constraints.yaml` (5 constraints: session-must-evaluate-a-subject, missing-data-requires-reason, invalidated-requires-reason, consensus-must-resolve-finding, safety-risk-triggers-escalation) | **Canonical-only.** No legacy analogue for any of these five — they formalize edge cases (missing data, safety escalation) the legacy monolith left unaddressed. |

---

## 6. Downstream Dependency Inventory (full repo scan)

### 6a. Already targeting canonical concepts (no action needed to avoid breakage)

| Dependent | Reference |
|---|---|
| `case-management/ontology/relationships.yaml:40-45` | `case_plan_references_need_assertion` → `needs_assessment:need_assertion` |
| `case-management/README.md:26` | names `case_plan_references_need_assertion` |
| `knowledge_layer_inventory.md:962` | lists `case_plan_references_need_assertion` under case-management's owned relationships |
| `impact/ontology/relationships.yaml:39` | `measurement_baseline_derived_from` → `needs_assessment:assessment_session` |
| `support-delivery/ontology/relationships.yaml:97` | `observation_escalates_to_assessment` → `needs_assessment:assessment_session` |
| `verification-operations/taxonomy/verification-findings.yaml:165-170` | cross-reference `scheme: needs_assessment:need_assertion`, `relation: supplies_values_for` |

These four live domains already treat the canonical folder as authoritative.
Retiring the legacy monolith will not break any of them.

### 6b. Still targeting legacy-only concepts (blocking retirement)

| Dependent | Legacy concept referenced | Why it's still open |
|---|---|---|
| `registration/taxonomy/needs.yaml:202-213` | `needs-assessment/taxonomy.yaml#need_severity` | Explicit placeholder, `references:` note, deferred to "Phase 5" per `Registration_Migration_Plan.md` decision **D5** — Registration owns a temporary local `need_severity` scheme pending this domain's migration. |
| `verification-operations/taxonomy/review-decisions.yaml:161-167` | prose: *"need_assertion (needs-assessment's **superseded_by** pattern)"* | Already uses the canonical entity name (`need_assertion`) but the canonical relationship is actually named `session_supersedes_assertion`, not `superseded_by` — `superseded_by` is the **legacy** relationship name. This is a naming leak from the old model into new prose and needs correcting once D6 (below) is ratified. |
| `ontology_authority_matrix.md:194-213` | Entire "Needs Assessment Domain" section: `assessment_depth`, `assessment_urgency`, `assessment_scope`, `assessment_status`, `assessment_methodology`, `finding_confidence`, `need_severity`, `Assessment`, `AssessmentFinding`, `IdentifiedNeed` | Governance table of record; references only legacy file paths. Zero canonical entries exist yet. |
| `knowledge_layer_inventory.md:795-826` | Full legacy taxonomy/ontology entries; canonical `ontology/*.yaml` and `taxonomy/*.yaml` files are **not inventoried at all** | Bigger gap than the authority matrix — the inventory doesn't acknowledge the canonical folder exists. |
| `knowledge_layer_inventory.md:401, 414` | `need_severity` reference inside the `registration/taxonomy/needs.yaml` entry | Mirrors 6b row 1; needs the same repoint. |
| `knowledge_layer_roadmap.md:214-215` | Marks legacy `taxonomy.yaml` / `ontology.yaml` "[Complete]" | Needs to reflect canonical folder status instead. |
| `needs-assessment/README.md` (whole file) | "Owns" section lists only legacy concepts; "Directory Structure" doesn't list `ontology/` or `taxonomy/` folders at all | Fully stale relative to current directory contents. |
| `README.md:158` (repo root) | prose: *"...verification findings into `IdentifiedNeed`s..."* | Terminology sync only — low risk. |

### 6c. Historical/planning documents (informational only, not live contracts)

These reference legacy `AssessmentFinding` / `IdentifiedNeed` / `need_severity`
but are discovery or decision-record artifacts, not files anything resolves
against at runtime. They do not block retirement, but will read as
referencing a deleted file once the monolith is gone:

- `case-management/discovery/Case_Management_Canonical_Implementation_Plan.md`
- `case-management/discovery/Case_Management_Domain_Model_Specification.md`
- `case-management/discovery/Case_Management_Migration_Plan.md`
- `case-management/discovery/Case_Management_Ontology_Readiness_Review.md`
- `docs/architecture/Registration_Content_Completion_Review.md`
- `docs/architecture/Registration_Domain_Audit.md`
- `docs/architecture/Registration_Migration_Plan.md`
- `docs/architecture/Community_Context_Migration_Plan.md:200`
- `shared/risk/governance.md:149` (a *negative* reference — states it does **not** duplicate `need_severity`; harmless but should eventually say `need_urgency`)

Note: case-management's *discovery* docs still say `AssessmentFinding`/
`IdentifiedNeed`, but its *live* ontology file (`case-management/ontology/relationships.yaml`)
already points at `need_assertion` — the discovery docs are simply frozen
snapshots from before that decision was finalized.

---

## 7. Concepts Present in Both, With No Divergence

For completeness, these carry over cleanly (same meaning, same shape, no
open question):

- `IdentifiedNeed` ↔ `need_assertion` (entity)
- `synthesizes_into` / `synthesized_from` relationship shape
- "must be synthesized from ≥1 finding" constraint
- "remains authoritative until superseded" constraint (canonical is a strict superset)

---

## 8. Open Decisions Requiring Content-Owner Sign-Off

| ID | Decision | Recommendation |
|---|---|---|
| **D1** | `assessment_depth` (rapid/detailed) has no canonical home. Author new, or declare deliberately dropped? | Author a new canonical data-property + taxonomy concept on `assessment_session`. This axis (rapid vs. detailed) is operationally load-bearing for Sphere-aligned triage and has no substitute in `assessment_modality` or `session_status`. |
| **D2** | `assessment_urgency` (routine/emergency — triage pressure on the assessment event) has no canonical home. | Author new — distinct from `need_urgency` (outcome severity). Add as a data-property on `assessment_session`, parallel to `assessment_modality`. |
| **D3** | `assessment_methodology` (structured/semi_structured/observational/participatory/clinical/mixed_method) has no canonical home. | Author new — `assessment_modality` covers channel, not methodological class; these are orthogonal axes. |
| **D4** | `based_on_claim` / `based_on_verified_fact` relationships have no canonical equivalent from the needs-assessment side. | Author two new relationships: `observation_based_on_claim` (→ `registration:registration_claim`) and `need_assertion_based_on_verified_fact` (→ `verification_operations:verification_finding`), formalizing what `verification-findings.yaml` currently only states in prose. |
| **D5** | `affects` (need_assertion → Subject direct edge) has no canonical equivalent; subject is only transitively reachable via session. | Confirm whether transitive reachability is sufficient, or whether a direct edge is needed for query/reporting. Non-blocking either way. |
| **D6** | `superseded_by` (Need↔Need) vs. canonical `session_supersedes_assertion` (Session→Need) is a structural divergence, not a rename. | Ratify canonical's session-driven model as the intended replacement (a new assessment session supersedes prior assertions, rather than needs superseding each other directly). This unblocks fixing the `review-decisions.yaml` prose in 6b. |
| **D7** | `need_severity` (4 values) → `need_urgency` (5 values) crosswalk is not 1:1 (`high→severe`, `medium→moderate`, `low→mild`, new `none` tier). | Ratify the crosswalk explicitly; this is what unblocks Registration's own deferred D5 decision in `Registration_Migration_Plan.md`. |
| **D8** | `finding_confidence` (4 values incl. `very_high`) → `confidence_level` (4 values incl. `highly_uncertain`) crosswalk; scope also widens from `AssessmentFinding`-only to `[observation, need_assertion]`. | Ratify crosswalk and the scope-widening as intentional. |
| **D9** | Legacy constraint "never creates new evidence records outside synthesized findings" is arguably inverted by canonical's `observation` entity (which *is* a domain-owned evidence record). | Confirm this architectural shift is intentional (it appears consistent with the AssessmentFinding→observation+need_assertion split in §2) rather than accidental scope creep. |

---

## 9. Migration Plan (phased, zero breakage)

**Phase 1 — Governance/documentation sync (no risk, can start immediately, no ontology changes):**
Update `ontology_authority_matrix.md`, `knowledge_layer_inventory.md`, and
`knowledge_layer_roadmap.md` to describe the canonical folder's actual
concept set alongside the legacy one, and add the canonical files that are
currently un-inventoried entirely (§6b). This is pure documentation
correction — it doesn't change any consumer's behavior.

**Phase 2 — Ratify D1–D9 with the content owner.**
Nothing downstream can be safely repointed until these are resolved, since
three of them (D1–D3) require authoring genuinely new canonical content, not
just renaming.

**Phase 3 — Author the missing canonical content per Phase 2 outcomes:**
new data-properties + taxonomy concepts for `assessment_depth`,
`assessment_urgency`, `assessment_methodology`; new relationships for
`based_on_claim` / `based_on_verified_fact`. This is the step that achieves
true 100% semantic coverage — until this lands, retiring the monolith would
silently drop three real concepts and two real relationships.

**Phase 4 — Repoint the two remaining legacy-only dependents:**
- `registration/taxonomy/needs.yaml`'s `need_severity` placeholder →
  canonical `need_urgency`, per the D7 crosswalk (closes Registration's own
  deferred D5).
- `verification-operations/taxonomy/review-decisions.yaml`'s prose
  `superseded_by` reference → `session_supersedes_assertion`, per D6.

**Phase 5 — Finalize governance docs and `needs-assessment/README.md`**
to canonical-only Owns/Does-Not-Own framing, mirroring the pattern already
applied to `beneficiary-lifecycle/README.md`, `case-management/README.md`,
`impact/README.md`, and `verification-operations/README.md` in this same
migration wave. Update `README.md:158` terminology (`IdentifiedNeed` →
`need_assertion`).

**Phase 6 — Verify zero remaining references,** via a repo-wide grep for
`AssessmentFinding|IdentifiedNeed|assessment_depth|assessment_urgency|assessment_scope|assessment_status|assessment_methodology|finding_confidence|need_severity`
outside historical/discovery documents (§6c, which are explicitly out of
scope and may retain the terminology as a frozen historical record, same
treatment already given to case-management's discovery docs).

**Phase 7 — Delete `needs-assessment/ontology.yaml` and
`needs-assessment/taxonomy.yaml`,** only after Phases 1–6 are complete and
Phase 6's verification grep is clean. This mirrors how
`verification-operations/verification-operations.yaml` was retired in the
prior migration wave (already reflected as a deletion in the current working
tree).

None of these seven phases have been executed in this pass — this document
is the plan only, per instruction.

---

## 10. Architectural Revision — Resolution of Validation Report Findings

This section resolves every blocker raised by
`Needs_Assessment_Canonical_Migration_Plan_VALIDATION_REPORT.md` (D10–D14,
plus classification of F7/F8/F10/F11). **This is an architectural decision
record, not an implementation.** No `ontology/`, `taxonomy/`, `reasoning/`,
or `README.md` file is touched by this section — every fix below is a
specification for Phase 3 (§9) to execute. It supersedes and extends §8's
Open Decisions table where the two overlap (D6, D9 are untouched; the
validation report's D10–D14 are new, higher-priority items that now sit
*before* D1–D9 in execution order, because several of D1–D9's own additions
would land on top of the entities/properties this section corrects).

### 10.1 — D10 (F1 / F2): Shared placeholder reconciliation

**Decision on `humanitarian_sector`:** Ownership stays with **Shared**,
exactly as `ontology_authority_matrix.md:48` already states — that row is
correct and is not being changed. What is wrong is that
`needs-assessment/ontology/data-properties.yaml`'s `thematic_sector` row
points at `programs_tax:thematic_sectors` instead of resolving the Shared
placeholder it was forward-declared for.

- **Rationale:** sector is a cross-cutting concept — Needs Assessment
  *produces* sector-tagged `need_assertion`s, Programs *consumes* them for
  eligibility/waitlist logic, and Case Management/Impact will eventually
  need to report by sector too. This is the textbook case
  `ARCHITECTURE.md`'s Shared Promotion Constraint exists for, and the
  concept already has a reserved home. Programs being a later-authored,
  currently-content-complete domain does not change who the architecturally
  correct owner is — it changes which domain currently holds the only
  authored copy of the values.
- **Fix specification (for Phase 3, not executed here):**
  1. `needs-assessment/ontology/data-properties.yaml`'s `thematic_sector`
     row: `taxonomy_ref: programs_tax:thematic_sectors` →
     `taxonomy_ref: shared:humanitarian_sector`.
  2. A new `shared/taxonomy/` scheme (`sectors.yaml`, scheme id
     `humanitarian_sector`) must be authored to back the now-resolved
     `shared:humanitarian_sector` entity, carrying the sector concept set
     (WASH, Shelter, Food Security, Livelihood, Health, Protection,
     Education, …) currently held in `programs/taxonomy/structure.yaml`'s
     `thematic_sectors` scheme.
  3. `programs/taxonomy/structure.yaml`'s `thematic_sectors` scheme is
     **not deleted outright** — under ADR-008 / `Canonical_Taxonomy_Schema.md`
     §9 ("a domain may reference a concept owned elsewhere; it must never
     redefine it"), Programs' own `taxonomy_ref` rows are repointed to
     `shared:humanitarian_sector`, and the local scheme is retired via a
     `references:` entry (`relation: extends` or a deprecation note) rather
     than silently dropped — this is a promotion, the same governance
     `ARCHITECTURE.md` already requires ("Concepts must only be promoted to
     `shared/` through an explicit architectural governance decision").
  4. **This promotion requires a short ADR** (proposed: *"Promote
     humanitarian_sector to Shared ownership, resolving the Needs Assessment
     forward-declaration"*) before Phase 3 executes it — this document
     recommends the ADR and records its content-intent above; it does not
     author `architecture-decisions/` itself, consistent with this being an
     architectural-revision-only pass.
  5. `ontology_authority_matrix.md:48`'s row does not need to change in
     substance — `humanitarian_sector`'s owner was always correctly recorded
     as Shared. What changes is that the placeholder finally gets resolved
     rather than bypassed.

**Decision on `assessment_tool`:** Ownership also stays with **Shared**, but
resolved by **specialization, not duplication.**

- **Rationale:** the legacy model treated "the tool used in an evaluation"
  as one opaque concept. The canonical model's decomposition into
  `assessment_instrument` (the formalized questionnaire/matrix) and
  `assessment_indicator` (the specific metric it measures) is a genuine,
  worthwhile refinement — finer-grained modeling is not the problem. The
  problem is that `assessment_instrument` was authored as a freestanding
  entity with no link back to the Shared placeholder it was meant to
  resolve, leaving two parallel, disconnected concepts for the same thing.
- **Fix specification (for Phase 3):**
  1. `needs-assessment/ontology/entities.yaml`'s `assessment_instrument` row
     gains `parent: shared:assessment_tool` (cross-domain form, per
     `Canonical_Ontology_Schema.md` §8 class hierarchy). `assessment_tool`
     becomes the abstract Shared supertype; `assessment_instrument` is Needs
     Assessment's concrete specialization of it. This is the same pattern
     already used for `person`/`household` under `shared:subject` — not a
     new mechanism.
  2. `assessment_indicator` has no Shared counterpart and needs none — it is
     a novel decomposition unique to this domain's finer-grained modeling
     and remains fully needs-assessment-owned.
  3. `ontology_authority_matrix.md:47`'s row is updated in a future pass to
     read "Placeholder for Needs Assessment — resolved via
     `needs_assessment:assessment_instrument` (`parent`)" instead of the
     current bare "Must not be redefined," so the resolution is visible in
     the authority table instead of only in this plan.
  4. No ADR is required for this one — `parent` is an ordinary, already-
     ratified mechanism (`Canonical_Ontology_Schema.md` §8), not a
     concept-ownership transfer. It resolves the placeholder without
     changing who owns what.

**Net effect:** both F1 and F2 close without deleting any already-authored
canonical content (backward compatible) and without inventing a new
ownership rule — both resolutions apply mechanisms the schema and the
authority matrix already provide (`parent` linkage, Shared promotion
governance) that simply were not used the first time.

### 10.2 — D11: Domain identifier normalization

**Decision:** `domain: needs-assessment` → `domain: needs_assessment` in all
8 canonical files (`ontology/entities.yaml`, `ontology/relationships.yaml`,
`ontology/data-properties.yaml`, `ontology/lifecycle-constraints.yaml`,
`ontology/semantic-constraints.yaml`, `taxonomy/evidence.yaml`,
`taxonomy/finding.yaml`, `taxonomy/session.yaml`).

- **Rationale:** every other multi-word domain in the repository already
  uses snake_case, every existing external consumer (`case-management`,
  `impact`, `support-delivery`, `verification-operations`) already
  references this domain as `needs_assessment:`, and the schema requires the
  header token to be identical to the CURIE prefix. There is no competing
  option to weigh — this is a typo fix, not a design decision.
- **Scope note:** this is purely a header-value correction. No `id`,
  `label`, `description`, relationship, or constraint changes. It carries
  zero semantic risk and no CURIE this domain's *own* content has minted
  needs to change (`(domain, id)` pairs are unaffected — only the `domain`
  half of the pair corrects to match what it was always supposed to be).
- **Sequencing:** execute this first in Phase 3, before any other §10 fix,
  so every subsequent CURIE this plan specifies (§10.1's `shared:`
  references, §10.3's retargeted relationship) is authored against the
  correct token from the start rather than needing a second pass.

### 10.3 — D12: Invalid cross-domain entity reference (`shared_org:organisation`)

**Decision:** retarget `session_conducted_by_org` from the non-existent
`shared_org:organisation` to the already-existing, already-forward-declared
`shared:actor` entity, and rename the row to make its broadened scope
explicit.

- **Options considered:**
  - *Option A — mint a new `shared:organisation` entity.* Rejected for now:
    it solves only this one row and reintroduces exactly the "invent an
    entity under schedule pressure" pattern ADR-023 §19 warns against for a
    different case. Nothing in the repository today needs an
    organisation-only concept distinct from what `actor` already covers.
  - *Option B (chosen) — repoint to `shared:actor`.* `shared/ontology/entities.yaml`
    already defines `actor` as "a placeholder for an operational
    participant (e.g., **volunteer, partner organization, AI agent**)...
    Forward-declared for Case Management and other operational domains" —
    a closer, already-existing semantic fit, requiring no new entity.
- **Fix specification (for Phase 3):**
  1. `needs-assessment/ontology/relationships.yaml`: rename the row
     `session_conducted_by_org` → `session_conducted_by_actor`; change
     `relationship: conducted_by_org` → `conducted_by_actor`; change
     `to: shared_org:organisation` → `to: shared:actor`.
  2. `session_conducted_by_person` (`→ shared_human:person`) is **left
     unchanged** — it is not broken, and unifying it with `actor` is a
     larger structural question (whether `person` acting operationally
     should be dual-modeled as `person` + `actor`, or whether `actor` should
     subsume `person` for this purpose) that is out of scope for a blocker
     fix. Logged below as a Phase 2 open question, not resolved here.
  3. `ontology_authority_matrix.md:50`'s existing `actor` row already covers
     this consumption; no authority-matrix change is required for this fix
     specifically (unlike §10.1, this is pure reference-not-redefine — no
     placeholder resolution bookkeeping needed).
- **Bonus effect on F10:** see §10.6 — this same fix substantially resolves
  the "algorithmic/AI assessor" gap, because `actor` already names "AI
  agent" as an in-scope concept once this relationship targets it.
- **Open question logged for Phase 2 (not blocking):** should
  `session_conducted_by_person` eventually be folded into
  `session_conducted_by_actor` for a single unified "who/what performed
  this session" edge, with `person` vs. `organisation` vs. `algorithmic
  system` distinguished by an `actor_type` taxonomy rather than by which
  relationship row is populated? Recorded, not decided — doing so now would
  touch a currently-working relationship for a stylistic unification, which
  is explicitly out of scope for a blocker-resolution pass.

### 10.4 — D13: Lifecycle architecture completion

Every lifecycle-governed entity gets a backing status property, a taxonomy
scheme for that property, and (where the legacy-derived pattern already
established a reason-requires-reason precedent) a semantic constraint. This
mirrors the shape `assessment_session`/`session_status` and
`need_assertion`/`finding_status` already correctly use — no new pattern is
invented, the existing one is simply applied to the three entities that were
missing it.

| Entity | New data property | New taxonomy scheme (proposed concepts) | New semantic constraint |
|---|---|---|---|
| `supervisor_review` | `review_status` (`taxonomy_ref`, `{min:1,max:1}`) | `review_status`: `pending`, `in_progress`, `approved`, `rejected` (identical to the entity's existing lifecycle states — no new states invented, just given a home) | — |
| `supervisor_review` | `rejection_reason` (`taxonomy_ref`, `{min:0,max:1}`) | `rejection_reason`: `insufficient_evidence`, `methodology_concern`, `inconsistent_with_prior_findings`, `requires_reassessment`, `other` | `rejected_review_requires_reason` — `required_if`, `property: rejection_reason`, `entities: [supervisor_review]`, `parameters: { condition: "review_status == rejected" }` — directly mirrors the already-existing `invalidated_finding_requires_reason` pattern on `need_assertion`. |
| `assessor_calibration` | `calibration_status` (`taxonomy_ref`, `{min:1,max:1}`) | `calibration_status`: `initiated`, `in_progress`, `resolved` (this entity currently has **no lifecycle entry at all** in `lifecycle-constraints.yaml` in addition to no data property — both must be authored together in Phase 3; proposed lifecycle: `initiated → in_progress → resolved`, mirroring `finding_consensus`'s shape since both are governance/analysis processes) | — |
| `assessor_calibration` | `calibration_outcome` (`taxonomy_ref`, `{min:0,max:1}`) | `calibration_outcome`: `bias_confirmed_corrective_action_issued`, `bias_confirmed_monitoring_only`, `no_bias_detected`, `inconclusive` | `resolved_calibration_requires_outcome` — `required_if`, `property: calibration_outcome`, `entities: [assessor_calibration]`, `parameters: { condition: "calibration_status == resolved" }` |
| `finding_consensus` | `consensus_status` (`taxonomy_ref`, `{min:1,max:1}`) | `consensus_status`: `initiated`, `under_review`, `resolved` (matches existing lifecycle states) | — |
| `finding_consensus` | `consensus_outcome` (`taxonomy_ref`, `{min:0,max:1}`) | `consensus_outcome`: `finding_upheld`, `finding_revised`, `finding_escalated`, `finding_invalidated` — closes the asymmetry with `verification-operations/taxonomy/review-decisions.yaml`'s richer decision vocabulary, which the validation report noted `finding_consensus` lacked despite that file explicitly citing this domain's `superseded_by` pattern as precedent | `resolved_consensus_requires_outcome` — `required_if`, `property: consensus_outcome`, `entities: [finding_consensus]`, `parameters: { condition: "consensus_status == resolved" }` |
| `reassessment_trigger` | `trigger_status` (`taxonomy_ref`, `{min:1,max:1}`) | `trigger_status`: `active`, `triggered`, `resolved`, `cancelled` (matches existing lifecycle states) | — |
| `reassessment_trigger` | `trigger_type` (`taxonomy_ref`, `{min:1,max:1}`) | `trigger_type`: `scheduled`, `incident_based`, `disaster_event`, `case_manager_request`, `data_quality_concern`, `other` — this scheme did not exist in any form previously; it directly answers the entity's own description ("An incident, schedule, or rule that mandates a new assessment session") | — |

- **Design discipline applied:** every new property/scheme is the minimum
  needed to make an already-declared lifecycle queryable and, where the
  domain already established a reason-on-terminal-negative-state pattern
  (`invalidation_reason`), extends that same pattern rather than inventing
  a new one. No entity gains more structure than its existing lifecycle
  already implied.
- **`assessor_calibration` is the one true net-new addition** (it had
  neither a lifecycle nor a data property before); the other three entities
  already had a lifecycle and are only gaining the property/scheme/
  constraint needed to back it.

### 10.5 — D14: Assessment scope — decision and rationale

**Decision: partial mutual exclusivity, not full exclusivity and not
unconstrained multi-scope.** Neither of the two extremes the validation
report weighed is correct on its own:

- **Full legacy-style mutual exclusivity** (exactly one of
  individual/household/community per session) is *too strict*. In routine
  humanitarian practice, a single household visit routinely produces both
  household-level findings (shelter, WASH) and individual-level findings
  nested inside it (a child protection screening, a specific member's
  medical need) in one episodic event. Forcing that into two separate
  `assessment_session` records would fragment a single field visit into
  artificial duplicates with no operational benefit.
- **Fully unconstrained multi-scope** (the canonical model's current,
  silent default) is *too loose*. A community-level rapid assessment (e.g.
  surveying a whole settlement) is a different unit of analysis, typically
  a different methodology, and often a different assessor team than an
  individual/household visit — combining `evaluates_community` with
  `evaluates_person`/`evaluates_household` in the same session conflates
  two operationally distinct assessment activities that should not share
  one record.

- **Rule:** `evaluates_person` and `evaluates_household` **may** co-occur on
  the same `assessment_session`. `evaluates_community` is **mutually
  exclusive** with both `evaluates_person` and `evaluates_household` — a
  session that evaluates a community may not simultaneously evaluate a
  named individual or household within the same record.
- **Fix specification (for Phase 3):** add to
  `needs-assessment/ontology/semantic-constraints.yaml`:
  ```
  - id: community_scope_excludes_individual_household
    type: mutually_exclusive
    property: evaluates_community
    entities: [assessment_session]
    parameters: { mutually_exclusive_with: [evaluates_person, evaluates_household] }
  ```
  (Exact `parameters` shape to be finalized against
  `Canonical_Ontology_Schema.md` §9's `mutually_exclusive` type when Phase 3
  authors it — the constraint *kind* and the entities/properties it binds
  are decided here; the literal parameter key names are an implementation
  detail deferred to that phase.) `session_must_evaluate_at_least_one_subject`
  is retained unchanged — the two constraints compose without conflict:
  "at least one of the three" plus "community excludes the other two."
- **This supersedes** the §3 mapping table's characterization of the legacy
  `assessment_scope` → canonical relationship conversion as a clean
  "MATCHED (structural change)." It was not clean; this section is the
  correction, and it deliberately does not simply restore the legacy rule
  verbatim — it improves on it using an operational distinction the legacy
  single enum could not express (individual+household nesting) while still
  closing the real gap the validation report found (unbounded multi-scope).

### 10.6 — Classification of F7, F8, F10, F11

| Finding | Classification | Rationale |
|---|---|---|
| **F7** — no `assessment_instrument`↔`assessment_indicator` composition relationship | **Required before implementation.** | An "instrument" whose contents cannot be structurally enumerated is barely modeled at all — this isn't a nice-to-have, it's the core meaning of the entity. Cheap to add (one relationship row, e.g. `instrument_contains_indicator`, `from: assessment_instrument`, `to: assessment_indicator`, `{min:1,max:unbounded}`, inverse `indicator_belongs_to_instrument`), no design ambiguity, no cross-domain dependency. Fix alongside §10.1's `assessment_instrument`/`shared:assessment_tool` `parent` linkage in the same Phase 3 pass. |
| **F8** — `supervisor_review`/`assessor_calibration`/`finding_consensus` have no "performed by" edge | **Safe for Phase 2.** | Real accountability gap (humanitarian audit-trail practice generally expects reviewer/calibrator identity to be recorded, and `verification-operations/taxonomy/review-decisions.yaml` treats reviewer independence as a live open question for the same reason), but the domain is structurally coherent without it — `assessment_session` already carries the primary actor-attribution need. Add `review_conducted_by_person`, `calibration_conducted_by_person`, `consensus_reached_by_person`/`_org` (mirroring §10.3's now-corrected `session_conducted_by_actor` pattern) early in Phase 2, not bundled into the blocker-resolution pass. |
| **F10** — no representation for algorithmic/AI assessors | **Safe for Phase 2 (substantially resolved by §10.3).** | Retargeting `session_conducted_by_org` to `shared:actor` (§10.3) already gives the ontology structural capacity to represent an algorithmic assessor, since `actor`'s own description names "AI agent" in scope. What remains is taxonomy *content* — an `actor_type` scheme distinguishing `person`/`organization`/`algorithmic_system` — which is vocabulary authoring, not architecture, and is correctly sequenced into Phase 2 alongside whatever domain ends up owning the `actor_type` scheme (likely Shared, by the same promotion logic as §10.1). |
| **F11** — namespace/IRI values hardcoded ahead of C-2, inconsistent across domains | **Future enhancement (repository-wide, not needs-assessment-specific).** | This is explicitly unresolved repository-wide business (`Canonical_Ontology_Schema.md`'s own status banner: Registration and Community Context, the two reference implementations, both have Phase 5 CURIE linking "blocked on a repository-wide manifest and ratified base IRI"). Needs Assessment cannot unilaterally fix this without guessing at C-2 a second time — the correct action is to mark its `namespaces:` block values as provisional in a header comment when Phase 3 executes, and revisit once C-2 ratifies for the whole repository. Not a needs-assessment blocker. |

### 10.7 — Revised execution order (supersedes §9 ordering for Phase 3)

Phase 3 (§9) now executes in this order, since §10's fixes create or rename
concepts that §9's D1–D9 additions (from §8) would otherwise land on top of:

1. §10.2 (D11 — domain token) — mechanical, zero dependency, do first.
2. §10.1 (D10 — Shared placeholder reconciliation for `humanitarian_sector`
   and `assessment_tool`), §10.3 (D12 — `shared:actor` retarget), §10.4
   (D13 — lifecycle completion), §10.5 (D14 — scope constraint), and F7 (now
   required) — these five can proceed together; none depends on another.
3. Original §8 D1–D9 (assessment_depth/urgency/methodology authoring, the
   `based_on_claim`/`based_on_verified_fact` relationships, etc.) — proceeds
   only after step 2, so it is authored against the corrected domain token,
   the resolved placeholders, and the completed lifecycle shape rather than
   against the pre-revision state.
4. F8 and F10's taxonomy-content follow-ups (§10.6) — Phase 2, after
   Phase 3 lands.
5. F11 — deferred indefinitely, pending repository-wide C-2 ratification.

Phases 4–7 of §9 (repointing `registration/taxonomy/needs.yaml` and
`verification-operations/taxonomy/review-decisions.yaml`, governance-doc
sync, README rewrite, final verification, monolith deletion) are unchanged
by this section and still execute in their original relative order, after
the above.

---

## 11. Final Architectural Readiness Assessment

**The revised architecture specified in §10 is sound and ready to guide
implementation. The canonical YAML files currently committed to the
repository are not yet conformant with it.**

Every blocker the validation report raised (D10–D14 / F1, F2, F3→D11,
F4→D12, F5/F6→D13, F9→D14) now has a specific, backward-compatible
resolution recorded above: no already-authored canonical entity, property,
or relationship is deleted; every fix either corrects a header value,
completes a lifecycle the domain had already committed to, adds a linkage
the domain's own entity descriptions already implied, or resolves a
placeholder using a mechanism (`parent`, Shared promotion governance) the
frozen contracts already provide. Humanitarian semantics are preserved and,
in two places (§10.1's instrument/indicator specialization, §10.5's
individual+household co-occurrence), improved on what the legacy monolith
could express — not merely carried forward.

**What remains before Needs Assessment can be marked ready in
`ARCHITECTURE.md`'s Domain Inventory:**

1. Phase 3 (§10.7) must actually be executed against the `ontology/` and
   `taxonomy/` files — this document is the specification, not the
   implementation.
2. The `humanitarian_sector` Shared-promotion ADR recommended in §10.1 must
   be drafted and ratified before that specific fix lands (all other §10
   fixes have no ADR dependency and can proceed immediately in Phase 3).
3. §9's original D1–D9 (the three missing taxonomy schemes, the two missing
   relationships, and the remaining value-crosswalk decisions) still require
   content-owner sign-off, unchanged by this revision, and still execute
   after §10 per the revised ordering in §10.7.
4. Phases 4–7 (downstream repoint, governance-doc sync, README rewrite,
   monolith deletion) remain gated on all of the above, exactly as §9
   already specified.

**Verdict: architecturally ready for implementation planning; not yet ready
for the "Complete"/canonical-implementation status `ARCHITECTURE.md`
currently records for this domain.** That status should be treated as
provisional until Phase 3 (§10.7) executes and a follow-up validation pass
confirms F1–F6 and F9 are closed in the actual files, not only in this
plan.
