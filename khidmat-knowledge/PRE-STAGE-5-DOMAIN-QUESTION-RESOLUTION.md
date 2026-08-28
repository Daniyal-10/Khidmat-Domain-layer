# PRE-STAGE-5 DOMAIN QUESTION RESOLUTION

This register acts as the final resolution pass before Stage 5. It evaluates every unresolved parameter against authoritative sources, resolving all ontological structure while carefully bounding genuinely absent values or deferred scope.

---

### Q1 — Person-sameness / identity resolution
| Field | Value |
| --- | --- |
| ID | Q1 |
| Domain Question | Person sameness / identity resolution |
| Source Evidence | BL V1 §5.1, §5.2, §17 |
| Established Domain Facts | A person is a persistent entity recognized across time. Identity dimensions are name, age, gender, marital status, and documentation. Biometrics are explicitly excluded. |
| Ontological Decision | The persisting subject is an Entity (P4). Asserting sameness between encounters is an Epistemic Stance (P3). |
| Primitive | P4 (Entity), P3 (Epistemic Stance) |
| Layer | L7 (Cognition), L2 (Entities) |
| Pillar | Pillar I: Human & Social Subject |
| Rule Established | Persistent identity relies on a collection of non-biometric attributes, structurally representing an epistemic stance on sameness over time. |
| Remaining Parameter, if any | The deterministic matching algorithm or threshold to calculate sameness between two claims of identity. |
| Why It Cannot Yet Be Determined | The sources exclude fraud/anomaly engines and operational deduplication from the V1 domain knowledge layer, deferring the algorithmic deduplication rules to runtime implementation. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

---

### Q2 — Vulnerability and compound-risk composition
| Field | Value |
| --- | --- |
| ID | Q2 |
| Domain Question | Vulnerability and compound-risk composition |
| Source Evidence | BL V1 §10, §11 |
| Established Domain Facts | Vulnerability emerges from multiple compounding factors (e.g., infant + malnutrition + low-income). Risk is a first-class concept with horizon, trend, and severity. |
| Ontological Decision | Vulnerability is an emergent composite State (L5) derived from compounding Conditions (P1) and Contexts. Risk is a Condition (P1). |
| Primitive | P1 (Condition) |
| Layer | L5 (States) |
| Pillar | Pillar III: Vulnerability & Need |
| Rule Established | Vulnerability is structurally emergent from the intersection of underlying Conditions and Context, rather than existing as an isolated trait. |
| Remaining Parameter, if any | The quantitative mathematical formula or weighting table for how factors compound into a numerical vulnerability score. |
| Why It Cannot Yet Be Determined | The sources establish the qualitative compounding logic but provide no mathematical formula or weighting rules. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

---

### Q3 — Family / household membership
| Field | Value |
| --- | --- |
| ID | Q3 |
| Domain Question | Family / household membership |
| Source Evidence | BL V1 §6, §7 |
| Established Domain Facts | Family is bounded by relationships (parent, child, spouse) and dependency. Household is a living unit defined by housing, utilities, and resilience. |
| Ontological Decision | Family and Household are both distinct Entities (P4). Membership and dependency are Relations (P7). |
| Primitive | P4 (Entity), P7 (Relation) |
| Layer | L2 (Entities), L3 (Relational Structure) |
| Pillar | Pillar I: Human & Social Subject |
| Rule Established | The domain strictly distinguishes kinship/dependency (Family) from co-residence/living unit (Household), recognizing that a subject can hold relationships to both concurrently. |
| Remaining Parameter, if any | The precise demographic boundary rules or temporal thresholds for determining when a member enters or exits a household or family unit. |
| Why It Cannot Yet Be Determined | The sources distinguish the concepts but do not specify the exact demographic boundary rules for membership. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

---

### Q4 — Human-facet value sets
| Field | Value |
| --- | --- |
| ID | Q4 |
| Domain Question | Human-facet value sets |
| Source Evidence | BL V1 §5.2, §5.3, §5.4 |
| Established Domain Facts | Human dimensions include Lifecycle stage (infant, toddler...), Capabilities (physical, cognitive...), and Health (acute, chronic...). |
| Ontological Decision | These dimensions are Facets (L1) which hold distinct States (L5). |
| Primitive | P1 (Condition) |
| Layer | L1 (Facets), L5 (States) |
| Pillar | Pillar I: Human & Social Subject |
| Rule Established | The ontology separates the structural dimensions of human capability and condition (Facets) from the actual manifestations (States). |
| Remaining Parameter, if any | Exhaustive controlled vocabularies and dictionaries for every possible value. |
| Why It Cannot Yet Be Determined | The sources define high-level categories and examples but lack complete reference data dictionaries for all values. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

---

### Q5 — Outcome / Impact ownership
| Field | Value |
| --- | --- |
| ID | Q5 |
| Domain Question | Outcome / Impact ownership |
| Source Evidence | RM §12.5, BL V1 §14 |
| Established Domain Facts | The goal is improved human wellbeing. Outcome and impact measurement occur sequentially inside the Beneficiary Lifecycle flow (BL V1 §14). |
| Ontological Decision | Outcomes and Impacts are State changes (L5) belonging to the Human Subject. Their measurement is an Event (L6). |
| Primitive | P2 (Event), P6 (Coordination Pattern) |
| Layer | L5 (States), L6 (Events) |
| Pillar | Pillar VI: Action & Coordination |
| Rule Established | Structural classification is resolved. However, operational ownership of the measurement (whether Case Journey or MEAL) is not established. |
| Remaining Parameter, if any | Operational ownership (Case Journey vs MEAL). |
| Why It Cannot Yet Be Determined | RM §12.5 leaves this `[OPEN]` as field evidence supports a separate MEAL capability, and BL V1 §14 does not explicitly assign ownership. |
| Status | GENUINELY OPEN / ownership: pending |

---

### Q6 — Organisation / Programme distinction
| Field | Value |
| --- | --- |
| ID | Q6 |
| Domain Question | Organisation / Programme distinction |
| Source Evidence | BL V1 §4 |
| Established Domain Facts | The "Programme / Organisation" actor defines the assistance available and eligibility criteria, acting as a single operational actor role in the lifecycle. |
| Ontological Decision | Organisation and Programme are collapsed into a single Entity (P4). |
| Primitive | P4 (Entity) |
| Layer | L2 (Entities) |
| Pillar | Pillar V: Actors & Ecosystem |
| Rule Established | The distinction is collapsed for the V1 business model, resolving earlier reference-model tensions. |
| Remaining Parameter, if any | None. |
| Why It Cannot Yet Be Determined | N/A |
| Status | RESOLVED |

---

### Q7 — Giving-side entities and coordination
| Field | Value |
| --- | --- |
| ID | Q7 |
| Domain Question | Giving-side entities and coordination |
| Source Evidence | RM §11.4, TD-01 (BD-TD01-004), BL V1 §17 |
| Established Domain Facts | Donors exist as actors and impose coordination/funding constraints, but the resource-supply side and donor-need matching are explicitly excluded from V1 implementation scope. |
| Ontological Decision | Donors are Entities (P4). Giving relationships and coordination are Coordination Patterns (L8). |
| Primitive | P4 (Entity), P6 (Coordination Pattern) |
| Layer | L8 (Coordination) |
| Pillar | Pillar V: Actors & Ecosystem |
| Rule Established | Donors are recognized as actors in humanitarian reality and coordinate with organisations, but their specific operational modeling is deferred as outside V1 build scope. |
| Remaining Parameter, if any | Specific resource taxonomy, donor kinds, and matching allocation rules. |
| Why It Cannot Yet Be Determined | BL V1 §17 explicitly defines the donor supply side as out of scope for the V1 build. |
| Status | OUTSIDE CURRENT DOMAIN SCOPE |

---

### Q8 — Funding restrictions
| Field | Value |
| --- | --- |
| ID | Q8 |
| Domain Question | Funding restrictions |
| Source Evidence | RM §11.4, TD-02 (BD-TD02-001, BD-TD02-003), BL V1 §17 |
| Established Domain Facts | Funding restrictions exist as donor-set priorities and compliance requirements that constrain who may receive what across altitudes. |
| Ontological Decision | A funding restriction is structurally a Constraint / Norm (P5). |
| Primitive | P5 (Constraint / Norm) |
| Layer | L4 (Norms & Constraints) |
| Pillar | Pillar V: Actors & Ecosystem |
| Rule Established | Funding restrictions act as norms/constraints limiting Coordination Patterns (L8) and Events (L6). |
| Remaining Parameter, if any | An exhaustive taxonomy of specific restriction types. |
| Why It Cannot Yet Be Determined | As the donor supply side is excluded from V1 scope, the authoritative sources provide no specific categories of restrictions. |
| Status | OUTSIDE CURRENT DOMAIN SCOPE |

---

### Q9 — Risk classification
| Field | Value |
| --- | --- |
| ID | Q9 |
| Domain Question | Risk classification |
| Source Evidence | BL V1 §11, Ontology derivations |
| Established Domain Facts | Risk is a first-class concept with a horizon, trend, and severity, distinct from needs but grounded in similar causal reality. |
| Ontological Decision | Risk is structurally classified as a Condition (P1). |
| Primitive | P1 (Condition) |
| Layer | L5 (States) |
| Pillar | Pillar III: Vulnerability & Need |
| Rule Established | Risk is formally a Condition; its previous structural ambiguity is resolved. |
| Remaining Parameter, if any | None. |
| Why It Cannot Yet Be Determined | N/A |
| Status | RESOLVED |

---

### Q10 — Evidence kinds / epistemic hierarchy
| Field | Value |
| --- | --- |
| ID | Q10 |
| Domain Question | Evidence kinds / epistemic hierarchy |
| Source Evidence | BL V1 §3.1, §14 |
| Established Domain Facts | Unverified information constitutes claims; verification turns claims into findings. Needs assessment applies confidence to these findings. |
| Ontological Decision | Evidence is NOT a primitive. Evidence acts as an Entity/Occurrence that grounds an Epistemic Stance (P3). |
| Primitive | P3 (Epistemic Stance), P4 (Entity) |
| Layer | L7 (Cognition) |
| Pillar | Pillar IV: Epistemics & Knowledge |
| Rule Established | Epistemic stance progresses from claim to finding via verification, rather than assuming certainty. |
| Remaining Parameter, if any | The numerical weighting of different evidence kinds and an exhaustive taxonomy of evidence types. |
| Why It Cannot Yet Be Determined | Exact numerical weights and exhaustive categories of evidence are not provided in the sources and must not be invented. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

---

### Q11 — Wellbeing standard
| Field | Value |
| --- | --- |
| ID | Q11 |
| Domain Question | Wellbeing standard |
| Source Evidence | BL V1 §9 |
| Established Domain Facts | A Need is fundamentally a gap between a current state and a basic standard of wellbeing. |
| Ontological Decision | The wellbeing standard is structurally a Context-dependent Norm (P5). |
| Primitive | P5 (Constraint / Norm) |
| Layer | L4 (Norms & Constraints) |
| Pillar | Pillar II: Context & Environment |
| Rule Established | Need exists as a relational gap measured against a normative baseline. |
| Remaining Parameter, if any | The precise quantitative baseline values constituting the basic standard. |
| Why It Cannot Yet Be Determined | The sources establish the comparative structure but do not supply the raw baseline numerical values. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

---

### Q12 — Missing information
| Field | Value |
| --- | --- |
| ID | Q12 |
| Domain Question | Missing information |
| Source Evidence | RM §10.5, BL V1 §3.1 |
| Established Domain Facts | The system operates under an open-world assumption where unstated information is unknown, not factually negative. |
| Ontological Decision | Open-world operation is established, but the concrete structural representation of missing information remains open. |
| Primitive | P3 (Epistemic Stance) |
| Layer | L7 (Cognition) |
| Pillar | Pillar IV: Epistemics & Knowledge |
| Rule Established | Open-world assumption is established. Concrete missing-information representation is explicitly left open by RM §10.5. |
| Remaining Parameter, if any | Structural representation mechanism for missing information. |
| Why It Cannot Yet Be Determined | The specific representation is unstated by any authoritative source. |
| Status | GENUINELY OPEN |

---

### Q13 — Contradiction representation and handling
| Field | Value |
| --- | --- |
| ID | Q13 |
| Domain Question | Contradiction representation and handling |
| Source Evidence | RM §10.5, BL V1 §14 |
| Established Domain Facts | Conflicting claims are preserved (epistemic humility). Resolution happens via a human-driven accountability loop (grievance, re-verification). |
| Ontological Decision | Epistemic humility is supported, but the specific structural representation of contradiction is open. |
| Primitive | P3 (Epistemic Stance) |
| Layer | L7 (Cognition), L8 (Coordination) |
| Pillar | Pillar IV: Epistemics & Knowledge |
| Rule Established | Contradiction is preserved in the knowledge model and resolution is enacted via human workflows. The structural representation of contradiction is explicitly left open by RM §10.5. |
| Remaining Parameter, if any | Structural representation mechanism for contradiction. |
| Why It Cannot Yet Be Determined | The specific representation is unstated by any authoritative source. |
| Status | GENUINELY OPEN |

---

### Q14 — Consent rules and parameters
| Field | Value |
| --- | --- |
| ID | Q14 |
| Domain Question | Consent rules and parameters |
| Source Evidence | BL V1 §3.2, §16 |
| Established Domain Facts | Data is collected with consent, and safety takes precedence over process. Consent governs data action. |
| Ontological Decision | Consent acts structurally as a Constraint / Norm (P5). |
| Primitive | P5 (Constraint / Norm) |
| Layer | L4 (Norms & Constraints) |
| Pillar | Pillar I: Human & Social Subject |
| Rule Established | Consent acts as a fundamental constraint that governs and restricts the coordination space and information collection. |
| Remaining Parameter, if any | The detailed operational consent policies, such as scopes and withdrawal mechanics. |
| Why It Cannot Yet Be Determined | BL V1 §16 explicitly defines consent parameters as a "minimal placeholder" in V1, deferring detailed policy formulation. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

### Q15 — Service Providers as Actors
| Field | Value |
| --- | --- |
| ID | Q15 |
| Domain Question | Service Providers as Actors |
| Source Evidence | RM §11.3 |
| Established Domain Facts | Healthcare providers, schools, and employers exist in humanitarian reality. |
| Ontological Decision | Whether they act with agency (as distinct Actors/Entities) remains open. |
| Primitive | P4 (Entity) / P2 (Context) |
| Layer | L2 (Entities) / L1 (Facets) |
| Pillar | Pillar V: Actors & Ecosystem |
| Rule Established | The operational agency of Service Providers is explicitly kept pending. |
| Remaining Parameter, if any | N/A |
| Why It Cannot Yet Be Determined | Authoritative sources do not definitively settle if they should be modeled as Actors with agency. |
| Status | GENUINELY OPEN |

---

### Q16 — Need interaction model
| Field | Value |
| --- | --- |
| ID | Q16 |
| Domain Question | Need interaction model |
| Source Evidence | RM §7.5 |
| Established Domain Facts | Needs can cascade and relate. |
| Ontological Decision | The general model of how needs relate remains open. |
| Primitive | P7 (Relation) |
| Layer | L3 (Relational Structure) |
| Pillar | Pillar III: Vulnerability & Need |
| Rule Established | A general model is unstated by any source and is deferred. |
| Remaining Parameter, if any | N/A |
| Why It Cannot Yet Be Determined | Sources do not specify the generalized semantics of need-to-need interactions. |
| Status | GENUINELY OPEN |

---

### Q17 — Funder altitude
| Field | Value |
| --- | --- |
| ID | Q17 |
| Domain Question | Funder altitude |
| Source Evidence | RM §11.4 |
| Established Domain Facts | Donors/funders exist, but an operational altitude beyond Programme/Case is unevidenced. |
| Ontological Decision | An implied but unevidenced third altitude remains open. |
| Primitive | P6 (Coordination Pattern) |
| Layer | L8 (Coordination) |
| Pillar | Pillar VI: Action & Coordination |
| Rule Established | Kept open and handled via UHR. |
| Remaining Parameter, if any | N/A |
| Why It Cannot Yet Be Determined | No source models this altitude. |
| Status | GENUINELY OPEN |

---

### Q18 — Orphanhood vs Unguardianed
| Field | Value |
| --- | --- |
| ID | Q18 |
| Domain Question | Orphanhood vs Unguardianed |
| Source Evidence | RM §6.3 |
| Established Domain Facts | Both involve children without present guardians. |
| Ontological Decision | RM does not distinguish the two; their structural separation remains open. |
| Primitive | P1 (Condition) / P7 (Relation) |
| Layer | L5 (States) |
| Pillar | Pillar I: Human & Social Subject |
| Rule Established | Structural distinction is explicitly deferred as an open tension. |
| Remaining Parameter, if any | N/A |
| Why It Cannot Yet Be Determined | The Reference Model does not distinguish them. |
| Status | GENUINELY OPEN |

---

### Q19 — Case Coordination/Orchestration capability status
| Field | Value |
| --- | --- |
| ID | Q19 |
| Domain Question | Case Coordination/Orchestration capability status |
| Source Evidence | Stage 4 Open Tensions (UHR-1) |
| Established Domain Facts | The capability handles complex routing and orchestration. |
| Ontological Decision | Whether it represents a standalone capability distinct from Case Management remains open. |
| Primitive | P6 (Coordination Pattern) |
| Layer | L8 (Coordination) |
| Pillar | Pillar VI: Action & Coordination |
| Rule Established | Addressed as a stub extension point (UHR-1) to avoid premature resolution. |
| Remaining Parameter, if any | N/A |
| Why It Cannot Yet Be Determined | Tier B/D evidence collection or practitioner evidence is required. |
| Status | GENUINELY OPEN |
