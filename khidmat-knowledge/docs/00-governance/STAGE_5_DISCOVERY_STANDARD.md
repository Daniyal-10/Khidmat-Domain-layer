---
id: DOC-GOV-STAGE_5_DISCOVERY_STANDARD
title: STAGE 5 DISCOVERY STANDARD
version: 1.0
status: Active
owner: Governance
---
# Khidmat AI — Stage 5 Domain Discovery Standard

## 1. Objective
This document establishes the official methodology, structure, and quality expectations for Stage 5 Domain Discovery within the Khidmat AI Foundation pipeline. It ensures every future discovery document captures humanitarian business reality consistently, comprehensively, and independent of implementation.

## 2. Discovery Principles
The Discovery Standard mandates adherence to the following core principles:
- **Reality First:** Document how humanitarian assistance actually works, not how software expects it to work.
- **Business First:** Focus on capabilities, decisions, and outcomes.
- **Evidence Driven:** Separate established facts from assumptions and open questions.
- **Architecture Aligned:** Strictly respect the domain boundaries defined in `BUSINESS_ARCHITECTURE.md`.
- **Ontology Independent:** Discover concepts and relationships without creating classes, properties, or RDF schemas.
- **Implementation Independent:** Ignore software architecture, databases, and APIs.
- **Technology Neutral:** Focus on human and organisational activity.

**Prohibited Artifacts:**
Software design, APIs, Databases, Workflows, BPMN, UML, ER Diagrams, RDF, OWL, Class Models, Microservices, and Technical Architecture are strictly prohibited during Stage 5.

## 3. Mandatory Discovery Sections
Every Domain Discovery document SHALL contain the following 20 sections in exact sequence:

1. **Purpose:** Why does the domain exist? What humanitarian problem does it solve? Why can't another domain own these responsibilities?
2. **Business Outcomes:** What successful outcomes does the domain produce? (Focus on business value, not operational tasks).
3. **Stakeholders:** Explicitly separate *Actors* (enduring participants) from *Roles* (transient responsibilities). Capture their purpose, responsibilities, interactions, and dependencies.
4. **Business Capabilities:** The enduring capabilities owned by the domain. (Do not redefine Business Architecture).
5. **Core Business Activities:** Recurring business activities required to execute the capabilities. (Do not describe step-by-step workflows).
6. **Business Decisions:** For every significant decision identify: purpose, decision maker, supporting evidence, governing policies, constraints, preconditions, alternative outcomes, escalation conditions, review triggers, appeal mechanisms, human override requirements, and uncertainty.
7. **Information Requirements:** Conceptual knowledge consumed by the domain. (Do not design information systems or tables).
8. **Business Concepts:** Important concepts naturally used by practitioners. (Do not classify or model them).
9. **Business Relationships:** Conceptual relationships described naturally (e.g., *Need justifies Support Plan*). (Do not create ontology).
10. **Business Events:** Meaningful business events (e.g., *Referral Accepted, Consent Withdrawn*).
11. **Knowledge Patterns:** Recurring conceptual patterns (e.g., *Claim -> requires -> Evidence -> supports -> Decision*).
12. **Policies:** Delineated by altitude (Universal, Regional, Government, Donor, Organisation, Programme) where applicable.
13. **Constraints:** Humanitarian, ethical, legal, financial, operational, security, political, or cultural constraints applicable to the domain.
14. **Terminology:** Preferred terms, synonyms, and ambiguous terms. (Do not modify the Foundation Glossary).
15. **Exceptions:** Unusual but legitimate business situations and edge cases.
16. **Domain Dependencies:** Explicitly document knowledge consumed from other domains, knowledge produced for other domains, and business dependencies. (Do not describe technical integrations).
17. **Business Tensions:** The competing forces the domain continuously balances (e.g., *Speed vs Accuracy, Equity vs Efficiency*).
18. **Discovery Evidence:** Separate findings strictly into *Established Facts*, *Reasonable Assumptions*, *Open Questions*, and *Knowledge Gaps*.
19. **Ontology Readiness:** Conceptual clusters likely to become stable ontology foundations. (Do not create ontology).
20. **Domain Completion Assessment:** Conclude whether the domain is `READY FOR FREEZE` or `REQUIRES FURTHER DISCOVERY` with architectural justification.

---

## 4. Reusable Discovery Template
*(Copy and paste this template for all future Stage 5 Discovery documents)*

```markdown
---
id: DOC-DISC-[DOMAIN_NAME]
title: [DOMAIN_NAME] DOMAIN DISCOVERY
version: 1.0
status: Draft
owner: Discovery
---
# [Domain Name] Domain Discovery Report

## 1. Purpose
[Describe why the domain exists, the problem it solves, and why it holds exclusive ownership.]

## 2. Business Outcomes
[Describe the successful outcomes and business value produced.]

## 3. Stakeholders
### Actors
- **[Actor Name]:** [Purpose/Responsibilities]

### Roles
- **[Role Name]:** [Purpose/Responsibilities/Interactions]

## 4. Business Capabilities
[List the enduring capabilities owned by this domain, matching Business Architecture.]

## 5. Core Business Activities
[List recurring business activities.]

## 6. Business Decisions
- **[Decision Name]:**
  - *Purpose:* 
  - *Decision Maker:* 
  - *Supporting Evidence:* 
  - *Governing Policies:* 
  - *Constraints:* 
  - *Preconditions:* 
  - *Alternative Outcomes:* 
  - *Escalation Conditions:* 
  - *Review Triggers:* 
  - *Appeal Mechanisms:* 
  - *Human Override:* 
  - *Uncertainty:* 

## 7. Information Requirements
[List conceptual information/knowledge consumed.]

## 8. Business Concepts
[List important concepts naturally used by practitioners.]

## 9. Business Relationships
[List conceptual relationships using natural language, e.g., A contains B.]

## 10. Business Events
[List meaningful business events.]

## 11. Knowledge Patterns
[Map recurring conceptual flow patterns.]

## 12. Policies
[Categorize applicable policies: Universal, Regional, Government, Donor, Organisation, Programme.]

## 13. Constraints
[List operational, ethical, legal, or financial constraints.]

## 14. Terminology
- **Preferred Terms:**
- **Synonyms:**
- **Ambiguous Terminology:**

## 15. Exceptions
[Describe edge cases and unusual business situations.]

## 16. Domain Dependencies
**Knowledge Consumed From:**
**Knowledge Produced For:**
**Business Dependencies:**

## 17. Business Tensions
[Identify competing forces the domain must balance, e.g., Speed vs. Accuracy.]

## 18. Discovery Evidence
### Established Facts
### Reasonable Assumptions
### Open Questions
### Knowledge Gaps

## 19. Ontology Readiness
[Identify stable conceptual clusters ready for future modeling.]

## 20. Domain Completion Assessment
[✅ READY FOR FREEZE / ❌ REQUIRES FURTHER DISCOVERY]
[Provide Justification]
```

---

## 5. Compliance Checklist
Before any Domain Discovery document is frozen, reviewers must confirm:
- [ ] **1. Completeness:** All 20 mandatory sections are present and populated.
- [ ] **2. Boundary Integrity:** The capabilities and responsibilities perfectly match `BUSINESS_ARCHITECTURE.md`.
- [ ] **3. Concept Purity:** The document contains NO references to databases, APIs, schemas, ER diagrams, classes, or RDF/OWL.
- [ ] **4. Stakeholder Clarity:** Actors (enduring) and Roles (transient) are explicitly separated.
- [ ] **5. Decision Depth:** Every major decision lists its evidence, policies, alternative outcomes, overrides, and escalation triggers.
- [ ] **6. Evidence Strictness:** Assumptions and Open Questions are clearly separated from Established Facts.
- [ ] **7. Tension Recognition:** The document accurately acknowledges at least one inherent business tension (Section 17) shaping the domain.
- [ ] **8. Classification Consistency:** Every concept in Section 8 has been classified against the rubric in §6 below, and the same concept is not classified differently in another domain.

---

## 6. Reality Knowledge / Operational Knowledge Rubric

*(Added under remediation B6. Constitution Article IV establishes the test; it did not establish how to apply it, and the seven original Stage 5 domains applied it inconsistently in at least six documented cases. This rubric makes the test reproducible so that two authors reach the same classification independently.)*

### 6.1 The test, restated

Constitution Article IV: a concept is **Reality Knowledge** if its omission would materially change the understanding of humanitarian reality, or the quality, safety, fairness, or appropriateness of a humanitarian decision. Otherwise it is **Operational Knowledge**, existing only because a particular organisation or application operates in a particular way.

### 6.2 Four ordered questions

Apply in order. The first question answered *yes* decides the classification.

1. **Would the concept still exist if every current organisation and software system disappeared, and humanitarian need continued?**
   Yes → **Reality Knowledge.** A household, a health condition, a kinship tie, a displacement event exist independently of anyone recording them.

2. **Does the concept determine, constrain, or justify who receives what assistance?**
   Yes → **Reality Knowledge**, even if it originates institutionally. An eligibility rule, a funding restriction, a recipient-category obligation and a consent authorization all originate in institutions, but their omission changes who receives aid — which is precisely what Article IV's "fairness or appropriateness of a humanitarian decision" clause covers.

3. **Does the concept carry an epistemic status — is it claimed, verified, uncertain, contested, or expired?**
   Yes → **Reality Knowledge.** Article III makes the warrant for a belief part of what must be understood before acting; a concept that carries warrant is part of the understanding, not part of the workflow.

4. **Otherwise → Operational Knowledge.** Queue states, routing rules, internal approval chains, notification settings, UI concepts, record-keeping artifacts, and roles that exist only to administer a process.

### 6.3 Boundary cases, decided

- **A role is Operational Knowledge; a relationship is Reality Knowledge.** *Head of Household* as an administrative designation is Operational; the underlying *responsibility for household decision-making* is Reality. *Registrar* is Operational; *Caregiver* is Reality, because caregiving persists whether or not anyone registers it.
- **An institutional artifact recording a real obligation is Reality Knowledge.** A *Grant* is not merely a record; it carries restrictions that determine eligibility (question 2).
- **A derived or computed value is neither until its basis is stated.** Where a concept is a score or ranking with no stated derivation, it is recorded as an open question rather than classified. Pillar P4 forbids unexplainable scores in any case.
- **When a concept passes question 1 in one aspect and question 4 in another, it is two concepts and must be split** (Rule AR-3, one concept one home). *Consent* splits this way: the person's act of authorising is Reality; the organisation's record of having captured it is Operational.

### 6.4 Standing obligation

A concept classified in one domain may not be classified differently in another. Where two domains disagree, the disagreement is escalated to `docs/03-cross-domain/CONCEPT_OWNERSHIP.md` §8 and resolved there, not settled locally.
