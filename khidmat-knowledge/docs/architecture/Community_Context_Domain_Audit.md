# Community Context Domain — Architectural Conformance Audit

> **Status:** ORIGINALLY AUDIT ONLY — no file was modified at the time this report
> was first written. The findings below are recorded as originally found, and the
> subsequent `Community_Context_Migration_Plan.md` has since executed Phases 1–4
> against them (Executive Summary Verdict and each finding's resolution note
> reflect the current, post-migration state). This report checks the
> `community-context/` domain for **structural conformance** against the two frozen
> contracts. It does not redesign the domain's content; content is treated as
> substantially correct and complete (confirmed against
> `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` and `community_context_discovery_report.md`
> in the companion Business Validation section of `Community_Context_Migration_Plan.md`).
>
> **Authorities:** `Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`,
> `Repository_Migration_Methodology.md`.
> **Reference implementation:** `registration/` (Phases 1–4 executed) and `shared/`
> (fully canonical) show the target shape.
> **Scope audited:** `community-context/{ontology,taxonomy}` — 16 governed files —
> plus `community-context-governance.md`, `community_context_discovery_report.md`,
> `_placeholder.yaml`, and `README.md` (informational, not governed).

---

## Executive Summary

Community Context is **content-mature but structurally pre-canonical** — the same
overall diagnosis Registration received before its own migration, with one
important difference: Registration's `attributes.yaml` existed (1143 lines of real
property detail migrated mechanically into `data-properties.yaml`). Community
Context's `entities.yaml` references an `attributes_ref: ontology/attributes.yaml#*`
target **that does not exist anywhere in the repository**. There is no file, no
prior draft, nothing to mechanically drain. Every scalar/coded property implied by
`key_attributes` is therefore a **genuine content gap** (`Repository_Migration_Methodology.md`
§5), not a relocation — this is the single largest divergence from the Registration
precedent and the one finding that cannot be closed by this migration alone.

Everything else was the familiar pre-canonical pattern **as originally found**
(all resolved by the Phase 1–4 migration; see the per-finding resolution notes
in the Critical Findings section below and the Verdict paragraph that follows):

1. **Taxonomy layer:** all 12 files use one of the non-conformant shapes the
   taxonomy contract's own audit (§2, T-1…T-9) names by number — comment-banner or
   partial-YAML headers, a `concepts: { <scheme>: {...} }` wrapper map instead of a
   `schemes:` list, `type: enum` dead metadata, and (in `settlement-types.yaml`)
   the single worst-shaped form in the whole repository: a list of single-key maps
   with **no `description` field at all**.
2. **Ontology layer:** `relationships.yaml` uses the retired cardinality enum and a
   forbidden `required:` field on every row (identical to Registration's pre-migration
   state). `entities.yaml` carries the deleted `key_attributes`/`attributes_ref`
   pattern, plus a redundant `external_references:` field that duplicates content
   `relationships.yaml` already expresses correctly.
3. **`semantic-constraints.yaml` is the domain's most distinctive divergence:** it
   authors real content, but in **hand-written OWL functional syntax**
   (`owl_mapping: "ObjectExactCardinality(...)"`) — the exact anti-pattern Ontology
   §9 names and forbids by name ("never as hand-authored OWL functional syntax").
   Two of its seven rows map cleanly onto the closed `type: cardinality` vocabulary;
   the other five use ad hoc `constraint_type` values
   (`cross_domain_boundary` ×2, `anti_recursion`, `domain_encapsulation`,
   `identity_disjointness`) that are **outside the closed §9 type vocabulary**
   (`cardinality`/`disjoint`/`required_if`/`mutually_exclusive`) and cannot be
   mechanically mapped without a disposition decision per row (Phase 0, below).
4. **The ontology `data-properties.yaml` file itself does not exist** — one of the
   fixed five files the module must contain even as a placeholder (Ontology §2).

**Verdict (updated at Phase 4 completion):** Community Context has completed
structural migration (Phases 1–3) and the mechanical portion of attribute
authoring (Phase 4): every finding below has been resolved except one precisely
scoped, genuine content gap
(`transportation_network_asset.surface_condition` — no taxonomy scheme exists to
wire it to). **Finding counts (original, all now resolved or narrowed):**
Critical **7** · Required **6** · Optional **3**. Classification split:
Mechanical **11** · Semantic **4** (all dispositions, resolved) · Genuine content
gap **1 of 18** properties (down from "the entire scalar-property set" at initial
audit — see CC-2's resolution note and
`Community_Context_Migration_Plan.md`'s Content Gap Log).

---

## Critical Findings

### CC-1 — `data-properties.yaml` does not exist · [MECHANICAL — RESOLVED at Phase 1/4]
**Contract:** Ontology §2, §13 (fixed five-file set, placeholders mandatory). The
module had `entities.yaml`, `relationships.yaml`, `semantic-constraints.yaml`,
`lifecycle-constraints.yaml` — missing `data-properties.yaml` entirely. **Resolved:**
created as a placeholder in Phase 1, populated with 44 rows in Phase 4.

### CC-2 — `attributes_ref` targets a file that does not exist · [RESOLVED at Phase 4]
**Contract:** Ontology §2 ("no `attributes.yaml`"), §4 (`attributes_ref` → deleted
concept). **File:** `entities.yaml`, all six entities carried
`attributes_ref: ontology/attributes.yaml#<entity>`. Unlike Registration, this path
resolved to **nothing** — `community-context/ontology/attributes.yaml` was never
authored. **Resolved:** the field was deleted (same as Registration R-R2), and
re-examination under methodology §2 found the `key_attributes` comments
(`community_id`, `livelihood_pattern`, `settlement_form`, `seasonal_events`,
`area_id`, `geographic_level`, …) were themselves already-present authoritative
content naming each property's source taxonomy file. Combined with Phase 2's now-
populated taxonomy schemes, 17 of 18 implied properties were mechanically wireable
into `ontology/data-properties.yaml` (Migration Plan Decision D-CC6). Only one
property (`transportation_network_asset.surface_condition`) remains a genuine
content gap — no taxonomy scheme anywhere in the domain enumerates
surface-condition values, so there is nothing existing to wire it to.

### CC-3 — `entities.yaml` carries a redundant, contract-forbidden `external_references` field · [MECHANICAL — RESOLVED at Phase 3]
**Contract:** Ontology §4 ("`external_references` → expressed as object properties
in `relationships.yaml`"). **File:** `entities.yaml`, on `built_infrastructure`
(`operating_organization_ref`) and `local_collective` (`member_ref`). Both
relationships **already exist correctly** in `relationships.yaml`
(`built_infrastructure_operated_by_organization`, `local_collective_composed_of_members`)
— `external_references` was a pure duplicate annotation with no information the
relationship row lacked. **Resolved:** field removed; no content lost.

### CC-4 — `relationships.yaml` uses the retired cardinality vocabulary · [MECHANICAL — RESOLVED at Phase 3]
**Contract:** Ontology §7. **File:** `relationships.yaml`, all 18 rows used
`one_to_one`/`one_to_many`/`many_to_many`/`many_to_one` instead of `{min, max}`.
Identical finding to Registration's C-R3. **Resolved:** all rows converted to
`{min, max}`.

### CC-5 — `relationships.yaml` carries a forbidden `required:` field · [MECHANICAL — RESOLVED at Phase 3]
**Contract:** Ontology §6 (obligation is `cardinality.min ≥ 1`; field set is
`id`/`from`/`relationship`/`to`/`cardinality`/`inverse`/`notes`). Every row also
carried `required: true|false`. Identical finding to Registration's R-R4.
**Resolved:** field removed from every row.

### CC-6 — All 12 taxonomy files use non-conformant root shapes · [MECHANICAL — RESOLVED at Phase 2]
**Contract:** Taxonomy §5–§6. Two distinct non-conformant shapes appear:
- **`concepts: { <scheme_name>: { description, type: enum, values: [...] } }`**
  (9 files: `accessibility`, `community-assets`, `community-hazards`,
  `essential-services`, `geographic-hierarchy`, `infrastructure-types`,
  `livelihood-patterns`, `local-organizations`, `physical-environment`,
  `seasonal-events`, `transportation` — 11 files, not 9; corrected count below)
  — scheme identity is a YAML map key, not an `id:` field; members sit under a
  `values:` wrapper, not `concepts:`; every scheme carries dead `type: enum`.
- **List-of-single-key-maps** (`settlement-types.yaml` only): each concept is
  `- some_id: "prose description"` — no `id:` field, no `label`, no `description`
  field (the value *is* the description, unlabeled) — the single most
  parser-hostile shape the taxonomy contract's own audit names (T-5 shape 1).
  `settlement-types.yaml` additionally has **no file header at all** (no `version`,
  `domain`, `file`, `status` keys of any kind — not even the comment-banner form
  other files use).

*(Corrected file count: 11 files use the `concepts: {map}` shape; 1
(`settlement-types.yaml`) uses list-of-single-key-maps. 11 + 1 = 12, all files.)*

### CC-7 — `semantic-constraints.yaml` is hand-authored OWL, not a target-neutral structure · [MECHANICAL + SEMANTIC — RESOLVED at Phase 3]
**Contract:** Ontology §9 ("never as hand-authored OWL functional syntax... a
constraint row states *what* is constrained; *how* that renders... is entirely a
generator concern"). **File:** `semantic-constraints.yaml`, all 7 rows use
`constraint_type`/`id`/`statement`/`owl_mapping`/`entities` — none use the
`id`/`type`/`property`/`entities`/`parameters` shape. Per-row disposition (Phase 0):

| Row | Current `constraint_type` | Disposition |
|---|---|---|
| `community_requires_geography` | `existential_dependency` | **Mechanical.** Maps directly onto §9's own illustrative example: `type: cardinality, property: located_in, entities: [community, geographic_area], parameters: {min:1,max:1}`. |
| `collective_requires_community` | `existential_dependency` | **Mechanical.** `type: cardinality, property: represents, entities: [local_collective, community], parameters: {min:1,max:1}`. |
| `built_vs_natural` | `identity_disjointness` | **Semantic, low-risk.** `type: disjoint` is in the closed vocabulary, but §9's `property` field has no natural class-level value (disjointness constrains classes, not a property). Recommended default: omit ambiguity by keying the row on the class pair only, `property` absent is not permitted (required field) — use a documented sentinel `property: rdf:type` (the property every individual's class membership is asserted through), consistent with how OWL's own `DisjointClasses` axiom needs no property either. Flagged, not silently decided — see Migration Plan Decision D-CC3. |
| `infrastructure_organization_reference` | `cross_domain_boundary` | **Mechanical — drop as redundant.** The `built_infrastructure_operated_by_organization` relationship row's `to: shared_org:organisation` already fixes the range; an `ObjectAllValuesFrom` restriction row would restate what the relationship schema already guarantees structurally. Not carried forward. |
| `collective_human_reference` | `cross_domain_boundary` | **Mechanical — relocate.** "No cascading deletes/ownership lifecycles" is lifecycle semantics, not a structural constraint. Moves to `lifecycle-constraints.yaml` on `local_collective` (a file that already exists and is explicitly "not a generation surface" per Ontology §9 — the correct home). |
| `geographic_area_anti_recursion` | `anti_recursion` | **Semantic — out of closed vocabulary.** Irreflexivity/asymmetry of `contains` has no §9 `type` to map onto (not `cardinality`/`disjoint`/`required_if`/`mutually_exclusive`). Recommended default: retain as a `notes:` field on the two `geographic_area`↔`geographic_area`-adjacent relationship rows in `relationships.yaml` (a tolerated, non-generation-affecting annotation, per the precedent Registration's audit already set for entity-level `notes:`) rather than inventing a new closed-vocabulary `type` under schedule pressure. |
| `no_operational_workflows` | `domain_encapsulation` | **Mechanical — relocate.** A governance boundary statement ("no outbound edges to Case Management workflows"), not a graph-structural fact about this domain's own entities. Moves into `community-context-governance.md`, which already states equivalent boundary rules for the taxonomy layer — this simply extends that document's existing pattern to the ontology layer. |

---

## Required Findings

### CC-R1 — Headers are non-conformant, in three different ways · [MECHANICAL — RESOLVED at Phase 1]
**Contract:** Ontology §12 / Taxonomy §4 (four top-level keys: `version`, `domain`,
`file`, `status`; `version` quoted three-part semver; `status` from the closed enum).
- `entities.yaml`, `relationships.yaml`, `lifecycle-constraints.yaml`,
  `semantic-constraints.yaml`: have `version`/`domain`/`file` but **no `status` key
  at all**; `version: "1.0"` is two-part, not three-part.
- 11 taxonomy files: comment-banner or partial-YAML headers (Taxonomy §2 T-1); use
  `taxonomy:` instead of `file:`; `version: 1.0.0`/`1.0.1` **unquoted**; no `status`
  key anywhere in the domain's taxonomy layer.
- `settlement-types.yaml`: no header of any kind.

### CC-R2 — Taxonomy scheme identity has no `id:` field · [MECHANICAL — RESOLVED at Phase 2]
**Contract:** Taxonomy §3, §5. Every scheme name is a YAML map key
(`physical_accessibility:`, `terrain:`, `geographic_level:`, …), not an explicit
`id:` field in a `schemes:` list — the same finding as Registration's C-R9 (merged
into C-R4 there; kept as its own line here because, unlike Registration, none of
Community Context's schemes have ever had an `id:` field under any wrapper).

### CC-R3 — `namespaces:` block uses file-path values, not CURIE prefixes · [MECHANICAL, manifest-blocked for final values]
**Contract:** Ontology §10 (CURIE, not file paths — the anti-pattern C-2 removes).
**Files:** `entities.yaml`, `relationships.yaml`:
```yaml
namespaces:
  shared_org: "shared/taxonomy/organisations.yaml"
  shared_human: "shared/human-model/ontology/entities.yaml"
```
Structurally present and already in the right *place* (a top-level `namespaces:`
block, exactly as §10 prescribes) — this is materially ahead of Registration, which
had no `namespaces:` block at all. Only the *values* are non-conformant (file paths
instead of manifest-registered CURIE prefixes); this is Phase-5/manifest-blocked
exactly as Registration's equivalent finding was, and the block shape itself
requires no change now.

### CC-R4 — `settlement-types.yaml` concepts have no `description` field · [MECHANICAL, content-preserving — RESOLVED at Phase 2]
**Contract:** Taxonomy §6 (`description` required on every concept; "never a bare
scalar with no description"). The one-line prose after each concept's colon *was*
its description (e.g. `metropolitan_center: "High-density, highly integrated core
of a major city."`) — recovered verbatim as the `description` field once the
record was converted to `{id, description}` shape. No content was missing; only
the shape was wrong. **Resolved.**

### CC-R5 — Cross-domain vocabulary reference is prose, not a `references:` entry · [MECHANICAL, manifest-blocked for values]
**Contract:** Taxonomy §8. `geographic-hierarchy.yaml`'s `alignment_notes` states in
free text that it "integrates with `shared/taxonomy/locations.yaml`" — this is
exactly the kind of relationship §8's structured `references:` block replaces.
Same-domain-side shape fix is mechanical now (bare form); the cross-domain CURIE
waits on the manifest.

### CC-R6 — `lifecycle-constraints.yaml` header lacks `status`; otherwise already closest to conformant · [MECHANICAL — RESOLVED at Phase 1/3]
Content shape (`lifecycle_constraints:` list keyed by `entity:`) already matched
Ontology §9's description of this file almost exactly — it was the domain's
best-conforming file at the time of audit. **Resolved:** header given the same
four-key fix as every other file (Phase 1); the relocated
`collective_human_reference` constraint (CC-7) landed here as a new list item
(Phase 3).

---

## Optional Findings

### CC-O1 — Governance boundary rules live in prose (`community-context-governance.md`), duplicating what `references:`/`ownership_boundary` will structurally express later · [FUTURE, OPTIONAL]
Not a defect — `community-context-governance.md` is exactly the kind of authoritative
companion document the taxonomy contract's own worked example (`settlement-types.yaml`
illustrative case, §14) assumes exists alongside the governed files. No action
required now; once Phase 5 CURIEs land, some of this prose becomes redundant with
structured `references:` entries, but the prose remains the human-readable source
and is not deleted.

### CC-O2 — `built_infrastructure`/`local_collective` cross-domain relationship rows point at plausible but unconfirmed target concepts · [FUTURE, OPTIONAL]
`shared_org:organisation` and `shared_human:person` are referenced; both concepts
exist in their respective domains today (confirmed:
`shared/taxonomy/organisations.yaml`, `shared/human-model` entities). No mismatch
found; flagged only so Phase 5 CURIE minting has a confirmed target list, not a
speculative one.

### CC-O3 — `_placeholder.yaml` is not a governed ontology/taxonomy file and is out of scope for this migration · [FUTURE, OPTIONAL]
It correctly declares deferred scope (population/demographics, governance,
culture, safety/security, public health) per the domain's own `README.md` "Does Not
Own" section. No structural contract governs it (it is neither an `ontology/` nor
`taxonomy/` file); no action required by this migration.

---

## Repository Readiness

| Gate | State | Blocks what |
|---|---|---|
| Ontology contract frozen | ✅ | — |
| Taxonomy contract frozen | ✅ | — |
| Reference implementation exists (Registration, Phases 1–4) | ✅ | — |
| Manifest / catalog (Finding R-1) | ❌ absent | CC-R3, CC-R5 *values* |
| Literal base IRI + prefixes (C-2) | ❌ not ratified | Same |
| `shared/taxonomy/organisations.yaml`, `shared/human-model` targets canonical | ✅ (both already migrated/canonical) | — (unlike Registration's `needs-assessment` blocker, both of Community Context's cross-domain targets are already conformant) |

**Conclusion (updated at Phase 4 completion):** Community Context's structural
migration and the mechanical portion of attribute authoring are both complete,
with no external domain blocking it (a materially better position than
Registration had with `needs-assessment`). The one remaining gap —
`transportation_network_asset.surface_condition` — requires a domain-knowledgeable
author to add a new taxonomy scheme before it can be authored, tracked in the
Migration Plan's Content Gap Log. It does not block any other part of the domain.
See `Community_Context_Migration_Plan.md` for the Phase 4 Completion Report.

*End of audit (as amended). See `Community_Context_Migration_Plan.md` for the
executable phase plan, Phase 0 Decision Table, and D-CC6 (Phase 4 decomposition
decision).*
