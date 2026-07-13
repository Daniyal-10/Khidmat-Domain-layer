# Support Delivery Concept Inventory

| Concept | Classification | Notes/Why |
|---|---|---|
| Delivery Event / Attempt / Handover | Type B (Support Delivery) | Core execution concepts. |
| Group Deliveries & Batching | Type B (Support Delivery) | Logistical optimization (e.g., school feeding) executed by SD. |
| Multi-beneficiary Delivery | Type B (Support Delivery) | One handover event resolving multiple Case Plans. |
| Conditional Cash / Vouchers | Type B (Support Delivery) | Modalities requiring specific redemption workflows. |
| Proxy/Guardian Handover Rules | Type C (Registration) | Registration owns proxy definitions; SD simply executes the check. |
| Chain of Custody | Type B (Support Delivery) | Tracked as `CustodyTransfer` edges between `DeliveryEvent` stages. |
| Proof Quality (e.g. Thumbprint) | Type B (Support Delivery) | SD owns the evidence of handover. |
| Delivery Constraints (Safety, Dignity) | Type B (Support Delivery) | E.g., Unbranded vehicle, gender-matched volunteer. |
| Security Incidents (Roadblocks, Hostility) | Type B (Support Delivery) | Operational exceptions occurring during execution. |
| Humanitarian Principles (Dignity/Privacy) | Type A (Covered Elsewhere) | Handled by architectural blueprint; SD operationalizes them via constraints. |
| Referral Deliveries | Type C (Case Management) | Referrals are planned by CM; SD just tracks the external handover. |
| Reverse Logistics / Returns | Type D (Future Roadmap) | Tracking warehouse restocking is an inventory concern (V2). |
| Beneficiary Confirmation (Post-delivery) | Type B (Support Delivery) | The accountability loop checking satisfaction and dignity. |
| Unanticipated Needs Discovered at Delivery | Type C (Needs Assessment) | SD flags them, but NA owns the new need generation. |
