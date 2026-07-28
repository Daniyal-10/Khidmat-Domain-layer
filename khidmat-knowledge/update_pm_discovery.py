import os

pm_dir = "docs/02-discovery/programme-management"

# 1. Update 01-domain-overview.md to include Business Outcomes, Capabilities, Activities
with open(os.path.join(pm_dir, "01-domain-overview.md"), "r", encoding="utf-8") as f:
    overview_content = f.read()

if "## Business Outcomes" not in overview_content:
    overview_content += "\n## Business Outcomes\n- Strategic alignment of funding to verified population needs.\n- Optimal resource efficacy across competing crises.\n- Governed execution via actionable eligibility rules and intervention catalogues.\n"
    overview_content += "\n## Business Capabilities\n- Programme Design & Strategy Formulation\n- Intervention Catalogue Management\n- Eligibility Policy Definition\n- Resource Prioritisation & Allocation\n- Strategic Monitoring & Adaptation\n"
    overview_content += "\n## Core Business Activities\n- Analyzing macro-level population vulnerability assessments.\n- Drafting and approving overarching programme mandates.\n- Allocating finite budgets across diverse intervention categories.\n- Defining the precise technical rules for who qualifies for aid.\n- Continuously adjusting rules and budgets based on burn rates and shifting ground realities.\n"
    with open(os.path.join(pm_dir, "01-domain-overview.md"), "w", encoding="utf-8") as f:
        f.write(overview_content)

# 2. Create Stakeholders
stakeholders_content = """# Stakeholders

## Actors (Enduring Participants)
- **Donor / Funder:** The external entity providing the financial resources.
- **Organisation / NGO:** The entity legally bound to deliver the programme.
- **Government Authority:** The host country or regional entity imposing regulatory constraints on aid.

## Roles (Transient Responsibilities)
- **Programme Director / Head of Programmes:** The senior role responsible for macro-level strategy and donor negotiations.
- **Programme Manager:** The role responsible for the design, budgeting, and execution of a specific programme.
- **Technical Advisor (Sector Lead):** The specialist who designs the specific interventions (e.g., a WASH expert designing water interventions).
- **Budget Holder:** The role with financial authority to approve reallocations.
"""
with open(os.path.join(pm_dir, "01b-stakeholders.md"), "w", encoding="utf-8") as f:
    f.write(stakeholders_content)

# 3. Create Knowledge Patterns
kp_content = """# Knowledge Patterns
- **The Hierarchical Constraint Pattern:** Donor Mandate constrains -> Programme constrains -> Intervention Catalogue constrains -> Intervention Offering constrains -> Eligibility Rule.
- **The Fungibility Boundary:** Restricted Funding cannot be diverted to a different Sector or Target Population without a formal Grant Amendment (unlike unrestricted funding which is highly fungible).
"""
with open(os.path.join(pm_dir, "04b-knowledge-patterns.md"), "w", encoding="utf-8") as f:
    f.write(kp_content)

# 4. Create Exceptions
exc_content = """# Exceptions
- **Emergency Reallocation (Crisis Modifier):** Re-routing restricted funds to an acute, unforeseen crisis (e.g., an earthquake strikes a conflict zone) prior to formal donor approval.
- **Rapid Scale-Up:** Exponentially increasing budgets and relaxing strict eligibility constraints overnight in response to mass displacement or epidemic outbreak.
- **Programme Merger:** Combining two overlapping programmatic silos to reduce administrative overhead and streamline field operations.
"""
with open(os.path.join(pm_dir, "05b-exceptions.md"), "w", encoding="utf-8") as f:
    f.write(exc_content)

# 5. Create Business Tensions
tens_content = """# Business Tensions
The Programme Management domain continuously balances competing strategic forces:
- **Equity vs Budget Constraints:** The tension between designing broad eligibility rules to help the maximum number of people versus narrow rules to ensure finite budgets aren't immediately exhausted.
- **Strategic Planning vs Emergency Adaptation:** The conflict between maintaining long-term, carefully budgeted resilience goals and repeatedly diverting resources to respond to sudden, acute crises.
- **Donor Restrictions vs Humanitarian Need:** The friction caused when funding is legally restricted to a specific sector or geography, while emergent field assessments reveal a desperate need elsewhere.
- **Coverage vs Depth of Assistance:** The mathematical trade-off between providing meaningful, transformative assistance to a few versus shallow, temporary relief to many.
- **Evidence-Based Planning vs Time Pressure:** The operational reality of needing to define budgets, rules, and intervention catalogues immediately, often before reliable population-level data can be fully gathered and analyzed.
"""
with open(os.path.join(pm_dir, "05c-business-tensions.md"), "w", encoding="utf-8") as f:
    f.write(tens_content)

# 6. Update Decision Points
decisions_content = """# Significant Business Decisions

## 1. Programme Initiation Decision
- **Purpose:** Determining if a new programme should be created.
- **Decision Maker:** Programme Director.
- **Supporting Evidence:** Population assessments, donor calls for proposals, strategic objectives.
- **Governing Policies:** Organisational mandate, Government response plans.
- **Constraints:** Overall organisational capacity, availability of donor funding.
- **Preconditions:** Identified systemic vulnerability at a population scale.
- **Alternative Outcomes:** Approved, Deferred, Rejected.
- **Escalation Conditions:** Critical unmet need but no available donor funding.
- **Review Triggers:** End of strategic cycle or sudden onset crisis.
- **Appeal Mechanisms:** Communities may lobby via civil society.
- **Human Override:** Executive decision to use unrestricted reserves to launch a programme immediately.
- **Uncertainty:** Long-term funding continuity is often highly uncertain.

## 2. Intervention Inclusion Decision
- **Purpose:** Determining which specific interventions belong in the catalogue.
- **Decision Maker:** Technical Advisor / Programme Manager.
- **Supporting Evidence:** Needs assessments, cost-benefit analyses, market feasibility from Logistics.
- **Governing Policies:** Humanitarian standards (Sphere), National technical standards.
- **Constraints:** Resource availability, logistical viability (e.g., cold chain).
- **Preconditions:** Intervention must align with the Programme mandate.
- **Alternative Outcomes:** Included, Excluded, Modified (e.g., Cash instead of In-Kind).
- **Escalation Conditions:** A critical life-saving intervention is deemed too expensive.
- **Review Triggers:** Post-distribution monitoring shows poor intervention efficacy.
- **Appeal Mechanisms:** Field staff (Case Management) can request additions.
- **Human Override:** Rapid inclusion during acute crisis without full feasibility study.
- **Uncertainty:** Whether the local market can actually absorb cash at scale.

## 3. Eligibility Rule Definition Decision
- **Purpose:** Setting the strict criteria for receiving an intervention.
- **Decision Maker:** Programme Manager.
- **Supporting Evidence:** Vulnerability criteria, donor mandates, available budgets.
- **Governing Policies:** Impartiality principles.
- **Constraints:** Finite budgets mathematically limit the number of eligible recipients.
- **Preconditions:** Intervention is approved and budgeted.
- **Alternative Outcomes:** Broad rules (high inclusion), Strict rules (high exclusion).
- **Escalation Conditions:** Rules are so strict that vulnerable people are dying without aid.
- **Review Triggers:** 50% budget consumed much faster or slower than predicted.
- **Appeal Mechanisms:** Not individually appealed here (Case Management handles individual appeals), but aggregated appeals trigger rule review.
- **Human Override:** Programme Director can formally relax rules.
- **Uncertainty:** The true demographic size of the eligible population is usually an estimate.

## 4. Resource Reallocation Decision
- **Purpose:** Shifting budgets between interventions or geographic areas.
- **Decision Maker:** Budget Owner / Programme Manager.
- **Supporting Evidence:** Burn rates, emergent field reports, logistical bottlenecks.
- **Governing Policies:** Donor flexibility policies (e.g., standard 10% budget line variance).
- **Constraints:** Strict earmarking of donor funds.
- **Preconditions:** Underspend in one area, overspend/acute need in another.
- **Alternative Outcomes:** Reallocated internally, Formal donor amendment requested, Denied.
- **Escalation Conditions:** Donor refuses amendment despite extreme field necessity.
- **Review Triggers:** Monthly budget variance reports.
- **Appeal Mechanisms:** Project managers can formally petition the budget holder.
- **Human Override:** Crisis Modifier clauses allowing instant, pre-authorized reallocation.
- **Uncertainty:** Reallocating today might leave a shortfall tomorrow.
"""
with open(os.path.join(pm_dir, "08-decision-points.md"), "w", encoding="utf-8") as f:
    f.write(decisions_content)

# 7. Update Evidence
evidence_content = """# Supporting Evidence

## Established Facts
- Programme Management sits structurally above Case Management, setting the rules that frontline workers must follow.
- Interventions cannot be offered by Case Management unless they have been formally designed, catalogued, and budgeted by Programme Management.
- Donor funding is rarely universally fungible; it is often tightly bound to specific sectors, geographic areas, or demographic targets.

## Reasonable Assumptions
- Budgets will frequently need to be reallocated mid-cycle due to unpredictable crises.
- Initial estimates of population size and vulnerability will often be inaccurate.

## Open Questions (Moved to 10-open-questions.md)
Refer to 10-open-questions.md

## Knowledge Gaps
- How is the mathematical translation between an overarching "Grant Budget" and a per-household "Intervention Cost" dynamically maintained when market prices fluctuate wildly?
"""
with open(os.path.join(pm_dir, "11-evidence.md"), "w", encoding="utf-8") as f:
    f.write(evidence_content)

# 8. Create Ontology Readiness
onto_content = """# Ontology Readiness

The following conceptual clusters appear highly stable and ready for subsequent formal Ontology Design (Stage 6):
- **The Hierarchical Constraint Model:** The strict relationship between Programme -> Intervention Catalogue -> Intervention Offering -> Eligibility Rule.
- **Funding Allocation Model:** The relationship between Donor Grant, Programme Budget, and Sector Allocation.
- **The Rule-Engine Boundary:** The conceptual structure where Programme Management defines the Rule and Case Management executes the Evaluation of that rule against an individual.

These concepts can be modelled without requiring implementation assumptions.
"""
with open(os.path.join(pm_dir, "14-ontology-readiness.md"), "w", encoding="utf-8") as f:
    f.write(onto_content)

print("Programme Management files updated successfully to meet the 20-point standard.")
