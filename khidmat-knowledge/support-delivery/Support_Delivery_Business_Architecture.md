# Support Delivery Business Architecture

**Status:** Draft / Business Architecture Freeze Pending
**Domain:** Support Delivery
**Purpose:** This document is the definitive statement of the business architecture for the Support Delivery domain within the Khidmat Humanitarian Operating System. It defines the concepts, actors, lifecycles, and principles the domain governs. It is purely conceptual and implementation-independent.

---

## 1. What is Support Delivery?
Support Delivery is the operational tip of the spear in the Khidmat ecosystem. It bridges the gap between an approved, abstract Case Plan (which dictates *what* is needed) and the real-world handover to a vulnerable human being. It models the logistics, constraints, attempts, proofs, and accountability loops required to safely, fairly, and securely execute assistance.

## 2. What it Owns
Support Delivery owns the *execution* of assistance. This includes:
- **Delivery Events & Windows:** The grouping, timing, scheduling, and occurrence of a delivery.
- **Delivery Modalities:** The physical, financial, or service form the delivery takes.
- **Delivery States & Attempts:** The lifecycle from dispatch to successful or failed handover.
- **Delivery Constraints & Safeguards:** Requirements enforcing dignity, safety, accessibility, and operational viability.
- **Delivery Quality & Observations:** Assessment of the goods provided and observations of the environment during delivery.
- **Proof of Delivery (PoD):** Evidence collected during the handover.
- **Exceptions, Failures & Escalations:** Managing operational friction and escalating severe issues.
- **Chain of Custody:** The sequence of transfers before reaching the beneficiary.
- **Accountability Loops:** Beneficiary confirmation, operational feedback, and protected grievances.

## 3. What it Never Owns
- **Needs & Eligibility:** The decision of *who* deserves *what* belongs entirely to Needs Assessment and Case Management.
- **Proxy Authorization Rules:** The definition of who can act as a proxy belongs to Registration. Support Delivery only executes the check.
- **Volunteer Profiles:** Tracking volunteer capability belongs to Volunteer Operations.
- **Impact Measurement:** Determining if the delivery actually resolved the underlying vulnerability belongs to Impact/Outcomes.

## 4. Delivery Modalities
Assistance takes different forms, each with unique execution mechanics:
- **Physical Goods:** Tangible items (food, blankets). Requires physical logistics, transport, and physical proof.
- **Digital Cash / Vouchers:** Financial instruments transferred via digital means. Delivery is a digital API call; proof is a telecom receipt.
- **Physical Cash / Vouchers:** Handover of paper money or tokens. Requires high-security chain of custody.
- **Services:** Intangible assistance. Support Delivery distinguishes between profoundly different service types:
  - *Medical:* Requires clinical privacy, bio-waste protocols, and specialized professional agents.
  - *Education:* Requires longitudinal attendance tracking and child-safe environments.
  - *Livelihood:* Requires asset verification and skills assessment follow-ups.
  - *Protection / Legal / Psychosocial:* Requires extreme privacy, anonymized handovers, and highly sensitive proof collection (often bypassing traditional signatures).

## 5. Compound Assistance
A single Delivery Event is rarely one isolated item. It frequently involves **Compound Assistance**, packaging multiple components—such as food, cash, a fuel voucher, and a referral for a medical checkup—into one synchronized event. Support Delivery orchestrates the handover of this entire bundle, allowing Case Management to resolve multiple planned interventions through one logistical effort.

## 6. Delivery Actors
- **Delivery Agent:** The volunteer, staff member, or digital system executing the handover.
- **Beneficiary:** The primary intended recipient.
- **Proxy / Guardian:** An authorized representative receiving assistance on behalf of the beneficiary.
- **Community Representative:** A local leader receiving community-level assets.
- **Custodians:** Intermediate handlers in the chain of custody.

## 7. Delivery Events and Windows
A **Delivery Event** is the fundamental unit of execution. To succeed, events must occur within valid **Delivery Windows**. These encompass:
- **Appointment Windows:** Mutually agreed times for handover.
- **Safe Access Windows:** Timeframes when conflict zones or hostile areas are momentarily safe.
- **Curfews & Weather Constraints:** Legal or environmental boundaries (e.g., stopping deliveries before monsoon rains or nighttime curfews).
- **Seasonal Constraints:** Broader windows dictating when certain assistance (e.g., winterization kits) must be delivered to be effective.

## 8. Delivery States
The macro lifecycle of a delivery:
- **Planned / Grouped:** Event is structured, constraints applied.
- **Dispatched:** Assistance has left the origin and entered the chain of custody.
- **Arrived:** Agent is on-site.
- **Handover Attempted:** The interaction has begun.
- **Delivered:** Handover is complete, and Proof of Delivery is secured.
- **Failed:** The delivery could not be completed and is aborted.
- **Returned:** Physical items have been returned to origin following a failure.

## 9. Delivery Constraints & Safeguarding
Operational rules prioritizing safety, dignity, and viability:
- **Child Safeguarding:** Handovers to or around unaccompanied minors require vetted personnel, specific witness protocols, and strict avoidance of exploitative conditions.
- **Accessibility & Inclusion:** Deliveries must adapt to disability, language, and cultural norms. A delivery fails its humanitarian mandate if a disabled beneficiary cannot physically access the distribution point, or if the interaction violates cultural privacy norms.
- **Protection Constraints:** E.g., `requires_unbranded_vehicle` or `anonymized_handover` (for extreme risk cases).

## 10. Humanitarian Principles During Delivery
The global principles of humanitarianism strictly constrain *how* Support Delivery operates:
- **Humanity & Dignity:** Deliveries must alleviate suffering without publicly shaming or stigmatizing the recipient.
- **Neutrality & Impartiality:** Distribution points must not be located in partisan facilities. Delivery agents must not condition handover on political, religious, or sectarian affiliation.
- **Independence:** The delivery chain of custody must remain free from control by armed or political actors. If an armed group demands control of the goods, the delivery is compromised.

## 11. Operational Observations & Escalation Triggers
Delivery agents are often the only human contact a beneficiary receives. 
- **Operational Observations:** If an agent observes abuse, severe malnutrition, or a cholera outbreak during a delivery, Support Delivery *records* the observation but does *not* assess the need or author a new Case Plan.
- **Escalation Triggers:** These observations, or severe operational failures (like a hostile crowd), trigger immediate escalations to:
  - *Needs Assessment* (for newly discovered vulnerabilities).
  - *Case Management* (for reassessment of the current plan).
  - *Protection* (for immediate safeguarding threats).
  - *Verification* (for suspected fraud or identity mismatch).

## 12. Delivery Exceptions & Quality
The specific reasons for failure or friction:
- **Beneficiary Exceptions:** `beneficiary_unavailable`, `refused_assistance`, `proxy_unauthorized`.
- **Operational Exceptions:** `safety_incident` (hostile environment), `roadblock`.
- **Quality Exceptions:** Assessment at the moment of handover, such as `damaged_goods`, `cold_chain_broken`, or `culturally_inappropriate` assistance.

## 13. Proof of Delivery (PoD) Concepts
Evidence that the handover occurred.
- **Types of Proof:** `signature`, `thumbprint`, `photograph`, `pin_code`, `api_receipt`, `community_attestation`.
- **Proof Quality:** The evaluation of the evidence (e.g., flagged for `blurry_photo`, `illegible_signature`, or `worn_fingerprint_biometric_failure`).

## 14. Accountability: Grievances vs. Feedback
- **Operational Feedback:** Routine beneficiary input on the delivery process (e.g., "the wait was too long" or "the food arrived late"). Handled within standard operational tuning.
- **Complaints:** Formal expressions of dissatisfaction regarding the quality or appropriateness of the assistance.
- **Protected Grievances:** Severe allegations (e.g., the volunteer demanded a bribe, or harassment occurred). These bypass standard Support Delivery reporting and enter a secure, anonymized protection lifecycle.

## 15. Delivery Metrics
To evaluate the health of the delivery network, Support Delivery tracks conceptual operational metrics:
- **Fulfillment:** Percentage of the Case Plan actually handed over.
- **Timeliness & Delay:** Adherence to the scheduled Delivery Windows.
- **Completion vs. Refusal:** Rates of successful handovers versus beneficiary rejections.
- **Spoilage:** Rates of quality exceptions (e.g., broken cold chains).

## 16. Cross-Domain Dependencies
- **Needs Assessment / Case Management:** Upstream source of truth for the need.
- **Registration:** Upstream source of truth for identity and proxy mapping.
- **Volunteer Operations:** Upstream source for delivery agent matching.
- **Impact / Outcomes:** Downstream consumer of the delivery success signal.

## 17. Operational Patterns
- **Hub-and-Spoke Distribution:** Multi-hop custody transfers before final handover.
- **Direct-to-Household:** High privacy, single custody transfer.
- **Group Aggregation:** Beneficiaries gather at a distribution point.
- **Digital Fulfillment:** Instantaneous transfer via API.

## 18. Business Rules
- Support Delivery logs *actual* quantities delivered (Partial Fulfillment). Case Management determines if the remaining deficit warrants a new event.
- Chain of Custody is strictly enforced for physical goods; every transfer between custodians requires a state update.
- Proof of Delivery is mandatory for transition to `Delivered`, but the *type* of proof is context-dependent (e.g., photos may be forbidden in certain cultural contexts).

## 19. Known Edge Cases
- **Post-mortem Delivery:** Beneficiary dies between planning and delivery.
- **Spontaneous Proxies:** An unregistered neighbor attempts to accept delivery for a hospitalized beneficiary.
- **Coerced Handovers:** Volunteer completes handover but under duress.

## 20. Unresolved Architectural Decisions
- **Multi-Beneficiary Resolution Logic:** How a single physical handover (e.g., 1 large food box to a household) technically resolves multiple individual Case Plans without emitting duplicate delivery events in the graph.

---

## Final Review Criteria

### 1. Scope
The Support Delivery domain completely maps the operational execution of humanitarian assistance, covering logistics, handover, constraints, observations, safeguarding, and accountability.

### 2. Out of Scope
Warehousing, macro-level supply chain management, fleet tracking, and automated fraud-detection algorithms. The knowledge layer tracks the *events and facts*, not the realtime telemetry of trucks. Needs assessment and case planning remain strictly out of scope.

### 3. Delivered Today
- Basic Delivery Event and Attempt tracking.
- Baseline Modalities (Physical, Cash, Service).
- High-level relationships to Case Plans and Volunteers.

### 4. Planned (V1 Finalization)
- Granular taxonomy for Exceptions, Constraints, and Proof Quality.
- Chain of Custody (CustodyTransfer modeling).
- Observations, Escalation Triggers, and Protected Grievances.

### 5. Future V2
- Full reverse logistics / returns integration with inventory systems.
- Offline-first runtime synchronization models.

### 6. Open Architectural Decisions
- Mechanism for linking a single `DeliveryEvent` or `Handover` to a Household/Community entity to implicitly resolve multiple individual Case Plans, avoiding graph duplication.
