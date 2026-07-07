# Registration Domain — Architectural Conformance Audit

> **Status:** AUDIT ONLY — no file has been modified. This report checks the
> `registration/` domain for **structural conformance** against the two frozen
> contracts. It does **not** redesign registration, the ontology, or the taxonomy.
> It does not propose meaning changes except where flagged explicitly as a
> *semantic* finding, which is reported separately from mechanical conformance.
>
> **Authorities:**
> - `docs/architecture/Canonical_Ontology_Schema.md` (the ontology contract)
> - `docs/architecture/Canonical_Taxonomy_Schema.md` (the taxonomy contract)
>
> **Reference implementation target:** `shared/ontology/*` and `shared/taxonomy/*`
> (already canonicalized and frozen) show the exact header, list, and `schemes:`
> shapes registration must reach.
>
> **Scope audited:** `registration/{ontology,taxonomy,reasoning,readiness,questioning,verification,gaps}`
> — 22 files.

---

## Executive Summary

Registration is the **most content-rich but least structurally conformant** domain
in the repository. Every one of its two governed modules (`ontology/`, `taxonomy/`)
diverges from the frozen contracts on multiple axes. None of the divergences are
architectural blockers against the contracts themselves — they are the *legacy
patterns the contracts were written to retire*, present here in their fullest form.

The headline structural facts:

1. **The `ontology/` module is missing 3 of its 5 canonical files** and contains
   **1 file the contract explicitly deletes** (`attributes.yaml`). Registration
   models attributes with the exact `attributes_ref` + `attributes.yaml` pattern
   the ontology contract §2/§4 removes.
2. **`relationships.yaml` uses the retired cardinality enum** (`one_to_one`,
   `one_to_many`, `many_to_many`, …) that ontology §7 replaces with `{min, max}`,
   on every row, plus a `required:` field §6 forbids.
3. **All 9 taxonomy files use one of the non-conformant root shapes** the taxonomy
   contract §2 (findings T-1…T-9) enumerates by name — they are literally the
   evidence that audit cites. None uses the canonical `schemes:` → `concepts:` list.
4. **Duplicate sources of truth** exist between `entities.yaml` (`key_attributes`),
   `attributes.yaml` (the real detail), and the taxonomy files (inline `values:`
   lists that also carry a `values_ref:` pointer to the same vocabulary).
5. **One broken/dangling reference** (`verification_brief` used as a relationship
   target, though it is a projection, not an entity) and **pervasive file-path
   references** (`values_ref:`, `imports:`, `ref:`) that must become manifest-
   resolved CURIEs — a conversion **blocked repository-wide** until the manifest
   (Finding R-1) and literal IRI values (Finding C-2) are ratified.

The good news: the *content* of registration is coherent and mostly complete. This
is a **normalization** exercise, not a redesign. The overwhelming majority of the
work is **mechanical re-serialization** into the frozen shapes. A smaller,
clearly-bounded set of **semantic** questions (nested object attributes, category/
subtype confusion, cross-domain vocabulary ownership) must be decided deliberately
because they cannot be resolved by re-serialization alone. A third set are **future
enhancements** that neither block conformance nor generation.

**Verdict:** Registration is **not yet** a valid canonical reference implementation.
It is, however, a *clean migration candidate* — its non-conformance is uniform and
predictable, and the reference shape already exists in `shared/`. It cannot be
declared conformant until the manifest/C-2 dependency lands, because a large fraction
of its references are cross-domain and CURIE-bound.

**Finding counts:** Critical **9** · Required **11** · Optional **7**.
Classification split: Mechanical **19** · Semantic **6** · Future **2**.

---

## Reading key

Each finding carries two orthogonal tags:

- **Severity** — its section (Critical / Required / Optional).
- **Class** — one of:
  - **[MECHANICAL]** — a pure re-serialization into a frozen shape. No meaning
    changes. Deterministic, low-risk.
  - **[SEMANTIC]** — cannot be resolved by re-serialization; requires a modeling
    decision that could change or clarify meaning. Must be reviewed before action.
  - **[FUTURE]** — neither blocks conformance nor generation; deferred enhancement.

The three classes are **never mixed within a fix**. Section "Scope of Future
Implementation" consolidates each class into its own worklist.

---

## Critical Findings

*These prevent registration from becoming the canonical reference implementation
and/or prevent deterministic generation. They must be resolved first.*

### C-R1 — Ontology module is missing 3 of 5 canonical files · [MECHANICAL]
**Contract:** Ontology §2, §13. **Files:** `registration/ontology/`.
The canonical module is a fixed five-file set:
`entities.yaml`, `data-properties.yaml`, `relationships.yaml`,
`semantic-constraints.yaml`, `lifecycle-constraints.yaml`.
Registration has only `entities.yaml`, `relationships.yaml`, and `attributes.yaml`.
**Missing:** `data-properties.yaml`, `semantic-constraints.yaml`,
`lifecycle-constraints.yaml`. The file set is mandatory even when empty
(placeholder header + empty list). `shared/ontology/` is the reference — it has all
five.

### C-R2 — `attributes.yaml` is a deleted concept and must not exist · [MECHANICAL + SEMANTIC]
**Contract:** Ontology §2 ("There is no `attributes.yaml`"), §4
("`attributes_ref` → deleted"). **File:** `registration/ontology/attributes.yaml` (1143 lines).
All datatype/value properties must live in `data-properties.yaml` as a property-
centric `data_properties:` **list keyed by `id`**. Registration instead keeps a
1143-line `attributes.yaml` whose top level is a **map keyed by entity name**
(`beneficiary:`, `household:`, …) with attributes nested beneath — the exact retired
form. **Mechanical** part: re-serialize flat scalar properties into `data_properties:`
rows. **Semantic** part: the file also carries nested object attributes (`contact`,
`location`, `guardian_status`, `treatment_plan`, `total_income`, `cost_estimate`,
`requested_amount`) that have no representation in the flat property model — these
require a modeling decision (see S-R2) and cannot be mechanically flattened.

### C-R3 — `relationships.yaml` uses the retired cardinality vocabulary · [MECHANICAL]
**Contract:** Ontology §7 (retires `one_to_one`/`one_to_many`/`many_to_many`/
`many_to_one`; mandates `{min, max}`). **File:** `registration/ontology/relationships.yaml`.
Every one of the 19 relationship rows uses the retired enum
(`cardinality: one_to_one`, `one_to_many`, `many_to_many`, `zero_to_many`,
`zero_to_one`). None uses `{min, max}`. This blocks the generator's single
cardinality code path.

### C-R4 — All 9 taxonomy files use non-conformant root shapes · [MECHANICAL]
**Contract:** Taxonomy §5 (payload is always a top-level `schemes:` list of
`id`-keyed records), §6 (`concepts:` list). **Files:** all of `registration/taxonomy/*`.
This is the finding the taxonomy contract §2 already names against registration:
- **T-5 shape 4 (flat root-level scheme keys):** `actors.yaml`
  (`registrant_types:`, `claim_basis:`, `proxy_consent:`), `needs.yaml`
  (`need_source:`, `need_categories:`, `need_duration:`), `claims.yaml`,
  `situations.yaml`, `case-outcomes.yaml`, `lead-statuses.yaml`,
  `referral-sources.yaml` — the scheme name is the YAML key, not an `id:` field
  in a `schemes:` list.
- **T-5 shape 5 (map keyed by category):** `evidence.yaml` `evidence_types:` is a
  map (`documentary:`/`physical:`/`testimonial:`) with nested subtypes, plus two
  further ungoverned root structures (`availability_classifications:`,
  `claim_evidence_matrix:`). Worst-shaped file in the domain.
- Many schemes additionally wrap members in a `values:` sub-key
  (`claim_basis.values`, `proxy_consent.values`, `need_source.values`,
  `trajectory.values`, `trigger_events.values`, `affected_domains.values`,
  `need_duration.values`, `information_sufficiency.values`,
  `information_consistency.values`) rather than the canonical `concepts:` list.
A generator cannot walk any of these with one code path.

### C-R5 — Duplicate source of truth: inline `values:` alongside `values_ref:` · [MECHANICAL]
**Contract:** Ontology §5 (exactly one of `datatype`/`taxonomy_ref`; coded values
are owned by the taxonomy, not duplicated). **File:** `attributes.yaml` (pervasive).
Nearly every coded property carries **both** a `values_ref:` pointer **and** an
inline `values: [...]` copy of the same enumeration — e.g. `gender`
(`values_ref: …persons.yaml#gender_vocabulary` **and** `values: [male, female,
not_disclosed]`), `need_category`, `claim_type`, `trajectory`, `case.status`, etc.
The enumerated members exist in two places that can silently drift. The taxonomy
scheme must be the single owner; the ontology property carries only a
`taxonomy_ref` scheme reference.

### C-R6 — Taxonomy hierarchy is expressed by embedded children · [MECHANICAL + SEMANTIC]
**Contract:** Taxonomy §6/§7 (hierarchy only via a child concept's `parent`;
`subtypes`/`allowed_subtypes` embedding is deleted). **Files:** `actors.yaml`
(`proxy.subtypes`), `needs.yaml` (every `need_categories[*].subtypes`),
`evidence.yaml` (`physical.subtypes`, `testimonial.subtypes`).
**Mechanical** part: invert each embedded child into a sibling concept with
`parent:`. **Semantic** part: this forces a decision on *scheme boundaries* — e.g.
whether `therapeutic_nutrition`, `surgical_treatment`, … are members of the same
scheme as their parent category (linked by `parent`) or a distinct `need_subtypes`
scheme. That boundary choice is a modeling decision, not a re-serialization (see S-R4).

### C-R7 — Non-`xsd` datatypes block generation · [MECHANICAL]
**Contract:** Ontology §5 (`datatype` values are real `xsd:*` tokens as YAML values).
**File:** `attributes.yaml`.
Properties declare `type: string | integer | enum | boolean | date | datetime |
float | number | object | list`. None are `xsd:*` tokens. Every literal property
must map to an `xsd:*` datatype (`string`→`xsd:string`, `datetime`→`xsd:dateTime`,
etc.); every coded (`type: enum`) property must instead carry a `taxonomy_ref` and
**no** `datatype`. `object`/`list` types have no scalar mapping — they resolve
through S-R2, not mechanically.

### C-R8 — Broken relationship target: `verification_brief` is not an entity · [MECHANICAL + SEMANTIC]
**Contract:** Ontology §6 (`to` is a target entity `id` or a cross-domain CURIE).
**File:** `relationships.yaml`, row `case_produces_verification_brief` → `to: verification_brief`.
`verification_brief` is defined **nowhere** in `entities.yaml`; the codebase
explicitly states it is a *projection of the Case*, not a stored entity
(`entities.yaml` case note; `verification/verification-brief-projection.yaml`).
The relationship therefore points at a dangling target. **Decision required**
(semantic): either drop this row (the projection is not part of the entity graph)
or model the projection explicitly. It cannot simply be re-serialized as-is.

### C-R9 — Taxonomy record shape has no addressable scheme identity · [MECHANICAL]
**Contract:** Taxonomy §3, §5 (a scheme's identity is `(domain, scheme_id)` via an
explicit `id:` field). **Files:** all `registration/taxonomy/*`.
Because schemes are YAML keys (C-R4), no scheme has an `id:` field distinct from its
file position, and `taxonomy_ref` on the ontology side cannot resolve to a stable
scheme identifier. This is the precondition that must be fixed before any
`taxonomy_ref`/`references` CURIE can be minted.

---

## Required Findings

*Mandatory for full conformance, but they do not by themselves block a first
generation pass. Fix after the Critical set.*

### R-R1 — Ontology & taxonomy headers are non-conformant · [MECHANICAL]
**Contract:** Ontology §12 / Taxonomy §4 (mandatory top-level keys `version`,
`domain`, `file`, `status`; `version` is quoted `"MAJOR.MINOR.PATCH"`;
`status ∈ {active, placeholder, draft, deprecated}`). **Files:** every registration file.
- **`status` missing** on `entities.yaml`, `relationships.yaml`, `attributes.yaml`,
  and 7 of 9 taxonomy files.
- **Invalid `status`:** `evidence.yaml` has `status: Level_1` (not in the enum — a
  T-4 violation). `support-interventions.yaml` `status: placeholder` is valid.
- **`version` format:** all files use two-part `"1.1"` / `"1.0"`, not three-part
  `"1.1.0"`. Reference `shared/*` uses `"1.0.0"`.
- **`file:` path** is module-relative (`ontology/entities.yaml`); the contract and
  `shared/ontology/entities.yaml` use repo-relative (`shared/ontology/entities.yaml`).
  (Note: `shared/taxonomy` is itself inconsistent here — flag exists repository-wide,
  but registration should follow the repo-relative form the contract states.)

### R-R2 — `entities.yaml` carries forbidden fields · [MECHANICAL]
**Contract:** Ontology §4 (`key_attributes` → `data-properties.yaml`;
`attributes_ref` → deleted). **File:** `entities.yaml`.
Every entity carries a `key_attributes:` list **and** an `attributes_ref:` pointer.
`key_attributes` duplicates the property ownership that belongs in
`data-properties.yaml`; `attributes_ref` is a deleted concept. Both must be removed
once `data-properties.yaml` exists (property `domain:` fields carry the ownership).

### R-R3 — Inconsistent entity-presence field naming · [MECHANICAL]
**Contract:** Ontology §1 (entity-presence cardinality `cardinality_in_case` is a
deferred, tolerated axis — `shared/ontology/entities.yaml` keeps it). **File:** `entities.yaml`.
Most entities use `cardinality_in_case: exactly_one | one_or_more | zero_or_more`
(acceptable, matches `shared/`). But `case`, `lead`, and `volunteer_review` instead
use a bare `cardinality:` key (`one_per_registration_conversation`, `zero_or_one`) —
a different, ad-hoc field name that collides with the property-cardinality term.
Normalize all entities to the single `cardinality_in_case` field.

### R-R4 — `relationships.yaml` carries a forbidden `required:` field and ad-hoc keys · [MECHANICAL]
**Contract:** Ontology §6 (no `required:`; obligation is `cardinality.min ≥ 1`; the
row field set is `id`/`from`/`relationship`/`to`/`cardinality`/`inverse`/`notes`).
**File:** `relationships.yaml`.
Rows carry `required: true`, `minimum: 1`, and `closure_rule:` — none are in the §6
field set. `required`/`minimum` fold into `{min, max}`; `closure_rule:` is lifecycle
semantics that belongs in `lifecycle-constraints.yaml` or reasoning, not on the edge.

### R-R5 — Taxonomy cross-references use `imports:`/file paths, not `references:` · [MECHANICAL, manifest-blocked for values]
**Contract:** Taxonomy §8 (cross-refs are structured `references:` records with
`scheme`/`relation`/`note`; never a bare `imports:` path). **Files:** `actors.yaml`
(`imports: shared/taxonomy/persons.yaml`), `evidence.yaml`
(`imports: [shared/taxonomy/document-types.yaml, registration/taxonomy/claims.yaml]`).
Re-express as `references:` entries. The **shape** fix is mechanical now; the CURIE
**values** depend on the manifest/C-2 (see Repository Readiness).

### R-R6 — Ontology `values_ref:` file paths must become `taxonomy_ref` scheme CURIEs · [MECHANICAL, manifest-blocked for values]
**Contract:** Ontology §5, §10; Taxonomy §3 (`taxonomy_ref` names a **scheme** CURIE,
resolved via manifest; never a file path). **File:** `attributes.yaml` (24 occurrences).
All `values_ref:` values are file-path#fragment strings
(`shared/taxonomy/persons.yaml#gender_vocabulary`,
`registration/taxonomy/needs.yaml#need_categories`, …). Under the contract these
become `taxonomy_ref:` scheme CURIEs. Structure is fixable now; literal prefixes wait
on C-2.

### R-R7 — Embedded constraint/reasoning logic inside attribute schemas · [SEMANTIC]
**Contract:** Ontology §2 (five-file separation), §9 (constraints are target-neutral
rows in `semantic-constraints.yaml`). **File:** `attributes.yaml`.
`attributes.yaml` conflates four concerns the contract separates: property typing
(→ `data-properties.yaml`), constraints (`required_when`, `derivation`, `validation`,
`coherence_rule` → `semantic-constraints.yaml`), gap logic (`gap_type`,
`gap_condition` → `reasoning/gaps`), and prose guidance (`notes`). Splitting these is
a **semantic relocation**, not a re-serialization: each `required_when` becomes a
`required_if` constraint row; each `gap_condition` moves to the reasoning layer that
already exists. Must be planned deliberately to avoid losing detection semantics.

### R-R8 — `claim_evidence_matrix` is a constraint, not a taxonomy scheme · [SEMANTIC]
**Contract:** Taxonomy §5 (taxonomy payload is `schemes:` of `concepts:`; constraints
are not taxonomy content). **File:** `evidence.yaml`.
`claim_evidence_matrix:` maps each `claim_type` to allowed evidence types/subtypes —
a cross-scheme validation rule, not an enumerated vocabulary. It has no home in the
taxonomy record shape. Decision required: relocate to a constraint/reasoning surface
(e.g. `semantic-constraints.yaml` as `mutually_exclusive`/`allowed_values` rows, or a
registration reasoning file). Not a taxonomy scheme.

### R-R9 — Cross-domain vocabulary ownership is unresolved (actors vs shared persons) · [SEMANTIC]
**Contract:** Taxonomy §9 / ADR-008 (every concept has exactly one owning scheme in
one owning domain; cross-domain use is a `references` link, never redefinition).
**Files:** `registration/taxonomy/actors.yaml` vs `shared/taxonomy/persons.yaml`.
`actors.yaml` `registrant_types` = `[beneficiary, proxy, volunteer]` overlaps
`shared/taxonomy/persons.yaml` `person_roles` = `[beneficiary, registrant, proxy,
volunteer, …]`. The shared file's comment says these roles are "declared here,
detailed in registration/taxonomy/actors.yaml" — an intended `extends` relationship
currently expressed as duplication. Must be resolved as a `references: {relation:
extends}` link with a single owner, not two copies.

### R-R10 — `need_severity` vocabulary is externally owned and duplicated · [SEMANTIC]
**Contract:** Taxonomy §9; Ontology §5. **File:** `attributes.yaml` `need.need_severity`.
`need_severity` carries `values_ref: needs-assessment/taxonomy.yaml#need_severity`
(a cross-domain reference to the **un-migrated** `needs-assessment/taxonomy.yaml`
monolith) **and** an inline `values: [critical, high, medium, low]`. Registration's
own `taxonomy/needs.yaml` does **not** define `need_severity`. Ownership must be
decided: does registration own severity, or does it reference needs-assessment? The
target is currently non-conformant (needs-assessment is not yet a migrated domain),
creating a dependency on a domain outside this audit's scope.

### R-R11 — `support-interventions.yaml` placeholder body is non-canonical · [MECHANICAL]
**Contract:** Taxonomy §5, §13 (a placeholder file has the standard header +
`status: placeholder` and an empty/absent `schemes:` list). **File:** `support-interventions.yaml`.
The file carries `status: placeholder` (good) but its body is ad-hoc keys
(`concepts_this_file_will_own:`, `dependency_note:`, `do_not_implement_until:`) with
no `schemes:` list. Normalize to the placeholder template; the planning prose can
live in `purpose:` or the domain governance doc.

---

## Optional Findings

*Cleanups and enhancements. None blocks conformance or generation.*

### O-R1 — Reusable-predicate granularity: generic `has` · [SEMANTIC · OPTIONAL]
**Contract:** Ontology §6/§11 (reusable predicates). **File:** `relationships.yaml`.
The predicate `has` is reused for eight structurally different compositions
(case→registrant, →beneficiary, →household, →situation, →need, …). This is legal
(domain-local predicate) but collapses distinct semantics into one edge label.
Consider more specific predicates (`has_beneficiary`, `has_situation`) or accept the
generic form. No conformance impact.

### O-R2 — Missing `inverse` declarations · [FUTURE · OPTIONAL]
**Contract:** Ontology §6 (`inverse` optional). **File:** `relationships.yaml`.
Clear inverse pairs exist (`registrant_conducts_case` / `case_has_registrant`;
`beneficiary_is_member_of_household` / `household_has_members`) but no row uses the
`inverse:` field. Adding it lets the generator emit `owl:inverseOf`. Enhancement only.

### O-R3 — `gaps/gap-types.yaml` placement is ambiguous · [SEMANTIC · OPTIONAL]
**Contract:** Ontology §13 template (no `gaps/` folder; `reasoning/` holds domain
rules). **File:** `gaps/gap-types.yaml`.
`gap-types.yaml` is a controlled vocabulary (records with `id`/`description`/
`severity`) living in a non-template `gaps/` folder. Open question for review:
is it a taxonomy scheme (→ `taxonomy/`) or a reasoning vocabulary (→ `reasoning/`)?
Either is defensible; the current standalone `gaps/` folder matches neither the
ontology nor taxonomy template. Non-blocking; decide during migration.

### O-R4 — Duplicate `description` in `gap-types.yaml` · [MECHANICAL · OPTIONAL]
`contact_gap` and `location_gap` share the identical description "No way to reach or
find the beneficiary." Distinguish them. Content polish only.

### O-R5 — Extension-field inventory is undeclared · [FUTURE · OPTIONAL]
**Contract:** Taxonomy §6/T-9 (extension fields permitted but bounded). **Files:** taxonomy/*.
Registration concept records carry many extension fields (`default_claim_basis`,
`questioning_note`, `verification_weight`, `contextual_prior`,
`requires_linked_member`, `inference_note`, `temporal_note`, `indicators`,
`hold_triggers`, `referring_organisation_types`, …). These are *allowed* as domain
extensions, but no declaration distinguishes core from extension. Optionally record
the domain's extension set in governance so a generator knows what it may ignore.
Note: `indicators:` and `referring_organisation_types:` are effectively embedded
sub-vocabularies that *could* be promoted to their own schemes — a modeling call,
deferred.

### O-R6 — Ancillary subfolders don't match the canonical header · [MECHANICAL · OPTIONAL]
**Files:** `reasoning/*`, `readiness/*`, `questioning/*`, `verification/*`, `gaps/*`.
These modules are **not governed** by either contract (ontology §13 lists
`reasoning/` as "unchanged by this spec"; the others are domain-specific). Their
two-part `version:` / missing `status:` headers are therefore **not violations**.
Aligning them to the canonical header shape anyway would give the repository one
header convention everywhere — optional consistency, not conformance.

### O-R7 — `registrant_type` denormalized onto `case` · [SEMANTIC · OPTIONAL]
**File:** `attributes.yaml` (`case.registrant_type` mirrors `registrant.registrant_type`).
A deliberate denormalization (documented in the notes). Acceptable as a modeled
duplicate; flagged only so the migration records it as intentional, not an accident.

---

## Repository Readiness

**Can registration be migrated to full conformance today? Partially.**

| Gate | State | Blocks what |
|------|-------|-------------|
| Ontology contract frozen | ✅ approved | — |
| Taxonomy contract frozen | ✅ approved | — |
| Reference implementation exists (`shared/`) | ✅ present | — |
| **Manifest / catalog (Finding R-1)** | ❌ **absent** | All CURIE minting: R-R5, R-R6, R-R9 *values* |
| **Literal base IRI + prefixes (Finding C-2)** | ❌ **not ratified** | Same — the literal CURIE strings |
| Versioning policy (Finding R-3) | ⚠️ open | `owl_version_iri` only (not mandatory) |
| `needs-assessment` domain migrated | ❌ not migrated | R-R10 target resolution |

**What this means for sequencing:**

- **Manifest-independent work can start immediately.** Everything that is a pure
  shape change — file-set completion (C-R1), `schemes:`/`concepts:` list conversion
  (C-R4, C-R6, C-R9), cardinality `{min,max}` (C-R3), header normalization (R-R1),
  removing forbidden fields (R-R2, R-R4), `xsd` datatypes (C-R7), de-duplicating
  inline `values:` (C-R5) — needs **no** external dependency. This is the bulk of the
  work.
- **CURIE-bound work is blocked** on the manifest (R-1) and C-2. The *structure* of
  `references:`/`taxonomy_ref` can be laid down now with same-domain bare ids; the
  *cross-domain literal prefixes* cannot be finalized until C-2. Attempting to mint
  them now would hard-code values C-2 may change.
- **One finding (R-R10) depends on a domain outside this audit** (`needs-assessment`),
  which is itself un-migrated. Severity-vocabulary ownership should be decided during
  registration migration but may leave a temporary same-domain placeholder until
  needs-assessment migrates.

**Conclusion:** Registration is **migration-ready for its mechanical and semantic
work now**, and **conformance-completable only after** the manifest/C-2 land. It
should not be *declared* the canonical reference until the CURIE layer is closed —
but it can and should be normalized up to that boundary first.

---

## Recommended Migration Order

Ordered to keep every step independently verifiable and to defer only what is truly
manifest-blocked. Each step is one reviewable change.

**Phase 0 — Decisions (no file changes; review gate)**
0.1 Ratify the semantic decisions (S-list below): `verification_brief` disposition
    (C-R8), nested-object modeling (S-R2/C-R2), scheme-boundary for subtypes
    (C-R6), `claim_evidence_matrix` relocation (R-R8), actors-vs-persons ownership
    (R-R9), `need_severity` ownership (R-R10), `gaps/` placement (O-R3).
    *These gate the mechanical work that depends on them.*

**Phase 1 — Headers & file set (mechanical, no dependencies)**
1.1 Normalize all governed-file headers to `{version:"x.y.z", domain, file, status}`
    (R-R1).
1.2 Create the three missing ontology files as placeholders
    (`data-properties.yaml`, `semantic-constraints.yaml`,
    `lifecycle-constraints.yaml`) (C-R1).

**Phase 2 — Taxonomy re-serialization (mechanical)**
2.1 Convert every taxonomy file to `schemes:` → `concepts:` lists; give each scheme
    an explicit `id` (C-R4, C-R9); drop `values:` wrappers and `type: enum`.
2.2 Invert embedded `subtypes`/`allowed_subtypes` into `parent` per the Phase-0
    scheme-boundary decision (C-R6).
2.3 Normalize placeholder file `support-interventions.yaml` (R-R11); relocate
    `claim_evidence_matrix` out of `evidence.yaml` per decision (R-R8).

**Phase 3 — Ontology entities & relationships (mechanical)**
3.1 `relationships.yaml`: convert cardinality to `{min,max}` (C-R3); drop
    `required:`/`minimum:`/`closure_rule:` (R-R4); resolve `verification_brief`
    row per decision (C-R8).
3.2 `entities.yaml`: remove `key_attributes` and `attributes_ref` (R-R2); normalize
    entity-presence to `cardinality_in_case` (R-R3).

**Phase 4 — Attribute decomposition (mechanical + semantic, largest step)**
4.1 Split `attributes.yaml` into: flat scalar properties → `data-properties.yaml`
    with `xsd:*` datatypes (C-R7) and one-of `datatype`/`taxonomy_ref` (C-R5);
    constraints (`required_when`, `validation`, `derivation`, `coherence_rule`) →
    `semantic-constraints.yaml` (R-R7); gap logic → existing reasoning layer.
4.2 Model nested-object attributes per the Phase-0 decision (S-R2).
4.3 Delete `attributes.yaml` once fully drained (C-R2).

**Phase 5 — CURIE layer (BLOCKED on manifest R-1 / C-2)**
5.1 Register registration in the manifest; convert `values_ref:` → `taxonomy_ref:`
    scheme CURIEs (R-R6) and `imports:` → `references:` (R-R5); finalize
    cross-domain prefixes and the actors/persons and severity ownership links
    (R-R9, R-R10).

**Phase 6 — Optional polish (any time)**
6.1 O-R1, O-R2, O-R4, O-R5, O-R6, O-R7 as capacity allows.

**Validation after each phase:** re-run this conformance check against the touched
files; confirm no downstream reference in `reasoning/`, `readiness/`, `questioning/`,
`verification/` broke (they reference attribute/entity/taxonomy names that shift in
Phases 2–4).

---

## Scope of Future Implementation

The three classes, consolidated and **kept separate** as instructed.

### A. Mechanical structural fixes (deterministic re-serialization, no meaning change)
> These are safe, reviewable, and the bulk of the work. Do these; do not deliberate them.

- C-R1 create the 5-file set · C-R3 `{min,max}` cardinality · C-R4 `schemes:`/`concepts:`
  lists · C-R5 remove duplicate inline `values:` · C-R7 `xsd:*` datatypes ·
  C-R9 explicit scheme `id`s.
- R-R1 header normalization · R-R2 remove `key_attributes`/`attributes_ref` ·
  R-R3 unify `cardinality_in_case` · R-R4 remove `required:`/`minimum:`/`closure_rule:` ·
  R-R11 placeholder normalization.
- O-R4 dedupe descriptions · O-R6 (optional) align ancillary headers.
- The **mechanical portion** of C-R2 (flat property re-serialization) and R-R5/R-R6
  (reference *shape*, not values).

### B. Semantic issues (require a modeling decision before action; may clarify meaning)
> These must be reviewed and decided (Phase 0) before the mechanical work that depends
> on them. They are **not** to be resolved by re-serialization.

- C-R2 / S-R2 — how to model nested-object attributes (`contact`, `location`,
  `guardian_status`, `treatment_plan`, `total_income`, `cost_estimate`,
  `requested_amount`): sub-entities vs flattened properties.
- C-R6 — scheme-boundary decision for need/evidence/actor subtypes (same scheme +
  `parent`, or distinct `*_subtypes` scheme).
- C-R8 — disposition of the `verification_brief` relationship target (drop vs model).
- R-R7 — how detection/constraint logic in `attributes.yaml` splits across
  `semantic-constraints.yaml` and the reasoning layer without losing semantics.
- R-R8 — where `claim_evidence_matrix` lives once it leaves the taxonomy.
- R-R9 / R-R10 — cross-domain vocabulary ownership (actors↔persons; severity↔
  needs-assessment).
- O-R1, O-R3, O-R7 — predicate granularity, `gaps/` placement, denormalization
  (all optional, but each is a modeling call, not a mechanical one).

### C. Future enhancements (neither blocks conformance nor generation)
> Defer until content and conformance are settled.

- O-R2 `inverse` declarations · O-R5 extension-field declaration + possible promotion
  of `indicators`/`referring_organisation_types` to their own schemes.
- `owl_version_iri` policy (Finding R-3, repository-wide).
- Artifact generation (Finding F-3) — out of scope for the entire freeze/audit phase.
- Localization (Taxonomy §11) — explicitly deferred by the contract.

---

## Explicitly Out of Scope for This Audit

- **`shared/`, `needs-assessment/`, and every other domain** — not audited here,
  though R-R10 surfaces a dependency on `needs-assessment`.
- **The frozen contracts themselves** — not questioned; this audit assumes them as
  authority. No architectural blocker against the contracts was found in registration.
- **Content correctness of registration's domain logic** — the reasoning, severity,
  and questioning *content* is treated as correct; only its structural placement is
  in scope. The two content-level observations noted (category/subtype confusion of
  `therapeutic_nutrition`; duplicate gap descriptions) are flagged but are for the
  domain owner to confirm, not for structural migration to silently change.

---

## Architect Final Review — Corrections to Recommendations

*Added during the pre-implementation architect review. These corrections supersede
the corresponding text above where they conflict. They change recommendations only —
no finding's underlying facts changed. The executable form of these corrections is
`Registration_Migration_Plan.md`.*

- **C-R9 merged into C-R4.** Converting each taxonomy file to a `schemes:` list of
  `id`-keyed records (§5) *is* minting each scheme's explicit `id`. C-R9 named no
  independent work and is withdrawn as a separate finding. **Critical count: 8.**
- **C-R8 default resolution = remove the row.** The repository already declares
  `verification_brief` a projection, not an entity (§6 requires `to` to be an entity/
  CURIE; the design forbids making it an entity). The Phase-0 item is a one-line
  confirmation of removal, not an open design decision.
- **R-R7 splits into mechanical + semantic.** Much of the embedded logic in
  `attributes.yaml` (`gap_type`, `gap_condition`) is a **duplicate** of
  `reasoning/gap-detection-rules.yaml`, and `classification_rules_ref` /
  `transition_rules_ref` are pointers to `reasoning/`/`readiness/`. These are
  **dropped** (mechanical), not relocated — but only after verifying the reasoning
  layer already covers them (new finding **N-R1** below). Only logic owned *solely*
  by `attributes.yaml` (`validation`, `derivation`, genuine `required_if`) relocates
  to `semantic-constraints.yaml` (semantic).
- **N-R1 (new, Required, [SEMANTIC gate → then MECHANICAL]).** Duplicate source of
  truth: `attributes.yaml` `gap_condition`/`gap_type` fields restate
  `reasoning/gap-detection-rules.yaml` detection conditions (e.g. `contact_gap`,
  `location_gap`, `severity_gap`). Before dropping them (R-R7), confirm each is
  present in the reasoning layer; any gap-condition owned *only* by `attributes.yaml`
  must be moved there, not lost. Contract basis: Ontology §2 (five-file separation),
  §9 (constraints/reasoning are their own surfaces).
- **R-R6 splits by reference locality (Ontology §5, §3; Taxonomy §3).**
  **Same-domain** `values_ref` (the ~14 `registration/taxonomy/*` refs) become
  `taxonomy_ref` with a **bare scheme id** — unblocked, mechanical, done in Phase 4.
  Only **cross-domain** refs (`shared/*`, `needs-assessment/*` — 7 refs) need
  manifest-resolved CURIEs and wait for Phase 5. The same split applies to R-R5
  `imports:` (evidence.yaml's `registration/taxonomy/claims.yaml` import is
  same-domain and unblocked; its `shared/*` import waits).
- **R-R2 re-sequenced.** Removing `key_attributes`/`attributes_ref` from
  `entities.yaml` must occur **after** `data-properties.yaml` is populated (Phase 4),
  not in Phase 3 — otherwise attribute ownership has no home during the window.
- **C-R5 de-dup carries an equality precondition.** Dropping an inline `values:` list
  is mechanical **only if** it equals the referenced scheme's concept ids. Any
  mismatch is a semantic reconciliation, not a deletion. Verified matches so far:
  `need_category`, `case.status`. Unverified/cross-domain: `gender`, `need_severity`,
  capability/location refs — check before dropping.
- **O-R1 and O-R5 reclassified to "no action during migration."** Generic `has`
  (§6/§11 permit reusable predicates) and list-valued extension fields (§6/T-9 permit
  them) are **conformant as-is**. Changing them is scope creep; Sonnet must leave them
  untouched to avoid rework.
- **Entity-level `notes:` — tolerated.** `entities.yaml` uses `notes:` on some
  entities. §4 neither lists it as a field nor in its "Not permitted" set; like
  `cardinality_in_case` it is a tolerated extension. **No action** (do not fold into
  `description`; that would be an unrequested content edit).

*End of audit. No files were modified. Awaiting review before any implementation.*
