# Business Master Plan — Governance Resolution

**Type:** Governance decision record
**Resolves:** The two outstanding Open Questions from `BUSINESS_MASTER_PLAN_BLUEPRINT.md` §8, identified as unresolved by `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md` §4.1
**Scope of action:** Governance decisions only. No Business Master Plan chapter is modified, expanded, or reopened by this document.
**Date:** 2026-07-22

---

## Why This Document Exists

The architecture review found that two of the blueprint's four Open Questions were never actually answered before Chapters 1–9 were authored — not because the questions were unimportant, but because authoring proceeded chapter by chapter under direct instruction, and no checkpoint existed at which the Human Owner (per `AI_WORKFLOW.md`) was asked to close them out. Leaving them open any longer would mean the Business Master Plan (BMP) gets frozen — per the separate `BUSINESS_MASTER_PLAN_FREEZE_CERTIFICATION.md` — while two of its own governing questions remain silently unanswered. This document closes both, explicitly, before that freeze occurs.

Resolving a governance question is not the same action as authoring business content. Nothing below adds, removes, or alters any statement in `BUSINESS_MASTER_PLAN.md`.

---

## Resolution 1 — Sequencing Relative to PHILOSOPHY.md / PRINCIPLES.md

**The question (blueprint §8, Open Question 1):** Should the BMP have waited for `docs/00-governance/PHILOSOPHY.md` and `PRINCIPLES.md` to be written first, per the blueprint's own dependency chain (§4), or does the project accept authoring them concurrently, at the risk of rework if a later-written principle contradicts an already-written BMP chapter?

**Finding that changes the terms of this decision:** In the course of resolving this question, `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` (root) was reviewed directly. Its §3, "Foundational Principles," already states five operative principles — epistemic humility (claims vs. facts), consent/dignity/do-no-harm, human oversight and governance, bidirectional accountability and beneficiary voice, and fairness/integrity — that predate the BMP and have been functioning, in practice, as the project's de facto philosophy statement. `docs/00-governance/PHILOSOPHY.md` and `PRINCIPLES.md` are not the *only* place this content already exists; a working substitute has existed since before BMP authoring began.

**Consistency check performed:** Each of the BMP's chapters was checked against V1 Blueprint §3 for direct contradiction. None was found:

| V1 Blueprint §3 principle | Corresponding BMP content | Consistent? |
|---|---|---|
| 3.1 Epistemic humility (claims, not facts) | Ch4 §4.4 Verification, Ch3 §3.4 | Yes — no claim is treated as fact without verification in either document |
| 3.2 Consent, dignity, do-no-harm | Ch1 §1.1, Ch2 §2.1, Ch7 §7.2 | Yes, though the BMP does not name "consent" as its own concept (see Backlog item RB-10) |
| 3.3 Human oversight and governance | Ch8 (all) | Yes — Ch8's entire premise (distributed, non-automated authority) is a direct elaboration of this principle |
| 3.4 Accountability and beneficiary voice | Ch2 §2.8, Ch3 §3.9 (reassessment) | Largely consistent; V1's explicit "grievance reopens the journey" mechanic is narrower than anything the BMP names (see Backlog item RB-11) |
| 3.5 Fairness and integrity | Ch7 §7.4 | Yes, direct correspondence |

**Decision:** Concurrent authoring is ratified retroactively. The BMP is not required to wait for the formal authoring of `PHILOSOPHY.md`/`PRINCIPLES.md`, on two grounds: (a) reopening the BMP to wait is foreclosed by this resolution's own scope, and (b) a functioning, consistent equivalent already existed in `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3 throughout authoring, and no contradiction with it was found.

**Binding condition attached to this decision:** When `docs/00-governance/PHILOSOPHY.md` and `PRINCIPLES.md` are eventually formally authored, their authors must check the resulting text against **both** the BMP's implicit commitments (as catalogued in the table above) **and** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §3 — not treat the formal governance documents as a blank slate. If either check reveals a genuine contradiction (not found by this review, but not exhaustively ruled out either), that contradiction must be resolved by amending the governance document, not by reopening the BMP.

---

## Resolution 2 — Relationship to KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md

**The question (blueprint §8, Open Question 4):** Is `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` superseded by the new BMP, a separate complementary document, or a direct input to it?

**Finding from direct review of that document:** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` is explicitly versioned ("V1"), explicitly scoped against delivery status (§16: "Delivered today" vs. "Planned"), explicitly declares items out of scope for this version with a named V2 horizon (§17), and continuously references actual repository structures by name (`shared/`, `registration/`, `verification-operations/`, `knowledge_layer_roadmap.md`). It states plainly: *"Where it names a concept, the authoritative definition lives in the repository... This document describes the target business architecture."* This is structurally a different kind of document from the BMP, which is deliberately timeless and would remain true in a world where Khidmat AI never existed.

**Decision:** The two documents are **separate and complementary, neither superseding the other**, because they answer different questions at different altitudes:

- `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` answers: *what does Khidmat AI, specifically, understand and deliver right now, in this version, against the humanitarian business reality it operates in* — an implementation-anchored, versioned business specification, tied to the actual repository and roadmap.
- `BUSINESS_MASTER_PLAN.md` answers: *how does humanitarian assistance work as a business domain, independent of any system* — a timeless business-reality description that exists whether or not Khidmat AI is ever built.

Neither document should be edited to resemble the other. The V1 Blueprint's versioned scope statements (§16–§17) remain the authoritative record of what Khidmat AI's *current version* commits to; the BMP remains the authoritative record of the *business domain* that all versions, current and future, exist to serve.

**Reconciliation finding worth registering, not resolving here:** The V1 Blueprint's own scope statements independently corroborate two items this review's architecture review separately flagged as BMP gaps:

- V1 Blueprint §1 and §17 explicitly name anticipatory/predictive need detection as the project's stated long-term vision *and* explicitly declare it out of scope for V1 ("a predictive/preventive engine... V2 horizon"). The BMP's silence on anticipatory need detection is therefore not an unnoticed oversight at the project level — it is consistent with an already-made scope decision — but the BMP itself still does not name the concept anywhere, which is a real gap in the *timeless* business description regardless of what any specific version delivers. Registered as Backlog item RB-01 with this context attached.
- V1 Blueprint §17 explicitly excludes "fraud/anomaly engines" as V1 operational tooling while noting "light integrity such as duplicate suspicion is already handled." The BMP's silence on inaccurate or fraudulent claims (architecture review §5, item 4) is similarly consistent with, not contradictory to, existing project scoping. Registered as Backlog item RB-04 with this context attached.

**Downstream instruction attached to this decision:** Authors of the Humanitarian Business Reference Model, Business Architecture, and Domain Discovery must treat `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §16–§17 as the authoritative statement of *current delivery scope*, and the BMP as the authoritative statement of *business-domain completeness*. Where the two differ — as with anticipatory need detection — that difference is the correct and expected shape of a versioned system maturing against a timeless domain description, not an error to be silently resolved in either document.

---

## Disposition Summary

| Open Question | Resolution | Action required on BMP content |
|---|---|---|
| 1 — Sequencing vs. PHILOSOPHY/PRINCIPLES | Concurrent authoring ratified retroactively; consistency check performed and passed; binding condition attached for future PHILOSOPHY/PRINCIPLES authoring | None |
| 4 — Relationship to V1 Blueprint | Separate, complementary documents at different altitudes; neither supersedes the other | None |

Both resolutions are now recorded explicitly, closing the governance gap identified in `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md` §4.1. Neither resolution required, or resulted in, any change to `BUSINESS_MASTER_PLAN.md`.
