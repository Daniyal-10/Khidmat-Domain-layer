---
id: DOC-DISC-GIVING_RESOURCE_ORIGIN
title: GIVING & RESOURCE-ORIGIN DOMAIN DISCOVERY
version: 1.0
status: Draft
owner: Discovery
created: 2026-07-29
remediation: B4 (closes Foundation Gap FG-4)
governed_by: docs/00-governance/STAGE_5_DISCOVERY_STANDARD.md
---

# Giving and Resource-Origin Domain Discovery Report

> **Provenance statement — read first.**
> Authored under remediation B4 of the accepted Foundation Readiness Assessment. FG-4 recorded that Human Owner decision **CL-002 ratified Donor as a valid humanitarian business concept** on 2026-07-27 — *"The exclusion of donor-facing functionality from Khidmat V1 is strictly an implementation-scope decision and not a statement about humanitarian reality"* — and that no discovery domain was ever opened for it. A repository search of `02-discovery/` returns zero occurrences of Zakat, Sadaqah or Islamic giving, and Donor appears only as an external constraint-setter in programme and logistics rules.
>
> This document promotes existing repository knowledge into a canonical domain. Its sources are `GLOSSARY.md` (Donor & Resource Terms), `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch1 and Ch9, `BUSINESS_MASTER_PLAN.md` §3 and §9, `CONTRADICTION_LOG.md` CL-002, and TD-01 Finding BD-TD01-006 — **the only externally corroborated statement in this domain**.
>
> **Scope discipline.** `BUSINESS_MASTER_PLAN.md` §2 places donor-facing functionality outside Khidmat's delivery scope. That remains true and is not altered here. This domain models giving as **humanitarian reality**, exactly as CL-002 directs, not as a Khidmat capability. The distinction is settled in ADR-001 (`DECISION_LEDGER.md`) under remediation B9.

---

## 1. Purpose

The Giving and Resource-Origin Domain exists to hold the **reality of where humanitarian resources come from, on what terms, and under what obligations** — as knowledge distinct from how those resources are subsequently budgeted (Programme Management) or physically moved (Resource & Logistics).

It solves the problem recorded in FG-4. Restricted funding is not a financial technicality; it is a **constraint on who may receive what**. `programme-management/12-domain-invariants.md` states it as an invariant: *"Restricted donor funding cannot be fungibly shifted without formal reallocation decisions, regardless of urgent ground need."* `KNOWLEDGE_TRANSFORMATION_PATTERNS.md` §4.5 traces the full chain — Donor Mandate → Programme Allocation → Intervention Catalogue → Eligibility Rule → Support Plan Approval — and observes that it creates "intense ethical friction" when a case worker finds a starving child under education-only funding. The origin of that constraint chain was never discovered.

Within the applicability context now stated in `BUSINESS_MASTER_PLAN.md` §2, Islamic charitable giving is the governing philanthropic framework, and Zakat carries recipient-category restrictions that are eligibility-determining. Under Constitution Article IV, a rule determining who may lawfully receive assistance is unambiguously Reality Knowledge.

No other domain can own this. Programme Management consumes funding as a constraint and explicitly classifies Grant and Budget as knowledge it holds operationally; its boundaries exclude fundraising. Resource & Logistics owns procurement and disbursement — the movement of resources, not their origin or the obligations attached. Organisation & Partner Management owns the institutional relationship with a donor, not the giving itself.

## 2. Business Outcomes

- An account of who provides humanitarian resources and on what terms.
- An account of the obligations and restrictions that travel with a resource from its origin to its recipient.
- A representation of religiously-grounded giving forms sufficient for their restrictions to be honoured rather than flattened.
- Visibility of the formal/informal split in giving, so that community-based giving is treated as legitimate rather than invisible.

## 3. Stakeholders

### Actors (Enduring Participants)
- **Donor / Funder:** an actor providing financial, material or technical support to implementing Organisations, enabling humanitarian work without necessarily delivering assistance directly. *(Source: `GLOSSARY.md`; `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch1; ratified by CL-002.)* Includes institutional funders, philanthropic foundations and private individuals *(HBRM Ch1)*.
- **Institutional Donor:** a formal funding body imposing compliance, reporting and earmarking requirements. *(Source: `programme-management/05-business-rules.md`, Donor Policies; `resource-logistics/05-business-rules.md`, Donor Rules.)*
- **Individual Giver:** a private person giving directly or through community networks. *(Source: HBRM Ch1's "horizontal" philanthropy; TD-01 BD-TD01-006.)*
- **Formal Giving Institution:** an institutionalised Zakat organisation or equivalent — HBRM Ch1's "vertical" philanthropy. *(Source: HBRM Ch1, Ch9; TD-01 BD-TD01-006.)*
- **Community Giving Network:** mosque committees, local self-help groups and mutual-aid structures through which informal giving flows — HBRM Ch1's "horizontal" philanthropy. *(Source: HBRM Ch1; TD-01 BD-TD01-005 and BD-TD01-006; `GLOSSARY.md` Local Organisation.)*

### Roles (Transient Responsibilities)
- **Grant Holder / Prime Recipient:** the Organisation legally accountable for a grant. *(Source: `organisation-partner-management/12-domain-invariants.md`, "The Liability Anchor: legal and financial liability always flows upward to the primary grant holder.")*
- **Budget Holder:** the role with financial authority to approve reallocations. *(Already named in `programme-management/01b-stakeholders.md`; referenced, not duplicated.)*

## 4. Business Capabilities

- Resource origin and obligation recording.
- Giving-form classification (recording which canonical giving form a contribution constitutes, and therefore which restrictions apply).
- Restriction and earmark representation.
- Formal/informal giving-channel distinction.

## 5. Core Business Activities

- Recording that a funding commitment has been made, by whom, on what terms.
- Recording a discrete act of giving against that commitment.
- Recording the restrictions attached — sector, geography, target population, recipient category, or giving-form obligation.
- Recording whether giving flowed through a formal institution or a community channel.

## 6. Business Decisions

### 6.1 Resource Reallocation Decision
*Already discovered and owned in `programme-management/08-decision-points.md` §4. Referenced, not duplicated, per Rule AR-3.* It is the point at which a donor restriction meets an urgent field need — decided by the Budget Owner / Programme Manager, governed by donor flexibility policies, constrained by strict earmarking, with outcomes of internal reallocation, formal donor amendment, or denial, and with Crisis Modifier clauses as the human override.

### 6.2 Giving-Form Restriction Application Decision
- *Purpose:* Determining which restrictions apply to a given resource, and therefore which recipients and which uses are permissible.
- *Decision Maker:* **Insufficient repository evidence.** No repository source states who determines the giving form of a contribution or adjudicates its restrictions.
- *Supporting Evidence:* The stated giving form; the donor's stated intent; the recipient's circumstances against the applicable recipient categories.
- *Governing Policies:* `GLOSSARY.md` establishes that each of the seven giving forms has "its own obligation basis and restriction shape," and that Zakat-Eligible Category is "a classification a Programme's Eligibility Rule may reference when a Programme is zakat-restricted — not a second eligibility engine."
- *Constraints:* The restriction is not discretionary; it is an obligation carried by the resource itself.
- *Alternative Outcomes / Escalation / Appeal / Override:* **Insufficient repository evidence.**
- *Uncertainty:* The repository does not record how a case is handled where a person is in evident need but falls outside every applicable recipient category.

**Recorded gap.** Decision content here is materially thinner than in the seven original domains. That is a truthful reflection of available evidence.

## 7. Information Requirements

- The identity and type of the funding actor *(consumed from Organisation & Partner Management for institutional donors)*.
- The terms of the commitment: amount, duration, restrictions, reporting obligations.
- The giving form and its obligation basis.
- The channel — formal institution or community network.
- Recipient-category eligibility where the giving form imposes one.

## 8. Business Concepts

### 8.1 Funding structure
*Source: `GLOSSARY.md` Donor & Resource Terms; `programme-management`.*

**Reality Knowledge**
- **Donor / Funder** — ratified as a humanitarian business concept by CL-002.
- **Grant** — a funding commitment instance issued by a donor, optionally funding one or more Programmes. `GLOSSARY.md` is explicit that a Programme may be funded directly, via a Grant, or both.
- **Contribution** — a single discrete act of giving: one gift, or one disbursement tranche of a Grant. `GLOSSARY.md` distinguishes it sharply from Grant: *"a Contribution records that one transfer occurred; a Grant represents the ongoing commitment."*
- **Funding Restriction** — the terms limiting how a resource may be used. Evidenced across three domains: sector, geographic and demographic earmarking (`programme-management/11-evidence.md`); origin constraints and embargoed-country restrictions (`resource-logistics/05-business-rules.md`); and localization quotas requiring a percentage of funding to flow through local NGOs (`organisation-partner-management/05-business-rules.md`).
- **Restricted vs. Unrestricted Funding** — `programme-management/04b-knowledge-patterns.md` names "The Fungibility Boundary" directly: restricted funding cannot be diverted to a different sector or target population without a formal Grant Amendment, unlike unrestricted funding which is highly fungible.

**Classification note.** `programme-management/03-concepts.md` currently classifies Grant as Operational Knowledge. That classification is reconciled under remediation B6 — a funding commitment carrying restrictions that determine recipient eligibility is decision-changing under Article IV. See `CONCEPT_OWNERSHIP.md` §8.

### 8.2 Islamic giving
*Source: `GLOSSARY.md` Donor & Resource Terms; HBRM Ch1 and Ch9; TD-01 BD-TD01-006.*

**Reality Knowledge**
- **Islamic Giving** — `GLOSSARY.md` names seven distinct, canonically defined charitable-giving forms recognised in this knowledge layer: **Zakat, Sadaqah, Sadaqah Jariyah, Waqf, Fidya, Kaffarah, Qurbani.** It states that each has its own obligation basis and restriction shape, and — importantly for modelling — that *"none is a synonym or regional alias for another."*
- **Zakat-Eligible Category** — one of the eight classical recipient categories (*asnaf*) to which Zakat funds may be distributed; a classification a Programme's Eligibility Rule may reference when a Programme is zakat-restricted (`GLOSSARY.md`).
- **Vertical Philanthropy** — formal, institutionalised Zakat organisations. *(HBRM Ch1, Ch9.)*
- **Horizontal Philanthropy** — informal, private Sadaqah given directly through community networks. *(HBRM Ch1, Ch9.)*

**Evidence disposition.** The vertical/horizontal distinction is the **only externally corroborated statement in this domain**: TD-01 Finding BD-TD01-006, Tier D, Medium confidence, two sources (Springer Nature 2020; ReliefWeb), applicability scope explicitly narrow to Islamic charitable-giving contexts. HBRM Ch1 states it as a structural difference with "different mechanisms of accountability, trust, and proximity," and HBRM Ch9 adds that "the rules of eligibility and accountability vary significantly between these frameworks."

**Insufficient repository evidence — recorded, not filled.** No repository source states:
- what the obligation basis of each of the seven forms actually is;
- what restriction shape each carries;
- what the eight asnaf categories are;
- how a beneficiary is determined to fall within an asnaf category;
- whether any other cultural or religious giving framework is in scope. *(This last is `ASSUMPTION_REGISTER.md` AR-013, which remains open.)*

These are deliberately **not** invented. `GLOSSARY.md` asserts that seven distinct forms exist and that they differ; the substance of those differences is genuinely undiscovered, and this domain records that rather than manufacturing it.

### 8.3 Resource
*Source: `GLOSSARY.md` Donor & Resource Terms.*

**Reality Knowledge**
- **Resource** — an abstract kind of thing that can be held and allocated: financial or material. `GLOSSARY.md` carries an explicit disambiguation warning that this is entirely distinct from **Recovery Resources** (a household's own internally-mobilizable coping assets, owned by the Vulnerability, Risk and Protection domain), and notes a Resource is never itself allocated with a quantity.

**Concepts explicitly *not* owned here** — all owned by Resource & Logistics, referenced only:
- **Inventory Item**, **Storage Location**, **Resource Allocation** (`GLOSSARY.md` assigns these to the tracked-stock and allocation layer, which is Resource & Logistics' subject matter per `resource-logistics/02-boundaries.md`).
- **Budget** and **Programme Budget** — owned by Programme Management (`CONCEPT_OWNERSHIP.md` §3.2).

## 9. Business Relationships

- A **Donor** issues a **Grant**.
- A **Grant** funds a **Programme**. *(Already stated in `programme-management/04-relationships.md`; referenced, not duplicated.)*
- A **Contribution** is a discrete transfer under a **Grant**, or a standalone act of giving.
- A **Funding Restriction** constrains a **Grant**, and transitively constrains the **Intervention Offerings** and **Eligibility Rules** derived from it. *(`KNOWLEDGE_TRANSFORMATION_PATTERNS.md` §4.5.)*
- An **Islamic Giving Form** determines the **Funding Restriction** shape carried by a **Contribution**.
- A **Zakat-Eligible Category** is referenced by an **Eligibility Rule** when a Programme is zakat-restricted. *(`GLOSSARY.md`, which is explicit that this is a reference, not a parallel eligibility engine.)*
- Giving flows through either a **Formal Giving Institution** or a **Community Giving Network**. *(HBRM Ch1.)*
- Liability for a **Grant** flows upward to the **Prime Recipient**. *(`organisation-partner-management/12-domain-invariants.md`.)*

**Plurality and temporal validity: partially evidenced.** A Grant may fund one or more Programmes (`GLOSSARY.md`); a Programme may be funded directly, by Grant, or both (`GLOSSARY.md`). Grant cycles are described as "rigid" with financial ceilings (`programme-management/05-business-rules.md`), implying temporal bounds, but no repository source states them.

## 10. Business Events

- **Funding Secured** — a grant or budget is formally committed. *(Already named in `programme-management/06-business-events.md`; referenced, not duplicated.)*
- **Contribution Received** — a discrete act of giving occurs.
- **Restriction Attached** — terms are bound to a resource at its origin.
- **Grant Amendment Requested / Granted / Refused** — the formal mechanism for altering a restriction. *(Derived from `programme-management/08-decision-points.md` §4, which names all three outcomes.)*
- **Grant Closed** — the commitment ends by expiry or exhaustion. *(Implied by `programme-management/06`, "Programme Closed: the initiative reaches its end date or exhausts funding.")*

## 11. Knowledge Patterns

- **The Hierarchical Constraint Pattern.** *Donor Mandate → Programme Allocation → Intervention Catalogue → Eligibility Rule → Support Plan Approval.* *(Already fully analysed in `KNOWLEDGE_TRANSFORMATION_PATTERNS.md` §4.5 and `programme-management/04b`; referenced, not duplicated.)* This domain owns its **origin** — the donor mandate that begins the chain.
- **The Fungibility Boundary.** *(Already named in `programme-management/04b`; referenced.)*
- **The Dual-Channel Pattern.** Giving flows through two structurally different mechanisms — formal institutional and informal community — carrying different accountability, trust and proximity characteristics, and different eligibility rules. *(HBRM Ch1, Ch9; TD-01 BD-TD01-006.)* This is the only pattern in this domain with external corroboration.
- **The Obligation-Travels-With-the-Resource Pattern.** A restriction originates with the giver and remains attached through allocation to the point of recipient eligibility. It is not re-negotiated downstream; it can only be formally amended at its origin. *(Derived from `programme-management/12-domain-invariants.md` read with §4.5 of the patterns document.)*

## 12. Policies

- **Universal.** Restricted funding cannot be fungibly shifted without formal reallocation, regardless of urgent ground need. *(`programme-management/12-domain-invariants.md`.)*
- **Universal.** Legal and financial liability flows upward to the primary grant holder. *(`organisation-partner-management/12-domain-invariants.md`.)*
- **Donor.** Funding may be earmarked by sector, geography or demographic target. *(`programme-management/11-evidence.md`.)*
- **Donor.** Origin constraints may prohibit purchase from specified countries. *(`resource-logistics/05-business-rules.md`.)*
- **Donor.** Localization targets may mandate that a percentage of funding flow through local NGOs. *(`organisation-partner-management/05-business-rules.md`.)*
- **Organisational (Khidmat).** Funding sources must align unconditionally with the operating principles; funding demanding proprietary data silos, exclusive commercial monetization of beneficiary data, or limits on the shared intelligence mandate is rejected. *(`BUSINESS_MASTER_PLAN.md` §4, Ethical Funding Safeguard.)*
- **Regional / Religious.** Where a giving form carries a recipient-category restriction, that restriction is an obligation on distribution, not a preference. *(`GLOSSARY.md` Zakat-Eligible Category.)*

## 13. Constraints

- **Financial.** Strict budget ceilings and rigid grant cycles. *(`programme-management/05-business-rules.md`.)*
- **Legal.** Anti-Money Laundering and Anti-Terrorism Financing checks gate any transfer of funds to an entity. *(`organisation-partner-management/05-business-rules.md`; `resource-logistics/08-decision-points.md` §3.)*
- **Legal.** Cross-border transfer is subject to restrictive banking law in conflict zones. *(`resource-logistics/08-decision-points.md` §3.)* Within the stated applicability context this is live, since donor and beneficiary geographies differ.
- **Structural.** Small grassroots organisations often lack the accounting systems required to pass donor due diligence, which restricts which channels funding can reach. *(`organisation-partner-management/05-business-rules.md`; the "Localization Paradox" of `organisation-partner-management/04b`.)*

## 14. Terminology

**Preferred terms:** Donor / Funder (the actor); Grant (the ongoing commitment); Contribution (the discrete transfer); Funding Restriction (the terms carried); Islamic Giving Form (the canonical category determining obligation and restriction).

**Ambiguous terminology.** *Resource* collides with *Recovery Resources* — an entirely distinct household-level concept owned by the Vulnerability, Risk and Protection domain. `GLOSSARY.md` already carries an explicit warning; it is restated here because the two domains now both exist and the collision is live.

*Giving* vs *Funding*: the repository uses "funding" for institutional flows and "giving" for individual and religious flows. Both are in scope; no repository source privileges either as the canonical term, so both are retained and the distinction is treated as real rather than terminological.

## 15. Exceptions

- **Emergency Reallocation (Crisis Modifier).** Re-routing restricted funds to an acute unforeseen crisis prior to formal donor approval. *(Already named in `programme-management/05b-exceptions.md`; referenced.)*
- **Donor refuses amendment despite extreme field necessity.** Named as an escalation condition with no stated resolution. *(`programme-management/08-decision-points.md` §4.)*
- **Need falling outside every applicable recipient category.** Structurally implied by restriction-bearing giving forms; **no repository source addresses it.**

## 16. Domain Dependencies

**Knowledge consumed from:**
- **Organisation & Partner Management:** the vetted institutional identity and trust state of an institutional donor or recipient organisation; due diligence clearance.

**Knowledge produced for:**
- **Programme Management:** funding commitments and the restrictions that bound programme design, intervention catalogues and eligibility rules.
- **Resource & Logistics:** origin constraints bearing on procurement and on permissible financial channels.
- **Accountability & Evaluation:** the donor obligations against which reporting and independent evaluation are required. *(`accountability-evaluation/05-business-rules.md` records that programmes over a financial threshold require mandatory independent endline evaluation — a donor-originated obligation.)*

## 17. Business Tensions

- **Donor restriction vs. humanitarian need.** *(Already named in `programme-management/05c-business-tensions.md`; referenced, not duplicated.)* This domain owns the origin of that restriction.
- **Donor accountability vs. affected-population accountability.** The repository's single strongest-evidenced tension — TD-02 BD-TD02-001, High confidence, ≥4 independent source families. It originates in this domain and is felt in Accountability & Evaluation.
- **Compliance vs. localization.** *(Already named in `organisation-partner-management/05c`; referenced.)*
- **Formal accountability vs. community proximity.** HBRM Ch1 records that vertical and horizontal philanthropy differ in accountability, trust and proximity; the formal channel is auditable and slow, the community channel is fast and locally legitimate but unauditable by donor standards.

## 18. Discovery Evidence

### Established Facts
- Donors are a recognised category of humanitarian actor. *(TD-01 BD-TD01-004, Tier B, Core Humanitarian Standard — a primary standard-setting source directly on point; ratified by CL-002. **The strongest external evidence in this domain.**)*
- Donor funding is rarely fungible; it is bound to sectors, geographies or demographic targets. *(`programme-management/11-evidence.md`; `programme-management/12-domain-invariants.md`.)*
- Islamic charitable giving splits structurally into vertical (formal, institutional) and horizontal (informal, community) mechanisms, with different eligibility and accountability rules. *(TD-01 BD-TD01-006, Tier D, Medium confidence, 2 sources; HBRM Ch1 and Ch9.)*
- Legal and financial liability flows upward to the prime grant holder. *(`organisation-partner-management/12-domain-invariants.md`.)*
- Grant and Contribution are distinct: a commitment versus a transfer. *(`GLOSSARY.md`.)*

### Reasonable Assumptions
- The seven Islamic giving forms are assumed to be canonically distinct with distinct obligation bases and restriction shapes, on the strength of `GLOSSARY.md` alone. The *distinctness* is assumed; the *substance* of each is not asserted. Recorded as AR-017.
- The existence of eight asnaf recipient categories is assumed on the same single source. Their content is not asserted. Recorded as AR-017.

### Open Questions
1. What is the obligation basis and restriction shape of each of the seven Islamic giving forms?
2. What are the eight Zakat-eligible recipient categories, and how is a beneficiary determined to fall within one?
3. Who determines the giving form of a contribution, and who adjudicates a disputed restriction?
4. How is a person in evident need handled when they fall outside every applicable recipient category?
5. Which other cultural or religious giving frameworks are in scope? *(`ASSUMPTION_REGISTER.md` AR-013, open.)*
6. How does giving through a community network — which by definition lacks formal accounting — enter a foundation whose institutional side requires due diligence?

### Knowledge Gaps
- **Tier A absent; Tier B/D present only via TD-01's two findings.** This domain has more external corroboration than Human Reality or Vulnerability/Risk, and still not enough to freeze.
- The substance of Islamic giving — the single most consequential body of knowledge here, since it determines recipient eligibility within the stated applicability context — is **entirely undiscovered**. `GLOSSARY.md` asserts that seven distinct forms exist; nothing states what they require.

## 19. Ontology Readiness

- **The commitment/transfer pair:** Grant as an ongoing commitment, Contribution as a discrete act under it.
- **The restriction as a travelling obligation**, originating with the giver and constraining recipient eligibility downstream — structurally a Constraint in the ontology sense, scoped by giving form.
- **The dual-channel structure** of formal and informal giving.
- **Giving form as a classification determining restriction shape** — a stable clustering, even though the shapes themselves are undiscovered.

## 20. Domain Completion Assessment

**❌ REQUIRES FURTHER DISCOVERY**

**Justification.** FG-4 is addressed as accepted: a domain now exists for giving and resource origin, ratified concept Donor has discovery behind it for the first time, funding restrictions are recorded as the eligibility-bearing constraints they are, and the Islamic giving framework is present in the canonical chain rather than only in an unevidenced glossary entry.

It cannot be frozen, and the reason is specific rather than generic: the **substance** of the seven Islamic giving forms and the eight asnaf categories is undiscovered, and within the applicability context stated in `BUSINESS_MASTER_PLAN.md` §2 that substance directly determines who may lawfully receive assistance. Asserting it without evidence would be inventing business knowledge in the one place where getting it wrong causes religious and legal harm. It is recorded as an open question and left open.
