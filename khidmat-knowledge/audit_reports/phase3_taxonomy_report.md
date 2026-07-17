# Phase 3 Taxonomy Certification Report

## Finding 1
**Title:** Canonical Naming Mismatch in Case Management
**Severity:** High
**Evidence:** `case-management/taxonomy/` files (e.g., `case_origin.yaml`, `case_status.yaml`, `closure_reason.yaml`) use underscores in filenames. All other domains (e.g., `beneficiary-lifecycle/taxonomy/engagement-stage.yaml`, `programs/taxonomy/eligibility-and-enrollment.yaml`) use hyphens.
**Impact:** Automated tooling, cross-domain references, and namespace resolution might fail or require special casing due to inconsistent filename separators, breaking canonical standards.
**Recommendation:** Rename all `.yaml` files in `case-management/taxonomy/` to use hyphens (e.g., `case-status.yaml`, `closure-reasons.yaml`) and update all inbound references to match.
**Release Impact:** Blocks Phase 3 completion until resolved.

## Finding 2
**Title:** Lack of Hierarchical Depth in Organisations Taxonomy
**Severity:** Medium
**Evidence:** `shared/taxonomy/organisations.yaml` contains a flat list of 8 organisation types without capturing capacity models, accountability chains, or sector alignments.
**Impact:** Future domains like Programs and Support Delivery will not be able to adequately route, partner, or measure capacity based on this simplistic categorisation.
**Recommendation:** Expand `organisations.yaml` to include hierarchical structures (Sector -> Type -> Subtype) and conceptual relationships defining accountability and scale.
**Release Impact:** Can be deferred to Phase 4, but structural changes are recommended before wider adoption.

## Finding 3
**Title:** Missing Taxonomy Structure in Consent and Privacy Domain
**Severity:** Low
**Evidence:** The `consent-and-privacy` directory contains an `ontology.yaml` directly in the root but lacks a `taxonomy/` directory for consent types, scopes, or durations.
**Impact:** Causes structural inconsistency across domains. Without a defined taxonomy, components cannot reference standard consent states.
**Recommendation:** Create `taxonomy/consent-types.yaml` and `taxonomy/consent-status.yaml` once the domain is moved out of the placeholder phase.
**Release Impact:** Acceptable as a placeholder for Phase 3; flag for resolution when the domain is built out.
