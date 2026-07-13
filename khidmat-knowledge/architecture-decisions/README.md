# Khidmat Knowledge Layer — Architecture Decision Records (ADR)

## What are ADRs?
Architecture Decision Records (ADRs) are short, standardized documents that capture important architectural decisions made along with their context, consequences, and alternatives considered.

## Why this repository uses ADRs
The Khidmat Knowledge Layer is a complex ontological and taxonomical foundation that supports multiple operational domains. Over time, decisions about domain boundaries, conceptual models, and knowledge graphs become embedded in YAML files. ADRs ensure that future contributors and AI systems understand the **why** behind the architecture without having to read and interpret every YAML file. 

## When a new ADR should be created
A new ADR should be created when a decision:
- Introduces a new architectural pattern.
- Defines ownership or boundaries between domains.
- Resolves a significant design ambiguity or overlap.
- Establishes a rule that must be followed by future ontology additions.

## ADR Lifecycle
1. **Draft:** The decision is proposed.
2. **Proposed:** Ready for review by the Knowledge Layer Architect.
3. **Accepted:** The decision is approved and becomes binding.
4. **Deprecated:** A later ADR supersedes this decision.

## ADR Numbering Convention
ADRs are numbered sequentially with a zero-padded three-digit prefix (e.g., ADR-001-title.md). The prefix ensures chronological sorting.

## ADR Index

| ADR | Title | Status | Purpose |
|---|---|---|---|
| [001](ADR-001-verification-brief-is-a-projection-not-an-entity.md) | Verification Brief is a Projection, Not an Entity | Accepted | The Verification Brief is generated from the Case at closure, not stored independently, so it is never a stale second source of truth. |
| [002](ADR-002-situation-contextualises-need-not-generates-it.md) | Situation Contextualises Need, Not Generates It | Accepted | A Situation explains why a Need is urgent; it does not always causally produce that Need. |
| [003](ADR-003-claim-quality-is-two-dimensional.md) | Claim Quality is Two-Dimensional | Accepted | Claim quality is assessed on two independent axes — information sufficiency and information consistency — so the AI responds correctly to each failure mode. |
| [004](ADR-004-placeholder-domain-strategy.md) | Placeholder Domain Strategy | Accepted | Future domains are declared as Level 2 placeholders with explicit scope and ownership boundaries before any implementation begins. |
| [005](ADR-005-claim-basis-is-inherited-from-registrant-not-per-claim.md) | Claim Basis is Inherited from Registrant, Not Per-Claim | Accepted | Claims inherit a registrant's default epistemic basis unless explicitly overridden, avoiding per-claim data-entry noise. |
| [006](ADR-006-safety-flag-triggers-immediate-assessment-not-automatic-closure.md) | Safety Flag Triggers Immediate Assessment, Not Automatic Closure | Accepted | A safety flag requires an assessment before case closure but does not automatically mark a case unsafe-to-verify. |
| [007](ADR-007-shared-human-model-as-a-first-class-knowledge-layer.md) | Shared Human Model as a First-Class Knowledge Layer | Accepted | Lifecycle, capability, dependency, family structure, and health condition concepts are promoted to a dedicated shared layer to prevent per-domain ontology drift. |
| [008](ADR-008-single-ownership-of-concepts.md) | Single Ownership of Concepts | Accepted | Every concept has exactly one authoritative owner, tracked in `ontology_authority_matrix.md`; all other references never redefine it. |
| [009](ADR-009-dependency-driven-domain-activation.md) | Dependency-Driven Domain Activation | Accepted | Domains activate only in the order `knowledge_layer_roadmap.md` defines, preventing premature concept invention. |
| [010](ADR-010-risk-domain-is-qualitative-not-quantitative.md) | Risk Domain is Qualitative Not Quantitative | Accepted | Risk, Vulnerability, and Resilience are qualitative levels with structured named inputs — no numeric scores or composite indices. |
| [011](ADR-011-risk-domain-does-not-prescribe-interventions.md) | Risk Domain Does Not Prescribe Interventions | Accepted | The Risk Domain produces signals only; intervention logic belongs to Case Management. |
| [012](ADR-012-horizon-and-persistence-are-distinct.md) | Horizon and Persistence are Distinct | Accepted | When harm might occur (Risk Horizon) and how long a risk-generating condition lasts (Persistence) are modeled as separate attributes. |
| [013](ADR-013-concept-vs.-instance-separation.md) | Concept vs. Instance Separation | Accepted | The Risk Domain defines types and categories; instance-level presence is tracked in case data domains, not in the ontology. |
| [014](ADR-014-risk-domain-composes-existing-entities.md) | Risk Domain Composes Existing Entities | Accepted | The Risk Domain references Shared Human Model concepts by reference and never redefines them. |
| [015](ADR-015-functional-capacity-is-a-derived-operational-summary.md) | Functional Capacity is a Derived Operational Summary | Accepted | `functional_capacity` is a derived operational summary, not an independent authoritative trait — `capabilities.yaml` remains the authoritative source. |
| [016](ADR-016-lifecycle-descriptive-placeholders-remain-descriptive.md) | Lifecycle Descriptive Placeholders Remain Descriptive Until Ontology Stabilization | Accepted | Descriptive placeholders in `lifecycle-stages.yaml` stay descriptive (not hard references) until the knowledge layer stabilizes. |
| [017](ADR-017-controlled-interim-support-intervention-taxonomy.md) | Controlled Interim Support Intervention Taxonomy for Verification Operations | Accepted | Verification Operations may use a controlled interim intervention taxonomy until the full, programme-validated taxonomy is finalized. |
| [018](ADR-018-shared-subject-supertype.md) | Shared Subject Supertype | Accepted | Introduces `Subject` as an authoritative Shared concept — the common abstraction for `Person` and `Household` — so domains stop inventing their own. |
| [019](ADR-019-archived-is-not-a-lifecycle-stage.md) | Removal of Archived as a Lifecycle Stage | Accepted | Removes `archived` from `engagement_stage` — archiving is a data-retention concern, not a humanitarian lifecycle state. |
| [020](ADR-020-decoupling-lifecycle-from-support-delivery.md) | Decoupling Lifecycle Progression from Support Delivery | Accepted | Replaces `receiving_support` with `engaged` in `engagement_stage` so lifecycle state doesn't couple to Support Delivery's operational details. |
| [021](ADR-021-case-lifecycle-handoff.md) | Case Lifecycle Handoff Between Registration and Case Management | Accepted | Registration's and Case Management's case-status vocabularies are declared sequential phases of the same canonical `Case` entity, owned by Case Management. |
| [022](ADR-022-canonical-concepts-and-regional-localization-strategy.md) | Canonical Concepts and Regional Localization Strategy | Accepted | Every concept has exactly one canonical identifier and definition; regional/localized labels are aliases, never new concepts. |
| [023](ADR-023-ontology-vocabulary-extension-value-objects-roles-runtime-objects.md) | Ontology Vocabulary Extension — Value Objects, Roles, Runtime/Reasoning Objects, and Future Entity Candidates | Proposed (pending reviewer ratification) | Extends the ontology contract with Value Objects, Roles, a Runtime/Reasoning boundary, and Future Entity Candidates, so composite attributes aren't defaulted into entity-explosion. Already applied in Registration's Phase 4 migration. |
| [024](ADR-024-foundational-layer-precedes-operational-activation.md) | Foundational Knowledge Layer May Be Authored Before Operational Activation | Accepted | A placeholder domain's organization-invariant foundation (Tier 1) may be authored ahead of its operational activation trigger; the operational/runtime layer (Tier 2) stays gated. Refines D-VO1/D-VO3; introduces the *Canonical (Foundational) — Operational Deferred* maturity state. Applied to Volunteer Operations. |
