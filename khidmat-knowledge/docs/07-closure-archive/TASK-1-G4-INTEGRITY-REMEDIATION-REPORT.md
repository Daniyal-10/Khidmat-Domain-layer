# TASK-1-G4-INTEGRITY-REMEDIATION-REPORT

## A. Scope
This remediation targeted Stage 7 Governance Decision G4 (`07-STAGE-7-GOVERNANCE-DECISIONS.md`) and its downstream references across the core ontology. The purpose was to ensure that governance decisions accommodating weak or single-source practitioner evidence (specifically concerning Need-Interactions, Service Providers, Outcome/Impact Ownership, Funder Altitude, and Case Orchestration) do not falsely present themselves as confirmed ontological truths or universal exclusions.

## B. Finding
G4 previously conflated a modeling accommodation with an ontological confirmation by using terms like "RESOLVED" and "ratified". Downstream files incorrectly hardened this into strong exclusions (e.g., claiming Need-to-Need interactions "are formally excluded as structural Relations. They exist solely as Cognition/documentation content"), thereby converting a lack of structural evidence into a negative domain claim. This misrepresented the true empirical weight of the single-source practitioner evidence.

## C. Evidence
- `docs/05-ontology/07-STAGE-7-GOVERNANCE-DECISIONS.md` (G4 entry)
- `docs/05-ontology/04-ARCHITECTURE-RULES.md` (Table entries for G4 items)
- `docs/05-ontology/02-ONTOLOGY-LAYERS.md` (Resolved tensions and specific layer notes)
- `docs/05-ontology/03-ONTOLOGY-PILLARS.md` (Pillar V and resolved tensions)
- `docs/05-ontology/GT-OQ16-R1.md` (Demonstrating single-source basis for Need-Interactions)

## D. Changes made
1. **`07-STAGE-7-GOVERNANCE-DECISIONS.md`**: Rewrote G4 to explicitly separate Governance decision, Ontological status (UNRESOLVED), and Evidence status (Weak/Single-source). Changed overall status from "RESOLVED" to "GOVERNED PROVISIONAL — single-source evidence acknowledged".
2. **`04-ARCHITECTURE-RULES.md`**: Updated the Need-interaction model from "Intentional Exclusion" to "Scope accommodation", explicitly stating that current evidence is insufficient to justify a formal relation type rather than denying its existence. Updated the status column for all five G4 items to "Governed provisional".
3. **`02-ONTOLOGY-LAYERS.md`**: Removed the strong exclusion ("should NOT be built") for Need Interactions and replaced all "Provisionally settled... ratified by Stage 7 G4" references across L2, L6, L8, and former open tensions with "Governed provisional — single-source practitioner evidence acknowledged by Stage 7 G4".
4. **`03-ONTOLOGY-PILLARS.md`**: Aligned wording in Pillar V and resolved tensions list, replacing "ratified" and exclusions with "Governed provisional" and cautious evidential accommodations.

## E. Status distinction
- **Governance decision**: What the project practically chooses to do for current modeling (e.g., treating Need-Interactions via Cognition/documentation).
- **Ontological status**: What the empirical evidence justifies asserting about the domain reality itself (currently UNRESOLVED for the G4 items, as they lack sufficient multi-source confirmation).
- **Evidence status**: The strength and corroboration of the supporting data (Weak/Single-source for the practitioner findings underlying G4).

## F. G4 final treatment
The final status of G4 and each of its five items (Need-Interactions, Service Providers, Outcome/Impact Ownership, Funder Altitude, Case Orchestration) is **GOVERNED PROVISIONAL — single-source evidence acknowledged**. The underlying domain propositions remain ontologically open.

## G. Non-changes
- No historical artifact (including `MERGED_BUSINESS_UNDERSTANDING.md` or files in `docs/07-closure-archive/`) was altered, preserving their historical accuracy.
- No new primitives were introduced, and no existing ones were removed.
- The 8 layers and 7 pillars were not redesigned.
- Downstream items not genuinely affected by the G4 conflation were not modified.

## H. Remaining uncertainty
The ontological nature of Need Interactions, Service Providers as independent active Entities, Funder Altitude, Case Orchestration, and Outcome/Impact Ownership remains unresolved. They are modeled provisionally based on current evidence but still require broader empirical corroboration from the field to either confirm or challenge these structures.

## I. Integrity verdict
PASS WITH RESIDUAL UNCERTAINTY
