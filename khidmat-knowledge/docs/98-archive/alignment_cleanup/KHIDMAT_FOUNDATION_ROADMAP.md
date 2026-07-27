---
title: Khidmat Foundation Roadmap
status: Active
owner: Governance
created: 2026-07-27
---

# Khidmat Foundation Roadmap

## 1. Purpose

The **Khidmat Foundation** is the complete, evidence-backed business knowledge baseline required to design the Khidmat Humanitarian Ontology correctly. 

The Foundation exists to ensure that ontology design is grounded in validated humanitarian business reality rather than technical assumptions or schema-first engineering. It is the bridge between raw humanitarian reality and formal ontology.

**How it differs from Business Discovery:**
Business Discovery is only one component of the Khidmat Foundation. While Discovery gathers the evidence, the Foundation also includes the synthesis of that evidence (Business Master Plan), the structural modeling of that evidence (Humanitarian Business Reference Model), and the operational configuration (Business Architecture). 

The Foundation is the absolute prerequisite for Domain Discovery and Ontology Design.

---

## 2. Foundation Scope

A complete Khidmat Foundation requires the finalization of the following components:

- **Canonical Governance:** Project Overview, Constitution, Vision, Glossary
- **Business Discovery Evidence:** Humanitarian Actors, Stakeholders, Lifecycles, Capabilities, Services, Value Streams, Intervention Categories
- **Governance Approvals:** Human Owner Decisions (Contradiction Resolution)
- **Business Master Plan:** Synthesis of business concepts and flows
- **Humanitarian Business Reference Model (HBRM):** Structural model of the business
- **Business Architecture:** Operational capability mapping

---

## 3. Foundation Completion Matrix

| Component | Source Documents | Current Status | Confidence | Remaining Work |
|---|---|---|---|---|
| **Governance & Mandate** | `PROJECT_OVERVIEW.md`, `CONSTITUTION.md`, `VISION.md`, `GLOSSARY.md` | **Complete** (Frozen v1.0) | High | Routine glossary synchronization. |
| **Business Discovery** | `TD-01` through `TD-06` | **Complete** (Handed off) | Medium (relies on Assumptions due to absent Tier A) | Minor discovery if new topics emerge. |
| **Contradiction Resolution** | `CONTRADICTION_LOG.md`, `HUMAN_OWNER_DECISION_BRIEF_01.md` | **Complete** | High | All contradictions resolved. |
| **Business Master Plan** | `BUSINESS_MASTER_PLAN.md` | **Not Started** | None | Draft and certify using discovery evidence. |
| **HBRM** | `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` | **Not Started** | None | Draft and certify based on BMP. |
| **Business Architecture** | `BUSINESS_ARCHITECTURE.md` | **Not Started** | None | Draft and certify based on HBRM. |

---

## 4. Readiness Assessment

**Is the Foundation currently ready to support Ontology Design?**  
**NO.**

**Remaining Work:**
1. ~~The open contradictions (CL-001, CL-002) must be resolved by the Human Owner.~~ (Resolved)
2. ~~Business Discovery must be formally closed.~~ (Closed)
3. The Business Master Plan must be authored and certified.
4. The Humanitarian Business Reference Model must be authored and certified.
5. The Business Architecture must be authored and certified.

Ontology Design **cannot** begin until this remaining work is complete.

---

## 5. Approval Gates

The project follows strict sequential approval gates:

- **Gate 1:** Khidmat Foundation Complete (All components above finalized)
- **Gate 2:** Lead Review Package A (Foundation) Approved
- **Gate 3:** Ontology Design may begin
- **Gate 4:** Lead Review Package B (Ontology Design Foundation) Approved
- **Gate 5:** Continue remaining Ontology Design (Pillars, Rules, Evidence, Governance)

---

## 6. Review Package Definition

When the repository is ready, the following two packages will be presented to the Project Lead. 

### Package A: Khidmat Foundation
*Purpose: Validate the humanitarian business reality.*
- Canonical Governance (Overview, Constitution)
- Complete Business Discovery Dossiers
- Resolved Contradiction Log and Decisions
- Business Master Plan
- Humanitarian Business Reference Model (HBRM)
- Business Architecture

### Package B: Ontology Design Foundation
*Purpose: Validate the conceptual structure of the ontology before technical engineering.*
**Includes ONLY:**
1. **Domain Primitives**
2. **Ontology Layers:**
   - Facets
   - Entities
   - Relationships
   - Constraints
   - States
   - Events
   - Cognition
   - Coordination Patterns

*(Note: Nothing beyond these two sections will be designed until Package B is approved).*

---

## 7. Risks

The following repository risks currently threaten the completion of the Khidmat Foundation and could weaken future Ontology Design:

- ~~**Unresolved Contradictions:** CL-001 (Programme vs Organisation definition) and CL-002 (Donor status) directly block the authoring of the Business Master Plan.~~ (Resolved)
- **Missing Tier A Evidence:** The absence of primary practitioner validation has resulted in 10 active assumptions (AR-001 through AR-010). These assumptions carry structural risk into the Master Plan.
- **Governance Dependencies:** If human owner decisions are delayed, the sequential methodology guarantees that the entire project remains stalled. Downstream phases cannot absorb the uncertainty of upstream contradictions.
