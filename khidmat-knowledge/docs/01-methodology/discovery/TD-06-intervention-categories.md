---
id: TD-06
title: Intervention Categories (BMP Chapter 6)
status: Handed off
created: 2026-07-27
governed_by: ../BUSINESS_DISCOVERY_BLUEPRINT.md
---

# Topic Dossier 06 — Intervention Categories

## 1. Scope
**Topic:** What broad categories of assistance exist in humanitarian practice, what distinguishes them (e.g., immediate relief vs. rehabilitative support), and how they should be classified as business concepts without preempting taxonomy encoding. (Derived from BMP Blueprint §7).
**Objective:** Discover the real categories of humanitarian interventions, distinguish between programme-altitude and case-altitude categorizations, and identify whether interventions can belong to multiple categories simultaneously.

## 2. Research Questions
1. What intervention categories exist in humanitarian practice and which are universally recognized?
2. Which vary by organization, region, or emergency type?
3. Which interventions operate primarily at programme altitude vs case altitude?
4. Can one intervention belong to multiple categories?
5. Which categories appear stable enough to represent enduring business concepts vs operational implementations?

## 3. Tier C (Internal artifacts)
- `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §9 (Needs Model) lists Food, Health, Education, Housing, Livelihood, Psychosocial, and Protection as categories.
- `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §12 (Support Model) categorizes support as Financial, Material, Medical, Educational, and Livelihood. It explicitly states the concrete intervention catalogue and eligibility per intervention are planned but currently out of scope, relying on operational input from programme staff.

## 4. Tier B (Recognized sector standards)
- **IASC Humanitarian Clusters:** The Inter-Agency Standing Committee (IASC) universally classifies humanitarian action into sectors/clusters (e.g., CCCM, Early Recovery, Education, Food Security, Health, Logistics, Nutrition, Protection, Shelter, WASH).
- **Modalities of Assistance:** The sector standardizes delivery methods into three primary modalities: Cash and Voucher Assistance (CVA), In-Kind Assistance, and Service Delivery.
- **The Triple Nexus (Humanitarian-Development-Peace):** The sector recognizes a temporal/objective categorization distinguishing Immediate Relief (saving lives), Rehabilitation/Recovery (restoring services), and Development (long-term resilience).

## 5. Tier D (Secondary literature)
- Secondary literature confirms the broad adoption of Multipurpose Cash (MPC) as a modality that crosses traditional sector boundaries, fulfilling multiple needs simultaneously.
- The shift from "Linking Relief, Rehabilitation and Development (LRRD)" to the "Triple Nexus" confirms that interventions are not strictly sequential but concurrent and mutually reinforcing.

## 6. Tier A Feasibility Assessment
- **Status:** Infeasible in the current execution environment.
- **Reasoning:** As with previous dossiers, direct access to primary humanitarian practitioners (Tier A) to confirm specific operational intervention catalogues for Khidmat's immediate context is unavailable. This dossier proceeds on Tier B, C, and D evidence to define the *categories* as business concepts.

## 7. Findings

**BD-TD06-001: The three dimensions of intervention categorization**
- **Statement:** Humanitarian interventions are categorized along three fundamentally distinct, universally recognized dimensions: Sector/Domain (what need is addressed, e.g., Health, Shelter), Modality (how it is delivered, e.g., Cash, In-kind, Service), and Temporal/Objective Phase (why/when it is delivered, e.g., Emergency Relief, Rehabilitation, Development).
- **What humanitarian business reality has been discovered?** Interventions cannot be flattened into a single list. An intervention exists at the intersection of these three dimensions (e.g., an Emergency [Temporal] In-kind [Modality] Shelter [Sector] intervention).
- **Why does it matter?** It prevents a future taxonomy from falsely forcing a hierarchical choice between a delivery method and a domain of need.
- **Is it universal, common practice, or context-specific?** Universal (aligned with IASC clusters, CVA standards, and Triple Nexus frameworks).
- **Does it reinforce, refine, or challenge previous discovery?** Refines the Tier C Support Model (`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`), which mixes modalities ("Financial", "Material") with sectors ("Medical", "Educational") in a single list.
- **Source:** Tier B (IASC, Humanitarian modalities standards, Triple Nexus definitions).
- **Confidence:** High.
- **Evidence Current As Of:** 2026-07-27.
- **Applicability Scope:** General/cross-context.

**BD-TD06-002: Sector categorizations operate at Programme altitude; Modalities operate at Case altitude**
- **Statement:** IASC Clusters (Sectors) are used to organize macro-level response, coordinate NGOs, and pool funding (Programme altitude). The selection of modality (e.g., Cash vs In-kind) is a decision made based on local market feasibility and individual household appropriateness (Case altitude).
- **What humanitarian business reality has been discovered?** The categorization of an intervention depends on the altitude from which it is viewed.
- **Why does it matter?** It clarifies governance boundaries. Programme designers define the Sector, but Case Managers or field conditions often dictate the Modality.
- **Is it universal, common practice, or context-specific?** Common practice.
- **Does it reinforce, refine, or challenge previous discovery?** Reinforces the Programme vs Case altitude split identified in TD-03 and TD-05.
- **Source:** Tier B/D (IASC Coordination guidance, CVA feasibility literature).
- **Confidence:** Medium-High.
- **Evidence Current As Of:** 2026-07-27.
- **Applicability Scope:** General/cross-context.

**BD-TD06-003: Multi-sectoral interventions (N:N mapping)**
- **Statement:** A single intervention can simultaneously address multiple sector categories. Multipurpose Cash (MPC) is the primary example, delivered as a single modality but intended to cover Food, Shelter, and WASH needs concurrently.
- **What humanitarian business reality has been discovered?** The mapping between a delivered intervention and a business sector is many-to-many, not one-to-one.
- **Why does it matter?** It means the business logic must allow a single case or intervention record to satisfy multiple distinct needs across different domains.
- **Is it universal, common practice, or context-specific?** Universal common practice in modern humanitarian response.
- **Does it reinforce, refine, or challenge previous discovery?** Challenges the assumption of clean, siloed capability execution; reinforces the need for integrated case-management spanning multiple capabilities.
- **Source:** Tier B/D (CVA standards, humanitarian policy literature).
- **Confidence:** High.
- **Evidence Current As Of:** 2026-07-27.
- **Applicability Scope:** General/cross-context.

**BD-TD06-004: Business concepts vs Operational implementations**
- **Statement:** The three dimensions (Sector, Modality, Temporal Phase) represent stable, enduring business concepts. The specific items delivered (e.g., "jerry cans," "school fees," "hygiene kits") are operational implementations that vary significantly by region, organization, and emergency type.
- **What humanitarian business reality has been discovered?** The detailed intervention catalogue is inherently volatile and context-dependent.
- **Why does it matter?** The Business Master Plan should define the dimensions (the business concepts) but must explicitly avoid hardcoding the operational catalogue, which belongs to downstream configuration or taxonomy.
- **Is it universal, common practice, or context-specific?** Universal.
- **Does it reinforce, refine, or challenge previous discovery?** Reinforces `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §12's assertion that the concrete catalogue is out of scope for the core logic layer.
- **Source:** Tier D (Supply chain literature) and Tier C.
- **Confidence:** High.
- **Evidence Current As Of:** 2026-07-27.
- **Applicability Scope:** General/cross-context.

## 8. Assumptions
- **AR-010:** Due to the absence of Tier A evidence, it is assumed that Khidmat partner organizations recognize and use these three standard dimensions (Sector, Modality, Temporal Phase) in their own programmatic design, even if their internal terminology differs slightly.

## 9. Contradictions
- None newly identified. (Note: Finding BD-TD06-001 refines an internal Tier C artifact's list, but this is a structural refinement of a draft document rather than a formal contradiction requiring Human Owner resolution).

## 10. Discovery Review
- **Limitations:** Tier A is absent (structural limitation). The discovery relies on Tier B (IASC, humanitarian standards) and Tier D (literature on CVA and Triple Nexus).
- **Completeness:** The dossier meets the Blueprint's requirements for Chapter 6. It identifies the broad kinds of assistance, what distinguishes them, and answers the specific research questions regarding altitude and multi-category membership.
- **Next Steps:** BMP Chapter 6 authoring can proceed using these findings, noting the Discovery Limitation regarding specific operational catalogues.

## 11. Handoff
- **Status:** Ready for BMP Chapter 6 authoring.
- **Discovery Limitation:** Yes (Tier A absent; relies on Tiers B, C, and D).
