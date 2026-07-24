---
dossier_id: TD-02
title: Stakeholder Interests and Tensions
status: "CLOSED — Handoff record produced. Discovery Limitation attached (Tier A structurally infeasible, as TD-01; non-exhaustive actor-pair coverage; automation/human-oversight tension Tier-C-only, not yet externally validated)."
feeds_bmp_chapter: "Chapter 2 — Stakeholder Interests and Tensions (BUSINESS_MASTER_PLAN_BLUEPRINT.md §6)"
source_topic: "BUSINESS_MASTER_PLAN_BLUEPRINT.md §7, 'For Chapter 2 (Stakeholder tensions)'"
opened: 2026-07-24
last_updated: 2026-07-24
governed_by: ../BUSINESS_DISCOVERY_BLUEPRINT.md
depends_on_dossier: TD-01 (feeds the actor map this topic's tensions are named between)
---

# TD-02 — Stakeholder Interests and Tensions

## Topic Statement

Derived, per Blueprint §7 Phase 1 (Scoping), from BMP Blueprint §7's Chapter 2 knowledge-required item and Chapter 2's own "Expected output" (BMP Blueprint §6):

- **Q1 (Interest mapping):** For each actor category named in TD-01, what does that actor category structurally want from the system of humanitarian assistance — and where do those wants conflict with another actor category's wants, in principle, independent of any specific case?
- **Q2 (Encountered tensions):** What tensions has the client/domain team already encountered in practice that have not yet surfaced as an ADR? (ADRs currently record *resolved* tensions; unresolved or not-yet-encountered ones are, by definition, undocumented — BMP Blueprint §7 names this gap explicitly.)

## Why This Topic Is Next

Per BMP Blueprint §6, Chapter 2's stated dependency is Chapter 1 ("requires the actor map"). TD-01 has been handed off (see its own Handoff Record) with a named Discovery Limitation on individual operational roles, but with sufficient institutional/organizational and informal-actor material to name tensions between actor *categories* at the level Chapter 2 requires. No chapter beyond Chapter 2 should be scoped before this topic reaches at least a provisional close, per the same chapter-ordering discipline TD-01 was opened under.

**Carried-forward caution:** because TD-01's Handoff explicitly did not clear Chapter 1 for authoring (Human Owner sign-off on CL-001/CL-002 is still pending), TD-02 may proceed at the *discovery* level — evidence-gathering does not require Chapter 1 to be authored, only for TD-01's findings to exist — but BMP authoring for either chapter remains blocked on that same sign-off. This dossier is discovery work, not BMP drafting, so it is not itself blocked by that gate.

## Scoping Output (Lifecycle Phase 1)

**Sufficiency bar** — this dossier is eligible for Handoff when:
- At least one named tension exists per pair of actor categories where TD-01 or Tier C material already suggests a structural conflict (e.g., dignity vs. accountability; speed vs. verification rigor — both named as candidate tensions in the BMP Blueprint's own Chapter 2 design).
- Q2 is either answered with tensions traceable to a citable internal source (an existing document naming a principle or a trade-off, even informally) or explicitly logged as an Open Gap — this project has, by its own admission, no ADR log yet (confirmed absent during TD-01's Tier C pass), so Q2 is expected in advance to rest heavily on Tier C narrative rather than a formal decision log.
- Every candidate tension is stated as a genuine structural pull between two legitimate interests, not a problem with an obvious correct answer — per BMP Blueprint Chapter 2's own instruction to *name* tensions, not resolve them.

**Explicitly not required for closure:** resolving any named tension (out of scope for both this dossier and the eventual BMP chapter — BMP Blueprint §2 explicitly excludes AI reasoning/resolution logic from Chapter 2's own scope).

## Evidence Sources Identified (Blueprint §5 tiers)

| Tier | Candidate sources for this topic | Status |
|---|---|---|
| **A — Practitioner evidence** | Direct elicitation on tensions practitioners have actually faced (e.g., a safety flag vs. speed of assistance; a donor reporting requirement vs. a beneficiary's preference for privacy). | Same structural infeasibility as TD-01's Tier A Disposition — not re-litigated here; carried forward as a standing constraint on this discovery process generally, not re-opened per topic. |
| **B — Sector standards and bodies** | Core Humanitarian Standard's own nine Commitments (already identified during TD-01 Tier B collection as bearing on accountability) likely name or imply sector-recognized tensions (e.g., timeliness vs. quality, accountability to donors vs. accountability to affected people); Sphere's Protection Principles. | Identified via TD-01 spillover; not yet reviewed specifically for tension content. |
| **C — Project-internal ratified artifacts** | `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3 ("Foundational Principles" — epistemic humility, consent/dignity/do-no-harm, human oversight, accountability in both directions, fairness/integrity) is candidate material: several of these principles are stated in a form that implies an underlying tension the principle resolves in one direction (e.g., "claims, not facts" implies a speed-vs-certainty tension). `PROJECT_OVERVIEW.md` Ch4.2 ("Dangers of Premature Automation") and Ch8 ("System Ethics") are similarly candidate sources. No ADR log exists in this repository (confirmed by direct search during TD-01), which is itself the expected answer to part of Q2, not an omission to fix. | Identified; internal, immediate retrieval possible. |
| **D — Secondary literature** | Humanitarian-sector literature on accountability tensions (donor accountability vs. beneficiary accountability), the "aid effectiveness vs. speed" literature, and localization-vs-standardization debates (directly relevant given TD-01's Islamic-giving/informal-actor findings, which already suggest a standardization-vs-local-variation axis). | Identified as likely productive, given TD-01's Tier D search already surfaced adjacent material (e.g., locally-led humanitarianism and donor risk-appetite tensions in the Sudan case study). Not yet retrieved for this topic specifically. |
| **E — General/unverified** | Not used for Findings; hypothesis-generation only. | N/A. |

## Scope Validation (Step 1)

Re-checked against the Business Discovery Blueprint before Collection began: Q1 and Q2 remain correctly scoped to *naming* tensions, not resolving them (§3 "What does NOT belong," restated from the BMP Blueprint's own Chapter 2 design). No ontology, taxonomy, schema, or BMP-chapter prose is produced below — every statement is either an internal-document observation (Tier C), an external-source observation (Tier B/D), or an explicitly labeled inference/assumption. Scope confirmed unchanged from the Scoping section above; proceeding to Collection.

## Tier C Collection (Step 2)

Reviewed: `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3 (Foundational Principles); `PROJECT_OVERVIEW.md` Chapters 1, 2, 4, 5, 8; confirmed (again) that `docs/80-decisions/` contains no ADR content, only a scope-defining README.

**Observations** (Tier C — evidence of this project's own stated intent, not independent evidence of humanitarian reality; each is a direct textual observation, not yet an inference):

- **TC2-1.** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3.1 states: *"Everything a registrant tells the system is a claim, not a confirmed fact... Verification converts claims into findings."*
- **TC2-2.** §3.2 states: *"Safety concerns (safeguarding, domestic violence, minors without guardians) take precedence over process."*
- **TC2-3.** §3.3 states: *"The system supports human decisions; it does not replace them... Consequential decisions... remain human decisions with a human accountable for them."*
- **TC2-4.** §3.4 states: *"Accountability runs in both directions. The system is accountable to the people it serves, not only to the organisation."*
- **TC2-5.** `PROJECT_OVERVIEW.md` Ch1.1 states: *"Success is frequently evaluated through operational outputs... because these are easier to report, audit, and fund. These measures are important, but they do not necessarily reflect whether a person's circumstances have genuinely improved."*
- **TC2-6.** `PROJECT_OVERVIEW.md` Ch4.2 states the proportionality rule: *"any decision whose error could materially affect a person's rights, safety, dignity, legal status, eligibility, access to essential services, or long-term wellbeing requires meaningful human review."*
- **TC2-7.** `PROJECT_OVERVIEW.md` Ch8.1 states: consent is preferred, but *"humanitarian necessity may justify the temporary collection or use of information"* under strict discipline, and *"Necessity never becomes a permanent substitute for consent."*
- **TC2-8.** No ADR exists in this repository (direct search, confirmed a second time this session) — this is the expected, not anomalous, answer to Q2's own framing ("tensions... not yet surfaced as an ADR" presupposes an ADR log that could contain them; none exists yet at all).

**Inference drawn from these observations (labeled as inference, not yet a Finding):** each of TC2-1 through TC2-7 is a principle stated in a form that resolves an underlying trade-off in one direction — which implies, but does not by itself externally confirm, that the trade-off itself is a real, recognized tension in humanitarian practice generally, rather than a Khidmat-specific invention. Tier B/D collection below tests this inference.

## Tier B / Tier D Collection (Steps 3–4)

Executed 2026-07-24, via web search, targeting each inferred tension above.

- Emerald Publishing, "The tension between INGOs' accountability to donors' agendas and to the affected population..." — [emerald.com](https://www.emerald.com/ijhrh/article-abstract/16/4/413/125247/The-tension-between-INGOs-accountability-to-donors)
- ODI Humanitarian Practice Network, "Reflections on the accountability revolution" — [odihpn.org](https://odihpn.org/en/publication/reflections-on-the-accountability-revolution/)
- Mohamud, "Lack of accountability, not budget cuts, is the real humanitarian crisis," *Disasters* (Wiley), 2025 — [onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/10.1111/disa.70005)
- IOM, "Accountability to Affected Populations" — [iom.int](https://www.iom.int/resources/accountability-affected-populations)
- ResearchGate, "Information Verification for Humanitarians: A Critical Review" — [researchgate.net](https://www.researchgate.net/publication/343626083_Information_Verification_for_Humanitarians_A_Critical_Review)
- CSIS, "Localizing Humanitarian Action in Africa" — [csis.org](https://www.csis.org/analysis/localizing-humanitarian-action-africa)
- ODI HPN, "Beyond definitional ambiguity: locally led action as baseline, localisation as reform" — [odihpn.org](https://odihpn.org/en/publication/beyond-definitional-ambiguity-locally-led-action-as-baseline-localisation-as-reform/)
- ScienceDirect, "Going local without localization: Power and humanitarian response in the Syrian war" — [sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0305750X23002784)
- ICRC, *Handbook on Data Protection in Humanitarian Action* — [icrc.org](https://www.icrc.org/en/data-protection-humanitarian-action-handbook)
- EJIL:Talk!, "Humanitarian NGOs and international transfer of personal data" — [ejiltalk.org](https://www.ejiltalk.org/humanitarian-ngos-and-international-transfer-of-personal-data-an-attempt-to-reconcile-the-rights-of-data-subjects-with-their-needs-as-affected-populations/)
- Devex, "Is data consent in humanitarian contexts too much to ask?" — [devex.com](https://www.devex.com/news/is-data-consent-in-humanitarian-contexts-too-much-to-ask-93133)

**Tier A:** not attempted for TD-02 specifically. This is the same structural constraint documented in TD-01's Tier A Disposition (no practitioner-elicitation channel exists in this discovery process) — re-confirmed as still applicable, not re-derived from scratch. See TD-01's dossier for the full disposition.

## Findings (Step 11, synthesized from Steps 6–10 below)

**BD-TD02-001 — Donor accountability and affected-population accountability structurally pull in different directions.**
A documented tension exists between humanitarian organizations' accountability to donors (financial reporting, compliance, donor-set priorities) and their accountability to the people they serve (voice, complaint/feedback mechanisms, alignment with actual need), attributed in the literature to unequal power relations between donors, INGOs, and affected people. **Source:** Tier D — Emerald journal article (title itself names this exact tension); corroborated by ODI HPN, *Disasters* (2025), and IOM. **Confidence: High.** Corroboration: ≥4 independent source families (academic journal, sector practice network, peer-reviewed journal, IGO). Evidence Current As Of: 2026-07-24. Applicability Scope: general, cross-context. **Relation to Tier C:** externally corroborates TC2-4 and TC2-5 — this is a recognized sector tension, not a Khidmat-specific framing.

**BD-TD02-002 — Speed and verification/data quality structurally conflict, and sector practice manages rather than resolves the conflict.**
Pressure for rapid response conflicts with the need to verify information before acting; the literature frames this as manageable through accelerated-but-present verification controls (minimum checks, community validation) rather than a binary choice. **Source:** Tier D — ResearchGate critical review; corroborated by expert-framework commentary on accelerated response with minimum controls. **Confidence: Medium-High.** Corroboration: 2 independent source families. Evidence Current As Of: 2026-07-24. Applicability Scope: general. **Relation to Tier C:** externally corroborates TC2-1 — Khidmat's claim/verification-finding split is a documented real-world response pattern to this tension, not an arbitrary design choice.

**BD-TD02-003 — Donor-driven standardization and locally-led legitimacy structurally conflict.**
Donor compliance and reporting requirements (standardized eligibility, beneficiary lists, financial controls) conflict with the flexibility, informal-network legitimacy, and local knowledge that make locally-led response effective; local actors are simultaneously expected to meet donor standards and to leverage the informal legitimacy such standardization can undermine. **Source:** Tier D — CSIS; ODI HPN; ScienceDirect (Syria case study). **Confidence: High.** Corroboration: 3 independent source families. Evidence Current As Of: 2026-07-24. Applicability Scope: general in structure; the Syria source is context-specific and should not be read as evidence this plays out identically everywhere. **New material, not previously named internally** — connects directly to TD-01's informal-actor Findings (BD-TD01-005, BD-TD01-006); flagged for the BMP author's attention as a candidate tension between TD-01's "Local Organisation" concept and any future donor-facing accountability layer.

**BD-TD02-004 — Consent and humanitarian necessity structurally conflict in data collection, and sector guidance already resolves this via a bounded exception.**
Genuine informed consent for personal data collection is frequently infeasible in emergency contexts (vulnerability, security, logistics); sector guidance resolves this via a bounded "necessity" exception rather than abandoning consent or blocking action, and explicitly warns against consent becoming a box-ticking exercise. **Source:** Tier B — ICRC *Handbook on Data Protection in Humanitarian Action* (authoritative primary sector guidance); corroborated by EJIL:Talk!, Devex, Ada Lovelace Institute. **Confidence: High.** Corroboration: 1 primary Tier B source + 3 independent secondary commentaries. Evidence Current As Of: 2026-07-24. Applicability Scope: general. **Relation to Tier C:** strongly corroborates TC2-7 — Khidmat's internal principle ("necessity never becomes a permanent substitute for consent... a bounded exception") already closely mirrors documented sector guidance. Noted as a positive-alignment finding, not merely a gap-filling one.

**Tier-C-only observation, not yet a Tier B/D-corroborated Finding:** the automation-vs-human-oversight tension (TC2-3, TC2-6) was not checked against AI/automation-in-humanitarian-response literature in this collection pass. It is retained as an internal design stance only, not elevated to a Finding — see Open Gaps and AR-004, below.

## Contradictions (Step 9)

No new contradiction was surfaced during TD-02's collection. Every Tier B/D source found corroborated, rather than conflicted with, the internal Tier C material it was checked against. `CONTRADICTION_LOG.md` entries CL-001 and CL-002 (from TD-01) are unrelated to this topic's subject matter and remain open, unaffected by this dossier.

## Assumptions (Step 8)

Two new assumptions recorded in `ASSUMPTION_REGISTER.md` (not silently omitted, not resolved here):

- **AR-003 — Tension coverage is not an exhaustive pairwise check across every TD-01 actor category.** The four Findings above are treated as the structurally significant tensions surfaced by this collection pass, not as proof no other actor-pair tension exists (e.g., Volunteer-vs-Case-Manager or Field-Verifier-vs-Human-Reviewer tensions were not specifically checked). Manufacturing additional tensions merely to achieve pairwise coverage would violate Blueprint Principle 6 (falsifiability) and Principle 7 (no finding for convenience) — so the gap is logged as an assumption instead.
- **AR-004 — Automation-vs-human-oversight is provisionally treated as a legitimate candidate tension on Tier C strength alone.** Not yet corroborated against AI/automation-in-humanitarian-response literature. Provisionally retained because it is explicitly stated as a foundational principle in two independent internal documents (§3.3 and Ch4.2), which is a weaker but non-trivial form of internal corroboration — this is recorded as an assumption specifically because it is *not* yet Tier B/D validated, not because the underlying claim is doubted.

## Open Gaps (Step 10)

1. **Non-exhaustive actor-pair tension coverage** (see AR-003).
2. **Automation-vs-human-oversight tension lacks Tier B/D corroboration** (see AR-004) — recommended as the specific target of a future, narrowly-scoped collection pass (AI/automation-in-humanitarian-response literature specifically, not general accountability literature).
3. **Tier A not attempted**, same structural constraint as TD-01 — see TD-01's Tier A Disposition; applies here without modification.
4. **No source retrieved was specific to this project's actual deployment geography** — same standing gap as TD-01's AR-002; applies to all four Findings above, which are general/cross-context by necessity.

## Discovery Limitation

TD-02 is marked with a **Discovery Limitation**, though a lighter one than TD-01's: all four core Findings reached Medium-High to High confidence with genuine multi-source corroboration — stronger, on average, than TD-01's evidentiary base. The limitation applies specifically to (a) Tier A's continued absence, (b) non-exhaustive actor-pair coverage (AR-003), and (c) the automation-vs-human-oversight tension remaining Tier-C-only (AR-004). A future BMP Chapter 2 author should treat the four core Findings as reasonably well-evidenced, and the automation/human-oversight tension as a named-but-not-yet-externally-validated candidate, not equivalent in strength to the other four.

## Discovery Review (Checkpoint per Blueprint §8, Step 12)

Checked against Business Discovery Blueprint §11's per-topic completion criteria, exactly as applied to TD-01:

1. **Every Finding sourced, tiered, confidence-rated.** ✅ BD-TD02-001 through 004, each with tier, citation, and confidence.
2. **Every known contradiction logged and routed.** ✅ None new; existing CL-001/CL-002 correctly left untouched as unrelated.
3. **Every unresolved gap explicitly named.** ✅ Four Open Gaps named.
4. **Provisional assumptions recorded with owner and overturn condition.** ✅ AR-003, AR-004 added to `ASSUMPTION_REGISTER.md`.
5. **At least one Validation pass attempted, outcome recorded regardless of success.** ✅ Multi-source corroboration (2–4 independent families per Finding) served this function; Tier A's infeasibility is recorded via reference to TD-01's Disposition, not silently skipped.
6. **Confidence outcome declared, not merely attempted.** ✅ Discovery Limitation section above states plainly which parts are strong and which are not.

**Review outcome:** TD-02 satisfies all six per-topic completion criteria and is ready for Handoff, carrying its (lighter) Discovery Limitation forward. As with TD-01, this Review does not clear BMP Chapter 2 for authoring on its own — per Blueprint §8, Chapter 1's still-open Contradiction Log entries (CL-001, CL-002) block Chapter 1 authoring, and Chapter 2 depends on Chapter 1 (BMP Blueprint §6), so **Chapter 2 authoring remains blocked transitively through Chapter 1's unresolved gate**, not through any new gate TD-02 itself introduces.

## TD-02 Handoff Record

**Dossier:** TD-02 — Stakeholder Interests and Tensions
**Status:** Handoff-ready, with Discovery Limitation attached (non-exhaustive actor-pair coverage; automation/human-oversight tension Tier-C-only; Tier A structurally infeasible, as TD-01).
**Findings delivered:** 4 (BD-TD02-001 through BD-TD02-004), spanning donor/beneficiary accountability, speed/verification, standardization/localization, and consent/necessity tensions; 1 additional Tier-C-only observation (automation/human-oversight) retained but not elevated to Finding status.
**Open items carried forward, not resolved here:** AR-003, AR-004 (Assumption Register); 4 Open Gaps (above). No new Contradiction Log entries.
**Gate this Handoff does *not* clear:** BMP Chapter 2 authoring remains blocked, transitively, by TD-01's still-open CL-001/CL-002 Human Owner sign-off (Chapter 2 depends on Chapter 1 per BMP Blueprint §6).
**Next discovery task:** to be opened per the same chapter-dependency discipline — Chapter 3 (The Humanitarian Lifecycle, Business View) depends on Chapters 1–2 (BMP Blueprint §6), so TD-03 would scope Chapter 3's knowledge-required topic next, once instructed to continue.
