---
id: DOC-METH-005
title: Business Discovery — Blueprint
version: 0.1.1
status: Draft for client review
owner: Khidmat Governance Board
reviewers: Core Architecture Team
created: 2026-07-24
last_updated: 2026-07-24 (corrections pass: epistemology, finding traceability, evidence freshness, applicability scope, confidence-outcome completion criterion)
depends_on: [PROJECT_OVERVIEW.md, CONSTITUTION.md, "VISION.md (referenced, not yet authored)", "PHILOSOPHY.md (placeholder)", "PRINCIPLES.md (placeholder)"]
consumed_by: ["Business Master Plan (not yet authored)", "Humanitarian Business Reference Model (not yet authored)"]
layer: 01-methodology
domain: Business Discovery Methodology
tags: [discovery, methodology, evidence, blueprint, client-review, draft]
---

# BUSINESS DISCOVERY — BLUEPRINT

**Type:** Discovery-of-discovery blueprint (not Business Discovery output itself)
**Governs the future conduct of:** Business Discovery — the evidence-gathering activity that precedes and feeds authoring of `docs/01-methodology/BUSINESS_MASTER_PLAN.md`
**Does not contain:** any humanitarian-domain finding, any actor list, any capability, any assumption about what the answers to Business Discovery's questions will be. This document defines *how discovery must be conducted and judged*, not what it will discover.
**Client instruction governing this document:** the client has directed that Business Discovery precede Business Master Plan (BMP) authoring, and that this blueprint design the discovery *process* only — not perform discovery, not write BMP content, not touch ontology, taxonomy, or schema.

---

## 1. Purpose

### Why Business Discovery exists as a distinct activity

The Business Master Plan Blueprint (`BUSINESS_MASTER_PLAN_BLUEPRINT.md`) already identified, chapter by chapter, that the knowledge needed to write the BMP "does not yet clearly exist anywhere in the repository, in written business-language form" (§7, Knowledge Required). That section named nine open discovery topics — one per chapter — and instructed that each "should be resolved — by interview with domain experts, by research, or by explicit provisional-assumption-and-flag — before that chapter is authored." That instruction is correct but incomplete: it names *that* discovery must happen, not *how* discovery should be conducted so its output is trustworthy enough to bear the weight of every downstream document.

This is the gap Business Discovery closes. Without a disciplined discovery method, "resolve by interview with domain experts" collapses in practice into whoever is authoring the BMP that week writing down what seems plausible, sourcing it informally, and never distinguishing a fact corroborated by three independent humanitarian practitioners from a guess that felt right. The repository has already suffered exactly this failure once — the Humanitarian Business Reference Model was certified against content that was never authored (see `docs/01-methodology/README.md`, Methodology Lifecycle correction, and `docs/98-archive/superseded-reviews/`). Business Discovery exists to make sure the *next* failure mode — content that exists but was never actually evidenced — cannot happen instead.

### The question Business Discovery must answer

Not "what does humanitarian assistance look like" (that is the BMP's job, and Business Discovery does not write BMP content). Business Discovery answers a narrower, prior question: **what has this project actually verified about humanitarian reality, from what source, at what confidence, and what remains genuinely unknown?** Its output is not a narrative description of the domain — it is an evidenced, sourced, confidence-rated body of raw material that the BMP's nine chapters can be authored *from*, with every claim traceable to where it came from.

### Audience

- **Primary:** whoever authors the Business Master Plan next — they need raw, sourced findings to write from, not another layer of unsourced narrative.
- **Secondary:** the Human Owner and any client-side domain expert who must be able to check "is this actually true?" against a named source, not against an author's judgment alone.
- **Tertiary:** future auditors (Constitution Article XVIII, reserved) who will need to trace any BMP claim back to evidence if its accuracy is ever challenged.

### How the Business Master Plan depends on it

Every chapter dependency the BMP Blueprint already declared (§6) presumes content to write from. Business Discovery is the activity that produces that content before authoring begins, organized so each BMP chapter's "Expected output" can cite specific discovery findings rather than being drafted from first principles. Where Business Discovery cannot resolve a topic with adequate evidence, the BMP Blueprint's own instruction (§9: "flag, don't guess") remains the fallback — Business Discovery's job is to shrink the number of times that fallback is needed, and to make each remaining flag an honest, recorded gap rather than a silent one.

---

## 2. Governance Positioning — Resolving a Sequencing Tension

**This section must be read before the rest of the blueprint. It surfaces a real conflict rather than resolving it unilaterally.**

Constitution Article XVI (Dependency Hierarchy) states the authoritative order as:

```
Project Overview → Constitution/Philosophy/Principles → Business Master Plan
    → Humanitarian Business Reference Model → Business Architecture
    → Domain Discovery → Ontology Design → Ontology Engineering
```

Article XVI does not name "Business Discovery" as a node. The client's kickoff instruction for this blueprint, by contrast, places Business Discovery as a distinct phase *before* the Business Master Plan, in the sequence: Reality → Business Discovery → Business Master Plan → Humanitarian Business Reference Model → Ontology Design → ... This is not the same document as `DOMAIN_DISCOVERY.md`, which already exists in the repository as an empty stub and is positioned, per the BMP Blueprint (§4) and Article XVI, *after* Business Architecture — it governs "which humanitarian domain is modelled next, and when," a sequencing decision among already-established domains, not first discovery of the domain itself. Conflating the two would misname both.

Two ways to reconcile this without inventing new constitutional authority (which this document does not have — Article XV forbids any methodology document from originating new mandate):

1. **Business Discovery is not a new node in Article XVI.** It is the disciplined method by which the existing "Business Master Plan" node's own prerequisite work — already described, if thinly, in the BMP Blueprint §7 Knowledge Required and §9 Writing Strategy — gets carried out. Under this reading, Business Discovery sits *inside* the Business Master Plan step of Article XVI, not before it, and this blueprint is best understood as an elaboration of BMP Blueprint §7 and §9, not a rival document.
2. **Business Discovery is a new node**, formally inserted between Philosophy/Principles and Business Master Plan, requiring an explicit amendment to Article XVI and a corresponding architectural decision record.

This blueprint proceeds under reading (1) — it treats Business Discovery as the evidence-gathering discipline that operationalizes the Business Master Plan's already-declared prerequisite ("resolve before that chapter is authored"), not as a new constitutionally sequenced document. This avoids amending governance the client has not asked this document to amend, while still giving the client's instruction — "Business Discovery precedes the Business Master Plan" — its full practical effect: no BMP chapter is drafted before its discovery work is done.

**Open governance question for the Human Owner (see also §10):** should reading (1) or (2) be formally ratified? If (2), Article XVI requires amendment and this blueprint's `depends_on`/`consumed_by` frontmatter would need to change accordingly. Business Discovery activity should not wait for that decision — the discipline in §§4–9 below applies either way — but the BMP should not be marked "complete" or "certified" until this question is answered, since certification language differs materially between the two readings.

---

## 3. Scope

### What belongs inside Business Discovery

- Identifying, for each BMP Blueprint §7 Knowledge Required topic (and any additional topic Business Discovery itself surfaces as evidence accumulates), what is already known, from where, and at what confidence.
- Locating, evaluating, and recording evidence: domain-expert interviews, humanitarian-sector literature (UN/OCHA, ICRC, Sphere Standards, published NGO operating manuals), the project's own already-ratified artifacts (`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, existing ADRs, `PROJECT_OVERVIEW.md`), and any client-supplied source material.
- Producing sourced, confidence-rated findings organized by topic, in a form the BMP's chapter authors can cite directly.
- Naming explicit assumptions where evidence is currently insufficient, with an owner and a path to later resolution — never silently filling a gap with an invented "fact."
- Surfacing contradictions between sources, and between sources and existing ratified project artifacts, without resolving them unilaterally — contradictions are logged and routed to the Human Owner (§8).
- Identifying, but not resolving, where a Knowledge Required topic turns out to be broader or different in shape than the BMP Blueprint anticipated (evidence is allowed to challenge the plan that asked for it).

### What does NOT belong inside Business Discovery

- Any Business Master Plan content — no chapter narrative, no "here is what actor types exist" conclusion written in BMP voice. Business Discovery produces the raw, sourced material; the BMP author synthesizes it into the nine chapters.
- Any HBRM, Business Architecture, Ontology Design, taxonomy, schema, or software content.
- Resolution of the §2 governance question or any other open architectural decision — those are routed to the Human Owner, not decided by the discovery process itself.
- Assumptions about what the ontology, taxonomy, or software will eventually need. Business Discovery is answerable only to "what is true of humanitarian reality," per the BMP Blueprint's own litmus test (§2 of that document): could this finding be true in a world where Khidmat AI was never built? If a candidate finding only makes sense because Khidmat AI exists, it is out of scope here.
- Validating or re-litigating repository engineering, governance, or methodology work already marked complete, unless discovery evidence produces a genuine, named contradiction with that work (in which case: log it, route it, do not silently override it).

**Litmus test for every discovery finding:** *Is this something the project has verified, from a named source, or is it something the project currently believes without having checked?* Every finding must be tagged one or the other — there is no third, unmarked category.

---

## 4. Principles of Evidence-Based Discovery

### 4.1 Discovery Epistemology

Business Discovery recognizes exactly four epistemic states for a claim about humanitarian reality. Every claim produced during discovery must sit in one of these states, and only one, at any given time:

- **Hypothesis** — an untested candidate claim, not yet checked against any named source. A hypothesis may be recorded internally to guide Collection (§7, Phase 2) but must never appear in a Topic Dossier's Findings as though it were evidenced.
- **Evidence** — a claim checked against at least one named, tiered source (§5). Evidence alone is not yet a Finding — it is the raw material a Finding is built from.
- **Finding** — evidence that has been tiered, confidence-rated, and recorded in a Topic Dossier (§6.1) per §5's evaluation criteria. A Finding is the only unit the Business Master Plan may cite.
- **Assumption** — a provisional statement adopted only when evidence is insufficient to produce a Finding and forward progress genuinely requires one. An Assumption is never the product of upgrading weak evidence — it is what stands in *only* where no adequate evidence exists, and it is always recorded in the Assumption Register (§6.2), never left implicit inside a Finding.

**Promotion rule:** a claim may move from Hypothesis to Evidence only by being checked against a named source (§5). It may move from Evidence to Finding only once tiered and confidence-rated. Nothing may move directly from Hypothesis to Finding or from Hypothesis to Assumption — an Assumption is a documented absence of evidence, not an untested guess adopted by default. A Finding may later be downgraded back to Assumption status if a Contradiction Log (§6.3) entry undermines its sourcing, but a Finding is never silently reclassified — any such downgrade is itself logged.

### 4.2 Principles

1. **Source before synthesis.** No finding is recorded without a named source. "It is generally known that..." is not a source.
2. **Confidence is explicit, not implied.** Every finding carries a confidence rating (§5) visible to whoever reads it later — a downstream author should never have to guess how much to trust a line of discovery output.
3. **Corroboration outranks authority.** Two independent, weaker sources that agree outweigh one authoritative source asserting alone. A single source, however credentialed, is a lead, not a finding, until corroborated or explicitly flagged as single-sourced.
4. **Absence of evidence is recorded as absence, not as a mild "probably."** If nothing has been found on a topic, Business Discovery says so plainly and names it an open gap, rather than letting a plausible-sounding draft quietly stand in for a missing fact.
5. **Discovery challenges the discovery plan itself.** The BMP Blueprint's nine topics (§7 of that document) are a starting scope, not a ceiling. If evidence surfaces a tenth topic the BMP will need, Business Discovery records and routes it rather than discarding it as out of scope.
6. **Findings are falsifiable.** Every finding must be stated in a form a domain expert could disagree with and say why — not so vague that no future evidence could ever contradict it.
7. **No finding is authored to make a downstream document easier to write.** Convenience for the BMP author is never a reason to round a weak finding up to a strong one.

---

## 5. Evidence Sources and How They Are Evaluated

### Authority tiers

| Tier | Source type | Examples | Default confidence ceiling |
|---|---|---|---|
| **A — Primary practitioner evidence** | Direct testimony from people who currently do the humanitarian work being described | Interviews/structured elicitation with case workers, program managers, community liaisons, the client's own domain experts | High, if corroborated across ≥2 independent practitioners; Medium if single-sourced |
| **B — Recognized sector standards and bodies** | Published, cross-organizationally recognized humanitarian frameworks | Sphere Standards, UN OCHA guidance, ICRC/IFRC operating doctrine, recognized NGO coordination frameworks (e.g., cluster system documentation) | High — these are already cross-validated by the sector, but must still be checked for relevance to this project's specific humanitarian context |
| **C — Project-internal ratified artifacts** | Documents this project has already produced and formally accepted | `PROJECT_OVERVIEW.md`, `CONSTITUTION.md`, `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, existing ADRs | High for what they explicitly state; these are evidence of the *client's* stated intent and existing decisions, not independent evidence of humanitarian reality generally — the distinction must be preserved in how a finding is written up |
| **D — Secondary literature and case studies** | Academic or field-research humanitarian literature, published case studies, sector reports (e.g., from academic humanitarian-studies journals, evaluation reports of past humanitarian programs) | Medium by default; High only if corroborating Tier A or B |
| **E — General or unverified sources** | General web content, unattributed claims, AI-model prior knowledge not traceable to a specific source | Low, always. May be used only to generate hypotheses to check against Tiers A–D — never recorded as a finding on its own |

### Evaluation criteria applied to every source

- **Relevance:** does this source speak to *this* project's humanitarian context (populations, regions, organizational scale), or to humanitarian work in a materially different setting? A finding sourced from a context that differs in a way that plausibly changes the answer must say so.
- **Recency:** humanitarian operating practice changes; a source's date must be recorded, and a stale source (e.g., superseded sector guidance) must be flagged rather than treated as current by default.
- **Independence:** two sources that both cite the same underlying origin are not two corroborating sources — they are one source cited twice. Corroboration requires genuine independence of origin.
- **Position/interest:** does the source have a structural interest in a particular answer (e.g., a donor-side source describing accountability requirements vs. a beneficiary-side source describing dignity concerns — both legitimate, per BMP Blueprint Chapter 2's stakeholder-tension framing, but neither is a neutral arbiter of "the" answer). Interested sources are not discarded — they are recorded *as* representing that interest, consistent with Chapter 2's mandate to name tensions rather than resolve them prematurely.

### Evidence Freshness

A Finding's "Evidence Current As Of" date (§6.1) starts a freshness interval, default **12 months**, during which the Finding may be used for BMP authoring without re-checking. The Human Owner may set a shorter interval for a specific topic at Scoping (§7, Phase 1) where the subject matter is known to change faster (e.g., regionally specific operating conditions). If BMP authoring for a chapter has not begun before a feeding Finding's freshness interval has elapsed, that Finding must undergo a revalidation pass — re-checked against its existing source or a current equivalent — before it may be used; the outcome of that revalidation (confirmed, updated, or superseded) is recorded against the same Finding ID rather than creating an untracked duplicate.

---

## 6. Discovery Artifacts

Business Discovery produces four artifact types, each with a fixed structure so BMP authors can consume them predictably. These are working documents, not certified repository chapters — they may live under a discovery workspace (e.g., a future `docs/01-methodology/discovery/` directory, or equivalent) rather than as top-level methodology documents, since they are inputs to authoring, not authored deliverables themselves. Where they should live physically is itself an open item for the Human Owner (§10) rather than decided here.

### 6.1 Topic Dossier (one per BMP Blueprint §7 topic, plus any topic discovery itself surfaces)

- **Topic statement** — the question being investigated, quoted or closely derived from BMP Blueprint §7.
- **Findings** — each finding as a single falsifiable statement, tagged with:
  - **Finding ID** — a stable identifier, unique within the dossier (e.g. `BD-<topic-code>-<sequence>`), so downstream documents can cite the finding directly rather than re-deriving it from dossier prose.
  - source(s) (tier + citation), confidence (High/Medium/Low per §5), corroboration status.
  - **Evidence Current As Of** — the date the evidence was verified current, per §5's Evidence Freshness rule.
  - **Applicability Scope** — the region, organization type, or humanitarian context the finding was evidenced against, so relevance is preserved as data rather than checked once and discarded.
- **Contradictions** — any place two credible sources disagree, both recorded, neither silently dropped.
- **Open gaps** — what remains unknown, stated plainly, with a suggested next evidence-gathering step if one is apparent.
- **Relevance to BMP chapter(s)** — which of the nine chapters (or which parts of them) this dossier feeds.

### 6.2 Assumption Register

A single running log of every place discovery could not fully resolve a topic and a provisional assumption was made to allow forward progress. Each entry: the assumption, why it was necessary, who made it, what evidence would overturn it, and its current status (open / resolved / superseded). This directly extends the BMP Blueprint's own instruction (§9) that unresolved Knowledge Required items must be "explicitly logged as an open assumption with a named owner," rather than silently dropped — the Assumption Register is where that logging actually happens, so Definition of Done item 3 in the BMP Blueprint has something concrete to check against.

### 6.3 Contradiction Log

Every instance where evidence conflicts — across sources, or between new evidence and an already-ratified project artifact (Tier C). Logged, never auto-resolved by whoever is running discovery. Routed to the Human Owner per §8.

### 6.4 Bias and Risk Log

A running record of where §9's identified risks were observed in practice during discovery (e.g., "only one practitioner interviewed on Chapter 6 intervention categories — single-source risk, flagged"), so the eventual synthesis step can weight or re-verify accordingly.

---

## 7. Discovery Lifecycle

Discovery proceeds in five phases per topic (not five phases for the whole activity at once — topics may be in different phases simultaneously, since the BMP Blueprint's chapter dependencies (§6 of that document) mean some topics can only usefully be investigated once an earlier chapter's topic has reached at least provisional resolution).

1. **Scoping.** Restate the topic precisely from BMP Blueprint §7 (or a newly surfaced topic per Principle 5). Identify candidate sources by tier. Identify what would count as sufficient evidence to close the topic (not aiming for exhaustiveness — aiming for a stated, defensible bar).
2. **Collection.** Gather evidence against the candidate sources. Record every finding immediately in its Topic Dossier as it is found, with source and confidence attached at the moment of capture — not reconstructed afterward from memory.
3. **Synthesis.** Within a topic, resolve corroborating findings into a coherent dossier; flag contradictions rather than picking a winner; identify remaining gaps.
4. **Validation.** Where possible, check synthesized findings against a second, independent source or practitioner before treating them as High confidence. For topics resting on a single practitioner or single document, this phase should actively seek a second source rather than accepting single-sourcing as final.
5. **Handoff.** The Topic Dossier is marked ready for BMP authoring use once it meets the per-topic sufficiency bar set in Scoping, or is explicitly marked "insufficient — proceed only with a flagged assumption," per BMP Blueprint §9.

A topic dossier does not need to reach exhaustive certainty to be handed off — it needs to honestly state what is known, at what confidence, and what is not.

---

## 8. Review and Governance During Discovery

- **No unilateral resolution of contradictions.** Any entry in the Contradiction Log (§6.3) is routed to the Human Owner for a decision before the affected dossier is marked ready for handoff. Business Discovery may recommend a resolution but does not have authority to decide one, consistent with Article XV's prohibition on methodology documents originating new mandate.
- **Periodic checkpoint, not continuous certification.** Given discovery proceeds topic-by-topic and asynchronously, a lightweight checkpoint (a status pass across the Topic Dossiers, Assumption Register, and Contradiction Log) should occur before BMP authoring begins for any chapter whose topics feed it — not a full blueprint-style Review/Resolution/Certification cycle, which the existing methodology lifecycle (`01-methodology/README.md`) reserves for Blueprint and Final-Methodology documents, a category discovery dossiers are not part of.
- **Human Owner sign-off gates BMP authoring start, not each dossier individually.** Requiring sign-off on every dossier would recreate the exact bottleneck discovery exists to avoid; requiring no sign-off at all would recreate the exact ungoverned-certification failure the repository has already experienced once (§1). The correct gate is: before a BMP chapter is drafted, its feeding dossiers must have been checkpointed and any contradictions they raised must have been resolved by the Human Owner.

---

## 9. Risks to Discovery Integrity and Mitigations

| Risk | How it biases discovery | Mitigation |
|---|---|---|
| **Confirmation bias toward the BMP Blueprint's own anticipated topics** | Discovery only looks for evidence that confirms what §7 already guessed, missing what evidence would actually say | Principle 5 (§4): discovery must be willing to surface topics the Blueprint didn't anticipate; Scoping phase explicitly asks "what would disconfirm this" before collection begins |
| **Single-source over-reliance** | A single well-spoken practitioner or one document becomes the de facto "truth" for a whole chapter | Tier-based confidence ceilings (§5) cap single-sourced findings at Medium; Validation phase (§7.4) actively seeks a second source |
| **Availability bias** | Whatever source is easiest to reach (an existing internal document) crowds out harder-to-reach but more representative evidence (field practitioners) | Evaluation criteria (§5) require relevance and independence checks, not just ease of access; Tier C sources are explicitly marked as evidence of client intent, not of humanitarian reality generally |
| **Interest-driven distortion** | A source with a structural stake in a particular answer (e.g., a donor-accountability framework) gets recorded as neutral fact | Position/interest criterion (§5) requires recording the source's structural interest alongside the finding, not stripping it out |
| **Premature closure** | Pressure to "finish discovery and move to the BMP" causes gaps to be quietly rounded up to findings | Principle 4 (§4): absence of evidence must be recorded as absence; Handoff (§7.5) explicitly allows "insufficient — proceed only with a flagged assumption" as a valid, honest outcome |
| **Discovery drifting into synthesis or ontology language** | Whoever runs discovery starts writing BMP-chapter prose or ontology-shaped structure directly into dossiers, collapsing the discovery/authoring boundary | Scope discipline (§3): dossiers record findings, not narrative; the BMP Blueprint's own litmus test (a world without Khidmat AI) is reapplied to every dossier entry |
| **Governance ambiguity (§2) left unresolved indefinitely** | Discovery proceeds for months without the Article XVI question ever being settled, and BMP authoring stalls waiting on it, or worse, proceeds under an unratified assumption | §2's open question is explicitly flagged for near-term Human Owner decision, separate from and not blocking topic-level discovery work, which can proceed under either reading |

---

## 10. Open Questions for the Human Owner

1. **Governance positioning (§2):** does Business Discovery amend Article XVI as a new dependency-chain node, or remain, as this blueprint assumes by default, an elaboration of the Business Master Plan's existing prerequisite work? This should be settled before the BMP is marked complete, even if topic-level discovery proceeds in the meantime.
2. **Where discovery artifacts live:** should Topic Dossiers, the Assumption Register, and the Contradiction Log be repository artifacts (and if so, where — a new `docs/01-methodology/discovery/` directory, or elsewhere), or working documents outside the versioned repository until BMP authoring consumes them?
3. **Who conducts primary-evidence collection (Tier A):** does the project currently have access to humanitarian practitioners for direct interview, or does Business Discovery need to begin by first securing that access (a project-management question this blueprint cannot answer)? If practitioner access is not yet available, several BMP topics — most acutely Chapter 6's intervention catalogue, already named in the BMP Blueprint as "the most urgent open research topic in this entire blueprint" — may need to proceed on Tier B/C/D evidence alone, provisionally, with that limitation explicitly recorded rather than hidden.
4. **Relationship to `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`:** this is the same open question the BMP Blueprint already raised (its §8, Open Question 4) and it is inherited here unresolved — Business Discovery treats that document as a Tier C source in the meantime, without presuming its eventual relationship to the BMP.

---

## 11. Completion Criteria — When Business Discovery (for a given topic) Is Done

A Topic Dossier is ready for BMP-authoring handoff when:

1. Every finding it contains is sourced, tiered, and confidence-rated per §5 — no unsourced claims remain.
2. Every known contradiction has been logged (§6.3) and routed to the Human Owner; none are silently absent from the dossier.
3. Every gap that evidence did not close is explicitly named as a gap, not rounded up into an unstated assumption.
4. Where a provisional assumption was necessary to allow the topic to close, it is recorded in the Assumption Register (§6.2) with an owner and a condition for revisiting it.
5. At least one Validation pass (§7.4) has been attempted — even if it fails to find a second independent source, that attempt and its result are recorded.
6. **Confidence outcome is declared, not just attempted.** If every Finding feeding the topic is Medium or Low confidence — i.e., no Finding reached High confidence through corroboration — the dossier must carry an explicit **Discovery Limitation** marker at the topic level, stating that the topic closed on weaker evidence. A topic marked with a Discovery Limitation is still eligible for handoff (per §7.5, "insufficient — proceed only with a flagged assumption" remains a valid outcome), but it must never appear to a BMP author as equivalent in strength to a topic that closed with corroborated High-confidence Findings.

Business Discovery overall (as a project activity, not a single certifiable document) is sufficiently advanced to permit BMP authoring to begin on a given chapter when every topic feeding that chapter (per BMP Blueprint §7's chapter mapping) has reached the state above — not when every topic across all nine chapters has closed. This allows BMP authoring to proceed chapter-by-chapter as its own feeding topics become ready, consistent with the BMP Blueprint's own chapter-ordered Writing Strategy (§9 of that document), rather than blocking all authoring on the slowest topic across the whole plan.

---

## 12. Explicit Non-Goals (Restated)

This blueprint does not, and must not be read to:

- Perform any Business Discovery finding itself.
- Write, imply, or pre-empt any Business Master Plan content.
- Resolve the Article XVI sequencing question it raises in §2.
- Propose ontology, taxonomy, schema, or software architecture of any kind.
- Assume that any topic named in BMP Blueprint §7 is the complete set discovery must cover — per Principle 5 (§4), that list is a floor, not a ceiling.
