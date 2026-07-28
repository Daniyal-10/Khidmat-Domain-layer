import os

rl_dir = "docs/02-discovery/resource-logistics"

# 1. Update 01-domain-overview.md to include Business Outcomes, Capabilities, Activities
with open(os.path.join(rl_dir, "01-domain-overview.md"), "r", encoding="utf-8") as f:
    overview_content = f.read()

if "## Business Outcomes" not in overview_content:
    overview_content += "\n## Business Outcomes\n- Safe, timely, and dignified delivery of approved aid.\n- Precise auditability of all resources from procurement origin to beneficiary receipt.\n- Efficient management of operational supply chains and financial service networks.\n"
    overview_content += "\n## Business Capabilities\n- Procurement & Sourcing\n- Supply Chain & Warehousing Management\n- Cash Transfer & Financial Service Execution\n- Physical Distribution & Last-Mile Logistics\n- Fulfillment Verification\n"
    overview_content += "\n## Core Business Activities\n- Sourcing quotes and selecting vendors.\n- Receiving, inspecting, and storing inventory.\n- Allocating stock to specific distribution points.\n- Authorizing FSPs to disburse cash.\n- Securing physical signatures or cryptographic proof of beneficiary receipt.\n"
    with open(os.path.join(rl_dir, "01-domain-overview.md"), "w", encoding="utf-8") as f:
        f.write(overview_content)

# 2. Create Stakeholders
stakeholders_content = """# Stakeholders

## Actors (Enduring Participants)
- **Vendor / Supplier:** External commercial entity providing physical goods or services.
- **Transporter:** External or internal entity physically moving goods.
- **Financial Service Provider (FSP):** Bank or mobile money operator executing cash transfers.
- **Individual:** The human being receiving the aid.

## Roles (Transient Responsibilities)
- **Procurement Officer:** Role responsible for sourcing and vendor selection.
- **Logistics Coordinator:** Role responsible for supply chain movement and dispatch.
- **Warehouse Manager:** Role responsible for inventory custody and storage.
- **Distribution Agent:** Role physically handing goods to beneficiaries.
"""
with open(os.path.join(rl_dir, "01b-stakeholders.md"), "w", encoding="utf-8") as f:
    f.write(stakeholders_content)

# 3. Create Knowledge Patterns
kp_content = """# Knowledge Patterns
- **Chain of Custody:** The epistemic transfer of liability alongside physical goods (Supplier -> Warehouse -> Transporter -> Distribution Point -> Beneficiary), requiring continuous verification handshakes.
- **The Execution Trigger Handoff:** An authorized Support Plan from Case Management crosses the domain boundary to become an Execution Trigger, shifting the epistemic focus from "why they need it" to "how they get it."
"""
with open(os.path.join(rl_dir, "04b-knowledge-patterns.md"), "w", encoding="utf-8") as f:
    f.write(kp_content)

# 4. Create Exceptions
exc_content = """# Exceptions
- **Reverse Logistics / Uncollected Goods:** Beneficiaries fail to appear, requiring goods to be formally returned to inventory.
- **Shrinkage / Spoilage:** Inventory is lost, stolen, or expires, breaking the expected balance between procured stock and fulfillable demand.
- **Partial Fulfillment (Backorder):** Beneficiary is approved for a full kit, but only partial stock is available; the domain must track the outstanding deficit.
- **Emergency Procurement Override:** Skipping standard bidding rules during an acute life-saving crisis.
"""
with open(os.path.join(rl_dir, "05b-exceptions.md"), "w", encoding="utf-8") as f:
    f.write(exc_content)

# 5. Create Business Tensions
tens_content = """# Business Tensions
The Resource and Logistics domain continuously balances competing operational forces:
- **Speed of Response vs Anti-Fraud Compliance:** The tension between bypassing slow procurement rules to save lives immediately versus maintaining strict competitive bidding and segregation of duties.
- **Local Market Stimulation vs Bulk International Efficiency:** The strategic tension of buying locally to support the economy (often more expensive/slower) versus importing bulk goods internationally (cheaper/faster but hurts local markets).
- **Security vs Access:** The friction of dispatching goods into highly insecure areas to reach vulnerable populations versus protecting staff and inventory from theft or harm.
- **In-Kind Logistics vs Cash Transfer Dependency:** The trade-off between the heavy physical burden of warehousing goods versus relying entirely on commercial FSP networks that may fail during infrastructure outages.
"""
with open(os.path.join(rl_dir, "05c-business-tensions.md"), "w", encoding="utf-8") as f:
    f.write(tens_content)

# 6. Update Decision Points
decisions_content = """# Significant Business Decisions

## 1. Procurement Sourcing Decision
- **Purpose:** Determining whether to buy locally, regionally, or internationally.
- **Decision Maker:** Procurement Officer / Logistics Manager.
- **Supporting Evidence:** Market feasibility assessments, cost quotes, lead times.
- **Governing Policies:** Donor origin constraints, Organisational financial thresholds.
- **Constraints:** Local market capacity, international shipping bottlenecks.
- **Preconditions:** Approved Programme budget and Intervention demand.
- **Alternative Outcomes:** Procured locally, Tendered internationally, Sourcing failed.
- **Escalation Conditions:** Critical items cannot be sourced within the required timeframe.
- **Review Triggers:** Routine anti-fraud audits.
- **Appeal Mechanisms:** Rejected vendors may formally contest the tender process.
- **Human Override:** Emergency waivers allowing single-source procurement.
- **Uncertainty:** Vendor reliability and hidden supply chain risks.

## 2. Dispatch Prioritisation Decision
- **Purpose:** Determining which execution triggers to fulfill first when available stock is lower than total demand.
- **Decision Maker:** Logistics Coordinator.
- **Supporting Evidence:** Real-time inventory levels, Case Management vulnerability priority tags.
- **Governing Policies:** "Life-saving first" operational mandates.
- **Constraints:** Warehouse location vs. Distribution point distance.
- **Preconditions:** Execution triggers received; partial stock available.
- **Alternative Outcomes:** Full dispatch to Priority A, Partial dispatch, Dispatch delayed.
- **Escalation Conditions:** Widespread stockouts during active crisis.
- **Review Triggers:** Post-distribution reconciliation.
- **Appeal Mechanisms:** Case Management can request urgent escalation.
- **Human Override:** Programme Director overrides standard queuing to direct aid to a specific flashpoint.
- **Uncertainty:** In-transit spoilage or hijacking.

## 3. Vendor / FSP Selection Decision
- **Purpose:** Determining which commercial entity will provide goods or facilitate cash transfers.
- **Decision Maker:** Procurement Committee.
- **Supporting Evidence:** Competitive bids, anti-terrorism vetting, past performance data, geographic reach.
- **Governing Policies:** Donor compliance, Anti-Money Laundering (AML) laws.
- **Constraints:** Highly restrictive banking laws in conflict zones.
- **Preconditions:** Vendor must pass basic legal/security screening.
- **Alternative Outcomes:** Contract awarded, Vendor blacklisted, Tender restarted.
- **Escalation Conditions:** Only available FSP fails security vetting, preventing cash delivery.
- **Review Triggers:** Annual vendor performance review.
- **Appeal Mechanisms:** Formal vendor grievance process.
- **Human Override:** None for anti-terrorism checks; waivers possible for standard bidding.
- **Uncertainty:** FSP liquidity during a sudden crisis.
"""
with open(os.path.join(rl_dir, "08-decision-points.md"), "w", encoding="utf-8") as f:
    f.write(decisions_content)

# 7. Update Evidence
evidence_content = """# Supporting Evidence

## Established Facts
- The person who procures cannot be the person who receives the goods into stock.
- The person who assesses vulnerability (Case Management) cannot physically distribute the aid.
- Every unit of material or cash must be mathematically traceable from procurement origin to beneficiary receipt.
- Execution triggers generated by Case Management are fulfilled without questioning the underlying vulnerability assessment.

## Reasonable Assumptions
- Emergency procurement rules will frequently be invoked, bypassing standard 3-quote minimums.
- Local FSPs may suffer acute liquidity shortages during mass cash distributions.

## Open Questions (Moved to 10-open-questions.md)
Refer to 10-open-questions.md

## Knowledge Gaps
- How is the physical security of a distribution point formally verified and continually reassessed before and during a dispatch?
- How does the domain manage cash liquidity crises in local markets when electronic transfers fail?
"""
with open(os.path.join(rl_dir, "11-evidence.md"), "w", encoding="utf-8") as f:
    f.write(evidence_content)

# 8. Create Ontology Readiness
onto_content = """# Ontology Readiness

The following conceptual clusters appear highly stable and ready for subsequent formal Ontology Design (Stage 6):
- **Chain of Custody Model:** The structural transfer of liability (Procurement -> Inventory -> Dispatch -> Fulfillment).
- **The Execution Trigger Boundary:** The conceptual distinction between a Support Plan (a justified need) and an Execution Trigger (an actionable logistics demand).
- **Resource Modality:** The clear structural differences between In-Kind Goods, Cash Transfers, and Service Vouchers.

These concepts can be modelled without requiring implementation assumptions.
"""
with open(os.path.join(rl_dir, "14-ontology-readiness.md"), "w", encoding="utf-8") as f:
    f.write(onto_content)

print("Resource and Logistics files updated successfully to meet the 20-point standard.")
