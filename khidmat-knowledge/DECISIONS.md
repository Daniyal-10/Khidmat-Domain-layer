# Khidmat Architectural Decision Log

This file records significant design decisions made during development
of the Khidmat knowledge domain. Each entry records what was decided,
why, and what alternatives were rejected.

Entries are added when a decision is made and are never removed.
If a decision is reversed, a new entry is added explaining the reversal.

**Note:** The formal Architecture Decision Record (ADR) system is now maintained in the `architecture-decisions/` directory. The contents of this file have been migrated to individual ADR documents.

---

## ADR-001: Verification Brief is a Projection, Not an Entity

**Date:** 2025  
**Status:** Accepted

**Decision:**  
The Verification Brief is generated from the Case at the point of closure.
It is not stored as an independent entity. It is a point-in-time view
of the Case and its contained entities.

**Reasoning:**  
If the brief were stored independently, it would become a second source
of truth about the case. Any update to the case after brief generation
would require a synchronisation step to keep the brief current.
In humanitarian operations, cases are frequently updated — new information
emerges, contact details change, needs are re-classified. A stored brief
would routinely be stale.

A projection approach means the brief is always current because it is
always generated from the canonical record.

**Consequence:**  
When a volunteer is assigned, the brief they receive is a snapshot
generated at the moment of assignment. If the case is subsequently
updated before the field visit, a new brief must be generated and
re-issued to the volunteer. This re-issuance mechanism is a
responsibility of the verification-operations domain (not yet active).

**Alternatives rejected:**  
- Storing the brief independently: rejected due to synchronisation risk.
- Versioning the brief as an entity: rejected as premature complexity for V1.

---

## ADR-002: Situation Contextualises Need, Not Generates It

**Date:** 2025  
**Status:** Accepted

**Decision:**  
The relationship between Situation and Need uses the verb `contextualises`,
not `generates` or `causes`.

**Reasoning:**  
The situation does not always causally produce the need. A household
experiencing bereavement (situation) may have a pre-existing medical need
that the bereavement did not cause — but the situation is the context
that makes the medical need urgent and explains why the household
cannot manage it independently. The word `generates` implied causation
that is not always present. `Contextualises` is epistemically accurate.

**Consequence:**  
Every need must be linked to at least one situation, but the link is
interpretive (this situation explains this need) rather than causal
(this situation caused this need). This distinction matters for how
volunteers assess the case in the field.

**Alternatives rejected:**  
- `causes`: too strong. Not all needs are caused by the identified situation.
- `relates_to`: too weak. The situation must do explanatory work, not just
  be associated.

---

## ADR-003: Claim Quality is Two-Dimensional

**Date:** 2025  
**Status:** Accepted

**Decision:**  
Claim quality is assessed along two independent axes:
`information_sufficiency` (how much do we know) and
`information_consistency` (does what we know hold together).

**Reasoning:**  
A single quality score collapses two different problems. A claim can be
complete (all key information is present) but contradictory (the stated
facts conflict with each other). It can also be consistent (no internal
contradictions) but partial (important details are missing).

These require different responses: sufficiency gaps require more questions;
consistency failures require gentle challenge and clarification.
A combined score would produce incorrect responses — more questions
when what is needed is a challenge, or a challenge when what is needed
is more questions.

**Alternatives rejected:**  
- Single quality score: rejected because it produces incorrect AI behaviour.
- Three or more dimensions: rejected as over-engineering for V1.

---

## ADR-004: Placeholder Domain Strategy

**Date:** 2025  
**Status:** Accepted

**Decision:**  
Future domains (verification-operations, case-management, beneficiary-lifecycle,
volunteer-operations, support-delivery, programs, impact) are declared as
Level 2 placeholders. Each placeholder contains:
- A scope statement
- A list of concepts the domain will own
- An explicit list of concepts it does not own
- A `do_not_implement_until` condition

**Reasoning:**  
Declaring domain boundaries before implementation prevents concept drift.
Without declared ownership, concepts get added to whichever domain is
currently active. This produces a bloated registration domain that
owns things it should not, requiring later refactoring. The placeholder
strategy locks ownership before the implementation pressure begins.

**Consequence:**  
Developers may not add concepts to placeholder domains. Any concept
that turns out to be needed earlier than expected must be promoted
to the shared domain or the owning domain must be activated.

**Alternatives rejected:**  
- Single large domain: rejected because it produces an unmanageable
  ontology and violates separation of concerns.
- No placeholder declarations: rejected because undeclared boundaries
  are always violated under time pressure.

---

## ADR-005: Claim Basis is Inherited from Registrant, Not Per-Claim

**Date:** 2025  
**Status:** Accepted

**Decision:**  
Each registrant has a `default_claim_basis` (first_hand, second_hand,
observational, or inferred). Claims inherit this basis unless explicitly
overridden. Only claims where the basis differs from the registrant
default need an explicit `claim_basis` value.

**Reasoning:**  
In most registrations, the registrant's epistemic relationship to the
information is consistent throughout the conversation. A self-registering
beneficiary makes first-hand claims throughout. A volunteer makes
observational claims throughout. Recording basis per-claim when it does
not change would be noisy and add friction to data entry.

**Consequence:**  
When the AI detects a claim whose basis should differ from the registrant
default (e.g., a proxy claiming first-hand knowledge of the beneficiary's
emotional state), it must explicitly set `claim_basis` on that claim.
The absence of an explicit value means the registrant default applies.

**Alternatives rejected:**  
- Per-claim basis with no default: rejected because it increases data
  entry burden without proportional accuracy gain in typical cases.

---

## ADR-006: Safety Flag Triggers Immediate Assessment, Not Automatic Closure

**Date:** 2025  
**Status:** Accepted

**Decision:**  
When a safety flag is raised during registration, the AI must conduct
a safety assessment before closing the case, but the case is not
automatically marked `unsafe_to_verify`. The outcome of the assessment
determines the final status.

**Reasoning:**  
In domestic violence situations, a safety flag is raised automatically.
But the beneficiary may have already moved to a safe location, or may
have a specific safe contact protocol that makes verification feasible.
Automatically marking cases as `unsafe_to_verify` without assessment
would block legitimate verifications and increase case review burden
unnecessarily.

**Consequence:**  
The AI must ask the safety assessment question in every case where a
safety flag is raised. The question and the response must be recorded
in `situation.safety_notes`. The resulting status depends on the answer.

**Alternatives rejected:**  
- Automatic `unsafe_to_verify` on any safety flag: rejected as too blunt.
- No safety gate at all: rejected as a safeguarding failure.

---

## ADR-007: Shared Human Model as a First-Class Knowledge Layer

**Date:** 2026
**Status:** Accepted

**Decision:**

Lifecycle stages, capabilities, dependencies, family structures, and health conditions will be modelled in a dedicated Shared Human Model layer.

These concepts are promoted to shared ownership.

**Reasoning:**

Future domains require a consistent representation of human development, household relationships, dependency structures, and capabilities.

Allowing each domain to define its own person model would create ontology drift.

A dedicated human model establishes a single source of truth.

**Consequence:**

Future domains must reference the Shared Human Model rather than defining competing human concepts.

**Alternatives rejected:**

* Defining lifecycle concepts independently in each domain.
* Extending registration ontology to own human concepts.
* Delaying human modelling until beneficiary lifecycle activation.

---

## ADR-008: Single Ownership of Concepts

**Date:** 2026
**Status:** Accepted

**Decision:**

Every concept in the knowledge layer must have exactly one authoritative owner.

Ownership is maintained through ontology_authority_matrix.md.

**Reasoning:**

Duplicate ownership creates ontology drift and inconsistent reasoning.

Concepts may be referenced by many files but defined by only one file.

**Consequence:**

When a concept appears in multiple locations, one location must be designated canonical and all others become references.

**Alternatives rejected:**

* Distributed ownership.
* Duplicate definitions across domains.

---

## ADR-009: Dependency-Driven Domain Activation

**Date:** 2026
**Status:** Accepted

**Decision:**

Domains activate according to the dependency order defined in knowledge_layer_roadmap.md.

Placeholder domains remain inactive until prerequisites are satisfied.

**Reasoning:**

Premature activation causes domains to invent concepts they do not own.

Dependency-first activation preserves architectural integrity.

**Consequence:**

Roadmap dependencies become governance constraints.

**Alternatives rejected:**

* Activating domains on implementation demand alone.
* Allowing placeholder domains to define concepts early.

---

## ADR-010: Risk Domain is Qualitative Not Quantitative

**Date:** 2026
**Status:** Accepted

**Decision:**
Risk, Vulnerability, and Resilience are qualitative levels supported by structured, named inputs. No numeric scores, weighted formulas, or composite indices may be used.

**Reasoning:**
Numeric scoring obscures the underlying logic and creates false precision. Qualitative judgment is more appropriate for humanitarian reasoning.

**Consequence:**
Risk files must not introduce numeric calculations.

---

## ADR-011: Risk Domain Does Not Prescribe Interventions

**Date:** 2026
**Status:** Accepted

**Decision:**
The Risk Domain produces signals (risk level, risk trend, compound risk flags) but does not define what should be done in response.

**Reasoning:**
Intervention logic belongs to Case Management (Stage 5). Mixing risk identification with intervention logic creates a monolithic reasoning layer.

**Consequence:**
Risk rules must not recommend interventions.

---

## ADR-012: Horizon and Persistence are Distinct

**Date:** 2026
**Status:** Accepted

**Decision:**
When harm might occur (Risk Horizon) and how long the risk-generating condition lasts (Risk Factor Persistence) are modeled as separate attributes.

**Reasoning:**
They are independent questions. A short-term condition might pose an immediate threat, or a long-term condition might pose a distant threat.

**Consequence:**
Never collapse these into a single enum.

---

## ADR-013: Concept vs. Instance Separation

**Date:** 2026
**Status:** Accepted

**Decision:**
The Risk Domain defines types and categories. Instance-level presence is tracked in case data domains.

**Reasoning:**
Separating ontology from data prevents the knowledge layer from becoming a database.

**Consequence:**
Risk files define the model; case domains hold the instances.

---

## ADR-014: Risk Domain Composes Existing Entities

**Date:** 2026
**Status:** Accepted

**Decision:**
The Risk Domain references lifecycle stages, capabilities, dependencies, health conditions, and family structures by reference. It does not redefine them.

**Reasoning:**
Prevents ontology drift and maintains the Shared Human Model as the single source of truth.

**Consequence:**
Must use `*_ref` patterns defined in shared/risk/governance.md.