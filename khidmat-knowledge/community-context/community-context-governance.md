# Khidmat Community Context Taxonomy — Governance and Documentation

**Authority:** Knowledge Layer Architect
**Source:** Companion governance document for `community-context/taxonomy/*.yaml`
**Purpose:** Boundary enforcement rules, cross-domain relationship patterns, and alignment contracts for the Community Context Domain. Written as a standalone governance document to preserve the taxonomy files' flat, mechanical schema while enforcing strict single-ownership principles (ADR-008).

---

## Boundary Enforcement Rules

These rules govern exactly what each taxonomy file in the Community Context Domain may and may not define, codifying the resolutions of architecture audits C1 through C4.

### 1. Physical Assets and Infrastructure (C1)
*   `transportation.yaml` **exclusively** owns all route, edge, and transit node classifications (e.g., roads, bridges, waterways, rail networks, airports).
*   `infrastructure-types.yaml` **exclusively** owns built infrastructure point/node facilities that are not transportation-related (e.g., health, education, water extraction, energy, markets, administrative buildings, community centers).
*   `community-assets.yaml` **exclusively** owns non-infrastructural, natural community resources (e.g., arable land, forests, grazing land, fishing grounds). It must not model built infrastructure.

### 2. Accessibility vs. Physical Environment (C2)
*   `accessibility.yaml` is the **sole canonical owner** of access-mode constraints and physical accessibility modes (how a location is reached).
*   `physical-environment.yaml` strictly owns pure physical geography (terrain, climate, land use, water systems) and must not model logistics constraints or access modes.

### 3. Geographic Hierarchy vs. Settlement Formality (C3)
*   `geographic-hierarchy.yaml` owns pure spatial granularity levels (e.g., country, district, village, neighbourhood). It must not include settlement forms.
*   `settlement-types.yaml` is the **sole canonical owner** of settlement formality (e.g., informal settlements, camps, planned settlements). A camp or informal settlement occupies a hierarchy level from `geographic-hierarchy.yaml` but defines its form via `settlement-types.yaml`.

### 4. Local vs. Shared Organizations (C4)
*   `local-organizations.yaml` constitutes a genuinely separate concept space from `shared/taxonomy/organisations.yaml`.
*   `local-organizations.yaml` strictly models community-native, informal, or semi-formal collectives (e.g., traditional leadership, mutual aid networks, council of elders).
*   It must not model formally registered, statutory, or externally structured entities (e.g., hospitals, state government offices, international NGOs). Those belong strictly to the shared taxonomy.

### 5. Exclusion of Mutable State
*   Community Context taxonomy files represent immutable semantic classification. Operational availability (e.g., emergency-only services, temporarily closed routes) represents mutable state and is strictly excluded from these taxonomies. Mutable state is modeled as an attribute of instances in the downstream ontology.

---

## Cross-Domain Relationship Patterns

### Pattern: Built Infrastructure to Shared Organizations
**Description:** How a physical facility relates to the formal organization operating it.
**Boundary Note:** `infrastructure-types.yaml` classifies the physical building (e.g., `health_facility`). It does not model the administrative entity running it. That relationship must be mapped in the ontology linking the infrastructure node to an instance of `shared/taxonomy/organisations.yaml`.

### Pattern: Local Organizations to Shared Human Model
**Description:** How individuals relate to community-native collectives.
**Boundary Note:** `local-organizations.yaml` models the *type* of collective. The membership or leadership roles of specific individuals within those collectives belong to the Shared Human Model (or Registration), mapped via ontology relationships, never hardcoded into the taxonomy.

---

## Ontology Boundary Rules

These rules govern what the `ontology/` module (entities, relationships) may not
own or originate — the ontology-layer counterpart to the taxonomy boundary rules
above. Relocated from `ontology/semantic-constraints.yaml` (`no_operational_workflows`
row) per Migration Decision D-CC2 (below), since this is a governance boundary
statement rather than a graph-structural fact about this domain's own entities.

### 6. No Operational Workflow Ownership
*   `community`, `built_infrastructure`, `natural_resource`, `transportation_network_asset`, and `local_collective` SHALL NOT directly own or originate operational workflows, case management lifecycles, or beneficiary status states.
*   There are no outbound edges from these entities to Case Management or Support Delivery workflows. Community Context provides context that those domains consume; it does not model their process.

---

## Canonical Migration Decisions (D-CC1–D-CC6)

The durable Phase-0 decisions from this domain's completed canonical migration are
recorded here (single authoritative home; the originating migration plan was a
one-time process artifact and is not retained). All were approved at their default
values.

*   **D-CC1** — The `infrastructure_organization_reference` constraint was **dropped**: it was redundant with the `built_infrastructure_operated_by_organization` relationship's own `to: shared_org:organisation` range. No information lost.
*   **D-CC2** — `collective_human_reference` was relocated to `ontology/lifecycle-constraints.yaml` (on `local_collective`); `no_operational_workflows` was relocated to §6 above.
*   **D-CC3** — The `built_vs_natural` disjoint constraint uses `property: rdf:type` (mirroring OWL's `DisjointClasses`). `geographic_area_anti_recursion` is retained as a `notes:` field on the `geographic_area_contains_*` / `community_located_in_geographic_area` relationship rows — no new constraint type was invented.
*   **D-CC4** — No `parent` conversion anywhere in this domain: none of the 12 taxonomy files nest child concepts; `infrastructure_type[*].category` is a cross-scheme tag (a permitted extension field), not embedded hierarchy.
*   **D-CC5** — The `namespaces:` cross-domain targets (`shared_org`, `shared_human`) are already single-owned canonical shared files; they are referenced, never redefined. No action.
*   **D-CC6** — One data property per scheme: **D-CC6a** for cumulative dimensions (cardinality `{min:0, max:unbounded}`); **D-CC6b** for mutually-exclusive alternatives (cardinality `{min:0, max:1}` each, plus a `mutually_exclusive` `semantic-constraints.yaml` row). A Value Object (Ontology §17) was considered and rejected because these are *alternative* single-value classifications, not *co-occurring* fields.

## Content Gap Log (final status)

17 of the original 18 content-gap rows were closed mechanically by the D-CC6a/D-CC6b
decomposition. **One row remains an open content gap** — it requires domain-knowledgeable
authoring, not a migration action:

*   `transportation_network_asset.surface_condition` — **not authored**: no scheme in `taxonomy/transportation.yaml` (or elsewhere in this domain) enumerates surface-condition concepts (e.g. `passable` / `degraded` / `washed_out`). The property will be wired once that scheme is authored.
