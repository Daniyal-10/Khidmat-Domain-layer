# Blueprint: Khidmat AI Business Master Plan

**Type:** Discovery & authoring blueprint (not the Business Master Plan itself)
**Governs the future authoring of:** `docs/01-methodology/BUSINESS_MASTER_PLAN.md`
**Status:** Draft for review

---

## 1. Purpose

### Why this document exists

Every ontology entity the repository has authored so far — `case`, `need`, `intervention`, `household`, `verification_activity` — is a formalization of *something that already happens in humanitarian practice*. The ontology work has been able to proceed only because that practice is, informally, already understood by whoever is writing the YAML. The Business Master Plan is the document that makes that understanding **explicit, written, and reviewable independent of any ontology** — so that the next domain to be modelled, the next reasoning rule to be written, and the next AI collaborator to join the project can check their design against a description of humanitarian reality, not against another engineer's memory of it.

Put simply: the ontology answers *"what do we call this, and how does it relate to other things?"* The Business Master Plan must answer the question that has to be settled *first* — **"what actually happens, to whom, done by whom, and why does it work that way?"**

### Questions it must answer

- Who does humanitarian assistance actually involve — as actors, not as data fields?
- What is the shape of the humanitarian lifecycle, independent of any one organization's workflow?
- What business capabilities does *any* humanitarian organization need, regardless of size, geography, or sector?
- What are the recurring value streams (need → assistance → outcome) that repeat across every domain the ontology has already modelled?
- Where does one capability's responsibility end and another's begin (the same "single ownership" discipline the ontology already enforces, but at the level of *business capability*, not concept)?
- What does "success" mean in humanitarian terms, before it is operationalized into any outcome-indicator vocabulary?
- What operating constraints (governance, ethics, resourcing, trust) shape *how* those capabilities may be exercised?

### Audience

- **Primary:** the humanitarian domain experts and knowledge architects who will next author the Humanitarian Business Reference Model and any new domain's foundational ontology — they need a business description to model *from*, not a technical one.
- **Secondary:** AI collaborators operating under `AI_WORKFLOW.md` (the "Chief Knowledge Architect," "Claude Supervisor," and "Antigravity Agent" roles) — they need this document as the checkable source of truth for "is this concept business-real or an invented convenience?"
- **Tertiary:** any future human stakeholder (client, NGO partner, reviewer) who needs to verify that Khidmat's model of humanitarian work matches lived reality, without reading a single line of YAML.

### How future documents depend on it

The Humanitarian Business Reference Model cannot categorize business capabilities it has not first been told exist. Domain Discovery cannot decide *when* a new domain (e.g., "Education" or "Healthcare") is ready to be modelled without a master plan describing where that domain sits in the humanitarian lifecycle and what capability gap it fills. Ontology Design cannot decide whether a candidate concept is a business-real entity or an engineering convenience without a business description to check it against. Every downstream document is a *narrowing* of this one — from "how humanitarian assistance works" down to "how we classify it" down to "how we formally model it."

---

## 2. Scope

### What belongs inside this document

- **The humanitarian ecosystem** — the organizations, actor types, and systemic relationships that exist in humanitarian work generally (NGOs, government bodies, donors, community structures, volunteers, beneficiaries) — described as *roles in a business process*, not as data entities.
- **Stakeholders and their interests** — who wants what from the system of humanitarian assistance, and where those interests align or conflict (e.g., donor accountability vs. beneficiary dignity vs. speed of relief).
- **The humanitarian lifecycle** — the macro sequence of business events from "a need exists" through "assistance is delivered" to "an outcome is achieved or not achieved" — described in business language (what happens, who does it, why), not in lifecycle-state-machine language.
- **Business capabilities** — the recurring *things a humanitarian organization must be able to do* (identify need, verify claims, coordinate resources, deliver assistance, measure outcome) independent of who does them or how.
- **Business services** — the concrete offerings a capability produces (a verified case, a delivered intervention, a closed referral) — the "what comes out" of a capability.
- **Value streams** — the end-to-end chains that connect a triggering event (a person in crisis) to a value-delivering outcome (sustainable recovery), cutting across capabilities.
- **Operational objectives** — what "doing this well" means at the business level (dignity preserved, verification quality, time-to-assistance, avoidance of duplicate aid) — the business-level ancestors of what will *later* become outcome indicators.
- **Intervention types, at the business level** — categories of assistance (immediate relief, rehabilitative support, sustainable independence pathways) described as business concepts, not as `support_intervention` taxonomy entries.
- **Success measures, in business language** — what changes in a person's or community's life when the system works, described narratively and by example, not as a measurement schema.
- **Governance boundaries** — who has authority over what kind of business decision (case-level, program-level, organizational-level) — the business-process ancestor of the ontology's "concept ownership" discipline.

### What does NOT belong here

- Ontology classes, entities, relationships, or any `entities.yaml`/`data-properties.yaml`-shaped content.
- Taxonomy schemes, controlled vocabularies, or enumerations.
- Database schemas, storage models, or data formats of any kind.
- API design, service boundaries, or integration contracts.
- AI reasoning rules, inference logic, or confidence-scoring mechanisms.
- Software architecture of any kind (this repository's own `AI_WORKFLOW.md` and `ARCHITECTURE.md` already govern that separately, for the knowledge layer specifically — the Business Master Plan is upstream of even that).
- Anything that names a YAML file, a file path, or a repository directory as part of its own content. If a sentence in the Business Master Plan could not be understood by someone who has never seen this repository, it is in scope. If it requires having read `Canonical_Ontology_Schema.md` to parse, it is out of scope.

**Litmus test for every candidate paragraph:** *Could this sentence be true of humanitarian assistance in a world where Khidmat AI was never built?* If yes, it belongs in the Business Master Plan. If the sentence only makes sense because Khidmat AI exists, it belongs in a downstream document instead.

---

## 3. Intended Audience

(Consolidated from §1 for the deliverable's required section — see above for full reasoning.)

1. Humanitarian domain experts / knowledge architects authoring downstream reference models.
2. The multi-agent AI collaboration roles defined in `AI_WORKFLOW.md`.
3. Human reviewers and stakeholders validating that the model matches reality.

---

## 4. Document Dependencies

### Recommended dependency chain (revised from the task's example)

```
PROJECT_OVERVIEW.md  (why the project exists — informal, working draft)
        ↓
VISION.md  (the mandate — formal, complete)
        ↓
PHILOSOPHY.md + PRINCIPLES.md  (the non-negotiable rules of understanding — formal, NOT YET WRITTEN)
        ↓
BUSINESS MASTER PLAN  ← this document's subject
        ↓
Humanitarian Business Reference Model  (categorizes the capabilities BMP describes)
        ↓
Business Architecture  (maps capabilities to the org boundaries that will exercise them)
        ↓
Domain Discovery  (decides which humanitarian domain is modelled next, and when)
        ↓
Ontology Design  (methodology: how a business concept becomes a candidate ontology concept)
        ↓
Ontology Engineering  (this repository's existing, mature, 29-ADR-deep practice)
```

### Why this differs from the task's example chain

The task's example places the Business Master Plan directly under the Project Overview and directly above the Humanitarian Business Reference Model, with no philosophy/principles step and no Business Architecture / Domain Discovery steps shown. Two corrections, both grounded in documents that already exist in this repository:

1. **PHILOSOPHY.md and PRINCIPLES.md must sit between VISION.md and the Business Master Plan, not be skipped.** The repository's own Blueprint (`docs/00-governance/PROJECT_OVERVIEW_BLUEPRINT.md`) states that Chapters 1–2 (Vision, then Philosophy/Principles) "must precede all other chapters," and that Chapters 5–6 (which include the Business Architecture and Business Reference Model) explicitly "depend on the constraints set in Ch 3-4," which in turn depend on Ch 1-2. Writing the Business Master Plan before Philosophy/Principles exist risks the Plan silently inventing its own operating principles (e.g., "AI may act autonomously when confidence is high") that later contradict whatever Chapter 2 eventually states formally.
2. **Business Architecture and Domain Discovery are real, separate downstream documents already scaffolded in this repository** (`docs/01-methodology/BUSINESS_ARCHITECTURE.md`, `DOMAIN_DISCOVERY.md`), and they are not the same thing as the Humanitarian Business Reference Model. Collapsing them into one step in the dependency chain would misrepresent what each is for: the Reference Model *categorizes* business capabilities; Business Architecture *maps* those capabilities onto organizational/operational boundaries; Domain Discovery *governs the sequencing decision* of which capability area gets modelled into ontology next (a decision this repository already makes informally via `knowledge_layer_roadmap.md` and ADR-009, but has never written a formal methodology for).

**Note on informal precedent:** This repository's own engineering practice (the ADR log, `AI_WORKFLOW.md`, `knowledge_layer_roadmap.md`) already encodes a working philosophy, a working set of principles, and a working (if implicit) business reference model — none of it written down as the formal documents this chain names. The Business Master Plan should be authored *with awareness of that existing practice*, treating the ADR log as evidence of what the humanitarian business reality already required the ontology to respect, not as a document to ignore until Ontology Engineering is formally reached again.

---

## 5. Relationship to Existing and Planned Documents

| Document | Unique responsibility | How it differs from the Business Master Plan |
|---|---|---|
| `PROJECT_OVERVIEW.md` | Informal, evolving statement of the project's current understanding — a working alignment point, explicitly *not* any formal document. | The Overview is provisional and personal-voice; the BMP is the first *normative*, stable business description. The Overview may eventually be retired once the formal chapters (VISION, PHILOSOPHY, BMP, etc.) collectively supersede it — that retirement decision is out of scope here. |
| `VISION.md` | States the mandate and the ultimate measure of success, in aspirational/existential terms ("what fundamental truth about the world will have changed"). | VISION answers *why the project should exist at all*. The BMP answers *how the business it describes actually operates*, independent of whether Khidmat AI exists to serve it. VISION is Khidmat-specific; the BMP's subject matter (humanitarian assistance) predates and would outlive Khidmat AI. |
| `PHILOSOPHY.md` | States the non-negotiable epistemic rules governing how understanding is built (e.g., "knowledge precedes automation," what it means for a system to "understand"). | PHILOSOPHY is about the *rules of knowing*; the BMP is about the *content known*. PHILOSOPHY would say "verification must precede trust" as a general rule; the BMP would describe what verification actually looks like as a business process, without yet deciding how a system enforces the rule. |
| `PRINCIPLES.md` | The small number of unbreakable design laws derived from PHILOSOPHY. | PRINCIPLES are constraints ON the BMP (and every document after it) — the BMP must be checked against PRINCIPLES, not the reverse. |
| Business Architecture | Maps the BMP's capabilities onto organizational structures, roles, and operational boundaries — "who within an org does this, and how do orgs coordinate." | Business Architecture asks "how is this capability organized and executed operationally"; the BMP asks "what is this capability and why must it exist." Business Architecture presumes the BMP's capability list as an input, not vice versa. |
| Humanitarian Business Reference Model | A structured *taxonomy* of the business capabilities and services the BMP describes narratively — the classification scheme. | The BMP is prose-level business understanding; the Reference Model is the first structured (but still non-ontological) categorization of it. The Reference Model cannot exist without the BMP's content to categorize. |

**Duplication discipline:** each document above answers a distinct question type — *why* (VISION), *how one must think* (PHILOSOPHY/PRINCIPLES), *what happens* (BMP), *how it is categorized* (Reference Model), *how it is organizationally executed* (Business Architecture). If two documents ever seem to need the same paragraph, that is a signal one of them is answering the wrong question type and should be revised — not that the content should be copied into both.

---

## 6. Complete Chapter Structure

Each chapter below is designed, not written. Every chapter states its purpose, why it exists, its dependencies, and its expected output — never its content.

### Chapter 1 — The Humanitarian Ecosystem

- **Purpose:** Describe who exists in the world of humanitarian assistance and what role each plays, before any Khidmat-specific concept is introduced.
- **Why it exists:** Every downstream document (Reference Model, ontology's `Actor`/`Organisation` concepts, ADR-018's `Subject` supertype) presumes a shared understanding of *who acts* in humanitarian work. Right now that understanding is implicit in scattered ADRs (e.g. ADR-025's donor model, ADR-026's volunteer boundary) rather than stated once, from the business side, up front.
- **Dependencies:** None internal to the BMP — this is the entry chapter. Externally depends on PHILOSOPHY/PRINCIPLES being settled first (per §4), so that how actors are described doesn't accidentally encode an unratified principle.
- **Expected output:** A narrative map of actor categories (affected populations, implementing organizations, donors/funders, government bodies, volunteers, community structures) and how they relate to one another as businesses and people — not as ontology entities.

### Chapter 2 — Stakeholder Interests and Tensions

- **Purpose:** Name what each stakeholder category wants and where those wants structurally conflict.
- **Why it exists:** The ontology already encodes some resolved tensions as ADRs (e.g., ADR-006's "safety flag triggers assessment, not automatic closure" is a resolution of a tension between speed and safety). The BMP should name the tension *before* the ontology resolves it, so future tensions are recognized and deliberated rather than resolved ad hoc inside a single YAML file.
- **Dependencies:** Chapter 1 (requires the actor map).
- **Expected output:** A structured list of stakeholder interests (dignity vs. accountability, speed vs. verification rigor, standardization vs. cultural/regional variation) with enough narrative to explain *why* each tension is real, not just that it exists.

### Chapter 3 — The Humanitarian Lifecycle (Business View)

- **Purpose:** Describe the macro sequence of business events — need arises, is recognized, is assessed, is responded to, is followed up on, is resolved or not — entirely in business language.
- **Why it exists:** This repository already has a *technical* lifecycle model (`knowledge_layer_roadmap.md`'s stage graph, `beneficiary-lifecycle`'s `engagement_stage` taxonomy). Neither is a business description; both presume one exists. Writing the business-level lifecycle first would let a future reviewer check whether `engagement_stage`'s values are a faithful technical rendering of it.
- **Dependencies:** Chapters 1–2 (the lifecycle is meaningless without knowing who participates in each stage and what interests are at stake at each transition).
- **Expected output:** A stage-by-stage business narrative (not a state machine) of how a humanitarian case unfolds, cross-checkable against — but written independently of — `beneficiary-lifecycle/taxonomy/engagement-stage.yaml`.

### Chapter 4 — Business Capabilities

- **Purpose:** Enumerate the recurring things a humanitarian organization must be able to do (need identification, verification, case coordination, resource management, delivery, monitoring/learning) as capability statements, independent of any specific organization's org chart.
- **Why it exists:** This is the direct business-level ancestor of the repository's domain list (`registration`, `verification-operations`, `case-management`, `support-delivery`, `impact`, etc.). Right now the domain list exists without a stated business-capability rationale for why those particular 13 domains, and no others, were chosen.
- **Dependencies:** Chapter 3 (capabilities exist to execute stages of the lifecycle).
- **Expected output:** A capability catalogue, each entry naming what the capability accomplishes, why it is distinct from neighboring capabilities, and what would be missing if it did not exist — written so that a reader could independently derive something like the repository's current domain list, as a validation exercise (not an exact match requirement).

### Chapter 5 — Business Services and Value Streams

- **Purpose:** Describe what each capability actually produces (a verified case, a delivered intervention, a closed referral) and trace the end-to-end value streams that connect a beneficiary's triggering need to a delivered, measurable outcome.
- **Why it exists:** Capabilities alone describe *ability*; value streams describe *flow*. The ontology's cross-domain relationships (e.g., `case_plan_addressed_by_intervention`, `resource_allocation_allocated_to_case_plan`) are technical renderings of value-stream connections that should first be describable in a sentence a non-technical stakeholder could follow.
- **Dependencies:** Chapter 4.
- **Expected output:** A small number of named, end-to-end value stream narratives (e.g., "Emergency Shelter Response," "Sustainable Livelihood Pathway"), each tracing which capabilities it activates in what order.

### Chapter 6 — Intervention Categories

- **Purpose:** Describe, at the business level, the broad kinds of assistance humanitarian actors provide (immediate relief, rehabilitative support, developmental/sustainable-independence support) and what distinguishes them.
- **Why it exists:** `registration/taxonomy/support-interventions.yaml` and `programs/taxonomy/interventions.yaml` already need this business grounding and currently lack it — `knowledge_layer_roadmap.md` names the support-intervention taxonomy as blocked on "operational input from programme staff," which is precisely the business-level knowledge this chapter should capture before that taxonomy is finalized.
- **Dependencies:** Chapters 3–5.
- **Expected output:** A categorized narrative of intervention types and the business logic distinguishing them (e.g., why an intervention is time-limited vs. sustained), stopping short of any taxonomy encoding.

### Chapter 7 — Operational Objectives and Success

- **Purpose:** State, in business language, what "doing this well" means — dignity preserved, verification integrity, timeliness, non-duplication, long-term recovery — and what evidence would show the system is failing at each.
- **Why it exists:** This is the direct business-level ancestor of the still-unwritten outcome-indicator vocabulary (`knowledge_layer_roadmap.md` "Stage 6," currently blocked pending exactly this kind of cross-domain business agreement).
- **Dependencies:** Chapters 3–6 (success is measured against the lifecycle, capabilities, and intervention types already described).
- **Expected output:** A set of named operational objectives, each with a short explanation of what success and failure look like in human terms, deliberately without any measurement methodology or indicator schema.

### Chapter 8 — Governance and Authority Boundaries (Business Level)

- **Purpose:** Describe, at the business level, who has the authority to make which kinds of decisions (case-level, program-level, organizational-level, cross-organizational/coordination-level) and why those boundaries exist.
- **Why it exists:** The ontology already enforces a technical version of this discipline (ADR-008's single ownership of concepts, `AI_WORKFLOW.md`'s human-approval-required workflow). This chapter is the business-reality justification for why that discipline is the right one — e.g., why a case worker's authority differs from a program director's, independent of any AI system.
- **Dependencies:** Chapters 1, 4, 5 (authority boundaries only make sense relative to actors, capabilities, and the value streams they participate in).
- **Expected output:** A narrative map of decision-authority boundaries in humanitarian organizations generally, which the Business Architecture chapter (a separate, later document) will subsequently formalize into structure.

### Chapter 9 — Boundary Conditions and Regional/Cultural Variation

- **Purpose:** Name explicitly what varies across humanitarian contexts (regional practice, cultural and religious frameworks, resource availability, regulatory environment) versus what the BMP asserts is universal.
- **Why it exists:** The ontology has already had to make this call at least once, concretely — ADR-022 ("Canonical Concepts and Regional Localization Strategy") establishes that regional/localized labels are aliases, never new concepts. That decision was made at the ontology level without, as far as this review can find, a preceding business-level statement of *which humanitarian variations are surface-level labeling and which are substantively different practices*. This chapter closes that gap retroactively and going forward.
- **Dependencies:** All prior chapters (this is a cross-cutting check on everything already described).
- **Expected output:** An explicit universal-vs-variable distinction, chapter by chapter if needed, that ADR-022 and any future regional extension work (e.g., the `extensions/humanitarian/islamic/` content noted in the prior architecture review as currently un-reconciled with the authority matrix) can be checked against.

---

## 7. Knowledge Required (Discovery Topics)

The following are areas where the knowledge needed to author each chapter does not yet clearly exist anywhere in the repository, in written business-language form. These should be resolved — by interview with domain experts, by research, or by explicit provisional-assumption-and-flag — before that chapter is authored.

**For Chapter 1 (Ecosystem):**
- What actor types exist in humanitarian work that the repository's ontology has *not yet* had to model (because no domain needing them has activated yet)? The BMP should not be limited to actors already visible in `shared/taxonomy/persons.yaml` or `donor-resource/`.
- How do informal/community actors (mosque committees, local self-help groups, informal moneylenders — several of which already appear as *taxonomy values* in `registration/taxonomy/situations.yaml`'s debt-source scheme) function as business actors, not just as classification labels?

**For Chapter 2 (Stakeholder tensions):**
- What tensions has the client/domain team already encountered in practice that have not yet surfaced as an ADR? (ADRs currently record *resolved* tensions; unresolved or not-yet-encountered ones are, by definition, undocumented.)

**For Chapter 3 (Lifecycle):**
- Does the business-level lifecycle genuinely match `beneficiary-lifecycle/taxonomy/engagement-stage.yaml`'s stages, or does that taxonomy already contain implementation-driven simplifications that a business-first description would not have produced independently?

**For Chapter 4 (Capabilities):**
- Is the current 13-domain list (registration, verification, needs assessment, case management, etc.) a complete rendering of humanitarian business capabilities, or were some capabilities never modelled because no operational trigger has occurred yet (as `consent-and-privacy`'s Level 2 status suggests may be true elsewhere)?
- What capability, if any, does the current domain list contain that has no clear humanitarian-business justification (i.e., may have been engineering-convenience-driven rather than business-reality-driven)?

**For Chapter 5 (Value streams):**
- Are there value streams humanitarian organizations run that do not cleanly decompose into the capability sequence the ontology currently assumes (e.g., area-level/programmatic response to a community-wide crisis, which `knowledge_layer_roadmap.md`'s Stage 8 gestures at but does not describe as a business process)?

**For Chapter 6 (Intervention categories):**
- What is the actual, programme-validated intervention catalogue? `knowledge_layer_roadmap.md` names this as the single most-cited concrete blocker in the entire roadmap ("cannot be invented by the knowledge layer alone") — it is the most urgent open research topic in this entire blueprint.
- What distinguishes a "time-limited" from a "sustained" intervention in business terms, independent of the household-resilience ontology that currently infers it?

**For Chapter 7 (Success):**
- What does the client/domain team currently use, informally, to judge whether an intervention "worked" — before any formal outcome-indicator vocabulary exists?

**For Chapter 8 (Governance boundaries):**
- Who, in practice (not in the ontology's `AI_WORKFLOW.md` sense, but in a real humanitarian organization's sense), has authority to override a system-generated recommendation, and under what circumstances?

**For Chapter 9 (Variation):**
- What other regional/cultural frameworks beyond the Islamic giving model already partially built (`extensions/humanitarian/islamic/`, `donor-resource/taxonomy/islamic-giving.yaml`) does the project intend to eventually support, and does the client consider them equally universal-with-local-aliasing (per ADR-022) or substantively distinct practices requiring their own business description?

**Additional discovery topics (merged from an archived, invalid review cycle — see `docs/98-archive/`; these four are retained because they are independently grounded in `docs/02-architecture/KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, a document that genuinely exists, not in the invalid review itself):**
- **Anticipatory / predictive need detection** has no home in this blueprint's lifecycle (Ch3) or capability (Ch4) design. `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §1/§17 already names this as the project's stated long-term vision and explicitly out of scope for the current implementation version — the BMP's timeless business description should still name the concept, likely as a future capability or lifecycle stage, even though no version needs it delivered yet.
- **Consent as an explicit business concept**, distinct from the general "dignity" and "control over one's story" language. `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3.2 already elevates consent to a foundational principle; the BMP should name it explicitly (likely in Chapter 2 or Chapter 8) so both documents use consistent vocabulary.
- **Voluntary withdrawal or declined assistance** — a legitimate lifecycle outcome distinct from closure/resolution, not yet named anywhere in this blueprint's lifecycle design.
- **The possibility of inaccurate or fraudulent claims** — `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §17 already scopes fraud/anomaly *engines* as out of scope for the current version while noting light integrity checking exists; the BMP should still name the possibility at the business level (Ch4 Verification, Ch7 Objectives) without prescribing any mechanism.

---

## 8. Open Questions

These are architectural/process questions this blueprint surfaces but cannot resolve on its own — they require a decision from the Human Owner (per `AI_WORKFLOW.md`) before or during BMP authoring:

1. **Sequencing conflict:** Should the Business Master Plan actually wait for PHILOSOPHY.md/PRINCIPLES.md to be written first (per §4's recommended dependency chain), or does the project intend to author them concurrently, accepting the risk of rework if a later-written principle contradicts an already-written BMP chapter?
2. **Retroactive vs. forward-looking scope:** Should the BMP describe humanitarian business reality as a timeless domain description (as this blueprint has assumed throughout), or should it also explicitly account for the fact that a large amount of ontology-level business logic has already been decided via ADRs — i.e., should the BMP be partly a retroactive business-language translation of decisions already made, so nothing already-ratified in the ADR log becomes silently contradicted?
3. **Ownership of the intervention-catalogue gap:** Chapter 6 depends on a programme-validated intervention catalogue that the ontology layer has already flagged as requiring "operational input from programme staff" and has been unable to resolve on its own. Is authoring that catalogue in scope for whoever writes the BMP, or is it a separate discovery workstream the BMP should simply reference as an open dependency?
4. **Relationship to `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`:** The repository (at `docs/02-architecture/KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`) already contains a populated document with "business logic" in its name. Before the new BMP is authored, is this document intended to be superseded by it, to remain as a separate (perhaps more product-oriented) document, or to be a direct input? This should be settled explicitly rather than discovered mid-authoring.

---

## 9. Writing Strategy

- **Author in the chapter order given in §6.** Each chapter's "Dependencies" line is a hard authoring constraint, not a suggestion — Chapter 6 (Intervention Categories) should not be attempted before Chapters 3–5 exist, because it needs the lifecycle and capability vocabulary those chapters establish.
- **Resolve §8's open questions before starting**, not during. In particular, Open Question 1 determines whether this blueprint's own recommended dependency chain (§4) is followed strictly or relaxed.
- **Treat the ADR log as a business-reality source, not just an engineering record.** Wherever a chapter's topic overlaps with a decision already made in `architecture-decisions/`, the chapter should be checked against that ADR for consistency — not to import ontology language, but to make sure the business description doesn't accidentally contradict a decision the client has already ratified for a good business reason.
- **Flag, don't guess, on every Knowledge Required item (§7).** Where a discovery topic in §7 has not actually been resolved by the time a chapter is drafted, the chapter should say so explicitly (a stated open assumption) rather than silently inventing an answer — mirroring the discipline `knowledge_layer_roadmap.md` already uses for the support-intervention taxonomy blocker.
- **Write for the litmus test in §2**, continuously: every drafted paragraph should be checked against "would this sentence be true in a world without Khidmat AI?"

---

## 10. Definition of Done

The Business Master Plan is complete when:

1. All nine chapters in §6 are written, each satisfying its own "Expected output" as designed here.
2. No chapter contains an ontology class name, a YAML file reference, a taxonomy value, a data schema, or any software/AI implementation detail (the §2 litmus test passes for every paragraph).
3. Every item in §7's Knowledge Required list has been either resolved (with its answer reflected in the relevant chapter) or explicitly logged as an open assumption with a named owner for future resolution — none are silently dropped.
4. Every open question in §8 has been explicitly answered by the Human Owner (or delegated decision-maker) and that answer is recorded (as an ADR, if it is an architectural decision, consistent with the project's existing practice).
5. A cross-check has been performed against every existing ADR whose subject matter overlaps a BMP chapter (e.g., ADR-022 against Chapter 9, ADR-006 against Chapter 2/7), confirming no contradiction — documented as a short traceability note per chapter, not a rewrite of the ADRs.
6. The Humanitarian Business Reference Model's author confirms the BMP gives them sufficient, unambiguous business-capability content to begin categorization without needing to independently re-derive business knowledge the BMP should have already captured.
7. A reviewer with no prior exposure to this repository's ontology can read the BMP end-to-end and describe how humanitarian assistance works, without having encountered a single technical or ontological term.
