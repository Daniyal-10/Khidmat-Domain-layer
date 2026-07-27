---
id: TD-05
title: Business Services and Value Streams (BMP Chapter 5)
status: Handed off
created: 2026-07-27
governed_by: ../BUSINESS_DISCOVERY_BLUEPRINT.md
---

# Topic Dossier 05 — Business Services and Value Streams

## 1. Scope
**Topic:** What each capability actually produces (e.g., a verified case, a delivered intervention, a closed referral) and trace the end-to-end value streams that connect a beneficiary's triggering need to a delivered, measurable outcome. (Derived from BMP Blueprint §7).
**Objective:** Discover what services exist, why they exist, who provides them, who receives value, what organizational purpose they serve, and at what altitude they operate.

## 2. Research Questions
1. Are there value streams humanitarian organizations run that would not cleanly decompose into a capability sequence (e.g., area-level/programmatic response to a community-wide crisis)?
2. What are the recognized value streams in the humanitarian sector?
3. What are the concrete services produced by business capabilities (as opposed to the capabilities themselves)?

## 3. Tier C (Internal artifacts)
- `PROJECT_OVERVIEW.md` describes the Cognitive Lifecycle (Evidence/Knowledge Acquisition → Understanding Formation → Reasoning → Responsible Action), treating automation/action as a consequence of understanding, not a stage itself.
- `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §14 outlines a Beneficiary Lifecycle flow: Awareness → Lead Creation → Registration → Verification → Needs Assessment → Eligibility → Support Planning → Volunteer Assignment → Support Delivery → Follow-up → Case Management → Outcome/Impact Measurement.
- `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §16 limits V1 scope to the "understanding" components, explicitly excluding the resource-supply side, donor matching, and logistics delivery.

## 4. Tier B (Recognized sector standards)
- **Humanitarian Value Stream Mapping (HVSM):** An established sector methodology adapted from Lean management. It maps the flow of resources and information between nodes in a supply chain, analyzing bottlenecks and waste. It treats humanitarian interventions as multiple, context-specific value streams built from distinct combinations of actors and resources.

## 5. Tier D (Secondary literature)
- **Humanitarian Value Chains:** Secondary literature emphasizes the complexity of the humanitarian value chain, describing it as an interconnected network of processes from donor relations to procurement, logistics, and field implementation. Modern research places strong emphasis on separating the "information flow" from the "material flow" to improve data-driven delivery for vulnerable populations.

## 6. Tier A Feasibility Assessment
- **Status:** Infeasible in the current execution environment.
- **Reasoning:** As documented in Phase Review 01 and earlier dossiers, direct access to primary humanitarian practitioners remains unavailable. The dossier proceeds relying on Tier B, C, and D evidence.

## 7. Findings

**BD-TD05-001: The dual-flow nature of humanitarian value chains**
- **Statement:** The humanitarian value chain comprises two concurrent and interdependent flows: an information/knowledge flow (registration, verification, needs assessment) and a material/resource flow (procurement, logistics, direct support delivery).
- **What humanitarian business reality has been discovered?** Humanitarian operations practically decouple the gathering and processing of contextual knowledge from the physical delivery of aid.
- **Why does it matter?** It validates the project's foundational premise (Tier C) that a dedicated "knowledge layer" is a real business requirement, structurally distinct from a logistics or transaction layer.
- **Is it universal, common practice, or context-specific?** Universal (inherent to modern humanitarian supply chain theory and HVSM methodologies).
- **Does it reinforce, refine, or challenge previous discovery?** Reinforces `PROJECT_OVERVIEW.md`'s sequence (Knowledge → Understanding → Reasoning → Responsible Action) and previous findings regarding the separation of claims from facts.
- **Source:** Tier D (Published HVSM literature and humanitarian supply chain research).
- **Confidence:** Medium-High.
- **Evidence Current As Of:** 2026-07-27.
- **Applicability Scope:** General/cross-context (per AR-002).

**BD-TD05-002: Programme-altitude value streams vs Case-level capability sequences**
- **Statement:** Area-level or community-wide crisis responses constitute distinct programmatic value streams that do not cleanly decompose into sequential, individual case-level capabilities. They operate on aggregated area-level triggers rather than waiting for individual beneficiary registrations.
- **What humanitarian business reality has been discovered?** Value streams operate at different altitudes. A community-level response is structurally distinct from an individual case-level value stream.
- **Why does it matter?** It answers the specific research question posed in the BMP Blueprint §7 for Chapter 5, ensuring the BMP does not falsely model all humanitarian action as individual case management.
- **Is it universal, common practice, or context-specific?** Universal across acute emergency and area-based response contexts.
- **Does it reinforce, refine, or challenge previous discovery?** Refines the Case vs Programme altitude split discovered in TD-03, confirming that value streams themselves split along this axis.
- **Source:** Tier D (Emergency operations case studies) and Tier C (`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §8 Community Model).
- **Confidence:** Medium-High.
- **Evidence Current As Of:** 2026-07-27.
- **Applicability Scope:** General/cross-context.

**BD-TD05-003: Services as capability outputs**
- **Statement:** Business services are the tangible outputs of capabilities (e.g., a verified claim, an assessed need, an approved support plan). A value stream is constructed by chaining the output services of discrete capabilities, not by merging the capabilities together.
- **What humanitarian business reality has been discovered?** The handoff of a service represents a clear governance and ownership boundary within a value stream.
- **Why does it matter?** It provides the structural mechanism for how a beneficiary moves through the humanitarian lifecycle, supporting the principle of single-ownership and clear governance boundaries.
- **Is it universal, common practice, or context-specific?** Common practice in structured sector methodologies (Lean/HVSM).
- **Does it reinforce, refine, or challenge previous discovery?** Reinforces the Beneficiary Lifecycle defined in TD-03 and Tier C artifacts.
- **Source:** Tier B/D (HVSM methodology).
- **Confidence:** High.
- **Evidence Current As Of:** 2026-07-27.
- **Applicability Scope:** General/cross-context.

## 8. Assumptions
- **AR-009:** Due to the absence of Tier A practitioner evidence, specific end-to-end value stream narratives (e.g., the exact operational sequence for an Emergency Shelter Response versus a Sustainable Livelihood Pathway) are assumed to structurally follow the generic Beneficiary Lifecycle logic described in Tier C, but the concrete operational differences between them remain unevidenced.

## 9. Contradictions
- None newly identified. Finding BD-TD05-002 (the distinction between Programme-level value streams and individual Case-level capability sequences) directly reinforces the existing Programme/Organisation conceptual split already logged in **CL-001**, further indicating that this altitude boundary is a real feature of humanitarian operations.

## 10. Discovery Review
- **Limitations:** Tier A is absent (structural limitation). Evidence relies heavily on secondary literature (Tier D) regarding Humanitarian Value Stream Mapping, combined with internal Tier C logic.
- **Completeness:** The topic has met the Blueprint's requirements. It successfully describes the dual-flow nature of value streams, answers the specific Blueprint research question about area-level responses, and defines the structural relationship between capabilities and services. 
- **Next Steps:** BMP Chapter 5 authoring can proceed, noting the Discovery Limitation regarding specific operational value stream narratives.

## 11. Handoff
- **Status:** Ready for BMP Chapter 5 authoring.
- **Discovery Limitation:** Yes (Tier A absent; relies on Tiers B, C, and D).
