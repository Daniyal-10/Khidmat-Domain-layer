# Khidmat Knowledge Layer: Operational Scenario Validation Suite

## Purpose
This suite contains comprehensive operational scenarios designed to validate the Khidmat Knowledge Layer v1.0.0. The scenarios stress-test the ontology against realistic humanitarian operations, disaster response, social service cases, and Islamic humanitarian assistance (Zakat).

Each scenario evaluates whether the existing ontology, taxonomy, and reasoning capabilities can accurately represent complex, real-world NGO and humanitarian situations.

---

## 01 Registration

### Scenario ID: REG-COMPLEX-001
**Title:** Unaccompanied Minor in Cross-Border Displacement
**Category:** Complex / Edge Case

**Background:** 
A 12-year-old boy, Ahmad, arrives at a border reception center. He was separated from his parents during a sudden conflict escalation. He has no identity documents, only knows his father's first name, and claims his uncle might be in a neighboring city. He requires immediate registration for protection and tracing, but standard household creation fails because there is no adult Head of Household.

**Actors:** 
- Registration Officer
- Child Protection Specialist
- Ahmad (Beneficiary)

**Entities involved:** 
- `Individual`
- `Household` (Fragmented/Temporary)
- `IdentityDocument` (Missing)
- `Vulnerability` (Unaccompanied Minor)

**Relationships involved:** 
- `isMemberOf` (Unknown Household)
- `hasGuardian` (Missing/Unknown)
- `requiresService` (Family Tracing)

**Lifecycle stages:** 
- Registration (Pre-registration / Temporary)
- Escalation (Child Protection)

**Expected ontology usage:** 
- Canonical entities: `Beneficiary`, `VulnerabilityProfile`, `ProtectionCase`.

**Expected taxonomy usage:** 
- Age Group: Child (U18)
- Vulnerability: Unaccompanied and Separated Children (UASC)
- Registration Status: Temporary/Incomplete

**Reasoning expectations:** 
- Rule: IF Age < 18 AND Guardian == NULL -> TRIGGER Child Protection Escalation.
- Rule: IF IdentityDocument == NULL -> SET VerificationLevel = Level 0.

**Verification requirements:** 
- Biometric capture (if permitted by policy for minors) or physical description.
- Cross-referencing with missing persons database.

**Expected outcome:** 
- Creation of a provisional Individual record.
- Automatic creation of a Child Protection case without requiring a standard Household entity.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
The ontology requires a `Head of Household` for many standard processes. The concept of an `UnaccompaniedMinorHousehold` or a `ProvisionalIndividual` without a household structure is often missing in standard models. We need a `HouseholdStructure` taxonomy that explicitly includes `Unaccompanied Child` to bypass adult-mandatory constraints.

---

## 02 Verification

### Scenario ID: VER-FRAUD-002
**Title:** Conflicting Identity Declarations in Urban Refugee Setting
**Category:** Fraud / Multi-domain

**Background:** 
A woman registers for cash assistance using a provided national ID card. During biometric deduplication, her fingerprints match an existing record under a different name and age, registered in a different region two years ago. The new ID card appears genuine but conflicts with the legacy database.

**Actors:** 
- Verification Officer
- Anti-Fraud Unit

**Entities involved:** 
- `Individual`
- `IdentityDocument` (x2)
- `BiometricRecord`
- `VerificationEvent`

**Relationships involved:** 
- `assertsIdentity`
- `conflictsWith` (Identity A vs Identity B)

**Lifecycle stages:** 
- Verification
- Suspension
- Fraud Investigation

**Expected ontology usage:** 
- Canonical entities: `VerificationRecord`, `FraudFlag`, `IdentityClaim`.

**Expected taxonomy usage:** 
- Verification Status: Disputed
- Fraud Type: Identity Mismatch / Potential Duplicate

**Reasoning expectations:** 
- Rule: IF BiometricMatch == TRUE AND IDDocumentMatch == FALSE -> TRIGGER Fraud Alert AND SET Status = Suspended.

**Verification requirements:** 
- Manual review by Anti-Fraud Unit.
- Contacting issuing authority of the ID card.

**Expected outcome:** 
- Both profiles linked via a `PotentialDuplicate` relationship.
- Cash assistance suspended pending resolution.

**Can the current Knowledge Layer represent this scenario?** 
YES

---

## 03 Needs Assessment

### Scenario ID: NA-MULTI-003
**Title:** Intersecting Vulnerabilities in Post-Earthquake Shelter
**Category:** Complex / Multi-domain

**Background:** 
Following an earthquake, an assessment team visits a temporary tent. Inside is a household of 6: a widowed mother, a grandfather with physical disabilities (wheelchair-bound), and four children, one of whom has severe asthma aggravated by dust. They need shelter, specialized health support, and mobility assistance.

**Actors:** 
- Field Assessor
- Health Specialist

**Entities involved:** 
- `Household`
- `Need` (Shelter, Health, WASH)
- `Assessment`

**Relationships involved:** 
- `hasNeed` (Multiple)
- `aggravatesNeed` (Environment -> Asthma)

**Lifecycle stages:** 
- Needs Assessment
- Prioritization

**Expected ontology usage:** 
- Canonical entities: `AssessmentForm`, `VulnerabilityIndicator`, `NeedScore`.

**Expected taxonomy usage:** 
- Vulnerability: Female-Headed Household, Elderly with Disability, Chronic Illness.
- Sector Needs: Shelter, Health.

**Reasoning expectations:** 
- Rule: Aggregate household vulnerability score based on sum of individual vulnerabilities.
- Rule: IF Need == Mobility AND Environment == Temporary Tent -> SET Priority = Critical.

**Verification requirements:** 
- Visual verification of living conditions and medical records for asthma.

**Expected outcome:** 
- A multi-sectoral need profile generated with a highly prioritized vulnerability score.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
The ontology generally handles individual needs well, but the relationship `aggravatesNeed` (e.g., environmental conditions exacerbating a health condition) is rarely modeled explicitly. The interaction between shelter context and health vulnerability needs a `ContextualRisk` entity.

---

## 04 Case Management

### Scenario ID: CM-LIFE-004
**Title:** Escalation and Transfer of Gender-Based Violence (GBV) Case
**Category:** Lifecycle / Exception

**Background:** 
A routine livelihood case manager notices signs of domestic abuse. The beneficiary discloses the abuse but requests extreme confidentiality. The livelihood case must remain open, but a separate, highly restricted GBV case must be opened and transferred to a specialized protection NGO, without the main household members knowing.

**Actors:** 
- Livelihood Case Worker
- GBV Specialist (External NGO)

**Entities involved:** 
- `Case` (Livelihood)
- `Case` (Protection/GBV)
- `ConsentForm`
- `DataMaskingPolicy`

**Relationships involved:** 
- `hasRelatedCase` (Hidden)
- `referredTo` (External Agency)

**Lifecycle stages:** 
- Case Creation
- External Referral
- Confidentiality Lock

**Expected ontology usage:** 
- Canonical entities: `Referral`, `CaseNote` (Restricted), `ConsentAgreement`.

**Expected taxonomy usage:** 
- Case Type: GBV Protection
- Security Level: Red / Highly Restricted

**Reasoning expectations:** 
- Rule: IF CaseType == GBV -> ENFORCE Strict Access Control (Only assigned specialist).
- Rule: IF Actor != AssignedSpecialist -> HIDE Case from Beneficiary Timeline.

**Verification requirements:** 
- Beneficiary verbal consent for external referral.

**Expected outcome:** 
- Two concurrent cases for the same individual with entirely different access control matrices.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
Current governance models usually apply access control at the `Role` level, not the `Case Instance` level combined with `Beneficiary Relationship`. The ontology needs a `ConfidentialityBoundary` concept that masks the existence of the Protection Case from the Livelihood Case Worker and Household Head.

---

## 05 Programs

### Scenario ID: PROG-NORM-005
**Title:** Graduation from Cash-for-Work to Micro-Enterprise
**Category:** Normal / Lifecycle

**Background:** 
A beneficiary successfully completes a 6-month Cash-for-Work (CfW) program. Upon completion, they qualify for a micro-enterprise grant. The transition requires closing the CfW enrollment and initiating a new grant program enrollment, transferring their compliance and attendance history as proof of qualification.

**Actors:** 
- Program Manager
- Livelihood Officer

**Entities involved:** 
- `Program` (CfW)
- `Program` (Micro-Enterprise)
- `Enrollment` (x2)
- `Milestone`

**Relationships involved:** 
- `prerequisiteFor`
- `graduatedFrom`

**Lifecycle stages:** 
- Program Completion
- New Enrollment

**Expected ontology usage:** 
- Canonical entities: `ProgramEnrollment`, `CompletionCertificate`, `EligibilityCriteria`.

**Expected taxonomy usage:** 
- Program Status: Completed, Active
- Intervention Type: Livelihood

**Reasoning expectations:** 
- Rule: IF Program A Status == Completed AND Attendance > 90% -> SET Program B Eligibility = TRUE.

**Verification requirements:** 
- Attendance logs and final project completion report.

**Expected outcome:** 
- Seamless transition of beneficiary between programs with historical linkage.

**Can the current Knowledge Layer represent this scenario?** 
YES

---

## 06 Support Delivery

### Scenario ID: DEL-EDGE-006
**Title:** Failed Delivery due to Geopolitical Blockade
**Category:** Edge / Exception

**Background:** 
A convoy carrying winterization kits is scheduled for delivery to a besieged community. Due to a sudden military blockade, the delivery fails. The goods are returned to the warehouse, but some perishable medical supplies in the convoy expire. Beneficiary statuses must be updated from "Scheduled" to "Pending - Blocked", and inventory must reflect the expired goods.

**Actors:** 
- Logistics Coordinator
- Field Distributor

**Entities involved:** 
- `DeliveryBatch`
- `InventoryItem`
- `Location`
- `DistributionPlan`

**Relationships involved:** 
- `allocatedTo`
- `preventedBy` (Blockade)

**Lifecycle stages:** 
- Dispatch
- Failed Delivery
- Inventory Reconciliation

**Expected ontology usage:** 
- Canonical entities: `DispatchRecord`, `ExceptionReport`, `InventoryWriteOff`.

**Expected taxonomy usage:** 
- Delivery Status: Failed (Force Majeure)
- Inventory Status: Damaged/Expired

**Reasoning expectations:** 
- Rule: IF DeliveryStatus == Failed -> REVERT Beneficiary Entitlement Status AND TRIGGER Rescheduling.

**Verification requirements:** 
- Incident report from convoy leader.

**Expected outcome:** 
- Beneficiaries remain eligible for the next cycle. Inventory is correctly reconciled.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
The ontology likely models `Delivery` success and failure, but the concept of `ForceMajeureEvent` preventing a `DistributionPlan` and triggering automated rollbacks on `Entitlement` and `Inventory` simultaneously requires complex event-driven reasoning often missing in static ontologies.

---

## 07 Impact

### Scenario ID: IMP-COMPLEX-007
**Title:** Longitudinal Educational Impact Tracking
**Category:** Complex / Lifecycle

**Background:** 
An NGO tracks the impact of a girls' education program over 5 years. They measure attendance, standardized test scores, and community attitudes towards female education. The challenge is attributing the change in test scores directly to the NGO's program vs. general macroeconomic improvements in the region.

**Actors:** 
- M&E Officer
- Data Analyst

**Entities involved:** 
- `Indicator` (Attendance, Test Scores)
- `ImpactMeasurement`
- `Baseline`
- `ExternalFactor`

**Relationships involved:** 
- `measuredAgainst`
- `influencedBy`

**Lifecycle stages:** 
- Baseline Assessment
- Midline Assessment
- Endline Evaluation

**Expected ontology usage:** 
- Canonical entities: `LogFrame`, `IndicatorValue`, `EvaluationReport`.

**Expected taxonomy usage:** 
- Evaluation Type: Longitudinal
- Sector: Education

**Reasoning expectations:** 
- Rule: Calculate delta between Baseline and current Measurement for specified Indicator.

**Verification requirements:** 
- School transcripts, surveys.

**Expected outcome:** 
- A comprehensive impact report linking interventions to long-term outcomes.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
Standard models track `Indicators` and `Measurements`, but modeling `ExternalFactors` (confounding variables) and attribution logic (`influencedBy`) in an ontology requires a highly sophisticated Causal Model which is typically outside basic M&E layers.

---

## 08 Community

### Scenario ID: COM-NORM-008
**Title:** Community Committee Resource Allocation
**Category:** Normal / Multi-domain

**Background:** 
A local Water, Sanitation, and Hygiene (WASH) committee in a rural village is formed. The NGO provides a grant to the committee, not an individual. The committee is responsible for building a well. The community entity itself is the beneficiary.

**Actors:** 
- Community Mobilizer
- Committee Chairman

**Entities involved:** 
- `CommunityGroup`
- `Grant`
- `Project`

**Relationships involved:** 
- `actsOnBehalfOf` (Village)
- `manages` (Well Project)

**Lifecycle stages:** 
- Group Formation
- Grant Disbursement
- Project Execution

**Expected ontology usage:** 
- Canonical entities: `CommunityEntity`, `CommitteeMember`, `CommunityProject`.

**Expected taxonomy usage:** 
- Beneficiary Type: Community/Group
- Intervention: WASH

**Reasoning expectations:** 
- Rule: IF BeneficiaryType == CommunityGroup -> BYPASS Individual Vulnerability Scoring.

**Verification requirements:** 
- Committee meeting minutes, signatures of members.

**Expected outcome:** 
- Grant disbursed to a collective entity, tracked through group milestones.

**Can the current Knowledge Layer represent this scenario?** 
YES

---

## 09 Volunteers

### Scenario ID: VOL-EDGE-009
**Title:** Spontaneous Volunteer Integration during Flash Flood
**Category:** Edge / Disaster Operations

**Background:** 
During a sudden flash flood, 50 local civilians show up to help distribute sandbags. They are not registered in the NGO system, have no background checks, and are operating in a high-risk environment. The NGO needs to rapidly register them as "Spontaneous Volunteers", assign them to team leaders, and track their hours for insurance/liability purposes.

**Actors:** 
- Volunteer Coordinator
- Spontaneous Volunteer

**Entities involved:** 
- `Volunteer` (Spontaneous)
- `Shift`
- `LiabilityWaiver`
- `RiskZone`

**Relationships involved:** 
- `assignedTo` (Team Leader)
- `deployedIn` (Risk Zone)

**Lifecycle stages:** 
- Rapid Onboarding
- Deployment
- Demobilization

**Expected ontology usage:** 
- Canonical entities: `VolunteerProfile`, `DeploymentRoster`, `IncidentReport`.

**Expected taxonomy usage:** 
- Volunteer Type: Spontaneous / Unvetted
- Status: Active Emergency

**Reasoning expectations:** 
- Rule: IF VolunteerType == Spontaneous -> REQUIRE Digital Liability Waiver AND RESTRICT from vulnerable beneficiary contact (e.g., unaccompanied minors).

**Verification requirements:** 
- Basic identity capture (photo of ID), digital signature on waiver.

**Expected outcome:** 
- Rapid deployment of unvetted volunteers with strict operational boundaries.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
The constraint logic (`RESTRICT from vulnerable beneficiary contact`) based on a `Spontaneous` taxonomy classification requires a dynamic capability-based access model linked directly to the `Volunteer` entity, which is often missing.

---

## 10 Donors

### Scenario ID: DON-COMPLEX-010
**Title:** Restricted Multi-Donor Funding Pool
**Category:** Complex / Compliance

**Background:** 
A health clinic is funded by three donors: Donor A (funds only pediatric medicine, no overhead), Donor B (funds staff salaries, requires quarterly reporting), Donor C (unrestricted funds). A batch of medical supplies and a month of salaries are distributed. The system must allocate the financial expenditures precisely to the correct donor grants to ensure compliance.

**Actors:** 
- Grant Manager
- Finance Officer

**Entities involved:** 
- `Donor`
- `Grant` (Restricted vs Unrestricted)
- `Expenditure`
- `CostCenter`

**Relationships involved:** 
- `funds`
- `restrictedTo` (Sector/Item)

**Lifecycle stages:** 
- Expenditure Incurred
- Allocation
- Donor Reporting

**Expected ontology usage:** 
- Canonical entities: `FundingStream`, `BudgetLine`, `ExpenseTransaction`.

**Expected taxonomy usage:** 
- Funding Restriction: Sector-specific, Cost-category specific.

**Reasoning expectations:** 
- Rule: IF ExpenditureItem == Pediatric Medicine -> ALLOCATE TO Grant A first. IF Grant A depleted, ALLOCATE TO Grant C.

**Verification requirements:** 
- Invoices, Timesheets.

**Expected outcome:** 
- Accurate financial drawdown aligned with donor restrictions.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
While standard systems link Expenditures to Grants, automated cascading allocation logic based on item-level taxonomy constraints (e.g., "Pediatric Medicine" cascading from restricted to unrestricted pools) requires an advanced `FundAllocationEngine` in the reasoning layer.

---

## 11 Resources

### Scenario ID: RES-FRAUD-011
**Title:** Phantom Warehouse Inventory
**Category:** Fraud / Resources

**Background:** 
A warehouse manager creates fictitious "damaged goods" reports to write off solar panels, which are actually being sold on the black market. The system shows inventory depleting due to "Damage," but community reports show local markets flooded with NGO-branded solar panels.

**Actors:** 
- Warehouse Manager (Malicious)
- Auditor

**Entities involved:** 
- `InventoryItem`
- `WriteOffReport`
- `Warehouse`
- `AuditFlag`

**Relationships involved:** 
- `locatedIn`
- `writtenOffBy`

**Lifecycle stages:** 
- Inventory Management
- Anomaly Detection
- Investigation

**Expected ontology usage:** 
- Canonical entities: `StockTransaction`, `LossReport`, `AuditTrail`.

**Expected taxonomy usage:** 
- Loss Reason: Damaged
- Audit Status: Under Investigation

**Reasoning expectations:** 
- Rule: IF LossReason == Damaged AND ItemValue > Threshold AND Frequency > Normal -> TRIGGER Anomalous Loss Alert.

**Verification requirements:** 
- Physical surprise audit.

**Expected outcome:** 
- System flags high-value, high-frequency write-offs for review.

**Can the current Knowledge Layer represent this scenario?** 
NO

**If PARTIALLY or NO:** 
The Knowledge Layer currently lacks an `AnomalyDetectionModel` for inventory. We have `WriteOffReports`, but no ontology for `BehavioralThresholds` or `FraudSignatures` related to resource depletion.

---

## 12 Cross-Domain Operations

### Scenario ID: CROSS-012
**Title:** Registration to Delivery in 24 Hours
**Category:** Normal / Multi-domain

**Background:** 
A new internally displaced persons (IDP) camp forms overnight. The NGO uses offline mobile tablets to register households, assess needs, approve cases, and issue e-vouchers. When the tablets sync the next day, the system must process Registration -> Assessment -> Case Approval -> Delivery Entitlement sequentially and instantly.

**Actors:** 
- Mobile Registration Team

**Entities involved:** 
- `Household`, `Assessment`, `Case`, `Entitlement`, `SyncEvent`

**Relationships involved:** 
- `triggers` (Sequential workflow)

**Lifecycle stages:** 
- Offline Capture
- Batch Sync
- Automated Provisioning

**Expected ontology usage:** 
- Canonical entities: `BatchImport`, `WorkflowTrigger`.

**Expected taxonomy usage:** 
- Sync Status: Pending, Processed.

**Reasoning expectations:** 
- Rule: UPON Sync -> Execute standard enrollment workflow bypassing manual approvals if EmergencyFlag == TRUE.

**Verification requirements:** 
- Data completeness checks post-sync.

**Expected outcome:** 
- Thousands of records processed across 5 domains without manual intervention.

**Can the current Knowledge Layer represent this scenario?** 
YES

---

## 13 Disaster Operations

### Scenario ID: DIS-EDGE-013
**Title:** Evolving Geographic Risk Zones
**Category:** Edge / Disaster

**Background:** 
A volcanic eruption creates lava flows that change daily. Beneficiaries are registered to specific villages. As the lava flow expands, the system must dynamically update the vulnerability status of households based on their geographic intersection with the updated "Red Zone" polygon.

**Actors:** 
- GIS Specialist
- Emergency Coordinator

**Entities involved:** 
- `GeoSpatialZone` (Red Zone)
- `HouseholdLocation`
- `RiskAlert`

**Relationships involved:** 
- `intersectsWith` (Spatial)
- `threatens`

**Lifecycle stages:** 
- Spatial Update
- Risk Reassessment
- Evacuation Order

**Expected ontology usage:** 
- Canonical entities: `GeoPolygon`, `HouseholdPoint`, `VulnerabilityModifier`.

**Expected taxonomy usage:** 
- Risk Level: Extreme, High, Safe.

**Reasoning expectations:** 
- Rule: IF HouseholdLocation INTERSECTS RedZonePolygon -> SET Status = Immediate Evacuation AND SEND SMS Alert.

**Verification requirements:** 
- Satellite imagery updates.

**Expected outcome:** 
- Automated, geographically-driven vulnerability updates.

**Can the current Knowledge Layer represent this scenario?** 
NO

**If PARTIALLY or NO:** 
The ontology does not natively support spatial reasoning (`intersectsWith`) or dynamic `GeoSpatialZone` entities out-of-the-box without a GIS extension. The core layer handles locations as static hierarchies (Country > Region > District), not dynamic polygons.

---

## 14 Protection Operations

### Scenario ID: PROT-EXC-014
**Title:** Witness Protection and Identity Obfuscation
**Category:** Exception / Protection

**Background:** 
A beneficiary is a witness to human trafficking in a refugee camp. They require support, but their real name, age, and location cannot exist in the standard database due to the risk of infiltration. They are given a pseudonym and generic location. The system must process their assistance delivery without breaking compliance rules regarding KYC (Know Your Customer).

**Actors:** 
- Protection Officer
- Compliance Officer

**Entities involved:** 
- `AliasProfile`
- `KYCWaiver`

**Relationships involved:** 
- `represents` (Hidden relationship to real identity, kept entirely offline or in a secure vault)

**Lifecycle stages:** 
- Obfuscated Registration
- Support Delivery

**Expected ontology usage:** 
- Canonical entities: `Alias`, `ExceptionApproval`.

**Expected taxonomy usage:** 
- Profile Type: Obfuscated/Protected.

**Reasoning expectations:** 
- Rule: IF ProfileType == Obfuscated -> BYPASS Standard Deduplication AND ALLOW Delivery without Biometrics.

**Verification requirements:** 
- Special offline authorization by Country Director.

**Expected outcome:** 
- Delivery of support without exposing the individual.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
The system requires a defined `ObfuscationProtocol` within the ontology to legally bypass KYC constraints. Normally, missing data triggers errors; here, it must be recognized as a deliberate and authorized state.

---

## 15 Zakat & Islamic Humanitarian Operations

### Scenario ID: ZAK-COMPLEX-015
**Title:** Strict Hawl and Nisab Qualification for Zakat Entitlement
**Category:** Complex / Zakat

**Background:** 
An organization distributes Zakat funds. A beneficiary applies for debt relief (Al-Gharimin). The assessment must verify that they do not possess wealth above the Nisab threshold, that their debt was not incurred for haram purposes, and the funds must be strictly segregated from Sadaqah (voluntary charity) pools.

**Actors:** 
- Zakat Assessor
- Shariah Compliance Officer

**Entities involved:** 
- `ZakatFund`
- `BeneficiaryWealth`
- `DebtRecord`

**Relationships involved:** 
- `qualifiesFor` (Asnaf category)
- `fundedBy` (Strict Zakat pool)

**Lifecycle stages:** 
- Shariah Assessment
- Disbursement

**Expected ontology usage:** 
- Canonical entities: `AsnafCategory`, `NisabThreshold`, `ZakatDisbursement`.

**Expected taxonomy usage:** 
- Asnaf: Al-Gharimin (The Debtors).
- Fund Type: Zakat (Restricted).

**Reasoning expectations:** 
- Rule: IF BeneficiaryWealth < Nisab AND DebtReason != Haram -> QUALIFY FOR Zakat Al-Gharimin.
- Rule: Zakat funds CANNOT be spent on operational overhead.

**Verification requirements:** 
- Review of debts and assets by a local committee.

**Expected outcome:** 
- Shariah-compliant disbursement of Zakat funds.

**Can the current Knowledge Layer represent this scenario?** 
YES

---

## 16 Fraud & Integrity

### Scenario ID: FRAUD-ORG-016
**Title:** Collusion Between Supplier and Field Staff
**Category:** Fraud / Complex

**Background:** 
A local food supplier and an NGO field officer collude. The supplier delivers 500 food parcels instead of the contracted 1000. The field officer falsifies the Goods Received Note (GRN) in the system to state 1000 were received. They split the profits of the 500 missing parcels. The anomaly is later detected when beneficiaries report receiving half-rations.

**Actors:** 
- Field Officer (Malicious)
- Supplier (Malicious)
- Beneficiary (Informant)

**Entities involved:** 
- `PurchaseOrder`
- `GoodsReceivedNote`
- `FeedbackTicket` (Complaint)

**Relationships involved:** 
- `contradicts` (Feedback vs GRN)

**Lifecycle stages:** 
- Procurement
- Receiving
- Feedback/Complaint
- Investigation

**Expected ontology usage:** 
- Canonical entities: `ComplaintMechanism`, `SupplierContract`, `AuditInvestigation`.

**Expected taxonomy usage:** 
- Complaint Type: Short-changing / Corruption.

**Reasoning expectations:** 
- Rule: IF Count(Complaints: Short-changing) > 5 AND Linked to Specific Supplier -> AUTOMATICALLY SUSPEND Supplier Contract AND FLAG Field Officer.

**Verification requirements:** 
- Beneficiary hotlines, independent audit of supplier logs.

**Expected outcome:** 
- Detection of systemic fraud via beneficiary feedback loop.

**Can the current Knowledge Layer represent this scenario?** 
PARTIALLY

**If PARTIALLY or NO:** 
The layer handles `Complaints` and `Contracts`, but the automated cross-entity reasoning rule (`contradicts`) linking beneficiary feedback directly to a supplier suspension is a complex multi-hop inference (`Beneficiary -> Distribution -> Warehouse -> GRN -> Supplier`) that requires specific graph traversal logic not present in base ontologies.

---

## 17 Rare & Extreme Edge Cases

### Scenario ID: EDGE-EXT-017
**Title:** Mass Statelessness / Border Shift
**Category:** Edge / Rare

**Background:** 
Following a treaty, a border is redrawn overnight. An entire camp of 20,000 beneficiaries goes from being "Internally Displaced Persons" (IDPs) in Country A to "Refugees" in Country B, without moving an inch. Their legal status, entitlement rights, and the governing donor compliance frameworks change instantaneously.

**Actors:** 
- Legal Advisor
- Database Administrator

**Entities involved:** 
- `LegalStatus`
- `Jurisdiction`
- `BeneficiaryProfile` (Bulk)

**Relationships involved:** 
- `subjectTo` (New Jurisdiction)

**Lifecycle stages:** 
- Legal Framework Shift
- Bulk Migration

**Expected ontology usage:** 
- Canonical entities: `LegalFramework`, `StatusTransitionBatch`.

**Expected taxonomy usage:** 
- Status Change: IDP -> Refugee.
- Geography: Country A -> Country B.

**Reasoning expectations:** 
- Rule: IF Location Jurisdiction Changes -> RE-EVALUATE all Entitlements based on New Jurisdiction Rules.

**Verification requirements:** 
- Official UN/Government decree.

**Expected outcome:** 
- A massive, automated recalculation of rights and legal status for 20,000 people without requiring individual reassessment.

**Can the current Knowledge Layer represent this scenario?** 
NO

**If PARTIALLY or NO:** 
Ontologies handle individual status changes well, but a "Jurisdictional Shift" that cascades a fundamental ontological state change (IDP to Refugee) across an entire geographic node requires `MacroEvent` modeling and bulk-recalculation rules that are highly specialized.
