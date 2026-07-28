# Terminology Harmonization

## 1. Executive Overview

In large-scale humanitarian ecosystems, the language used to describe reality dictates how the system responds to that reality. Across the Khidmat Domain Layer, isolated domains—such as Case Management, Programme Management, and Cross-Organisational Coordination—have evolved divergent dialects to describe overlapping realities. This document establishes a unified semantic framework across all domains. It isolates conflicting terms, standardizes definitions, and outlines the structural consequences of linguistic ambiguity, providing the authoritative terminology baseline required for the subsequent ontological design.

## 2. Purpose

The purpose of this document is to eliminate semantic drift between distinct humanitarian domains. When terms like "Monitoring" or "Referral" mean completely different things depending on the operational context, the resulting friction creates data silos, prevents inter-agency coordination, and fundamentally harms the beneficiaries the system aims to support. This document enforces a canonical vocabulary to ensure that when a concept is invoked, its meaning is universally understood, structurally sound, and legally precise.

## 3. Scope

This harmonization spans the foundational business domains: Case Management, Accountability & Evaluation, Cross-Organisational Coordination, Programme Management, and Organisation & Partner Management. It explicitly targets terms that represent cross-domain handoffs, ambiguous concepts that cause operational failure, and evolving language driven by shifting humanitarian principles (e.g., "localization").

## 4. Detailed Analysis: Preferred vs. Rejected Terminology

### 4.1. "Needs Assessment"
* **Ambiguity:** Used interchangeably to mean assessing an individual's specific vulnerabilities (micro) and evaluating a regional population's overall crisis severity (macro).
* **Preferred Terminology:** 
  * **Individual Needs Assessment:** Reserved strictly for Case Management when evaluating a specific person or household.
  * **Regional Vulnerability Assessment:** Reserved for Programme Management when defining macro-level funding and intervention strategies.
* **Rejected Terminology:** "Needs Assessment" as a standalone, unqualified term.
* **Reason for Canonical Selection:** Prevents catastrophic scoping errors where a macro-level survey is mistakenly treated as an actionable mandate for individual aid delivery.
* **Business Consequences of Inconsistency:** If macro surveys are ingested as micro assessments, logistics pipelines are triggered for unverified individuals, leading to massive aid diversion and budget exhaustion.

### 4.2. "Monitoring"
* **Ambiguity:** Can denote tracking an individual beneficiary's recovery over time (health, status), or it can denote the statistical measurement of a programme's overall efficacy (M&E).
* **Preferred Terminology:**
  * **Case Monitoring:** The continuous, individual follow-up managed by Case Management.
  * **Programmatic Monitoring (or MEAL):** The aggregate, statistical tracking managed by Accountability & Evaluation.
* **Rejected Terminology:** "Monitoring" without an operational prefix.
* **Reason for Canonical Selection:** Case Monitoring requires extreme privacy safeguards and actionable triggers, whereas Programmatic Monitoring requires anonymization and objective distance.
* **Business Consequences of Inconsistency:** Applying programmatic data rules to a case monitor strips the data of its identifying context, rendering follow-up impossible and abandoning the beneficiary.

### 4.3. "Referral"
* **Ambiguity:** Denotes passing a case to a specialized colleague within the same NGO, or passing a case across legal boundaries to an entirely different organisation.
* **Preferred Terminology:**
  * **Internal Escalation / Handoff:** Movement of a case within a single sovereign entity (Case Management).
  * **External Referral:** The legally fraught transfer of sensitive case context across independent organisational boundaries (Cross-Organisational Coordination).
* **Rejected Terminology:** "Referral" without specifying internal or external.
* **Reason for Canonical Selection:** External Referrals trigger severe data protection protocols, require explicit beneficiary consent, and involve inter-agency trust vetting. Internal escalations do not.
* **Business Consequences of Inconsistency:** Treating an external referral like an internal handoff results in massive GDPR and safeguarding breaches, exposing vulnerable individuals to unvetted external actors.

### 4.4. "Sharing"
* **Ambiguity:** Sharing can mean sending the raw, unencrypted narrative files of a beneficiary's trauma, or it can mean broadcasting a cryptographic proof that a beneficiary is receiving a specific service without revealing their identity.
* **Preferred Terminology:**
  * **Raw Context Transfer:** The movement of full, unencrypted data (used only in highly trusted, localized External Referrals).
  * **Privacy-Preserving Proofs:** Cryptographic or minimal-disclosure indicators used for deduplication.
* **Rejected Terminology:** "Data Sharing".
* **Reason for Canonical Selection:** "Data Sharing" implies a loss of sovereign control over sensitive information, which NGOs fiercely resist. 
* **Business Consequences of Inconsistency:** NGOs will default to hoarding data rather than "sharing" it, breaking all coordination and deduplication efforts.

### 4.5. "Capacity"
* **Ambiguity:** Used to describe an organisation's technical expertise (e.g., surgical skills) and its financial/logistical scale (e.g., ability to absorb a $10M grant).
* **Preferred Terminology:**
  * **Capability:** The specific technical or sectoral skills an organisation possesses.
  * **Scale:** The logistical, geographic, or financial volume an organisation can manage.
* **Rejected Terminology:** "Capacity" as a blanket term.
* **Reason for Canonical Selection:** A highly capable local medical NGO may have zero financial scale to absorb Western donor funds. Conflating the two forces them out of the ecosystem.
* **Business Consequences of Inconsistency:** Essential local partners are excluded from consortia because their "capacity" (scale) is deemed too low, despite having the exact "capacity" (capability) required to save lives.

### 4.6. "Closure"
* **Ambiguity:** The end of a single intervention episode versus the permanent exit of the beneficiary from the humanitarian system.
* **Preferred Terminology:**
  * **Intervention Closure:** The completion of a specific Support Plan.
  * **Case Exit / Graduation:** The formal determination that an individual is resilient and no longer requires any humanitarian interface.
* **Rejected Terminology:** "Case Closure".
* **Reason for Canonical Selection:** A person can complete a food distribution (Intervention Closure) but remain highly vulnerable to violence (Active Case).
* **Business Consequences of Inconsistency:** Premature Case Closure artificially deflates vulnerability metrics, causing Programme Management to prematurely cut funding to unstable regions.

## 5. Competing, Historical, and Regional Terminology

The humanitarian sector is burdened by the legacy of colonial architecture and donor-centric language.
* **Beneficiary vs. Affected Person:** Historically, "Beneficiary" implied a passive, grateful recipient of Western charity. The preferred modern term is "Affected Person" or "Individual," establishing their agency and rights. However, legal frameworks still rely on "Beneficiary." We adopt **Individual** as the structural entity, and **Beneficiary** strictly as a transient role they occupy when interacting with the system.
* **Local Partner vs. Implementing Partner / Subcontractor:** INGOs often use "Implementing Partner" to denote a subcontractor. This strips local NGOs of their sovereign agency. We standardize on **Partner Organisation**, affirming their equal legal standing and independent mandate.
* **CFM (Complaints and Feedback Mechanism) vs. AAP (Accountability to Affected Populations):** Different donors mandate different acronyms for the exact same capability. We harmonize on **Grievance and Feedback Mechanisms (GFM)** for the operational capability, maintaining AAP as the strategic principle.

## 6. Migration Recommendations

To migrate existing systems and operational mindsets to this harmonized terminology, we recommend:
1. **Ontological Hardcoding:** Embed the exact preferred terminology into the Stage 6 Ontology. Code structures, API endpoints, and database schemas must use `ExternalReferral` and `IndividualNeedsAssessment`, rejecting ambiguous legacy terms.
2. **Policy Rewrites:** All newly drafted Standard Operating Procedures (SOPs) and Information Sharing Protocols (ISPs) must explicitly define terms using this document's taxonomy.
3. **UI/UX Enforcement:** Front-facing applications used by field workers must label buttons and workflows with the disambiguated terms (e.g., "Trigger External Referral" instead of "Refer").

## 7. Open Terminology Questions

* How do we universally categorize grassroots, unregistered community networks that act as an "Organisation" but legally do not exist in the host country's registry?
* Should the term "Vulnerability" be replaced with a less deficit-oriented term, such as "Resilience Gap," to align with modern dignified aid principles?
* How is "Consent" accurately translated into contexts where individual consent is culturally superseded by patriarchal household consent?
