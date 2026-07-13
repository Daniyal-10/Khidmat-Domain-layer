# Support Delivery: Operational Patterns

## Pattern 1: Hub and Spoke Distribution
Goods move from Central Depot -> Regional Hub -> Local Distribution Point -> Beneficiary. Each link requires a `CustodyTransfer` event before the final `PhysicalHandover`.

## Pattern 2: Direct-to-Household
Volunteer picks up goods and drives directly to the beneficiary's shelter. Single custody transfer, high privacy constraint.

## Pattern 3: Group Aggregation
Beneficiaries are called to a central Distribution Point on a specific day. High efficiency, low privacy. Proof of Delivery is often batched (e.g., a signed manifest sheet).

## Pattern 4: Digital Fulfillment
API integration triggers a mobile money transfer. The "Volunteer" is an automated system. Proof of Delivery is the telecom's API success receipt.
