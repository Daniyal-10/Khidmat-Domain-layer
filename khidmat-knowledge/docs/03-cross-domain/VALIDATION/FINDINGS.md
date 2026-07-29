# Validation Findings

This document details the discrepancies, unsupported claims, and architectural risks identified during the independent validation of the `03-cross-domain` harmonization layer against the `02-discovery` authoritative source.

## 1. Critical Findings

### CRIT-01: Ontology Terminology Leakage in Business Documentation
* **Description:** The `SHARED_CONCEPT_CATALOG.md` uses explicit ontology implementation terminology, specifically referring to `Foundation:Identity` as a "class" that anchors the ontology.
* **Evidence:** `SHARED_CONCEPT_CATALOG.md` under the Identity section. Stage 5 constraints strictly forbid OWL constructs, RDF, or classes in business architecture documentation.
* **Impact:** Blurs the line between business requirements and technical implementation, potentially constraining Stage 6 ontology engineers with premature structural dictates.
* **Recommended Action:** Remove the word "class" and the syntax `Foundation:Identity`. Rewrite to state that "Identity is a strong candidate for a core foundational concept in future ontology design."
* **Priority:** Critical

## 2. Major Findings

### MAJ-01: Invalid Generalization of Evidence Lifecycle
* **Description:** `SHARED_CONCEPT_CATALOG.md` claims that the Evidence lifecycle is universally immutable across the repository.
* **Evidence:** Cross-referencing `registration-identity/12-domain-invariants.md` and `case-management/12-domain-invariants.md` contradicts this. While birth certificates in Registration are immutable, malnutrition evidence in Case Management is highly point-in-time and explicitly expires.
* **Impact:** If the ontology models all evidence as immutable, case workers will be unable to invalidate outdated vulnerability claims, breaking core humanitarian logic.
* **Recommended Action:** Revise the Evidence definition in `SHARED_CONCEPT_CATALOG.md` to explicitly recognize polymorphic validity periods (Immutable vs. Point-in-Time).
* **Priority:** Major

### MAJ-02: Unjustified Canonical Ownership of Location
* **Description:** `CONCEPT_OWNERSHIP.md` assigns canonical ownership of "Location" to `organisation-partner-management`.
* **Evidence:** Discovery documents show `resource-logistics` heavily manages locations (warehouses, camps, delivery nodes). There is no explicit evidence that Partner Management is the canonical authority over spatial data repository-wide.
* **Impact:** Forcing ownership without evidence creates artificial dependencies and risks data fragmentation if Logistics is forced to consume locations from an HR/Partner domain.
* **Recommended Action:** Mark Location ownership as an unresolved Architectural Decision Record (ADR) or "Insufficient Evidence" rather than inventing a canonical owner.
* **Priority:** Major

## 3. Minor Findings

### MIN-01: Missing Reciprocal Dependency (Programme Baselines)
* **Description:** `CROSS_DOMAIN_DEPENDENCIES.md` maps that `accountability-evaluation` consumes baseline data from `programme-management`.
* **Evidence:** `accountability-evaluation/09-information-requirements.md` claims consumption, but `programme-management/09-information-requirements.md` does not list structured baselines as a *Produced* output.
* **Impact:** M&E expects data that Programme Management is not formally contracted to provide.
* **Recommended Action:** Note this as a "Missing Producer Dependency" in `CROSS_DOMAIN_DEPENDENCIES.md` rather than assuming the dependency is healthy.
* **Priority:** Minor

## 4. Observations

### OBS-01: Robust Abstraction of Knowledge Patterns
* **Description:** The formulation of the "Evidentiary Verification Pattern" in `KNOWLEDGE_TRANSFORMATION_PATTERNS.md` successfully synthesizes isolated discovery findings from three separate domains without distorting their original intent.
* **Evidence:** Matches workflows in `registration-identity`, `case-management`, and `organisation-partner-management`.
* **Impact:** Highly positive. This represents exactly the type of business-level harmonization expected in Stage 5.

## 5. Recommendations

### REC-01: Clarify Household Dissolution
* **Description:** While `SHARED_CONCEPT_CATALOG.md` asks the open question of how a Household splits, it does not mandate which domain should answer it.
* **Recommended Action:** Update `CONCEPT_OWNERSHIP.md` to assign responsibility for resolving the "Household split" business rule (likely to `registration-identity`).
