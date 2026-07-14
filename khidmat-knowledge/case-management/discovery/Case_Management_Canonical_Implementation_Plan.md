# Case Management Canonical Implementation Plan

## 1. Final Repository Layout

Once the migration is complete, the `case-management/` directory will perfectly mirror the canonical 5-file ontology standard and the scheme-separated taxonomy layout.

```text
case-management/
├── ontology/
│   ├── entities.yaml
│   ├── data-properties.yaml
│   ├── relationships.yaml
│   ├── semantic-constraints.yaml
│   └── lifecycle-constraints.yaml
├── taxonomy/
│   ├── case_origin.yaml
│   ├── case_status.yaml
│   ├── closure_reason.yaml
│   ├── delegation_status.yaml
│   ├── objective_status.yaml
│   ├── priority_level.yaml
│   ├── referral_status.yaml
│   ├── referral_type.yaml
│   └── suspension_reason.yaml
├── reasoning/
│   └── (Reserved for future rule modeling)
└── discovery/
    ├── Case_Management_Architecture_Alignment.md
    ├── Case_Management_Business_Architecture.md
    ├── Case_Management_Business_Flow_Validation_Report.md
    ├── Case_Management_Concept_Inventory.md
    ├── Case_Management_Domain_Audit.md
    ├── Case_Management_Domain_Model_Specification.md
    ├── Case_Management_Edge_Cases.md
    ├── Case_Management_Migration_Plan.md
    ├── Case_Management_Ontology_Readiness_Review.md
    ├── Case_Management_Operational_Patterns.md
    ├── Case_Management_Repository_Gap_Report.md
    ├── Case_Management_Unknown_Unknowns.md
    └── Case_Management_Canonical_Implementation_Plan.md
```
*(Note: the legacy monolithic files `ontology.yaml` and `taxonomy.yaml` will be deleted from the root level).*

---

## 2. Legacy → Canonical Mapping

This table maps every concept currently in the legacy `ontology.yaml` and `taxonomy.yaml` to its canonical destination.

| Legacy Concept | Type | Canonical Destination | Notes |
|----------------|------|-----------------------|-------|
| `Case` | Entity | `ontology/entities.yaml` | Root aggregate. |
| `CasePlan` | Entity | `ontology/entities.yaml` | **Remains an Entity.** It must possess outbound relationship edges (to `Program`, `AssessmentFinding`), which Value Objects cannot hold per Canonical Schema §6. |
| `Referral` | Entity | `ontology/entities.yaml` | **Remains an Entity.** It requires an outbound relationship edge to `Consent`, which Value Objects cannot hold per Canonical Schema §6. |
| `FollowUp` | Entity | `ontology/data-properties.yaml` | Demoted to composite Value Object owned by `case_timeline`. |
| `CaseAssignment` | Entity | `ontology/relationships.yaml` | Refactored into Roles: `has_lead_coordinator`, `has_statutory_owner`. |
| `CaseNote` | Entity | `ontology/data-properties.yaml` | Demoted to composite Value Object owned by `case_timeline`. |
| `CaseOutcome` | Entity | `ontology/data-properties.yaml` | Demoted to a state property of the `case`. |
| `has_case_plan` | Rel | `ontology/relationships.yaml` | Retained. Edge between `Case` and `CasePlan` Entities. |
| `has_referral` | Rel | `ontology/relationships.yaml` | Retained. Edge between `Case` and `Referral` Entities. |
| `has_follow_up` | Rel | *Deleted* | Handled intrinsically by data-property nesting. |
| `has_case_assignment`| Rel | *Deleted* | Replaced by Role-based object properties. |
| `has_case_note` | Rel | *Deleted* | Handled intrinsically by data-property nesting. |
| `has_case_outcome` | Rel | *Deleted* | Handled intrinsically by scalar state properties. |
| `superseded_by` | Rel | `ontology/relationships.yaml` | Preserved for administrative merge actions. |
| `references_subject` | Rel | `ontology/relationships.yaml` | `case_primary_subject` linking to `shared_human_model:subject`. |
| `references_assessment`| Rel | `ontology/relationships.yaml` | Linked from `case_plan` to `needs_assessment:assessment_finding`. |
| `references_consent` | Rel | `ontology/relationships.yaml` | Linked from `referral` to `shared:consent`. |
| `references_intervention_type`| Rel | `ontology/data-properties.yaml` | Demoted to a `taxonomy_ref` on the `Referral` Entity. |
| `references_lifecycle` | Rel | *Deleted* | Boundary violation; Case references Identity/Subject directly. |
| `references_actor` | Rel | `ontology/relationships.yaml` | Expressed as Role relationships pointing to `shared:actor`. |
| `case_status` | Tax | `taxonomy/case_status.yaml` | Scheme extracted to distinct file; add `graduated`, `reopened`. |
| `case_plan_status` | Tax | `taxonomy/case_plan_status.yaml`| Retained as scheme to identify current vs history. |
| `referral_status` | Tax | `taxonomy/referral_status.yaml` | Scheme extracted to distinct file. |
| `referral_type` | Tax | `taxonomy/referral_type.yaml` | Scheme extracted to distinct file. |
| `case_assignment_status`| Tax | *Deleted* | Replaced by Role temporal tracking. |
| `priority_level` | Tax | `taxonomy/priority_level.yaml` | Scheme extracted to distinct file. |
| `case_origin` | Tax | `taxonomy/case_origin.yaml` | Scheme extracted to distinct file. |
| `case_outcome` | Tax | *Deleted* | Merged into `closure_reason.yaml` to simplify resolution tracking. |
| `administrative_closure_reason`| Tax | `taxonomy/closure_reason.yaml`| Consolidated closure taxonomy scheme. |

---

## 3. File Dependency Graph

The implementation must proceed in the following order to ensure cross-references are valid at the time of creation:

**Step 1: Taxonomy Schemes (`taxonomy/*.yaml`)**
*Reasoning:* Data properties rely heavily on `taxonomy_ref`. The taxonomy schemes must exist first to provide valid target IDs.

**Step 2: Entities (`ontology/entities.yaml`)**
*Reasoning:* The root context. We only have one (`case`), but it must exist before relationships or properties can bind to it. (Note: this file is already authored).

**Step 3: Relationships (`ontology/relationships.yaml`)**
*Reasoning:* Object properties representing external references and Roles must be established before we define constraints over them.

**Step 4: Data Properties (`ontology/data-properties.yaml`)**
*Reasoning:* This is the largest and most complex file. It will define the `case_plan`, `timeline`, and `referrals` as composite Value Objects. It depends on `entities.yaml` for its `domain` key, and `taxonomy/` for its `taxonomy_ref` keys.

**Step 5: Semantic Constraints (`ontology/semantic-constraints.yaml`)**
*Reasoning:* Must be authored last (excluding lifecycle), as it binds strictly to the IRIs generated in Steps 2-4.

**Step 6: Lifecycle Constraints (`ontology/lifecycle-constraints.yaml`)**
*Reasoning:* Sits at the top of the stack, describing state machine transitions utilizing the vocabulary generated in prior steps.

---

## 4. Migration Checklist

### Phase 1: Taxonomy Generation
- [ ] Create `taxonomy/case_status.yaml` (includes `graduated`, `reopened`).
- [ ] Create `taxonomy/priority_level.yaml`.
- [ ] Create `taxonomy/case_origin.yaml`.
- [ ] Create `taxonomy/referral_status.yaml`.
- [ ] Create `taxonomy/referral_type.yaml`.
- [ ] Create `taxonomy/closure_reason.yaml`.
- [ ] Create `taxonomy/suspension_reason.yaml` (New).
- [ ] Create `taxonomy/delegation_status.yaml` (New).
- [ ] Create `taxonomy/objective_status.yaml` (New).

### Phase 2: Ontology Structural Authoring
- [x] Author `ontology/entities.yaml` (Complete).
- [ ] Author `ontology/relationships.yaml` (Map Roles and Outbound Dependencies).
- [ ] Author `ontology/data-properties.yaml` (Map `CasePlan`, `Timeline`, `Referral` as Value Objects using `fields:`).

### Phase 3: Ontology Logic Authoring
- [ ] Author `ontology/semantic-constraints.yaml` (Apply the 7 invariants from the Domain Specification).
- [ ] Author `ontology/lifecycle-constraints.yaml` (Model decades-long timeline behavior).

### Phase 4: Validation & Cleanup
- [ ] Ensure all references in the new files resolve properly.
- [ ] Execute Legacy File Retirement Plan (Delete monolithic root files).

---

## 5. Validation Gates

After **Phase 1 (Taxonomy)**:
- *Gate 1:* Verify `Canonical_Taxonomy_Schema.md` compliance. Every file must have the correct headers and use the `(scheme_id, concept_id)` resolution pattern.

After **Phase 2 (Structural Ontology)**:
- *Gate 2:* Verify `Canonical_Ontology_Schema.md` compliance. Specifically, verify ADR-023: Ensure no new entities crept in, and verify the `fields:` array properly models the `CasePlan` and its children as Value Objects.
- *Gate 3:* Verify acyclic dependency compliance. Ensure cross-domain references use CURIE format and do not cycle back to Case Management.

After **Phase 3 (Logic)**:
- *Gate 4:* Ensure constraints map 1:1 with the 7 invariants listed in `Case_Management_Domain_Model_Specification.md`.

---

## 6. Legacy File Retirement Plan

The monolithic legacy files (`ontology.yaml`, `taxonomy.yaml`) must NOT be deleted until:
1. Every new file in `ontology/` and `taxonomy/` has passed the Validation Gates.
2. A direct grep search confirms that there are no internal cross-references still pointing to the legacy monolithic files.
3. The new files have been committed to source control.

Once confirmed, the files `case-management/ontology.yaml` and `case-management/taxonomy.yaml` will be safely permanently deleted.

---

## 7. Git Migration Strategy

To ensure a safe, reviewable, and reversible migration, use the following commit strategy:

**Commit 1: "chore(case-management): Finalize discovery and business architecture"**
- Commits all the markdown files generated during the Business Discovery phase.

**Commit 2: "feat(case-management): Extract taxonomy into canonical multi-file schemes"**
- Creates the `taxonomy/` folder and its 9 independent `.yaml` files.
- (Does not yet touch ontology files).

**Commit 3: "feat(case-management): Establish structural ontology (Entities & Relationships)"**
- Commits `ontology/entities.yaml` and `ontology/relationships.yaml`.

**Commit 4: "feat(case-management): Demote fact-bundles to Value Objects (ADR-023)"**
- Commits `ontology/data-properties.yaml` containing the massive nested `CasePlan` and `Timeline` definitions.
- *Review Checkpoint:* This is the most complex commit and should be reviewed independently to ensure ADR-023 was correctly applied.

**Commit 5: "feat(case-management): Apply semantic and lifecycle invariants"**
- Commits the two constraints files.

**Commit 6: "refactor(case-management): Retire legacy level-1 YAML monoliths"**
- Deletes `case-management/ontology.yaml` and `case-management/taxonomy.yaml`.
- *Rollback Point:* If the new implementation breaks external dependencies, we can revert this specific commit to restore the legacy files while debugging.
