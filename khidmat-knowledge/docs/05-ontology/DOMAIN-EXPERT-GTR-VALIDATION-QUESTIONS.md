# Domain Expert GTR Validation Questions (Draft)

This document serves as the **Master Question Set** for the upcoming Ground Truth (GT) validation sessions with the Khidmat domain expert. 

**Purpose:** The goal is *not* to defend or confirm the current ontology design, but to discover actual operational reality. The answers to these questions will provide the real-world evidence required to resolve the existing 47 Ground Truth Review (GTR) items, allowing us to confidently move them to Confirmed, Refined, or Challenged states.

---

## 1. Facets (Dimensions & Characteristics)

**Question 1.1: Categorizing Human Needs and Conditions**
- **Main question:** When assessing a person or household, what specific categories of information do you actually record in practice (e.g., health, shelter, capabilities)? Are there categories you track that do not neatly fit into standard templates?
- **Why we need the answer:** To validate the axes of our Facets layer against actual field data collection, and see if our definitions of conditions and states match reality.
- **Evidence/Example to ask for:** Blank or redacted intake forms, survey templates, or system screenshots showing dropdowns/fields.
- **Ontology area affected:** Facets (L1), Condition (P1).
- **Resolves GTR:** GT-L1, GT-OQ4, GT-P1.

**Question 1.2: Compounding Vulnerabilities**
- **Main question:** When a household has multiple overlapping issues, how do you practically determine and record that they are "highly vulnerable"? Is there an explicit rule/formula, or is it a caseworker judgment call?
- **Why we need the answer:** To understand if vulnerability is composed of measurable facets or is an emergent, subjective state.
- **Evidence/Example to ask for:** A case record or assessment matrix showing how multiple risks were aggregated into a final vulnerability score or decision.
- **Ontology area affected:** Facets, Condition (P1).
- **Resolves GTR:** GT-OQ2, GT-PL3, GT-OQ9.

**Question 1.3: Conceptualizing the Individual**
- **Main question:** When thinking about a person you are assisting, do you naturally group their identity, age/lifecycle, physical capability, and health together as "facts about the person," completely separate from their external environment or household? 
- **Why we need the answer:** To test whether our Pillar I boundary (keeping human attributes strictly separated from household, environmental factors, or needs) matches actual practitioner mental models.
- **Evidence/Example to ask for:** Examples of how caseworkers narratively describe a person in free-text case notes.
- **Ontology area affected:** Pillar I (Human & Social Subject).
- **Resolves GTR:** GT-PL1.

## 2. Entities (Things That Persist)

**Question 2.1: Identity and Person Resolution**
- **Main question:** Without using biometrics, how do you determine if a newly registered person is the same person already in your system? What happens when you are unsure, and how often does this fail?
- **Why we need the answer:** Our ontology relies heavily on "Person" persisting across encounters. We need to know how identity matching actually works (and fails) on the ground.
- **Evidence/Example to ask for:** Standard operating procedures (SOPs) for registration, or an email/communication thread resolving a duplicate or mistaken identity.
- **Ontology area affected:** Entities (L2, P4).
- **Resolves GTR:** GT-OQ1, GT-P4, GT-AR6.

**Question 2.2: Organisations vs. Programmes**
- **Main question:** In your day-to-day operations, do you treat "the organisation" providing the aid and "the programme" under which the aid is provided as the same thing, or do you have to track them distinctly?
- **Why we need the answer:** The current ontology collapses these into a single entity, which may contradict how practitioners view and interact with them.
- **Evidence/Example to ask for:** Reporting structures, referral forms, or partnership agreements that show how entities refer to themselves.
- **Ontology area affected:** Entities (L2).
- **Resolves GTR:** GT-OQ6, GT-PL5.

**Question 2.3: Defining a "Case" and Service Providers**
- **Main question:** What actually constitutes a "case" in your records? Additionally, do you interact with service providers (schools, clinics) as distinct actors with their own interests, or merely as locations/services a person accesses?
- **Why we need the answer:** To ensure our definitions of Case and Actor/Service Provider align with operational boundaries.
- **Evidence/Example to ask for:** Case management system documentation or redacted case summaries; referral logs to external providers.
- **Ontology area affected:** Entities (L2).
- **Resolves GTR:** GT-L2, GT-OQ15, GT-OQ7.

## 3. Relationships (Connections & Dependencies)

**Question 3.1: Household vs. Family Structure**
- **Main question:** Have you had cases where someone's "family" and their "household" did not match (e.g., due to displacement, fostering, migration)? How did you decide who gets recorded under which group for assistance purposes?
- **Why we need the answer:** To correctly model the boundaries and overlap between Family and Household entities.
- **Evidence/Example to ask for:** Real case notes or registration forms handling split families or non-relative households.
- **Ontology area affected:** Relationships (L3, P7).
- **Resolves GTR:** GT-OQ3.

**Question 3.2: Dependency Cascades and Need Interactions**
- **Main question:** Can you describe a real situation where a risk or vulnerability in one person directly caused a need in another person who depends on them? Have you encountered children who were orphaned but well-guardianed, or unguardianed but not orphaned?
- **Why we need the answer:** To validate how needs and risks transfer across social ties, which is currently unevidenced in our foundation.
- **Evidence/Example to ask for:** Case notes showing support for dependents, specifically addressing guardianship or compounding household needs.
- **Ontology area affected:** Relationships (P7).
- **Resolves GTR:** GT-P7, GT-OQ16, GT-OQ18, GT-L3.

## 4. Constraints (Rules & Limits)

**Question 4.1: Conflicting Rules and Constraints**
- **Main question:** Have you ever faced a situation where two rules conflicted (e.g., donor reporting requirements vs. a family's preference for privacy)? How was it actually handled on the ground? 
- **Why we need the answer:** To understand if constraints decompose cleanly into a rule + scope, or if they clash and require overriding context.
- **Evidence/Example to ask for:** Email threads discussing policy overrides, or notes detailing exceptions made.
- **Ontology area affected:** Constraints (L4, P5).
- **Resolves GTR:** GT-L4, GT-P5, GT-AR5, GT-OQ14 (Consent).

**Question 4.2: Funding Restrictions and Wellbeing Standards**
- **Main question:** What practical standards or restrictions dictate whether someone is eligible for assistance? What standard defines that someone has "enough" and no longer has a need?
- **Why we need the answer:** To validate the taxonomy of rules and restrictions bounding the work.
- **Evidence/Example to ask for:** Donor agreements, eligibility checklists, or standardized wellbeing baselines.
- **Ontology area affected:** Constraints.
- **Resolves GTR:** GT-OQ8, GT-OQ11.

## 5. States (Changes Over Time)

**Question 5.1: Tracking Outcomes and Impact**
- **Main question:** After an intervention is provided, how do you record whether it actually worked? Is this done by the case manager on the same timeline, or by a separate monitoring team later?
- **Why we need the answer:** To determine who owns the state change of an outcome and when it gets recorded (Case Journey vs. MEAL).
- **Evidence/Example to ask for:** Post-distribution monitoring (PDM) surveys, MEAL reports, or case closure records.
- **Ontology area affected:** States (L5).
- **Resolves GTR:** GT-OQ5, GT-PL6.

**Question 5.2: Evolving Conditions vs. Admin Status**
- **Main question:** How do you record changes in a person's life situation separately from their administrative status in your programme? Does the same condition (e.g., damaged roof) mean something different depending on context (season, location)?
- **Why we need the answer:** To validate the separation of administrative clocks from lived-reality clocks, and test context-dependent states.
- **Evidence/Example to ask for:** System screenshots showing status fields vs. condition/needs fields; documentation showing varying criteria across contexts.
- **Ontology area affected:** States (L5), Context (P2).
- **Resolves GTR:** GT-AR3, GT-L5, GT-PL2, GT-P2.

## 6. Events (Moments in Time)

**Question 6.1: Non-Linear Case Timelines**
- **Main question:** Could you walk through a real case from first contact to the present, focusing on dateable events? How often do cases go "backwards" (e.g., reopening, reassessment) instead of straight through to closure? What constitutes a single event vs an ongoing state?
- **Why we need the answer:** To test our assumption of non-linearity and understand the precise boundary between an Occurrence (event) and a Condition (state).
- **Evidence/Example to ask for:** A chronological case log, history view from a database, or a documented timeline of a complex case.
- **Ontology area affected:** Events (L6, P6).
- **Resolves GTR:** GT-L6, GT-P6, GT-AR2.

## 7. Cognition (Claims, Evidence, and Verification)

**Question 7.1: Missing vs. Negative Information**
- **Main question:** In your records, how do you practically distinguish between "we checked and this is not true" versus "we have not checked this yet"?
- **Why we need the answer:** Validates the open-world commitment of the ontology (Epistemic Stance)—absence of evidence is not evidence of absence.
- **Evidence/Example to ask for:** Survey forms indicating "N/A" vs blank fields, or data entry guidelines on how to handle unknowns.
- **Ontology area affected:** Cognition (L7, P3).
- **Resolves GTR:** GT-L7, GT-OQ12, GT-P3.

**Question 7.2: Conflicting Information and Evidence Weighting**
- **Main question:** If two sources give you contradictory information about a family's situation, what happens to both pieces of information? What kinds of evidence carry more weight in your practice?
- **Why we need the answer:** To understand how contradictory claims and evidence hierarchy are handled in practice, and what decisions require human oversight.
- **Evidence/Example to ask for:** Verification reports, case notes resolving discrepancies, SOPs on evidence hierarchy, or examples of mandatory human sign-offs.
- **Ontology area affected:** Cognition.
- **Resolves GTR:** GT-PL4, GT-OQ13, GT-OQ10, GT-AR4.

## 8. Coordination Patterns (Multi-Actor Flows)

**Question 8.1: Handoffs, Referrals, and Service Delivery**
- **Main question:** When referring a case to another person or organization, what makes it a "referral" or "handoff" rather than a brand new case for them? Is there a distinct role for case coordination across organizations?
- **Why we need the answer:** To validate recurring humanitarian flows and understand case orchestration across boundaries.
- **Evidence/Example to ask for:** Referral forms, inter-agency email threads, or service delivery logs.
- **Ontology area affected:** Coordination Patterns (L8).
- **Resolves GTR:** GT-L8, GT-OQ19, GT-PL7.

**Question 8.2: Funder and High-Level Coordination**
- **Main question:** Have you seen situations where terms like "needs assessment" or "coordination" meant something completely different at a high programme/funder level compared to an individual casework level? Does funder coordination happen on a distinct layer?
- **Why we need the answer:** To check the altitude qualification rules and funder orchestration mechanics.
- **Evidence/Example to ask for:** Program-level strategy documents, inter-agency meeting minutes, compared against casework guidelines.
- **Ontology area affected:** Coordination Patterns.
- **Resolves GTR:** GT-AR1, GT-OQ17.

---

## Resolution Flow

During and after the discussion with the domain expert, we will follow this flow for every finding:

1. **Domain expert answer** (Their practical explanation)
2. **→ Real operational evidence/example** (Forms, emails, systems, SOPs)
3. **→ Compare with current GTR assumption** (What our ontology currently states)
4. **→ Determine** `CONFIRMED` / `REFINED` / `CHALLENGED` / `UNRESOLVED`
5. **→ Identify ontology implication** (Which layers/primitives are affected)
6. **→ Remediation** (Drafting changes to the architecture if needed)
7. **→ Governance/closure where required** (Escalation to final audit)
8. **→ Final authoritative ontology** (Updated source files)

---

## What We Need From the Domain Expert

To the domain expert: **We need ground-level reality.**

Our goal is not to get you to agree with a theoretical model we have built. Our goal is to test if our model survives contact with actual field operations. 

We need you to:
- Describe reality in your own operational language.
- Point out where our assumptions completely miss how things actually happen.
- Provide concrete examples, stories, and edge cases.
- Show us (where safe and permitted) the artifacts you actually use: surveys, intake forms, emails, MEAL reports, case management screens, and templates. 

If something we ask doesn't make sense in the context of your daily work, that friction itself is an answer we need to document.
