# Contradiction Log

Per `BUSINESS_DISCOVERY_BLUEPRINT.md` §6.3. Every entry here is routed to the Human Owner for resolution — this discovery process does not resolve contradictions unilaterally.

---

## CL-001 — Programme / Organisation: conflated or distinct concepts?

**Raised during:** TD-01, Tier C collection.
**Conflict:** `docs/02-architecture/KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 lists "Programme / Organisation" as a single combined actor-table row. `docs/90-reports/Khidmat_Knowledge_Layer_Status_Report.html` (a report describing a prior/archived ontology state) treats `organisation` and `program` as two distinct canonical entities with their own funds/implements relationship.
**External evidence bearing on this (TD-01, Tier B, 2026-07-24):** Findings BD-TD01-002 and BD-TD01-003 — every sector coordination source retrieved (OCHA, UNHCR/IASC) consistently names implementing organizations separately from the programmes/clusters they lead. This leans toward "distinct," but is evidence to weigh, not a resolution — an internal V1-scoping decision is not automatically wrong merely because general sector practice draws the distinction differently.
**Status:** Open. Awaiting Human Owner decision.

---

## CL-002 — Is Donor an actor?

**Raised during:** TD-01, Tier C collection.
**Conflict:** `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4/§17 explicitly states "Donors and the resource-supply side are intentionally not V1 actors." `docs/00-governance/GLOSSARY.md`'s Donor Profile entry, and the archived Status Report's `person_roles` controlled vocabulary, both include `donor`.
**External evidence bearing on this (TD-01, Tier B, 2026-07-24):** Finding BD-TD01-004 — the Core Humanitarian Standard's own definition of "humanitarian actor" explicitly includes organizations that fund without directly delivering assistance. This suggests the internal disagreement may be a *delivery-scope* question (what V1 builds first) rather than a genuine disagreement about whether donors are actors in humanitarian reality — but this reframing does not itself close the contradiction; the two internal documents still disagree in their current wording.
**Status:** Open. Awaiting Human Owner decision on how to reconcile the two documents' wording.
