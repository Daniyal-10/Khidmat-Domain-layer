# Business Discovery — Working Directory

**Status:** Provisional location. `BUSINESS_DISCOVERY_BLUEPRINT.md` §10, Open Question 2 has not yet been answered by the Human Owner — it is undecided whether Topic Dossiers, the Assumption Register, and the Contradiction Log belong in the versioned repository at all, and if so, where. This directory is used in the meantime so discovery work has a consistent home; nothing here should be treated as certified or final, and its location may move once Open Question 2 is resolved.

## Contents

- `TD-01-humanitarian-ecosystem-actors.md` — Topic Dossier for BMP Chapter 1 (The Humanitarian Ecosystem). **Handed off** (see its own Discovery Review / Handoff Record), carrying a Discovery Limitation (Tier A structurally infeasible in this execution environment — see its Tier A Disposition) and two open Contradiction Log entries still pending Human Owner sign-off before Chapter 1 may be authored.
- `TD-02-stakeholder-interests-and-tensions.md` — Topic Dossier for BMP Chapter 2 (Stakeholder Interests and Tensions). **Handed off**, with a lighter Discovery Limitation than TD-01 (non-exhaustive actor-pair coverage; automation/human-oversight tension Tier-C-only). Chapter 2 authoring remains blocked transitively through TD-01's still-open Contradiction Log entries.
- `TD-03-humanitarian-lifecycle-business-view.md` — Topic Dossier for BMP Chapter 3 (The Humanitarian Lifecycle, Business View). **Handed off**, with a Discovery Limitation: two Findings strongly corroborate existing internal concepts (case-lifecycle non-linearity; Engagement-Stage/Human-Development-Stage split), two Findings surface open design questions for the future BMP Chapter 3 author rather than settled facts (programme-cycle/case-cycle scope boundary; whether outcome/impact/learning belong inside the case lifecycle). Chapter 3 authoring remains blocked transitively through Chapters 1–2's unresolved gates, plus its own open question (AR-006).
- `ASSUMPTION_REGISTER.md` — running log per Blueprint §6.2. 6 entries as of Checkpoint 1 (AR-001–AR-006).
- `CONTRADICTION_LOG.md` — running log per Blueprint §6.3. 2 entries as of Checkpoint 1 (CL-001, CL-002), both still open, both pending Human Owner decision.
- `DISCOVERY_PHASE_REVIEW_01.md` — retrospective quality checkpoint across TD-01–TD-03, performed before opening TD-04. Reviews process health, recurring concepts/patterns, and the two registers above; does not modify the Blueprint, resolve any open item, or authorize BMP authoring.
- `HUMAN_OWNER_DECISION_BRIEF_01.md` — decision-support brief for `CONTRADICTION_LOG.md` entries CL-001 and CL-002, prepared because the Phase Review flagged a growing gap between discovery output and governance throughput. Restates each contradiction, the evidence gathered, and the implications of each possible path — makes no recommendation and does not modify the Contradiction Log. Resolution remains a Human Owner action, to be recorded in `docs/80-decisions/` once made.

## Note on "certification"

Discovery dossiers in this directory do not go through the Blueprint/Final-Methodology Review→Resolution→Certification cycle defined in `01-methodology/README.md`. Business Discovery Blueprint §8 deliberately reserves that heavier cycle for methodology documents and applies a lighter **Discovery Review / Handoff** checkpoint to dossiers instead — see TD-01's own "Discovery Review" section for the reasoning. Do not describe a dossier in this directory as "certified."

## Governing document

All structure, fields, and process in this directory follow `../BUSINESS_DISCOVERY_BLUEPRINT.md` exactly. Do not modify dossier structure here without first amending the Blueprint — this directory contains discovery *output*, not methodology.
