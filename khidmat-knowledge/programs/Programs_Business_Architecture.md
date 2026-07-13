# Programs Business Architecture

**Status:** Draft / Business Architecture Freeze Pending
**Domain:** Programs
**Purpose:** This document is the definitive statement of the business architecture for the Programs domain within the Khidmat Humanitarian Operating System. It defines the concepts, actors, lifecycles, and principles the domain governs. It is designed to model global humanitarian operations (UN, INGOs) and complex national welfare structures without hardcoding specific regional schemes.

---

## 1. What is Programs?
Programs is the governance, structuring, and compliance domain of Khidmat. It represents the formal initiatives created by NGOs, governments, foundations, and trusts to address specific vulnerabilities. While Case Management deals with a single family's journey, Programs deals with the design, rules, cohorts, funding structures, compliance, and offerings that authorize and constrain that journey.

## 2. What it Owns
Programs owns the *structure, rules, and lifecycle* of assistance initiatives. This includes:

### A. Program Identity & Topology
- **Program Entity:** The core structural initiative (e.g., "Emergency Flood Response 2026", "National Pension Scheme").
- **Program Inheritance & Variations:** Parent-child relationships for geographic rollouts (e.g., a multi-country UN program with state-level or local implementing variations).
- **Program Versions & Amendments:** Tracking changes to a program's structure (e.g., eligibility rules changing due to inflation or political priorities) over time.

### B. Eligibility & Targeting rules
- **Eligibility Criteria:** Rule definitions evaluated against a household's profile.
- **Criteria Versioning:** Tracking which version of rules applied at the time of a beneficiary's enrollment.

### C. The Intervention Catalogue
- **Intervention Definition:** What modalities (cash, material, service) the program offers.
- **Conditionality & Phasing:** Rules governing milestone-based assistance (e.g., cash conditional on vaccination), recurring vs. one-off assistance, and phased assistance (gradual step-downs).

### D. Funding & Compliance Constraints
- **Funding Restrictions:** Earmarked funding vs. unrestricted funding rules.
- **Co-funding & Partner Delegation:** Tracking programs where one entity funds, another governs, and a third implements.
- **Compliance & Audit Checkpoints:** Reporting periods, regulatory compliance checks, and indicator ownership.

### E. Program Lifecycles
- **Program Stages:** Pilot, Permanent, Emergency Activation, Suspended (due to conflict or funding cuts), Reopened, Closed, Renewed.
- **Successor Relationships:** Tracking when a defunded or concluding program is replaced by a new program, enabling cohort transitions.

### F. Enrollment & Cohort Dynamics
- **Enrollment State:** Applied, Waitlisted, Enrolled, Suspended, Graduated, Administratively Terminated.
- **Enrollment Prioritization:** Rules for waitlist management (e.g., prioritizing highest vulnerability scores).
- **Exceptions & Appeals:** Manual approval authorities, humanitarian overrides, and appeal pathways.
- **Cross-Program Relationships:** Mutually exclusive programs (anti-double-dipping), prerequisite programs, dependency programs, and graduation pathways (Program A feeds into Program B).

## 3. What it Never Owns
- **The Need:** Needs exist independently of programs. Programs define offerings, not realities.
- **The Individual Case Plan:** Programs provide the menu and rules; Case Management orchestrates the individual's specific journey.
- **Operational Delivery:** Logistics and proof-of-delivery belong to Support Delivery.
- **Granular Financial Ledger (ERP):** Programs model funding *constraints* and conceptual budgets, but do not replace double-entry accounting software.

## 4. Program Topologies (Global & India Readiness)
The domain natively models diverse real-world patterns:
- **Entitlement / Subsidy Programs:** Government welfare (e.g., food rations, social pensions) characterized by statutory eligibility and theoretically infinite capacity.
- **Direct Benefit Transfers (DBT):** Programs characterized by digital execution and strict identity verification prerequisites.
- **Graduation & Livelihood Missions:** Phased, multi-intervention pathways designed to pull households from extreme poverty to self-sufficiency.
- **Emergency / Disaster Relief:** Rapid-activation, short-lifecycle programs with relaxed geographic eligibility.
- **Sponsorship & NGO Grants:** Earmarked, 1:1 conceptual mapping of donors to cohorts.
- **CSR / Foundation Initiatives:** Corporate social responsibility initiatives with strict annual reporting and compliance checkpoints.

## 5. Humanitarian Principles
- **Impartiality:** Eligibility criteria must be transparent and uniformly applied.
- **Accountability to Affected Populations (AAP):** Exception and appeal pathways must exist to challenge exclusion.
- **Continuity of Care (Do No Harm):** Programs must model transition and successor pathways so that defunding does not abandon enrolled beneficiaries abruptly.

## 6. Open Architectural Decisions
- **Intervention Taxonomy Ownership:** Currently placed in Registration, the `support-interventions` taxonomy architecturally belongs to Programs.
