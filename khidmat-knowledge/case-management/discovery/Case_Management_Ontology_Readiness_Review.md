# Case Management Ontology Readiness Review

## 1. Pressure Testing the Architecture

In this final review, we subject the Case Management Business Architecture to rigorous scrutiny against common domain-driven design failure modes to ensure it is structurally sound before any YAML authoring begins.

### 1.1 Entity Explosion
- **Challenge:** Are we creating Entities for concepts that have no independent identity?
- **Analysis:** Our migration plan strictly addressed this by demoting `Referral`, `FollowUp`, `CaseNote`, and `CaseOutcome` from Entities to Value Objects bound to the `CasePlan` or `CaseTimeline`.
- **Verdict:** PASSED. The core entities are strictly limited to `Case` and `CasePlan`.

### 1.2 Hidden Aggregates
- **Challenge:** Are multiple distinct concepts hiding inside one massive entity?
- **Analysis:** A `Case` could easily become a dumping ground. However, by cleanly separating the `CasePlan` (the strategy) from the `Timeline` (the history) and making them distinct, we avoid a hidden aggregate. The `Case` acts as the root aggregate coordinating these parts.
- **Verdict:** PASSED.

### 1.3 Cyclic Ownership
- **Challenge:** Do domains own each other in a circle?
- **Analysis:** Case Management points *outward* to the `Shared` domain for `Subject`, to `Needs Assessment` for findings, and to `Programs` for constraints. None of these domains point back to Case Management to define their core entities.
- **Verdict:** PASSED. The DAG (Directed Acyclic Graph) rule is preserved.

### 1.4 Duplicate Concepts & Ownership Violations
- **Challenge:** Is Case Management trying to own something it shouldn't?
- **Analysis:** We explicitly defined `LeadCoordinator` and `StatutoryOwner` as Roles on `Actor` (owned by Shared), preventing the creation of a duplicate "CaseWorker" entity. We explicitly barred mass disaster cases, deferring to Community Context.
- **Verdict:** PASSED.

### 1.5 Boundary Leaks
- **Challenge:** Are external details leaking into Case Management?
- **Analysis:** Funding logic could leak in. We prevented this by creating a boundary state (`Suspended_Due_To_Funding`) that references the Program domain without recreating budget rules inside Case Management.
- **Verdict:** PASSED.

### 1.6 Incorrect Value Objects
- **Challenge:** Did we demote something to a Value Object that actually needs to be referenced independently by other domains?
- **Analysis:** Is a `Referral` ever queried independently of a Case? Yes, Support Delivery needs to see the Referral to act on it. However, the `Referral` acts as a *message* (or Event) passed between domains, not a permanent structural Entity. Per ADR-023, it is safe as a Value Object/Event payload originating from the Case.
- **Verdict:** PASSED.

### 1.7 Missing Runtime Objects & Domain Events
- **Challenge:** Are we trying to store ephemeral operations in the permanent graph?
- **Analysis:** We formally designated `Escalation`, `ReviewDecision`, and `Recommendation` as Runtime Objects. Furthermore, `ReferralSent` and `CaseTransferred` should be modeled as **Domain Events** (appended to the Timeline) rather than structural graph edges.
- **Verdict:** PASSED. The Runtime boundary is enforced.

---

## 2. Structural Model Definition

This section defines the structural guarantees for the upcoming ontology.

### 2.1 Owned Objects (Aggregate Roots)
- `Case` (Root Entity)
  - *owns* `CaseTimeline` (Value Object collection)
  - *owns* `CaseStatus` (Value Object / State)
  - *owns* `CasePlan` (Entity - strictly lifecycle-bound to Case)
    - *owns* `Objective` (Value Object)
    - *owns* `Referral` (Value Object / Event Payload)
    - *owns* `FollowUpSchedule` (Value Object)

### 2.2 Roles
- `StatutoryOwner`
- `LeadCoordinator`
- `ParticipatingAgency`

### 2.3 External References (Outbound Only)
- *references* `Subject` (Shared Domain)
- *references* `Actor` (Shared Domain - fills Roles)
- *references* `AssessmentFinding` (Needs Assessment Domain)
- *references* `Program` (Programs Domain - for funding constraints)
- *references* `InterventionType` (Shared Ontology)

### 2.4 Lifecycle Owner
- The `Case` entity exclusively controls the lifecycle of its `CasePlan` and `Timeline`. A `CasePlan` cannot exist without a parent `Case`.

### 2.5 Core Business Invariants
1. A Case must have exactly one `Subject` (Individual or Household).
2. A Case must have exactly one `StatutoryOwner` and exactly one `LeadCoordinator` (though they may be the same `Actor`).
3. Only one `CasePlan` may be marked "Active" at any given time per Case.
4. Value Objects (`Referral`, `CaseNote`) are immutable once committed to the timeline; corrections require a new addendum, never an overwrite.
5. A Case cannot move to `Active` without an approved `CasePlan`.
6. Administrative Closure does not equate to Graduation; they must use distinctly separate taxonomic paths.

---

## 3. Conclusion

The Case Management domain has been thoroughly subjected to business discovery, edge-case pressure testing, and architectural failure-mode analysis. The boundaries hold, ADR-023 is strictly enforced, and the resulting aggregate models are lean and accurate.

**Ready for Ontology Authoring.**
