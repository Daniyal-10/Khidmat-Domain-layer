---
id: DECISION-BRIEF-01
title: Human Owner Decision Brief — CL-001 and CL-002
status: Decision support only — no recommendation made, no decision recorded
covers: [CL-001, CL-002]
source_dossiers: [TD-01]
created: 2026-07-24
governed_by: ../BUSINESS_DISCOVERY_BLUEPRINT.md
---

# Human Owner Decision Brief 01

**Purpose:** prepare the Human Owner to resolve `CONTRADICTION_LOG.md` entries CL-001 and CL-002. This brief restates each contradiction, the evidence gathered, and the implications of each possible path — it does not recommend one, does not decide, and does not modify the Contradiction Log or any repository document. Per the checkpoint review, further web research cannot resolve either item, because both concern reconciling Khidmat's own prior internal artifacts against each other, not an open question about humanitarian reality.

**Once a decision is made:** recording it is a governance action outside this brief's scope. `docs/80-decisions/README.md` scopes that directory to exactly this kind of chronological decision record (ADR/RFC/KDR) — the natural next step, not performed here.

---

## CL-001 — Programme / Organisation: conflated or distinct concepts?

### 1. Neutral restatement

Should "Programme" and "Organisation" be treated as one combined business concept, or as two distinct concepts with their own relationship to each other?

### 2. Which internal documents disagree, and how

- **`docs/02-architecture/KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4** (the "Actors and Operational Roles" table) lists a single combined row: *"Programme / Organisation — Defines the assistance actually available, the eligibility criteria, and the accountability structure the case operates within."* One row, one description, no distinction drawn between the implementing body and the initiative it runs.
- **`docs/90-reports/Khidmat_Knowledge_Layer_Status_Report.html`** (a report describing a prior, now-archived ontology-drafting effort) lists `organisation` and `program` as two of eight separate canonical entities, with a stated relationship between them ("Programme funded/implemented by an Organisation").

Both documents are internal and pre-date this Business Discovery phase; neither was authored with the other in view at the time of writing (confirmed during TD-01's Tier C pass — this is a reconciliation gap, not a newly introduced conflict).

### 3. External evidence collected during discovery

From TD-01, Tier B (sector coordination-architecture sources):

- **BD-TD01-002** (High confidence, corroborated across OCHA and UNHCR sources): the IASC cluster coordination system consistently names lead/co-lead *organizations* (e.g., UNHCR for Protection; IFRC/IOM for Shelter, Land, and Site Coordination) separately from the coordination structure (*cluster*) they lead.
- **BD-TD01-003** (Medium-High confidence, consistent across all Tier B sources retrieved, though no single source states it as an explicit definitional rule): every source retrieved treats an implementing/coordinating body as distinct from the funded initiative or structure it participates in.

Both Findings lean toward "distinct," but neither is a primary source stating "Organisation and Programme are formally different concepts" as an explicit rule — the evidence is consistent, structural inference from how sources name things, not a quoted definition.

### 4. What each possible decision would imply

- **Treat them as one combined concept** (ratify `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4's framing; the archived Status Report's split entities are superseded): keeps V1's actor model simple — one row, one concept — and requires no edit to the currently-referenced business logic document.
- **Treat them as two distinct concepts** (ratify the archived report's structure, aligned with external evidence): requires revising `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4's table row into two entries with a stated relationship between them, and requires that relationship (e.g., "funds," "implements") to itself be named.
- **Defer:** leave both documents standing as-is, and let whichever BMP chapter first needs this distinction (Chapter 1's Ecosystem narrative, or later Chapter 4's Business Capabilities, which BLB §16 already names "Programs (eligibility, cycles, enrollment, budget, reporting)" as a planned-but-undelivered domain) resolve it at that point.

### 5. Risks of each option

- **Combined-concept option:** diverges from every external source examined without a documented reason; carries a rework risk if the planned Programs domain (BLB §16) later needs the split anyway, since eligibility/cycles/enrollment/budget more naturally attach to a Programme than to an Organisation as a whole.
- **Distinct-concepts option:** requires editing `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`, a document already flagged in its own header as "not yet synchronized" against the Overview/Constitution — this would be an additional, separate edit to an already-open item, not a clean one-line fix. Also carries a scope risk worth naming: defining the Organisation–Programme relationship precisely edges toward an ontology-shaped decision (a relationship between two concepts), which is a decision this project's own methodology reserves for Ontology Design, not for a Business Discovery contradiction resolution — the Human Owner may want to resolve only the naming/conflation question here and explicitly leave relationship mechanics for later.
- **Defer option:** does not remove the cost, only postpones it — and the Phase Review checkpoint already flagged Chapter 4 (Capabilities) and Chapter 8 (Governance & Authority Boundaries) as the chapters most likely to need this distinction, so deferral risks the same question resurfacing, unresolved, at a point where more work already depends on an answer.

### 6. Downstream artifacts affected

BMP Chapter 1 (Ecosystem) directly; transitively Chapter 4 (Business Capabilities) and Chapter 8 (Governance & Authority Boundaries), per the Phase Review's own flagged watch-item; the eventual Humanitarian Business Reference Model's Organisation and/or Programme entries; `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 (if the distinct-concepts option is chosen); the archived Status Report's standing (if the combined-concept option is chosen, its split-entity structure would need to be explicitly marked superseded rather than left ambiguous).

### 7. Evidence sufficiency

**Sufficient to inform the decision; not sufficient, and not improvable by further research, on the reconciliation question itself.** The evidence gathered establishes the *general sector pattern* (organizations and the programmes they run are usually treated as distinct) at Medium-High to High confidence — reasonably solid, though resting on two source families rather than three or more. It does not and cannot establish which choice best fits Khidmat's own product and V1-scoping intent — that is inherently a judgment about this project's own priorities, which is exactly why this is a Human Owner decision rather than a discovery question. One narrow, optional way discovery could still add marginal value: a third independent Tier B source corroborating the organisation/programme distinction would move BD-TD01-003 from Medium-High to High confidence — not necessary for a decision, but available if the Human Owner wants a slightly stronger evidentiary base before ratifying "distinct."

---

## CL-002 — Is Donor an actor?

### 1. Neutral restatement

Should "Donor" be modeled as an actor at all — and if so, is its current absence from Khidmat's V1 actor set a statement about humanitarian reality (donors aren't really actors) or a statement about delivery scope (Khidmat V1 doesn't build donor-facing features yet, even though donors are actors)?

### 2. Which internal documents disagree, and how

- **`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 and §17** state plainly: *"Donors and the resource-supply side are intentionally not V1 actors"* and list *"The donor / resource-supply side and donor–need matching"* under "Explicitly Out of Scope for V1."
- **`docs/00-governance/GLOSSARY.md`** defines a detailed **Donor Profile** entry: *"The record of a person's or organisation's giving relationship with Khidmat... Attaches behind an existing Person or Organisation record, mirroring how Volunteer Profile attaches behind the shared Actor."* This entry treats Donor as attaching to the same shared Actor concept Volunteer does.
- **`docs/90-reports/Khidmat_Knowledge_Layer_Status_Report.html`** lists `donor` inside its `person_roles` controlled vocabulary, alongside `beneficiary`, `registrant`, and `proxy`.

The Business Logic Blueprint excludes Donor from the actor set; the Glossary and the archived Status Report both already treat Donor as an actor-adjacent or actor-classified concept.

### 3. External evidence collected during discovery

From TD-01, Tier B:

- **BD-TD01-004** (High confidence by source-tier ceiling, but flagged with a Discovery Limitation for resting on a single retrieved document): the Core Humanitarian Standard's own definition of "humanitarian actors" explicitly includes organizations that provide financial, material, or technical support to other organizations without directly delivering assistance themselves. This is the standard-setting body's own primary definitional statement, directly on-point.

### 4. What each possible decision would imply

- **Exclude Donor from the actor model entirely** (for both V1 delivery and the full conceptual model): treats GLOSSARY's Donor Profile entry and the archived Status Report's `person_roles` vocabulary as premature and requiring removal or deferral until a Donor & Resource domain is actually built.
- **Include Donor as a conceptual actor, with V1 delivery explicitly scoped to exclude donor-facing features**: ratifies `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`'s exclusion as a statement about what V1 *builds*, not about what donors *are* — requires a small wording clarification in §4/§17 to remove the current ambiguity between the two readings, but preserves the definitional work already done in GLOSSARY.
- **Defer:** leave both documents as currently worded, and treat the distinction as immaterial until the Donor & Resource domain (already named as planned in `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §16) is actually scheduled for work.

### 5. Risks of each option

- **Exclude entirely:** diverges from CHS's own definition without a documented reason; risks needing to reverse this decision once the already-planned Donor & Resource domain (BLB §16) is eventually built, since that domain's own existence presumes Donor is a real, modelable actor.
- **Include conceptually, exclude from V1 delivery:** the risk here is mainly editorial — a small, low-cost edit to a document already flagged as unsynchronized. One second-order risk worth the Human Owner's attention: if this "delivery-scope vs. actor-taxonomy" framing is adopted for Donor, the same question plausibly applies to other actors named in §4 that may not be fully delivered in V1 either (e.g., Field Verifier, Human Reviewer) — this decision could set a precedent the Human Owner may want to apply consistently rather than case-by-case.
- **Defer:** the ambiguity is not a remote, future concern — TD-02 (Chapter 2, Stakeholder Interests and Tensions) already found the donor-vs-beneficiary accountability tension to be its single most strongly-evidenced finding, which presumes Donor is a real actor category worth naming a tension about. Deferral leaves this presumption unexamined in a document (TD-02) that has already been handed off.

### 6. Downstream artifacts affected

BMP Chapter 1 (Ecosystem) and Chapter 2 (Stakeholder Interests and Tensions — TD-02's donor-accountability tension is a direct downstream consumer of however this is resolved); `GLOSSARY.md`'s Donor Profile entry; `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4/§17 wording; the eventual Donor & Resource domain and any future HBRM entry for Donor.

### 7. Evidence sufficiency

**Sufficient to inform the external-reality question; not sufficient, nor improvable by further research, on the internal delivery-scope question.** CHS's definition is authoritative and directly on-point — a primary, standard-setting source, not a secondary description — so the claim "donors are generally recognized as actors in humanitarian practice" is well-grounded even though it currently rests on one retrieved document (TD-01 flagged this single-sourcing explicitly with a Discovery Limitation, despite the source's own high authority). Whether Khidmat's V1 should build donor-facing capability, or should describe Donor as a full conceptual actor regardless of what V1 delivers, is a product-scoping and resourcing decision — not something additional literature search can settle. One optional way discovery could still add marginal value: retrieving a second independent Tier B source (e.g., OCHA or Sphere material specifically addressing donor status, rather than CHS alone) would remove the single-sourcing flag and raise this Finding's corroboration from one source to two — a modest strengthening, not a precondition for deciding.
