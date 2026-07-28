# 16. Domain Dependencies and Boundaries

## Owns
- The rules of inter-agency context sharing.
- External referral tracking and handshakes.
- Deduplication protocols and conflict resolution rules.
- Organisational trust modeling.

## Consumes
- **From Case Management:** Verified identity claims, Support Plans, and explicit beneficiary consent to share data.
- **From Programme Management:** Organisational mandates and geographic coverage areas.

## Produces
- **For Case Management:** Deduplication alerts (warning that a Support Plan conflicts with another agency), and incoming external referrals.
- **For Programme Management:** Gap analysis data (showing which geographies are over/under-served by the broader ecosystem).

## Explicitly Out of Scope
- Assessing the vulnerability of the individual (Case Management).
- Determining an Organisation's internal eligibility rules (Programme Management).
- Commanding another Organisation to cease an intervention. (Coordination can warn of duplication, but cannot command cessation).
