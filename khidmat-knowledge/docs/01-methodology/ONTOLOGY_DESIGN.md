---
id: DOC-METH-006
title: Khidmat Ontology Design
version: 1.0.0
status: Canonical — governs all ontology design work
owner: Khidmat Governance Board
reviewers: Project Lead, Domain Approval Authority
created: 2026-07-24
last_updated: 2026-07-27
depends_on: docs/00-governance/PROJECT_OVERVIEW.md (v1.0, primary source of truth), docs/00-governance/CONSTITUTION.md (v1.0)
supporting_references: KHIDMAT_AI.md, FOUNDATION.md, GLOSSARY.md, discovery dossiers TD-01 through TD-06
consumed_by: All future ontology design, ontology engineering, and architecture work
layer: 01-methodology
domain: Ontology Design
tags: [ontology, design, canonical, framework]
supersedes: ONTOLOGY_DESIGN.md v0.1.0 (draft framework)
---

# KHIDMAT ONTOLOGY DESIGN

## Preamble — What This Document Is

This document defines **how the Khidmat Humanitarian Ontology will be designed, discovered, validated, and governed**. It is the canonical design reference for all future ontology work.

It deliberately contains **no ontology content**. No entity, relationship, facet, state, event, constraint, taxonomy value, classification of any business concept, or schema appears anywhere in it. Where a humanitarian concept is mentioned, it is mentioned only to illustrate that a design question exists — never to answer it. The ontology itself will be authored later, under this document's rules, and only after the approval gates of Constitution Article XVI are cleared.

**Position in the authority hierarchy (Constitution, Articles XIV–XV).** This document is subordinate to `PROJECT_OVERVIEW.md` and `CONSTITUTION.md`. It originates no new philosophy, principle, or mandate; every rule below elaborates or operationalizes what those documents already establish, and cites its source. It is supreme over all downstream ontology design content, ontology engineering, and architecture: no later document may override or reinterpret it.

**Relationship to prior work.** This document supersedes the v0.1.0 draft framework. Ontology engineering artifacts produced before the Architectural Reset — including any inherited vocabulary carrying enumerated value sets, machine-format relation names, or storage and derivation decisions — are **not binding inputs** to ontology design. They may be consulted as candidate evidence of past thinking, but every concept they name must re-enter through the discovery, evidence, and promotion discipline defined here, exactly as if it had never been modeled. Design must precede engineering (`FOUNDATION.md`, "Why ontology design before ontology engineering"); nothing engineered earlier is grandfathered past that sequence.

**The single idea that shapes everything below.** The mandate (Overview Ch. 2.1, Article I) requires trustworthy, evidence-based understanding of humanitarian reality *before* any decision, recommendation, or automation. An ontology serving that mandate cannot model only what is true of the world; it must also model **what the system is entitled to believe about the world** — what is claimed versus verified, how confident a conclusion is, where uncertainty remains, and where a human must decide (Overview Ch. 2.3, 5.2, 7.2). This is why the required structure contains layers — Cognition, Evidence, Ground Truth Reviews — that a conventional ontology design would omit. They are not extensions. They are the point.

---

## 1. Domain Primitives

### 1.1 What a Domain Primitive Is

A Domain Primitive is one of the small, closed set of **foundational categories of concept** from which the entire ontology is built. A primitive is not a business concept; it is the *kind of thing* a business concept can be. Primitives are the classification axes that make every later modeling decision decidable by rule rather than by the instinct of whoever is authoring that week.

The warrant for this layer comes directly from the Overview (Ch. 5.1): certain forms of knowledge are foundational because *every* humanitarian domain depends on them — the Overview names identity, relationships, evidence, uncertainty, temporal change, and humanitarian context as the minimum structure required to understand reality regardless of domain. Domain Primitives is the design layer where that insight becomes operative: before any domain's concepts are modeled, the ontology must fix the categories that all domains share.

A primitive answers the first question asked of any candidate concept: *what kind of thing is this?* Everything in every Layer (Section 2) must be classifiable under the primitive set. A concept that cannot be classified under any primitive is either evidence that the concept is not yet understood, or evidence that the primitive set is incomplete — and the second possibility is a foundational governance event (Section 7), never a casual edit.

### 1.2 How Primitives Are Discovered

Primitives are **discovered by abstraction from validated business reality, never invented in the abstract**. The discovery procedure is:

1. **Start from evidence, not imagination.** The input material is the validated business knowledge of the project — the discovery dossiers, the resolved Human Owner decisions, and the business foundation documents as they are completed. Primitives are abstracted *from* this material; they are never proposed because a modeling tradition, a textbook upper ontology, or a prior engineering artifact contains them. This is the ontology-design application of "Evidence precedes conclusions" (Article II).
2. **Ask the kind-question repeatedly.** For each validated business concept, ask *what kind of thing is this?* — and then ask the same question of the answer, until answers stop multiplying and begin repeating. The small set of answers that recur across every humanitarian domain examined is the candidate primitive set. The Overview's own foundational list (identity, relationships, evidence, uncertainty, temporal change, context — Ch. 5.1) predicts roughly where this recursion will stabilize, but the actual set must be *derived*, not copied from that prediction.
3. **Test each candidate against the Knowledge Foundation Boundary (Article IV).** A primitive must pass the same admission test as any knowledge: would its omission materially change the understanding of humanitarian reality or the quality, safety, fairness, or appropriateness of a humanitarian decision? A category that fails this test is a convenience, not a primitive.
4. **Test the set as a whole for coverage.** Every currently validated business concept must be classifiable somewhere in the candidate set without forced fit. Any concept left structurally homeless falsifies the set.

### 1.3 What Qualifies as a Primitive

A candidate qualifies as a Domain Primitive only if it satisfies **all** of the following:

- **Abstract.** It is a category of concept, not itself a concept a business catalogue would define. If a future business glossary could sensibly contain an entry for it, it is too concrete to be a primitive.
- **Universal across humanitarian domains.** It must be required whether the domain is health, education, shelter, livelihoods, disaster response, or a domain not yet discovered (Overview Ch. 5.1's layering of foundational versus domain-specific knowledge). A category needed by only one domain belongs to that domain, not to the primitive set.
- **Necessary.** Removing it must leave some class of validated knowledge unclassifiable — not merely awkward to classify. Minimality is a design requirement: every additional primitive multiplies the decisions every future author must make.
- **Evidence-grounded.** At least one validated business concept must already require it. No primitive may exist speculatively, awaiting a concept that might someday need it.
- **Independent of organisation and technology.** Per the governing principle of Ch. 5.1, a primitive must make sense independent of any specific organisation, application, or implementation technology. A category that only makes sense because of how some system stores or processes information is Operational Knowledge and is excluded (Article IV).

### 1.4 Rules Governing the Primitive Set

- **The set is closed.** Once ratified, the primitive list may be extended or amended only through the foundational governance tier (Section 7). An author who encounters a concept that seems to need a new primitive escalates; they do not extend.
- **One primary classification.** Every concept is classified under exactly one primary primitive. Where a concept genuinely appears to require two, that tension is treated as information — evidence that the concept should be decomposed, or that the primitive set needs review — and is escalated rather than resolved by permitting dual classification. This keeps the primitive layer decisive; a classification system under which everything belongs everywhere decides nothing.
- **Primitives are checked against reality.** Every Ground Truth Review (Section 5) includes the standing question: has any concept surfaced by real humanitarian practice failed to classify under the existing primitives? A "yes" is a finding of the highest severity this design recognizes.

**This document does not identify the primitives.** Producing the ratified primitive list is the first authoring act of the ontology itself, performed under this framework, from the discovery procedure of §1.2, and approved per Section 7 and Constitution Article XVI (Package B).

---

## 2. Layers

### 2.0 The Layer System as a Whole

The Layers are the eight kinds of formal thing the ontology is permitted to contain. Every concept admitted to the ontology lives in exactly one layer, is classified under exactly one primitive (§1.4), and got there through the promotion test (§4.2). The layers are peers in one sense — each is a distinct kind of ontological citizen — but they are not independent: several presuppose others, and the movement rules in §2.9 govern how a concept's layer assignment can change as understanding deepens.

The Overview's description of humanitarian reality dictates why precisely these eight exist. Reality is **relational** (meaning emerges from relationships, not isolated records — Ch. 5.1), **continuously evolving** (Ch. 5.1), **multidimensional** (every person exists within interconnected layers of context — Ch. 1.2), **rule-bounded but locally variable** (Ch. 6.1's universal capabilities with locally adaptable execution), and — critically — **observed through evidence, under uncertainty** (Ch. 5.2). Entities, Relationships, Facets, States, Events, Constraints, Cognition, and Coordination Patterns are the minimum set of formal kinds needed to represent a reality with exactly those properties. Remove any one, and some property of humanitarian reality the Overview identifies becomes unrepresentable.

A dependency note, stated once: the order below is the required presentation order. Authoring the actual ontology content will follow dependency — a dimension cannot be designed before the kind of thing it qualifies exists, a transition cannot be designed before the conditions it transitions between exist. Section 4 (Architecture Rules) makes the authoring dependency binding; this section's order is about meaning, not sequence.

### 2.1 Facets

**Purpose.** A Facet is an independently varying **dimension** of something else — a qualification, condition, or aspect that describes part of a thing's situation without being a separate thing itself.

**Why this layer exists.** The Overview establishes that a person exists within many interconnected, continuously changing layers of context (Ch. 1.2), and that two families identical on paper may live in completely different realities. If the only way to express a new dimension of someone's situation were to define a new kind of thing, the ontology would multiply kinds without limit, and each would freeze one moment's understanding into a permanent category. Facets exist so that richness of context can be expressed as *composable, revisable dimensions* — added, revised, superseded, or retired independently, without redefining what the underlying thing fundamentally is.

**How it differs.** A Facet has no identity of its own: it cannot be re-identified across encounters except through the thing it qualifies. The moment a candidate needs to be tracked in its own right over time, it has outgrown this layer (§2.9). A Facet also differs from a State (§2.5): a State is one of an enumerable set of conditions a thing occupies *at a point in its progression*; a Facet is a descriptive dimension that varies continuously and independently of any progression.

**Design obligations.** Because uncertainty, evidence, and competing observations are part of reality itself, not exceptions to be resolved before storage (Ch. 5.1), a Facet is never a bare attribute. Every Facet is designed as an **evidence-bearing assertion**: it must be able to carry its provenance, its time of observation, and its epistemic status (Cognition, §2.7). A dimension of a person's reality that could not answer "who observed this, when, and how sure are we?" would reintroduce exactly the false certainty the mandate exists to prevent.

### 2.2 Entities

**Purpose.** An Entity is a thing with **independent identity that persists through time** — something the rest of the ontology is *about*, and that must be re-identifiable as the same thing across separate observations, conversations, organisations, and years.

**Why this layer exists.** The Overview's central criticism of current systems is that they capture a person as a single point in time rather than as a continuously evolving human journey (Ch. 1.2), and that knowledge resets between programmes because nothing persists (Ch. 1.3). Continuity of understanding — the defining change Khidmat exists to make (Ch. 2.1) — is only possible for things that have durable identity. Entities are the anchors of continuity: everything accumulated (dimensions, relationships, history, evidence) accumulates *on* them.

**How it differs.** Identity is the entire test. An Entity is re-identifiable in its own right; a Facet is only findable through what it qualifies; a Relationship exists only between things that already exist; an Event happened once and is never re-identified as "the same event, continuing." For every Entity kind the ontology later defines, the design must state its **identity criteria** — what makes two encounters an encounter with the *same* thing — because without stated criteria, the deduplication and continuity failures of Ch. 1.1 are rebuilt inside the ontology itself.

**Design obligations.** Each Entity kind must state: its identity criteria; its minimal always-true nature independent of any currently attached Facet; and its primitive classification. Entity kinds are deliberately few. The default answer to "is this a new kind of Entity?" is *no* — most candidate richness is a Facet, a Relationship, or a State of an existing Entity (§4.2).

### 2.3 Relationships

**Purpose.** A Relationship is a **connection between things with identity** — kinship, dependency, membership, provision, participation, proximity — carrying its own meaning, duration, and evidence.

**Why this layer exists.** "Humanitarian reality is deeply relational, where meaning emerges from relationships rather than isolated records" (Ch. 5.1). Understanding one person requires understanding the relationships in which they exist (Ch. 1.2). If connections were mere attributes of the things they connect, the ontology could not say anything *about the connection itself* — that it is claimed but unverified, that it began after a displacement, that it ended — without distorting one of the parties. Relationships are first-class precisely because in humanitarian reality the connection is often the fact that matters most.

**How it differs.** A Relationship has no meaning apart from the things it connects, which distinguishes it from an Entity; but it can carry its own dimensions, evidence, and temporal validity, which distinguishes it from a bare structural link. A claimed family tie and a verified one are different epistemic situations attached to the *same* relationship — representable only if the relationship itself can bear evidence (Ch. 5.2).

**Design obligations.** Every Relationship kind must state: what kinds of thing it connects and whether direction matters; its temporal validity (relationships begin and end — reality is continuously evolving, Ch. 5.1); its expected plurality (whether more than one may hold concurrently, stated explicitly, never assumed); and its epistemic treatment (claimed versus verified, per Cognition). Whether Facets may attach to Relationships as well as Entities is answered affirmatively by design: dimensions of a connection (its strength, its verification status, its history) are real and must be expressible without inventing pseudo-entities to hold them.

### 2.4 Constraints

**Purpose.** A Constraint is a **rule bounding which configurations of the other layers are valid** — what may coexist, what must accompany what, what quantities and combinations reality actually permits.

**Why this layer exists.** Understanding reality includes understanding its regularities. But the Overview is explicit that humanitarian reality is *discovered rather than predefined* (Ch. 5.1), and Ch. 6.1 establishes that universal capabilities coexist with locally variable execution. The gravest constraint-level error is therefore not a missing rule but a **false universal**: a regularity observed in one context silently encoded as if true everywhere. The Constraints layer exists to hold rules *with their scope made explicit*.

**How it differs.** A Constraint is conditional and empirical: it holds because evidence shows reality works this way, here. This distinguishes it categorically from a Pillar (Section 3), which is unconditional and normative — true by the project's founding commitments, in every context, without exception. Misfiling a Pillar as a Constraint makes the non-negotiable overridable; misfiling a local regularity as a universal Constraint encodes one context's reality as everyone's. Both misfilings are named failure modes the promotion test (§4.2) screens for.

**Design obligations.** Every Constraint carries a mandatory **universal-or-variable tag**. A universal tag is a strong empirical claim requiring correspondingly strong evidence (Section 6) and remains flagged *untested* until a Ground Truth Review (Section 5) has checked it against at least one real context. A variable Constraint names the scope in which it holds. No Constraint's scope is ever left implicit.

### 2.5 States

**Purpose.** A State is one of an **enumerable set of conditions** a thing occupies at a point in time within some recognized progression — the stopping points of a journey, catalogued as concepts without reproducing the flow between them.

**Why this layer exists.** The Overview's alternative to transactional aid is the humanitarian *journey*: circumstances evolve, interventions build on one another, recovery progresses or regresses (Ch. 1.3, 9.2). A journey is only understandable if the ontology can express *where in it* something currently is. States make progression representable — and therefore make continuity, re-assessment, and "has this actually improved?" (Ch. 9.2) askable questions.

**How it differs.** A State is enumerable and positional (one of a known set of conditions in a progression); a Facet is a free dimension with no implied progression. An Event is an occurrence *at* a point in time; a State is a condition *across a span* of time. Events and States are designed together but are not the same kind: transitions between States are what Events cause or evidence.

**Design obligations.** Two obligations follow directly from the Overview. First, **plurality**: because a household's needs evolve independently and interventions interrelate (Ch. 4.1's worked example), the design must permit multiple simultaneous States across different aspects of one thing's situation, rather than forcing a single global status — which granularity a State attaches at is a per-concept design decision made under this rule. Second, **epistemic honesty**: a State assignment is the system's current, evidence-based belief about a condition, not an unconditional fact; it carries the same provenance and confidence treatment as any assertion (Ch. 5.2, §2.7). "We believe this situation has stabilized, based on this evidence, as of this date" is the only form of state-claim the mandate permits.

### 2.6 Events

**Purpose.** An Event is an **occurrence at a point in time** — something that happened — which causes, or is evidence for, change in the rest of the model: a transition between States, the beginning or end of a Relationship, the revision of a Facet.

**Why this layer exists.** The Overview requires the system to preserve *how circumstances came to exist* — "what events led to the current situation, how previous interventions have influenced future outcomes" (Ch. 1.2), including "significant life events, displacement, crises, or disasters." A model with only current conditions and no occurrences cannot explain anything; explanation is causal history, and Events are its unit. Events are also load-bearing for accountability: every decision must remain auditable after the fact (Article X), which requires an honest record of what actually happened.

**How it differs.** Point-in-time occurrence versus span-of-time condition is the Event/State boundary. An Event, once recorded, is **history**: it is never silently corrected, revised, or deleted. If an Event is later found to rest on a false account, the correction is itself a new occurrence, layered on top, superseding but preserving the original — because "conflicting observations should not be treated as system failures" (Ch. 5.2) and an audit trail that can be rewritten is not an audit trail.

**Design obligations.** Every Event kind must state what it is an occurrence *of* or *about*; what changes it can cause or evidence; and its evidential character — most Events are themselves evidence (a verification visit, an observation, a delivery are simultaneously things that happened and grounds for belief), which is the designed connection point between this layer and Section 6.

### 2.7 Cognition

**Purpose.** The Cognition layer is the ontological representation of the **system's own epistemic condition**: what is claimed versus verified, what confidence a conclusion currently deserves, what evidence would change it, what remains unknown, and where the threshold lies past which the system must stop and defer to human judgment.

**Why this layer exists — stated fully, because it is the least conventional.** The mandate makes understanding a *precondition* of action, and the Constitution makes that precondition law: Article III's four-part Standard of Understanding, and Article VIII's human review rule. These are only enforceable if the ontology can *represent* the facts they depend on. "Sufficient reliable evidence has been gathered" (Article III-a) is checkable only if evidential sufficiency is representable. "Significant uncertainty has been explicitly identified, not concealed" (III-c) is satisfiable only if uncertainty is a first-class, attachable representation — the Overview states plainly that uncertainty and confidence levels belong to the foundational dimensions of humanitarian reality itself (Ch. 1.2), and that levels of "uncertainty, confidence, and verification for every important conclusion" must be captured. If confidence and claim-status lived only in application code, the founding sequence Knowledge → Understanding → Reasoning → Responsible Action would be an implementation convention, revisable by any future engineering team. Cognition exists to make it a structural property of the knowledge itself. This is the layer without which the architecture will fail — because the architecture's entire safety model (thresholds, escalation, human review) would rest on facts the knowledge foundation could not express.

**How it differs.** Cognition asserts nothing about humanitarian reality. Every other layer models the world; Cognition models the *warrant* for what the other layers assert. It is designed as a cross-cutting epistemic treatment that every assertion-bearing element (Facets, Relationships, States, and evidential Events) must carry — not as a parallel catalogue of business concepts, and not as a place where any business concept is ever defined.

**Design obligations.** The Cognition layer must make representable, at minimum: the distinction between an assertion made and an assertion the system is entitled to rely on (the claim/accepted-conclusion distinction of Ch. 5.2, where a conclusion becomes "operationally accepted" yet "remains open to revision"); a confidence treatment whose form is qualitative and evidence-traceable rather than an unexplainable score (bias mitigation and explainability requirements, Ch. 8.2, Article X); the explicit representation of *what is unknown* (a gap in understanding is itself knowledge — Ch. 2.3's requirement that "significant uncertainties are explicitly identified rather than ignored"); and the representability of the Article VIII threshold — the fact *that* a given conclusion's consequence class requires human review must be expressible in the knowledge itself, while the operational mechanics of escalation (queues, routing, notification) are Operational Knowledge and are excluded (Ch. 7.2).

### 2.8 Coordination Patterns

**Purpose.** A Coordination Pattern is a **recurring, recognizable configuration involving multiple parties and their relationships, states, and events over time** — the formal representation of how understanding and responsibility move across organisational boundaries: a handoff that carries accumulated understanding forward, a shared response by many actors to one situation, an escalation from insufficient confidence to human judgment.

**Why this layer exists.** Cross-Organisational Coordination is one of the Overview's cross-cutting capabilities (Ch. 6.1), and the entire long-term vision is an ecosystem in which understanding accumulates *across* organisations instead of resetting per programme (Ch. 3.2, 9.1). Fragmentation — each organisation solving its slice in isolation — is the root failure of Ch. 1.1. If the ontology could describe individual situations but not the recurring multi-party shapes through which organisations share and act on understanding, it would model the very fragmentation it exists to overcome.

**How it differs, and a boundary that must be actively policed.** A Coordination Pattern is a *shape*, not a procedure. It names which kinds of parties, relationships, states, and events recur together and what constraints and confidence thresholds the configuration carries. It never specifies execution: no sequencing mechanics, no task logic, no automation instruction. How any organisation operationalizes a pattern is Operational Knowledge (Ch. 6.1's explicit rule: the universal capability is shared; the workflow is local). This layer sits closest to the automation boundary and therefore receives the strictest review attention (Section 7): the recurring failure to guard against is a pattern description that quietly becomes a workflow specification.

**How it depends.** Coordination Patterns compose everything above; they are necessarily the last-designed layer for any given area of the ontology.

### 2.9 How Concepts Move Between Layers

Layer assignment is a *finding about reality*, and like every finding it is revisable under evidence (Ch. 5.2). Movement between layers is governed by three rules:

1. **Initial placement is decided by the promotion test** (§4.2), applied to the evidence gathered about the concept — never by analogy to how a similar-sounding concept was placed, and never by inheritance from prior engineering artifacts.
2. **Reclassification is triggered by evidence, in either direction.** A dimension that field reality shows must be re-identified and tracked in its own right has outgrown Facet status; a kind of thing that in practice is never re-identified independently was never really an Entity; a rule tagged universal that fails in one real context becomes variable (§2.4, Section 5). The test is always the same: what does the evidence now show this thing to *be*?
3. **Movement is a governed, recorded change — never a silent edit.** Reclassification alters what every dependent concept may assume, so it proceeds through the governance tier appropriate to its blast radius (Section 7), and the concept's history — including its former classification and the evidence that changed it — is preserved under the same no-silent-rewriting discipline as Events (§2.6). The ontology's understanding of reality improves the same way the system's understanding of a family does: by revision that leaves an honest trail, not by replacement that pretends the earlier belief never existed.

---

## 3. Pillars

Pillars are the **unconditional commitments every ontology decision must satisfy**. They are not additional principles — Article II forbids adding to the five foundational principles — but the five principles and the mandate, translated into binding tests for ontology design. Every candidate primitive, layer concept, constraint, pattern, and rule is checked against the Pillars before acceptance; nothing is ever checked the other way. A Pillar differs from a Constraint (§2.4) categorically: a Constraint is conditionally true of reality somewhere; a Pillar is true of *this project* everywhere, by its founding commitments, and no context, deployment, or evidence overrides it.

**P1 — Reality only.** *(from the mandate, Article I, and the Knowledge Foundation Boundary, Ch. 5.1 / Article IV.)* The ontology models humanitarian reality — people, relationships, circumstances, evidence, uncertainty, events, context — and nothing else. A concept is admitted only if its omission would materially change the understanding of humanitarian reality or the quality, safety, fairness, or appropriateness of a humanitarian decision. Workflow states, queue mechanics, organisational procedures, and anything that exists only because a particular system operates a particular way are Operational Knowledge and are permanently excluded.

**P2 — Evidence precedes conclusions.** *(Principle 3, Ch. 5.2, Article V.)* No concept enters the ontology, no classification is made, and no constraint is tagged universal, except on identifiable, evaluable evidence. An unsupported assertion is not evidence because it has been written down — this applies to the ontology's own design decisions exactly as it applies to claims about a family.

**P3 — Verification precedes trust.** *(Principle 4, Ch. 5.2.)* The distinction between what has been asserted and what has been verified is structural, everywhere. The ontology must never contain a place where a claim and a verified conclusion are indistinguishable — not in its content, and not in its own design record, where an untested assumption must remain visibly an assumption (Section 6).

**P4 — Uncertainty is represented, never concealed.** *(Principle 2 and the Standard of Understanding, Ch. 2.3 / Article III.)* Uncertainty, confidence, and competing observations are part of reality itself (Ch. 5.1). Every layer that asserts anything must be able to carry the epistemic treatment of §2.7. A design that permits an unqualified, unattributed, confidence-free assertion about a person's reality violates this Pillar regardless of how convenient it is.

**P5 — Human dignity governs representation.** *(Principle 5, Ch. 2.2, Ch. 8, Articles IX–X.)* People are represented as persons within evolving networks of relationships, history, and context — never reduced to a current deficiency, a transaction record, or a demographic category (Ch. 1.3, 8.2). The ontology must be able to represent a person's agency over their own information — what exists about them, consent, correction, challenge (Ch. 8.1) — and need is evaluated through evidence about circumstances, never through assumptions about identity or group membership (Article X).

**P6 — Understanding precedes automation, structurally.** *(Principles 1–2, Ch. 4.2, Articles III, VII, VIII.)* The conditions under which action is permitted — evidential sufficiency, considered dimensions, explicit uncertainty, transparent justification, and the human-review threshold — must be representable *in the knowledge itself* (§2.7), so that the canonical sequence Knowledge → Understanding → Reasoning → Responsible Action is a property of the foundation, not a convention of whatever software consumes it.

**P7 — Continuity through time.** *(Ch. 1.2, 1.3, 2.1.)* The ontology represents journeys, not snapshots. Every design decision is tested against time: identity persists, relationships begin and end, conditions progress and regress, history is preserved, and revision leaves a trail. A design choice that captures the present by discarding the past recreates the knowledge-reset failure Khidmat exists to end.

Amendment of Pillar wording follows the foundational governance tier (Section 7); amendment of Pillar substance is impossible below constitutional level, because each Pillar's substance is the Overview's and the Constitution's, not this document's.

---

## 4. Architecture Rules

These are the conceptual laws every future ontology author obeys. They govern *how* design decisions are made and recorded — not what the ontology says, and not any software architecture.

**AR-1 — The admission test.** Every candidate concept, before anything else, passes the Knowledge Foundation Boundary test (Article IV / P1): would its omission materially change understanding of humanitarian reality or the quality of a humanitarian decision? Fail: it is excluded, whatever its local usefulness. Pass: it proceeds to AR-2. No concept skips this gate, including concepts inherited from prior artifacts or present in sector standards.

**AR-2 — The promotion test.** Layer placement is decided by one fixed, ordered sequence of questions, applied to the evidence about the concept, so that two authors reach the same placement independently:

1. Is it a *rule about valid configurations* rather than a thing, connection, condition, or occurrence? → **Constraint** (then AR-5).
2. Does it *have independent identity that must be re-identified through time*? → **Entity**.
3. Is it an *occurrence at a point in time*? → **Event**.
4. Is it one of an *enumerable set of conditions within a progression* that something occupies across a span of time? → **State**.
5. Is it a *connection between two or more things that already have identity*? → **Relationship**.
6. Does it *qualify something else and vary independently of it, with no identity of its own*? → **Facet**.
7. Is it a *recurring configuration of multiple parties and their relationships, states, and events*? → **Coordination Pattern**.
8. None of the above → it is not modeled; it is either folded into an existing concept, rejected, or escalated as a possible primitive-set gap (§1.4).

An author who cannot answer a question decisively from evidence stops and escalates (AR-9); the test is never resolved by guessing. Before first use on real content, the test itself must be pressure-tested against a deliberately mixed sample of validated business concepts — clear cases and genuinely ambiguous ones — and refined under governance until independent authors converge.

**AR-3 — One concept, one definition, one home.** Every concept has exactly one canonical name, one authoritative definition, one layer, and one primary primitive classification. It may be referenced anywhere but defined only once. Two names for one meaning are merged; one name for two meanings is split. (The project has already paid for this lesson once; the rule makes it law.)

**AR-4 — Epistemic completeness.** No concept's design is complete until its epistemic treatment is stated: what kinds of evidence can support assertions of this concept, how confident the system is ever entitled to be about it, and whether conclusions involving it can meet the Article VIII human-review threshold. A concept whose epistemic treatment cannot be stated is not yet understood well enough to model (Ch. 2.3, applied reflexively).

**AR-5 — No silent universals.** Every Constraint carries an explicit universal-or-variable tag; every universal tag is either backed by a passed Ground Truth Review or visibly marked untested. Absence of a tag blocks acceptance.

**AR-6 — History is never rewritten.** Published concepts are amended, deprecated, split, or superseded through recorded procedures; identifiers are never reused or silently redefined; the design record preserves what was previously believed and what evidence changed it (§2.9, mirroring §2.6).

**AR-7 — Design purity.** No ontology design artifact may contain storage decisions, encoding formats, machine-readable naming conventions, derivation or computation rules, enumerated value lists formatted for machines, or any statement whose truth depends on a technology choice. The litmus test: could this statement be true of any competently designed humanitarian ontology regardless of implementation? If not, it belongs to engineering and is deferred. Prior artifacts violating this rule are inputs to *discovery*, never to design.

**AR-8 — Business language, business derivation.** Every concept is named and defined in humanitarian business language, traceable to evidence about humanitarian reality. No part of the ontology is organized around organisational departments, software modules, or the functional categories of existing NGO systems (Article VI) — the fragmentation of Ch. 1.1 must not be reproduced as structure.

**AR-9 — Flag, don't guess.** Any unresolved classification, any apparent Pillar conflict, any primitive-set gap, and any contradiction between evidence sources is recorded and escalated through Sections 6 and 7. Silent resolution of a genuine open question is a design defect even when the silent answer happens to be right.

**AR-10 — Dependency-ordered authoring.** Ontology content is authored in dependency order: primitives before layers; things with identity before the dimensions, connections, conditions, and occurrences that presuppose them; constraints after the configurations they bound; patterns last. Presentation order (Section 2) is unaffected.

**AR-11 — Reality strata over organisational strata.** No layer content may be named, grouped, or scoped by an operational domain. Domain provenance is recorded as metadata only. Where a concept appears in more than one domain, the ontology names it once, by what it is in reality, never by which domain discovered it.

*Why this rule exists, stated because it is the newest and least obvious.* AR-8 forbids the ontology from being organised around organisational departments, and derives that prohibition from Article VI and from the fragmentation diagnosed in Overview Ch1.1. AR-8 governs the ontology's own structure. It says nothing about the structure of the material the ontology is authored *from* — and that material is departmentally scoped: Stage 5 discovery is organised as Registration, Case Management, Programme Management, Resource & Logistics, Accountability & Evaluation, Coordination, Partner Management, which is substantially the functional decomposition Ch1.1 names as the sector's failure. Concept inventories, relationship lists and event lists all inherit that cut.

An author working faithfully from those inputs, obeying AR-8's letter, can still reproduce the fragmentation — by carrying forward a Case-Management-shaped person alongside a Registration-shaped identity, or a Logistics-shaped delivery alongside a Case-shaped one, because that is how the inputs are filed. AR-11 closes that path. The discovery domains remain the correct record of *where knowledge was found*; they are not permitted to become the shape of *what is known*.

*Applying it.* Before layer authoring begins, the concept inventory is re-indexed by what each concept is about — the person and the social units they exist within; their circumstances; the warrant for what is believed about them; the response made; the institutions acting; the coordination between them — and each concept retains its discovering domain as a provenance note. Two concepts differing only in the domain that named them are one concept under AR-3 and are merged. A concept that cannot be stated without naming an operational domain has not yet been separated from the process that produced it, and is escalated under AR-9 rather than admitted.

---

## 5. Ground Truth Reviews

A Ground Truth Review is the formal check of ontology content against **lived humanitarian reality** — not against literature, standards, or the project's own prior documents. It exists because humanitarian reality is *discovered rather than predefined* (Ch. 5.1), and because the domain discovery procedure the Constitution mandates already requires exactly this: engagement "directly through domain experts, field practitioners, and observed practice, before any structural modeling begins" (Article XI-b). Ground Truth Reviews are that requirement applied to ontology design — no new review machinery is invented beyond what the Constitution and Overview already demand.

**What is reviewed.** Three things, corresponding to the three ways a designed ontology can be wrong about reality: (a) the primitive set — has practice surfaced anything unclassifiable (§1.4)? (b) concept definitions and layer placements — do they match how the reality they model actually behaves, including how affected people themselves would describe their own situation? (c) universal Constraint tags — does the rule actually hold in the specific real context examined (AR-5)?

**Who constitutes ground truth.** Two sources, both required over time because they answer different questions (Ch. 6.2's research step; Ch. 8.1's agency commitments): domain experts and field practitioners, who validate whether the model matches humanitarian practice; and, wherever consent and context responsibly allow, the people the ontology models, who validate whether it matches lived reality as they experience it. The Overview's definition of success is stated in terms of the second (Ch. 9.2); a review discipline that only ever consulted the first would validate the sector's view of people rather than people's reality.

**When reviews occur.** At three trigger points, all already present in the canonical documents: before concepts of a domain are formally included (the Review step, Article XI-d); when the system encounters reality the current foundation cannot represent — an unrepresentable situation is potential evidence the foundation must grow (Ch. 7.2, 9.1); and recurringly, because reality is continuously evolving and a model validated once is not validated forever (Ch. 5.1, 9.1).

**Disposition of findings.** Where ground truth and the model conflict, **reality wins and the model is corrected** — reality sits above every document in the authority hierarchy (Article XIV), and the correction follows §2.9's movement rules and Section 7's governance. Every review records what was tested against what, so untested content remains visibly untested (P3 applied to the ontology's own claims) — this record is the same assumption-and-evidence discipline of Section 6, not a new apparatus.

**A standing honesty requirement.** Until a channel to practitioners and affected communities exists, no Ground Truth Review can pass, and content dependent on one — every universal Constraint tag above all — remains marked untested, however strong its documentary evidence. Literature corroboration is evidence (Section 6); it is not ground truth. This limitation is recorded, not worked around.

---

## 6. Evidence

Ontology design decisions are humanitarian conclusions about what reality contains, and they are held to the same evidentiary discipline the Overview demands for conclusions about a family (Ch. 5.2, Article V). This section governs the evidence *for the ontology's own design* — what justifies admitting, defining, classifying, and tagging concepts.

**What counts as evidence.** An observation, document, testimony, standard, or record whose origin can be identified and evaluated (Article V). An assertion in any prior project artifact — including frozen ones — is not evidence for a design decision merely because it was recorded; its provenance must itself be evaluable. Evidence for design decisions is weighed by the same factors as all evidence in Khidmat: source credibility, method of collection, relevance, timeliness, completeness, corroboration, and consistency with other trusted evidence.

**Evidence requirements scale with commitment.** The more structural the decision, the stronger the required evidence, because the cost of a wrong structural commitment compounds (Ch. 5.1's warning against premature structural commitment):

- *Admitting a concept* (AR-1) requires evidence that the concept exists in humanitarian reality and materially affects understanding or decisions — independent corroboration from more than one source family, not a single mention.
- *Layer placement* (AR-2) requires evidence about the concept's actual behaviour — identity, variation, duration, recurrence — sufficient to answer the promotion test's questions decisively.
- *A universal Constraint tag* requires the strongest case: corroboration across contexts *and* a passed Ground Truth Review; documentary evidence alone leaves the tag marked untested (Section 5).
- *A primitive* requires all of the above plus the coverage test of §1.2.

**Confidence.** Every design decision carries a declared confidence — qualitative, justified by the evidence factors above, and traceable to the specific evidence weighed (explainability, Article X, applied to design). Confidence is never implied by a decision's mere presence in the document. Where evidence is inadequate but progress requires a working position, the position is recorded as an **assumption** — with its owner and the condition that would overturn it — and remains visibly an assumption until evidence resolves it (P3; this is the discipline the discovery phase's assumption register already practices, continued unchanged into design).

**Contradiction handling.** Conflicting evidence about reality is a natural consequence of observing complexity from different perspectives, not a failure (Ch. 5.2). When sources conflict about what reality contains or how it behaves: both observations are preserved with their provenance; the contradiction is recorded, not smoothed over; no side is discarded merely to produce a single answer; resolution comes only from further evidence, a Ground Truth Review, or — where the contradiction blocks progress and evidence cannot presently resolve it — a recorded Human Owner decision, which settles the design position while leaving the underlying evidence trail intact and revisable. A design decision that quietly picked a winner without recording the conflict violates AR-9 and is defective regardless of whether it picked correctly.

---

## 7. Governance

Ontology governance answers one question: **who may change what, under how much scrutiny**. It operates entirely within the authority structure the Constitution already establishes; nothing here creates new bodies or organisational workflows.

**Authority.** The authority hierarchy of Article XIV binds all ontology work: Reality above the Project Overview, above the Constitution, above this document, above all ontology content, above everything engineered from it. Within that hierarchy: the **Domain Approval Authority** (Article XVII — the Project Lead and the designated human owners of the architectural review board) holds approval authority over ontology design content, including the Package B gate (Article XVI: Domain Primitives and Ontology Layers only, with all further work blocked until approved). The **Audit Authority** (Article XVIII) may inspect the evidence chain behind any ontology design decision and suspend downstream work that cannot trace its reasoning to verified humanitarian business reality. Admission of any new humanitarian domain's concepts follows Article XI's four-step procedure without exception.

**Tiers of change.** Not every change is the same order of decision. Scrutiny scales with blast radius — the same reasoning by which the Constitution reserves different decisions to different authorities:

- **Tier 1 — Content changes within settled structure.** Refining a definition, adding a dimension to an already-accepted concept, revising a variable Constraint's stated scope. Reviewed against the Pillars and Architecture Rules; recorded; approvable within the ontology design process itself.
- **Tier 2 — Structural changes.** Admitting a new concept to any layer, reclassifying a concept between layers (§2.9), retagging a Constraint universal, deprecating or splitting a published concept. Requires the full evidence discipline of Section 6, a consistency review against existing content (Article XI-d), and Domain Approval Authority approval. Coordination Patterns receive Tier 2 scrutiny at minimum for any change, given their proximity to the automation boundary (§2.8).
- **Tier 3 — Foundational changes.** Amending the primitive set, a Pillar's wording, an Architecture Rule, or this document. Rare and high-consequence by design: requires demonstration that the change is consistent with the Overview and Constitution (which it cannot override — Article XIV), formal written decision by the Domain Approval Authority, and recording in the decision ledger (the governance ledger, per Article XVII). No Tier 3 change may violate the Mandate or the five principles (Article XIX).

**Review.** Every proposed change, at every tier, follows the same discipline the project already applies to its documents: it is proposed with its evidence and declared confidence; independently reviewed against the admission test, the promotion test, the Pillars, and existing content; its contradictions and assumptions recorded per Section 6; and formally closed with a recorded disposition. Escalations arrive from three standing sources and may not be resolved informally: Ground Truth Review failures (Section 5), evidence contradictions (Section 6), and author escalations under AR-9.

**Approval.** Approval is explicit, written, and recorded; silence is never approval. A certification issued for content that does not exist or that skipped a gate is void (Article XVI). Once approved, content is stable until changed through this section — no downstream document, engineering effort, or implementation convenience may reinterpret it (Article XIV). The Package B checkpoint is absolute: after Domain Primitives and the Ontology Layers are designed, all work stops until the Project Lead's approval is received.

---

## Closing Statement

This document is the complete design law for the Khidmat Humanitarian Ontology. It defines what kinds of thing the ontology may contain, the tests that decide every placement, the unconditional commitments every decision must satisfy, the evidence and validation discipline that keeps the design honest about reality and about its own uncertainty, and the authority under which any of it may change.

It contains no ontology. The ontology itself begins with the discovery of the Domain Primitives (§1.2) and proceeds in dependency order (AR-10), under the gates of Article XVI — and it models reality only as fast as evidence justifies, because that is the mandate, applied to the foundation itself.
