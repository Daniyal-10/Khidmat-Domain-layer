# Khidmat Risk Domain — Governance and Documentation

**Authority:** Knowledge Layer Architect
**Source:** Companion governance document for `shared/risk/*.yaml`
**Purpose:** Boundary enforcement rules, cross-domain relationship patterns,
anti-patterns, and alignment contracts for the Risk Domain. Written as a
standalone governance document — following the remediation pattern
established for `health-conditions.yaml` — so that ontology files stay
free of documentation bloat.

---

## Boundary Enforcement Rules

These rules govern what the Risk Domain may and may not define.

1. **No lifecycle definitions.** Risk files reference `lifecycle-stages.yaml` by `stage_ref`. They do not define what an infant or an elderly person is, and they do not redefine stage boundaries.
2. **No capability definitions.** Risk files reference `capabilities.yaml` by `domain_ref` and reuse its four-level scale (`full`, `functional`, `partial`, `minimal`) by value, never by redefinition.
3. **No dependency definitions.** Risk files reference `dependency.yaml` by `dependency_ref`. They do not define what caregiving or financial dependency means.
4. **No family role or family structural attribute definitions.** Risk files reference `family-structure.yaml` by `role_ref` or `attribute_ref`. They do not redefine kinship roles, support roles, or structural attributes such as `single_provider_household` or `family_support_network`.
5. **No health condition definitions.** Risk files reference `health-conditions.yaml` by `condition_ref` and reuse its `disability_potential` and `condition_caregiver_intensity` attributes by value.
6. **No need, claim, or situation definitions.** Risk files reference `registration/taxonomy/needs.yaml` and `registration/taxonomy/situations.yaml` by `need_ref` / `trigger_event_ref`. They do not redefine need categories or trigger events.
7. **No geographic or temporal hazard instantiation.** Hazard Category is a qualitative classification only. Geography, dates, and calendars belong to the Community Context Domain (Stage 8).
8. **No scores.** Risk, Vulnerability, and Resilience are qualitative levels. No file in this domain may introduce a numeric composite, weighted sum, or index.
9. **No intervention or action logic.** This domain produces signals (risk level, risk trend, compound risk flags). It does not define what should be done in response. That is Case Management (Stage 5).
10. **No longitudinal tracking or cross-household aggregation.** This domain composes a single case at a single point in time. Tracking change for one household across time is Beneficiary Lifecycle (Stage 7). Aggregating across many households is Community Context (Stage 8).

---

## Cross-Domain Relationship Patterns

These patterns formalise how Risk Domain files reference other domain
files. Every Risk Domain file that cites an external concept must use one
of these patterns rather than inventing an ad hoc reference shape.

### Pattern: Capability Gap Reference

**Description:** How a risk factor relates to a capability domain falling
below `full`. References `capabilities.yaml` by `domain_ref`.

**Required Fields:**
- `domain_ref`: `"capabilities.yaml#{domain_id}"`
- `qualifying_level`: one of `functional`, `partial`, `minimal` (the
  capability level at or below which this risk factor is considered present)
- `relevance_note`: text describing why this capability gap is risk-relevant

**Boundary Note:** Does not redefine capability levels or domains. Only
describes which existing level qualifies as risk-relevant.

### Pattern: Dependency Concentration Reference

**Description:** How a risk factor relates to a dependency relationship
becoming concentrated in a single provider. References `dependency.yaml` by
`dependency_ref`.

**Required Fields:**
- `dependency_ref`: `"dependency.yaml#{dependency_type_id}"`
- `concentration_condition`: text describing the concentration pattern
  (e.g., single provider for multiple dependents of this dependency type)

**Boundary Note:** Does not redefine dependency types. Only describes the
risk-relevant concentration pattern.

### Pattern: Health Condition Reference

**Description:** How a risk factor relates to a health condition.
References `health-conditions.yaml` by `condition_ref`.

**Required Fields:**
- `condition_ref`: `"health-conditions.yaml#{condition_id}"`
- `reuses_attribute`: one of `disability_potential`,
  `condition_caregiver_intensity` (the condition-file attribute this risk
  factor's severity reasoning draws on)

**Boundary Note:** Does not redefine condition properties. Reuses the
existing attribute by value.

### Pattern: Lifecycle Stage Reference

**Description:** How a risk factor relates to a lifecycle stage's
characteristic vulnerability. References `lifecycle-stages.yaml` by
`stage_ref`.

**Required Fields:**
- `stage_ref`: `"lifecycle-stages.yaml#{stage_id}"`
- `formalises`: a short quoted phrase from that stage's
  `characteristic_vulnerabilities` or `reasoning_implications` that this
  risk factor formalises into the risk vocabulary

**Boundary Note:** This is the formal resolution mechanism for the
lifecycle-stages.yaml alignment flag (see Alignment Contracts below). It
does not modify `lifecycle-stages.yaml` — the narrative text there remains
as-is; this pattern only maps it forward into a named risk factor.

### Pattern: Family Structural Attribute Reference

**Description:** How a risk or protective factor relates to an existing
structural attribute already defined in `family-structure.yaml` Part 7.
References that file by `attribute_ref`.

**Required Fields:**
- `attribute_ref`: `"family-structure.yaml#{section}.{attribute_id}"`
- `qualifying_value`: the value of that attribute which makes this risk or
  protective factor present (e.g., `single_provider_household: true`)

**Boundary Note:** Does not redefine the structural attribute. Only
attaches risk/protective significance to an existing value.

### Pattern: Registration Reference

**Description:** How a risk factor relates to a registration-owned
trigger event or need category. References `registration/taxonomy/` files.

**Required Fields:**
- `trigger_event_ref` or `need_category_ref`: pointer into the owning
  registration taxonomy file
- `relevance_note`: text describing the risk relevance

**Boundary Note:** Does not redefine trigger events or need categories.

### Pattern: Persistence Source Reference

**Description:** How a risk factor's persistence (how long the
risk-generating condition lasts) is determined. Used in `vulnerability.yaml` and `exposure.yaml`.

**Required Fields:**
- `persistence_source`: one of `situation_ref`, `need_ref`,
  `condition_ref`, `none`
- If not `none`: a pointer to the owning file's duration-equivalent
  attribute (`situation.trajectory`, `need.need_duration`,
  `condition.typical_progression` / `reversibility`)
- If `none`: a `local_persistence` value from the
  `risk_factor_persistence` vocabulary defined in `vulnerability.yaml` and `exposure.yaml`,
  used only for risk factors with no existing duration-equivalent owner

**Boundary Note:** This pattern exists specifically to prevent the Risk
Domain from inventing a fourth general-purpose duration taxonomy when three
already exist (situation trajectory, need duration, condition progression).
Local persistence values are a narrow exception for genuinely unowned
cases (chiefly environmental/structural risk factors).

---

## Boundary Notes and Anti-Patterns

### What This Domain Does NOT Own

- This domain does not own lifecycle, capability, dependency, family, or health condition definitions. It references all of them by `*_ref`. If a paragraph could be copied into one of those files, it does not belong here.
- This domain does not own need, claim, or situation definitions. It references registration's taxonomies. It does not duplicate `need_severity`, `information_sufficiency`, or `trajectory` — note specifically that `situation.trajectory` (retrospective, how a situation developed) is a distinct concept from `risk.risk_trend` (prospective, whether risk is changing). The two are never merged or treated as synonyms anywhere in this domain.
- This domain does not own geography, seasonal calendars, or hazard instantiation. `hazard-categories.yaml` defines categories and a qualitative, non-geographic seasonality note only. Any file that adds dates, regions, or a calendar structure to a hazard category is in violation of this boundary and that content belongs in the future Community Context Domain.
- This domain does not define numeric scores, weighted formulas, or composite indices for Risk, Vulnerability, or Resilience. All three are qualitative levels.
- This domain does not define interventions, eligibility criteria, or prioritisation logic. It defines risk signals; Case Management (Stage 5) decides what to do about them.
- This domain does not track change over time for a single household across multiple registrations. That is Beneficiary Lifecycle (Stage 7). The Risk Domain's `risk_trend` is a single-point, current-best-assessment classification, not a tracked series.
- This domain does not aggregate Vulnerability, Resilience, or Risk across multiple households into an area-level signal. That is Community Context (Stage 8), which consumes this domain's concepts by reference rather than redefining them.
- This domain does not define outcome or change-classification vocabulary (improved/unchanged/deteriorated/exited). That is the Outcome Layer (Stage 6). Risk Trend and Outcome change-classification are conceptually adjacent (both describe direction of change) but operate on opposite time arrows and must never be merged into one taxonomy.

### What This Domain Owns That Nothing Else Owns

- Risk, Vulnerability, Resilience, Hazard Category, and Exposure as concepts
- Risk Factor and Protective Factor taxonomies (concept layer)
- Risk Horizon vocabulary
- Risk Factor Persistence vocabulary (local-only, for unowned risk factors)
- Risk Trend vocabulary
- Compound Risk concepts: concentration compounding and interaction compounding
- Compound risk detection reasoning

---

## Alignment Contracts

### Lifecycle Stages Alignment (new flag — FLAG-005)

**Contract Source:** `lifecycle-stages.yaml` `characteristic_vulnerabilities`
and `reasoning_implications` fields, written before the Risk Domain existed
as a descriptive anticipation of risk concepts.

**Resolution:** `vulnerability.yaml` and `exposure.yaml` formalise selected lifecycle-stage
vulnerabilities into named risk factors using the Lifecycle Stage Reference
pattern above. The narrative text in `lifecycle-stages.yaml` is **not**
modified — it remains valid descriptive context. The formal vocabulary now
lives in `vulnerability.yaml` and `exposure.yaml`. This mirrors exactly how FLAG-004 was
resolved between `lifecycle-stages.yaml` and `capabilities.yaml`.

**Status:** Resolved at time of Risk Domain implementation. Recorded
formally in `ontology_authority_matrix.md` as FLAG-005.

### Family Structure Alignment

**Contract Source:** `family-structure.yaml` Part 7 (`family_level_attributes`)
and its own `future_ontology_opportunities` entry: "Family resilience
model... requires both this file and the risk domain to be active."

**Resolution:** `household-resilience.yaml` and `protective-factors.yaml`
compose `family-structure.yaml`'s existing structural attributes
(`dependency_burden`, `earning_structure`, `caregiving_structure`,
`decision_making_structure`, `family_support_network`) rather than
redefining them. No new structural attribute is added to
`family-structure.yaml`. Where a genuinely new protective factor is needed
(financial buffer, insurance, community standing) it is defined in
`protective-factors.yaml` as new vocabulary, not retrofitted into
`family-structure.yaml`.

**Status:** Resolved.

### GLOSSARY.md Stub Alignment

**Contract Source:** `GLOSSARY.md` already contained placeholder
definitions for **Vulnerability**, **Risk Factor**, and **Household
Resilience** under "Risk and Vulnerability Terms," written before this
domain existed.

**Resolution:** Those definitions are updated to match the formal
definitions in this domain exactly, and the missing terms (**Risk**,
**Protective Factor**, **Hazard**, **Exposure**, **Risk Horizon**,
**Risk Trend**, **Compound Risk**) are added to the same section.

**Status:** Resolved as part of this implementation.

---

## Future Extensions

### Concept: Risk Factor Presence Detection (General)

**Belongs In:** A future extension of `registration/reasoning/` or a
later Risk Domain reasoning file, once case-level data exists to detect
against in production.

This implementation includes compound risk detection (concentration and
interaction compounding) because those patterns can be detected directly
from registration's existing `situation.trigger_event` and
`family-structure` support-role data. General single-factor risk presence
detection (e.g., automatically flagging every capability-gap-based risk
factor whenever a capability is recorded as `minimal`) is left for a later
pass — it requires the capability and dependency instance data to actually
be collected during registration first, which is itself a known gap
(`functional_capacity`/capability fields are currently dormant per
`knowledge_layer_inventory.md`).

### Concept: Hazard Instantiation and Seasonal Calendar

**Belongs In:** Community Context Domain (Stage 8)

`hazard-categories.yaml` defines categories and a qualitative seasonality
note. The actual calendar — which district enters monsoon in which month —
requires the geographic hierarchy that `shared/taxonomy/locations.yaml`
does not yet have. Stage 8 consumes hazard categories by reference; it
does not redefine them.

### Concept: Cross-Household Vulnerability and Resilience Aggregation

**Belongs In:** Community Context Domain (Stage 8)

Area-level concentration of vulnerable households is an aggregation
operation over this domain's per-household Vulnerability and Resilience
outputs, not a new definition of either concept.

### Concept: Risk Trend Tracking Over Time

**Belongs In:** Beneficiary Lifecycle Domain (Stage 7)

`risk.yaml` defines Risk Trend as a single-point snapshot classification.
Tracking how that classification changes across a household's repeated
registrations requires the persistent Person/Household/Family entity that
Stage 7 introduces.

### Concept: Risk-Informed Intervention Eligibility

**Belongs In:** Case Management Domain (Stage 5)

Whether a given risk level or compound risk flag should change
intervention urgency or eligibility is an operational decision that
belongs to Case Management, which consumes this domain's signals by
reference.

---

*Governance document authored at Risk Domain implementation, Phase 3.0.*
*Authority: Knowledge Layer Architect.*