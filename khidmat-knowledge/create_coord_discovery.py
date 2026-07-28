import os

coord_dir = "docs/02-discovery/cross-organisational-coordination"
os.makedirs(coord_dir, exist_ok=True)

files = {}

files["README.md"] = """# Cross-Organisational Coordination Domain Knowledge Base
This directory contains the modular Discovery Knowledge Base for the Cross-Organisational Coordination domain.
"""

files["CROSS_ORGANISATIONAL_COORDINATION_DISCOVERY.md"] = """---
id: DOC-DISC-CROSS_ORGANISATIONAL_COORDINATION
title: CROSS-ORGANISATIONAL COORDINATION DOMAIN DISCOVERY (EXECUTIVE)
version: 1.0
status: Draft
owner: Discovery
---
# Cross-Organisational Coordination Domain Discovery (Executive Narrative)

The Cross-Organisational Coordination Domain exists to align independent humanitarian actors within a shared crisis context. It solves the profound problems of duplicated aid, fractured continuity of care, and systemic inefficiency that occur when hundreds of autonomous NGOs operate in the same geographic space without communicating.

Crucially, this domain operates entirely on *Context Sharing*, not *Control*. It does not exert command-and-control over another Organisation's internal operations. Instead, it securely facilitates the exchange of verified context, inter-agency referrals, and deduplication alerts, allowing autonomous actors to make informed, coordinated decisions.

Successful outcomes of this domain include preventing duplicate interventions, ensuring a beneficiary seamlessly transitions between specialized care providers (e.g., from an emergency medical NGO to a long-term shelter NGO), and fostering a landscape of verified organisational trust.

For authoritative business knowledge, concepts, rules, and events, refer to the modular artifacts within this Knowledge Base.
"""

files["01-domain-overview.md"] = """# Domain Overview: Cross-Organisational Coordination

## 1. Purpose
The domain exists to align interventions, share context, and deduplicate efforts across completely independent NGO boundaries. It ensures that the broader humanitarian response functions as a cohesive ecosystem rather than a chaotic collision of siloed operations.

## 2. Business Outcomes
- **Deduplication:** Prevention of the same individual receiving the exact same intervention from multiple agencies simultaneously.
- **Continuity of Care:** Seamless referral of an individual from one specialized NGO to another.
- **Shared Situational Awareness:** Aggregated visibility into which populations have received aid and which remain underserved.

## 4. Business Capabilities
- Inter-Agency Context Sharing & Consent Propagation
- Intervention Deduplication & Conflict Resolution
- External Referral Management
- Organisational Trust & Verification Brokering

## 5. Core Business Activities
- Alerting Partner Organisations when a beneficiary registers for conflicting aid.
- Brokering the transfer of verified case context during an external referral.
- Managing the revocation of beneficiary consent across a network of agencies.
- Establishing and verifying the operational mandate and trust level of partner NGOs.
"""

files["01b-stakeholders.md"] = """# 3. Stakeholders

## Actors (Enduring Participants)
- **Organisation (NGO/Agency):** An autonomous legal entity providing humanitarian aid.
- **Coordination Body (e.g., UN OCHA / Cluster Leads):** Enduring entities that facilitate macro-level sector coordination.
- **Individual / Household:** The human being whose context is being shared across boundaries.

## Roles (Transient Responsibilities)
- **Referral Focal Point:** The role within an Organisation responsible for receiving and dispatching external referrals.
- **Data Protection Officer (DPO):** The role responsible for authorizing the release of sensitive context across boundaries.
- **Cluster Coordinator:** The role responsible for guiding strategy among multiple Organisations operating in the same sector (e.g., the WASH Cluster).
"""

files["02-boundaries.md"] = """# 16. Domain Dependencies and Boundaries

## Owns
- The rules of inter-agency context sharing.
- External referral tracking and handshakes.
- Deduplication protocols and conflict resolution rules.
- Organisational trust modeling.

## Consumes
- **From Case Management:** Verified identity claims, Support Plans, and explicit beneficiary consent to share data.
- **From Programme Management:** Organisational mandates and geographic coverage areas.

## Produces
- **For Case Management:** Deduplication alerts (warning that a Support Plan conflicts with another agency), and incoming external referrals.
- **For Programme Management:** Gap analysis data (showing which geographies are over/under-served by the broader ecosystem).

## Explicitly Out of Scope
- Assessing the vulnerability of the individual (Case Management).
- Determining an Organisation's internal eligibility rules (Programme Management).
- Commanding another Organisation to cease an intervention. (Coordination can warn of duplication, but cannot command cessation).
"""

files["03-concepts.md"] = """# 8. Business Concepts

- External Referral
- Deduplication Alert
- Consent Propagation
- Partner Organisation
- Trust Level / Verification Status
- Shared Context / Encrypted Payload
- Coordination Cluster
- Sectoral Gap
"""

files["04-relationships.md"] = """# 9. Business Relationships

- An **External Referral** transfers a **Case Context** to a **Partner Organisation**.
- **Consent** authorizes the creation of **Shared Context**.
- A **Deduplication Alert** warns an **Organisation** of a conflict.
- An **Organisation** participates in a **Coordination Cluster**.
"""

files["04b-knowledge-patterns.md"] = """# 11. Knowledge Patterns

- **The Consent Chain:** Individual Consent -> authorizes -> Local Sharing -> which requires -> Partner Validation -> before yielding External Visibility. If consent is revoked at the root, the revocation must propagate across the entire chain.
- **Context Over Control:** Information is shared as an Alert or a Recommendation, never as an Execution Trigger across organisational boundaries.
"""

files["05-business-rules.md"] = """# 12. Policies and 13. Constraints

## Policies
- **Universal:** No sensitive beneficiary context can be shared outside the originating Organisation without explicit, informed, and documented consent.
- **Coordination:** Deduplication alerts must preserve privacy (e.g., verifying a cryptographic hash of an identity rather than broadcasting a name).
- **Organisation:** An Organisation will only accept external referrals from a Partner Organisation that meets their internal Data Protection and Safeguarding thresholds.

## Constraints
- **Legal/GDPR:** Cross-border data sharing faces massive legal friction.
- **Ethical:** Sharing context about highly persecuted minorities (e.g., ethnic refugees) with external actors carries extreme life-or-death risk.
- **Trust:** Organisations inherently distrust the verification standards of rival Organisations.
"""

files["05b-exceptions.md"] = """# 15. Exceptions

- **Emergency Life-Saving Override:** Sharing critical medical context with an external surgical NGO without documented consent if the individual is unconscious.
- **Mandatory Reporting Override:** Legally mandated sharing of safeguarding abuse context with a state authority, bypassing the consent requirement.
- **Trust Suspension:** Immediately cutting off all context sharing with a Partner Organisation if they suffer a severe data breach or safeguarding scandal.
"""

files["05c-business-tensions.md"] = """# 17. Business Tensions

The Coordination domain continuously balances competing operational forces:
- **Collaboration vs Competition:** The humanitarian ideal of sharing data freely versus the reality that NGOs compete for the same donor funding and often guard their beneficiary lists as proprietary assets.
- **Data Sharing vs Data Privacy:** The tension between sharing enough context to prevent duplicate aid versus minimizing data exposure to protect beneficiary lives.
- **Interoperability vs Sovereignty:** The desire for a unified, seamless humanitarian response versus the fierce independence and sovereign mandates of individual NGOs.
- **Speed of Referral vs Vetting Protocols:** The friction of urgently needing to refer a critical medical case versus the administrative delay of vetting a new Partner Organisation's data protection standards.
"""

files["06-business-events.md"] = """# 10. Business Events

- **External Referral Initiated:** An Organisation formally requests another to take over a case.
- **Referral Accepted / Declined:** The Partner Organisation formally responds to the request.
- **Deduplication Alert Triggered:** A conflict is detected between two Organisations trying to provide the exact same aid to the exact same person.
- **Consent Revoked:** A beneficiary formally withdraws permission to share their context externally.
- **Partner Vetted:** A new Organisation is formally trusted and added to the network.
"""

files["07-business-lifecycles.md"] = """# Business Lifecycles (Supporting Context)

## External Referral Lifecycle
1. **Initiation:** Originating NGO identifies an out-of-scope need and requests beneficiary consent.
2. **Brokering:** The context is securely packaged and offered to a Partner NGO.
3. **Assessment (Partner):** The Partner evaluates if they have the capacity and mandate to accept.
4. **Handshake:** The Partner formally accepts, and the Originator formally closes their intervention.
5. **Feedback Loop:** The Partner occasionally updates the Originator on macro-outcomes.
"""

files["08-decision-points.md"] = """# 6. Significant Business Decisions

## 1. External Referral Acceptance Decision
- **Purpose:** Determining whether a Partner Organisation will accept an incoming referral.
- **Decision Maker:** Referral Focal Point (at the receiving Partner Organisation).
- **Supporting Evidence:** The shared case context, internal capacity, internal eligibility rules.
- **Governing Policies:** Organisational mandate, Data Protection agreements.
- **Constraints:** Limited bed space in a hospital; restricted funding.
- **Preconditions:** Originating NGO must have obtained beneficiary consent.
- **Alternative Outcomes:** Accepted, Declined due to capacity, Declined due to eligibility.
- **Escalation Conditions:** Receiving NGO declines a life-or-death referral.
- **Review Triggers:** Originating NGO disputes a rejection based on eligibility.
- **Appeal Mechanisms:** Originator can escalate to a Cluster Coordinator to mediate.
- **Human Override:** Executive decision to accept an out-of-mandate referral for humanitarian necessity.
- **Uncertainty:** The receiving NGO must trust that the originating NGO's initial assessment was accurate.

## 2. Deduplication Conflict Resolution Decision
- **Purpose:** Determining which NGO will proceed with an intervention when a duplication alert fires.
- **Decision Maker:** Programme Managers from both conflicting NGOs.
- **Supporting Evidence:** Registration timestamps, geographic proximity, beneficiary preference.
- **Governing Policies:** Cluster deduplication protocols (e.g., "First to register takes the case").
- **Constraints:** Neither NGO has formal command authority over the other.
- **Preconditions:** A cryptographic or administrative match alerts both parties.
- **Alternative Outcomes:** NGO A withdraws, NGO B withdraws, Both proceed (wasting resources), Both withdraw (harming the beneficiary).
- **Escalation Conditions:** NGOs refuse to compromise and begin a territorial dispute.
- **Review Triggers:** Monthly cluster coordination meetings.
- **Appeal Mechanisms:** Escalation to the overarching UN Cluster Lead.
- **Human Override:** Beneficiary explicitly demands aid from NGO A and rejects NGO B.
- **Uncertainty:** The cryptographic match might be a false positive (two different people with identical names/birthdates).

## 3. Organisational Trust Authorization Decision
- **Purpose:** Deciding whether to legally and technically permit context sharing with a new NGO.
- **Decision Maker:** Data Protection Officer / Country Director.
- **Supporting Evidence:** Security audits, legal MOUs, past collaboration history.
- **Governing Policies:** GDPR, National intelligence laws, Organisational risk appetite.
- **Constraints:** High legal liability for data breaches.
- **Preconditions:** Both NGOs sign an Information Sharing Protocol (ISP).
- **Alternative Outcomes:** Authorized, Rejected, Conditionally Authorized (restricted data only).
- **Escalation Conditions:** Critical need to share data with a high-risk local partner who fails the security audit.
- **Review Triggers:** Annual ISP renewal, or a reported data breach.
- **Appeal Mechanisms:** None; risk aversion usually prevails.
- **Human Override:** Emergency waiver signed by Country Director assuming full legal liability.
- **Uncertainty:** Impossible to continuously verify the internal data hygiene of the partner.
"""

files["09-information-requirements.md"] = """# 7. Information Requirements

- **Consent Proof:** Immutable evidence that the individual agreed to the sharing.
- **Encrypted Context:** The actual vulnerability or identity data, shared strictly on a need-to-know basis.
- **Organisational Mandates:** Who is doing what, and where (the "4W" matrix: Who does What, Where, and When).
- **Trust Topologies:** Which organisations are legally permitted to share with which other organisations.
"""

files["10-open-questions.md"] = """# 18. Open Questions (Moved from Evidence)

- How does the domain guarantee that a "Consent Revoked" event successfully forces a Partner NGO to delete data they already ingested?
- In the absence of a central authority, how is a Deduplication Conflict structurally resolved if both NGOs adamantly refuse to withdraw?
- How is organisational trust established with informal, community-led grassroots organizations that lack formal legal registration?
"""

files["11-evidence.md"] = """# 18. Discovery Evidence

## Established Facts
- Independent NGOs have sovereign authority over their own operations; no NGO can command another to stop an intervention.
- The fundamental barrier to coordination is not technology, but Organisational Trust and competition for donor funding.
- Beneficiary consent is the absolute legal boundary for sharing sensitive context.

## Reasonable Assumptions
- False positives will occur during deduplication due to poor data quality in crisis zones.
- NGOs will frequently attempt to hoard beneficiary data rather than share it freely.

## Open Questions
Refer to 10-open-questions.md

## Knowledge Gaps
- The specific legal mechanisms required to share data across borders when the host government actively demands access to that data.
"""

files["12-domain-invariants.md"] = """# Domain Invariants (Supporting Context)

- **Context over Control:** Coordination shares awareness, never execution authority.
- **The Sovereign Boundary:** An NGO's internal assessment and decision-making apparatus cannot be overridden by an external coordinating body.
- **Consent is King:** No external sharing occurs without the explicitly documented consent of the individual (barring immediate life-saving exceptions).
"""

files["13-business-language.md"] = """# 14. Terminology

## Preferred Terms
- **External Referral:** Sending a case to a completely different legal entity.
- **Deduplication:** The act of preventing duplicate interventions.
- **Partner Organisation:** A vetted, trusted external entity.

## Synonyms
- **Coordination Body / Cluster:** UN-led sector groups (e.g., WASH Cluster, Protection Cluster).
- **4W:** Who does What, Where, and When (standard coordination matrix).

## Ambiguous Terminology
- **Referral:** Can mean an *Internal* Referral (Case Worker to Protection Officer within the same NGO) or an *External* Referral. In this domain, it strictly means External.
- **Sharing:** Can imply sending raw data (violating privacy) or sending encrypted cryptographic proofs (preserving privacy).
"""

files["14-ontology-readiness.md"] = """# 19. Ontology Readiness

The following conceptual clusters appear highly stable and ready for subsequent formal Ontology Design (Stage 6):
- **The Trust Edge:** The structural relationship representing Information Sharing Protocol between Organisation A and Organisation B.
- **The Consent Chain:** The propagation of Consent authorizing the creation of Shared Context.
- **The Deduplication Conflict:** A conceptual entity representing the collision of two overlapping Support Plans requiring Resolution.

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
    filepath = os.path.join(coord_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
print("Cross-Organisational Coordination files created successfully to meet the 20-point standard.")
