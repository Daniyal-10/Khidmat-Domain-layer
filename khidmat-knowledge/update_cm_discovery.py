import os

cm_dir = "docs/02-discovery/case-management"

# 1. Update 01-domain-overview.md to include Business Outcomes, Capabilities, Activities
with open(os.path.join(cm_dir, "01-domain-overview.md"), "r", encoding="utf-8") as f:
    overview_content = f.read()

if "## Business Outcomes" not in overview_content:
    overview_content += "\n## Business Outcomes\n- Verified understanding of an individual's context.\n- Justified recommendations matching verified needs to available resources.\n- Continuity of care adapting to the individual's changing situation.\n"
    overview_content += "\n## Business Capabilities\n- Evidence & Knowledge Acquisition\n- Understanding Formation\n- Reasoning & Justified Recommendation\n- Verification\n- Continuity & Re-assessment\n"
    overview_content += "\n## Core Business Activities\n- Registering individuals.\n- Capturing claims and consent.\n- Synthesizing field observations and evidence.\n- Developing support plans.\n- Monitoring individual recovery and vulnerability over time.\n"
    with open(os.path.join(cm_dir, "01-domain-overview.md"), "w", encoding="utf-8") as f:
        f.write(overview_content)

# 2. Create Stakeholders
stakeholders_content = """# Stakeholders

## Actors (Enduring Participants)
- **Individual:** The human being affected by a crisis.
- **Household:** The enduring family or social unit.
- **Caregiver / Guardian:** A person legally or informally responsible for another individual (e.g., a minor).
- **Organisation:** The NGO or entity providing aid.

## Roles (Transient Responsibilities)
- **Beneficiary / Registrant:** The administrative status of an Individual actively interacting with a Case.
- **Case Worker:** The frontline humanitarian responsible for intake, assessment, and recommendation.
- **Approver / Protection Officer:** The senior humanitarian responsible for authorizing Support Plans and handling escalations.
"""
with open(os.path.join(cm_dir, "01b-stakeholders.md"), "w", encoding="utf-8") as f:
    f.write(stakeholders_content)

# 3. Create Knowledge Patterns
kp_content = """# Knowledge Patterns
- **The Epistemic Justification Loop:** Claim -> requires -> Evidence -> supports -> Decision -> produces -> Support Plan.
- **The Verification Barrier:** Unverified Claim cannot cross the boundary to Execution Trigger without formal Verification.
- **Household Fluidity:** Individuals merge into and split from Households dynamically based on conflict, displacement, and reunification.
"""
with open(os.path.join(cm_dir, "04b-knowledge-patterns.md"), "w", encoding="utf-8") as f:
    f.write(kp_content)

# 4. Create Exceptions
exc_content = """# Exceptions
- **Emergency Necessity / Consent Deferral:** Action may proceed without explicit, documented consent if doing so is required to preserve life or immediate safety (with consent deferred until stability allows).
- **Verification Impossibility:** In acute crisis, formal evidence may be impossible to gather, relying entirely on community validation or assumed truth.
- **Household Splitting:** A household may dynamically fracture during a crisis, requiring cases to split and merge context on the fly.
"""
with open(os.path.join(cm_dir, "05b-exceptions.md"), "w", encoding="utf-8") as f:
    f.write(exc_content)

# 5. Create Business Tensions
tens_content = """# Business Tensions
The Case Management domain continuously balances competing operational forces:
- **Rapid Response vs Evidence Verification:** The ethical pressure to provide immediate life-saving aid versus the operational mandate to rigorously verify identity and need.
- **Individual Need vs Programme Constraints:** The tension a case worker faces when an individual's verified, desperate need falls outside the rigid eligibility criteria established by Programme Management.
- **Human Judgement vs Standardised Policy:** The friction between applying a uniform rule equitably across thousands of cases versus making subjective, compassionate exceptions for highly nuanced edge cases.
- **Privacy vs Information Sharing:** The mandate to protect an individual's sensitive data versus the necessity to share their information across organisations to ensure continuity of care and prevent duplication.
- **Community Validation vs Documentary Evidence:** The conflict between trusting informal community knowledge (which is rapid and culturally grounded) and requiring formal documentation (which is slow, restrictive, but auditable).
"""
with open(os.path.join(cm_dir, "05c-business-tensions.md"), "w", encoding="utf-8") as f:
    f.write(tens_content)

# 6. Update Decision Points
decisions_content = """# Significant Business Decisions

## 1. Eligibility Decision
- **Purpose:** Determining if an individual's verified needs meet the criteria for a specific intervention.
- **Decision Maker:** Approver (Final Decision), with Case Worker (Recommendation).
- **Supporting Evidence:** Verified claims, field observations, vulnerability indicators.
- **Governing Policies:** Programme eligibility criteria.
- **Constraints:** Finite budgets, strict donor rules.
- **Preconditions:** Individual must be identified; consent must be granted.
- **Alternative Outcomes:** Approved, Rejected, Waitlisted, Escalated.
- **Escalation Conditions:** Individual has extreme vulnerability but technically fails eligibility rule.
- **Review Triggers:** Appeal filed by beneficiary, or audit flag.
- **Appeal Mechanisms:** Beneficiary can submit grievance to Accountability domain.
- **Human Override:** Protection Officer can grant a 'Policy Waiver' for life-saving necessity.
- **Uncertainty:** May rely on unverified community assertions in acute crisis.

## 2. Reassessment Decision
- **Purpose:** Determining if a case needs to be reopened, escalated, or closed based on new information.
- **Decision Maker:** Case Worker.
- **Supporting Evidence:** Fulfillment loops, new claims, changing context, follow-up observations.
- **Governing Policies:** Reassessment frequency policies.
- **Constraints:** Heavy caseloads limiting face-to-face time.
- **Preconditions:** Active or previously closed case exists.
- **Alternative Outcomes:** Interventions added, Suspended, or Case Closed.
- **Escalation Conditions:** Discovery of severe safeguarding abuse during follow-up.
- **Review Triggers:** Automatic time-lapse (e.g., 6 months post-distribution).
- **Appeal Mechanisms:** None required for internal reassessment unless it removes aid.
- **Human Override:** Mandatory human judgment on whether recovery is genuine.
- **Uncertainty:** Beneficiary may hide recovery to maintain aid flow.

## 3. Referral Decision
- **Purpose:** Determining if a need should be transferred to an external Partner Organisation.
- **Decision Maker:** Case Worker or Protection Officer.
- **Supporting Evidence:** Needs assessment identifying out-of-scope vulnerabilities.
- **Governing Policies:** Information sharing agreements; GDPR/Data privacy.
- **Constraints:** Lack of secure interoperable data sharing channels.
- **Preconditions:** Explicit beneficiary consent for data sharing.
- **Alternative Outcomes:** Referred, Declined by partner, Cannot refer due to lack of partners.
- **Escalation Conditions:** Partner refuses critical medical referral.
- **Review Triggers:** SLA timeouts (partner hasn't responded in 48 hours).
- **Appeal Mechanisms:** Beneficiary can refuse referral.
- **Human Override:** Life-or-death situations may force immediate physical transfer without formal digital referral.
- **Uncertainty:** Lack of visibility into partner's capacity to accept the referral.

## 4. Safeguarding Escalation Decision
- **Purpose:** Determining if immediate intervention is required to protect a vulnerable individual from harm.
- **Decision Maker:** Protection Officer or Senior Case Worker.
- **Supporting Evidence:** Direct observation, community reports, safeguarding flags.
- **Governing Policies:** Child protection laws, Gender-Based Violence (GBV) protocols.
- **Constraints:** Severe legal and physical security risks to both staff and beneficiary.
- **Preconditions:** Suspicion of abuse or severe exploitation.
- **Alternative Outcomes:** Immediate extraction, Police referral, Silent monitoring.
- **Escalation Conditions:** Abuser is a humanitarian staff member or local authority.
- **Review Triggers:** Automatic independent review within 24 hours.
- **Appeal Mechanisms:** Strictly regulated legal appeals.
- **Human Override:** Standard programme rules are entirely bypassed.
- **Uncertainty:** High ambiguity; victims often deny abuse due to fear.
"""
with open(os.path.join(cm_dir, "08-decision-points.md"), "w", encoding="utf-8") as f:
    f.write(decisions_content)

# 7. Update Evidence
evidence_content = """# Supporting Evidence

## Established Facts
- The domain operates a non-linear, looping lifecycle (Assessment -> Planning -> Implementation -> Monitoring -> Reassessment).
- There is a strict structural separation between a person's administrative status (Engagement Stage) and their actual recovery (Human Development Stage).
- Case Management consumes rules from Programme Management and triggers execution in Resource & Logistics.

## Reasonable Assumptions
- Case workers will face pressure to bypass strict verification in favor of speed during acute crises.
- Different organisations will have differing definitions of what constitutes acceptable "Evidence."

## Open Questions (Moved to 10-open-questions.md)
Refer to 10-open-questions.md

## Knowledge Gaps
- How are conflicting evidence sources reconciled in practice when community validation contradicts documentary proof?
- How is uncertainty formally represented when an assessor suspects a vulnerability but lacks hard evidence?
"""
with open(os.path.join(cm_dir, "11-evidence.md"), "w", encoding="utf-8") as f:
    f.write(evidence_content)

# 8. Create Ontology Readiness
onto_content = """# Ontology Readiness

The following conceptual clusters appear highly stable and ready for subsequent formal Ontology Design (Stage 6):
- **Actor/Role Separation:** The distinction between an enduring Individual and their transient Beneficiary role.
- **Epistemic Model:** The separation of Claim from Evidence, and the process of Verification.
- **Dual Lifecycles:** The structural separation of Engagement Stage and Human Development Stage.
- **Service Handoffs:** The conceptual boundary between Support Plan (the knowledge decision) and its execution.

These concepts can be modelled without requiring implementation assumptions.
"""
with open(os.path.join(cm_dir, "14-ontology-readiness.md"), "w", encoding="utf-8") as f:
    f.write(onto_content)

print("Case Management files updated successfully to meet the 20-point standard.")
