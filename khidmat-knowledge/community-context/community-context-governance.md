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
row) per `docs/architecture/Community_Context_Migration_Plan.md` Decision D-CC2,
since this is a governance boundary statement rather than a graph-structural fact
about this domain's own entities.

### 6. No Operational Workflow Ownership
*   `community`, `built_infrastructure`, `natural_resource`, `transportation_network_asset`, and `local_collective` SHALL NOT directly own or originate operational workflows, case management lifecycles, or beneficiary status states.
*   There are no outbound edges from these entities to Case Management or Support Delivery workflows. Community Context provides context that those domains consume; it does not model their process.
