---
dossier_id: TD-02
title: Stakeholder Interests and Tensions
status: Scoping complete — Collection not yet started
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

## Immediate Next Actions

1. Tier C review of `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3 and `PROJECT_OVERVIEW.md` Ch2–Ch4, Ch8, extracting every place a principle is stated in a form that implies a named or implied trade-off — mirroring TD-01's own Tier C-first sequencing.
2. Tier B/D collection targeting CHS's own tension-adjacent commitments and the accountability/localization literature.
3. Tier A: no new attempt needed — TD-01's Tier A Disposition already established this discovery process's structural limitation; it applies here without re-testing.
