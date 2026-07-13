# Repository Gap Report: Support Delivery

### Type A — Already Covered
- **Authorized Proxies & Guardians**: Handled by Registration's `family-structure` and proxy claims.
- **Referral Generation**: Case Management owns the decision to refer to an external partner.

### Type B — Belongs to Support Delivery
- **Complex Modalities**: The current taxonomy (`physical_goods`, `cash`, `service`) is too shallow. Needs breakdown into digital voucher, restricted cash, specialized medical service, legal service, etc.
- **Dignity & Protection Constraints**: The ontology needs a robust vocabulary for constraints like `requires_unbranded_vehicle`, `requires_anonymized_handover`, `gender_restricted_access`.
- **Proof of Delivery Depth**: Taxonomy of proof types (Signature, Thumbprint, Photo, PIN Code, Community Leader Attestation).
- **Delivery Exceptions**: Expanded taxonomy including `hostile_environment`, `goods_spoiled`, `beneficiary_relocated`, `proxy_unauthorized`.
- **Accountability Loop**: Formal tracking of beneficiary feedback regarding the delivery experience itself.

### Type C — Belongs to Existing Domain
- **New Need Triggers**: If a volunteer notices a sick child during a food delivery, this triggers a new Needs Assessment (belongs to NA/CM).

### Type D — Future Roadmap
- **Logistics & Warehousing**: Real-time fleet tracking, temperature logging sensors, warehouse inventory counts.
- **Fraud Detection Algorithms**: Automated flagging of suspicious proof patterns (e.g., identical signatures).

### Type E — Requires Architectural Decision
- **Multi-Beneficiary Resolution**: When 1 box of food is delivered to a household of 5, how does SD notify Case Management to close 5 distinct Case Plans? Does SD emit 5 handovers, or 1 handover with 5 `fulfills` edges?
