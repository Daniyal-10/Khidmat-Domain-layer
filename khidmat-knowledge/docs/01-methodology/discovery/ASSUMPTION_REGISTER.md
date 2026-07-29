# Assumption Register

Per `../../98-archive/execution_cleanup/BUSINESS_DISCOVERY_BLUEPRINT.md` §6.2. Recorded whenever discovery cannot fully resolve a topic and a provisional assumption is needed to allow forward progress. Distinct from a Finding — an assumption is never the product of upgrading weak evidence; it is what stands in only where no adequate evidence exists (Blueprint §4.1).

---

## AR-001 — Individual operational-role vocabulary assumed provisionally valid pending Tier A

**Assumption:** The five operational roles named in `BUSINESS_ARCHITECTURE_BLUEPRINT.md` §4 (Registrant, Proxy, Field Verifier, Human Reviewer, Case Manager) are provisionally treated as plausible candidate business roles for BMP Chapter 1 drafting purposes, pending independent validation.
**Why necessary:** TD-01's Tier B/D collection (2026-07-24) found no external source — sector standard or academic literature — operating at this granularity; all retrieved sources describe organizational/coordination-level actors, not individual intake-conversation roles. Waiting indefinitely for Tier A would block Chapter 1 drafting entirely.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier A practitioner evidence either corroborating these five roles as accurately describing real intake/verification/case-management practice, or surfacing a different role decomposition.
**Status:** Open.

---

## AR-002 — General/cross-context Applicability Scope assumed adequate in the absence of a stated deployment geography

**Assumption:** TD-01 Findings BD-TD01-001, 002, 003, 005 are recorded with a general/cross-context Applicability Scope, on the assumption that this is an acceptable starting scope for BMP Chapter 1 drafting even though no source was checked against this project's actual initial deployment region.
**Why necessary:** No document reviewed anywhere in this project states an initial deployment geography, so no narrower scope could be tested against even if desired.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** The project stating a specific initial deployment context, after which every general-scope Finding above should be re-validated (or explicitly re-scoped) against it rather than assumed to transfer automatically.
**Status:** **CLOSED (2026-07-29, remediation B1).** The overturn condition has been met: `BUSINESS_MASTER_PLAN.md` §2 "Initial Applicability Context" (v1.3) now states the deployment geography, population, crisis profile, donor context, currencies, philanthropic framework and connectivity assumptions, sourced from client-supplied project material. Two dimensions — initial partner set and languages — remain explicitly unstated for lack of repository evidence and are recorded as open in that section rather than assumed.
**Residual obligation (not a new assumption).** Closing this entry makes the general-scope Findings of TD-01 through TD-06 *re-scopeable*; it does not re-scope them. Re-testing each Finding against the stated context is validation work gated on the ground truth channel (remediation B13). Until that occurs, those Findings retain their original general/cross-context scope tag, now by explicit record rather than by absence of any alternative.
**Applied beyond TD-01** — TD-02's Findings (BD-TD02-001 through 004) were covered by this same assumption and are covered by this same closure.

---

## AR-003 — Tension coverage is not an exhaustive pairwise check across every TD-01 actor category

**Assumption:** TD-02's four Findings are treated as the structurally significant tensions surfaced by this collection pass, not as proof that no other actor-pair tension exists among TD-01's named actor categories (e.g., Volunteer-vs-Case-Manager or Field-Verifier-vs-Human-Reviewer tensions were not specifically checked).
**Why necessary:** An exhaustive pairwise tension analysis across every TD-01 actor category was out of scope for a single collection pass, and manufacturing additional tensions merely to achieve pairwise coverage would violate Business Discovery Blueprint §4 Principle 6 (findings must be falsifiable) and Principle 7 (no finding authored for convenience).
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier A practitioner evidence, or a further Tier B/D pass, surfacing a materially different or additional structural tension among actor pairs not already covered.
**Status:** Open.

---

## AR-004 — Automation-vs-human-oversight tension provisionally accepted on Tier C strength alone

**Assumption:** The automation/human-oversight tension (`BUSINESS_ARCHITECTURE_BLUEPRINT.md` §3.3; `PROJECT_OVERVIEW.md` Ch4.2) is provisionally treated as a legitimate candidate tension for BMP Chapter 2, on the strength of two independent internal documents stating it, pending Tier B/D corroboration specifically from AI/automation-in-humanitarian-response literature, which was not searched in TD-02's collection pass.
**Why necessary:** TD-02's Tier B/D search targeted the four tensions with the clearest external literature; automation-vs-human-oversight is a distinct research question requiring its own targeted search, not a byproduct of the searches already run.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** A future, narrowly-scoped Tier B/D collection pass on AI/automation-in-humanitarian-response literature, either corroborating this as a recognized sector tension or reframing it as a Khidmat-specific design commitment without broader sector precedent (which would not make it false, only differently sourced).
**Status:** Open.

---

## AR-005 — Programme-cycle/case-cycle coupling mechanism unevidenced

**Assumption:** TD-03's finding that a programme-level (coordination/resourcing) lifecycle and a case-level (individual) lifecycle are structurally distinct (BD-TD03-001) is treated as real and business-relevant, but exactly how the two are coupled in practice (e.g., how resource-mobilization outcomes concretely constrain case-level Support Planning/Delivery) is assumed to exist without being evidenced in detail.
**Why necessary:** The Tier B sources reviewed established the two cycles as conceptually distinct but did not describe their coupling mechanism.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier B/D or Tier A evidence describing the actual coupling mechanism, or evidence the two cycles are more loosely coupled than assumed.
**Status:** Open.

---

## AR-006 — Placement of outcome/impact/learning within or outside the case lifecycle left undecided

**Assumption:** Whether outcome measurement, impact measurement, and organizational learning belong inside the same business-level case lifecycle Khidmat's own `BUSINESS_ARCHITECTURE_BLUEPRINT.md` §14 currently structures them as (BD-TD03-003), or as a related-but-separate business capability, is left genuinely open — not defaulted toward the existing internal structure.
**Why necessary:** Deciding this either way would exceed Business Discovery's mandate (naming business reality, not authoring a business decision); sector case-management standards reviewed end at closure, treating outcome/impact as a related-but-distinct discipline, which conflicts with how Khidmat's own artifact is currently structured — but this is a design choice for BMP Chapter 3 to make explicitly, not one this process can resolve.
**Owner: Stage 5 Domain Discovery
**What would overturn or resolve it:** Further Tier B/D evidence on M&E-integrated case-management models, or an explicit authorial decision once BMP Chapter 3 drafting begins.
**Status:** Open. **Substantially informed by TD-04** (BD-TD04-001, MEAL as a distinct sector-standard capability) — not resolved; the evidence now leans toward "separate capability," but the decision itself remains for a future BMP Chapter 3/4 author.

---

## AR-007 — MEAL, CFM, and Case Coordination treated as candidate capability-catalogue additions, without amending PROJECT_OVERVIEW.md

**Assumption:** Monitoring/Evaluation/Accountability/Learning (MEAL), Complaints & Feedback Mechanisms (CFM), and — more tentatively — Case Coordination/Orchestration are treated as strong candidate additions to a future BMP Chapter 4 capability catalogue, without this discovery process asserting that `PROJECT_OVERVIEW.md` Ch6.1's capability framing is incomplete as a governance matter.
**Why necessary:** `PROJECT_OVERVIEW.md` is explicitly a pre-formal, working document by its own stated terms ("before formal foundational documents are written"); amending or correcting it is outside Business Discovery's mandate. This assumption lets the gap be recorded as evidence for a future author without overstepping into governance.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** BMP Chapter 4 explicitly deciding whether and how to incorporate MEAL, CFM, and Case Coordination into the eventual capability catalogue.
**Status:** Open.

---

## AR-008 — Case Coordination/Orchestration rests on Tier C-only inference

**Assumption:** Case Coordination/Orchestration is treated as a plausible candidate distinct capability on the strength of an internal-document comparison alone (TD-04, §3), pending independent Tier B/D validation not yet performed.
**Why necessary:** TD-04's external collection targeted MEAL and CFM specifically (both confirmed); Case Coordination as its own named, sector-recognized capability distinct from case-management execution was not separately searched this session.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** A future, targeted Tier B/D search specifically on case coordination/orchestration as a named capability.
**Status:** Open.

---

## AR-009 — Specific operational value stream narratives deferred pending Tier A/programme input

**Assumption:** Due to the absence of Tier A practitioner evidence, specific end-to-end value stream narratives (e.g., the exact operational sequence for an Emergency Shelter Response versus a Sustainable Livelihood Pathway) are assumed to structurally follow the generic Beneficiary Lifecycle logic described in Tier C, but the concrete operational differences between them remain unevidenced.
**Why necessary:** Secondary literature (Tier D) provides the structural framework of Humanitarian Value Stream Mapping but does not provide the precise operational workflows used by specific Khidmat partner organizations, which requires practitioner input.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier A practitioner evidence detailing the actual operational workflows for specific value streams.
**Status:** Open.

---

## AR-010 — Standard intervention dimensions apply to Khidmat context

**Assumption:** Due to the absence of Tier A evidence, it is assumed that Khidmat partner organizations recognize and use the three standard dimensions of intervention categorization (Sector, Modality, Temporal Phase) in their own programmatic design, even if their internal terminology differs slightly.
**Why necessary:** Tier B and D evidence strongly supports these dimensions, but without Tier A, we assume they align with Khidmat's specific operational context.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier A practitioner evidence indicating that Khidmat partner organizations use a fundamentally different framework for categorizing their interventions.
**Status:** Open.

---

## AR-011 — Informal success criteria criteria remains unevidenced

**Assumption:** The specific, informal criteria the client and domain team currently use in practice to judge whether an intervention "worked" (prior to formal outcome indicators) is assumed to align broadly with the business-level Operational Objectives drafted in Chapter 7, but the exact informal criteria remain undocumented.
**Why necessary:** `PROJECT_OVERVIEW.md` provides broad indicators of human flourishing, but does not provide the concrete informal criteria currently used by the domain team in practice.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier A practitioner evidence detailing the actual informal success criteria used by the domain team.
**Status:** Open.

---

## AR-012 — Authority to override system recommendations unevidenced

**Assumption:** Who, in actual humanitarian practice, possesses the specific operational authority to override a system-generated recommendation (and under what exact circumstances) remains an open discovery topic. The overarching boundary that high-consequence decisions require human review is established, but the specific authority boundaries are not.
**Why necessary:** While `PROJECT_OVERVIEW.md` establishes the principle of meaningful human review, it does not specify which operational roles hold this override authority in practice.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier A practitioner evidence detailing the specific operational roles and circumstances for overriding system recommendations.
**Status:** Open.

---

## AR-013 — Additional regional/cultural frameworks unevidenced

**Assumption:** Beyond the Islamic giving model (Zakat/Sadaqah), what other specific regional or cultural frameworks the project intends to support—and whether they represent surface-level labeling aliases or substantively distinct business practices—remains an open assumption.
**Why necessary:** Existing artifacts reference the Islamic giving model as a primary example, but do not provide an exhaustive list of other intended regional/cultural frameworks.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Formal documentation from the Human Owner or client specifying additional regional/cultural frameworks in scope for the project.
**Status:** Open.

---

## AR-014 — Private Sector and Market Actors unevidenced as formal category

**Assumption:** While `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Chapter 5 describes a "Material and Resource Flow" (logistics, procurement) and Chapter 6 describes "Cash and Voucher Assistance," the specific role of "Private Sector and Market Actors" (e.g., local merchants, financial service providers, logistics vendors) is assumed to exist as a distinct, missing actor category in Chapter 1.
**Why necessary:** These actors execute the physical delivery and financial transaction components of assistance, but TD-01 did not explicitly capture them alongside NGOs, Governments, and Communities.
**Owner: Stage 5 Domain Discovery
**What would overturn it:** Tier A practitioner evidence indicating how market actors are classified in the Khidmat ecosystem.
**Status:** Open.

---

## AR-015 — Human-reality decompositions carried on a single archived internal source

**Assumption:** The decompositions promoted into `docs/02-discovery/human-reality/HUMAN_REALITY_DISCOVERY.md` from `98-archive/execution_cleanup/BUSINESS_ARCHITECTURE_BLUEPRINT.md` — the nine lifecycle stages (§5.2), the five capability classes (§5.3), and the five health-condition kinds (§5.4) — are treated as a plausible starting decomposition of a person's situation.
**Why necessary:** Remediation B2 required the human-reality content dropped by the skipped Stage 4 reconciliation to re-enter the canonical chain. Promoting it with its weakness recorded is preferable to either leaving the Facets layer with no substrate at all, or inventing a replacement decomposition with no source.
**Owner:** Human Reality domain (Stage 5).
**What would overturn it:** Tier A practitioner evidence, or Tier B sector-standard evidence, either corroborating these decompositions or surfacing a materially different cut of a person's situation.
**Status:** Open. These are **not** Findings and must not be read as such.

---

## AR-016 — Risk assembly and protective-factor model carried on `GLOSSARY.md` alone

**Assumption:** Fourteen of the twenty-nine concepts in `docs/02-discovery/vulnerability-risk-protection/` — principally the Risk Composition → Risk Characterization → Risk Profile assembly structure, Hazard Category, Exposure, Protective Factor and its four named instances — are retained as coherent and load-bearing despite being present in `GLOSSARY.md` and nowhere else.
**Why necessary:** Remediation B3 directed that the glossary risk terms be re-validated *or retired*. Fifteen validated against a second internal source; these fourteen did not. Retiring them would discard the only account the project has of how risk is assembled and of what protects a person, leaving the domain purely deficit-oriented in violation of Pillar P5.
**Owner:** Vulnerability, Risk and Protection domain (Stage 5).
**What would overturn it:** Tier A or Tier B evidence either corroborating the assembly model or showing that practitioners assemble risk differently.
**Status:** Open. Each affected concept is individually marked *Carried unvalidated* in the domain document.

---

## AR-017 — Islamic giving forms assumed distinct; their substance not asserted

**Assumption:** `GLOSSARY.md`'s claim that seven canonically distinct Islamic giving forms exist (Zakat, Sadaqah, Sadaqah Jariyah, Waqf, Fidya, Kaffarah, Qurbani), each with its own obligation basis and restriction shape and none a synonym or alias for another, and that eight Zakat-eligible recipient categories exist, is assumed valid as to *distinctness*.
**Why necessary:** Remediation B4 required the ratified concept Donor (CL-002) to acquire discovery. The distinctness claim is load-bearing for modelling — a foundation that treats the seven as aliases cannot honour their differing restrictions — while the substance of each form is genuinely undiscovered.
**Scope limit, stated explicitly:** the **substance** of each form's obligation basis and restriction shape, and the content of the eight asnaf categories, is **not** assumed and **not** asserted anywhere. Within the applicability context stated in `BUSINESS_MASTER_PLAN.md` §2 this substance determines who may lawfully receive assistance; inventing it would risk religious and legal harm.
**Owner:** Giving and Resource-Origin domain (Stage 5).
**What would overturn it:** Evidence that any two forms are in fact aliases, or authoritative sourcing of the obligation bases and recipient categories.
**Status:** Open. Related to, and does not supersede, AR-013.

---

## AR-018 — Need, intervention-fit and outcome decompositions carried on single sources

**Assumption:** The seven need categories and four outcome categories (from `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §§9, 13), the three need-relationship qualifiers, the four intervention-relationship types, Intervention Readiness, Intervention Objective Category, and the six-stage Human Development trajectory (all from `GLOSSARY.md`) are treated as plausible starting decompositions.
**Why necessary:** Remediation B5 required case-altitude content for Need, Intervention Fit and Outcome, which TD-06 had covered only at programme altitude. These are the only accounts the repository holds.
**Owner:** Case Management and Accountability & Evaluation domains (Stage 5).
**What would overturn it:** Tier A or Tier B evidence corroborating or replacing any decomposition.
**Status:** Open.

---

## Note on AR-011 (informal success criteria)

AR-011 was examined during remediation B5 and **remains Open**. Four independent repository sources (`HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch7; this register's AR-011; `case-management/10-open-questions.md`; `98-archive/.../BUSINESS_ARCHITECTURE_BLUEPRINT.md` §13) agree that the criteria by which practitioners judge an intervention to have worked are unknown. No repository evidence exists from which to close it, and supplying an answer would constitute inventing business knowledge. Its overturn condition — Tier A practitioner evidence — is gated on remediation B13.
