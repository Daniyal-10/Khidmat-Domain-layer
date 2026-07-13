# Support Delivery: Business Scenarios

## Scenario 1: Protection-sensitive Handover
A domestic violence survivor requires cash assistance.
**Constraints**: Delivery must be unbranded, executed by a female volunteer, and handed over only to the primary beneficiary (no proxies).
**Failure Mode**: Male proxy demands the cash. Volunteer triggers `ProxyUnauthorized` exception.

## Scenario 2: Community Asset Delivery
Delivery of a communal water filtration system.
**Execution**: Delivered to a `CommunityRepresentative`. Fulfills the abstract need of the community rather than a specific individual's `CasePlan`.

## Scenario 3: Partial Fulfillment due to Looting
A truck carrying 100 food parcels is partially looted. 
**Execution**: 40 parcels are delivered. SD logs 40 successful handovers and 60 `SafetyIncident` exceptions. Case Management must recalculate remaining needs.

## Scenario 4: Medical Service Delivery
A mobile clinic visit.
**Execution**: The "delivery" is the consultation. Proof of delivery is the physician's log and the patient's signature. No physical goods change hands.
