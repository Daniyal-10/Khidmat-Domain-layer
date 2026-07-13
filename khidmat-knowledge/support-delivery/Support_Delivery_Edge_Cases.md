# Support Delivery: Edge Cases

- **Post-mortem Delivery**: Beneficiary has died between Case Plan approval and delivery arrival. (Exception: `BeneficiaryDeceased`).
- **Nomadic Relocation**: Beneficiary household has moved to a new informal settlement. (Exception: `BeneficiaryRelocated` -> triggers Registration update).
- **Quality Refusal**: Beneficiary refuses food parcel because it contains culturally inappropriate items not caught during planning. (Exception: `CulturallyInappropriate`).
- **Coerced Handover**: Volunteer completes handover but flags it under duress (e.g., armed actor demanded the goods). (Exception: `CoercedHandover`).
- **Biometric Failure**: Beneficiary is present but their fingerprints are worn from manual labor, failing biometric Proof of Delivery.
