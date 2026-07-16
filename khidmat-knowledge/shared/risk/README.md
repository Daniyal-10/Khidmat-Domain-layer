# Shared Risk Domain

**Layer:** shared/risk/
**Status:** Phase 3.0 — Active
**Authority:** Knowledge Layer Architect
**Governing ADRs:** ADR-007, ADR-008, ADR-010, ADR-011, ADR-012, ADR-013, ADR-014
**Prerequisite:** Shared Human Model (Phase 2.4 — Complete)

---

# Purpose

The Registration Domain and the Shared Human Model both describe a household
as it presents itself — a snapshot of who someone is, what situation they
are in, and what they currently need. Neither answers a different, forward-
looking question: **what might happen to this person or household next, and
how exposed and able to withstand it are they?**

The Risk Domain exists to answer that question. It does not replace need
identification (registration) or human modelling (the Shared Human Model).
It sits above both, composing their outputs into a forward-looking signal:
a household with a damaged roof is a shelter repair case in registration's
terms; the same household in a flood-prone area with monsoon approaching is
additionally a risk signal that registration's need-based model cannot
express on its own.

The Risk Domain is the mechanism by which Khidmat AI moves from reactive
need identification toward anticipatory humanitarian reasoning — the
explicit objective named in the business logic blueprint as identifying
needs that are "implied," "emerging," and "likely to occur in the future."

---

# Scope

The Risk Domain owns the following concept areas:

- **Risk** — the forward-looking, time-bound likelihood and severity of harm
  to a specific person, family, or household
- **Vulnerability** — the standing, latent capacity deficit that makes harm
  more likely or more severe when a hazard is encountered
- **Risk Factor** — an atomic characteristic, condition, event, or
  circumstance that increases the likelihood or severity of harm
- **Protective Factor** — the atomic, symmetric inverse of a Risk Factor
- **Resilience** — the composite, household/family-level capacity to absorb,
  adapt to, and recover from adversity
- **Hazard Category** — the qualitative classification of what kind of harm
  a risk factor relates to (not its geographic or temporal instantiation)
- **Exposure** — the relationship between a person/household and a hazard
  category describing the degree to which they are positioned to encounter it
- **Risk Horizon** — when harm might occur, as a qualitative band
- **Risk Trend** — whether risk is improving, stable, or deteriorating at
  the point of assessment
- **Compound Risk** — concentration compounding and interaction compounding
  between co-occurring risk factors
- **Protection Indicator** — a closed vocabulary of specific, observable
  exploitation and coercion signals belonging under the social_protection
  hazard category (added Stage 3B)

These concepts may be referenced by future domains but are defined only
here. No other domain may redefine them.

---

# Design Principles

**Risk Domain composes; it does not redefine.**
Every input to Vulnerability and Resilience already has an owner elsewhere
in the knowledge layer — capability levels, dependency types, health
conditions, lifecycle stages, family structural attributes. The Risk Domain
adds the composition logic and the concepts that genuinely have no existing
owner (Hazard, Exposure, Risk Horizon, Risk Trend, Compound Risk). It does
not re-author what `capabilities.yaml`, `dependency.yaml`,
`health-conditions.yaml`, `lifecycle-stages.yaml`, or `family-structure.yaml`
already define. See `risk-domain-governance.md` for the full boundary
enforcement ruleset.

**No scores. Qualitative composition only.**
Every prior Shared Human Model file explicitly rejects numeric scoring in
favour of structured, qualitative judgment. The Risk Domain — the file most
tempted toward a Hazard × Exposure × Vulnerability ÷ Capacity formula — holds
the same line. Risk, Vulnerability, and Resilience are qualitative levels
supported by structured, named inputs, not computed numbers.

**Horizon and persistence are different axes.**
When harm might occur (horizon) and how long the risk-generating condition
lasts (persistence) are independent questions. They are modelled as
separate attributes, never collapsed into a single enum.

**Concept and instance are separate.**
The Risk Domain defines risk factor *types*, hazard *categories*, and
protective factor *types*. Whether a specific risk factor is present in a
specific case is an instance-level fact that belongs to whichever domain
holds case data — registration today, eventually case management and
beneficiary lifecycle.

**The Risk Domain produces signals; it does not act on them.**
What to do about an identified risk — which intervention, what priority,
what resource allocation — is explicitly out of scope. That reasoning
belongs to Case Management (Stage 5).

---

# File Structure

The file list below intentionally differs from the original roadmap sketch
in `knowledge_layer_roadmap.md`. The deviations are deliberate decisions
made during architecture review, not omissions:

| Originally sketched | Implemented as | Reason |
|---|---|---|
| `risk-factors.yaml` | absorbed | Conceptually split between `vulnerability.yaml` (internal capacity deficits) and `exposure.yaml` (external situational positioning) during implementation. |
| `risk-trajectory.yaml` | folded into `risk.yaml` | Risk Trend (renamed from "trajectory" to avoid colliding with `situation.trajectory`) is an attribute of the Risk entity, not an independent taxonomy. It does not need its own file. |
| `vulnerability.yaml` | `vulnerability.yaml` | unchanged |
| `household-resilience.yaml` | `household-resilience.yaml` | unchanged |
| `seasonal-risk.yaml` | `hazard-categories.yaml` | Retitled and rescoped. The original file implied a geographic/temporal calendar, which is explicitly Stage 8 (Community Context) territory. This file owns only the qualitative, non-geographic hazard category taxonomy. |
| *(not originally listed)* | `exposure.yaml` | Exposure was elevated to a first-class concept during architecture review, distinct from both Hazard and Vulnerability. |
| *(not originally listed)* | `protective-factors.yaml` | Protective Factor was elevated to a first-class, symmetric taxonomy alongside Risk Factor, rather than left as an undefined residual category. |
| *(not originally listed)* | `risk-domain-governance.md` | Boundary enforcement rules, cross-domain reference patterns, and anti-patterns are centralised here rather than repeated inline in every ontology file, following the repository governance pattern established for ontology domains. |
| "Risk inference rules" | `reasoning/compound-risk-detection.yaml` | Scoped specifically to compound risk detection (concentration and interaction compounding), which closes the long-standing "Compound Situation Inference Rules" gap recorded in `ontology_completion_checklist.md`. General risk-factor-presence detection is left for a later reasoning pass once case-level risk data exists to detect against. |

```
shared/risk/
├── README.md                          (this file)
├── risk-domain-governance.md          (boundary rules, cross-domain patterns, anti-patterns)
├── hazard-categories.yaml             (Hazard Category taxonomy — concept layer only)
├── exposure.yaml                      (Exposure — first-class relationship concept)
├── protective-factors.yaml            (Protective Factor taxonomy)
├── protection-indicators.yaml          (Protection Indicator taxonomy — added Stage 3B)
├── vulnerability.yaml                 (Vulnerability concept + composition model)
├── household-resilience.yaml          (Resilience concept + composition model)
├── risk.yaml                          (Risk concept, Risk Trend, Compound Risk)
└── reasoning/
    └── compound-risk-detection.yaml   (concentration + interaction compounding detection)
```

---

# Relationship to Other Domains

## Shared Human Model

The Risk Domain is the primary downstream consumer of the Shared Human
Model. Risk factors, vulnerability composition, and resilience composition
reference lifecycle stage, capability level, dependency type, health
condition, and family structural attributes by `*_ref` — never by
redefinition. See `risk-domain-governance.md` for the formal reference
patterns and `ontology_authority_matrix.md` for the concept ownership
declarations this file introduces.

## Registration Domain

The Risk Domain references registration's `situation` taxonomy (trigger
events, affected domains) and `need` taxonomy as inputs to risk factor and
compound risk detection. It does not modify any registration entity,
attribute, or reasoning rule. Registration's existing single-trigger
inference rules (`registration/reasoning/inference-rules.yaml`) continue to
operate unchanged, driving in-conversation questioning. The Risk Domain's
compound risk reasoning is a separate, later-stage composition over
registration's output — not a replacement for registration's own inference
layer.

## Case Management Domain (future — Stage 5)

Case management reasons about intervention fit and urgency. Risk level and
risk trend are inputs to that reasoning. The Risk Domain does not own
intervention eligibility, prioritisation, or resource allocation.

## Beneficiary Lifecycle Domain (future — Stage 7)

The Risk Domain defines Vulnerability, Resilience, and Risk Trend as
single-case, point-in-time compositions. Tracking how those compositions
change for the *same* household across multiple registrations over time is
explicitly a Beneficiary Lifecycle Domain concern. The Risk Domain does not
track history.

## Community Context Domain (future — Stage 8)

The Risk Domain owns hazard *categories* and a qualitative, non-geographic
seasonality note per category. It does not own geographic hierarchy, the
actual seasonal calendar, area-level hazard instantiation, or aggregation
of Vulnerability/Resilience across many households. Those are Community
Context concerns that consume the Risk Domain's concepts by reference.

---

# Ownership Boundaries

## This domain owns:

- Risk, Vulnerability, Resilience, Hazard Category, Exposure concepts
- Risk Factor and Protective Factor taxonomies (concept layer)
- Risk Horizon and Risk Factor Persistence (local-only) vocabularies
- Risk Trend vocabulary
- Compound Risk concepts (concentration and interaction compounding)
- Compound risk detection reasoning

## This domain does NOT own:

- Lifecycle stage, capability, dependency, family structure, or health
  condition definitions (Shared Human Model)
- Need, situation, claim, or case definitions (Registration Domain)
- Geographic hierarchy, seasonal calendars, hazard instantiation, or
  cross-household aggregation (Community Context Domain, Stage 8)
- Intervention eligibility, prioritisation, or resource allocation
  (Case Management Domain, Stage 5)
- Longitudinal tracking of risk/vulnerability/resilience across multiple
  registrations for the same household (Beneficiary Lifecycle Domain,
  Stage 7)
- Outcome/change classification after an intervention (Outcome Layer,
  Stage 6)

Any concept that crosses this boundary must be escalated for architectural
review. It must not be silently added to this domain.

---

# Activation Criteria

The Risk Domain is considered complete and ready to enable Stage 5
(Case Management, jointly with Stage 4) when:

- [x] All planned files exist and are not placeholders
- [x] Ownership of all concepts is declared in `ontology_authority_matrix.md`
- [x] All new terms are added to `GLOSSARY.md` under the correct section
- [x] `knowledge_layer_inventory.md` is updated for all new files
- [x] `ontology_completion_checklist.md` reflects completion status
- [x] `knowledge_layer_roadmap.md` Stage 3 is marked substantially complete
- [ ] Human Owner has approved the model for downstream use
- [ ] ADR-010 through ADR-014 are reviewed and recorded by the Human Owner