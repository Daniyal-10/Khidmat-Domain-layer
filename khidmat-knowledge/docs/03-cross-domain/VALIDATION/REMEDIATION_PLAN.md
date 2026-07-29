# Remediation Plan

This plan details the required corrective actions to resolve the findings identified during the independent validation of the `03-cross-domain` documentation layer. Do not modify the original discovery files to make them fit the harmonization; you must modify the harmonization to fit the discovery.

---

## Remediation Task: REM-01 (Addresses CRIT-01)
* **Problem:** `SHARED_CONCEPT_CATALOG.md` contains explicit ontology implementation terminology (`Foundation:Identity` as a "class").
* **Discovery Evidence:** None. Stage 5 constraints explicitly forbid this.
* **Why it matters:** It violates the strict separation between business architecture and software/ontology implementation, artificially constraining Stage 6.
* **Recommended Correction:** Remove the word "class" and the syntax `Foundation:Identity`. Rewrite the section to state, in pure business terms, that Identity is a highly stable, universally utilized concept that should anchor downstream knowledge models.
* **Affected Documents:** `SHARED_CONCEPT_CATALOG.md`
* **Priority:** Critical

---

## Remediation Task: REM-02 (Addresses MAJ-01)
* **Problem:** The harmonization layer claims the Evidence lifecycle is universally immutable.
* **Discovery Evidence:** `case-management/12-domain-invariants.md` shows that evidence of vulnerability is explicitly point-in-time and expires.
* **Why it matters:** If built as immutable, the system will permanently trap individuals in historical vulnerability states, violating case management principles.
* **Recommended Correction:** Revise the Evidence entry to explicitly state that Evidence is polymorphic in its validity periods. Contrast Registration (immutable birth records) with Case Management (expirable vulnerability evidence).
* **Affected Documents:** `SHARED_CONCEPT_CATALOG.md`
* **Priority:** Major

---

## Remediation Task: REM-03 (Addresses MAJ-02)
* **Problem:** Canonical ownership of "Location" is assigned to `organisation-partner-management` without justification.
* **Discovery Evidence:** `resource-logistics/02-boundaries.md` indicates Logistics heavily relies on and manages spatial data (warehouses, distribution points). 
* **Why it matters:** Inventing ownership where discovery is ambiguous creates artificial, unworkable dependencies.
* **Recommended Correction:** Change the canonical owner of Location to "Unresolved / Pending ADR". Explicitly document the tension between Logistics (who need operational locations) and Partner Management (who need administrative locations).
* **Affected Documents:** `CONCEPT_OWNERSHIP.md`
* **Priority:** Major

---

## Remediation Task: REM-04 (Addresses MIN-01)
* **Problem:** A reciprocal dependency regarding programmatic baselines is claimed but missing from the producer's documentation.
* **Discovery Evidence:** `accountability-evaluation/09-information-requirements.md` claims consumption; `programme-management/09-information-requirements.md` does not list production.
* **Why it matters:** Handoffs fail if the producer does not know they are required to produce the data.
* **Recommended Correction:** Update `CROSS_DOMAIN_DEPENDENCIES.md` to flag the Baseline data handoff as a "Missing Producer Dependency" and explicitly note that Programme Management does not currently recognize this obligation.
* **Affected Documents:** `CROSS_DOMAIN_DEPENDENCIES.md`
* **Priority:** Minor

---

*Note: Execution of this plan must be verified before the repository can achieve full certification.*
