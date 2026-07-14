# Case Management Architecture Alignment Review

## Objective
To compare the finalized `Case_Management_Domain_Model_Specification.md` against the repository's governing architecture (`Canonical_Ontology_Schema.md` and `Canonical_Taxonomy_Schema.md`) to ensure zero structural drift before YAML authoring begins.

---

### 1. Does the current Case Management model fit the canonical ontology schema?
**Yes, perfectly.**
The Case Management Domain Model Specification was explicitly designed to test and exercise the recently proposed ADR-023 amendments (Value Objects, Roles, and Runtime Objects). 
- `Case` and `CasePlan` fit the strict definition of `entities.yaml` (independent lifecycle).
- `Referral`, `CaseNote`, and `FollowUp` perfectly fit the `data-properties.yaml` `fields:` block as **Value Objects** (§17).
- `StatutoryOwner` and `LeadCoordinator` perfectly fit the **Roles** paradigm (§18), requiring no standalone entities.
- `Escalation` and `ReviewDecision` align with the **Runtime Objects** boundary (§19), staying out of the ontology entirely.

### 2. Are any canonical patterns missing?
From a structural modeling perspective, no patterns are missing. The domain model captures everything needed to populate the 5 canonical ontology files (`entities.yaml`, `data-properties.yaml`, `relationships.yaml`, `semantic-constraints.yaml`, `lifecycle-constraints.yaml`) and the `taxonomy/` schemes.

### 3. Are there repository conventions that the domain must follow?
When authoring begins, Case Management must strictly adhere to:
- **File Structure:** The legacy `ontology.yaml` and `taxonomy.yaml` monolithic files must be deleted and replaced with the fixed 5-file ontology layout and specific taxonomy scheme files.
- **Header Standards:** All YAML files must use the mandatory top-level keys (`version`, `domain`, `file`, `status`).
- **CURIE References:** Cross-domain references (e.g., to `Shared Human Model`, `Programs`) must use the `prefix:id` format (e.g., `shared_human_model:subject`) and be registered in the manifest.
- **Hierarchy:** Class and concept hierarchies must use the `parent` key. The `subtypes` array is prohibited.
- **Cardinality:** Must use the `{min, max}` object pattern, abandoning old descriptors like `one_to_many`.
- **Taxonomy Naming:** Taxonomy concepts must follow the `(scheme_id, concept_id)` uniqueness scope.

### 4. Does Case Management require extensions to the canonical schema?
**No.** The canonical schema (specifically the ADR-023 amendments) was built exactly for complex orchestrators like Case Management. No new YAML affordances or schema extensions are required.

### 5. Would implementing the current ontology violate repository architecture?
- **If we implemented the *old* `ontology.yaml`:** Yes, it would grossly violate the architecture (causing Entity Explosion and violating the 5-file layout).
- **If we implement the *new* Domain Model Specification:** No, it will be 100% compliant with the canonical architecture.

---

### 6. Gap Analysis

| Feature | Canonical Schema Requirement | Case Management Domain Model Specification | Gap Status |
|---------|------------------------------|--------------------------------------------|------------|
| **Entity Definition** | `entities.yaml` (ID, Description, Parent) | `Case`, `CasePlan` defined as root aggregates. | **Aligned** |
| **Fact-Bundles** | Value Objects via `fields:` in `data-properties.yaml` (§17) | `Referral`, `CaseNote`, `TimelineEntry` designated as Value Objects. | **Aligned** |
| **Operational Accountability** | Roles defined as data-properties or relationships (§18) | `CaseAssignment` eliminated; replaced with `LeadCoordinator` and `StatutoryOwner` roles. | **Aligned** |
| **Diagnostic/Ephemeral Findings** | Runtime Objects (Excluded from Ontology) (§19) | `Escalation`, `ReviewDecision`, `Recommendation` explicitly excluded. | **Aligned** |
| **Cross-Domain Dependencies** | Acyclic DAG via CURIE references (§10) | Dependencies on `Shared`, `Needs Assessment`, and `Programs` map outward only. No cycles. | **Aligned** |
| **File Headers & Shape** | Strict YAML headers, 5-file ontology layout | *To be applied during YAML authoring phase.* | **Procedural (No conceptual gap)** |
| **Taxonomy Record Shape** | `schemes` list containing `concepts` list | *To be applied during YAML authoring phase.* | **Procedural (No conceptual gap)** |

---

## Conclusion
The Case Management Domain Model Specification is fully compatible with the repository standards. It requires no deviations or extensions from `Canonical_Ontology_Schema.md` or `Canonical_Taxonomy_Schema.md`.

**The domain is cleared for canonical YAML implementation.**
