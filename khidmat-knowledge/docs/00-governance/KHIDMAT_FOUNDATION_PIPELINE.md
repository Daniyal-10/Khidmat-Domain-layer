# Khidmat AI — Foundation Pipeline & Readiness Tracker

**Purpose:** This tracks the full dependency chain from Project Overview through to Ontology Engineering. Each stage has a status, its real artifacts (where they exist), and the concrete action needed to close it out. Do not begin a stage until the ones above it are marked ready — that's the whole point of the chain.

**Governing principle:** Per Chapter 5.1 and Appendix A of the Project Overview, ontology work is downstream of business and governance foundations. Skipping ahead means inventing structure instead of discovering it — a direct violation of "Evidence precedes conclusions" (Ch 2.2).

---

## Pipeline Overview

```
1. Project Overview               ✅ Done (v1.0)
        ↓
2. Business Master Plan           ✅ Done (Frozen)
        ↓
3. Humanitarian Business
   Reference Model (HBRM)         ✅ Done (Frozen)
        ↓
4. Business Architecture          ✅ Done (Frozen)
        ↓
5. Domain Discovery                🟡 Active (per-domain, repeatable)
        ↓
6. Ontology Design Prerequisites   🔴 Blocked on stage 5
        ↓
7. Ontology Design                 🔴 Blocked on stage 6
        ↓
8. Ontology Engineering            🔴 Blocked on stage 7
```

Legend: ✅ Done · 🟡 Draft exists, needs work · 🔴 Not started / blocked

---

## Stage 1 — Project Overview
**Status: ✅ Done**

v1.0, frozen conceptual foundation. All downstream stages should trace back to this document's mandate, five operating principles, and Chapter 6.1/6.2 methodology.

---

## Stage 2 — Business Master Plan
**Status: ✅ Done (Frozen)**

**What exists:**
- `BUSINESS_MASTER_PLAN_BLUEPRINT.md` — detailed blueprint
- `BUSINESS_MASTER_PLAN.md` — stub only

**What this stage should contain:** the mission and mandate from the Project Overview turned into strategy — funding/sustainability model, phased rollout plan, organizational structure, partnership strategy, and the Ch 9.2 success metrics turned into concrete, time-bound targets.

**Action:**
- [ ] Author the canonical `BUSINESS_MASTER_PLAN.md` from `BUSINESS_MASTER_PLAN_BLUEPRINT.md`
- [ ] Confirm it's consistent with Project Overview Ch 2 (mandate) and Ch 9 (success measures) before treating it as final
- [ ] Get lead sign-off

**Blocks:** Stage 5 onward (Domain Discovery needs a stable strategic frame to know which domains are even in scope for this phase of the project).

---

## Stage 3 — Humanitarian Business Reference Model (HBRM)
**Status: ✅ Done (Frozen)**

**What exists:** Chapter 6.1 of the Project Overview defines the Core Cognitive Lifecycle (Evidence & Knowledge Acquisition → Understanding Formation → Reasoning & Justified Recommendation → Responsible Action), Cross-Cutting Capabilities (Verification, Continuity & Re-assessment, Cross-Organizational Coordination), and Emergent Properties (Trust, Shared Humanitarian Understanding) — but not as a dedicated document.

**Action:**
- [ ] Check whether `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` (see Stage 4) already contains HBRM content under a different label — the "lifecycle" and "principles" sections it reportedly covers may overlap with Ch 6.1. Extract and separate this material rather than assuming it belongs entirely to Business Architecture.
- [ ] Draft HBRM as its own document once that separation is clear
- [ ] Get lead sign-off that it's stable enough to build the ontology's "cognition" and "coordination pattern" layers on top of

**Blocks:** Stage 4 (Business Architecture reconciliation needs a stable HBRM to reconcile against) and Stage 7 Layer 2 (cognition/coordination patterns).

---

## Stage 4 — Business Architecture
**Status: ✅ Done (Frozen)**

**What exists:** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` — already captures actors, principles, lifecycle, and business models. Explicitly marked as unsynchronized with the current Project Overview and Constitution, and not yet authoritative.

**Action:**
- [ ] Review the blueprint section by section against Project Overview v1.0 — flag each section as **keep**, **revise**, or **replace**
- [ ] Separate out any content that actually belongs to HBRM (Stage 3) rather than Business Architecture proper — see note above
- [ ] Reconcile against the Constitution once Stage 0-equivalent governance answers exist (see note below)
- [ ] Once reconciled, formally rename/adopt it as the canonical Business Architecture document

**Note on Constitution:** the Project Overview defers domain-approval authority (Ch 6.2) and audit authority (Ch 8.2) to a future Constitution. If the Constitution doesn't yet exist or is still in draft, get at minimum a **provisional answer** to those two governance questions before finalizing Business Architecture and before Stage 6's readiness gate. This isn't a separate numbered stage here, but it's a hard dependency for Stages 4, 6, and 8.

**Blocks:** Stage 5 (Domain Discovery needs a settled actor/capability model to know what it's discovering against) and Stage 6 (governance readiness gate).

---

## Stage 5 — Domain Discovery
**Status: 🟡 Active — repeatable per domain**

*(Corresponds to Chapter 6.2, Steps 1–2: Proposal + Research and Understanding)*

This stage runs once per domain (e.g., needs-assessment, case-management, a future vertical) and produces evidence and qualified concepts — not ontology structure yet.

### 5.1 Domain Scope
- [ ] Which humanitarian domain?
- [ ] What problem is being modeled? (state as a decision/understanding gap, not a feature)
- [ ] What is explicitly out of scope?

### 5.2 Stakeholder Mapping
- [ ] Primary actors (e.g., beneficiaries, affected families)
- [ ] Secondary actors (e.g., case workers, volunteers, field staff)
- [ ] External actors (e.g., relatives, referring agencies)
- [ ] Regulators
- [ ] Organizations
- [ ] Communities

### 5.3 Evidence Discovery
Collect evidence from:
- [ ] Existing Khidmat documents (Project Overview, Business Master Plan, HBRM, Business Architecture)
- [ ] Existing Khidmat work — validated concepts from the `needs-assessment` and `case-management` adversarial audits
- [ ] Domain experts / practitioners
- [ ] Humanitarian standards (Sphere, CPMS, UNHCR proGres, OCHA HXL)
- [ ] Existing software data models (if applicable)
- [ ] Forms, policies, case notes, research papers, interviews

Log each: concept name, source, one-line description, why it might matter. No structuring yet.

### 5.4 Concept Qualification
*(Ch 6.2 Step 3 — evaluating whether a concept belongs, not just filtering)*
- [ ] Test every candidate against the Ch 5.1 principle: *would its absence materially change understanding of reality or the quality of a decision?*
- [ ] Qualified → Reality Knowledge, carried to Stage 7
- [ ] Not qualified → Operational Knowledge, explicitly marked out of scope (keep the list — it documents reasoning)

**Output of Stage 5:** Domain Scope statement, Stakeholder Map, evidence inventory, and a qualified concept list (Reality Knowledge vs. Operational Knowledge) — for one domain.

**Blocks:** Stage 6 (readiness gate needs qualified concepts to check against the Stable Core).

---

## Stage 6 — Ontology Design Prerequisites
**Status: 🔴 Blocked on Stage 5**

This is a short readiness gate, not a research phase — it confirms the Stable Core is defined and that Stage 5's qualified concepts are consistent with it, plus confirms Stages 2–4 inputs are actually usable.

### 6.1 Stable Core Alignment
*(Ch 5.1 — foundational architecture, defined once, reused across every domain)*
- [ ] Identity — working definition confirmed or drafted
- [ ] Relationships — working definition confirmed or drafted
- [ ] Evidence — working definition confirmed or drafted
- [ ] Uncertainty — working definition confirmed or drafted
- [ ] Temporal change — working definition confirmed or drafted
- [ ] Context — working definition confirmed or drafted
- [ ] Cross-check each against Ch 1.2's contextual dimensions and Ch 5.2's evidence/trust framework
- [ ] Confirm every Stage 5 qualified concept can be described in terms of the core (has identity, participates in relationships, carries evidence, exists in time, carries uncertainty, exists in context). A concept that can't be aligned this way is a signal to revisit Stage 5, not to bypass the core.

### 6.2 Readiness Gate
- [ ] Business Master Plan authored and signed off (Stage 2)
- [ ] HBRM drafted and signed off (Stage 3)
- [ ] Business Architecture reconciled and adopted (Stage 4)
- [ ] Provisional Constitution governance answers exist (domain-approval authority, audit authority)
- [ ] Stage 5 output exists for the domain being designed

**Output of Stage 6:** A "Stable Core Definitions" note, plus a signed-off readiness checklist confirming every upstream stage is closed.

---

## Stage 7 — Ontology Design
**Status: 🔴 Blocked on Stage 6**

Once Stages 2–6 produce real artifacts, the 7-part structure has grounded inputs. Note: the Stable Core does not *generate* primitives — discovery does (Stage 5). The Stable Core *governs* how a discovered primitive is modeled.

> **Example:** If "Beneficiary" appears repeatedly across interviews, documents, and standards (Stage 5.3), and passes qualification (Stage 5.4), it becomes a domain primitive. The Stable Core (Stage 6.1) then tells you *how* to model it — identity, relationships, evidence, time, uncertainty, context.

| Ontology Structure Item | Draws From |
|---|---|
| 1. Domain primitives | Discovered from Stage 5 evidence + qualified concepts; **constrained by** Stage 6 Stable Core |
| 2. Layers (facets, entities, relationships, constraints, states, events, cognition, coordination patterns) | Stage 6 core + Stage 3 HBRM (cognition & coordination layers map directly to Ch 6.1 capabilities) |
| 3. Pillars | Ch 2.2 five operating principles + Ch 1.2 contextual dimensions |
| 4. Architecture rules | Ch 5.1 governing principle + Reality Knowledge / Operational Knowledge distinction |
| 5. Ground truth reviews | Ch 6.2 Step 4 review process — requires provisional governance answer (Stage 4 note) |
| 6. Evidence | Ch 5.2 evidence/trust framework — requires a provenance schema, drafted during Stage 5 |
| 7. Governance | Provisional Constitution answer (Stage 4 note) |

**Output of Stage 7:** The conceptual ontology — primitives, layers, pillars, architecture rules, review process, evidence model, governance model — for the domain in scope.

---

## Stage 8 — Ontology Engineering
**Status: 🔴 Blocked on Stage 7**

Where the conceptual ontology becomes a technical artifact — this is where "RDF/OWL/Knowledge Graph readiness" (a stated design goal for the Domain Layer) actually gets implemented.

**Action (once reached):**
- [ ] Translate domain primitives → OWL classes
- [ ] Translate relationships → object properties, with domain/range constraints
- [ ] Translate constraints → SHACL shapes (or equivalent validation layer)
- [ ] Translate states/events → temporal/versioning model in the knowledge graph
- [ ] Choose tooling (e.g., Protégé for authoring, a triple store / graph DB for runtime)
- [ ] Establish versioning strategy so the ontology can evolve without breaking existing data (consistent with the 20-year durability goal in Ch 9.1)
- [ ] Validate the technical model against Stage 7's conceptual design — engineering should not silently reinterpret design decisions

**Output of Stage 8:** A working, versioned, technically validated ontology implementation.

---

## Summary Status Table

| Stage | Status | Blocking Dependency |
|---|---|---|
| 1. Project Overview | ✅ Done | — |
| 2. Business Master Plan | ✅ Done | — |
| 3. HBRM | ✅ Done | — |
| 4. Business Architecture | ✅ Done | — |
| 5. Domain Discovery | 🟡 Active | Needs Stage 4 closed (Now complete) |
| 6. Ontology Design Prerequisites | 🔴 Blocked | Needs Stage 5 |
| 7. Ontology Design | 🔴 Blocked | Needs Stage 6 |
| 8. Ontology Engineering | 🔴 Blocked | Needs Stage 7 |

---

*Treat this as a living tracker — update statuses as each stage closes. The two highest-leverage next actions right now are: (1) reconcile `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, separating out anything that actually belongs to HBRM before relabeling the rest as Business Architecture; and (2) author the Business Master Plan from its existing blueprint. Both are prerequisites for Domain Discovery even starting.*