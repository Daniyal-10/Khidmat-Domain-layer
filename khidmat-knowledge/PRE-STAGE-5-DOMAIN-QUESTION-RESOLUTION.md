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
| Pillar | Pillar I (The Human Subject) |
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
| Pillar | Pillar IV (Vulnerability & Risk) |
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
| Pillar | Pillar II (The Unit of Support) |
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
| Pillar | Pillar I (The Human Subject) |
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
| Source Evidence | BL V1 §13, §14 |
| Established Domain Facts | The goal is improved human wellbeing. Outcome and impact measurement occur inside the Beneficiary Lifecycle (Case Journey), progressing from support delivery to outcome measurement to impact measurement. |
| Ontological Decision | Outcomes and Impacts are State changes (L5) belonging to the Human Subject. Their measurement is an Event (L6) within Case Journey Coordination (L8). |
| Primitive | P2 (Event), P6 (Coordination Pattern) |
| Layer | L6 (Events), L8 (Coordination) |
| Pillar | Pillar VI (The Case Journey) |
| Rule Established | Outcome and Impact ownership belongs to the Case Journey, overriding prior tensions that placed it in a separate MEAL discipline. |
| Remaining Parameter, if any | None. |
| Why It Cannot Yet Be Determined | N/A |
| Status | RESOLVED |

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
| Pillar | Pillar V (The Actors) |
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
| Pillar | Pillar V (The Actors) |
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
| Pillar | Pillar VII (The Operations Frame) |
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
| Pillar | Pillar IV (Vulnerability & Risk) |
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
| Pillar | Pillar VII (The Operations Frame) |
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
| Pillar | Pillar III (Needs) |
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
| Source Evidence | BL V1 §3.1, RM §10.3 |
| Established Domain Facts | The system operates under an open-world assumption where unstated information is unknown, not factually negative. |
| Ontological Decision | Missing information is handled natively via the absence of an Epistemic Stance (P3) in the Cognition layer (L7). |
| Primitive | P3 (Epistemic Stance) |
| Layer | L7 (Cognition) |
| Pillar | Pillar VII (The Operations Frame) |
| Rule Established | Absence of information reflects a lack of epistemic stance, not a negative domain fact. |
| Remaining Parameter, if any | None. |
| Why It Cannot Yet Be Determined | N/A |
| Status | RESOLVED |

---

### Q13 — Contradiction representation and handling
| Field | Value |
| --- | --- |
| ID | Q13 |
| Domain Question | Contradiction representation and handling |
| Source Evidence | BL V1 §14 |
| Established Domain Facts | Conflicting claims are preserved (epistemic humility). Resolution happens via a human-driven accountability loop (grievance, re-verification). |
| Ontological Decision | Contradictions are represented as competing Epistemic Stances (P3). |
| Primitive | P3 (Epistemic Stance) |
| Layer | L7 (Cognition), L8 (Coordination) |
| Pillar | Pillar VII (The Operations Frame) |
| Rule Established | Contradiction is preserved in the knowledge model; resolution is enacted via human coordination workflows, not an algorithmic scoring mechanism. |
| Remaining Parameter, if any | The exact operational routing paths for the re-verification process. |
| Why It Cannot Yet Be Determined | The sources define the principle and human loop but lack the low-level operational workflow routes. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |

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
| Pillar | Pillar VII (The Operations Frame) |
| Rule Established | Consent acts as a fundamental constraint that governs and restricts the coordination space and information collection. |
| Remaining Parameter, if any | The detailed operational consent policies, such as scopes and withdrawal mechanics. |
| Why It Cannot Yet Be Determined | BL V1 §16 explicitly defines consent parameters as a "minimal placeholder" in V1, deferring detailed policy formulation. |
| Status | PARTIALLY RESOLVED — SPECIFIC PARAMETER REMAINS |
