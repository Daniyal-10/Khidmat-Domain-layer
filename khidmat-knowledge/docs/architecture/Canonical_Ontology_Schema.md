# Canonical Ontology Authoring Contract

> **Phase:** FREEZE — architecture specification, awaiting review and explicit approval.
> **This document changes no ontology content.** No domain has been migrated. Community Context is
> **not** yet a reference implementation. This specification becomes the source of truth *first*;
> migration happens only after approval.
>
> **Sequencing (do not skip a step):**
> 1. ✅ Freeze architecture — *this document.*
> 2. → Review architecture — reviewer ratifies or amends the rules below.
> 3. → Migrate Community Context — first reference implementation, only after step 2.
> 4. → Validate, then migrate remaining domains.

**Purpose:** the normative authoring contract that every current and future domain's `ontology/`
module must follow. The repository is the source of truth; OWL, RDF, RDFS, SHACL, LPG/JSON-LD, and
every other representation are *generated from* it, never authored *into* it. This document exists
to eliminate architectural ambiguity *before* any ontology content is modified. When this document
and a domain file disagree (after approval), this document wins.

---

## 0. How to read this document — ratification status

Each section is tagged so the reviewer can see what is already agreed versus newly proposed:

- **[RATIFIED]** — decision already approved in prior architectural discussion; restated here for a
  single source of truth. Subject only to confirmation.
- **[PROPOSED]** — introduced by this document for approval in the review step. Not previously
  ratified. These are the sections to scrutinize most closely.

Nothing here is applied to repository content until the whole document is approved.

---

## 1. Scope

**Governed by this specification:**
- Deterministic repository / module file layout.
- `entities.yaml` serialization.
- `data-properties.yaml` serialization (the single canonical home for datatype/value properties).
- `relationships.yaml` serialization (reusable object properties).
- The single cardinality model used by both data and object properties.
- Class-hierarchy expression.
- Identifier uniqueness scope and CURIE stability (§3).
- Constraint expression as a target-neutral structure (§9).
- Namespace and cross-domain resolution conventions (structural; §10).
- Reusable predicate ownership (§11).
- Metadata / file-header conventions (structural; §12).
- The domain template (§13).

**Delegated to their own findings (this document states the *convention*, not the final values):**
- **Concrete IRI values** — the literal base IRI and per-domain prefix strings are ratified under
  Finding **C-2**. §10 fixes the *form*; C-2 fixes the *values*.
- **Full versioning / `owl:versionIRI` policy and normalization tooling** — Finding **R-3**. §12
  fixes the *header shape*; R-3 fixes the versioning policy.
- **Taxonomy-internal record shape and concept-level anchoring** — Finding **R-4**, authored as its
  own peer document, **`Canonical_Taxonomy_Schema.md` (not yet written)**. This document freezes the
  *ontology-module* contract only. Repository-wide migration cannot begin until the taxonomy peer
  document also freezes: it fixes the taxonomy record shape, taxonomy-concept identifier scope, and
  how `taxonomy_ref` resolves through the same deterministic namespace mechanism as §§10–11
  (CURIE-based, manifest-resolved) rather than as an arbitrary file path. Until then, `taxonomy_ref`
  values in this document (§5, §14) are illustrative, not frozen.
- **Entity-presence cardinality** (`cardinality_in_case`) — a distinct axis from property
  cardinality; unaddressed here, unified later.
- **Artifact generation** (OWL/RDF/SHACL/LPG emission) — Finding **F-3**. This document fixes only
  the repository-side structure; every rendering into a target vocabulary is non-normative
  (Appendix A) and belongs to the generator, never to the source files.

---

## 2. Repository & module layout — [RATIFIED]

Every domain's ontology module is a folder with a deterministic, fixed set of files:

```
<domain>/ontology/
  entities.yaml             # classes: identity, hierarchy, description, ownership
  data-properties.yaml      # datatype/value properties (canonical, single source)
  relationships.yaml        # reusable object properties, edges, inverses
  semantic-constraints.yaml # structural restrictions / graph invariants
  lifecycle-constraints.yaml# descriptive lifecycle semantics (not a generation surface)
```

Rules:
- The file set is **fixed**. A domain with no data properties or no relationships still includes the
  file as a placeholder (header + empty list + one-line note), mirroring the existing
  `shared/ontology/relationships.yaml` placeholder convention, so the module shape is deterministic.
- `attributes_ref` and any per-entity attribute-file pointer are **removed from the architecture.**
  Datatype/value properties live only in `data-properties.yaml`. There is no `attributes.yaml`.
- **Sub-modules.** A bounded context (e.g. `shared/`) may contain independently owned sub-modules
  (e.g. `shared/human-model/`, `shared/risk/`) — this is a clarification of the existing architecture,
  not a new pattern: ADR-007 and `ARCHITECTURE.md` already establish `shared/human-model/` as a
  distinct, first-class-owned concept area. Each such sub-module follows this identical `ontology/`
  layout (and `taxonomy/` layout per `Canonical_Taxonomy_Schema.md`, where the sub-module owns
  controlled vocabularies) exactly as a top-level domain does.

---

## 3. Identifier uniqueness, scope & CURIE stability — [PROPOSED]

Every serialization section below (§§4–6, §9) mints an `id`. This section fixes the one rule they
all share, so identity is decided once instead of assumed differently by each migrated domain.

**Uniqueness scope:** an `id` must be unique across **all kinds** (entity, data property,
relationship row, constraint) **within its owning domain** — not merely unique within its own file
or its own kind. Rationale: every kind mints into the *same* per-domain IRI namespace
(`<BASE>/<domain>#<local_name>`, §10); if an entity and a data property in the same domain both used
`id: status`, they would collide at the IRI level (OWL punning) with no source-level signal. Fixing
the scope now removes that failure mode before it can be authored.

- The pair **`(domain, id)`** is therefore the true identity key and must be unique **globally**
  across the repository. Two different domains *may* each mint their own `id: status` — they resolve
  to different IRIs because the domain segment differs — but a single domain may never reuse an
  `id` across its entities, data properties, relationships, or constraints.
- **Taxonomy-concept identifiers** are a distinct namespace, scoped and finalized by the peer
  **Canonical_Taxonomy_Schema.md** (§1, R-4); this document only reserves the same domain-wide,
  cross-kind uniqueness rule for taxonomy concepts so `taxonomy_ref` composes IRIs the same
  deterministic way once that peer document freezes.
- **CURIE generation is a pure function of `(domain, id)`:** `curie = "<domain_prefix>:<id>"` and
  `iri = "<BASE>/<domain>#<id>"`, where `domain_prefix` and `BASE` are the literal values C-2
  ratifies. No other input (label, file path, ordering) participates in minting.
- **Stability:** an `id` is frozen the moment it is written to a merged file. Renaming an `id` is a
  breaking change to every CURIE and reference that targets it; until a deprecation policy exists
  (Finding F-5), `id`s are treated as immutable, not merely "discouraged from changing."

---

## 4. `entities.yaml` — classes — [RATIFIED]

`entities:` is **always a YAML list**, each item keyed by `id`. Never a map. Never wrapped in a
domain root key (no `community_context:` / `case_management:` wrapper).

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | Stable snake_case local name, unique per §3. **Frozen once written.** |
| `label` | optional | Human-readable name. Present only when it adds meaning beyond `id`. |
| `description` | yes | Prose definition of the class. |
| `required` | optional | Domain-level presence expectation (boolean) — *does the domain model expect an instance of this class to exist at all*. This is a distinct axis from property **cardinality** (§7), which governs *how many values a property may hold once an instance exists*. The two are never unified. |
| `ownership_boundary` | optional | Bounded-context ownership note. Governance, not emitted. |
| `parent` | optional | Superclass `id` (§8). |

**Not permitted in entities.yaml** (each relocated to its single source of truth):
- `key_attributes` → `data-properties.yaml`.
- `attributes_ref` → deleted (concept removed).
- `external_references` → expressed as object properties in `relationships.yaml`.
- `subtypes` → deleted; hierarchy is expressed **only** by the child's `parent` (§8). The generator
  derives the inverse if needed.

The target-vocabulary rendering of each field (e.g. which field becomes `rdfs:comment` vs.
`skos:definition`) is non-normative and lives in Appendix A — it is a generator decision, not part
of the repository contract.

---

## 5. `data-properties.yaml` — datatype / value properties — [RATIFIED]

The **single canonical home** for all attribute-level (literal or coded) properties.
Property-centric: each property declares its owning class, mirroring the reusable object-property
model.

`data_properties:` is a YAML list keyed by `id`.

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | snake_case local name, unique per §3. |
| `domain` | yes | Owning entity `id`. May be a list if the property is reused. |
| `datatype` | one-of | `xsd:*` literal type (e.g. `xsd:string`, `xsd:dateTime`). |
| `taxonomy_ref` | one-of | Reference to the controlled-vocabulary concept the value is drawn from (coded property). Same-domain references are a bare local concept `id`; cross-domain references are a CURIE resolved via the manifest (§10) — never a raw file path. The exact taxonomy addressing granularity is fixed by the peer **Canonical_Taxonomy_Schema.md** (§1, R-4); this document fixes only the resolution *mechanism*. |
| `cardinality` | yes | `{ min, max }` (see §7). |
| `label` | optional | Human-readable name, only when meaningful beyond `id`. |

Rules:
- Exactly **one** of `datatype` or `taxonomy_ref` per property (mutually exclusive, jointly
  required). Every value's typing is therefore unambiguous.
- `datatype` values are real `xsd:*` tokens as YAML values — **never** free-text comments such as
  `# datatype: xsd:dateTime`. Mandatory `datatype` (or `taxonomy_ref`) on every literal property.
- Whether a `taxonomy_ref` property finally emits as a datatype property with an enumerated range or
  an object property to individuals is a **generator decision** (Appendix A); the source stays
  unambiguous either way.

---

## 6. `relationships.yaml` — reusable object properties — [RATIFIED]

`relationships:` is **always a separate YAML list** keyed by `id`. Relationships are never embedded
inside entities.

**Topology:** object properties are **reusable**. A predicate such as `located_in`, `contains`,
`represents`, `operated_by`, or `composed_of` is **one** canonical property (ownership rule: §11).
Each list row is a single directed edge (one domain→range axiom) that *uses* a reusable predicate.
The row `id` is a **row identifier only** — not a distinct property.

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | Row identifier, unique per §3. Referenced by `inverse`. Not itself a property. |
| `from` | yes | Source entity `id`. |
| `relationship` | yes | The **canonical reusable object-property** local name (e.g. `located_in`); owned per §11. |
| `to` | yes | Target entity `id` (or cross-domain CURIE, e.g. `shared_org:organisation`). |
| `cardinality` | yes | `{ min, max }` on the `to` side, per one `from` instance (see §7). |
| `inverse` | optional | The `id` of the reverse-edge row. Omit if no reverse row exists. |
| `notes` | optional | Human note. Prose "Inverse of X" statements are replaced by `inverse`. |

**Not present** (generator responsibilities — never duplicated in source):
- No `domain` / `range` fields — `from` / `to` are canonical.
- No `required` field — obligation is expressed by `cardinality.min ≥ 1`.

Cross-file integrity: the `relationship` value used here is the same property name that
`semantic-constraints.yaml` must reference (see §9).

---

## 7. Cardinality model — [RATIFIED]

One representation, used by **both** data properties and relationships:

```yaml
cardinality:
  min: <non-negative integer>
  max: <positive integer | unbounded>
```

- `max: unbounded` denotes no upper bound.
- Both `min` and `max` are always present — obligation is never implicit.
- For relationships, cardinality reads as: *for one `from` instance, how many `to` instances are
  permitted;* the inverse direction carries its own cardinality on its own row.

This model **retires** every prior vocabulary — the `one_to_one` / `one_to_many` / `many_to_many` /
`many_to_one` enum on relationships and any `"1"` scalar on properties.

How `{min, max}` renders into any target vocabulary's restriction syntax is non-normative and shown
in Appendix A — the repository contract fixes only the YAML shape above.

---

## 8. Class hierarchy — [RATIFIED]

Hierarchy is expressed **only** by a child's `parent` (§4). The reverse (`subtypes`) is never
stored; it is derivable. This keeps one direction as the single source of truth.

---

## 9. Constraints files — [RATIFIED]

- **`semantic-constraints.yaml`** expresses every constraint as a **target-neutral structure** —
  never as hand-authored OWL functional syntax, SHACL, SPARQL, or any other target vocabulary. A
  constraint row states *what* is constrained; *how* that renders into OWL/SHACL/LPG is entirely a
  generator concern (Appendix A).

  | Field | Required | Meaning |
  |-------|----------|---------|
  | `id` | yes | Constraint identifier, unique per §3. |
  | `type` | yes | The structural constraint kind (e.g. `cardinality`, `disjoint`, `required_if`, `mutually_exclusive`). The kind vocabulary is closed and extended only by amending this document. |
  | `property` | yes | The **canonical reusable property name** the constraint binds (the `relationship` value from §6, or a `data_properties` `id` from §5) — never a per-row relationship `id`. |
  | `entities` | yes | The class `id`(s) the constraint applies to. |
  | `parameters` | type-dependent | A small map of type-specific values (e.g. `{ min: 1, max: 1 }` for `type: cardinality`). Shape is defined by `type`, never free text. |

  Example — replaces the previous OWL-functional-syntax form:
  ```yaml
  - id: community_requires_geography
    type: cardinality
    property: located_in
    entities: [community, geographic_area]
    parameters: { min: 1, max: 1 }
  ```
  This is exactly equivalent in meaning to the retired form
  (`ObjectExactCardinality(1 located_in geographic_area)`), but as structured data a generator can
  render into OWL, SHACL, or an LPG constraint with no per-domain special-casing, and it introduces
  no OWL-specific syntax into the repository.

- **`lifecycle-constraints.yaml`** is descriptive lifecycle semantics keyed by `entity:`. It is not
  a generation surface and is unconstrained by §§4–7. The taxonomy/ontology, reasoning/ontology, and
  lifecycle/semantic-constraint separations are preserved.

---

## 10. Namespace & cross-domain resolution conventions — [PROPOSED] (form only; values ratified in C-2)

This section fixes the *shape* of cross-domain identity, and the deterministic *mechanism* by which
a reference resolves, so §§4–6 and §9 are unambiguous at repository scale. The literal base IRI and
per-domain prefix strings remain **deferred to C-2**.

Proposed conventions:
- **CURIE, not file paths.** Every cross-domain reference is a CURIE of the form `prefix:local_name`
  (e.g. `shared_org:organisation`). The current file-path namespace values
  (`shared_org: "shared/taxonomy/organisations.yaml"`) are the **anti-pattern C-2 removes**; they are
  documented here only as what conformance replaces.
- **Namespace block placement.** A file that references other domains declares a top-level
  `namespaces:` block mapping each `prefix` → that domain's namespace IRI. Same-domain references use
  bare local `id`s (no prefix).
- **The manifest is the authoritative resolver.** A per-file `namespaces:` block is a *local
  declaration*, never an independent source of truth: every `prefix` it uses must already be
  registered in the repository-wide manifest/catalog (Finding R-1), which is the single place that
  maps each domain to its CURIE prefix and base-IRI segment. If a per-file block and the manifest
  ever disagree, the manifest wins.
- **Acyclic cross-domain dependency (DAG) requirement, restated here.** Cross-domain references form
  a directed acyclic graph: if domain A references domain B (via CURIE, in `namespaces:`), domain B
  must not reference domain A, directly or transitively, in the same layer. This rule already governs
  the repository (`ARCHITECTURE.md`); it is restated here so the ontology contract does not depend on
  knowledge external to it. A relationship that is conceptually bidirectional across two domains is
  still expressed as two independent rows, one owned by each domain, never as a cyclic import.
- **Base IRI form (to ratify in C-2).** A single base IRI with a per-domain segment and a
  `local_name` fragment, e.g. `<BASE>/<domain>#<local_name>`. The concrete `<BASE>` (HTTP vs URN)
  and per-domain prefixes are the C-2 decision.
- **Local names are frozen at authoring.** Per §3, the `id` values in entities / data-properties /
  relationships / constraints are the permanent local names; C-2 prefixes but never renames them.

*Open decision for the reviewer/C-2:* the literal base IRI. Everything above can be approved
independently of that value.

---

## 11. Reusable predicate ownership — [PROPOSED]

§6 makes object properties reusable predicates (`located_in`, `contains`, …) rather than one
property per row. Reuse without an ownership rule produces silent collisions or accidental merges
once dozens of domains each want to use the same predicate name — this section fixes that rule.

- Every reusable predicate local name has exactly **one** canonical owning location.
- **Domain-local:** if a predicate is used only by rows within one domain's own `relationships.yaml`,
  that domain owns it; it is referenced by its bare local name within the domain, with no prefix.
- **Promoted to Shared:** the moment a predicate is used by rows in **two or more** domains, it must
  be defined once in the shared predicate vocabulary (`shared/ontology/relationships.yaml`, or a
  dedicated shared-predicates list within it) and referenced cross-domain by CURIE
  (e.g. `shared:located_in`). A domain must never mint its own copy of an already-shared predicate
  name — that would be a duplicate concept, which the repository's governance already forbids for
  entities and must forbid identically for predicates.
- **Promotion governance** is the same process already used to promote any shared concept: it is
  proposed, reviewed, and — once accepted — the originating domain's row is updated to reference the
  shared predicate instead of redefining it locally. No domain unilaterally "shares" a predicate by
  convention alone.
- **Deterministic lookup.** The manifest (Finding R-1) — or, until it exists, the
  `shared/ontology/relationships.yaml` predicate list — is the single place a domain author checks
  before naming a new predicate, to confirm it is not already shared under a different domain.

---

## 12. Metadata / file-header conventions — [PROPOSED] (shape only; policy ratified in R-3)

This section fixes the *shape* of the file header so tooling can key off it deterministically. The
full versioning and `owl:versionIRI` policy is **deferred to R-3.**

Proposed conventions:
- **Header as top-level YAML keys, never comments.** (Some current files carry `# domain: …`
  comment headers; those are non-conformant.)
- **Mandatory keys:** `version`, `domain`, `file`, `status`.
- **`status` enum:** `active | placeholder | draft | deprecated`.
- **`version` format:** one canonical form — a quoted semantic-version string, `"MAJOR.MINOR.PATCH"`
  (resolving the current quoted-vs-unquoted, `version`-vs-`ontology_version` inconsistency).
- **`owl_version_iri`:** recommended; its exact policy (per-release minting, deprecation) is R-3.

*Open decision for the reviewer/R-3:* the versioning/deprecation policy and whether
`owl_version_iri` is mandatory. The header *shape* above can be approved now.

---

## 13. Domain template — [RATIFIED shape, PROPOSED headers per §12]

The canonical skeleton a new (or migrated) domain copies. Placeholder files use empty lists.

```
<domain>/
  ontology/
    entities.yaml            # header + entities: [ ... ]
    data-properties.yaml     # header + data_properties: [ ... ]   (or [] placeholder)
    relationships.yaml       # header + namespaces: {…} + relationships: [ ... ]  (or [] placeholder)
    semantic-constraints.yaml
    lifecycle-constraints.yaml
  taxonomy/                  # controlled vocabularies (shape → Canonical_Taxonomy_Schema.md, R-4)
  reasoning/                 # domain rules (unchanged by this spec)
  governance.md              # domain governance (naming → D-3)
  discovery/report.md        # discovery report (placement → D-4)
```

Minimum conformance for a new domain: the five `ontology/` files present (placeholders allowed),
each with a §12 header, entities as list-of-`id`, data properties in `data-properties.yaml`,
relationships reusable and separate, constraints structured per §9, one cardinality model.

---

## 14. Illustrative example — not applied to any domain

Illustrative only, to make §§4–7, 9 concrete. **This is not a migrated file and has not been
written to the repository.**

```yaml
# entities.yaml
entities:
  - id: community
    label: Community
    description: >
      The central social, economic, and spatial aggregation unit.
    required: true
```
```yaml
# data-properties.yaml
data_properties:
  - id: community_id
    domain: community
    datatype: xsd:string
    cardinality: { min: 1, max: 1 }
  - id: settlement_form
    domain: community
    taxonomy_ref: settlement_form   # local taxonomy-concept id; exact addressing form fixed by
                                     # Canonical_Taxonomy_Schema.md (R-4), not by this document
    cardinality: { min: 0, max: 1 }
```
```yaml
# relationships.yaml
relationships:
  - id: community_located_in_geographic_area
    from: community
    relationship: located_in
    to: geographic_area
    cardinality: { min: 1, max: 1 }
    inverse: geographic_area_contains_community
```
```yaml
# semantic-constraints.yaml
constraints:
  - id: community_requires_geography
    type: cardinality
    property: located_in
    entities: [community, geographic_area]
    parameters: { min: 1, max: 1 }
```

---

## 15. Conformance summary (what an approved generator may assume)

1. `entities:` is a list of `id`-keyed classes; hierarchy via `parent` only.
2. All datatype/value properties live in `data-properties.yaml`, property-centric, each with a
   `domain`, exactly one of `datatype` / `taxonomy_ref`, and a `{min,max}` cardinality.
3. All object properties are reusable predicates with exactly one owning domain (§11);
   `relationships.yaml` rows are directed edges with `from` / `relationship` / `to`, `{min,max}`
   cardinality, optional `inverse` (row id).
4. One cardinality model everywhere: `{min, max}` with `max: unbounded`.
5. Every constraint in `semantic-constraints.yaml` is a target-neutral structure
   (`id` / `type` / `property` / `entities` / `parameters`) — no OWL, SHACL, SPARQL, or other target
   syntax is ever authored into the repository.
6. Every `id` is unique within `(domain, id)` across all kinds in that domain (§3); CURIEs and IRIs
   are a pure function of that pair.
7. Cross-domain references are CURIEs resolved through one manifest (§10), forming an acyclic
   dependency graph.
8. No `attributes_ref`, no `external_references` in entities, no embedded relationships, no wrapper
   root keys, no duplicate `domain`/`range`, no `required` on relationships, no `subtypes`.
9. Headers are YAML-key, per §12.
10. All OWL/RDFS/SHACL/LPG rendering rules a generator may use are non-normative and live in
    Appendix A — none of them are part of the repository contract itself.

---

## Appendix A — Non-normative generation notes

*Everything in this appendix describes how a future generator **may** render the repository's
structural facts into a target vocabulary. None of it is part of the contract in §§1–15, is never
authored by hand into any domain file, and carries no approval weight of its own — it exists only so
reviewers can see that the structural fields above are sufficient to generate from.*

**§4 `entities.yaml` fields:**

| Field | Illustrative target rendering |
|-------|-------------------------------|
| `description` | `rdfs:comment` / `skos:definition` |
| `parent` | `rdfs:subClassOf` |
| `label` | `rdfs:label` |

**§5 `data-properties.yaml` fields:**

| Field | Illustrative target rendering |
|-------|-------------------------------|
| `domain` | `rdfs:domain` |
| `datatype` | `rdfs:range` of an `owl:DatatypeProperty` |
| `taxonomy_ref` | either an enumerated-range datatype property, or an object property to
`skos:Concept` individuals — a generator decision, not fixed by the source |

**§6 `relationships.yaml` fields:**

| Field | Illustrative target rendering |
|-------|-------------------------------|
| `from` | `rdfs:domain` |
| `to` | `rdfs:range` |
| `inverse` | `owl:inverseOf` |

**§7 cardinality → target restriction (illustrative only):**

| `{min, max}` | Illustrative OWL restriction | Illustrative SHACL |
|--------------|-------------------------------|---------------------|
| `min: 1, max: 1` | `owl:cardinality 1` | `sh:minCount 1; sh:maxCount 1` |
| `min: 1, max: unbounded` | `owl:minCardinality 1` | `sh:minCount 1` |
| `min: 0, max: 1` | `owl:maxCardinality 1` | `sh:maxCount 1` |
| `min: 0, max: unbounded` | (no restriction) | (no restriction) |

**§9 constraint `type` → target rendering (illustrative only):**

A `type: cardinality` row with `property: located_in`, `entities: [community, geographic_area]`,
`parameters: { min: 1, max: 1 }` could render as the OWL functional-syntax axiom
`ObjectExactCardinality(1 located_in geographic_area)`, or as an equivalent SHACL node shape, or as
an equivalent LPG/Neo4j constraint — the repository states only the structural fact; the target
syntax is chosen entirely by the generator implementation (Finding F-3).

---

## 16. Approval gate

This specification is **not** in effect until explicitly approved. On approval:
- §§2, 4–9, 13–15 (RATIFIED) become binding immediately.
- §§3, 10–12 (PROPOSED) become binding as conventions; their open values are finalized in C-2 / R-3.
- Repository-wide migration additionally waits on the peer **Canonical_Taxonomy_Schema.md** (§1,
  R-4) reaching the same approval state.
- Only then does Community Context migration (step 3 of the sequencing banner) begin, as the first
  reference implementation validating this document.

Until approval, no ontology YAML in any domain is modified.
