# Community Context Domain — Migration Implementation Plan

> **Audience:** the executing agent. **Status:** Phase 0 decisions recorded and
> approved below (defaults accepted per `Repository_Migration_Methodology.md`'s
> "mechanical by default" principle — none override a frozen contract rule).
> Phases 1–3 executed in an earlier pass. **Phase 4 executed in this pass**: 17 of
> 18 Content Gap Log rows closed mechanically (Decision D-CC6); 1 row
> (`transportation_network_asset.surface_condition`) remains genuinely open — no
> taxonomy scheme exists to wire it to, and inventing one is content authoring,
> not migration. Phase 5 externally blocked, as for every domain.
>
> **Authorities:** `Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`
> (frozen structural contracts) and `Repository_Migration_Methodology.md` (frozen
> process contract). This plan states only what is specific to Community Context.
> **Companion:** `Community_Context_Domain_Audit.md` (findings).

---

## Business Validation (Phase 2 of the assigned task)

Cross-checked `community-context/` against
`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, the humanitarian operating flow it
describes, and `community_context_discovery_report.md`:

- **Settlements, geography, accessibility, infrastructure, hazards, seasonal
  events, services, livelihoods, organisations** — all present with a full
  taxonomy file and a clear single-ownership boundary
  (`community-context-governance.md` C1–C4). **Classification: Already covered.**
- **Community assets** — present (`community-assets.yaml`, scoped to natural
  resources after the C1 remediation moved built assets to
  `infrastructure-types.yaml`). **Already covered.**
- **Geographic hierarchy vs. `shared/taxonomy/locations.yaml`** — checked for
  duplication risk (the roadmap's Stage 8 prerequisite says locations.yaml "must be
  extended with geographic hierarchy"). No duplication found:
  `shared/taxonomy/locations.yaml` explicitly defers this content ("Future domains
  will extend this file... Do not add those here until those domains are active")
  and `community-context/taxonomy/geographic-hierarchy.yaml` is exactly that
  extension, correctly owned in the new domain rather than bloating `shared/`.
  **Already covered — no action needed; the roadmap note is now historical.**
- **Population & demographics, market integration, governance & institutions,
  social cohesion/exclusion, culture, safety & security, public health** — all
  explicitly deferred in `_placeholder.yaml` and the domain's own `README.md`
  ("Does Not Own"), pending Volunteer Operations / Support Delivery activation.
  **Classification: Future domain** (a deliberate, already-documented deferral —
  not a gap this migration should close; authoring this content now would be
  scope creep beyond "make Community Context canonical," which is a structural,
  not content-expansion, objective).
- **Missing concepts:** none found beyond the above deferred set.
- **Duplicated concepts:** none found between Community Context and any other
  domain's governed files (checked against `shared/taxonomy/organisations.yaml`,
  `shared/taxonomy/locations.yaml`, `shared/risk/taxonomy/hazard-categories.yaml`,
  `shared/human-model/taxonomy/health-conditions.yaml` — all four are referenced
  correctly, never redefined).
- **Misplaced ownership:** none — `community-context-governance.md`'s C1–C4
  boundary rules already resolved every internal boundary question (transportation
  vs. infrastructure vs. natural assets; accessibility vs. physical environment;
  geographic hierarchy vs. settlement formality; local vs. shared organisations).
- **Missing reasoning / missing taxonomy / missing ontology:** the domain has no
  `reasoning/` module at all (unlike Registration). This is **not** a structural
  defect — Ontology §13's template lists `reasoning/` as present "where the domain
  has rules to state," and `community_context_discovery_report.md` §16 names five
  candidate reasoning modules (seasonal-risk-inference, service-accessibility-rules,
  economic-shock-inference, volunteer-safety-rules, aggregate-vulnerability-rules)
  that are explicitly **candidates for a later stage**, consumed by Case
  Management / Volunteer Operations once those domains activate. **Classification:
  Future domain** — correctly out of scope for a structural migration.
- **Architectural decision required:** the `semantic-constraints.yaml` type
  disposition questions in the audit's CC-7 table (D-CC1–D-CC3 below).

**Conclusion:** Community Context requires **no new business concepts** and **no
ontology ownership changes** to reach canonical structural maturity. Every
finding in the audit is either mechanical re-serialization or one of the three
narrow disposition decisions below — exactly the profile the assigned task
authorizes for immediate implementation.

---

## Content Gap Log

> **Updated at Phase 4 completion.** Re-examined against
> `Repository_Migration_Methodology.md` §2: the `key_attributes` comments on each
> entity in `entities.yaml` (e.g. `settlement_form # from taxonomy/settlement-types.yaml`)
> are themselves "an adjacent comment that describes only that one record and no
> other" — exactly the kind of already-present authoritative content §2 recognizes
> as mechanically recoverable. Combined with the fact that every named taxonomy
> file already exists with real, populated schemes (Phase 2), 17 of the original
> 18 rows were mechanically wireable without inventing any new taxonomy concept or
> humanitarian content — see Decision D-CC6 below and the authored
> `ontology/data-properties.yaml`. **17 rows CLOSED. 1 row remains OPEN.**

| Status | Entity | Property (from `key_attributes`) | Resolution |
|---|---|---|---|
| CLOSED | `community` | `community_id` | `xsd:string`, mechanical |
| CLOSED | `community` | `livelihood_pattern` | decomposed into 4 sibling `taxonomy_ref` properties (D-CC6a) |
| CLOSED | `community` | `settlement_form` | `taxonomy_ref: settlement_formality` |
| CLOSED | `community` | `seasonal_events` | decomposed into 4 sibling `taxonomy_ref` properties (D-CC6a) |
| CLOSED | `geographic_area` | `area_id` | `xsd:string`, mechanical |
| CLOSED | `geographic_area` | `geographic_level` | `taxonomy_ref: geographic_level` |
| CLOSED | `geographic_area` | `physical_environment` | decomposed into 5 sibling `taxonomy_ref` properties (D-CC6a) |
| CLOSED | `geographic_area` | `physical_accessibility` | `taxonomy_ref: physical_accessibility` |
| CLOSED | `geographic_area` | `hazards` | decomposed into 4 sibling `taxonomy_ref` properties (D-CC6a) |
| CLOSED | `built_infrastructure` | `infrastructure_id` | `xsd:string`, mechanical |
| CLOSED | `built_infrastructure` | `infrastructure_type` | `taxonomy_ref: infrastructure_type` |
| CLOSED | `built_infrastructure` | `essential_service` | decomposed into 7 sibling `taxonomy_ref` properties (D-CC6a) |
| CLOSED | `natural_resource` | `resource_id` | `xsd:string`, mechanical |
| CLOSED | `natural_resource` | `resource_type` | `taxonomy_ref: natural_resources` |
| CLOSED | `transportation_network_asset` | `asset_id` | `xsd:string`, mechanical |
| CLOSED | `transportation_network_asset` | `asset_type` | decomposed into 5 sibling `taxonomy_ref` properties, mutually exclusive (D-CC6b) |
| **OPEN** | `transportation_network_asset` | `surface_condition` | **Genuine content gap.** No scheme anywhere in `taxonomy/transportation.yaml` (or elsewhere in this domain) enumerates surface-condition concept values (e.g. "passable"/"degraded"/"washed_out"). Every other row above had an existing scheme to wire to; this one does not — inventing the concept values themselves would be content authoring, not mechanical inference. **A domain-knowledgeable author must add a `surface_condition` (or similarly named) scheme to `taxonomy/transportation.yaml` with real concept values before this property can be authored.** |
| CLOSED | `local_collective` | `collective_id` | `xsd:string`, mechanical |
| CLOSED | `local_collective` | `collective_type` | decomposed into 4 sibling `taxonomy_ref` properties, mutually exclusive (D-CC6b) |

**Phase 4 is not fully closed while the one OPEN row above remains** (methodology
§10, Content Completion Gate) — but it no longer blocks the rest of the domain,
since every other property is now authored and every relationship/constraint file
is complete. This is a single, narrow, precisely-scoped remaining gap, not a
structural blocker.

---

# PHASE 0 — Review Decisions (no file changes)

### Decision Table

| ID | Decision | Contract basis | Recommended default | Approved value |
|----|----------|----------------|---------------------|----------------|
| **D-CC1** | Disposition of `infrastructure_organization_reference` (`cross_domain_boundary`, `ObjectAllValuesFrom`). | Ontology §9 closed type vocabulary; the relationship row `built_infrastructure_operated_by_organization`'s `to: shared_org:organisation` already fixes the range. | **Drop the row** — redundant with the relationship schema's own `to:` field; no information lost. | ☑ Approved (default) |
| **D-CC2** | Disposition of `collective_human_reference` (`cross_domain_boundary`, "no cascading deletes") and `no_operational_workflows` (`domain_encapsulation`). | Ontology §9 (constraints are structural graph facts, not governance prose); `lifecycle-constraints.yaml` is explicitly "not a generation surface" (Ontology §9) and `community-context-governance.md` already states equivalent boundary rules for the taxonomy layer. | **Relocate** `collective_human_reference` into `lifecycle-constraints.yaml` (on `local_collective`); **relocate** `no_operational_workflows` into `community-context-governance.md` as a new "Ontology Boundary Rules" section extending the document's existing pattern. | ☑ Approved (default) |
| **D-CC3** | `property` field value for the one `type: disjoint` row (`built_vs_natural`), and disposition of `geographic_area_anti_recursion` (no closed-vocabulary `type` fits irreflexivity/asymmetry). | Ontology §9 (`property` required for every constraint row; type vocabulary closed). | For `built_vs_natural`: keep `type: disjoint`, set `property: rdf:type` (the only property every individual's class membership is asserted through — mirrors OWL's own `DisjointClasses` axiom needing no bound property). For `geographic_area_anti_recursion`: **do not invent a new constraint type.** Retain as a `notes:` field on the `geographic_area_contains_*`/`community_located_in_geographic_area` relationship rows (tolerated non-generation-affecting annotation, per the precedent already set for entity-level `notes:` in Registration's audit). | ☑ Approved (default) |
| **D-CC4** | Hierarchy handling for taxonomy files with no embedded `subtypes` (unlike Registration, none of Community Context's 12 taxonomy files nest child concepts — `infrastructure-types.yaml`'s `category:` field on `infrastructure_type` concepts is a cross-scheme tag, not embedded hierarchy). | Taxonomy §7. | **No `parent` conversion needed anywhere in this domain.** `infrastructure_type[*].category` values reference the sibling `infrastructure_category` scheme's concept ids by convention, not by containment — preserved verbatim as a domain extension field (Taxonomy §6, "extension fields... not part of the core contract"), same treatment as Registration's `default_claim_basis`. | ☑ Approved (default) |
| **D-CC5** | Ownership of the `namespaces:` cross-domain targets (`shared_org`, `shared_human`). | Taxonomy §9 / ADR-008; both targets are already-canonical shared files. | **No action needed.** Unlike Registration's D4/D5 (which had to resolve overlap with an un-migrated or ambiguous target), Community Context's two cross-domain targets are already single-owned and already correctly referenced, never redefined. | ☑ Approved (default) |
| **D-CC6** *(added at Phase 4)* | How a single `key_attributes` comment naming a taxonomy *file* with more than one independent scheme becomes one or more `data-properties.yaml` rows, given Ontology §5's "exactly one of `datatype`/`taxonomy_ref`" rule (a property cannot point at several schemes at once). | Ontology §5, §17 (Value Objects — considered and rejected here, see below); `Repository_Migration_Methodology.md` §2 (the `key_attributes` comment is already-present authoritative content naming the source file). | **One data property per scheme** (D-CC6a for cumulative dimensions, cardinality `{min:0,max:unbounded}`; D-CC6b for mutually-exclusive alternatives, cardinality `{min:0,max:1}` each **plus** a `mutually_exclusive` semantic-constraints.yaml row — the closed §9 vocabulary already has this type, so no new constraint type is invented). A Value Object (§17) was considered for the mutually-exclusive case (`asset_type`, `collective_type`) and rejected: §17's promotion test asks whether the group is "created, updated, and removed exactly when its owning entity is" — true here — but a Value Object bundles *co-occurring* fields under one row, whereas these are *alternative* single-value classifications; forcing them into one `fields:` row would still need an internal exclusivity rule with no clean place to state it under §17, whereas `mutually_exclusive` in §9 states it directly and is the vocabulary already designed for exactly this fact. | ☑ Approved (default) |

### Phase 0 validation checklist
- [x] Every decision D-CC1–D-CC5 has an approved value (default, no overrides needed).
- [x] Every override reconciled against its citing contract section — none violate a frozen rule.
- [x] Decision Table pasted into this plan.
- [x] No repository file modified during Phase 0.

---

# PHASE 1 — Headers & File Set (mechanical)

**Objective.** Canonical four-key header on every governed file; create the missing
`data-properties.yaml` placeholder.
**Files affected:** `community-context/ontology/{entities,relationships,semantic-constraints,lifecycle-constraints}.yaml`
(header only); `community-context/taxonomy/*.yaml` (all 12, header only); new
`community-context/ontology/data-properties.yaml`.

**Rules:**
1. Header = exactly four top-level keys, in order: `version`, `domain`, `file`, `status`.
2. `version: "1.0.0"` for every file currently at `1.0`/`1.0.0`/`1.0.1` (promote
   unquoted/two-part to quoted three-part; `infrastructure-types.yaml`'s existing
   `1.0.1` is preserved as `"1.0.1"`, not reset).
3. `domain: community_context` (unchanged; already the correct snake_case token
   everywhere except nothing needs fixing here — the domain's existing `domain:`
   values are already conformant snake_case, unlike Registration's Title-Case peers).
4. `file:` = repo-relative path, e.g. `community-context/taxonomy/accessibility.yaml`.
5. `status: active` for every populated file; `status: placeholder` for the new
   `data-properties.yaml`.
6. `settlement-types.yaml` additionally gets the header it currently lacks entirely.
7. `data-properties.yaml` is created as: header + `data_properties: []` +
   a one-line note pointing at the Content Gap Log above.
8. Comment-banner prose (the `# ====` blocks, `Purpose:`/`Scope:`/`ADR Validation:`
   sections) is preserved **below** the new YAML header, not deleted — it is
   legitimate authorial documentation, just no longer doing double duty as the
   header.

### Phase 1 validation checklist
- [ ] Every governed file's first four keys are `version`/`domain`/`file`/`status`.
- [ ] Every `version` is a quoted three-part string.
- [ ] Every `status` ∈ {`active`, `placeholder`}.
- [ ] Every `file:` equals the true repo-relative path.
- [ ] `community-context/ontology/` lists exactly the five canonical files.
- [ ] No payload content changed in this phase (headers only).

---

# PHASE 2 — Taxonomy Re-serialization (mechanical, gated by D-CC4)

**Objective.** Convert all 12 taxonomy files to `schemes:` → `concepts:` lists.
**Files affected:** all `community-context/taxonomy/*.yaml`.

**Rules:**
1. Each `concepts: { <scheme_key>: {...} }` map entry becomes a `schemes:` list
   item with `id: <scheme_key>`.
2. Drop the `values:` wrapper — members move directly under `concepts:`.
3. Drop `type: enum` (dead metadata, Taxonomy §5).
4. Each concept: `id`, `description` (from the existing `description`), `label`
   (from the existing `label`, where present).
5. Extension fields preserved verbatim: `infrastructure_type[*].category` (cross-scheme
   tag, D-CC4).
6. **`settlement-types.yaml` specifics:** each `- key: "prose"` list item becomes
   `{id: key, description: "prose"}` — no `label` is fabricated (none existed).
7. **`geographic-hierarchy.yaml` specifics:** the `alignment_notes` prose citing
   `shared/taxonomy/locations.yaml` becomes a `references:` entry
   (`scheme: shared_locations:location_precision` is premature — cross-domain CURIE
   waits on the manifest; use the bare descriptive form permitted pre-Phase-5:
   record it as a plain comment, mirroring Registration's D5 treatment of
   `need_severity`, since no manifest prefix exists yet to mint a real CURIE).
8. `alignment_notes` blocks (all 12 files) are preserved verbatim at the file's end
   — they are domain documentation, not `schemes:`/`concepts:` payload, and the
   taxonomy contract does not forbid a trailing informational block.

### Phase 2 validation checklist
- [ ] Every taxonomy file's payload root is a `schemes:` list.
- [ ] Every scheme has `id` + real `description`; every concept has `id` +
      real `description`.
- [ ] No `values:` wrapper, no `type: enum` remains anywhere.
- [ ] Concept/scheme ids unchanged from originals (frozen-id rule).
- [ ] All extension fields (`category` on infrastructure types) preserved.
- [ ] `settlement-types.yaml` now has a full four-key header and `schemes:` shape.
- [ ] Concept counts per scheme equal pre-migration counts exactly.

---

# PHASE 3 — Ontology Relationships, Entities & Constraints (mechanical, gated by D-CC1–D-CC3)

**Objective.** Normalize `relationships.yaml` cardinality/fields, clean `entities.yaml`,
re-serialize `semantic-constraints.yaml` per the Phase-0 dispositions.
**Files affected:** `relationships.yaml`, `entities.yaml`, `semantic-constraints.yaml`,
`lifecycle-constraints.yaml`, `community-context-governance.md`.

**Rules:**
1. **Cardinality (Ontology §7):** `one_to_one`→`{min:1,max:1}`;
   `one_to_many`→`{min:1,max:unbounded}`; `many_to_one`→`{min:0,max:1}` on the `to`
   side per one `from` instance — wait, `many_to_one` reads as "many `from` map to
   one `to`", so per one `from` instance the `to` cardinality is `{min:1,max:1}`;
   verified against each row's actual semantics rather than applied as a blind
   string substitution. `many_to_many`→`{min:0,max:unbounded}`.
2. **Remove `required:` from every relationship row** (obligation is `min ≥ 1`,
   already captured by rule 1's mapping).
3. **D-CC3:** add a `notes:` field to `community_located_in_geographic_area` and
   `geographic_area_contains_community` (and the built-infrastructure/natural-resource/
   transportation `contains` rows) recording the anti-recursion/asymmetry intent
   from the dropped `geographic_area_anti_recursion` constraint.
4. **`entities.yaml`:** remove `key_attributes` (ownership now belongs to
   `data-properties.yaml` via `domain:`, once Phase 4 populates it) and
   `attributes_ref` (deleted concept); remove `external_references` (CC-3 —
   redundant with `relationships.yaml`). Keep `required:` (a permitted §4 field,
   not the ad-hoc `cardinality:` problem Registration had).
5. **`semantic-constraints.yaml`:** re-serialize per the CC-7 table:
   - `community_requires_geography`, `collective_requires_community` →
     `type: cardinality` rows, mechanical.
   - `built_vs_natural` → `type: disjoint`, `property: rdf:type` (D-CC3).
   - `infrastructure_organization_reference` → dropped (D-CC1).
   - `collective_human_reference` → moved to `lifecycle-constraints.yaml` (D-CC2).
   - `no_operational_workflows` → moved to `community-context-governance.md` (D-CC2).
   - `geographic_area_anti_recursion` → dropped from this file, becomes relationship
     `notes:` (D-CC3, rule 3 above).

### Phase 3 validation checklist
- [ ] No relationship row contains a retired cardinality enum or `required:`.
- [ ] Every relationship `cardinality` is `{min,max}`, individually verified against
      the row's stated semantics (not a blind enum substitution).
- [ ] `entities.yaml` has no `key_attributes`/`attributes_ref`/`external_references`.
- [ ] `semantic-constraints.yaml` contains exactly 3 rows (`community_requires_geography`,
      `collective_requires_community`, `built_vs_natural`), each in the
      `id`/`type`/`property`/`entities`/`parameters` shape.
- [ ] `lifecycle-constraints.yaml` gained the relocated `collective_human_reference`
      note on `local_collective`.
- [ ] `community-context-governance.md` gained the relocated
      `no_operational_workflows` boundary rule.
- [ ] `geographic_area`-adjacent relationship rows carry the anti-recursion `notes:`.
- [ ] Every `to:`/`from:` in `relationships.yaml` names a real `entities.yaml` id or
      a declared `namespaces:` prefix.

---

# PHASE 4 — Attribute Authoring (mechanical portion executed; 1 row genuinely blocked)

**Objective.** Populate `data-properties.yaml` with every scalar/coded property
implied by the (removed) `key_attributes` comments.
**Status: executed.** Re-examination under `Repository_Migration_Methodology.md`
§2 (see Content Gap Log above) found that 17 of the original 18 rows were
mechanically wireable — the property name and its source taxonomy file were
already present as an adjacent comment on the owning entity (§2's own recognized
form of already-present authoritative content), and every named taxonomy file
already has real, populated schemes from Phase 2. These 17 rows are now authored
in `ontology/data-properties.yaml` per Decision D-CC6 (decomposition rule) above,
with two new `mutually_exclusive` rows added to `semantic-constraints.yaml` for
the two mutually-exclusive decompositions (`asset_type`, `collective_type`).

**The one genuinely blocked row** (`transportation_network_asset.surface_condition`)
is **not** authored by migration: unlike every other property, no taxonomy scheme
anywhere in this domain enumerates surface-condition values, so closing it means
inventing new taxonomy concepts — a domain-knowledgeable author's job (methodology
§7), not a migration's. It remains in the Content Gap Log until a human adds the
scheme to `taxonomy/transportation.yaml`.

---

# PHASE 5 — Cross-domain CURIE Layer (BLOCKED — external dependencies, same as every domain)

**Preconditions:** repository manifest (R-1), ratified base IRI/prefixes (C-2).
Unlike Registration, Community Context has **no un-migrated cross-domain target** —
both `shared/taxonomy/organisations.yaml` and `shared/human-model/` are already
canonical, so Phase 5 here is a pure mechanical CURIE substitution once C-2/R-1
land, with zero additional target-domain blockers.

---

# Success Criteria

Community Context is **structurally canonical up to the CURIE boundary** when:
1. `community-context/ontology/` contains exactly the five canonical files.
2. `entities.yaml`: no `key_attributes`/`attributes_ref`/`external_references`.
3. `relationships.yaml`: `{min,max}` cardinality, no `required:`.
4. `semantic-constraints.yaml`: 3 rows, all closed-vocab target-neutral shape.
5. `lifecycle-constraints.yaml`: gained the one relocated constraint.
6. All 12 taxonomy files: `schemes:`→`concepts:` lists, four-key headers.
7. Every file passes its phase's validation checklist.
8. No concept/entity/scheme `id` was renamed.

**Fully canonical** (content-complete) additionally requires the Content Gap Log's
one remaining row (Phase 4) to be closed by a domain-knowledgeable author —
outside this migration's authority per methodology §7. With 17 of 18 rows closed,
Community Context is now **Canonical (Content Pending)** — see
`Community_Context_Domain_Audit.md` for the full classification rationale.

# Exit Criteria

- **Phase 0:** stop until Decision Table approved (done, above).
- **Phases 1–3:** exit when every checklist item passes and YAML parses (done).
- **Phase 4:** exits when the Content Gap Log is empty. **Currently 17/18 closed**;
  the remaining row is genuinely blocked on human taxonomy authoring, not a
  migration task — this is the correct, expected stopping point.
- **Phase 5:** exits only when manifest + C-2 land.

*End of plan.*
