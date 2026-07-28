import os

ae_dir = "docs/02-discovery/accountability-evaluation"
os.makedirs(ae_dir, exist_ok=True)

files = {}

files["README.md"] = """# Accountability and Evaluation Domain Knowledge Base
This directory contains the modular Discovery Knowledge Base for the Accountability and Evaluation domain.
"""

files["ACCOUNTABILITY_EVALUATION_DISCOVERY.md"] = """---
id: DOC-DISC-ACCOUNTABILITY_EVALUATION
title: ACCOUNTABILITY & EVALUATION DOMAIN DISCOVERY (EXECUTIVE)
version: 1.0
status: Draft
owner: Discovery
---
# Accountability and Evaluation Domain Discovery (Executive Narrative)

The Accountability and Evaluation Domain exists to provide independent, objective oversight of the humanitarian response. It answers the fundamental question: *Did our interventions actually work, and are we doing harm?*

It operates entirely outside the command structures of Case Management and Programme Management to prevent conflicts of interest. The domain manages macro-level Monitoring, Evaluation, Accountability, and Learning (MEAL) as well as the micro-level Complaints and Feedback Mechanism (CFM). 

Successful outcomes of this domain include systemic learning that forces Programme Management to adapt failing strategies, and the safe, impartial resolution of beneficiary grievances.

For authoritative business knowledge, concepts, rules, and events, refer to the modular artifacts within this Knowledge Base.
"""

files["01-domain-overview.md"] = """# Domain Overview: Accountability and Evaluation

## 1. Purpose
The domain exists to provide independent measurement of humanitarian impact and an impartial channel for beneficiary grievances. It cannot be owned by Case Management or Programme Management because those who design or execute aid cannot objectively evaluate their own success or investigate complaints against themselves.

## 2. Business Outcomes
- Objective measurement of long-term programmatic impact.
- Safe, impartial resolution of beneficiary complaints and grievances.
- Systemic learning that forces structural adaptation in Programme Management.

## 4. Business Capabilities
- Impact Evaluation & Learning (MEAL)
- Complaints and Feedback Management (CFM)
- Independent Post-Distribution Monitoring (PDM)
- Quality and Compliance Auditing

## 5. Core Business Activities
- Conducting surveys and focus groups with beneficiaries after aid delivery.
- Receiving, triaging, and investigating complaints through hotlines or community desks.
- Publishing evaluation reports on programme efficacy.
- Escalating severe safeguarding or fraud allegations to independent authorities.
"""

files["01b-stakeholders.md"] = """# 3. Stakeholders

## Actors (Enduring Participants)
- **Individual:** The human being providing feedback or being evaluated.
- **Community:** The collective social unit impacted by a programme.
- **External Auditor:** Third-party entity providing independent verification.

## Roles (Transient Responsibilities)
- **MEAL Officer:** Role responsible for conducting impact assessments and PDM.
- **CFM Operator:** Role receiving initial complaints (e.g., hotline worker).
- **Grievance Investigator:** Role responsible for investigating serious complaints of fraud or abuse.
- **Complainant:** An Individual actively raising a grievance.
"""

files["02-boundaries.md"] = """# 16. Domain Dependencies and Boundaries

## Owns
- Complaints and Feedback Mechanism (CFM).
- Post-Distribution Monitoring (PDM).
- Programme impact evaluation.

## Consumes
- **From Case Management:** Closed cases (as subjects for evaluation).
- **From Programme Management:** Programme objectives and logical frameworks (to know what to measure).
- **From Resource & Logistics:** Dispatch records (to verify if aid actually arrived).

## Produces
- **For Programme Management:** Impact reports, systemic learning, and adaptation mandates.
- **For Case Management:** Grievance resolutions (e.g., forcing a case to be reopened).

## Explicitly Out of Scope
- Assessing individual vulnerability to determine aid eligibility (Case Management).
- Modifying programme budgets based on learning (Programme Management).
- Investigating criminal activity (Law Enforcement).
"""

files["03-concepts.md"] = """# 8. Business Concepts

- Grievance / Complaint
- Feedback
- Post-Distribution Monitoring (PDM)
- Impact Evaluation
- Indicator
- Logical Framework (Logframe)
- Baseline / Endline
- Triaging
- Systemic Learning
"""

files["04-relationships.md"] = """# 9. Business Relationships

- An **Impact Evaluation** measures a **Programme**.
- A **Grievance** is raised by a **Complainant**.
- A **PDM** verifies a **Fulfillment**.
- A **Baseline** is compared against an **Endline**.
- **Systemic Learning** mandates a change to an **Intervention Catalogue**.
"""

files["04b-knowledge-patterns.md"] = """# 11. Knowledge Patterns

- **The Objective Distance Pattern:** Evaluator must have zero operational authority over Executor. To maintain truth, the entity measuring success must not be the entity responsible for achieving it.
- **The Feedback Loop:** Observation -> generates -> Learning -> forces -> Adaptation (in Programme Management).
"""

files["05-business-rules.md"] = """# 12. Policies and 13. Constraints

## Policies
- **Universal:** Beneficiaries have an absolute right to complain without fear of retribution or loss of aid.
- **Donor:** Programmes over a certain financial threshold require mandatory independent endline evaluations.
- **Organisation:** Severe allegations (fraud, sexual exploitation) must bypass standard local management and go directly to HQ.

## Constraints
- **Cultural:** In many contexts, beneficiaries are culturally discouraged from criticizing authority figures, severely suppressing feedback.
- **Security:** In conflict zones, investigating a complaint of aid diversion by local armed groups puts the investigator at extreme physical risk.
- **Ethical:** PDM surveys extract data from traumatized individuals; there is an ethical constraint against over-surveying ("assessment fatigue").
"""

files["05b-exceptions.md"] = """# 15. Exceptions

- **Anonymous Whistleblowing:** Grievances submitted without any identity attached, making standard investigation impossible but still requiring systemic risk logging.
- **Malicious Complaints:** Coordinated false grievances designed to sabotage a specific case worker or vendor.
- **Immediate Safeguarding Override:** If a CFM operator receives a complaint indicating active, ongoing harm (e.g., abuse), standard triaging is bypassed for an immediate physical intervention by Case Management Protection Officers.
"""

files["05c-business-tensions.md"] = """# 17. Business Tensions

- **Independence vs Relevancy:** The tension between remaining completely separate from operations to maintain objectivity, versus being so detached that evaluation reports are ignored by operational teams.
- **Accountability vs Assessment Fatigue:** The ethical mandate to gather feedback versus the reality of repeatedly interrogating traumatized people who just want to be left alone.
- **Quantitative Metrics vs Qualitative Reality:** The donor pressure to provide neat, numerical impact statistics versus the complex, unquantifiable reality of human recovery.
"""

files["06-business-events.md"] = """# 10. Business Events

- **Complaint Received:** A grievance enters the CFM.
- **Complaint Escalated:** A grievance is flagged as severe (fraud/abuse).
- **Complaint Resolved:** The grievance is formally closed with the complainant.
- **Evaluation Initiated:** A formal study of a programme begins.
- **Learning Published:** A verified insight is formally handed to Programme Management.
"""

files["07-business-lifecycles.md"] = """# Business Lifecycles (Supporting Context)

## CFM Lifecycle
1. Intake (Receipt of complaint)
2. Triage (Categorization by severity)
3. Investigation (Fact-finding)
4. Resolution (Decision and action)
5. Feedback (Closing the loop with the complainant)

## Evaluation Lifecycle
1. Baseline (Measurement before intervention)
2. PDM (Monitoring immediately after distribution)
3. Endline (Measurement at the end of the programme)
4. Impact Assessment (Long-term measurement years later)
"""

files["08-decision-points.md"] = """# 6. Significant Business Decisions

## 1. Grievance Triage Decision
- **Purpose:** Categorize a complaint to determine the speed and seniority of the investigation.
- **Decision Maker:** CFM Operator / MEAL Manager.
- **Supporting Evidence:** Initial claim, tone, supporting artifacts.
- **Governing Policies:** Organisational CFM escalation matrix.
- **Constraints:** Limited initial information; often anonymous.
- **Preconditions:** Complaint must be received.
- **Alternative Outcomes:** Standard (Service issue), High (Fraud), Critical (Safeguarding/Abuse).
- **Escalation Conditions:** Allegation involves senior management.
- **Review Triggers:** Routine audit of triaged complaints.
- **Appeal Mechanisms:** None at triage stage.
- **Human Override:** Operator intuition that a "minor" complaint is masking severe abuse.
- **Uncertainty:** High ambiguity; complainants often downplay severity initially.

## 2. Grievance Resolution Decision
- **Purpose:** Determining if a complaint is valid and what action to mandate.
- **Decision Maker:** Grievance Investigator.
- **Supporting Evidence:** Interviews, distribution logs, Case Management records.
- **Governing Policies:** Legal standards, Code of Conduct.
- **Constraints:** Lack of subpoena power; relies on voluntary cooperation.
- **Preconditions:** Investigation phase completed.
- **Alternative Outcomes:** Upheld (Action mandated), Dismissed (Unfounded), Inconclusive.
- **Escalation Conditions:** Resolution requires firing staff or canceling a vendor contract.
- **Review Triggers:** Complainant dissatisfaction.
- **Appeal Mechanisms:** Complainant can appeal to an independent ombudsman.
- **Human Override:** Executive board can overrule a dismissal.
- **Uncertainty:** Often a "he said, she said" scenario with no hard proof.

## 3. Impact Conclusion Decision
- **Purpose:** Formally declaring whether a Programme achieved its intended outcomes.
- **Decision Maker:** External Auditor / Senior MEAL Officer.
- **Supporting Evidence:** Baseline/Endline datasets, PDM surveys.
- **Governing Policies:** Donor logical framework agreements.
- **Constraints:** Difficult to prove causality (did *we* cause the improvement, or did the economy recover?).
- **Preconditions:** Programme is complete.
- **Alternative Outcomes:** Successful, Partially Successful, Failed.
- **Escalation Conditions:** Report shows the programme caused active harm to the community.
- **Review Triggers:** Donor dispute of findings.
- **Appeal Mechanisms:** Programme Management can formally respond to dispute findings.
- **Human Override:** None; independence must be maintained.
- **Uncertainty:** High statistical margins of error in conflict zones.
"""

files["09-information-requirements.md"] = """# 7. Information Requirements

- **Operational Data:** Who received what, when, and where (from Case Management and Logistics).
- **Strategic Data:** What the programme was supposed to achieve (from Programme Management).
- **Beneficiary Contact Data:** Secure channels to reach individuals for surveys or feedback without compromising their safety.
"""

files["10-open-questions.md"] = """# 18. Open Questions (Moved from Evidence)

- How does the domain structurally mandate Programme Management to adopt a "Learning" if Programme Management refuses?
- How are complaints tracked and deduplicated when a beneficiary submits the same grievance through 4 different channels anonymously?
- How does PDM data flow back into active Case Management if an evaluator discovers a beneficiary is starving despite being marked "Resilient"?
"""

files["11-evidence.md"] = """# 18. Discovery Evidence

## Established Facts
- The entity measuring success must be structurally independent from the entity executing the work.
- Beneficiaries routinely suppress complaints due to fear of losing future aid.
- MEAL data is heavily reliant on Case Management and Logistics records for its foundational truth.

## Reasonable Assumptions
- Malicious complaints against vendors or staff will occur and require investigation.
- Programme Management will resist negative evaluations, necessitating a formal "management response" mechanism.

## Open Questions
Refer to 10-open-questions.md

## Knowledge Gaps
- The exact mathematical thresholds used to determine if an evaluation sample size is statistically significant in a highly fluid displaced population.
"""

files["12-domain-invariants.md"] = """# Domain Invariants (Supporting Context)

- **The Principle of Independence:** Accountability mechanisms cannot be subordinate to operational management. A CFM operator cannot report to a Programme Manager.
- **The Right to Complain:** Every individual has an irrevocable right to provide feedback on the assistance they receive.
- **Do No Harm (Data Protection):** The act of investigating a complaint must never put the complainant at greater risk of harm or retaliation.
"""

files["13-business-language.md"] = """# 14. Terminology

## Preferred Terms
- **Grievance:** A formal complaint requiring investigation and resolution.
- **Feedback:** General commentary (positive or negative) that does not require a formal investigation.
- **Endline:** The final measurement of vulnerability at the close of a programme.

## Synonyms
- **MEAL:** Monitoring, Evaluation, Accountability, and Learning.
- **CFM / AAP:** Complaints and Feedback Mechanism / Accountability to Affected Populations (used interchangeably depending on the donor).

## Ambiguous Terminology
- **Monitoring:** Can mean tracking a single beneficiary's health (Case Management) or tracking the overall statistical progress of a programme (Accountability).
"""

files["14-ontology-readiness.md"] = """# 19. Ontology Readiness

The following conceptual clusters appear highly stable and ready for subsequent formal Ontology Design (Stage 6):
- **The Grievance Entity:** The structure of a Complaint, its Severity Level, and its Resolution Status.
- **The Measurement Model:** The relationship between a Logical Framework, an Indicator, a Baseline, and an Endline.
- **The Independence Boundary:** The structural separation ensuring Accountability Roles do not intersect with Execution Roles.

These concepts can be modelled without requiring implementation assumptions.
"""

files["STATUS.md"] = """# 20. Domain Completion Assessment

`
Overview: Complete
Boundaries: Complete
Concepts: Complete
Relationships: Complete
Business Rules: Complete
Events: Complete
Lifecycles: Complete
Decision Points: Complete
Information Requirements: Complete
Open Questions: 3 identified
Evidence: Complete
Domain Invariants: Complete
Business Language: Complete
Client Validation: Pending
Overall Discovery Maturity: READY FOR FREEZE
`
"""

for filename, content in files.items():
    filepath = os.path.join(ae_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
print("Accountability and Evaluation files created successfully to meet the 20-point standard.")
