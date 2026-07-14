# Needs Assessment Repository Gap Report

## 1. Domain Ownership Friction
- **Verification vs. Assessment:** Currently, there is a risk of overlap with Verification Operations (referenced by Programs). If a Needs Assessment checks if a person is disabled, is that an Assessment or a Verification? 
  *Resolution Idea:* Assessment is the epistemological act of determining a need or vulnerability (e.g., "This person cannot walk"). Verification is the administrative act of confirming a claim against a legal standard (e.g., "This person has a valid government disability card"). Needs Assessment owns the former.

## 2. Missing Core Constructs
- **Algorithmic/AI Assessors:** As humanitarian contexts increasingly use AI or ML for Proxy Means Testing, the repository lacks a clear way to represent an algorithm as an `assessor`. 
- **Time-Decay of Need:** Needs expire. A critical need for water after a flood is not relevant 3 years later, even if no Support Delivery is recorded. We lack a standardized "Time-to-Live" (TTL) concept for Need Assertions.

## 3. Registration Dependencies
- Needs Assessment relies heavily on `shared_human:person` and `shared_human:household`. However, in emergency contexts, an assessment may happen on an unregistered group (e.g., assessing a crowd of IDPs). Can Needs Assessment attach to an "Unregistered Cohort" or must Registration create ghost records first? ADR-008 dictates Registration owns Identity. Thus, Registration must support rapid/ghost cohort creation for Needs Assessment to link against.

## 4. Case Management Dependencies
- Does a Needs Assessment automatically open a Case? The boundary must be strict: Needs Assessment outputs data; Case Management evaluates that data via rules to decide if a Case is warranted. Needs Assessment must not contain logic that forces a Case creation.
