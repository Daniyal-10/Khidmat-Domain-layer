# Repository Architecture Improvement Program

## Purpose
This document is the implementation roadmap that translates the Repository Architecture Report
into concrete architectural work. Its single objective is to **freeze a clean, deterministic,
scalable repository contract** — so that the remaining taxonomy and ontology work, and every
future domain, is authored once, on a stable foundation, and can later generate OWL / RDF /
RDFS / SHACL / Knowledge Graph artifacts **without repository redesign**.

This is an ontology-architecture document. It is intentionally **not** a project-management,
release-planning, sprint, or CI/CD plan. Where automation is referenced it is described only as
an architectural artifact (a schema that *defines* the freeze), never as a delivery process.

## Authority
This document is the highest-priority architectural reference for the repository's structural
evolution. All refactoring and all new domain creation must conform to it and to the frozen
contract it defines.

## Scope
Repository structure, canonical folder layout, ontology and taxonomy file schemas,
entity/relationship serialization, namespace/IRI strategy, the metadata (file-header) contract,
the reusable domain template, the machine-readable manifest, and reference integrity.

## Current Architecture Status
The repository is conceptually strong and semantically disciplined, sitting on a mechanically
inconsistent physical foundation. Governance intent is enterprise-grade; the file contract is not
yet deterministic enough for a single-code-path generator. The repository is ~70–80% complete: the
remaining work is finalization, not greenfield.

## Target Architecture Vision
A deterministic, parser-friendly, IRI-native canonical source that a single generator consumes
without per-domain special-casing. Every domain follows one frozen schema for entities,
relationships, taxonomy, constraints, and metadata, registered in one machine-readable manifest
under one namespace strategy.

---

## Freeze-First Principle (governing rule)
Because the repository is ~70–80% complete, the dominant risk is **authoring the remaining
20–30% on conventions that are about to change**, which forces a second migration.

**Rule: no new taxonomy or ontology content may be authored — in any domain — until the Freeze
Set below is locked.** Finalization of existing content and the remaining domains resumes only on
the frozen contract.

This rule reclassifies priority by *freeze-dependency*, which is distinct from a finding's
*severity*. A finding can be low-severity (the repo still works today) yet freeze-blocking
(all future content depends on it). D-1 and D-2 are the clearest examples: they are severity
"Design" but are **freeze-blocking** and are therefore part of the Freeze Set.

### The Freeze Set (must be locked before content authoring resumes)
| ID | What it freezes | Severity | Freeze-blocking |
|----|-----------------|----------|-----------------|
| C-1 | Entity + relationship serialization (incl. data-property **xsd datatype** typing) | Critical | Yes |
| C-2 | Namespace / IRI strategy (base IRI + per-domain prefix + local-name rule) | Critical | Yes |
| C-3 | Reference-resolution contract (how `*_ref` / cross-file links are expressed) | Critical | Yes |
| R-1 | Machine-readable manifest (catalog) + cross-domain import DAG | Required | Yes |
| R-3 | File-header / metadata contract | Required | Yes |
| R-4 | Taxonomy record shape | Required | Yes |
| D-1 | Canonical module template + its meta-schema artifact | Design (freeze-blocking) | Yes |
| D-2 | Canonical folder layout (no flat vs. nested divergence) | Design (freeze-blocking) | Yes |

Everything outside the Freeze Set (R-2 generalization, D-3–D-7 housekeeping, all of Phase 4) may
proceed **after** the freeze and does not gate content authoring.

### Deferred deliberately (do NOT do now)
Physical RDF/OWL/SHACL emission (F-3), provenance/XAI layer (F-4), version-IRI/deprecation
policy (F-5), and legacy-domain migration (F-1) are correctly deferred. They depend on a frozen
contract and add no value before it exists. Building them now would be over-engineering.

---

## Success Criteria
- One enforced entity/relationship/taxonomy serialization schema across all domains.
- One IRI strategy (base URI + per-domain CURIE prefix + deterministic local names).
- One machine-readable manifest describing domains, file roles, and the import DAG.
- One mandatory file-header/metadata contract.
- Data properties carry explicit `xsd` datatypes.
- Zero dangling references.
- One folder layout; no flat/nested divergence.
- A published meta-schema artifact that *defines* conformance (independent of any CI that runs it).

## Implementation Principles
- **Schema over convention** — the contract is a written, versioned schema artifact, not prose.
- **IRI-first identity** — every class, property, and individual has a stable IRI.
- **Determinism** — the repository parses on a single code path.
- **Bounded contexts** — preserve existing single-ownership and acyclic cross-domain rules.
- **Freeze before finalize** — lock the contract before authoring remaining content.

## Migration Order
Standardize foundations first so dependents migrate onto stable ground:
1. **Shared Human / Shared Risk** — foundational base models.
2. **Community Context** — flagship template source (but correct its file-path namespaces to CURIEs).
3. **Registration** — depends on shared concepts.
4. **Needs Assessment / Case Management** — legacy, heaviest refactor.
5. **Beneficiary Lifecycle / Verification Operations** — operational, multi-context.
6. **Consent & Privacy** — cross-cutting; stabilize once subject IRIs are firm.
7. **Programs / Support Delivery / Volunteer Operations** — placeholders; activate last.

---

## Implementation Phases

Each finding lists only ontology-relevant fields: the problem, the architectural goal, why it
matters, its generation impact, dependencies, steps, acceptance, the actually-affected domains,
and whether it is in the Freeze Set.

### Phase 1 — Critical (Freeze Set)

#### C-1 — Entity & relationship serialization schema
- **Problem:** No single entity schema. Domains variously use a list keyed by `id`, a map keyed by PascalCase names (`beneficiary-lifecycle`, `needs-assessment`, `consent-and-privacy`), or a list keyed by `name` under a redundant wrapper (`case-management`). Relationship shapes diverge similarly.
- **Goal:** Freeze one serialization for `entities.yaml` and `relationships.yaml`, including a mandatory **data-property datatype clause**: every data property declares an `xsd` datatype (`xsd:string`, `xsd:dateTime`, `xsd:integer`, …). Object properties declare domain, range, and (where applicable) inverse and cardinality in one uniform form.
- **Why:** Without this, no generator runs on a single code path; and without xsd typing, RDF/OWL data-property ranges cannot be emitted.
- **Generation impact:** OWL/RDF/SHACL — blocker. KG — non-deterministic load.
- **Dependencies:** None. **Freeze Set:** Yes.
- **Steps:** Define canonical entity/relationship/data-property schema → publish as the meta-schema artifact (see D-1) → migrate domains per Migration Order.
- **Acceptance:** All `entities.yaml`/`relationships.yaml` share identical structure; all data properties carry xsd datatypes.
- **Affected domains:** all active domains (legacy map-keyed and `name`-keyed domains change most).

#### C-2 — Namespace / IRI strategy
- **Problem:** No base IRI anywhere. Two conflicting "namespace" conventions coexist: CURIE URIs (`khidmat:needs-assessment:core`) in some domains and **relative file paths** (`shared/taxonomy/organisations.yaml`) in the flagship `community-context`.
- **Goal:** Adopt the CURIE convention repository-wide; define base IRI + per-domain prefix + deterministic local-name rule; specify class-vs-individual minting. Correct `community-context` off file-path namespaces.
- **Why:** RDF/RDFS/OWL are IRI-native; without stable IRIs there are no stable subjects for reasoning, KG load, XAI, or exchange.
- **Generation impact:** OWL/RDF/SHACL/KG — blocker.
- **Dependencies:** C-1 (stable identity tokens first). **Freeze Set:** Yes.
- **Steps:** Define base IRI and minting rules → standardize on CURIEs → convert all `namespaces:` blocks and `*_ref` targets.
- **Acceptance:** Every class, property, and individual resolves to one stable IRI; zero file-path namespaces remain.
- **Affected domains:** all; `community-context`, `needs-assessment`, `consent-and-privacy`, `verification-operations` carry existing namespace blocks to reconcile.

#### C-3 — Reference-resolution contract & integrity
- **Problem:** Hard references to non-existent paths: `community-context/ontology/entities.yaml` points to `ontology/attributes.yaml` (absent) and to `shared/human-model/ontology/entities.yaml` (no such subfolder).
- **Goal:** Define how cross-file/cross-domain references are expressed (CURIE + fragment, resolved via the manifest) and repair all existing dangling links.
- **Why:** Resolvers either fail or behave non-deterministically on broken links; if the flagship pattern is propagated, the broken links become canonical.
- **Generation impact:** OWL import graph / RDF / SHACL — high.
- **Dependencies:** C-2 (references resolve to IRIs), R-1 (manifest resolves them). **Freeze Set:** Yes.
- **Steps:** Define the reference form → fix `community-context` links → align all `*_ref` targets to the frozen form.
- **Acceptance:** Zero dangling references; every reference resolves via the manifest.
- **Affected domains:** `community-context` (known breaks); audit all for `*_ref`.

### Phase 2 — Required

#### R-1 — Machine-readable manifest (Freeze Set)
- **Problem:** The only indices are markdown. No root catalog declares domains, file roles, or the cross-domain import DAG (that DAG currently lives only as prose in `ARCHITECTURE.md`).
- **Goal:** Author one machine-readable `catalog` at the repository root: domains, their files and roles (entities/relationships/constraints/taxonomy/reasoning), maturity, and the explicit import DAG.
- **Why:** Generators need a deterministic entrypoint instead of globbing and guessing roles; it is also the basis for `owl:imports`.
- **Generation impact:** OWL/RDF/SHACL — blocker for repo-wide parsing.
- **Dependencies:** None. **Freeze Set:** Yes (new domains must register here).
- **Steps:** Design manifest schema → author it for current domains → make registration part of the domain template.
- **Acceptance:** The whole repository is parseable starting solely from the manifest; the DAG is represented and acyclic.
- **Affected domains:** repository-level (all domains referenced).

#### R-2 — Uniform OWL-mapping convention + SHACL source layer
- **Problem:** `owl_mapping` exists only in `community-context`; no SHACL source exists anywhere.
- **Goal:** Make the `owl_mapping` annotation and a `shacl-shapes` source slot part of the frozen template so every constraint-bearing file carries them uniformly. Centralize mapping *rules* in the (future) generator rather than hand-authoring OWL fragments per domain.
- **Why:** Today OWL/SHACL generation is possible for ~1 of ~8 domains.
- **Generation impact:** OWL — blocker for full-repo; SHACL — blocker for validation.
- **Dependencies:** C-1, D-1. **Freeze Set:** No (annotation *slot* is frozen via D-1; populating it is post-freeze). Boundary: R-2 defines the **mapping source**, F-3 performs the **emission**.
- **Steps:** Add `owl_mapping` + `shacl-shapes` to the template → backfill constraint files after freeze.
- **Acceptance:** Every constraint-bearing file exposes the mapping/shape slots defined by the template.
- **Affected domains:** all constraint-bearing domains.

#### R-3 — File-header / metadata contract (Freeze Set)
- **Problem:** Version metadata is inconsistent — quoted string, unquoted semver, a differently-named key (`ontology_version`), comment-only, or absent. No `owl:versionIRI` concept.
- **Goal:** One mandatory header schema as YAML keys (never comments): `version`, `domain`, `file`, `status`, `owl_version_iri`.
- **Why:** Tooling cannot deterministically key off metadata for provenance or versioning.
- **Generation impact:** OWL/RDF metadata — medium.
- **Dependencies:** None. **Freeze Set:** Yes.
- **Steps:** Define header schema → normalize all files to it.
- **Acceptance:** 100% of ontology/taxonomy files carry the identical header contract.
- **Affected domains:** all (comment-only headers in `shared/*` and absent headers in `beneficiary-lifecycle` change most).

#### R-4 — Taxonomy record shape (Freeze Set)
- **Problem:** Taxonomy values appear as list-of-single-key-maps (`- metropolitan_center: "…"`), nested category dicts, and `id`/`description` records; metadata sits in comments in some files, YAML keys in others.
- **Goal:** One record shape (`- id: … / label: … / description: …`) suitable for mechanical emission of `skos:Concept` / `owl:NamedIndividual`.
- **Why:** List-of-single-key-maps is the most parser-hostile form and blocks deterministic taxonomy emission.
- **Generation impact:** OWL/RDF taxonomy — high.
- **Dependencies:** None. **Freeze Set:** Yes.
- **Steps:** Define record schema → migrate taxonomy files.
- **Acceptance:** Uniform taxonomy serialization repository-wide.
- **Affected domains:** all taxonomy-bearing domains (`community-context`, `registration`, `shared`, `verification-operations`).

### Phase 3 — Design

#### D-1 — Canonical module template + meta-schema **(freeze-blocking)**
- **Problem:** The 8-file module split is aspirational; four of its files (`data-properties`, `annotation-properties`, `shacl-shapes`, `reasoning-mappings`) do not exist even in the flagship, and nothing enforces the layout.
- **Goal:** Freeze the module template and publish it as a **meta-schema artifact** (JSON Schema / SHACL-over-YAML) that *defines* conformance. Keep `reasoning-mappings` as the ontology↔rules bridge but locate reasoning rules in a top-level `reasoning/` folder so the ontology/reasoning separation stays clean.
- **Why:** This is the reusable template every future domain follows; the project goal makes it freeze-blocking despite its "Design" severity.
- **Generation impact:** Foundational — determines whether all later generation is single-code-path.
- **Dependencies:** C-1 (schema content). **Freeze Set:** Yes.
- **Steps:** Author the meta-schema → include header (R-3), manifest registration (R-1), mapping slots (R-2), datatype clause (C-1) → designate it the template for all new domains.
- **Acceptance:** A new domain scaffolded from the template validates against the meta-schema with no edits.
- **Affected domains:** template-level; applies to all future and migrated domains.

#### D-2 — Canonical folder layout **(freeze-blocking)**
- **Problem:** Flat `ontology.yaml` (`case-management`, `needs-assessment`, `beneficiary-lifecycle`, `consent-and-privacy`) coexists with nested `ontology/` folders (`registration`, `community-context`, `verification-operations`).
- **Goal:** One folder layout for every domain, matching the D-1 template.
- **Why:** Folder-role determinism is required before the manifest and generator can address files uniformly; freeze-blocking for the same reason as D-1.
- **Generation impact:** OWL/RDF/SHACL — high (addressing files by role).
- **Dependencies:** D-1. **Freeze Set:** Yes.
- **Steps:** Define layout in the template → migrate flat domains to nested (this is executed with F-1 for legacy domains, but the layout itself is frozen now).
- **Acceptance:** No flat domain structures remain; all domains match the template layout.
- **Affected domains:** the four flat domains above.

#### D-3 — Governance file standardization
- **Problem:** Governance is three differently-named scattered files (`community-context-governance.md`, `risk-domain-governance.md`, `health-conditions-governance.md`).
- **Goal:** Standardize to `<domain>/governance.md`, co-located to preserve bounded-context locality.
- **Why:** Deterministic discoverability without centralizing governance away from its domain.
- **Generation impact:** None. **Dependencies:** None. **Freeze Set:** No.
- **Steps:** Rename/relocate → update references.
- **Acceptance:** Every domain with governance uses the standard name and location.
- **Affected domains:** `community-context`, `shared/risk`, `shared/human-model`.

#### D-4 — Discovery report standardization
- **Problem:** Only `community-context` has a discovery report, snake-cased in the domain root.
- **Goal:** `discovery/report.md` per domain.
- **Why:** Keeps the domain root clean and discoverable.
- **Generation impact:** None. **Dependencies:** None. **Freeze Set:** No.
- **Steps:** Move `community_context_discovery_report.md` → `discovery/report.md`; set the standard for future domains.
- **Acceptance:** Reports live only under `discovery/`.
- **Affected domains:** `community-context`.

#### D-5 — Root documentation into `docs/`
- **Problem:** 11 markdown files clutter the repository root alongside domain folders.
- **Goal:** Move docs into `docs/{architecture,workflows,roadmap,archive}`; keep only `README.md` at root.
- **Why:** Navigability; signals maturity. Cosmetic for tooling.
- **Generation impact:** None. **Dependencies:** None. **Freeze Set:** No.
- **Steps:** Move files → update inter-doc links.
- **Acceptance:** Root contains only domains, `docs/`, `README.md`.
- **Affected domains:** repository root only.

#### D-6 — Placeholder hygiene
- **Problem:** `_placeholder.yaml` persists in the fully-built `community-context`, confusing status detection.
- **Goal:** Small fixed placeholder metadata contract (`status: placeholder` + owned-concept list); remove placeholders on activation.
- **Why:** Prevents ambiguity about whether a domain is active or a placeholder.
- **Generation impact:** Low. **Dependencies:** None. **Freeze Set:** No (small; do with template rollout).
- **Steps:** Define placeholder schema → remove the stale `community-context/_placeholder.yaml`.
- **Acceptance:** No active domain contains a placeholder file.
- **Affected domains:** `community-context` (stale); `impact`, `programs`, `support-delivery`, `volunteer-operations`, `beneficiary-lifecycle` (valid placeholders to normalize).

#### D-7 — Preserve sound separations (invariant, not a task)
- **Status:** No change required. The taxonomy/ontology, reasoning/ontology, and lifecycle-vs-semantic-constraint separations are correct and sophisticated.
- **Goal:** Encode these as **immutable invariants** in the D-1 meta-schema so future domains cannot merge the concerns.
- **Why:** Protects modeling quality already achieved.
- **Generation impact:** Positive (supports correct reasoning). **Dependencies:** D-1. **Freeze Set:** No (preservation).
- **Acceptance:** Meta-schema rejects files that merge the separated concerns.
- **Affected domains:** template-level.

### Phase 4 — Future (do not start before the freeze)

#### F-1 — Migrate legacy domains to the frozen template
- **Goal:** Bring `case-management`, `beneficiary-lifecycle`, `needs-assessment`, `consent-and-privacy` onto the frozen schema and layout.
- **Why:** Full-repository consistency.
- **Dependencies:** C-1, C-2, C-3, R-1, R-3, R-4, D-1, D-2 (the entire Freeze Set). **Freeze Set:** No.
- **Acceptance:** 100% domain conformance to the template.

#### F-2 — Meta-schema execution (validation harness)
- **Goal:** Run the D-1 meta-schema and reference-integrity checks automatically (the *execution* of the artifact authored in D-1/C-3, not a CI/CD process design).
- **Why:** Converts the frozen contract from documented to guaranteed; would have caught C-3.
- **Dependencies:** D-1. **Freeze Set:** No.
- **Acceptance:** Non-conforming files and broken references are rejected mechanically.

#### F-3 — RDF/OWL/SHACL emission pipeline
- **Goal:** A `build/` step producing `.ttl`/`.owl`/SHACL from the YAML source.
- **Why:** Enables automated consumption by GraphDB / Stardog / TopBraid.
- **Dependencies:** R-1, R-2 (+ frozen schema). **Freeze Set:** No.
- **Acceptance:** Emitted artifacts pass W3C validation and are reproducible from source.

#### F-4 — Provenance / XAI layer
- **Goal:** A PROV-O-aligned provenance annotation on `reasoning-mappings` linking each reasoning output to the rule + axiom + source concept.
- **Why:** Explainable AI and traceability.
- **Dependencies:** C-2. **Freeze Set:** No.
- **Acceptance:** Reasoning outputs trace back to source concepts.

#### F-5 — Ontology versioning & deprecation policy
- **Goal:** `owl:versionIRI` per release, `owl:deprecated` deprecation policy, per-ontology changelog.
- **Why:** Needed once external consumers depend on stable IRIs.
- **Dependencies:** C-2, R-3. **Freeze Set:** No.
- **Acceptance:** Releases carry stable version IRIs and changelogs.

---

## Verification
Verification is defined by architectural artifacts, not process:
- The **meta-schema artifact** (D-1) is the definition of "frozen"; conformance is checked against it.
- **Reference integrity** (C-3) resolves every reference through the manifest (R-1).
- **Single-code-path parse:** the repository loads from the manifest with no per-domain branching.
- Datatype coverage: every data property declares an `xsd` datatype.

## Completion Criteria
The freeze is complete when the Freeze Set (C-1, C-2, C-3, R-1, R-3, R-4, D-1, D-2) is locked, the
meta-schema artifact is published, zero references dangle, and the repository parses on a single
code path. Only then does remaining taxonomy/ontology authoring — and Phase 4 — resume. The program
is complete when the repository is a canonical, machine-consumable RDF/OWL/SHACL source requiring no
non-deterministic logic for generation.
