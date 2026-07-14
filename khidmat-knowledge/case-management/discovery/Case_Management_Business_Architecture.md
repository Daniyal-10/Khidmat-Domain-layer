# Case Management Business Architecture

## 1. Core Operating Model
Case Management models the reality of humanitarian and welfare coordination. It handles the complexity of decentralized, multi-agency efforts spanning variable timelines, ensuring that assessed needs translate into structured, trackable objectives.

## 2. Authority and Ownership (Delegated Authority)
Authority in Case Management is split to reflect humanitarian reality:
- **Statutory Authority (Legal Custody):** The entity legally responsible (e.g., Child Welfare Committee, Court, District Magistrate, UNHCR).
- **Operational Authority (Executing Agency):** The entity executing the plan (e.g., an NGO, a local social worker).
- **Transfers and Revocations:** Statutory owners can delegate Operational Authority to an NGO. This delegation can be temporarily suspended, transferred (Handoff), or revoked entirely. If an NGO loses funding or mandate, Operational Authority returns to the Statutory Owner or is reassigned.

## 3. The Case Conference
A Case Conference is not just a meeting; it is a critical coordination event for multi-disciplinary cases (e.g., Child Protection involving Police, NGO, Medical, and Legal).
- **Role:** It produces binding Decisions, reassigns responsibilities, and modifies the Case Plan.
- **Participants:** Includes internal caseworkers, external agencies, and sometimes the beneficiary.
- **Architecture:** Modeled as a Value Object or Event attached to the Case Timeline, producing Runtime Objects (Decisions/Recommendations) that update the Case Plan.

## 4. Timeline Reality
Humanitarian cases span wildly different time horizons:
- **1-Day Case:** Emergency stabilization (e.g., immediate shelter placement).
- **3-Year Case:** Livelihood rehabilitation.
- **20-Year Case:** Orphan care or refugee settlement.
- **Lifecycle States:** Cases use states to handle time gracefully: `Active`, `Paused` (awaiting external action), `Suspended` (funding dried up, or beneficiary hospitalized), `Administratively Closed` (lost contact, refused service), `Graduated` (objectives met), and `Reopened` (crisis returned).

## 5. Funding Reality
Case Management operates under resource constraints, but *does not own the funding logic*.
- **The Programs Boundary:** The Programs domain owns "Grants", "Donor Restrictions", and "Budgets".
- **Case Impact:** A Case Plan may be *partially funded* or forced into *Suspension* due to funding exhaustion. The Case Plan references the Program it relies on. If the Program ends, the Case must either find a new Program, refer out, or Suspend.

## 6. India Context Readiness
The architecture intrinsically supports the Indian welfare ecosystem by avoiding hardcoded terms:
- *Statutory Owner* maps cleanly to "District Magistrate" or "CWC".
- *Operational Owner* maps to "Implementing NGO" or "Anganwadi Worker".
- *Multi-agency coordination* supports an ASHA (health), Panchayat Secretary (admin), and NGO (livelihood) collaborating on a single Household Case.
