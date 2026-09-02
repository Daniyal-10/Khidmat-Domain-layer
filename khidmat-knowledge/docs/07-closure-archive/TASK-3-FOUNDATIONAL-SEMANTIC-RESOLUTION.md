# TASK 3 — FOUNDATIONAL SEMANTIC RESOLUTION

## 1. Executive Summary
This resolution task audited and refined the foundational semantic boundaries of the Khidmat ontology prior to architecture. The investigation confirmed that the existing seven primitives are sufficient to express the necessary distinctions without over-engineering. Specific semantic clarifications were made to Occurrences to resolve temporal ambiguities. The ontology foundation is now stable, and the remaining limitations (e.g., giving-side depth, evidence taxonomies) are explicitly bounded as source-depth limitations rather than foundational defects.

## 2. Identity / Person / Record
*   **Finding:** The ontology must prevent conflating a real-world person with an administrative record, an identifier, a sameness claim, or the confidence in that claim.
*   **Evidence:** Reference Model §3.1 and Ground Truth findings (GT-P4, GT-OQ1) explicitly demand separating the "beneficiary card" (record) from the "person".
*   **Minimum sufficient treatment:** The existing ontology provides the structural basis for this boundary:
    *   **Person:** real-world Entity
    *   **Identifier / Reference:** means of referring to an Entity
    *   **Sameness Claim:** assertion that two references denote the same Entity
    *   **Epistemic Stance:** an agent's position/warrant/confidence regarding that Claim

    A *Person* is a distinct Entity from an administrative *Record/Case*. *Identifiers* are attributes or relations. The *sameness assertion* is a Claim, and the system's *Epistemic Stance* (P3) evaluates the warrant for that claim. No additional primitive is currently justified for Identity/Sameness.
*   **Primitive impact:** None. Existing primitives (P4, P3, P7) are sufficient. No new "Identity" primitive is currently justified.
*   **Layer impact:** None. Entities (L2) and Cognition (L7) accommodate this split.
*   **Final status:** RESOLVED. The semantic boundary is structurally established.

## 3. Occurrence / Event / State
*   **Examples tested:** Displacement, registration, assessment, assistance/delivery.
*   **Temporal finding:** An occurrence (like a delivery or a displacement journey) can have duration. Defining an occurrence strictly as an instantaneous "point in time" creates an artificial boundary where spanning events are forced into States. The true distinction is between something that *happens* (even over a bounded period) and something that *holds* as an ongoing condition.
*   **Minimum sufficient rule:** "Occurrence = something that happens, potentially over a bounded period. State = a condition that holds. An occurrence may establish, change, or end a state."
*   **Primitive impact:** P6 (Occurrence) definition updated to explicitly permit a "bounded period" rather than being restricted to an instantaneous "point in time".
*   **Layer impact:** Architecture Rule LCR-5 (Event completion rule) updated to specify an Event is complete once it has "finished happening", clarifying the temporal boundary with Layer 5 (States).
*   **Final status:** RESOLVED. Temporal coherence is achieved without introducing a complex process or episode ontology.

## 4. Reality / Claim / Evidence / Epistemic Stance
*   **Minimum semantic distinction:** The ontology must prevent confusing what exists (Reality) with what is asserted (Claim), what supports the assertion (Evidence), and the system's warrant for it (Epistemic Stance).
*   **Primitive impact:** None. The existing P3 (Epistemic Stance) separates the system's warrant from the first-order domain primitives modeling reality (P1, P4, P6).
*   **Layer impact:** None. Layer 7 (Cognition) quarantines Claims, Findings, and Confidence. The minimum sufficient interpretation is maintained:
    *   **Evidence artifact / evidence-bearing occurrence:** an Entity or Occurrence that may serve an evidential role
    *   **Evidential role:** a Relation connecting evidence to a Claim
    *   **Claim:** assertion about reality
    *   **Epistemic Stance:** agent's position regarding that Claim

    This distinguishes an evidence artifact or observation from its role in grounding a belief.
*   **Final status:** RESOLVED. The epistemic boundaries are semantically established.

## 5. Out-of-Scope Findings
*   **Support:** Sector/Modality/Phase dimensionality is sufficient; full taxonomy expansion is excluded.
*   **Coordination:** Layer 8 remains abstract shapes; executable workflow is explicitly deferred to architecture.
*   **Giving-side coverage:** Entities (Donors, Funds) are under-described in the Reference Model. This is accepted as a source-depth limitation, not an ontology defect.
*   **Evidence taxonomy:** Exhaustive evidence types (e.g., biometric, testimony) are deferred to implementation.
*   **CCR-7 (Dual-clock):** Remains UNRESOLVED and non-mandatory pending broader field evidence.

These items are NOT being remediated now because they do not threaten the semantic foundational integrity required to begin architecture; they are merely areas awaiting localized vocabulary or deeper empirical data.

## 6. Changes Made
*   `01-DOMAIN-PRIMITIVES.md`: Clarified P6 (Occurrence) to allow a "bounded period" rather than forcing it to be a strict point in time.
*   `04-ARCHITECTURE-RULES.md`: Updated LCR-5 (Event completion rule) to align with the revised P6 boundary (Events are complete when they "finish happening").

## 7. Remaining Foundational Risks
While material foundational ambiguities (specifically Event vs. State and Identity mapping) have been bounded using existing structures and rules, residual risks remain regarding the practical implementation of identity resolution mechanics and the depth of evidence taxonomies. These must be carefully managed during architectural design to ensure the conceptual boundaries hold in practice.

## 8. Final Ontology Assessment
**FOUNDATION STABLE — PROCEED TO FINAL BASELINE AUDIT**
