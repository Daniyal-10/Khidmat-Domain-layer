# Beneficiary Lifecycle — Engagement Stage Semantics

**Purpose**: This document provides the explicit semantic boundaries and rules for each `engagement_stage` in the Beneficiary Lifecycle taxonomy. It is the authoritative reference for future reasoning, validation, and AI agents.

## 1. identified
*   **Business Meaning**: First contact made; formal registration has not begun.
*   **Entry Criteria**: A record is created via outreach, informal lead, or initial contact.
*   **Exit Criteria**: The subject begins providing formal data for registration.
*   **Typical Transition Triggers**: Lead creation, initial outreach event.
*   **Referenced Bounded Contexts**: Intake/Leads.
*   **Does NOT mean**: That the subject has requested aid or is eligible for anything.

## 2. registration_initiated
*   **Business Meaning**: Data collection is underway.
*   **Entry Criteria**: A formal registration conversation starts.
*   **Exit Criteria**: The registration conversation is completed and a case is created.
*   **Typical Transition Triggers**: Registration started event.
*   **Referenced Bounded Contexts**: Registration.
*   **Does NOT mean**: That the registration data is verified or complete.

## 3. registered
*   **Business Meaning**: Registration data is complete; awaiting formal verification.
*   **Entry Criteria**: The Registration domain marks the case as complete.
*   **Exit Criteria**: Verification activity begins.
*   **Typical Transition Triggers**: `registration/case` submitted.
*   **Referenced Bounded Contexts**: Registration, Verification Operations.
*   **Does NOT mean**: That the subject is eligible for aid. Registration is merely a collection of claims.

## 4. verification_pending
*   **Business Meaning**: Identity or eligibility claims actively being verified.
*   **Entry Criteria**: Verification Operations initiates field or desk review.
*   **Exit Criteria**: Verification Operations issues a final finding.
*   **Typical Transition Triggers**: `verification_activity` started.
*   **Referenced Bounded Contexts**: Verification Operations.
*   **Does NOT mean**: The subject is approved or rejected yet.

## 5. active
*   **Business Meaning**: Fully verified and in good standing, eligible for assessment or enrollment.
*   **Entry Criteria**: Verification successfully validates claims without safety/fraud blocks.
*   **Exit Criteria**: Subject is engaged in a program, suspended, or exited.
*   **Typical Transition Triggers**: Positive `verification_finding`.
*   **Referenced Bounded Contexts**: Verification Operations.
*   **Does NOT mean**: That the subject is receiving aid. It only represents eligibility and good standing.

## 6. engaged
*   **Business Meaning**: The subject is actively engaged with one or more humanitarian services, programs, or interventions within the Khidmat ecosystem.
*   **Entry Criteria**: Admission into a program, receipt of an emergency package, or active medical referral.
*   **Exit Criteria**: The intervention or program completes, or the subject drops out.
*   **Typical Transition Triggers**: Program enrollment event, intervention delivered event.
*   **Referenced Bounded Contexts**: Programs, Support Delivery.
*   **Does NOT mean**: Program enrollment, financial assistance, material aid, or specific delivery mechanisms. It is a neutral, macro-level state representing interaction, decoupled from how the aid is delivered.

## 7. monitored
*   **Business Meaning**: Active intervention has ended; being monitored for sustainability or impact.
*   **Entry Criteria**: Program graduation or intervention completion.
*   **Exit Criteria**: The monitoring period ends, or a new risk triggers re-engagement.
*   **Typical Transition Triggers**: Program completion, outcome measurement start.
*   **Referenced Bounded Contexts**: Outcome Measurement.
*   **Does NOT mean**: That the subject is receiving ongoing aid.

## 8. suspended
*   **Business Meaning**: Ecosystem engagement is paused, often due to a flagged risk.
*   **Entry Criteria**: A risk threshold is exceeded, or compliance data is missing.
*   **Exit Criteria**: The block is resolved, or the subject is moved to review/exited.
*   **Typical Transition Triggers**: `shared-risk/risk_characterization` threshold breached, compliance failure.
*   **Referenced Bounded Contexts**: Shared Risk, Governance.
*   **Does NOT mean**: That the subject is permanently removed.

## 9. review_required
*   **Business Meaning**: Triggered by inactivity or alerts; pending a human decision on continuation vs. exit.
*   **Entry Criteria**: Prolonged inactivity or systemic alerts require manual review.
*   **Exit Criteria**: A human makes a formal decision to exit or reinstate the subject.
*   **Typical Transition Triggers**: Inactivity timer, recurring suspensions.
*   **Referenced Bounded Contexts**: Case Management.
*   **Does NOT mean**: Automated exit. It enforces a manual review checkpoint.

## 10. exited
*   **Business Meaning**: Relationship concluded manually (e.g., graduation, permanent relocation).
*   **Entry Criteria**: A human formally approves an `exit_reason`.
*   **Exit Criteria**: Terminal state (unless a brand new lifecycle is initiated later).
*   **Typical Transition Triggers**: Manual case decision.
*   **Referenced Bounded Contexts**: Case Management.
*   **Does NOT mean**: Data deletion or archiving. It merely ends the semantic humanitarian journey.
