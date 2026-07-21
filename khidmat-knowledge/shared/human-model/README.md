# Shared Human Model

**Layer:** shared/human-model/
**Status:** Phase 2.0 — Architecture defined, implementation in progress
**Authority:** Knowledge Layer Architect
**Governing ADRs:** ADR-007, ADR-008

---

# Purpose

The Registration Domain captures snapshots of people at a moment in time.
A registration records who presented, what they said, and what was observed
during a single conversation. It is inherently point-in-time.

The Shared Human Model provides something different: a persistent,
cross-domain understanding of people as they actually are — across
lifecycle stages, within families, across time, and in relation to one
another.

Without the Shared Human Model, every domain that reasons about people
must invent its own person representation. A registration domain person,
a case management person, and a beneficiary lifecycle person become
incompatible representations of the same human being. This is ontology
drift. The Shared Human Model prevents it by establishing a single source
of truth for human concepts.

Future domains depend on this layer being correct before they can function.
No domain may define competing human concepts once this model is in place.

---

# Scope

The Shared Human Model owns the following concept areas:

- **Lifecycle Stages** — developmental stages of human life, each with
  characteristic needs, dependencies, capabilities, and expected outcomes
- **Capabilities** — what a person is able to do; strengths and assets,
  not only deficits
- **Dependencies** — relationships in which one person relies on another
  for care, support, protection, or decision-making
- **Family Structures** — the social unit of individuals connected through
  kinship, caregiving, or recognised relationships; distinct from household
- **Health Conditions** — chronic conditions, disabilities, and clinical
  states that affect a person's functioning, needs, and trajectory

These concepts may be referenced by many domains but are defined only
here. No other domain may redefine them.

**Governing decisions:**
- ADR-007: Shared Human Model as a First-Class Knowledge Layer
- ADR-008: Single Ownership of Concepts

---

# Design Principles

**Model people, not cases.**
A case is an administrative record. A person exists before, during, and
after any case. The models in this layer describe people, not the process
of registering them.

**Model strengths as well as vulnerabilities.**
Capabilities are first-class concepts alongside needs. A person's ability
to contribute, participate, and support others is as important to
humanitarian reasoning as their deficits.

**Model individuals, families, households, and communities simultaneously.**
Human experience is not individual. A mother's vulnerability is an infant's
vulnerability. A household's resilience depends on who is in it. These
models must represent people in relation to each other, not in isolation.

**Support reasoning, not just classification.**
Taxonomy classifies. These models must enable inference. Knowing that a
person is in the infant lifecycle stage should allow a system to reason
about developmental needs, caregiver dependency, and malnutrition risk —
not merely to label the person as "infant".

**Support preventative intervention planning.**
The model must be rich enough for a future system to identify risk before
a person presents. A household with a dependent infant and a single
caregiver of advanced age is a future risk, not just a current need.

**Support future risk modelling.**
The Risk Domain (Stage 3) depends entirely on the concepts defined here.
Lifecycle stage and capability are the inputs to risk factor assessment.
These models must be designed with that dependency in mind.

---

# Relationship to Other Domains

## Registration Domain

Registration references lifecycle stage and family structure when
classifying household members and assessing need severity. The Registration
Domain does not own these concepts — it borrows them. When the Shared Human
Model is complete, registration inference rules can be extended to use
lifecycle-aware reasoning (e.g., detecting developmental malnutrition risk
for an infant in a food-insecure household).

## Risk Domain (future — Stage 3)

The Risk Domain is the primary downstream consumer of this model. Risk
factors are assessed in relation to lifecycle stage and capability.
Vulnerability is a composite of individual, family, household, and
community factors — all of which reference concepts defined here. The Risk
Domain cannot activate before this model is complete.

## Beneficiary Lifecycle Domain (future — Stage 7)

The Beneficiary Lifecycle Domain tracks a person across time. It requires
a stable lifecycle stage model to assess whether a person's developmental
context has changed between registrations, and a capability model to
detect functional improvement or deterioration over time.

## Case Management Domain (future — Stage 5)

Case management reasons about intervention fit. Whether a given
intervention is appropriate for a person depends on their lifecycle stage,
capabilities, and dependency relationships. This domain references but
does not own those concepts.

## Impact Domain (future — Stage 9)

Impact measurement assesses whether a person's situation changed after
intervention. Measuring change requires knowing what the baseline human
context was — which is precisely what this model defines.

**The Shared Human Model does not own interventions, programs, or
outcomes.** Those concepts belong to the Case Management, Programs, and
Impact domains respectively.

---

# Planned Files

## lifecycle-stages.yaml

**Purpose:** Defines developmental stages of human life as reasoning
contexts, not merely age ranges. Each stage carries associated
developmental expectations, characteristic vulnerabilities, and capability
profiles.

**Ownership:** Shared Human Model. No other domain may define lifecycle
stage concepts.

**Example reasoning opportunities:**
- An infant (0–12 months) in a food-insecure household triggers
  developmental malnutrition risk distinct from adult food need
- An adolescent female in a financially distressed household triggers
  educational continuity and protection risk flags
- An elderly person living alone with no caregiver triggers a
  self-sufficiency and caregiver dependency signal

---

## capabilities.yaml

**Purpose:** Defines what a person is able to do — across physical,
cognitive, social, economic, and caregiving dimensions. Models capacity
as an asset, not only as a deficit descriptor.

**Ownership:** Shared Human Model. No other domain may define capability
concepts.

**Example reasoning opportunities:**
- A person with vocational skills and literacy has a different
  livelihood intervention pathway than a person without
- A person whose caregiver capabilities are intact can support a
  dependent household member without external assistance
- Reduction in capability over time (between registrations) is a
  detectable signal of deterioration

---

## dependency.yaml

**Purpose:** Defines the dependency relationship — one person relying on
another for care, support, resources, supervision, protection, or
decision-making. Classifies dependency types and the directionality of
the relationship.

**Ownership:** Shared Human Model. No other domain may define dependency
relationship concepts.

**Example reasoning opportunities:**
- A mother's vulnerability cascades directly to a dependent infant
  without a separate registration
- A household with multiple dependents and a single caregiver has a
  structural resilience risk
- Legal dependency (guardianship) triggers different verification
  and safeguarding requirements than physical dependency

---

## family-structure.yaml

**Purpose:** Defines the family as a social unit connected through
kinship, caregiving, marriage, guardianship, or other recognised
relationships. Distinct from the household (which is a physical and
economic unit). Multiple families may coexist within a household.

**Ownership:** Shared Human Model. No other domain may define family
structure concepts.

**Example reasoning opportunities:**
- Decision-making authority within a family determines whose consent
  is required for interventions
- Internal family support capacity affects whether external assistance
  is supplementary or primary
- A multigenerational household may contain two or more distinct family
  units with different need profiles

---

## health-conditions.yaml

**Purpose:** Defines a structured vocabulary of health conditions relevant
to humanitarian reasoning. Covers chronic conditions, physical and
cognitive disabilities, malnutrition classifications, and mental and
behavioural health conditions at a level of granularity sufficient for
need identification and severity reasoning.

**Ownership:** Shared Human Model. No other domain may define health
condition vocabulary.

**Example reasoning opportunities:**
- Severe acute malnutrition (SAM) in a child triggers a clinical
  urgency flag distinct from household food insecurity
- A chronic condition with no treatment plan and no access to healthcare
  has a different severity classification than the same condition under
  active management
- A mental health condition in a caregiver directly affects the
  dependency model for any dependents in the household

---

# Ownership Boundaries

## This model owns:

- Lifecycle concepts
- Capability concepts
- Dependency concepts
- Family concepts
- Health condition concepts

## This model does NOT own:

- Risk factors (owned by Risk Domain, Stage 3)
- Vulnerability scoring (owned by Risk Domain, Stage 3)
- Interventions (owned by Case Management Domain, Stage 5)
- Outcomes (owned by Outcome Indicator vocabulary, Stage 6)
- Program classifications (owned by Programs Domain, Stage 9)

Any concept that crosses this boundary must be escalated for architectural
review. It must not be silently added to this model.

---

# Activation Criteria

The Shared Human Model is considered complete and ready to enable Stage 3
(Risk Domain) when:

- [ ] All planned files exist and are not placeholders
- [ ] Ownership of all concepts is declared in `ontology_authority_matrix.md`
- [ ] All new terms are added to `GLOSSARY.md` under the correct section
- [ ] `catalog.yaml` reflects any new modules
- [ ] `knowledge_layer_roadmap.md` Stage 2 is marked substantially complete
- [ ] Human Owner has approved the model for downstream use
