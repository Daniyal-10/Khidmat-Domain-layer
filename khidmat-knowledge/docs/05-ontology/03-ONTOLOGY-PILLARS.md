# 3 — Ontology Pillars

**Ontology Design, step 3 of 7.** Status: **Structurally resolved; pending Stage 5/7.**

Derived from `02-ONTOLOGY-LAYERS.md` and `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md`.

---

## 1. Purpose and scope

Pillars are ontology-level organizing concepts. They describe the major, coherent areas of humanitarian reality that the Khidmat ontology must represent. They are not application modules, database tables, AI agents, workflows, or architectural components. They slice through the ontology layers to bundle entities, relationships, states, events, and cognitive stances into understandable domains of reality.

This document represents the completion of **Phase 3** of the ontology design. It is built to represent the *entire* humanitarian system described in the Reference Model, encompassing both the operational response side and the human reality side, without distorting either.

---

## 2. Derivation method

The pillars are derived systematically:
1. **Reference Model (§§3–15)** establishes what exists in humanitarian reality.
2. **Domain Primitives (Step 1)** establish the *kinds* of things those concepts are (Entity, Condition, Context, etc.).
3. **Ontology Layers (Step 2)** establish the structural representation (Entities, States, Events, Cognition, etc.).
4. **Pillars (Step 3)** slice vertically through the layers, grouping reality into major thematic domains that are internally cohesive and externally distinct.

---

## 3. Pillar definitions

### Pillar I: Human & Social Subject
**What domain reality it represents:** The people who exist independently of humanitarian response, their capabilities, and their structural social fabric (family, household).
**Layers contributing:** Entities (Person, Household), Relationships (Dependency, Caregiving), States (Health, Lifecycle, Capability), Facets (Demographics), Constraints (Consent, Dignity).
**Supporting primitives:** Entity (P4), Relation (P7), Condition (P1), Norm (P5).
**RM concepts within it:** Person, Family, Household, Lifecycle, Capability, Dependency, Outcomes (Wellbeing), Impact (Resilience, Independence).
**Why it is a pillar:** It is the persistent "who" of humanitarian reality. It cannot be reduced to an application module or an entity record because it encompasses identity, social connections, and spanning conditions (capabilities). It exists whether or not help is provided.
**Boundary:** Universal. Jurisdiction-specific localizations (e.g., specific national ID systems or joint-family structures) will extend this at Level 2, but the core pillar is independent of jurisdiction.
**What remains outside:** The environment they live in, the acute deficits they suffer, and their interactions with NGOs.

### Pillar II: Context & Environment
**What domain reality it represents:** The physical, economic, and temporal world a household lives in, which changes the meaning and severity of any given condition.
**Layers contributing:** Facets (Context dimensions), Constraints (Applicability bounds), Entities (Community).
**Supporting primitives:** Context (P2).
**RM concepts within it:** Geography, Seasonality, Hazard, Local Economy, Distance to services, Settlement type.
**Why it is a pillar:** It scopes reality. The same damaged roof is a minor repair or an emergency depending on the season and location. It provides the frame within which all other pillars operate.
**Boundary:** Universal. Jurisdiction-specific localizations (e.g., specific administrative boundaries or monsoon seasons) will specialize the context dimensions, but Context itself is universal.
**What remains outside:** The actors and the specific needs.

### Pillar III: Vulnerability & Need
**What domain reality it represents:** What requires a humanitarian response. The open-ended set of humanitarian situations (e.g., displacement, illness, debt), the needs derived from them, and the compounded vulnerability of the subject. Situations are explicitly Open-World, allowing new humanitarian realities to emerge without requiring a new primitive or pillar structure.
**Layers contributing:** States (Need lifecycle), Facets (Severity, Horizon), Relationships (Cascading need).
**Supporting primitives:** Condition (P1), Relation (P7).
**RM concepts within it:** Situations, Needs, Risk, Vulnerability, Outcomes (Need/Risk resolution).
**Why it is a pillar:** This is the core problem space of humanitarian action. It is highly dynamic (needs open, cascade, and close) and is structurally distinct from the human subject (a person *has* a need; they are *not* the need).
**Boundary:** Universal.
**What remains outside:** The interventions that solve the needs, and the baseline capabilities of the person.
**Dependencies:** Both Risk and Need placements are resolved (see §8, items 1–2, and `04-ARCHITECTURE-RULES.md` §1). No structural tension remains for this pillar's definition; population and evidentiary depth remain future work (Stage 5) — see `01a-PRIMITIVE-EVIDENCE-AUDIT.md`.

### Pillar IV: Epistemics & Knowledge
**What domain reality it represents:** What the system (and humanitarian actors) know, how well they know it, and what they do *not* know.
**Layers contributing:** Cognition (Stances, Confidence), Entities (Evidence artifacts), Constraints (Decision thresholds).
**Supporting primitives:** Epistemic Stance (P3), Norm (P5).
**RM concepts within it:** Claims, Findings, Evidence, Confidence, Uncertainty, Contradiction, Missing Information, Epistemic weight of actors.
**Why it is a pillar:** Humanitarian reality is defined by contested, partial, and evolving information. Two actors can hold different epistemic stances about the same Human Subject. This pillar governs AI reasoning, verification boundaries, and human oversight. It guarantees that cognition is a first-class feature of the ontology, not an afterthought.
**Boundary:** Universal. Jurisdiction-specific localizations (e.g., specific poverty-line cards as evidence artifacts) will map here, but the epistemic structure is universal.
**What remains outside:** Ground truth reality (Pillars I and III).

### Pillar V: Actors & Ecosystem
**What domain reality it represents:** The entities that respond to, fund, or coordinate humanitarian action, including Government bodies, Healthcare providers, Schools, and Employers, which act with agency. It models the rules binding them.
**Layers contributing:** Entities (Organisation, Donor, Programme), Relationships (Implements, Funds, Adopts), Constraints (Compliance, Eligibility, Funding restrictions).
**Supporting primitives:** Entity (P4), Relation (P7), Norm (P5).
**RM concepts within it:** Organisations, Programmes, Donors, Community Groups, Governments, Accountability.
**Why it is a pillar:** It models the resource and response side of the equation. It is distinct from the human subject and is necessary to represent accountability, funding chains, and ecosystem coordination.
**Boundary:** Universal. Jurisdiction-specific localizations (e.g., local charity regulations or specific government bodies) will populate this layer, but the structure is universal. Organisation and Programme are collapsed into one Entity per Tier 1 authority precedence (BL V1 §4), closing the previous evidence-based divergence (see `02-ONTOLOGY-LAYERS.md` A-04).
**What remains outside:** The specific actions they take (Events).

### Pillar VI: Action & Coordination
**What domain reality it represents:** How help happens over time, how actors engage with subjects, and how reality is altered or measured.
**Layers contributing:** Events (Occurrences), Coordination Patterns (Loops, Handoffs, Altitude coupling), Constraints.
**Supporting primitives:** Occurrence (P6), Relation (P7), Context (P2), Norm (P5).
**RM concepts within it:** Registration, Verification, Delivery, Follow-up, Handoffs, Case Journey, Grievance loops, Reassessment, Verification events.
**Why it is a pillar:** It tracks actual interventions in the world. It is a pillar because it synthesizes actors, subjects, and needs into sequenced shapes. It adheres to the RM §12 quarantine: actions are things done *to* reality.
**Boundary:** Universal.
**What remains outside:** The static entities and the resources themselves.

### Pillar VII: Resources & Support
**What domain reality it represents:** The resources, modalities of help, gifts, and matching that fuel the response.
**Layers contributing:** Facets (Support dimensions), Entities (Gifts, Resources), Events (Delivery, Matching).
**Supporting primitives:** Entity (P4), Condition (P1), Occurrence (P6).
**RM concepts within it:** Interventions, Sector × Modality × Phase, Cash, In-kind, Giving, Matching.
**Why it is a pillar:** The giving side (donors, resources) needs equal representation to the receiving side to enable the full Khidmat vision. Support is an artifact distinct from the Action of delivering it or the Actor funding it.
**Boundary:** Universal. Jurisdiction-specific localizations (e.g., specific digital payment transfers or local ration items) sit at Level 2.
**What remains outside:** Needs (what it targets), Actors (who gives it).

---

## 4. Primitive → Layer → Pillar traceability

The pillars consume the entire ontology stack without gaps:

| Pillar | Primitives | Primary Layers |
|---|---|---|
| **I. Human & Social Subject** | Entity, Relation, Condition, Norm | Entities, Relationships, States, Constraints |
| **II. Context & Environment** | Context | Facets, Constraints |
| **III. Vulnerability & Need** | Condition, Relation | States, Facets, Relationships |
| **IV. Epistemics & Knowledge** | Epistemic Stance, Norm | Cognition, Entities, Constraints |
| **V. Actors & Ecosystem** | Entity, Relation, Norm | Entities, Relationships, Constraints |
| **VI. Action & Coordination** | Occurrence, Relation, Context, Norm | Events, Coordination Patterns |
| **VII. Resources & Support** | Entity, Condition, Occurrence | Entities, Facets, Events |

---

## 5. Full-domain coverage test

Tested against the required Reference Model coverage list:

* Person, Family, Household, Community, Identity → **Covered (Pillars I, II)**
* Situation, Need, Vulnerability, Risk → **Covered (Pillar III)**
* Evidence, Claims, Verification, Assessment → **Covered (Pillar IV handles the knowledge; Pillar VI handles the action)**
* Volunteer/field activity → **Covered (Pillar V handles the Actor; Pillar VI handles the Action)**
* Organisations, Programmes → **Covered (Pillar V)**
* Support/interventions, Resources, Giving/donors, Matching, Delivery → **Covered (Pillar VII handles Resources/Interventions; Pillar V handles Donors; Pillar VI handles Delivery)**
* Re-verification, Outcomes, Long-term wellbeing → **Covered (Pillar VI handles Re-verification; Pillar I handles Wellbeing; Pillar III handles Outcomes/Risk trajectories)**
* Accountability, Context → **Covered (Pillar V handles Accountability Constraints; Pillar II handles Context)**
* Knowledge/cognition, Coordination → **Covered (Pillar IV handles Knowledge; Pillar VI handles Coordination)**

**Coverage Result:** The 7-pillar structure covers the complete Reference Model. There are no unmapped concepts, no concepts forced into incorrect pillars, and no workflow concepts accidentally becoming pillars. The giving/donor side is fully represented without reducing the human subject to an administrative record.

---

## 6. Cognition coverage test

The lead required explicit testing of whether the ontology can represent cognition. This is fully isolated and protected within **Pillar IV: Epistemics & Knowledge**.

Pillar IV explicitly models:
* **what is known / what is claimed:** Managed via the Claim vs Finding distinction (derived from Epistemic Stance).
* **what is evidenced:** Managed via Evidence entities grounding Epistemic Stances.
* **what is uncertain / unknown:** Managed via the open-world commitment in the Cognition layer (Missing Information as a recognized state).
* **conflicting information:** Managed via Contradiction representation between Claims.
* **confidence/epistemic stance:** Managed via Confidence attributes on assessed needs.
* **reasoning boundaries / what requires human verification:** Managed via Norm/Constraints bound to Epistemic Stances (escalation thresholds).

**Result:** Cognition is treated as a structural domain of reality, not an implementation detail or an AI agent design.

---

## 7. Universal vs Localization boundary (Jurisdiction Strategy)

The pillars enforce a strict two-level jurisdiction strategy:

* **Level 1 (Universal Ontology):** All 7 pillars and their foundational concepts (Person, Need, Resource, Identity, Geography) are universally applicable to any humanitarian context globally.
* **Level 2 (Jurisdiction Localization):** Jurisdiction-specific concepts specialize the universal ontology but do not define it. (e.g., a specific national ID specializing *Identity Document*, or a specific local government tier specializing *Geography/Community*).

The ontology is fully capable of supporting localization for any specific jurisdiction (e.g., Pakistan, UAE, USA, or UK) by adding Level 2 specializations without altering the 7 fundamental pillars.

---

## 8. Resolved decisions and final ontological closures

The primary structural tensions have been formally resolved:

1. **Risk Placement:** Risk is classified as a *Condition* (Pillar III). Confidence *about* a Risk is an *Epistemic Stance* (Pillar IV).
2. **Need Placement:** Need is fundamentally a Condition (RESOLVED — see `01-DOMAIN-PRIMITIVES.md` §6.2 and `04-ARCHITECTURE-RULES.md` §1). Its relational definition describes what a Need means, not what kind of ontological object it is; as a tracked object it carries severity and a lifecycle, which Condition governs and which Relation's own boundary rule cannot accommodate, since the wellbeing standard it is measured against is a Norm, not a persisting Entity.
3. **Outcome / Impact Ownership:** Outcome and Impact are domain realities representing state changes in the relevant human subject (Wellbeing, Resilience, Need Resolution). They are owned by the Human Subject (Pillars I and III). *Outcome/Impact Measurement* (MEAL) is an operational activity that structurally belongs to the Beneficiary Lifecycle (Case Journey) per BL V1 §14 precedence over contradictory evidence.
4. **Family Structure vs Household (RM §4.3):** Both are *Entities*. *Family* is bounded by kinship (persistent). *Household* is bounded by co-residence/shared economy (volatile).
5. **States vs Events Boundary:** The point-versus-span distinction derives structurally from RM quarantining actions from ongoing reality.
6. **Service Providers as Actors:** Government, healthcare, schools, and employers are modeled as Actors (Entities) with agency (Pillar V).
7. **Humanitarian Situations:** Open-world. New situations emerge dynamically without requiring a schema update.
8. **Identity & Biometrics (RM §3.1):** *Identity* is not a primitive (per `01-DOMAIN-PRIMITIVES.md` §5.3). The persisting subject is the **Entity (P4)**; identity resolution — establishing that a subject is the same subject across encounters — is an **Epistemic Stance**, grounded by Evidence. Biometrics, documents, and attestation are subclasses of Evidence conferring different epistemic weights on that stance.
9. **Undocumented Status (RM §3.2):** The absence of *Evidence* (Cognition) structurally instantiates as a *Constraint* limiting formal Coordination Patterns, and a *Condition* aggravating Vulnerability.
10. **Wellbeing Standard (RM §3.6):** A *Norm* that is strictly *Context-dependent* (Pillar II). Need is a *Condition* assessed against this Norm.
11. **Crisis Typology (RM §5.4):** A Crisis is a *Macro-Context* (Pillar II) that cascades *Constraints* and *Conditions* down to Subjects. Phase is a temporal *State*.
12. **Orphanhood vs Unguardianed (RM §6.3):** *Orphanhood* is an irreversible *State* of a kinship Relation. *Unguardianed* is a reversible *State* of a caregiving Relation.
13. **Need Interactions (RM §7.5):** Needs interact via *Dependency Relationships* (Layer 3).
14. **Vulnerability Composition (RM §8.4):** Vulnerability is an emergent composite *State* derived from multiple compounding *Conditions* (e.g., health, capability, household and environmental Conditions) and *Contexts*, per RM §8.4's own framing of "multiple compounding factors." Risk (RM §8.1–8.3) is one *Condition* among several that can compound into Vulnerability; Vulnerability composition is not defined as derived from Risk alone. The composition rule itself is a Source-Absent Parameter (see `01a-PRIMITIVE-EVIDENCE-AUDIT.md`; `04-ARCHITECTURE-RULES.md` UHR-2).
15. **Contradiction Modeling (RM §10.5):** Defined in Cognition as multiple *Epistemic Stances* asserting mutually exclusive *States*.
16. **Funder Altitude (RM §11.4):** The Giving side operates as a third *Funding Altitude*, extending the *Altitude Coupling* Coordination Pattern. It imposes *Constraints* on the Programme Altitude.
17. **Proactive Triggers (RM §16.4):** *Capability* and *Opportunity* function identically to Risk/Need as valid initiating triggers for *Events* and *Coordination Patterns*.

**Empirical and Governance Dependencies:**

Future domain population, jurisdiction-specific localization, exact taxonomies, practitioner enrichment, and implementation details remain open. The foundational ontology's structure — the seven primitives, eight layers, and seven pillars,
and the resolved classification decisions listed above — is resolved and structurally stable.
This constitutes a formal structural resolution; all prior structural governance dependencies are closed.

---

## 9. Stage 3 completion status

* **Stage 1 (Domain Primitives):** Structurally Stable and Formally Closed.
* **Stage 2 (Ontology Layers):** Structurally Stable and Formally Closed.
* **Stage 3 (Ontology Pillars):** Structurally Stable and Formally Closed.

Architecture has **NOT** been designed yet. The Stage 1-3 foundation is **structurally stable and formally closed**:
its categories, layers and pillars are fully resolved against authoritative project sources.
While practitioner validation exists to validate and enrich the
ontology, it will not reopen the structural foundation unless evidence identifies a genuine
structural category that cannot be represented. Architecture design may now proceed on this
fully resolved and closed basis.

