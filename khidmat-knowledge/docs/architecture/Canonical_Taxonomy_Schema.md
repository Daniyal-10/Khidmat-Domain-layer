# Canonical Taxonomy Authoring Contract

> **Phase:** RATIFIED and in effect. It fixes Finding **R-4**
> and closes the dependency the peer
> **[Canonical_Ontology_Schema.md](Canonical_Ontology_Schema.md)** left open at its §1 and §3: the
> taxonomy record shape, the taxonomy-concept identifier scope, and how `taxonomy_ref` resolves
> through the same deterministic, manifest-based mechanism as ontology cross-domain references —
> rather than as an arbitrary file path.
>
> **Sequencing (historical — superseded by actual migration order):**
> 1. ✅ Freeze ontology architecture — `Canonical_Ontology_Schema.md`.
> 2. ✅ Freeze taxonomy architecture — *this document.*
> 3. ✅ Review both architectures — ratified.
> 4. ✅ Migrate Registration — first reference implementation (not Community Context, as originally
>    sequenced here; see `Canonical_Ontology_Schema.md`'s status banner).
> 5. ✅ Migrate Community Context — second reference implementation (Phases 1–4 of
>    its canonical migration complete, 17/18 content rows authored; Phase 5 CURIE
>    linking remains blocked, see `community-context/community-context-governance.md`). → validate and migrate remaining domains next.

**Purpose:** the normative authoring contract that every current and future domain's `taxonomy/`
module must follow. The repository is the source of truth; every downstream representation is
*generated from* it, never authored *into* it. This document exists to eliminate taxonomy-layer
ambiguity *before* any taxonomy content is modified. When this document and a domain file disagree
(after approval), this document wins.

**Relationship to the ontology contract:** this document is a **peer**, not a subset, of
`Canonical_Ontology_Schema.md`. It governs only the controlled-vocabulary layer (`taxonomy/`
modules). It does not redefine `entities.yaml`, `data-properties.yaml`, `relationships.yaml`, or
constraint files — those remain governed exclusively by the ontology contract. Where the two
documents share a mechanism (identifier uniqueness, CURIE resolution, header shape, status enum),
this document reuses the ontology contract's rule by reference instead of restating a divergent
one, so the repository has exactly one namespace mechanism, one header contract, and one status
vocabulary — not two.

---

## Table of Contents

- [0. How to read this document — ratification status](#0-how-to-read-this-document--ratification-status)
- [1. Scope](#1-scope)
- [2. Audit — what currently exists, and why it blocks deterministic generation](#2-audit--what-currently-exists-and-why-it-blocks-deterministic-generation)
- [3. Identifier uniqueness, scope & concept-addressing granularity](#3-identifier-uniqueness-scope--concept-addressing-granularity--proposed)
- [4. Taxonomy file header](#4-taxonomy-file-header--ratified-by-reference-to-the-ontology-contract)
- [5. Concept-scheme record — `schemes:`](#5-concept-scheme-record--schemes--proposed)
- [6. Concept record — `concepts:`](#6-concept-record--concepts--proposed)
- [7. Hierarchy within a scheme](#7-hierarchy-within-a-scheme--ratified-by-reference-to-the-ontology-contract)
- [8. Cross-reference conventions](#8-cross-reference-conventions--proposed-form-only-values-ratified-in-c-2)
- [9. Taxonomy concept ownership](#9-taxonomy-concept-ownership--ratified-by-reference-to-adr-008)
- [10. Naming conventions](#10-naming-conventions--proposed)
- [11. Localization strategy](#11-localization-strategy--proposed-explicitly-minimal)
- [12. Structural invariants](#12-structural-invariants--proposed-definition-of-conformance-only-not-a-validator-spec)
- [13. Taxonomy file template](#13-taxonomy-file-template--ratified-shape)
- [14. Illustrative example](#14-illustrative-example--not-applied-to-any-domain)
- [15. Conformance summary](#15-conformance-summary-what-an-approved-generator-may-assume)
- [16. Future work](#16-future-work)
- [17. Approval gate](#17-approval-gate)

---

## 0. How to read this document — ratification status

Each section is tagged so the reviewer can see what is already agreed versus newly proposed:

- **[RATIFIED]** — restates a decision already ratified in `Canonical_Ontology_Schema.md`, applied
  here to the taxonomy layer. Subject only to confirmation.
- **[PROPOSED]** — introduced by this document for approval in the review step. Not previously
  ratified. These are the sections to scrutinize most closely.

Nothing here is applied to repository content until the whole document is approved.

---

## 1. Scope

**Governed by this specification:**
- Deterministic `taxonomy/` file layout and file-to-scheme relationship.
- The concept-scheme / concept record schema (§§5–6).
- Hierarchy representation within a scheme (§7).
- Taxonomy-concept identifier scope and addressing granularity — resolving the open item left by
  `Canonical_Ontology_Schema.md` §1 (Finding R-4) and §3 (taxonomy-concept namespace).
- How `taxonomy_ref` (defined on the ontology side) resolves to a scheme, and how a concept's own
  identity resolves, through the same manifest mechanism as ontology cross-domain references (§8).
- Metadata / file-header conventions for taxonomy files (§4) — the *same* header contract as the
  ontology side, not a second one.
- Single-ownership of taxonomy concepts, consistent with ADR-008 (§9).
- Naming conventions (§10), localization posture (§11), and structural invariants (§12).
- The reusable taxonomy-file template (§13).
- Sub-module taxonomy folders within a bounded context (e.g. `shared/human-model/taxonomy/`,
  `shared/risk/taxonomy/`) follow this identical template — this is a clarification of the existing
  architecture, per `Canonical_Ontology_Schema.md` §2's sub-module rule, not a new pattern.

**Not governed here (delegated elsewhere or explicitly out of scope):**
- **Concrete IRI/base values, per-domain CURIE prefixes** — ratified under Finding **C-2**, the
  same finding the ontology contract defers to. This document fixes only the *form* of taxonomy
  addressing; C-2 fixes the literal values.
- **Entity, data-property, relationship, and constraint schemas** — `Canonical_Ontology_Schema.md`
  owns these exclusively.
- **Artifact generation into any target representation** — Finding **F-3**. This document fixes
  only the repository-side structure; how that structure is rendered downstream is entirely a
  future generator's decision, never the source files'.
- **Localization / translation infrastructure** — §11 states the posture (single canonical
  authoring language, no i18n layer today) but does not design a translation mechanism; that is
  future work if and when it becomes a real requirement.
- **CI/CD, validation tooling, build pipelines** — Finding F-2. §12 states the structural
  invariants a future validator checks; it does not implement one.

---

## 2. Audit — what currently exists, and why it blocks deterministic generation

Before proposing a schema, this section records what was found across every taxonomy file
presently in the repository: `community-context/taxonomy/*` (12 files), `registration/taxonomy/*`
(9 files), `shared/taxonomy/*` (5 files), `verification-operations/taxonomy/*` (7 files) — 33 files
across 4 domains. No file was modified during this audit.

### T-1 — Four incompatible file-header shapes

- **Comment-only banner, no YAML header keys at all in the file's first block**
  (`community-context/taxonomy/accessibility.yaml`, `community-assets.yaml`,
  `community-hazards.yaml`, `essential-services.yaml`, `livelihood-patterns.yaml`,
  `local-organizations.yaml`, `seasonal-events.yaml`, `settlement-types.yaml`,
  `transportation.yaml`): a ~30-line `#`-comment block carries `Domain:`, `Context:`, `File:` as
  prose, with the actual `domain:` / `taxonomy:` / `version:` YAML keys appearing only *after* the
  comment block, well past line 30.
- **Shorter comment banner + earlier YAML header** (`community-context/taxonomy/geographic-hierarchy.yaml`,
  `infrastructure-types.yaml`, `physical-environment.yaml`): `domain:` / `taxonomy:` / `version:`
  appear as flat YAML keys near the top, but the key set (`taxonomy:`, not `file:`) differs from
  the ontology contract's header shape.
- **Flat YAML header, no comment banner** (`registration/taxonomy/*`, `shared/taxonomy/*`):
  `version:` / `domain:` / `file:` / occasionally `status:` / `imports:` as top-level keys —
  closest to the ontology contract's §12 header shape, but inconsistent about which keys are
  present (`status` appears only on 2 of 9 registration files).
- **Nested `metadata:` map** (`verification-operations/taxonomy/*`, all 7 files): header fields are
  a sub-map — `metadata: { file, domain, layer, status }` — rather than top-level keys, and adds a
  `layer:` key not present anywhere else.

A generator cannot locate `version`/`domain`/`status` with one code path; it must special-case four
structurally different header locations.

### T-2 — `domain` field is not a stable, consistent token

- `domain: community_context` (snake_case) — community-context files.
- `domain: registration`, `domain: shared` — single-word, effectively snake_case.
- `domain: Verification Operations` (**Title Case with a literal space**) — every
  `verification-operations/taxonomy/*` file, inside `metadata:`.

A Title-Case-with-space value cannot be used as a CURIE prefix or IRI path segment without an
undocumented normalization step. This is the taxonomy-side instance of the same failure mode
Finding C-2 identifies for ontology namespaces: the identity token is inconsistent before any IRI
scheme is even applied.

### T-3 — `version` is expressed three incompatible ways, and is sometimes absent entirely

- Unquoted three-part semver, `version: 1.0.0` / `version: 1.0.1` — all `community-context/taxonomy/*`
  files.
- Quoted two-part string, `version: "1.0"` / `version: "1.1"` — all `registration/taxonomy/*` and
  `shared/taxonomy/*` files.
- **No `version` key at all** — every `verification-operations/taxonomy/*` file; `status: Phase 4.1`
  is carried instead, which is a lifecycle marker, not a version number.

This is the exact inconsistency Finding R-3 already identifies on the ontology side, reproduced
independently in taxonomy files rather than shared as one contract.

### T-4 — `status` is free text, not a closed vocabulary, where it exists at all

Observed values: `Level_1` (`registration/taxonomy/evidence.yaml`), `placeholder`
(`registration/taxonomy/support-interventions.yaml`), `Phase 4.1`
(`verification-operations/taxonomy/*`, all 7 files), `"Phase 4.0 — Active"`
(`shared/taxonomy/time.yaml`) — four different vocabularies, three of which are sprint/phase labels
rather than a lifecycle-state enum. No file uses the `active | placeholder | draft | deprecated`
enum `Canonical_Ontology_Schema.md` §12 already proposes for ontology headers.

### T-5 — Five incompatible root/record structures for the enumerated values themselves

Confirms and extends Finding R-4 with the exact shapes found:

1. **List-of-single-key-maps** (the form R-4 already names as most parser-hostile) —
   `community-context/taxonomy/settlement-types.yaml`: `- metropolitan_center: "High-density..."`.
   Each list item is a one-entry, dynamically-keyed object; a generator must read the map's only
   key as the id and its only value as the description, with no `label` at all.
2. **Bare scalar list, no structure whatsoever** — `shared/taxonomy/organisations.yaml`
   (`organisation_types: [hospital_or_clinic, school_or_madrasa, ...]`),
   `shared/taxonomy/document-types.yaml` (five categories, all bare scalar lists), and
   `shared/taxonomy/persons.yaml` (`person_roles`, `gender_vocabulary`). There is no `id` field to
   even key off of — the scalar *is* the identifier, description and label do not exist.
3. **`concepts: { <scheme>: { description, type: enum, values: [ {id, label, description} ] } }`** —
   `community-context/taxonomy/accessibility.yaml`, `community-hazards.yaml`,
   `geographic-hierarchy.yaml`, `infrastructure-types.yaml`, `physical-environment.yaml`, and
   others: schemes are nested two levels inside a `concepts:` wrapper map keyed by scheme name, and
   each carries a redundant `type: enum` (every taxonomy scheme is inherently an enumeration; the
   field carries no information a generator can act on differently).
4. **Flat root-level scheme keys, `{id, label, description}` records, no wrapper** —
   `registration/taxonomy/*` (`need_source:`, `claim_types:`, `case_statuses:`, …),
   `shared/taxonomy/locations.yaml` (`location_precision:`, `location_stability:`), and
   `verification-operations/taxonomy/*` (`verification_status:`, `could_not_complete_reason:`, …):
   this is the closest to a clean, generator-friendly shape, but scheme identity is the YAML key
   itself rather than an explicit `id:` field, so the scheme has no addressable identifier distinct
   from its file position.
5. **Map keyed by category name, values as sub-maps, not a list at all** —
   `registration/taxonomy/evidence.yaml`: `evidence_types:` is a map (`documentary:`, `physical:`,
   `testimonial:`, …) each holding `label` / `description` / optional `subtypes:`, rather than a
   list of `{id, ...}` records — the same list-vs-map divergence Finding C-1 identifies for
   `entities.yaml`, reproduced here for taxonomy categories.

A generator cannot walk any of these with one code path; it must detect which of five shapes a
given file uses before it can extract a single value.

### T-6 — Hierarchy is expressed by embedding children, the exact anti-pattern retired on the ontology side

`registration/taxonomy/actors.yaml` (`proxy.subtypes`), `evidence.yaml` (`physical.subtypes`,
`testimonial.subtypes`), and `needs.yaml` (every `need_categories` entry's `subtypes`) nest child
concepts as an inline list under the parent, mirroring the `subtypes:` field
`Canonical_Ontology_Schema.md` §4 explicitly removes from `entities.yaml` ("hierarchy is expressed
**only** by the child's `parent`"). `evidence.yaml` additionally uses a *third*, unrelated field
name — `allowed_subtypes:` (a same-spelling but different-meaning constraint list referencing
another scheme's ids, not an embedding of children) — for a fourth file
(`documentary`/`medical`/`financial`/etc. blocks), which is easy to confuse with the embedding
`subtypes:` field on casual reading despite meaning something structurally different.

### T-7 — Cross-file/cross-domain references use four incompatible mechanisms, none of them CURIEs

- `imports: shared/taxonomy/persons.yaml` — a bare scalar file path
  (`registration/taxonomy/actors.yaml`).
- `imports: [shared/taxonomy/document-types.yaml, registration/taxonomy/claims.yaml]` — a list of
  file paths (`registration/taxonomy/evidence.yaml`).
- `ref: shared/human-model/capabilities.yaml#capability_levels` — a singular file-path-plus-fragment
  field (`shared/taxonomy/persons.yaml`, `functional_capacity`).
- `cross_references:` list items that fold a file-path-plus-fragment and multi-line prose
  explanation into **one plain YAML scalar** — every `verification-operations/taxonomy/*` file,
  e.g.:
  ```yaml
  cross_references:
    - verification-operations/verification-operations.yaml#verification_activity
        This file supplies the controlled status vocabulary for the
        verification_activity concept already declared there. It does
        not redefine verification_activity itself.
  ```
  Because the continuation lines are indented deeper than the `-` and contain no block-scalar
  indicator (`|` / `>`), YAML's plain-scalar folding rule merges the path and the prose paragraph
  into a **single folded string** with no field boundary between "what is referenced" and "why."
  No generator can mechanically separate the reference target from the explanation without
  re-parsing free text — this is the most parser-hostile pattern found in the entire audit, worse
  than the list-of-single-key-map form R-4 already names, because it is not even reliably
  splittable by punctuation.

All four are the taxonomy-layer instance of Finding C-2/R-1: relative file paths standing in for
IRIs/CURIEs, with no manifest-resolved mechanism and no acyclic-dependency enforcement visible at
the file level.

### T-8 — Identifier collisions are already latent under a naive "unique per domain" rule

`shared/taxonomy/locations.yaml` defines `id: unknown` in **both** `location_precision` and
`location_stability` — two different schemes in the same file, same domain. Under the ontology
contract's §3 rule taken naively ("unique across all kinds... within its owning domain"), this
would already be a collision. It demonstrates that taxonomy-concept identity cannot reuse the
ontology's flat `(domain, id)` uniqueness scope unmodified — a taxonomy concept's true identity key
must include its owning scheme (§3 below), which is exactly the addressing-granularity question
`Canonical_Ontology_Schema.md` §1 (Finding R-4) left open for this document to resolve.

### T-9 — Auxiliary/domain-specific fields are unbounded and undeclared

Concept records carry ad hoc extra fields with no reserved-vs-extension boundary:
`default_claim_basis`, `questioning_note`, `verification_weight`, `contextual_prior`,
`requires_linked_member`, `note` (multiple unrelated meanings across files), `governing_adr`,
`design_notes`, `alignment_notes`. Some are scheme-level, some concept-level, with no rule for
which is which, and no declared boundary between "core taxonomy fields every generator must
understand" and "domain-authored extension fields a generator may ignore."

### Summary — why this blocks deterministic generation

Every one of the findings a generator would need resolved before it could run on a single code path
(header location, version format, status vocabulary, record shape,
hierarchy expression, reference resolution, identifier scope) is inconsistent across the 33 files
audited, in ways that parallel — but are not identical to, and were not previously enumerated
alongside — the ontology-side findings C-1, C-2, C-3, R-3, R-4. This document exists to close all
nine (T-1…T-9) with one schema before any taxonomy file is migrated.

---

## 3. Identifier uniqueness, scope & concept-addressing granularity — [PROPOSED]

This is the central architectural decision this document makes, resolving the item
`Canonical_Ontology_Schema.md` §1 and §3 explicitly deferred here.

**Two addressable kinds, not one.** A taxonomy file contains **concept schemes** (a named,
governed vocabulary — e.g. `settlement_formality`, `verification_status`) and, inside each scheme,
**concepts** (the enumerated members — e.g. `informal_urban_settlement`). Both are independently
addressable, for the same reason `Canonical_Ontology_Schema.md` addresses classes and properties
independently: `taxonomy_ref` (ontology §5) names *which vocabulary constrains a value* — that is a
**scheme** reference — while a stored value is *one specific member of that vocabulary* — that is a
**concept** reference. Collapsing the two into one flat identifier space is exactly what produced
Finding T-8's latent collision (`unknown` reused as a concept id under two different schemes in the
same file).

**Uniqueness scope, fixed by evidence in T-8:**
- A **scheme `id`** must be unique within its owning domain (same discipline as ontology §3's
  domain-scoped uniqueness, applied to the scheme kind).
- A **concept `id`** must be unique **within its owning scheme**, not globally within the domain.
  Two different schemes in the same domain (even the same file, as `location_precision` and
  `location_stability` already do) may each mint their own `id: unknown` — they are different
  concepts because their owning scheme differs, exactly as two different ontology domains may each
  mint `id: status` because their owning domain differs.
- The true identity key for a concept is therefore the pair **`(scheme_id, concept_id)`**, and for
  a scheme it is the pair **`(domain, scheme_id)`** — mirroring the ontology contract's
  `(domain, id)` key one level down.

**CURIE and IRI form, deferred to C-2 for literal values, fixed here for shape:**
- A scheme resolves as `scheme_curie = "<domain_prefix>:<scheme_id>"`, identical in form to an
  ontology entity/property CURIE.
- A concept resolves as `concept_curie = "<domain_prefix>:<scheme_id>.<concept_id>"` — the scheme
  segment is mandatory in a concept's local name because concept ids are not domain-unique (T-8).
- `taxonomy_ref` on the ontology side (§5 of the ontology contract) always names a **scheme**
  CURIE, never a bare concept id, so an ontology data property's controlled vocabulary is
  unambiguous independent of which concept within it a given instance holds.
- Same-domain references use the bare local form (`scheme_id` or `scheme_id.concept_id`);
  cross-domain references are full CURIEs resolved via the manifest, per the ontology contract's
  §10 mechanism — there is no second resolution mechanism for taxonomy.

**Stability:** per the same rule as ontology §3, a scheme or concept `id` is frozen the moment it
is written to a merged file. Renaming is a breaking change to every CURIE and reference that
targets it; `id`s are immutable until a deprecation policy exists (Finding F-5, out of scope here).

---

## 4. Taxonomy file header — [RATIFIED by reference to the ontology contract]

The header is **the same contract** as `Canonical_Ontology_Schema.md` §12, applied to taxonomy
files — not a second, taxonomy-specific header shape. This directly resolves T-1, T-2, T-3, T-4.

- **Header as top-level YAML keys, never comments, never a nested `metadata:` map.** The
  comment-banner header (T-1, community-context legacy files) and the nested `metadata:` map
  (T-1, verification-operations) are both non-conformant.
- **Mandatory keys:** `version`, `domain`, `file`, `status` — identical set to the ontology header.
- **`status` enum:** `active | placeholder | draft | deprecated` — the same closed vocabulary as
  the ontology contract, not a phase/sprint label (T-4). `Phase 4.1`, `Level_1`, and similar values
  are not `status` values; if a domain wants to record a phase or sprint marker, it is a distinct,
  non-mandatory, explicitly-named field (e.g. `delivery_phase`), never overloaded onto `status`.
- **`domain` is the same snake_case token the domain's ontology module uses** — never a Title-Case
  label with spaces (T-2). `Verification Operations` becomes `verification_operations`, matching
  the domain's own ontology `domain:` value exactly, because both feed the same CURIE prefix.
- **`version` format:** one canonical form — a quoted semantic-version string,
  `"MAJOR.MINOR.PATCH"` — resolving the unquoted-`x.y.z`-vs-quoted-`"x.y"`-vs-absent inconsistency
  (T-3).
- **`file`:** the file's own repo-relative path, matching the ontology header's convention.
- A taxonomy file's header carries no ontology-side fields (`ownership_boundary`, `owl_version_iri`
  are ontology-module concerns); if a taxonomy file needs a versionIRI-equivalent, that is decided
  by the same Finding R-3 process as the ontology side, not invented independently here.

---

## 5. Concept-scheme record — `schemes:` — [PROPOSED]

Every taxonomy file's payload is **always a top-level `schemes:` YAML list**, each item an
explicit, `id`-keyed scheme record — never a `concepts:` wrapper map keyed by scheme name (T-5
shape 3), never flat root-level keys with the scheme name as the YAML key itself (T-5 shape 4),
never a map keyed by category name (T-5 shape 5). This is the taxonomy-layer equivalent of the
ontology contract's "`entities:` is always a list, never a map" rule (ontology §4), applied for the
same reason: a list of explicit records gives every scheme a real `id` field a generator can read,
independent of YAML key position or casing.

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | Stable snake_case local name, unique per §3. **Frozen once written.** |
| `label` | optional | Human-readable scheme name. Present only when it adds meaning beyond `id`. |
| `description` | yes | Prose definition of what the scheme classifies and its boundary (mirrors ontology §4's class `description`). |
| `concepts` | yes | A YAML list of concept records (§6). Never empty for an `active` scheme — a scheme with no concepts is `status: placeholder` at the file level, not an empty list inside an active scheme. |

**Not permitted in a scheme record:**
- `type: enum` — deleted (T-5 shape 3). Every scheme is inherently an enumeration; the field
  encodes no distinguishing information and is removed rather than carried forward as dead
  metadata.
- Embedded child schemes or a second-level `values:`/`concepts:` wrapper beyond the one `concepts:`
  list — one scheme, one flat concept list (hierarchy inside it is `parent`, §7).

A file may declare **multiple independent schemes** (this is not restricted) — e.g. one file may
define `need_source`, `need_categories`, and `need_duration` as three list items in the same
`schemes:` list, exactly as `registration/taxonomy/needs.yaml` already does conceptually, just
flattened into one list instead of three ungoverned root keys.

---

## 6. Concept record — `concepts:` — [PROPOSED]

`concepts:` inside a scheme (§5) is a YAML list, each item an explicit `id`-keyed concept record.
Resolves T-5 (all five conflicting shapes) and T-9 (undeclared auxiliary fields) into one shape.

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | Stable snake_case local name, unique within its owning scheme per §3. **Frozen once written.** |
| `label` | optional | Human-readable name, only when it adds meaning beyond `id`. |
| `description` | yes | Prose definition of the concept. Never a bare scalar with no description (T-5 shapes 1–2 are non-conformant for this reason alone). |
| `parent` | optional | Sibling concept `id` within the **same scheme** (§7). Never a nested/embedded child list. |

**Extension fields (domain-authored, not part of the core contract):** a concept record may carry
additional domain-specific fields beyond the four above — e.g. `default_claim_basis`,
`verification_weight`, `requires_linked_member`, `questioning_note` — exactly as today's files
already do. This document does not forbid them; it fixes the boundary T-9 found missing:
- The four fields above are the **only** fields every generator is required to understand.
- Any other field is a **domain extension**: authored freely by the owning domain, ignored by a
  generic generator unless that generator is specifically written to understand it, and never
  assumed to exist by any cross-domain reference or by this contract's structural invariants (§12).
- An extension field must not shadow or duplicate the meaning of a core field (e.g. a `note` field
  is fine as a domain extension; a `notes` field that silently doubles as `description` is not).

**Not permitted in a concept record:**
- `subtypes` / `allowed_subtypes` embedding child concepts inline — deleted (T-6); hierarchy is
  expressed **only** by the child's `parent` (§7), exactly as the ontology contract retires
  `subtypes` from `entities.yaml` for the identical reason (one direction of truth, not two).
- Bare scalar list membership with no record at all (T-5 shape 2) — every concept is a record with
  at minimum `id` and `description`.

---

## 7. Hierarchy within a scheme — [RATIFIED by reference to the ontology contract]

Hierarchy is expressed **only** by a child concept's `parent` field (§6), naming a sibling
concept's `id` within the same scheme. The reverse (an inline `subtypes`/`allowed_subtypes` list on
the parent) is never stored; it is derivable. This is the exact rule
`Canonical_Ontology_Schema.md` §8 already ratifies for `entities.yaml`, applied here to resolve T-6
— one direction of truth for class hierarchy, one direction of truth for concept hierarchy, using
the same mechanism so a generator has a single hierarchy-walking code path across both layers.

A concept with no `parent` is a top-level concept of its scheme. Depth is not restricted (a
concept's parent may itself have a parent), mirroring the unrestricted depth `entities.yaml`
already permits via `parent`.

---

## 8. Cross-reference conventions — [PROPOSED] (form only; values ratified in C-2)

Resolves T-7. Every cross-file or cross-domain reference a taxonomy file makes — to another
taxonomy scheme, to an ontology entity/property it supplies values for, or to governance material —
is a **structured list of explicit-field records**, never a bare file-path scalar (`imports:`,
`ref:`), never a folded plain-scalar mixing a path and prose (`cross_references:`).

```yaml
references:
  - scheme: <curie-or-bare-scheme-id>     # what is referenced — always a scheme, per §3
    relation: extends | constrains | supplies_values_for | informs
    note: >                                # optional; a real block scalar, never folded
      Free-text explanation, structurally separate from `scheme` and `relation`.
```

Rules:
- **`scheme`** is a scheme reference per §3 — a bare local `id` for same-domain references, a
  full CURIE (`prefix:scheme_id`) for cross-domain references — resolved via the same
  repository-wide manifest the ontology contract's §10 defines. There is no second, taxonomy-only
  manifest or resolution path.
- **`relation`** is a closed, small vocabulary describing *why* the reference exists:
  `extends` (this scheme adds concepts to one owned elsewhere), `constrains` (this scheme narrows
  or validates another), `supplies_values_for` (this scheme is the controlled vocabulary an
  ontology entity/property draws from — the taxonomy-side mirror of an ontology `taxonomy_ref`
  pointing back), `informs` (a looser, non-binding relationship, replacing free-text notes like
  "response_window ... informs how long ... may remain open").
- **`note` is always its own field**, using a real YAML block scalar (`>` or `|`), never folded
  into the same string as `scheme`. This is the specific fix for T-7's worst finding: path and
  prose must never occupy one scalar.
- **Acyclic requirement.** The same DAG rule the ontology contract states in §10 applies
  identically here: if scheme A's `references` names scheme B, B must not reference A, directly or
  transitively.

---

## 9. Taxonomy concept ownership — [RATIFIED by reference to ADR-008]

This section states, as a binding contract rule rather than as prose scattered across individual
files' `purpose`/`alignment_notes` blocks (as the audit found — e.g. settlement-types.yaml's
"Confirmed as the sole canonical owner of settlement formality..."), the same single-ownership
discipline ADR-008 already establishes repository-wide and `Canonical_Ontology_Schema.md` §11
already applies to reusable object properties. Taxonomy needs the identical rule because a
concept, like a predicate, is trivially easy to redefine by accident once two domains both want a
similar vocabulary.

- **Every taxonomy concept has exactly one owning scheme, in exactly one owning domain.** A concept
  is minted once, per §3's identity key, and that domain is its sole source of truth.
- **A domain may reference a concept owned elsewhere; it must never redefine it.** Cross-domain use
  of another domain's vocabulary is expressed only through a `references` entry (§8) pointing at
  the owning scheme — never by re-declaring an equivalent concept locally under a new `id`.
- **Duplicate concepts across taxonomies are prohibited.** If two domains independently mint
  semantically equivalent concepts (e.g. an "unknown" precision value and an "unknown" stability
  value are *not* a duplicate — they are legitimately distinct concepts in distinct schemes, per
  T-8 — but two domains each minting their own `organisation_type` vocabulary *would* be), the
  duplication is a governance defect to resolve by promotion, not to leave standing.
- **A concept that becomes genuinely cross-domain is promoted to `shared/taxonomy/`**, using the
  same promotion governance `Canonical_Ontology_Schema.md` §11 already defines for predicates: it
  is proposed, reviewed, and, once accepted, every other domain's reference is updated to point at
  the shared scheme instead of a locally redefined one. No domain unilaterally "shares" a concept
  by convention alone.

This is a restatement of an existing, already-ratified repository rule (ADR-008) applied
explicitly to the taxonomy layer — it introduces no new governance process beyond the one the
ontology contract already established for predicates.

---

## 10. Naming conventions — [PROPOSED]

- **File names:** kebab-case, `.yaml` extension — already consistent across all 33 audited files;
  ratified as-is, no change required.
- **`domain` header value:** snake_case, identical to the token the domain's ontology module uses
  (fixes T-2's Title-Case-with-space case).
- **Scheme `id` and concept `id`:** snake_case, English canonical terms — consistent with the
  existing ADR-022 (Regional Localization) convention already followed in most files (e.g.
  `informal_urban_settlement` rather than a regional alias); this document does not introduce a new
  naming philosophy, it makes the existing one universal instead of observed only in some domains.
- **No PascalCase keys, no map-keyed identity** anywhere in a taxonomy file — identity is always an
  explicit `id:` field inside a list record (§§5–6), never a YAML map key standing in for identity
  (T-5 shapes 3–5).
- **`label` casing:** Title Case for the human-readable label value is a rendering choice, not a
  contract requirement — the current mix of Title Case (`"Metropolitan Center"`) and plain prose
  (`Expressed`) labels is acceptable; `label` is explicitly non-normative for machine consumption
  and exists only for human readability.

---

## 11. Localization strategy — [PROPOSED, explicitly minimal]

**Current state:** every taxonomy file today is authored in a single language (English), with
`label`/`description` as plain scalars. No file has ever attempted a translation mechanism.

**Decision, matching the "avoid over-engineering" instruction governing this document:** this
contract does **not** introduce an i18n/translation layer. `label` and `description` remain single
plain-language values. Localization — if and when a real product requirement for it exists — is a
**future, additive** concern (e.g. an optional `labels: { en: ..., ur: ... }` map alongside, or
replacing, the scalar `label`), decided in its own finding when the need is concrete, not designed
speculatively now. This section exists only to record that the omission is deliberate, not an
oversight — so a future author does not have to re-discover whether localization was considered.

---

## 12. Structural invariants — [PROPOSED] (definition of conformance only; not a validator spec)

This section is a short pointer, not a restatement: it names the invariants a future conformance
check (Finding F-2, out of scope here) would test, each already fully defined by the section that
owns it. It exists so "conformance" has one place to point to, without duplicating the schema a
second time in checklist form.

A conforming taxonomy file: has the header §4 requires; expresses `schemes:` and `concepts:` as the
lists §§5–6 require, with the identifier uniqueness §3 requires; expresses hierarchy only via
`parent` (§7); expresses cross-references only via `references` entries with `scheme`, `relation`,
and an independent `note` (§8); and respects the single-ownership rule (§9). Nothing here is a new
requirement — each is a cross-reference to the section that already normatively states it.

---

## 13. Taxonomy file template — [RATIFIED shape]

The canonical skeleton a new (or migrated) taxonomy file copies:

```yaml
version: "1.0.0"
domain: <domain>
file: taxonomy/<name>.yaml
status: active

purpose: >
  What this file's schemes classify, and what they explicitly do not
  (single-ownership boundary note — same convention already used across
  the repository's ADR-008 discipline).

schemes:
  - id: <scheme_id>
    label: <Optional Human Label>
    description: >
      What this scheme classifies.
    concepts:
      - id: <concept_id>
        label: <Optional Human Label>
        description: >
          What this concept means.
      - id: <child_concept_id>
        label: <Optional Human Label>
        description: >
          A narrower concept within the same scheme.
        parent: <concept_id>

references:
  - scheme: <bare-id-or-curie>
    relation: extends | constrains | supplies_values_for | informs
    note: >
      Optional prose, always its own field.
```

At the domain-module level, the `taxonomy/` folder itself is unrestricted in file count (unlike the
ontology module's fixed five-file set) — a domain authors one file per coherent vocabulary area, as
it already does — but **every** file in it follows this template.

---

## 14. Illustrative example — not applied to any domain

Illustrative only, to make §§5–8 concrete against a real case found in the audit. **This is not a
migrated file and has not been written to the repository.**

```yaml
# taxonomy/settlement-types.yaml — illustrative only
version: "1.0.0"
domain: community_context
file: taxonomy/settlement-types.yaml
status: active

purpose: >
  Classifies the structural settlement pattern and formality of a
  community's physical arrangement. Does not model land ownership,
  political governance, or individual beneficiary conditions
  (ADR-008 single-ownership boundary).

schemes:
  - id: settlement_formality
    label: Settlement Formality
    description: >
      Classification of a settlement by structural permanence and
      formal planning status.
    concepts:
      - id: planned_formal_settlement
        label: Planned Formal Settlement
        description: >
          Settlement constructed according to official zoning,
          planning, and building codes.
      - id: informal_urban_settlement
        label: Informal Urban Settlement
        description: >
          Dense, unplanned urban or peri-urban settlement lacking
          formal recognition or structural compliance.
      - id: organized_displaced_settlement
        label: Organized Displaced Settlement
        description: >
          Formally planned camp or settlement established specifically
          for displaced populations.
        parent: planned_formal_settlement

references:
  - scheme: geographic_hierarchy
    relation: informs
    note: >
      A settlement occupies a standard geographic_hierarchy level; its
      formality is expressed here, not as a separate hierarchy level.
```

```yaml
# community-context/ontology/data-properties.yaml — illustrative, ontology side
data_properties:
  - id: settlement_form
    domain: community
    taxonomy_ref: settlement_formality   # scheme CURIE per §3 — not a value id, not a file path
    cardinality: { min: 0, max: 1 }
```

---

## 15. Conformance summary (what an approved generator may assume)

1. Every taxonomy file's header is four top-level YAML keys — `version`, `domain`, `file`,
   `status` — identical shape and status enum to the ontology contract.
2. `schemes:` is always a list of `id`-keyed scheme records; `concepts:` inside each is always a
   list of `id`-keyed concept records. Never a map, never a wrapper, never a bare scalar list.
3. A concept's true identity is `(scheme_id, concept_id)`; a scheme's true identity is
   `(domain, scheme_id)`. CURIEs are a pure function of these pairs, resolved through the one
   repository-wide manifest shared with the ontology contract.
4. `taxonomy_ref` on the ontology side always names a scheme, never a bare concept id.
5. Hierarchy is expressed only by a concept's `parent`; no `subtypes`/`allowed_subtypes` embedding
   is ever authored.
6. Every cross-reference is a `references` list entry with explicit `scheme` / `relation` /
   optional `note` fields — never a folded path+prose scalar, never a bare `imports:`/`ref:` path.
7. Core concept fields are exactly `id` / `label` / `description` / `parent`; anything else is a
   declared domain extension a generic generator may ignore.
8. Every concept has exactly one owning scheme in exactly one owning domain (§9); cross-domain use
   references the owning scheme, it never redefines the concept locally.
9. No PascalCase keys, no Title-Case `domain` values, no `type: enum` dead metadata.
10. Localization is out of scope; `label`/`description` are single-language scalars today.
11. How this structure renders into any downstream representation is entirely a future generator's
    decision (Finding F-3) — not part of this contract.

---

## 16. Future work

Once both `Canonical_Ontology_Schema.md` and this document are approved, the repository undergoes
one final comprehensive audit of every existing ontology and taxonomy file against the two frozen
contracts. Only after both layers conform does work resume on completing the remaining ontology and
taxonomy content. The workflow is, in order: **Freeze Architecture → Final Repository Audit →
Complete Remaining Knowledge Layer.** Artifact generation (OWL/RDF/SHACL/property graphs/etc.)
remains a later phase, out of scope for both this step and the audit step.

---

## 17. Approval gate

This specification has been approved and is in effect:
- §§4–10, 13–15 are binding as the taxonomy authoring contract.
- §3 and §8 are binding as conventions; their open literal values (base IRI, per-domain
  prefixes) remain to be finalized in C-2, identically to the ontology contract's own open items.
- Registration, not Community Context, was the first domain migrated onto both this document and
  `Canonical_Ontology_Schema.md` together (Phases 1–4 of `Registration_Migration_Plan.md`).
  Community Context migration remains a future step.
- **`Canonical_Ontology_Schema.md` and this document together complete the architecture freeze for
  the knowledge layer.** Further work should be directed at repository conformance, ontology and
  taxonomy content completion, and knowledge quality — not at authoring additional architecture
  documents. Any genuinely new architectural concern discovered during the audit or completion
  phases is raised as an amendment to one of these two documents, not as a new one.
