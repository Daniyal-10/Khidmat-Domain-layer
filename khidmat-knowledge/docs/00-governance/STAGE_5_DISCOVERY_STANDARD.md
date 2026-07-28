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
