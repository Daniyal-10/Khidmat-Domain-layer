# Registration Domain — Migration Implementation Plan

> **Audience:** the executing agent (Sonnet). **Status:** Phase 1 complete; Phase 2
> paused — a Content Completion Gate is open (see Registration Content Gap Log below).
> **Authorities:** `Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`
> (frozen structural contracts) and `Repository_Migration_Methodology.md` (frozen
> process contract — governs *how* this plan is executed; this plan states only
> what is specific to registration). **Companion:** `Registration_Domain_Audit.md`
> (findings + architect corrections).
>
> **Design intent of this plan:** once Phase 0 is approved, every later phase is
> **mechanical**, under the principles and source-authority rules
> `Repository_Migration_Methodology.md` defines once for every domain. This document
> contains only registration-specific facts: which files are affected, which concepts
> exist, which domain-specific decisions (D1–D6) had to be made, and the current
> Content Gap Log. It does not restate general migration policy — see the methodology
> document for that.

---

## How to use this plan

This plan follows `Repository_Migration_Methodology.md` §1 (principles), §10
(approval gates), and §9 (stopping criteria) exactly; only registration-specific
sequencing notes are repeated here:

1. **Phase 0 is a human gate** (methodology §10, Gate 0). Sonnet does not execute
   Phases 1–5 until the Decision Table (§Phase 0) is filled with approved values.
2. **Phases run in order**, each with explicit preconditions (methodology §10,
   per-phase gate).
3. **Phase 2 is additionally gated by the Content Completion Gate** (methodology
   §6/§10): it cannot be marked complete while the Registration Content Gap Log
   below is non-empty.
4. **Phase 5 is externally blocked** (manifest / Finding C-2 / cross-domain target
   migration). Registration reaches "canonical up to the CURIE boundary" after Phase 4
   and "fully canonical" only after Phase 5 unblocks. This is expected and acceptable.

---

## Registration Content Gap Log

Per `Repository_Migration_Methodology.md` §5/§6: these records were checked
exhaustively against every governed registration file, every other domain's
governed files (via the canonical ownership registry), and — before that
registry check was known to be the correct test — against general repository
documentation (confirmed **not** a valid source per methodology §2). Nineteen
records were confirmed as genuine content gaps (one of which, `registrant_types`,
has an incidental match in `GLOSSARY.md`, which is documentation, not a governed
file, and is therefore correctly excluded, not "recovered," to keep the domain's
gap handling uniform).

**Phase 2 does not complete until every row below is closed** by a
domain-knowledgeable author writing the real `description` directly into the
governed source file (methodology §6). No placeholder text and no `status`
change are written by the migration process for any of these.

| Status | File | Scheme / concept |
|---|---|---|
| OPEN | `actors.yaml` | `registrant_types` (scheme) |
| OPEN | `needs.yaml` | `need_categories` (scheme) |
| OPEN | `needs.yaml` | `need_duration` (scheme) |
| OPEN | `needs.yaml` | `need_severity` (scheme) |
| OPEN | `needs.yaml` | `need_severity.critical` |
| OPEN | `needs.yaml` | `need_severity.high` |
| OPEN | `needs.yaml` | `need_severity.medium` |
| OPEN | `needs.yaml` | `need_severity.low` |
| OPEN | `claims.yaml` | `claim_types` (scheme) |
| OPEN | `evidence.yaml` | `evidence_types` (scheme) |
| OPEN | `evidence.yaml` | `availability_classifications` (scheme) |
| OPEN | `situations.yaml` | `trigger_events.bereavement` |
| OPEN | `situations.yaml` | `trigger_events.job_loss` |
| OPEN | `situations.yaml` | `trigger_events.accident_or_injury` |
| OPEN | `situations.yaml` | `trigger_events.illness_onset` |
| OPEN | `situations.yaml` | `trigger_events.displacement` |
| OPEN | `situations.yaml` | `trigger_events.domestic_violence` |
| OPEN | `situations.yaml` | `trigger_events.natural_disaster` |
| OPEN | `situations.yaml` | `trigger_events.legal_crisis` |

**Known carry-over requiring correction before Phase 2 resumes:** the working
tree currently contains, in `actors.yaml`, `needs.yaml`, `claims.yaml`,
`evidence.yaml`, and `situations.yaml`, placeholder description text and a
`status: draft` change written under a since-superseded draft of Phase 2 rule
10 (before this methodology was adopted). Two distinct corrections are needed
once Phase 2 resumes, and they are independent of each other:
- The fabricated placeholder text on the nineteen records above must be
  **removed**, leaving those specific `description` fields absent (accurately
  reflecting an open genuine gap, per methodology §5), while the surrounding
  *structural* conversion those files already received (the `schemes:`/
  `concepts:` shape, `parent`-expressed hierarchy, extension-field
  preservation) is **not** undone — that part remains valid, mechanical work.
- Each file's `status` must be **reverted to `active`** (its Phase 1 value) —
  not because the content is complete, but because status is never inferred
  from content completeness in the first place (methodology principle 1).
This correction is **not** performed now; no domain files are modified by this
update.

---

# PHASE 0 — Review Decisions (no file changes)

**Objective.** Resolve every irreducible semantic decision so all later work is
mechanical. **Mechanical/Semantic:** Semantic (human). **Files affected:** none.
**Expected output:** an approved Decision Table (below), pasted back into this plan.

Each decision cites the contract section that constrains it and gives a recommended
default. Where the contract *forces* the outcome, that is noted — those need only
confirmation.

### Decision Table

| ID | Decision | Contract basis | Recommended default | Approved value |
|----|----------|----------------|---------------------|----------------|
| **D1** | Disposition of the `case_produces_verification_brief` relationship row (target `verification_brief` is a projection, not an entity). | Ontology §6 (`to` must be an entity/CURIE); repo design states it is not an entity. | **Remove the row.** Contract + existing design both forbid the alternative (inventing the entity). Near-forced. | ☑ Approved (default) |
| **D2** | How embedded taxonomy `subtypes` become hierarchy. | Taxonomy §7 (`parent` must name a **same-scheme** sibling; cross-scheme parent forbidden). | **One scheme per existing grouping; each embedded subtype becomes a concept in that same scheme with `parent = <enclosing concept id>`.** This is the only §7-conformant way to preserve the hierarchy. Applies uniformly to `needs.yaml` (categories+subtypes), `actors.yaml` (`proxy` sub-roles), `evidence.yaml` (`physical`/`testimonial` observations). | ☑ Approved (default) |
| **D3** | Destination of `evidence.yaml` `claim_evidence_matrix` (a claim-type→allowed-evidence mapping — not a vocabulary). | Taxonomy §5 (not taxonomy content); Ontology §9 constraint-type vocabulary is **closed** (`cardinality`/`disjoint`/`required_if`/`mutually_exclusive`) and does not include an "allowed-values matrix" type. | **Relocate to a new `registration/reasoning/evidence-rules.yaml`** (the `reasoning/` layer is un-governed by the contracts and may hold domain validation tables). Do **not** force it into `semantic-constraints.yaml` (no matching closed constraint type without amending a frozen contract). | ☑ Approved (default) |
| **D4** | Ownership of the registrant-role vocabulary shared between `registration/taxonomy/actors.yaml` (`registrant_types`) and `shared/taxonomy/persons.yaml` (`person_roles`). | Taxonomy §9 / ADR-008 (one owning scheme; cross-domain use is a `references` link, never redefinition). `persons.yaml` comment already says roles are "declared here, detailed in registration." | **`shared` owns the role identities; `registration/taxonomy/actors.yaml` keeps only the registration-specific epistemic detail (`default_claim_basis`, `questioning_note`, `proxy` sub-roles) and links via `references: {relation: extends, scheme: <persons person_roles>}`.** (CURIE finalized in Phase 5.) | ☑ Approved (default) |
| **D5** | Ownership of `need_severity` (referenced from un-migrated `needs-assessment/taxonomy.yaml`, also inlined in registration). | Taxonomy §9; Ontology §5. Target domain is not migrated and is non-conformant. | **Registration temporarily owns a local `need_severity` scheme** in `registration/taxonomy/needs.yaml` (`critical/high/medium/low`), with a `references` note to reconcile with `needs-assessment` when that domain migrates. Unblocks registration now; defers the cross-domain merge to its proper governance step. | ☑ Approved (default) |
| **D6** | How nested-object attributes are modeled (the flat `data-properties` model has no object/list datatype). | Ontology §5 (a data property has exactly one `datatype`/`taxonomy_ref`; no nested objects). | **Promote each nested object to its own entity + a relationship from the owner; its scalar fields become that entity's data-properties.** Mapping table below. Deterministic once approved. *(This is the highest-review-value decision — it grows the entity graph. Override here if a different granularity is wanted.)* | ☑ Approved (default) |

**D6 nested-object → entity mapping (applies only if D6 default approved):**

| Owner.attribute (in `attributes.yaml`) | New entity | Owner→entity relationship (cardinality) |
|---|---|---|
| `beneficiary.contact`, `registrant.contact` | `contact_point` | `has_contact` (0..1 each) |
| `beneficiary.location` | `location` | `has_location` (1..1) |
| `household.guardian_status` | `guardian` | `has_guardian` (0..1) |
| `household.total_income` | `income` | `has_income` (0..1) |
| `need.treatment_plan` | `treatment_plan` | `has_treatment_plan` (0..1) |
| `need.cost_estimate` | `cost_estimate` | `has_cost_estimate` (0..1) |
| `support_intervention.requested_amount` | `requested_amount` | `has_requested_amount` (0..1) |
| `case.open_gaps` (list) | `open_gap` | `has_open_gap` (0..unbounded) |

*Note (future, not this migration): `income`, `cost_estimate`, `requested_amount`
share an amount/currency shape and could later consolidate into a shared monetary
value — deliberately **not** done now to avoid a cross-domain promotion decision.*

### Phase 0 validation checklist
- [ ] Every decision D1–D6 has an approved value (default or override).
- [ ] Any override is reconciled against the citing contract section (no override
      violates a frozen rule).
- [ ] The approved Decision Table is pasted back into this plan.
- [ ] No repository file was modified during Phase 0.

---

# PHASE 1 — Headers & File Set (mechanical)

**Objective.** Bring every governed file's header to the canonical shape and create the
missing ontology files as placeholders. **Mechanical/Semantic:** Mechanical.
**Preconditions:** Phase 0 approved.

**Files affected:**
- Headers: `registration/ontology/{entities,relationships}.yaml`;
  `registration/taxonomy/*.yaml` (all 9).
- New placeholders: `registration/ontology/data-properties.yaml`,
  `registration/ontology/semantic-constraints.yaml`,
  `registration/ontology/lifecycle-constraints.yaml`.
- (`attributes.yaml` header is **not** touched — the file is deleted in Phase 4.)

**Rules (deterministic):**
1. Header = exactly four top-level keys, in order: `version`, `domain`, `file`,
   `status` (Ontology §12 / Taxonomy §4).
2. `version: "1.1.0"` (promote every two-part `"1.1"`/`"1.0"` to three-part quoted
   semver; keep the existing major.minor, append `.0`).
3. `domain: registration` (unchanged).
4. `file:` = **repo-relative** path, e.g. `registration/ontology/entities.yaml`
   (match `shared/ontology/entities.yaml`; replace the current module-relative form).
5. `status: active` for all populated files; `status: placeholder` for the three new
   ontology placeholders and for `support-interventions.yaml`. Replace the invalid
   `status: Level_1` on `evidence.yaml` with `active`.
6. Placeholder ontology files contain header + the canonical empty payload:
   `data_properties: []`, `constraints: []`, and (lifecycle) `# no lifecycle
   semantics yet` per the `shared/ontology` placeholder convention.

**Expected output.** All governed registration files carry an identical, conformant
four-key header; the ontology module physically contains all five canonical files.

### Phase 1 validation checklist
- [ ] Every governed file's first four keys are `version`/`domain`/`file`/`status`,
      no comment banners, no nested `metadata:`.
- [ ] Every `version` is a quoted three-part string.
- [ ] Every `status` ∈ {`active`, `placeholder`}; no `Level_1`.
- [ ] Every `file:` value equals the file's true repo-relative path.
- [ ] `registration/ontology/` now lists exactly the five canonical files (+ the
      still-present `attributes.yaml`, removed in Phase 4).
- [ ] No payload/content below the header changed in any file this phase.

---

# PHASE 2 — Taxonomy Re-serialization (mechanical, gated by D2/D5, gated by Content Completion Gate)

**Objective.** Convert all 9 taxonomy files to the canonical `schemes:` → `concepts:`
list shape. **Mechanical/Semantic:** Mechanical (rules fixed by D2/D5).
**Preconditions:** Phase 1 done; D2 and D5 approved; the Registration Content Gap
Log above is **empty** (`Repository_Migration_Methodology.md` §6/§10, Content
Completion Gate) — Phase 2 cannot be marked complete while it is not, and the
known carry-over (above) must be corrected first.

**Files affected:** all `registration/taxonomy/*.yaml`.

**Rules (deterministic):**
1. Payload root is a single `schemes:` **list** (Taxonomy §5). Each current root
   scheme-key (`registrant_types:`, `need_categories:`, `claim_types:`,
   `case_statuses:`, `trajectory:`, …) becomes a `schemes:` list item with an explicit
   `id:` equal to the former key. (This subsumes former finding C-R9.)
2. Drop every `values:` wrapper — the concept list moves directly under `concepts:`
   (Taxonomy §6).
3. Each concept is a record with `id` (required), `description` (required), `label`
   (optional). Preserve existing `label`/`description`.
4. **Hierarchy (D2 default):** each embedded `subtypes` child becomes a concept in the
   **same scheme** with `parent: <enclosing concept id>`. Delete the `subtypes`/
   `allowed_subtypes` embedding (Taxonomy §6/§7).
5. **Extension fields are preserved verbatim** as-is on their concept/scheme
   (`default_claim_basis`, `questioning_note`, `verification_weight`,
   `contextual_prior`, `requires_linked_member`, `inference_note`, `temporal_note`,
   `indicators`, `hold_triggers`, `referring_organisation_types`, …). Do **not**
   delete, rename, or promote them (Taxonomy §6/T-9; audit O-R5 = no action).
6. **`evidence.yaml` specifics:** `evidence_types` map → a scheme with concepts
   `documentary`/`physical`/`testimonial` (top-level) and the observation subtypes as
   children with `parent`; `availability_classifications` → its own scheme;
   **`claim_evidence_matrix` is removed from this file** and relocated per D3 in
   Phase 3 (leave a one-line pointer note only if helpful).
7. **`support-interventions.yaml` (placeholder):** normalize to header +
   `status: placeholder` + no `schemes:` (or empty); move the planning prose
   (`concepts_this_file_will_own`, `do_not_implement_until`) into `purpose:`.
8. **`needs.yaml` (D5):** add the local `need_severity` scheme (`critical`/`high`/
   `medium`/`low`). The `needs-assessment/taxonomy.yaml#need_severity` dependency
   is a duplicated-content case (`Repository_Migration_Methodology.md` §3): no
   `references:` entry is created and no CURIE is invented; the dependency is
   recorded only as a plain `#` comment above the scheme, pending Phase 5.
9. Cross-references stay as-is this phase (`imports:` untouched) — they are
   converted in Phase 4/5, per the same methodology §3 rule.
10. **Content-gap handling** (methodology §5/§6) applies to every scheme/concept
    listed in the Registration Content Gap Log above. Phase 2 does not write
    placeholder text or infer a `status` change for these records — see the
    Content Gap Log for the current, authoritative list and the required
    carry-over correction.

**Expected output.** Nine taxonomy files, each a header + `schemes:` list of
`id`-keyed scheme records containing `concepts:` lists with `parent`-expressed
hierarchy; no `values:` wrappers, no embedded `subtypes`, no `type: enum`. Every
record listed in the Content Gap Log has its `description` field genuinely
absent (not fabricated) until closed by content authoring; every other record
has its real, migrated description.

### Phase 2 validation checklist
- [ ] Every taxonomy file's payload root is a `schemes:` list; no root scheme-keys
      remain.
- [ ] Every scheme/concept not on the Content Gap Log has `id` + a real
      `description`; every scheme/concept on the log has no fabricated text in
      its place (methodology §5/§8).
- [ ] No `subtypes`/`allowed_subtypes` remains; all hierarchy is `parent` within one
      scheme.
- [ ] No `values:` wrapper and no `type: enum` remains anywhere.
- [ ] Concept `id`s are unchanged from the originals (no renames — frozen ids,
      Taxonomy §3).
- [ ] All extension fields still present, unmodified.
- [ ] `claim_evidence_matrix` no longer resides in `evidence.yaml`; no `references:`
      entry was created for `need_severity` (methodology §3).
- [ ] `need_severity` scheme present in `needs.yaml` with a plain-comment Phase 5
      pointer, not a `references:` entry.
- [ ] No file's `status` was changed as an inference from content completeness
      (methodology principle 1).
- [ ] The Registration Content Gap Log is empty (Content Completion Gate,
      methodology §10) — otherwise Phase 2 is not complete, regardless of how
      much structural conversion has already been done.
- [ ] YAML parses; concept counts per scheme equal the pre-migration counts
      (+ the promoted subtypes, which were already present as children, + the
      4 new `need_severity` concepts authorized by D5).

---

# PHASE 3 — Ontology Relationships + Constraints Scaffold (mechanical, gated by D1/D3)

**Objective.** Normalize `relationships.yaml` to the canonical edge shape and place the
relocated `claim_evidence_matrix`. **Mechanical/Semantic:** Mechanical (rules fixed by
D1/D3). **Preconditions:** Phase 1 done; D1 and D3 approved.
**Note:** entity-attribute cleanup (`key_attributes`/`attributes_ref` removal) is
deliberately **deferred to Phase 4** (audit correction — must follow
`data-properties.yaml` creation).

**Files affected:** `registration/ontology/relationships.yaml`;
`registration/ontology/entities.yaml` (cardinality-field normalization only);
new `registration/reasoning/evidence-rules.yaml` (D3 relocation target).

**Rules (deterministic):**
1. **Cardinality (Ontology §7):** replace every retired enum with `{min, max}`:
   `one_to_one`→`{min: 1, max: 1}`; `one_to_many`→`{min: 1, max: unbounded}`;
   `zero_to_many`→`{min: 0, max: unbounded}`; `zero_to_one`→`{min: 0, max: 1}`;
   `many_to_many`→`{min: 0, max: unbounded}` (on the `to` side; the reverse edge, if
   any, carries its own). Fold any `minimum: 1` into `min: 1`.
2. **Remove `required:` from every relationship row** (Ontology §6 — obligation is
   `min ≥ 1`). Remove `minimum:`. Move any `closure_rule:` text to a `notes:` field
   **or** to `lifecycle-constraints.yaml` (do not keep it as an edge field).
3. **D1:** delete the `case_produces_verification_brief` row.
4. Keep `relationship:` predicate names as-is (audit O-R1 = no action; generic `has`
   is conformant).
5. **Entity-presence field normalization (Ontology §1 tolerated axis, match
   `shared/`):** in `entities.yaml`, replace the ad-hoc `cardinality:` key on `case`,
   `lead`, `volunteer_review` with `cardinality_in_case:` (`one_per_registration_
   conversation`→`exactly_one`; `zero_or_one`→`zero_or_one`). Do not touch
   `key_attributes`/`attributes_ref` yet.
6. **D3:** create `registration/reasoning/evidence-rules.yaml` (standard header) and
   move the `claim_evidence_matrix` content there as a domain validation table.

**Expected output.** `relationships.yaml` rows use only `id`/`from`/`relationship`/
`to`/`cardinality{min,max}`/optional `inverse`/optional `notes`; no `required`/
`minimum`/`closure_rule`; no dangling `verification_brief`. Entities use a single
`cardinality_in_case` field. The claim-evidence matrix lives in `reasoning/`.

### Phase 3 validation checklist
- [ ] No relationship row contains a retired cardinality enum, `required:`,
      `minimum:`, or `closure_rule:`.
- [ ] Every relationship `cardinality` is `{min, max}` with valid values.
- [ ] The `verification_brief` row is gone; no relationship `to:` targets a
      non-entity.
- [ ] Every `to:`/`from:` names an `id` present in `entities.yaml`.
- [ ] `entities.yaml` uses `cardinality_in_case` uniformly; no bare `cardinality:`
      remains.
- [ ] `key_attributes`/`attributes_ref` are **still present** (removed in Phase 4).
- [ ] `reasoning/evidence-rules.yaml` exists and contains the full matrix;
      `evidence.yaml` no longer does.

---

# PHASE 4 — Attribute Decomposition (mechanical + gated semantic, largest phase)

**Objective.** Drain `attributes.yaml` into the canonical surfaces and delete it; wire
same-domain `taxonomy_ref`; finish entity cleanup. **Mechanical/Semantic:** Mechanical
**after** D6/N-R1 are settled (Phase 0 + the N-R1 reconciliation step below).
**Preconditions:** Phases 1–3 done; D6 approved; N-R1 reconciliation complete.

**Files affected:** new `registration/ontology/data-properties.yaml` (fill);
`registration/ontology/semantic-constraints.yaml` (fill);
`registration/ontology/relationships.yaml` (add D6 sub-entity relationships);
`registration/ontology/entities.yaml` (add D6 sub-entities; remove
`key_attributes`/`attributes_ref`); delete `registration/ontology/attributes.yaml`.

**Step 4.0 — N-R1 reconciliation (gate).** An application of
`Repository_Migration_Methodology.md` §8's "verify before drop" validation
requirement: for every `gap_type`/`gap_condition` in `attributes.yaml`, confirm
the same detection exists in `reasoning/gap-detection-rules.yaml`. Produce a
diff list. Conditions already covered → **drop** during decomposition.
Conditions owned **only** by `attributes.yaml` → move to
`gap-detection-rules.yaml` first. Do not proceed until the diff is empty.

**Rules (deterministic):**
1. **Scalar properties → `data-properties.yaml`** (Ontology §5) as a
   `data_properties:` list keyed by `id`. Each row: `id`, `domain` (owning entity id),
   `cardinality {min, max}`, and exactly one of `datatype`/`taxonomy_ref`.
2. **Datatype mapping (Ontology §5):** `type: string`→`xsd:string`;
   `integer`→`xsd:integer`; `boolean`→`xsd:boolean`; `date`→`xsd:date`;
   `datetime`→`xsd:dateTime`; `number`→`xsd:decimal`; `float`→`xsd:float`.
   `type: enum` → **no `datatype`**; instead `taxonomy_ref` (rule 4).
3. **Cardinality mapping:** `required: true`→`{min: 1, max: 1}`;
   `required: false`→`{min: 0, max: 1}`; `type: list`→`{min: 0..1, max: unbounded}`
   (use `minimum:` if present for `min`); `required: conditional` →`{min: 0, max: 1}`
   **plus** a `required_if` constraint (rule 5).
4. **`taxonomy_ref` (same-domain only, unblocked):** every `values_ref:` pointing at
   `registration/taxonomy/*` becomes `taxonomy_ref: <bare scheme id>` (Taxonomy §3 —
   same-domain refs use the bare scheme id). **Drop the inline `values:` list** after
   confirming it equals the scheme's concept ids (C-R5 equality check; verified matches
   include `need_category`, `case.status`, `gender`). **Cross-domain** `values_ref:`
   (`shared/*`, `needs-assessment/*`) are **left as a TODO marker** for Phase 5 — do
   not invent a CURIE.
5. **Constraints → `semantic-constraints.yaml`** (Ontology §9) as target-neutral rows
   (`id`/`type`/`property`/`entities`/`parameters`). Map: `required_when: X` →
   `type: required_if`; `validation: expr` → `type: cardinality`/domain rule as the
   closed vocab allows; `derivation:` and `coherence_rule:` → if expressible in the
   closed §9 type set, add a row; otherwise move to `reasoning/` (do not invent a new
   constraint `type` — the vocab is closed).
6. **Gap logic** (`gap_type`, `gap_condition`) → **dropped** (owned by
   `reasoning/gap-detection-rules.yaml` per Step 4.0). Prose `notes:` → drop or fold
   into the property's `label`/an adjacent reasoning file; do not carry free-text
   guidance into `data-properties.yaml`.
7. **D6 nested objects:** for each mapping-table row, add the new entity to
   `entities.yaml`, add its scalar fields as `data-properties` (rules 1–5), and add the
   owner→entity relationship to `relationships.yaml` with the stated cardinality.
8. **Entity cleanup (R-R2, now unblocked):** remove `key_attributes:` and
   `attributes_ref:` from every entity in `entities.yaml` (ownership now lives in
   `data-properties.yaml` via each property's `domain`).
9. **Delete `attributes.yaml`** once every field above has a confirmed destination.

**Expected output.** `attributes.yaml` gone; `data-properties.yaml` holds every scalar
property with `xsd`/`taxonomy_ref` + `{min,max}`; `semantic-constraints.yaml` holds the
relocated constraints; D6 sub-entities + relationships exist; entities carry no
`key_attributes`/`attributes_ref`. Cross-domain refs bear explicit Phase-5 TODO
markers.

### Phase 4 validation checklist
- [ ] Step 4.0 diff is empty (no gap condition lost).
- [ ] `attributes.yaml` no longer exists.
- [ ] Every `data_properties` row has `id`, `domain`, `{min,max}`, and exactly one of
      `datatype`(an `xsd:*` token)/`taxonomy_ref`.
- [ ] No inline `values:` remains where a `taxonomy_ref`/`values_ref` exists;
      every dropped inline list was confirmed equal to its scheme.
- [ ] Same-domain `taxonomy_ref` uses bare scheme ids that exist in
      `registration/taxonomy/*`.
- [ ] Cross-domain refs carry a Phase-5 TODO marker (not a fabricated CURIE).
- [ ] Every constraint row uses a closed §9 `type`; none is hand-authored OWL/SHACL.
- [ ] All D6 sub-entities exist with their data-properties and owner relationships.
- [ ] No entity retains `key_attributes`/`attributes_ref`.
- [ ] Every `data_properties.domain` names a real entity id; every `taxonomy_ref`
      names a real scheme id.

---

# PHASE 5 — Cross-domain CURIE Layer (BLOCKED — external dependencies)

**Objective.** Convert cross-domain references to manifest-resolved CURIEs and finalize
cross-domain ownership links. **Mechanical/Semantic:** Mechanical (once unblocked).
**Preconditions (all external to registration):**
- Repository manifest / catalog exists (Finding **R-1**).
- Literal base IRI + per-domain prefixes ratified (Finding **C-2**).
- Cross-domain targets are canonical: `shared/human-model/taxonomy/capabilities.yaml`
  and `needs-assessment/taxonomy.yaml` are **currently legacy-shaped** and must expose
  a resolvable scheme id before a conformant CURIE can point at them.

**Files affected:** `registration/ontology/data-properties.yaml` (cross-domain
`taxonomy_ref` TODO markers); `registration/taxonomy/{actors,evidence}.yaml`
(`imports:`→`references:` for cross-domain); `registration/taxonomy/needs.yaml`
(D5 reconciliation link once needs-assessment migrates).

**Rules (deterministic, when unblocked):**
1. Replace each Phase-4 cross-domain TODO with `taxonomy_ref: <prefix>:<scheme_id>`
   using the manifest prefix (Ontology §10 / Taxonomy §3, §8).
2. Convert taxonomy `imports:` file paths to `references:` records with
   `scheme`/`relation`/`note` (Taxonomy §8); D4's actors→persons `extends` link is
   finalized here.
3. Confirm the cross-domain dependency graph stays acyclic (Ontology §10).

**Expected output.** No file-path reference remains anywhere in registration; all
cross-domain references are manifest CURIEs.

### Phase 5 validation checklist
- [ ] No `values_ref:`, `imports:`, or `ref:` file-path reference remains.
- [ ] Every cross-domain `taxonomy_ref`/`references.scheme` is a CURIE registered in
      the manifest.
- [ ] The actors→persons (D4) and needs↔needs-assessment (D5) links resolve.
- [ ] Cross-domain reference graph is acyclic.

---

# PHASE 6 — Optional Polish (no-action set)

**Objective.** Record the audit's optional items that are **explicitly not executed**
during migration, so Sonnet does not touch them. **Mechanical/Semantic:** N/A.

- **No action:** O-R1 (generic `has` is conformant), O-R5 (list-valued extension
  fields are conformant), O-R7 (documented denormalization), entity `notes:`
  (tolerated). Touching these is scope creep.
- **Optional, only if separately requested:** O-R2 (`inverse:` declarations), O-R4
  (dedupe `contact_gap`/`location_gap` descriptions — content edit, needs owner
  sign-off), O-R3 (`gaps/` folder placement — a governance decision, not migration).
- **Out of scope entirely:** artifact generation (F-3), localization (Taxonomy §11),
  `owl_version_iri` policy (R-3).

---

# Success Criteria

Registration is **fully canonical** when all hold:
1. `registration/ontology/` contains exactly the five canonical files; no
   `attributes.yaml`.
2. `entities.yaml`: list of `id`-keyed classes; hierarchy via `parent` only; no
   `key_attributes`/`attributes_ref`/`subtypes`; entity-presence via
   `cardinality_in_case`.
3. `data-properties.yaml`: property-centric list; each row has `domain`, one of
   `datatype`(xsd)/`taxonomy_ref`, `{min,max}`.
4. `relationships.yaml`: reusable-predicate edges with `{min,max}`; no `required`; no
   dangling targets.
5. `semantic-constraints.yaml`: only closed-vocab target-neutral rows.
6. All 9 taxonomy files: `schemes:`→`concepts:` lists; hierarchy via `parent`; no
   `values:`/`type: enum`/embedded subtypes; canonical four-key header.
7. All references are either bare same-domain ids or manifest CURIEs — **zero file
   paths**.
8. Every governed file passes its phase validation checklist; no concept/entity/
   scheme `id` was renamed (frozen-id rule, §3).
9. The domain generates on a single code path (the conformance summaries of both
   contracts hold).

# Exit Criteria (per phase — when to stop and hand back)

- **Phase 0:** stop until the Decision Table is fully approved.
- **Phases 1–4:** a phase exits when **every** checklist item passes and YAML parses;
  a failing item halts that phase (do not proceed) and returns to review.
- **Phase 4:** exits registration to **"canonical up to the CURIE boundary."** This is
  the last unblocked phase — the correct stopping point until Phase 5's external
  dependencies land.
- **Phase 5:** exits only when the manifest, C-2, and the two cross-domain target
  migrations are all present; otherwise it remains parked with TODO markers in place
  (a valid, expected end-state).

# Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Wrong D6 granularity** → entity-graph rework | Med | High | Isolate D6 in Phase 0; conservative sub-entity default; Phase 4 is reversible per-entity. |
| **C-5 blind de-dup** where inline `values:` ≠ scheme → silent data loss | Med | High | Rule 4 equality check is mandatory before any drop; unverified/cross-domain refs excluded. |
| **N-R1 gap loss** dropping a `gap_condition` owned only by attributes | Med | Med | Step 4.0 diff gate; move-before-drop. |
| **Premature CURIE minting** in Phase 4 hard-codes values C-2 may change | Low | Med | Phase 4 leaves explicit TODO markers; CURIEs only in Phase 5. |
| **Cross-domain target still legacy** (capabilities/needs-assessment) | High | Low | Phase 5 precondition; registration parks with TODOs — does not block Phases 1–4. |
| **Downstream ancillary files** (`reasoning/`, `readiness/`, `questioning/`, `verification/`) reference moved names | Low | Low | They reference by concept name, not file path (verified); names are frozen and unchanged. Spot-check after Phase 2/4. |
| **Scope creep** into O-R1/O-R5/content edits | Med | Low | Phase 6 explicit no-action list; Sonnet makes no architectural decisions. |

# Rollback Considerations

- **Commit granularity:** one commit per phase (or per file within Phase 2/4), never
  mixing mechanical and semantic changes — so any phase reverts cleanly.
- **`attributes.yaml` is deleted only in Phase 4 step 9**, after every field has a
  confirmed destination; until then it remains the intact source of truth, so Phases
  1–3 are fully reversible without data risk.
- **Frozen-id invariant** means no rename ever occurs; a rollback never has to
  reconstruct changed identifiers.
- **Phase 5 is additive** (path→CURIE substitution over TODO markers); reverting it
  restores the Phase-4 parked state, which is itself valid.
- Keep the pre-migration `registration/` tree tagged; each phase diff is reviewable
  against it.

# Deterministic Checklist for Sonnet (no architectural decisions)

> Execute top to bottom. Do not start a line whose preconditions are unmet. If any
> validation fails, stop and hand back.

```
[ ] 0.  Confirm Decision Table D1–D6 is approved and pasted in. Else STOP.
[ ] 1a. Rewrite headers of entities.yaml, relationships.yaml, all 9 taxonomy files
        to {version:"x.y.0", domain:registration, file:<repo-relative>, status}.
[ ] 1b. Create data-properties.yaml, semantic-constraints.yaml,
        lifecycle-constraints.yaml as canonical placeholders.
[ ] 1c. Run Phase 1 checklist. All pass? Else STOP.
[ ] 2a. Convert each taxonomy file to schemes:->concepts: lists; scheme id = old key.
[ ] 2b. Drop values: wrappers; move embedded subtypes to same-scheme parent (D2).
[ ] 2c. evidence.yaml: schemes for evidence_types + availability; REMOVE
        claim_evidence_matrix (held for Phase 3). needs.yaml: add need_severity (D5).
        support-interventions.yaml: placeholder normalize.
[ ] 2d. Preserve all extension fields and all concept ids verbatim.
[ ] 2e. Run Phase 2 checklist. All pass? Else STOP.
[ ] 3a. relationships.yaml: enum->{min,max}; drop required/minimum/closure_rule.
[ ] 3b. Delete case_produces_verification_brief row (D1).
[ ] 3c. entities.yaml: bare cardinality: -> cardinality_in_case (case/lead/review).
[ ] 3d. Create reasoning/evidence-rules.yaml; move claim_evidence_matrix there (D3).
[ ] 3e. Run Phase 3 checklist. All pass? Else STOP.
[ ] 4.0 Build gap_condition diff (attributes.yaml vs gap-detection-rules.yaml).
        Move attributes-only conditions into gap-detection-rules.yaml. Diff empty?
        Else STOP.
[ ] 4a. Scalar attrs -> data-properties.yaml (xsd datatypes; {min,max}).
[ ] 4b. Same-domain values_ref -> taxonomy_ref bare id; drop inline values: after
        equality check. Cross-domain refs -> Phase-5 TODO marker.
[ ] 4c. required_when/validation/derivation -> semantic-constraints.yaml (closed
        §9 types only). Drop gap_type/gap_condition/notes.
[ ] 4d. D6: add sub-entities + their data-properties + owner relationships.
[ ] 4e. Remove key_attributes/attributes_ref from all entities.
[ ] 4f. Delete attributes.yaml.
[ ] 4g. Run Phase 4 checklist. All pass? -> registration is canonical to the CURIE
        boundary. STOP here until Phase 5 unblocks.
[ ] 5.  (Blocked) Only when manifest + C-2 + cross-domain targets ready: convert
        TODO markers and imports: to CURIE references; run Phase 5 checklist.
[ ] 6.  No action on O-R1/O-R5/O-R7/notes. Optional items only on explicit request.
```

*End of plan. No repository files were modified in producing it. Awaiting approval of
the Phase 0 Decision Table before any execution.*
