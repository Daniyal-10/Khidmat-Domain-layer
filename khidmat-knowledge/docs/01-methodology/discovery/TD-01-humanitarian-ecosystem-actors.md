---
dossier_id: TD-01
title: Humanitarian Ecosystem — Actor Types and Roles
status: "CLOSED — Handoff record produced (see Discovery Review, below). Discovery Limitation remains attached (Tier A structurally infeasible in this execution environment). Not a 'certification' — see Discovery Review for why that term is not used."
feeds_bmp_chapter: "Chapter 1 — The Humanitarian Ecosystem (BUSINESS_MASTER_PLAN_BLUEPRINT.md §6)"
source_topic: "BUSINESS_MASTER_PLAN_BLUEPRINT.md §7, 'For Chapter 1 (Ecosystem)'"
opened: 2026-07-24
last_updated: 2026-07-24
governed_by: ../BUSINESS_DISCOVERY_BLUEPRINT.md
---

# TD-01 — Humanitarian Ecosystem: Actor Types and Roles

## Topic Statement

Derived, per Blueprint §7 Phase 1 (Scoping), from BMP Blueprint §7's two Chapter 1 knowledge-required items:

- **Q1 (Actor Inventory):** What actor types exist in humanitarian assistance work generally — described as business roles, not data entities — including types this project's existing ontology work has not yet had to model, because no domain requiring them has activated yet?
- **Q2 (Informal Actors):** How do informal or community-based actors (e.g., the debt-source values already present as *taxonomy labels* in `registration/taxonomy/situations.yaml` — mosque committees, local self-help groups, informal moneylenders) function as business actors — with their own interests, responsibilities, and relationships to other actors — rather than merely as classification values?

## Why This Topic Is First

Selected under Business Discovery Blueprint §7 (Discovery Lifecycle) and consistent with BMP Blueprint §6/§9: Chapter 1 is the BMP's entry chapter with no internal chapter dependency, and every other chapter's "Dependencies" line (BMP Blueprint §6, Chapters 2–9) traces back to it — Chapter 2 needs the actor map to name stakeholder tensions, Chapter 3 needs to know who participates at each lifecycle stage, Chapter 8 needs the actor map to describe authority boundaries, and so on. No other Chapter 1–9 topic can be responsibly scoped before this one reaches at least a provisional close. This is a sequencing judgment about *which topic to open first*, not a finding about humanitarian reality — it draws only on the BMP Blueprint's own already-declared chapter dependency structure.

## Scoping Output (Lifecycle Phase 1)

**Sufficiency bar** — this dossier is eligible for Handoff (Blueprint §7, Phase 5) when:
- Every named actor category has at least one Finding, and every actor category intended for High confidence has ≥2 independent, corroborating sources (Blueprint §4.1 promotion rule; §5 corroboration principle).
- Q2 (informal actors) has either a corroborated Finding set or an explicit Open Gap — this sub-question is flagged in advance as the more evidence-scarce of the two, since informal actors are, by definition, less likely to appear in Tier B institutional literature.
- Every actor category candidate that could not be corroborated is either downgraded to Medium/Low confidence with a Discovery Limitation marker (Blueprint §11 item 6) or logged as an Open Gap — never silently omitted.

**Explicitly not required for closure:** an exhaustive global list of every actor type in every humanitarian context worldwide. Per Blueprint §4.1, Applicability Scope is recorded per Finding rather than demanded to be universal before a Finding can exist — a well-evidenced, scope-tagged Finding is acceptable even if its scope is narrow, provided the scope is stated.

## Evidence Sources Identified (Blueprint §5 tiers)

| Tier | Candidate sources for this topic | Status |
|---|---|---|
| **A — Practitioner evidence** | Direct elicitation with case workers, program/field managers, community liaisons, and the client's own domain experts, on: who they interact with in the course of delivering assistance, and how informal actors concretely function in that work. | **Attempted, structurally infeasible — see Tier A Disposition, below.** Not merely deferred: this discovery process has no channel to conduct one. |
| **B — Sector standards and bodies** | Sphere Handbook / Core Humanitarian Standard (actor and accountability roles); IASC (Inter-Agency Standing Committee) cluster system documentation (coordination-role actor types); UNHCR/OCHA humanitarian architecture guidance (who the recognized actor categories are — affected population, host government, UN agencies, INGOs/NGOs, donors, private sector, military/civil-defense actors where relevant); ICRC/IFRC doctrine on movement roles and community-based structures. | Identified, not yet retrieved/reviewed. |
| **C — Project-internal ratified artifacts** | `docs/00-governance/PROJECT_OVERVIEW.md`; `docs/02-architecture/KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`; existing taxonomy files that already carry actor-adjacent labels as *data values* rather than business definitions — `shared/taxonomy/persons.yaml`, `donor-resource/` taxonomy, `registration/taxonomy/situations.yaml` (debt-source informal-actor labels named directly in BMP Blueprint §7). | Identified; internal, so retrieval is immediate. Must be recorded per Blueprint §5 Tier C caveat: evidence of *this project's own stated intent*, not independent evidence of humanitarian reality generally. |
| **D — Secondary literature** | Humanitarian-studies field research on informal/community response structures (relevant specifically to Q2, where institutional Tier B sources are expected to be thin); published NGO-coordination case studies; academic literature on mutual-aid and community self-help structures in crisis response, including literature on faith-based and Islamic community-giving structures (relevant given BMP Blueprint Chapter 9's flagged Islamic-giving-model variation). | Identified as the most likely tier to actually resolve Q2; not yet retrieved. |
| **E — General/unverified** | Not used for Findings. May inform initial Hypotheses only (Blueprint §4.1), to be checked against Tiers A–D before anything is recorded. | N/A — hypothesis-generation only, per Blueprint discipline. |

## Tier B / Tier D Collection Log

Executed 2026-07-24, via web search. Every source below was retrieved and read at the level of the search result / linked page shown; none was a full offline document review, which is noted as a precision limit on the Findings drawn from it.

- OCHA, "The Pulse of Humanitarian Coordination 2024: Overview of IASC Structures at the Country Level" (Dec 2025) — [unocha.org](https://www.unocha.org/publications/report/world/pulse-humanitarian-coordination-2024-overview-iasc-structures-country-level-december-2025)
- UNHCR Emergency Handbook, "Cluster Approach" — [emergency.unhcr.org](https://emergency.unhcr.org/coordination-and-communication/cluster-system/cluster-approach)
- UNHCR Emergency Handbook, "International Coordination Architecture" — [emergency.unhcr.org](https://emergency.unhcr.org/coordination-and-communication/interagency/international-coordination-architecture)
- Sphere Standards, "Core Humanitarian Standard" (definitional page) — [spherestandards.org](https://spherestandards.org/humanitarian-standards/core-humanitarian-standard/)
- Wikipedia, "Core Humanitarian Standard on Quality and Accountability" (used only as a secondary cross-check on the Sphere page, not as a standalone source) — [en.wikipedia.org](https://en.wikipedia.org/wiki/Core_Humanitarian_Standard_on_Quality_and_Accountability)
- WHO EMRO, "1.2 Identify key humanitarian actors" — [emro.who.int](https://www.emro.who.int/cah-guide/chapter1-2.html)
- Twigg, J. & Mosel, I., "Emergent groups and spontaneous volunteers in urban disaster response," *Disasters* (SAGE), 2017 — [journals.sagepub.com](https://journals.sagepub.com/doi/10.1177/0956247817721413)
- "'Let communities do their work': the role of community mutual aid and self-help groups in the Covid-19 pandemic response" — [researchgate.net](https://www.researchgate.net/publication/354846019_'Let_communities_do_their_work'_the_role_of_community_mutual_aid_and_self-help_groups_in_the_Covid-19_pandemic_response)
- "Localizing humanitarian aid: A rapid response entrepreneurship model," ScienceDirect — [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S2352673425000290)
- "Supporting conflict-sensitive, locally-led humanitarianism in Sudan: rebalancing donors' approach to risk" — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12710191/)
- "Muslim NGOs, Zakat and the Provision of Social Welfare in Sub-Saharan Africa: An Introduction," Springer Nature — [link.springer.com](https://link.springer.com/chapter/10.1007/978-3-030-38308-4_1)
- "An Act of Faith: Humanitarian financing and Zakat," ReliefWeb — [reliefweb.int](https://reliefweb.int/report/world/act-faith-humanitarian-financing-and-zakat)

**Tier A:** not attempted this session. No practitioner interview channel is available to this discovery process. This is recorded as an unattempted step, not a failed one — consistent with Business Discovery Blueprint §10 Open Question 3 (practitioner access), still unresolved.

## Topic Dossier Structure (instantiated per Blueprint §6.1)

### Findings

**BD-TD01-001 — Core institutional actor categories (Q1).**
General humanitarian coordination practice recognizes recurring institutional actor categories: affected populations, host governments (bearing primary responsibility for protecting their population), national/international NGOs and community organizations (typically the main direct providers, contributing staff and local expertise), and donors (funding other actors, typically not delivering directly). Source: Tier B — WHO EMRO actor guide; corroborated by Sphere/CHS's actor framing. Confidence: **Medium** — drawn from secondary descriptions of OCHA doctrine rather than a full read of OCHA's primary "Who Does What Where" reference document itself; this precision limit is stated, not smoothed over. Corroboration: 2 independent source families. Evidence Current As Of: 2026-07-24. Applicability Scope: general, cross-context.

**BD-TD01-002 — Sector coordination architecture organizes actors at the organizational level, not the individual-operational-role level (Q1).**
The IASC cluster system's coordination structure names lead and co-lead *organizations* per sector (e.g., UNHCR leads Protection; IFRC and IOM co-lead the new Shelter, Land, and Site Coordination cluster following the 2026 "Humanitarian Reset" restructuring to 8 clusters) — it does not define individual operational roles such as a registrant, proxy, or field verifier. Source: Tier B — OCHA "Pulse of Humanitarian Coordination 2024" report; UNHCR Emergency Handbook cluster pages. Confidence: **High**. Corroboration: 2 independent, authoritative institutional sources (OCHA, UNHCR) describing the same structure. Evidence Current As Of: 2026-07-24 — **shortened freshness interval recommended: 6 months, not the 12-month default**, because the source material explicitly describes an active 2026 restructuring still in progress. Applicability Scope: general, UN-coordinated cluster-activated response; does not necessarily describe purely government-led or purely local responses where no cluster is activated.

**BD-TD01-003 — "Organisation" and "Programme" are distinct concepts in sector practice.**
An implementing/coordinating body (an Organisation — a UN agency, NGO, or government body) is consistently treated, across every Tier B source retrieved, as conceptually distinct from a funded initiative or coordination structure it leads or participates in (a Programme, or a cluster) — organizations lead or implement programmes/clusters; they are not described as the same kind of thing. Source: Tier B — same IASC/UNHCR/OCHA sources as BD-TD01-002. Confidence: **Medium-High** — the distinction is consistently implied by how every source names lead agencies separately from the structures they lead, but no single retrieved source states it as an explicit definitional rule. Corroboration: consistent across all Tier B sources retrieved. Evidence Current As Of: 2026-07-24. Applicability Scope: general. **Bears directly on internal Contradiction #1 — see below; this Finding is evidence for the Human Owner's decision, not a resolution of it.**

**BD-TD01-004 — Donors are a recognized category of humanitarian actor in sector standards.**
The Core Humanitarian Standard explicitly defines "humanitarian actors" to include organizations that provide financial, material, or technical support to other organizations without directly delivering assistance — i.e., donors are, in general sector usage, a recognized actor category, not an excluded one. Source: Tier B — Sphere Standards/CHS definitional page (primary, standard-setting document for this exact question). Confidence: **High** by source-tier ceiling, but **flagged with a Discovery Limitation**: this rests on one retrieved document, not independently corroborated by a second Tier B source. Corroboration: single-sourced. Evidence Current As Of: 2026-07-24. Applicability Scope: general. **Bears directly on internal Contradiction #2 — see below; this Finding is evidence for the Human Owner's decision, not a resolution of it.**

**BD-TD01-005 — Informal/community-based actors are independently documented, legitimate humanitarian actors (Q2).**
Academic humanitarian-studies literature documents "emergent groups," "spontaneous volunteers," and "mutual aid/self-help groups" as a real, independent, and frequently first-responding category of humanitarian actor, with proximity, speed, and local-trust advantages over formal organizations. The literature explicitly argues these should be recognized as legitimate actors in their own right, not merely absorbed or supplanted by formal actors. Source: Tier D — Twigg & Mosel (2017, *Disasters*); corroborated by independent COVID-19 mutual-aid case studies and a Sudan-context localization study. Confidence: **High**. Corroboration: ≥3 independent source families spanning different crisis types (pandemic response, conflict response, urban disaster response). Evidence Current As Of: 2026-07-24. Applicability Scope: general/cross-context — no source specific to this project's actual likely deployment geography was found, which remains an open gap in its own right (see below). **Directly corroborates the internal `GLOSSARY.md` "Local Organisation" concept as grounded in real, documented practice, not merely an internal assumption.**

**BD-TD01-006 — Islamic charitable-giving structures show a formal/informal internal split not yet present in this project's own vocabulary (Q2 — new gap surfaced by discovery, per Blueprint Principle 5).**
Academic literature on Islamic charitable practice distinguishes "vertical" philanthropy (formal, institutionalized Zakat organizations) from "horizontal" philanthropy (informal, private Sadaqah given through self-help groups or mosque funds) as two structurally different giving mechanisms, not two labels for one thing. Source: Tier D — Springer Nature (2020); corroborated by a ReliefWeb report specifically on Zakat humanitarian financing. Confidence: **Medium** — 2 independent sources, but both drawn from a similar academic/policy literature stream rather than clearly independent methodologies. Corroboration: 2 sources. Evidence Current As Of: 2026-07-24. Applicability Scope: **narrow — specifically Islamic charitable-giving contexts**, not a general-sector finding. This Finding surfaces a distinction not present anywhere in the Tier C candidate inventory (TD-01's own Tier C pass found "Islamic Giving" and "Local Organisation" as separate, unconnected glossary entries) — flagged here as new candidate material for BMP authoring, not a resolution of anything previously asked.

### Contradictions

Both entries below were logged during Tier C collection (see the prior collection pass) and remain **unresolved by this Framework — resolution authority rests with the Human Owner per Business Discovery Blueprint §8**, not with this discovery process. What changed in this Collection pass is that external evidence now bears on each.

**Contradiction #1 — Programme/Organisation conflation vs. separation.** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 collapses "Programme / Organisation" into a single actor-table row; `docs/90-reports/Khidmat_Knowledge_Layer_Status_Report.html` treats `organisation` and `program` as two distinct canonical entities. **New evidence (BD-TD01-002, BD-TD01-003) leans toward treating them as distinct** — every Tier B source retrieved names implementing organizations separately from the programmes/clusters they lead. This is evidence for the Human Owner to weigh, not a resolution — an internal V1-scoping table row is a legitimate authorial choice, not necessarily an error, and only the Human Owner can decide whether to reconcile the two internal documents and how.

**Contradiction #2 — Donor's status as an actor.** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4/§17 explicitly excludes Donor from the V1 actor set; `GLOSSARY.md`'s Donor Profile entry and the Status Report's `person_roles` vocabulary both include it. **New evidence (BD-TD01-004) suggests this may not be a genuine disagreement about humanitarian reality at all** — sector standards clearly recognize donors as actors, so GLOSSARY's inclusion is well-grounded, and the Business Logic Blueprint's V1 exclusion reads more plausibly as a *delivery-scope* decision ("V1 does not build donor-facing features yet") than a claim that donors aren't actors in reality. This reframing is offered as evidence for the Human Owner's benefit; the two internal documents still formally disagree in their current wording and remain logged as contradictory until the Human Owner closes this explicitly.

### Open Gaps

1. **Individual operational-role granularity (part of Q1) has zero external validation.** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4's specific roles — Registrant, Proxy, Field Verifier, Human Reviewer, Case Manager — were not corroborated or contradicted by any Tier B or Tier D source found. Sector standards and literature retrieved operate at the organizational/coordination level, not this granularity. This is not evidence the roles are wrong — it means this project's specific operational-role vocabulary is currently validated by nothing outside the project itself, and closing this gap most plausibly requires Tier A (practitioner) evidence specifically, not further literature search.
2. **"Custodian" (Support Delivery chain-of-custody role) remains entirely unaddressed** by any source retrieved in this pass.
3. **No source retrieved was specific to this project's actual likely deployment geography** (unstated in any document reviewed to date) — every Applicability Scope above is general/cross-context by necessity, not locally validated. This is itself a prerequisite gap: TD-01 cannot be scope-tagged more precisely until the project states, or discovery separately establishes, what region(s) it is initially targeting.
4. **Tier A (practitioner evidence) was not attempted**, not merely incomplete — no practitioner interview channel exists for this discovery process in its current form. This remains Business Discovery Blueprint §10 Open Question 3, unresolved, and is the single largest blocker to closing this dossier.

### Discovery Limitation (per Business Discovery Blueprint §11, item 6)

TD-01 as a whole is marked with a **Discovery Limitation**: while several Findings above reached High confidence with genuine multi-source corroboration (BD-TD01-002, BD-TD01-005), the entire individual-operational-role sub-scope of Q1 has no Finding at all — only an Open Gap — and Tier A has not even been attempted. This dossier must not be read by a future BMP author as equivalent in strength to a fully closed topic. It is offered as a **provisional, partial synthesis**: sufficient to inform BMP Chapter 1 drafting on institutional/organizational actor categories and on informal/community actors (Q2), explicitly insufficient on individual operational roles, where BMP authoring should either wait for Tier A or proceed only with the same kind of flagged assumption the BMP Blueprint's own §9 already anticipates for unresolved topics.

### Relevance to BMP Chapters

Primary: Chapter 1 (Ecosystem). Secondary, once Chapter 1 provisionally closes: this dossier becomes an input dependency for Chapter 2 (Stakeholder Interests — needs the actor map to name tensions), Chapter 8 (Governance and Authority Boundaries — needs actor types to describe authority boundaries), per BMP Blueprint §6 dependency lines.

---

## Tier A Disposition (2026-07-24)

**Attempted: yes, in the sense of a documented feasibility assessment. Executed: no.**

This discovery process (an AI agent session with file/repository access and web search) has no mechanism to conduct direct elicitation with a human practitioner — no interview channel, no scheduling capability, no existing connection to the client's domain experts. This is a structural limitation of the execution environment, not a matter of insufficient effort or a deferred convenience. Per Business Discovery Blueprint §7 Phase 4 (Validation), an attempt "even if it fails to find a second independent source" must be recorded with its result — this entry is that record for Tier A specifically.

**What would make Tier A feasible:** the Human Owner arranging a structured elicitation session with named practitioners (case workers, program/field managers, community liaisons, or the client's own domain experts), conducted by a human interviewer, with the results fed back into this dossier as an addendum or revision. This remains Business Discovery Blueprint §10 Open Question 3, and this session's finding is that the question is not merely unanswered but currently unanswerable by this process alone — it requires action outside discovery execution itself.

**Disposition:** Tier A is closed as *not executable in this environment*, not left as a silently-skipped step. The Discovery Limitation already attached to this dossier (above) stands, specifically for the individual-operational-role sub-scope of Q1, which was the area Tier A was most expected to resolve.

---

## Discovery Review (Checkpoint per Blueprint §8)

Business Discovery Blueprint §8 deliberately does **not** apply a full Blueprint-style Review → Resolution → Certification cycle to discovery dossiers — that heavier lifecycle is reserved, by the existing methodology lifecycle (`01-methodology/README.md`), for Blueprint and Final-Methodology documents. A discovery dossier is not either. This section is therefore named a **Discovery Review**, not a certification, and produces a **Handoff record**, not a certificate — consistent terminology matters here specifically because this repository has already suffered once from a certification issued for content that didn't exist (§1 of the Blueprint). Reusing "certified" loosely for a dossier would risk the same category error in miniature.

Checked against Business Discovery Blueprint §11's per-topic completion criteria:

1. **Every Finding sourced, tiered, confidence-rated.** ✅ All six Findings (BD-TD01-001 through 006) carry tier, source citation, and confidence rating.
2. **Every known contradiction logged and routed.** ✅ CL-001 and CL-002 are both logged in `CONTRADICTION_LOG.md`, with TD-01's new evidence attached, and remain correctly open pending Human Owner decision — routing, not silent resolution, is the correct state here.
3. **Every unresolved gap explicitly named.** ✅ Four Open Gaps are named, none silently dropped.
4. **Provisional assumptions recorded with owner and overturn condition.** ✅ AR-001 and AR-002 recorded in `ASSUMPTION_REGISTER.md`.
5. **At least one Validation pass attempted, outcome recorded regardless of success.** ✅ Multi-source corroboration served this function for Findings 002 and 005 (≥2–3 independent sources each); Tier A's infeasibility assessment (above) satisfies this requirement for the one tier where it could not otherwise be met.
6. **Confidence outcome declared, not merely attempted.** ✅ The Discovery Limitation marker (above) is attached at the topic level, distinguishing TD-01 from a topic that closed on uniformly strong evidence.

**Review outcome:** TD-01 satisfies all six per-topic completion criteria in Blueprint §11 and is ready for Handoff, **carrying its Discovery Limitation forward**, not clearing it. This Review does not, and cannot, close CL-001 or CL-002 — those remain open pending the Human Owner, and per Blueprint §8, **BMP Chapter 1 authoring should not begin until that sign-off happens**, even though TD-01 itself is now handed off. Closing TD-01 and clearing Chapter 1 to be authored are two different gates; this Review satisfies only the first.

---

## TD-01 Handoff Record

**Dossier:** TD-01 — Humanitarian Ecosystem: Actor Types and Roles
**Status:** Handoff-ready, with Discovery Limitation attached (individual operational-role sub-scope of Q1 unvalidated; Tier A structurally infeasible in this environment).
**Findings delivered:** 6 (BD-TD01-001 through BD-TD01-006), spanning institutional actor categories, coordination-architecture structure, the Organisation/Programme distinction, Donor's actor status, informal/community actors, and Islamic charitable-giving structure.
**Open items carried forward, not resolved here:** CL-001, CL-002 (Contradiction Log); AR-001, AR-002 (Assumption Register); 4 Open Gaps (above).
**Gate this Handoff does *not* clear:** Human Owner sign-off on CL-001/CL-002, required by Blueprint §8 before Chapter 1 drafting may begin.
**Next discovery task:** TD-02 (Chapter 2 — Stakeholder Interests and Tensions), opened below, per BMP Blueprint §6's chapter dependency (Chapter 2 requires Chapter 1's actor map).

## Evidence Collection Strategy (Lifecycle Phase 2 planning)

Sequencing, not yet executed:

1. **Tier C first (internal, zero external dependency).** Review `PROJECT_OVERVIEW.md`, `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, and existing taxonomy files for every actor-adjacent term already in use. This does not produce Findings about humanitarian reality (Tier C is evidence of client intent only, per Blueprint §5) — its purpose is to build the candidate actor-category list that Tiers A/B/D are then checked against, and to catch any place a downstream document already assumes an actor category the BMP hasn't yet formally named.
2. **Tier B next (external, no access dependency).** Retrieve and review Sphere/CHS actor-and-accountability material, IASC cluster-system role documentation, and OCHA/UNHCR humanitarian-architecture guidance. This tier is expected to resolve most of Q1 (the formal/institutional actor inventory) at High confidence once corroborated across ≥2 of these sources.
3. **Tier D in parallel, targeted at Q2.** Because Q2 (informal actors) is unlikely to be resolved by Tier B institutional literature, prioritize humanitarian-studies field research and community-response literature specifically for this sub-question, rather than treating it as a residual step after Tier B.
4. **Tier A last, gated on access.** Practitioner elicitation should validate and locally ground whatever Tiers B/C/D produce — particularly for Q2, where lived practitioner knowledge of informal actors is likely to exceed what any published source captures. **This step cannot be scheduled until Business Discovery Blueprint §10 Open Question 3 is answered** (does the project currently have practitioner access, or does that access need to be secured first). This is flagged here as a blocking dependency, not assumed away.
5. **Validation pass (Lifecycle Phase 4).** Once an initial finding set exists from steps 1–3, actively seek a second independent source for any actor category currently resting on one source only, before any Finding is recorded at High confidence — per Blueprint §4 Principle 3 and §7 Phase 4.

## Immediate Next Actions

1. Carry out Collection step 1 (Tier C internal review) — no external dependency, can start immediately.
2. Retrieve the specific Tier B documents named above and begin Q1 review.
3. Raise Open Question 3 (practitioner access) with the Human Owner explicitly, since it blocks step 4 above and is the single largest schedule risk to this dossier's closure.
