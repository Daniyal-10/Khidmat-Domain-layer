# Community Context Domain: Discovery Report & Boundary Definition (Revised)

## 1. Purpose of the Domain
The **Community Context Domain** models the geographic, environmental, social, cultural, economic, and infrastructural environment in which Beneficiaries, Families, and Households reside. Its purpose is to transition the Khidmat AI from reasoning about cases in isolation to reasoning about households within their lived environment. This domain equips the AI to understand how a community's characteristics—ranging from seasonal hazards and service availability to social capital, security, and economic engines—amplify or mitigate individual vulnerability, enabling predictive flagging, safe volunteer dispatch, and programmatic response orchestration.

## 2. Scope
- **Geographic and Administrative Hierarchy:** Spatial boundaries from granular neighbourhoods to larger districts.
- **Physical Environment:** Terrain, topography, environmental conditions, and logistics constraints.
- **Population & Demographics:** Migration, displacement, transient populations, and demographic stability.
- **Service & Infrastructure Availability:** Presence, distance, quality, and accessibility of critical services (healthcare, education, markets, transport, WASH, communications, internet, mobile connectivity).
- **Economy & Livelihoods:** Primary livelihoods, agriculture, employment, market integration, seasonal income, and financial inclusion.
- **Governance & Institutions:** Local governance, village councils, religious institutions, community leaders, women's groups, youth groups, and local NGOs.
- **Social Context:** Social cohesion, social exclusion, ethnic/caste dynamics, and vulnerable populations.
- **Culture:** Language, customs, festivals, gender norms, and local practices.
- **Safety & Security:** Conflict, crime, political instability, volunteer safety, and unsafe routes.
- **Public Health Context:** Endemic diseases, environmental health, and community nutrition context.
- **Environmental & Seasonal Dynamics:** Seasonal risk calendars and standing hazards.
- **Community Assets:** Local capacity, volunteers, skilled people, local organizations, and resilience assets.

## 3. Non-Scope
- **Individual/Household Risk:** Specific vulnerabilities of a person or household are owned by the **Risk Domain**.
- **Individual Case Management:** Orchestrating interventions for a specific household remains the responsibility of the **Case Management Domain**.
- **Delivery Mechanics:** How services are delivered by Khidmat (vendors, logistics) belongs to the **Support Delivery Domain**.
- **Registration of Individuals:** Capturing individual beneficiary data belongs to the **Registration Domain**.

## 4. Why This Domain Exists
A household does not exist in a vacuum. A damaged roof in a dry area is a standard repair need; the same damaged roof in a known flood zone two weeks before monsoon season is an emergency. A clinic may be 2km away, but if the terrain is impassable, or if the household belongs to an excluded social group, or if the route runs through a conflict zone, the clinic is effectively inaccessible. This domain exists so the AI can:
- **Contextualize Needs:** Adjust urgency and severity based on external environmental, economic, and social factors.
- **Identify Clustered Vulnerability:** Detect when multiple cases in a single area signal a systemic issue requiring a programmatic response rather than isolated case management.
- **Determine Feasibility & Safety:** Evaluate whether a proposed intervention is viable given local infrastructure, terrain, cultural norms, and security constraints.

## 5. Domain Responsibilities
- Defining the taxonomy of geographic hierarchies, infrastructure types, terrain, security statuses, cultural norms, and economic profiles.
- Modelling seasonal events and their temporal predictability.
- Calculating and representing service accessibility (considering physical distance, terrain, cost, season, and social exclusion).
- Aggregating household-level data to create dynamic community vulnerability maps.
- Providing contextual signals to inference engines in Case Management, Volunteer Operations, and Risk domains.

## 6. Ownership Boundaries
- **Owns:** Geographic Area, Infrastructure/Service Access, Seasonal Event, Community Hazard, Community Resilience, Social/Cultural Profile, Economic Profile, Security Status, Local Institutions, Community Assets.
- **Does Not Own:** Person, Household (Shared); Need, Case (Case Management/Registration); Hazard Category (Risk Domain); Health Condition Definitions (Shared Human Model).
- **Rule of Thumb:** If it affects everyone in the village regardless of their specific family structure, or defines the environment they navigate, it belongs in Community Context.

## 7. Canonical Entities
- `GeographicArea`: The spatial boundary (can be administrative or organically defined, e.g., a neighbourhood or block).
- `ServiceInfrastructure`: Physical or institutional resources available to the community (e.g., clinic, school, well, WASH facility, cell tower).
- `SeasonalEvent`: Predictable temporal periods carrying specific risks or constraints.
- `LocalHazard`: Standing environmental or social threats specific to the area.
- `LocalInstitution`: Formal or informal power structures, village councils, and gatekeepers.
- `CommunityAsset`: Human capital, local volunteers, skilled people, and collective resilience mechanisms.
- `SupportEcosystem`: Community-level social safety nets and local organisations.

## 8. Concepts That Must Be Referenced From Other Domains
- `Household` (from Shared Ontology)
- `Person` (from Shared Ontology)
- `HazardCategory` (from Risk Domain)
- `HealthCondition` (from Shared Human Model, for endemic diseases)
- `Location` (from Shared Taxonomy)
- `OrganisationType` (from Shared Taxonomy)
- `TemporalGranularity` / `ObservationWindows` (from Shared Time Taxonomy)

## 9. Concepts That Community Context Owns
- `geographic_hierarchy` (e.g., District → Block → Village → Ward/Neighbourhood)
- `terrain_type` & `logistics_constraint`
- `demographic_stability` & `population_mobility`
- `infrastructure_type` (extended to include WASH and communications)
- `accessibility_status` (physical, seasonal, AND social barriers)
- `seasonal_calendar`
- `primary_economic_engine` & `market_integration_level`
- `governance_structure`
- `social_cohesion_status` & `exclusion_dynamics`
- `cultural_norms` (languages, gender norms)
- `security_status`
- `endemic_health_risks` & `environmental_health_baseline`
- `community_vulnerability_profile` & `community_resilience_assets`

## 10. Bounded Context Analysis
The Community Context sits structurally above the individual/household level and acts as an environmental wrapper around them. It is a highly referenced context. It interacts heavily with:
- **Shared Domain:** Consumes and enriches location and health condition data.
- **Risk Domain:** Provides the environmental half of the exposure equation (Hazard + Community Exposure = Local Risk).
- **Case Management / Programs:** Consumers of community context to decide *where*, *how*, and *whether* it is safe to intervene.
- **Volunteer Operations:** Depends entirely on this domain to avoid dispatching volunteers into unsafe routes or culturally inappropriate scenarios.

## 11. Cross-Domain Dependency Graph
- **Depends On:** Stage 2 (Shared Human Model), Stage 3 (Risk Domain).
- **Enables:** Stage 9 (Programs Domain - to target area-level interventions), Volunteer Operations (for safe dispatch), Predictive Risk Modelling (future).

## 12. Upstream Dependencies
- `shared/taxonomy/locations.yaml`: Needs to be extended beyond "dispatch precision" to support geographic hierarchies.
- `shared/risk/taxonomy/hazard-categories.yaml`: Provides the vocabulary of harms that the Community Context maps geographically.
- `shared/taxonomy/organisations.yaml`: Provides baseline organisation types.
- `shared/human-model/taxonomy/health-conditions.yaml`: Provides the health vocabulary for mapping endemic diseases.

## 13. Downstream Consumers
- **Case Management:** Will use service availability, social exclusion data, and cultural norms to filter referrals and intervention design.
- **Programs Domain (Future):** Will use aggregate vulnerability mapping and economic profiles to design block-level interventions.
- **Predictive Risk Engines:** Will use seasonal calendars and economic shock reasoning to generate proactive outreach flags.
- **Volunteer Operations:** Will strictly consume security status, terrain data, and cultural norms to manage field assignments and ensure volunteer safety.

## 14. Candidate Taxonomy Files
- `community-context/taxonomy/geographic-hierarchy.yaml`
- `community-context/taxonomy/physical-environment.yaml` (Terrain, logistics constraints)
- `community-context/taxonomy/infrastructure-types.yaml` (Includes WASH, digital, communications)
- `community-context/taxonomy/demographics-and-culture.yaml` (Mobility, displacement, language, gender norms)
- `community-context/taxonomy/economy.yaml` (Livelihood bases, market integration, seasonal income)
- `community-context/taxonomy/governance-and-social.yaml` (Governance structures, exclusion dynamics, social cohesion)
- `community-context/taxonomy/safety-and-health.yaml` (Security status, crime, political instability, endemic risks)
- `community-context/taxonomy/accessibility.yaml` (Physical, seasonal, social)
- `community-context/taxonomy/seasonal-events.yaml`
- `community-context/taxonomy/community-hazards.yaml`

## 15. Candidate Ontology Files
- `community-context/ontology/entities.yaml` (Defining GeographicArea, ServiceInfrastructure, SeasonalEvent, LocalInstitution, CommunityAsset)
- `community-context/ontology/attributes.yaml` (Defining properties like distance_to_market, infrastructure_status, primary_language, security_level, terrain_type, demographic_stability)
- `community-context/ontology/relationships.yaml` (Defining how Households are `located_in` Areas, Areas `contain` Infrastructure/Institutions/Assets, Areas `exposed_to` SeasonalEvents/Hazards, Areas `governed_by` LocalInstitutions)

## 16. Candidate Reasoning Modules
- `community-context/reasoning/seasonal-risk-inference.yaml`: Projects area-level seasonal risks onto resident households.
- `community-context/reasoning/service-accessibility-rules.yaml`: Derives effective access based on distance, cost, season, terrain, and social exclusion.
- `community-context/reasoning/economic-shock-inference.yaml`: Projects market or livelihood disruptions onto households based on area economic profiles.
- `community-context/reasoning/volunteer-safety-rules.yaml`: Evaluates security status, unsafe routes, and terrain to block or restrict operational dispatch.
- `community-context/reasoning/aggregate-vulnerability-rules.yaml`: Rules for when a cluster of individual cases escalates to a community-level programmatic flag.

## 17. AI Reasoning Responsibilities
- **Contextual Amplification:** Looking up the community profile when assessing a case (e.g., food need during a "lean season" in an agrarian community is a systemic stress).
- **Feasibility & Safety Checking:** Validating interventions against local reality (e.g., "Cannot recommend hospital referral; road is seasonally cut off and runs through a high-crime zone.").
- **Clustering:** Recognizing when multiple identical needs from the same `GeographicArea` synthesize a community-level alert.

## 18. Human-in-the-Loop Responsibilities
- **Ground-Truthing:** Infrastructure status, terrain passability, and security conditions must be verifiable by field volunteers.
- **Updating the Baseline:** Community contexts change (new clinics open, tensions rise, demographics shift). Human operatives must have a mechanism to update the community profile independently of registering a specific case.
- **Cultural Nuance:** Validating social capital, power dynamics, and informal governance often requires human qualitative assessment.

## 19. Knowledge Graph Role
The Community Context acts as the central connective tissue in the Knowledge Graph for spatial, social, and environmental reasoning. 
- Path: `Household` → `located_in` → `GeographicArea` → `exposed_to` → `SeasonalEvent`.
- Path: `Household` → `located_in` → `GeographicArea` → `governed_by` → `LocalInstitution`.
- Path: `Household` → `located_in` → `GeographicArea` → `served_by` → `ServiceInfrastructure`.
- Path: `Household` → `located_in` → `GeographicArea` → `protected_by` → `CommunityAsset`.

## 20. RDF/OWL Considerations
- **Acyclic Dependencies:** Ensure that `Household` references `GeographicArea`, but `GeographicArea` does not embed a hard list of all households (avoiding circular dependency).
- **Temporal Validity:** `ServiceInfrastructure`, `AccessibilityStatus`, and `SecurityStatus` must support temporal annotations (e.g., valid_from, valid_until) to handle infrastructure decay, seasonal road closures, or temporary conflict zones.

## 21. Potential Future ADRs
- **ADR-XXX: Administrative vs. Organic Boundaries:** Deciding whether a `GeographicArea` maps strictly to government administrative boundaries or supports overlapping, organically defined community boundaries.
- **ADR-XXX: Dynamic Infrastructure & Security Maintenance:** Deciding who has authority to declare infrastructure "offline" or an area "unsafe", and how that state propagates to active cases and volunteer operations.
- **ADR-XXX: Aggregation Thresholds:** Defining the statistical threshold at which household-level needs trigger a community-level programmatic response.

## 22. Risks of Incorrect Modelling
- **Granularity Mismatch:** If the geographic unit is too large, service access and security assumptions will be dangerously wrong (averaging out the remote or unsafe villages).
- **Static Decay:** Treating infrastructure or security as static. If the model cannot handle temporal degradation, the AI will dispatch volunteers to unsafe areas or make impossible referrals.
- **Ignoring the Human Element:** Treating the community purely as infrastructure while ignoring social exclusion, power dynamics, or cultural norms, leading to interventions that fail upon contact with reality.

## 23. Long-Term Extensibility
- **Climate Change & Macro-trends:** Incorporating long-term environmental degradation as slowly shifting community hazards.
- **Digital Ecosystems:** Modelling digital connectivity and remote service availability.
- **Macro-Economic Factors:** Housing localized inflation rates, market price tracking, and supply chain disruptions.

---
