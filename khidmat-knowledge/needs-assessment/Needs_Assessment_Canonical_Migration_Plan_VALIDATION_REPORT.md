# Needs Assessment Canonical Migration Plan — Independent Validation Report

## Verdict

**FAILS review. Needs Assessment is NOT ready for canonical implementation.**

The prior migration plan (`Needs_Assessment_Canonical_Migration_Plan.md`) correctly mapped legacy↔canonical
concepts, but it audited the migration plan's *own consistency* — it never checked the canonical
files that already exist against the frozen schemas, the two governing ADRs, or the repository's
other domains. This review does that, and finds structural defects the prior pass did not catch,
including two direct violations of an explicit, binding rule already written down in
`ontology_authority_matrix.md`. No files are modified in this pass.

Reviewed against: `Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`, ADR-008, ADR-022,
ADR-023, `ARCHITECTURE.md` (Dependency Rules / Domain Inventory), `ontology_authority_matrix.md`,
and the live ontology files of Registration, Case Management, Impact, Verification Operations,
Beneficiary Lifecycle, Support Delivery, and Shared.

---

## Findings

### F1 — [CRITICAL] `thematic_sector` bypasses an explicitly reserved Shared placeholder, creating an ownership inversion

`ontology_authority_matrix.md:48` states, as a binding rule:

> `humanitarian_sector` | HumanitarianSector | `shared/ontology/entities.yaml` | Shared Ontology |
> **Placeholder for Needs Assessment. Must not be redefined.**

`shared/ontology/entities.yaml:31-35` confirms the entity already exists, forward-declared exactly
for this domain:

```yaml
  - id: humanitarian_sector
    label: HumanitarianSector
    description: >
      A placeholder for a universal humanitarian sector (e.g., WASH, Shelter).
      Forward-declared for Needs Assessment.
```

Instead, `needs-assessment/ontology/data-properties.yaml:73-76` sources `thematic_sector`'s
controlled vocabulary from a different domain entirely:

```yaml
  - id: thematic_sector
    domain: need_assertion
    taxonomy_ref: programs_tax:thematic_sectors
```

`programs_tax:thematic_sectors` is `programs/taxonomy/structure.yaml`'s scheme — owned by
**Programs**, a domain that:
- Has no forward-declared claim on this concept anywhere in `ontology_authority_matrix.md`.
- Is, by Needs Assessment's own `README.md` and `Needs_Assessment_Domain_Audit.md` §4, a
  **consumer** of Needs Assessment output ("Programs consumes Need Assertions and Vulnerability
  Scores to drive waitlist prioritization").

This inverts the intended dependency direction: the domain that *produces* sector-tagged data
(Needs Assessment) now depends on the vocabulary owned by the domain that *consumes* it (Programs),
in direct contradiction of `ARCHITECTURE.md`'s Dependency Rules ("Acyclic Dependencies... Shared
Promotion Constraint") and ADR-008 (single ownership already assigned this concept to Shared). It
also silently orphans the Shared placeholder — `humanitarian_sector` now sits unused, reserved for
a consumer that never materializes.

**This is not a stylistic issue — it is a documented governance rule being violated by a file
already checked into the canonical folder.**

**Fix:** `thematic_sector`'s `taxonomy_ref` must resolve against `shared:humanitarian_sector` (the
Shared placeholder must be populated with the WASH/Shelter/Health/etc. concept set and the
`programs_tax` reference removed). If Programs is judged the correct long-term owner after all,
that requires an explicit ADR reassigning the concept and updating
`ontology_authority_matrix.md` — not a silent divergence baked into a `data-properties.yaml` row.

---

### F2 — [CRITICAL] `assessment_instrument` duplicates the reserved `assessment_tool` placeholder instead of resolving it

The same authority-matrix row group (`ontology_authority_matrix.md:47`) reserves a second concept
for this domain:

> `assessment_tool` | AssessmentTool | `shared/ontology/entities.yaml` | Shared Ontology |
> **Placeholder for Needs Assessment. Must not be redefined.**

`needs-assessment/ontology/entities.yaml:7-11` instead mints an unrelated, freestanding entity:

```yaml
  - id: assessment_instrument
    label: Assessment Instrument
    description: >
      The formalized tool, questionnaire, or matrix defining the structure of the evaluation.
```

There is no `parent: assessment_tool` (cross-domain form: `shared:assessment_tool`), no
relationship resolving the Shared placeholder, and no annotation anywhere recording that the
placeholder was deliberately superseded. The repository now has two parallel concepts for "the
tool used to conduct an evaluation" — one dead (Shared's forward-declaration, never consumed,
never retired) and one live (`needs-assessment`'s own). This is precisely the duplicate-concept
failure mode ADR-008 exists to prevent, reproduced inside a file already presented as canonical.

**Fix:** either (a) `assessment_instrument` formally inherits from `shared:assessment_tool` via
`parent`, or (b) the Shared placeholder row is explicitly retired through a recorded governance
decision and `ontology_authority_matrix.md` updated to reassign ownership — but the decision must
be made and logged, not defaulted into silently.

---

### F3 — [HIGH] Domain identifier `needs-assessment` (hyphenated) does not match the CURIE prefix every consumer already uses

Every canonical `needs-assessment/ontology/*.yaml` and `taxonomy/*.yaml` file declares:

```yaml
domain: needs-assessment
```

Cross-checked against every other multi-word domain's own header:

| Domain | `domain:` header value |
|---|---|
| `beneficiary-lifecycle` | `beneficiary_lifecycle` |
| `case-management` | `case_management` |
| `community-context` | `community_context` |
| `support-delivery` | `support_delivery` |
| `verification-operations` | `verification_operations` |
| `volunteer-operations` | `volunteer_operations` |
| **`needs-assessment`** | **`needs-assessment`** ← the only hyphenated value in the repository |

Meanwhile every live cross-domain reference already uses the underscore form:
`case-management/ontology/relationships.yaml:43` (`needs_assessment:need_assertion`),
`impact/ontology/relationships.yaml:39` (`needs_assessment:assessment_session`),
`support-delivery/ontology/relationships.yaml:97` (same),
`verification-operations/taxonomy/verification-findings.yaml:165` (same).

Per `Canonical_Taxonomy_Schema.md` §4/§10 (the same header rule governs both ontology and taxonomy
files), `domain:` must be "the same snake_case token the domain's ontology module uses... because
both feed the same CURIE prefix." This is the exact T-2-class defect the taxonomy schema audit
already found and fixed for Verification Operations' old `"Verification Operations"` header —
reproduced here, unnoticed, across all 8 needs-assessment canonical files.

**Fix:** `domain: needs-assessment` → `domain: needs_assessment` in all 8 files, before any Phase 5
CURIE-linking work begins.

---

### F4 — [HIGH] `session_conducted_by_org` targets an entity that does not exist anywhere in the repository

`needs-assessment/ontology/relationships.yaml:43-47`:

```yaml
  - id: session_conducted_by_org
    from: assessment_session
    relationship: conducted_by_org
    to: shared_org:organisation
    cardinality: { min: 0, max: unbounded }
```

`shared/ontology/entities.yaml` (read in full) defines exactly seven entities: `subject`, `person`,
`household`, `assessment_tool`, `humanitarian_sector`, `intervention_type`, `actor`. There is no
`organisation` entity. There is no `shared/organisations/ontology/` sub-module — the only file
matching that name is `shared/taxonomy/organisations.yaml`, a **taxonomy** vocabulary of
organisation *types*, not an ontology entity. A repository-wide search for `id: organisation` in
any `entities.yaml` returns nothing.

This relationship row's `to:` target is a dangling reference to a canonical entity that has never
been authored. Notably, `shared/ontology/entities.yaml` already forward-declares `actor` —
"A placeholder for an operational participant (e.g., **volunteer, partner organization**, AI
agent)... Forward-declared for Case Management and other operational domains" — which is a much
closer semantic fit than the invented `shared_org:organisation`.

**Fix:** either mint `organisation` as a real Shared entity before this row can be considered
valid, or repoint `session_conducted_by_org` at `shared:actor`, consistent with the placeholder
that already exists for exactly this purpose.

---

### F5 — [HIGH] Three of five lifecycle-governed entities have no data property to hold the state they transition through

`ontology/lifecycle-constraints.yaml` defines full multi-state lifecycles for `supervisor_review`
(pending → in_progress → approved/rejected), `finding_consensus` (initiated → under_review →
resolved), and `reassessment_trigger` (active → triggered → resolved/cancelled).

`ontology/data-properties.yaml` contains **zero** rows for `supervisor_review` and
`assessor_calibration`, and exactly one row for `finding_consensus` (`consensus_date`, a scalar
timestamp — not a status field). There is no `review_status`, no `consensus_status`, no
`trigger_status` property anywhere in the file.

Compare to the two entities that *are* correctly modeled: `assessment_session` has `session_status`
(`taxonomy_ref: session_status`) and `need_assertion` has `finding_status`
(`taxonomy_ref: finding_status`) — both backing their lifecycle with a real, queryable field.

A lifecycle description with no backing property is not implementable: nothing in the ontology
records "which state is this `supervisor_review` currently in." Per
`Canonical_Ontology_Schema.md` §9, `lifecycle-constraints.yaml` is descriptive of an entity's
semantics — it presumes the state it describes is actually stored somewhere.

**Fix:** add `review_status`, `consensus_status`, and `trigger_status` (or equivalent)
`taxonomy_ref` data-property rows for these three entities before their lifecycles can be
considered real rather than aspirational documentation.

---

### F6 — [MEDIUM] Missing taxonomy schemes and missing semantic constraints, following directly from F5

- No taxonomy scheme exists anywhere (`taxonomy/session.yaml`, `finding.yaml`, `evidence.yaml`) for
  review outcomes, consensus states, or reassessment-trigger states — the three status fields F5
  requires have no controlled vocabulary to draw from even once authored.
- `supervisor_review`'s `rejected` state has no reason vocabulary. Contrast `need_assertion`, where
  `invalidation_reason` is mandatory whenever `finding_status == invalidated`
  (`semantic-constraints.yaml`, `invalidated_finding_requires_reason`). No equivalent
  `rejection_reason` scheme or `required_if` constraint exists for a rejected review — a supervisor
  can reject a session/finding with no structural way to record why.
- `reassessment_trigger` has no `trigger_type`/`trigger_reason` scheme at all, despite its own
  description implying exactly this classification: "An incident, **schedule**, or **rule** that
  mandates a new assessment session." Schedule-driven, incident-driven, disaster-driven, and
  manual/case-manager-requested triggers are operationally distinct and currently indistinguishable.

---

### F7 — [MEDIUM] Missing relationship: `assessment_instrument` has no structural link to the `assessment_indicator`s it contains

`entities.yaml`'s own description of `assessment_indicator` states it is "the specific question,
metric, or indicator **measured by an assessment instrument**" — implying a composition
relationship. No such relationship exists in `relationships.yaml`. The only edge involving
`assessment_indicator` is `observation_evaluates_indicator` (an *instance-level* edge, i.e. one
specific observation to one specific indicator). There is no structural way to ask "what
indicators does instrument X contain" independent of already-collected observation data — the
entity's own stated purpose and the relationship graph disagree with each other, independent of
any comparison to the legacy model.

---

### F8 — [MEDIUM] Inconsistent actor modeling: `assessment_session` records who conducted it; the three governance entities do not

`assessment_session` correctly has `session_conducted_by_person` / `session_conducted_by_org`.
`supervisor_review`, `assessor_calibration`, and `finding_consensus` — all explicitly
human-governance/QA processes per their own descriptions — have no equivalent edge to the
person(s) who performed the review, the calibration, or reached consensus. This is an internal
inconsistency within the same file: one episodic entity in this domain models its actor; three
others of the identical kind (a governance event performed by a person) do not.

---

### F9 — [MEDIUM] Silent loss of a legacy invariant: `assessment_scope` mutual exclusivity is gone, and the prior migration plan mischaracterized this as a clean structural match

Legacy `assessment_scope` was a **single-valued** taxonomy (`cardinality: "1"`): a session had
exactly one scope — individual, household, or community. Canonical converts this into three
independent, optional relationships:

```yaml
session_evaluates_person:    { min: 0, max: 1 }
session_evaluates_household: { min: 0, max: 1 }
session_evaluates_community: { min: 0, max: 1 }
```

governed by exactly one constraint, `session_must_evaluate_at_least_one_subject` — a `required_if`
enforcing "not all three empty." Nothing enforces "at most one" or "exactly one."
`Canonical_Ontology_Schema.md` §9 explicitly lists `mutually_exclusive` as an available constraint
`type` — it is simply never used here. As written, a single `assessment_session` can legally
evaluate a person, a household, and a community simultaneously, which the legacy model's
single-valued enum structurally forbade.

The prior migration plan's §3 mapping table logged this transition as "MATCHED (structural
change)" with no flag — that characterization understated a genuine, silent loss of an invariant.

**Fix:** add a `mutually_exclusive` constraint across the three `evaluates_*` relationships, or
explicitly ratify multi-scope sessions as a deliberate capability extension beyond the legacy
model (not a default nobody decided).

---

### F10 — [MEDIUM] Missing humanitarian business concept, already self-identified by the domain and dropped anyway

`needs-assessment/Needs_Assessment_Repository_Gap_Report.md` §2 flags "Algorithmic/AI Assessors"
(Proxy Means Testing, ML-driven vulnerability scoring, increasingly standard in humanitarian
targeting) as a missing core construct. The canonical model does not address it:
`session_conducted_by_person` / `session_conducted_by_org` only accept `shared_human:person` /
`shared_org:organisation` (itself non-existent, per F4) as targets — there is no way to record that
a session, or a `need_assertion`'s synthesis, was produced by an algorithm rather than a human
actor. A gap the domain's own discovery work identified was carried into the canonical structure
unresolved, and the prior migration plan does not mention it at all.

---

### F11 — [LOW] Namespace/IRI values are hardcoded ahead of the reference implementations, and disagree with themselves across domains

`Canonical_Ontology_Schema.md`'s status banner states the literal base IRI (Finding C-2) remains
unratified, and that even Registration and Community Context — the two designated reference
implementations — have Phase 5 CURIE linking explicitly "blocked on a repository-wide manifest and
ratified base IRI." Despite this, `needs-assessment/ontology/relationships.yaml` and
`data-properties.yaml` already hardcode a specific IRI scheme in their `namespaces:` blocks, ahead
of the domains meant to prove the pattern first — and that scheme disagrees with what other
"Complete" domains already did:

| File | Namespace value style |
|---|---|
| `case-management/ontology/relationships.yaml` | bare placeholder (`needs_assessment: needs_assessment`) |
| `impact/ontology/relationships.yaml` | `https://khidmat.org/ontology/...` |
| `needs-assessment/ontology/relationships.yaml` | `http://khidmat.org/ontology/...` (no S) |

`needs-assessment`'s own aliasing is additionally inconsistent with itself: it names the
community-context prefix `community_ctx`, but community-context's actual `domain:` token
(confirmed directly against `community-context/ontology/entities.yaml`) is `community_context` —
an invented abbreviation with no manifest backing it, in a repository whose entire C-2/manifest
mechanism exists specifically to prevent exactly this kind of divergent, independently-guessed
prefix.

This is not fatal on its own (C-2 is repository-wide unfinished business, not a needs-assessment-
specific defect), but it means needs-assessment's `namespaces:` blocks will need rework regardless
of what this review concludes, once C-2 actually ratifies.

---

## Confirmed non-issues (checked, passed)

- **ADR-022 (regional localization).** All three canonical taxonomy files
  (`evidence.yaml`, `finding.yaml`, `session.yaml`) use globally neutral terminology throughout. No
  country-specific concept, alias, or ownership found.
- **ADR-023 Entity vs. Value Object vs. Role classification.** `observation` correctly fails the
  Value Object promotion test (§17 rule 1 — `finding_consensus` needs to reference specific
  `observation` instances via `consensus_reviews_observation`) and is correctly kept as an Entity.
  No role (assessor, supervisor, calibrator) was incorrectly minted as its own Entity — every one
  is referenced via a relationship row to `shared_human:person`, consistent with §18. No
  reasoning-output concept (score, flag, gap) was found absorbed into the ontology, consistent with
  §19.
- **`IdentifiedNeed` ↔ `need_assertion`.** Direct, clean match — no divergence found beyond what
  the prior migration plan already logged.
- **`semantic-constraints.yaml` structural shape.** Every constraint row correctly uses `id` /
  `type` / `property` / `entities` / `parameters`, and every `property` value correctly resolves to
  either a relationship's `relationship` field or a `data-properties.yaml` id, per §9's rule (never
  a per-row relationship `id`).

---

## What This Means for the Prior Migration Plan

`Needs_Assessment_Canonical_Migration_Plan.md`'s decisions D1–D9 remain necessary but are no longer
sufficient. Before any of D1–D9 are actioned, or the legacy monolith is retired, the following must
happen first — these are new, higher-priority blockers this review adds:

- **D10 (new, blocks everything):** Resolve F1 and F2 — reconcile `thematic_sector` and
  `assessment_instrument` against the Shared placeholders already reserved for this domain in
  `ontology_authority_matrix.md`. This is a correctness fix, not a judgment call — the current
  state contradicts a written governance rule.
- **D11 (new):** Fix F3 (`domain:` token) in all 8 canonical files. Mechanical, zero design risk,
  should happen immediately regardless of any other decision.
- **D12 (new):** Resolve F4 — either mint `shared:organisation` or repoint at `shared:actor`.
- **D13 (new):** Resolve F5/F6 — author the missing status properties and taxonomy schemes for
  `supervisor_review`, `assessor_calibration`, `finding_consensus`, `reassessment_trigger`, or the
  lifecycle-constraints entries for those four entities are descriptive fiction with nothing behind
  them.
- **D14 (new):** Decide F9 — ratify `mutually_exclusive` scope, or explicitly accept multi-scope
  sessions as intentional.
- Everything else in this report (F7, F8, F10, F11) should be logged as open items but does not
  block a first correct implementation pass the way F1–F6/F9 do.

## Required Structural Fixes Before Implementation (summary)

1. Repoint `thematic_sector` → `shared:humanitarian_sector`; populate the Shared placeholder.
2. Link `assessment_instrument` to `shared:assessment_tool` via `parent`, or formally retire the
   Shared placeholder through a recorded decision.
3. `domain: needs-assessment` → `domain: needs_assessment` across all 8 canonical files.
4. Fix or repoint the `session_conducted_by_org` → `shared_org:organisation` dangling reference.
5. Add `review_status`, `consensus_status`, `trigger_status` data properties and their taxonomy
   schemes; add a rejection-reason scheme + constraint for `supervisor_review`; add a
   `trigger_type`/`trigger_reason` scheme for `reassessment_trigger`.
6. Add an `instrument_contains_indicator`-style relationship.
7. Add actor-attribution relationships for `supervisor_review`, `assessor_calibration`,
   `finding_consensus`, matching the pattern already used on `assessment_session`.
8. Add a `mutually_exclusive` constraint on session scope, or explicitly document multi-scope as
   intended.
9. Represent (or explicitly defer, with a tracked note) algorithmic/AI assessors.
10. Treat the `namespaces:` IRI values as provisional pending repository-wide C-2 ratification —
    do not treat them as final.

Until items 1–5 and 8 are resolved, Needs Assessment should not be marked "ready for canonical
implementation" in `ARCHITECTURE.md`'s Domain Inventory, despite its current "Complete" status
there.
