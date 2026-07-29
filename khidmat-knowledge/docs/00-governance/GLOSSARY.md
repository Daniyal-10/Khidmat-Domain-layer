---
id: DOC-GOV-003
title: Khidmat Ubiquitous Language Glossary
version: 1.1
status: Candidate Vocabulary — non-normative pending per-term provenance (downgraded from Normative under remediation B15)
owner: Governance
reviewers: Governance
last_updated: 2026-07-28
depends_on: docs/00-governance/PROJECT_OVERVIEW.md (v1.0), docs/01-methodology/BUSINESS_MASTER_PLAN.md (v1.0), docs/01-methodology/HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md (v1.0), docs/01-methodology/BUSINESS_ARCHITECTURE.md (v1.0)
consumed_by: All Downstream Documents
layer: 00-governance
domain: Foundation
tags: [glossary, terminology, ubiquitous-language]
---

# Khidmat Ubiquitous Language

> ## Status: Candidate Vocabulary — non-normative
>
> **Downgraded from `Normative` on 2026-07-29 under remediation B15.**
>
> **Why.** This glossary defines roughly 120 terms. The accepted Foundation Readiness Assessment established that a large proportion of them appeared in no discovery document anywhere in the repository — the risk, resilience, protection, human-model, community-context, giving and intervention-fit vocabularies among them. A document with `status: Normative` makes those terms binding on all downstream work, which conflicts with Constitution Article V (*"an unsupported assertion is not evidence merely because it has been recorded"*) and with `ONTOLOGY_DESIGN.md` §6, which applies the same rule to the ontology's own design decisions including those sourced from frozen artifacts.
>
> Two further problems flow from the same cause. This glossary pre-commits **enumerated value sets** (four resilience capacities, seven Islamic giving forms, eight recipient categories, four trajectory values, four claim-basis values, three need-relationship qualifiers, four intervention-relationship types) and **relationship semantics** (`need_influences_need`, `assertion_influences_assertion`). Under `ONTOLOGY_DESIGN.md` AR-7 (design purity) enumerated value sets are deferred to engineering, and under AR-2 relationship placement is decided by the promotion test. A normative glossary that fixes both in advance is a structural commitment made before ontology design — the precise failure `PROJECT_OVERVIEW.md` Ch5.1 warns against.
>
> **What changed as a result of remediation.** Terms that have since acquired discovery are no longer glossary-only. Under B2, B3, B4 and B5 the human-model, risk/resilience/protection, community-context, giving and need/intervention/outcome vocabularies were promoted into discovery documents where each term carries an explicit disposition — **Validated (Tier C)** where a repository source independent of this glossary corroborates it, **Carried unvalidated** where it does not. Those dispositions, not this glossary, are now the authority on evidential weight.
>
> **How to use this document.** As candidate vocabulary and as the repository's index of terminology in use. It remains the right place to look up what a term means. It is not authority that the term is real, and no ontology design decision may cite it as evidence on its own.
>
> **Path back to Normative.** Per-term provenance across the whole document, and removal or deferral of the enumerated value sets. Neither is in scope for the current remediation phase.

## Core Terms

**Beneficiary**
The person whose need is being registered, verified, or addressed.
The beneficiary is not always the registrant.

**Registrant**
The person conducting the registration conversation.
May be the beneficiary, a proxy, or a volunteer.

**Household**
The unit of people sharing living conditions and pooled resources.
The primary context for assessing vulnerability and need.

**Situation**
A set of circumstances that create or sustain vulnerability for a household.
A household may have more than one simultaneous situation.

**Need**
A specific, concrete gap between a household member's current state
and a basic standard of wellbeing.
Needs are contextualised by situations but are not synonymous with them.

**Need Relationship (need_influences_need)**
A diagnosed connection between two confirmed needs within the same case,
distinct from a situation contextualising a need. Qualified by
need_relationship_type: contributes_to (the source need drives or worsens
the target need â€” e.g. income instability contributes_to food insecurity),
blocks (the source need must be resolved before the target can be
effectively addressed â€” e.g. a documentation gap blocks an income_support
need), or compounds (the source need increases the target's severity
whenever both are present, without causing it â€” e.g. a disability compounds
a caregiver_burden need). Mirrored at the synthesized-finding level in the Needs
Assessment domain as assertion_influences_assertion.

**Debt Source and Debt Characteristic**
Two independent classifications elaborating a situation's unmanageable_debt
indicator. Debt source records who or what the debt is owed to (formal
institution, self-help group/cooperative, government-supported credit,
employer advance, family/relatives, friends/community, shopkeeper/vendor
credit, informal moneylender, or mixed/multiple sources). Debt
characteristic records the humanitarian shape of the debt situation as a
whole â€” manageable, burdensome, high_risk, or exploitative â€” never a
monetary threshold, balance, or interest calculation.

**Claim**
An assertion made during registration that requires external confirmation.
Claims are made by registrants. Needs generate claims. Claims require verification.

**Evidence**
Material that may support or refute a claim.
Evidence is identified during registration and confirmed during verification.

**Support Intervention**
The specific type of assistance being requested to address a need.
Distinct from the delivery mechanism, which is determined post-verification.

**Case**
The central, long-lived operational container coordinating holistic support for a subject. A case governs the sequence of assessment, planning, implementation, and closure for an individual or household.

**Verified Claim**
The atomic unit of truth. An assertion made during registration or assessment that has been externally confirmed via the Verification capability, forming the justified basis for support planning.

**Gap**
A piece of information required to adequately understand the beneficiary's situation that has not yet been provided during registration. Gaps are classified by severity: critical, high, or medium.
Gap types will be formally enumerated during ontology engineering.

**Registrant Type**
The role of the person conducting the registration.
Values: beneficiary (self-registering), proxy (on behalf of another), volunteer (field worker).

**Claim Basis**
The epistemic relationship between the registrant and the claim they are making.
Values: first_hand, second_hand, observational, inferred.
Determines verification weight and questioning approach.

**Trajectory**
The pattern of how a situation developed over time.
Values: structural (chronic, pre-existing), crisis_triggered (caused by an event),
progressive (gradually worsening), acute (sudden onset).

## Human Model Terms

**Lifecycle Stage**
A developmental stage of human life associated with characteristic needs, dependencies, capabilities, vulnerabilities, and expected outcomes.
Examples include infant, child, adolescent, adult, and elderly.
Lifecycle stages are reasoning concepts, not merely age ranges.

**Capability**
A person's ability to perform activities, contribute to household wellbeing, participate in society, or support others.
Capabilities represent strengths and assets rather than deficits.

**Dependency**
A relationship in which one person relies on another for care, support, resources, supervision, protection, or decision-making.
Dependencies may be developmental, physical, financial, emotional, or legal.

**Family**
A social unit consisting of individuals connected through kinship, caregiving, marriage, guardianship, or other recognised relationships.
A family is distinct from a household.
Multiple families may exist within a household.

## Risk and Vulnerability Terms

**Vulnerability**
A condition that increases exposure to harm or reduces the ability to withstand adverse circumstances.
Vulnerability may exist at individual, family, household, or community level.

**Risk Factor**
A characteristic, condition, event, or circumstance that increases the likelihood of a negative outcome.
A risk factor does not necessarily indicate current harm.

**Household Resilience**
The composite household-level capacity to maintain essential functioning, adapt to disruption, and recover from adversity.

**Absorptive Capacity**
The capacity of a household to continue functioning during disruption without immediate breakdown of essential support structures, responsibilities, and household operations.

**Adaptive Capacity**
The capacity of a household to reorganize responsibilities, substitute disrupted functions, and adjust internal arrangements in response to changing circumstances.

**Recovery Capacity**
The capacity of a household to restore stability and re-establish essential functioning following disruption or loss.

**Support Redundancy**
The presence of alternative providers for critical household support functions such that disruption of a single individual does not eliminate a required household function.

**Role Substitution Capacity**
The ability of a household to replace, compensate for, or redistribute a disrupted support role among available household members and existing support relationships.

**Buffering Capacity**
The ability of a household to absorb disruption while maintaining essential household functioning and stability.

**Recovery Resources**
Existing household-accessible assets, relationships, capabilities, and internal support resources that can be mobilized to restore household functioning after disruption.

**Caregiving Continuity**
The ability of a household to maintain necessary caregiving support despite disruption affecting individual caregivers.

**Decision Continuity**
The ability of a household to maintain effective decision-making and authority structures despite disruption affecting individual decision-makers.

**Risk**
A qualitative, forward-looking assessment of the likelihood and potential severity of harm to a specific person, family, or household.

**Risk Composition**
The structured qualitative composition of hazard categories, exposure, vulnerability, and household resilience that together create a risk condition.

**Risk Characterization**
The qualitative interpretation of a risk composition describing the nature, pattern, and overall expression of risk at the point of assessment.

**Risk Profile**
The structured representation of a current risk picture including the underlying composition, characterization, and associated risk attributes.

**Protective Factor**
The atomic, symmetric inverse of a Risk Factor. A positive, present condition that moderates hazard-specific risk. Assessed by positive characterisation, not logical negation of a risk.

**Financial Buffer**
Accumulated household economic reserves (savings, assets) functioning as a structural economic floor independently of current earning.

**Livelihood Diversity**
The structural independence of a household's income sources across independently-failing modes, distinct from mere count of earners.

**Treatment Continuity Active**
The positive state where a person with a manageable health condition is currently receiving functioning treatment, maintaining a stable health trajectory rather than deteriorating.

**Hazard Category**
The qualitative classification of what kind of harm a risk factor relates to (not its geographic or temporal instantiation).

**Exposure**
The relationship between a person/household and a hazard category describing the degree to which they are positioned to encounter it.

**Risk Horizon**
The qualitative timeframe within which harm may occur if current conditions persist.

**Intervention Objective Category**
The underlying humanitarian purpose an intervention serves (survival and
stabilization, restoration, capacity building, protective, connective, or
resilience building), independent of its delivery modality (cash, voucher,
in-kind, service, asset) and its thematic sector (WASH, livelihood,
health, etc.).

**Intervention Readiness**
A structured, qualitative judgement (ready / partially_ready / not_ready
/ not_assessed) of whether the actual context and capacity for a
specific intervention are currently in place for a specific beneficiary
or household. Distinct from eligibility (categorical, rule-based
qualification), vulnerability (latent susceptibility to harm), and
capability (general ability independent of any specific intervention).

**Intervention Relationship (prerequisite / mutually exclusive / reinforces / substitutes)**
Four relationships between intervention offerings recording that one
ordinarily precedes another, that two should not ordinarily be combined,
that two strengthen each other without either being a strict
prerequisite, or that two address the same underlying need such that
ordinarily only one would be selected.

**Protection Indicator (Exploitation and Coercion Indicators)**
A specific, independently observable behavioural or circumstantial signal â€”
such as coached testimony, an evasive travel or work account, inability to
confirm a claimed relationship, an age/document mismatch, third-party
control of documents or earnings, or restricted movement â€” that experienced
officers recognise as warranting closer attention and possible safeguarding
referral. An indicator is a prompt for care, not a conclusion that
exploitation, trafficking, or coercion has occurred. Owned by the Risk
Domain under the social_protection hazard category; recorded, when
observed in a specific case, on Registration's situation entity.

**Risk Trend**
A qualitative assessment of whether risk appears to be improving, stable, deteriorating, or uncertain at the point of assessment.

**Risk State**
The current qualitative status of risk at the time of assessment.

**Risk Severity**
The qualitative characterization of the potential impact of harm should the identified risk materialize.

**Compound Risk**
Concentration compounding and interaction compounding between co-occurring risk factors.

## Verification Operations Terms

**Verification Subject**
The target of verification. This is typically a claim or assertion made during registration that requires external confirmation.

**Verification Activity**
A verification event performed against a verification subject. It is time-bound, evidence-generating, and repeatable.

**Field Observation**
A direct observation recorded during a verification activity.

**Verification Finding**
A verification conclusion derived from verification inputs and field observations.

**Reverification Trigger**
A condition indicating that future verification should occur, derived from a verification finding (e.g., expiring evidence, temporary documentation).

**Verification Outcome**
A derived concept representing the final verification decision; derived from verification findings and not a first-class ontology concept itself.

## Outcome Terms

**Outcome Indicator**
A measurable signal used to assess whether an intervention produced meaningful change in a beneficiary, family, household, or community.
Outcome indicators support lifecycle tracking, Programme evaluation, and impact measurement.

## Needs Assessment Terms

**Assessment Session**
The episodic event of applying an assessment instrument to a person, household, or community at a specific time and location.

**Observation**
A raw, uninterpreted piece of evidence or data point gathered during an assessment session.

**Need Assertion**
The synthesized, evidence-weighted conclusion that a subject has a specific deficit, vulnerability, or capacity gap â€” distinct from Registration's Need, which is the intake-time claim it synthesizes.

**Confidence Level**
The degree of certainty attached to an observation or finding: high, medium, low, or highly uncertain.

**Finding Consensus**
The governance record that resolves conflicting findings or elevates a finding to authoritative status.

## Case Management Terms

**Case Plan**
The structured, approved operational strategy guiding the coordination of interventions for a Case. Addressed by one or more Support Interventions.

**Referral**
A formal request for a specialized service provided by an internal (Programme) or external (Organisation) party.

**Follow-Up**
A scheduled or completed case-level review or monitoring activity revisiting a beneficiary's situation after initial support.

## Beneficiary Lifecycle Terms

**Engagement Stage**
The beneficiary's administrative relationship to the Khidmat ecosystem (identified, registered, active, engaged, monitored, exited, etc.). Strictly distinct from Human Development Stage.

**Human Development Stage**
The beneficiary's or household's own position in the humanitarian developmental trajectory â€” crisis, stabilization, recovery, self-reliance, resilience, or community contribution. Never to be conflated with Engagement Stage.

**Lifecycle Transition**
An immutable event representing a macro-state change within a beneficiary's lifecycle, optionally triggered by a registration case, a verification finding, a risk characterization, a case decision, or an impact evaluation.

## Programmes Terms

**Organisation**
The formally registered external implementing body that holds legal accountability, employs staff, and manages overarching resources. Distinct from the Programmes it runs.

**Programme**
The bounded structural initiative through which assistance is funded, governed, and delivered, possessing specific eligibility criteria.

**Intervention Offering**
A specific support modality and conditionality defined within a Programme's catalogue.

**Enrollment**
The macro-state and historical record of a beneficiary's participation in a Programme.

## Community Context Terms

**Settlement Type**
The classification of a community's physical settlement pattern (e.g., rural, peri-urban, informal urban).

**Local Organisation**
A persistent, community-native civic, economic, or mutual-aid institution (e.g., a micro-savings and credit collective, a women's collective), distinct from formally registered external organisations.

**Livelihood Pattern**
The dominant, persistent community-level economic activity base â€” a macro-economic classification, distinct from any individual household's own employment or enterprise status.

## Support Delivery Terms

**Delivery Event**
The fundamental unit of execution, representing the grouping, timing, and occurrence of a delivery. Fulfills a Case Plan.

**Delivery Modality**
The physical, financial, or service form a delivery takes, and the handling/custody requirements that come with it â€” distinct from Programmes' Intervention Modality and Thematic Sector.

**Proof of Delivery**
Evidence collected during the handover confirming a delivery occurred.

**Chain of Custody**
The sequence of Custody Transfers tracking goods between custodians before reaching the final beneficiary.

**Volunteer**
A frontline responder who contributes time, skills, and effort to conduct field operations, assessments, verification, or direct delivery without acting as a formal, compensated employee of an implementing Organisation.

**Assignment**
The operational association between a volunteer and a field task (e.g., a registration, a verification activity, a delivery event) they are responsible for carrying out.

## Donor & Resource Terms

**Donor / Funder**
An actor that provides financial, material, or technical support to implementing Organisations, enabling humanitarian work without necessarily delivering direct assistance themselves. Donors introduce accountability requirements regarding how resources are allocated, utilized, and reported.

**Grant**
A funding commitment instance issued by a Donor Profile, optionally funding one or more Programmes. Distinct from, and additive to, a Programme's existing direct funding-by-organisation relationship â€” a Programme may be funded directly, via a Grant, or both.

**Contribution**
A single discrete act of giving: one gift, or one disbursement tranche of a Grant. Distinct from Grant itself â€” a Contribution records that one transfer occurred; a Grant represents the ongoing commitment.

**Resource**
An abstract kind of thing Khidmat holds and can allocate â€” financial or material. Not to be confused with **Recovery Resources** (Risk and Vulnerability Terms, above), which describes a household's own internally-mobilizable coping assets; this is an entirely distinct, unrelated concept describing humanitarian stock Khidmat itself holds. A Resource is never itself allocated or tracked with a quantity â€” see Inventory Item.

**Inventory Item**
The tracked instance of a Resource: a specific quantity, in a specific condition, at a specific Storage Location, right now. Never collapsed into Resource â€” Resource describes the kind; Inventory Item describes the tracked stock.

**Storage Location**
A physical space (warehouse, distribution Centre, cold-chain facility, temporary storage site, or mobile storage unit) holding Inventory Items. Not a software or database concept.

**Resource Allocation**
The decision that reserves or commits a specific Inventory Item to a Programme or a Case Plan, before delivery. Distinct from delivery itself, which remains Support Delivery's Delivery Event.

**Islamic Giving**
Seven distinct, canonically defined charitable-giving forms recognized in this knowledge layer: Zakat, Sadaqah, Sadaqah Jariyah, Waqf, Fidya, Kaffarah, and Qurbani. Each has its own obligation basis and restriction shape; none is a synonym or regional alias for another.

**Zakat-Eligible Category**
One of the eight classical recipient categories (asnaf) to which Zakat funds may be distributed. A classification a Programme's Eligibility Rule may reference when a Programme is zakat-restricted â€” not a second eligibility engine.

## Governance Terms

**Concept Ownership**
The assignment of a concept to exactly one authoritative file or domain.
A concept may be referenced by many files but may only be defined by one owner.

## Business Domains & Capabilities (Added from Stage 4)

**Case Management Domain**
The business domain responsible for the individual and household lifecycle, including screening, context and needs assessment, support planning, and ongoing case monitoring.

**Programme Management Domain**
The business domain governing macro-level coordination, resourcing, budget allocation, and strategic boundaries of humanitarian assistance.

**Resource and Logistics Domain (Material Flow)**
The business domain managing the physical and financial execution of assistance, translating approved support plans into the delivery of goods, services, or cash.

**Accountability and Evaluation Domain**
The business domain providing systemic oversight and independent learning mechanisms to ensure operations meet ethical standards and intended outcomes.

**Cross-Organisational Coordination Domain**
The business domain facilitating the sharing of verified evidence and operational context across different humanitarian actors to prevent duplication.

**MEAL (Monitoring, Evaluation, Accountability, and Learning)**
A structured capability dedicated to observing operations, evaluating outcomes against intended objectives, and integrating lessons into future programme design.

**Complaints and Feedback Mechanisms (CFM)**
A dedicated, structurally separate capability providing affected populations with a direct channel to raise grievances, report abuse, or provide feedback.

**Evidence & Knowledge Acquisition**
The ability to continuously gather claims, observations, and data from affected populations and the operational environment.

**Understanding Formation**
The ability to synthesize disparate pieces of evidence into a coherent, contextual understanding of a person's or community's reality.

**Reasoning & Justified Recommendation**
The ability to evaluate needs against available resources and constraints to produce actionable, justifiable recommendations for assistance.

**Responsible Action**
The ability to execute recommendations safely and effectively, delivering the planned support to the intended recipient.