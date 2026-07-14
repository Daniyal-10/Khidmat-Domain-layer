# Registration Content Completion Sprint — Review Document

> **Status:** DRAFT FOR REVIEW. No YAML has been modified. This document proposes
> wording for all 19 records in the Registration Content Gap Log
> (`Registration_Migration_Plan.md`). Nothing here is applied until you approve
> the wording, record by record or as a whole.
>
> **This is content authoring, not migration.** No id was added, renamed, or
> removed. No concept was added. No ownership changed. No reasoning or runtime
> behavior is introduced. Every proposed description explains purpose and
> boundary only.

---

## Sources consulted (per your instruction, in priority order)

1. `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` — read in full.
2. `registration/README.md` — confirmed empty (0 bytes); no content to draw from.
3. ADRs — `ADR-002` (situation contextualises need), `ADR-003` (claim quality is
   two-dimensional), `ADR-005` (claim basis inherited from registrant),
   `ADR-008` (single ownership of concepts).
4. Repository architecture decisions — `Registration_Migration_Plan.md` (D1–D6),
   `Repository_Migration_Methodology.md`.
5. Existing registration ontology/taxonomy — all 9 taxonomy files, `entities.yaml`,
   `relationships.yaml`, and, for cross-checking meaning (not copying), the
   registration reasoning files (`severity-rules.yaml`, `gap-detection-rules.yaml`).
6. Repository consistency — cross-checked against `shared/taxonomy/persons.yaml`,
   `case-management/taxonomy/`, `gaps/gap-types.yaml` specifically to rule out
   duplicate meaning (detailed per record below).

---

## 1. `actors.yaml` — `registrant_types` (scheme)

**Proposed description:**
> Classifies the role of the person conducting the registration conversation,
> and thereby the epistemic starting point for the claims made in it. Every
> case has exactly one registrant, classified as the beneficiary registering
> directly, a proxy registering on the beneficiary's behalf, or a volunteer
> registering after a field encounter. Proxies are further distinguished by
> their relationship to the beneficiary (family member, community member, or
> professional advocate). This scheme governs who is speaking, not the
> beneficiary being spoken about, and not the per-claim epistemic weight of
> what is said — that is `claim_basis`, a separate scheme in this file.

**Why this wording is correct:** it states what the scheme classifies (the
registrant's role), names its members at the level already fixed by the
existing concepts (no new content beyond what's already in the file), and
draws the one boundary a reader could plausibly get wrong — confusing
"registrant role" with "claim epistemic weight," which are deliberately
separate schemes in the same file (the file's own `purpose:` already
distinguishes "roles and epistemic relationships" as two things).

**Business Blueprint alignment:** the Blueprint doesn't name registrant roles
directly (they're a registration-process concept, not one of its Human/Family/
Household/Needs/Vulnerability/Risk/Support/Outcome models), so this is framed
as supporting the Blueprint's philosophy — knowing *who is speaking* is what
lets the system correctly weigh "why do they need it" and "who else is
affected" rather than treating every statement as equally first-hand.

**Duplicate-meaning check:** `shared/taxonomy/persons.yaml#person_roles`
already lists `beneficiary`/`registrant`/`proxy`/`volunteer` as role
*identities* — this description does not redefine those identities, it
describes what the *registration-specific* grouping of them means, matching
the file's existing note ("Person base vocabulary is in
`shared/taxonomy/persons.yaml`").

**ADR-008 / ownership check:** consistent with D4 (`Registration_Migration_Plan.md`)
— `shared` owns the role identities, registration owns the epistemic/behavioral
detail. No new duplication introduced; D4's eventual reference conversion
(Phase 5) is unaffected by this wording.

---

## 2. `needs.yaml` — `need_categories` (scheme)

**Proposed description:**
> Classifies the substantive domain of a need — the area of life in which the
> gap between a household member's current state and a basic standard exists.
> This is the registration domain's working realization of the Business
> Blueprint's Needs Model (food, health, education, housing, and livelihood
> needs, plus protection needs such as widow or child-protection support):
> food, medical, shelter, education, livelihood, and psychosocial. Each
> category carries its own subtypes describing qualitative differences in need
> *type*. This scheme does not describe how long a need persists
> (`need_duration`) or how urgent it is (`need_severity`) — both separate
> schemes in this file.

**Why this wording is correct:** it names the classification axis (substantive
domain), explicitly cross-references the two schemes a reader could confuse it
with (duration, severity) using language the file's own `purpose:` already
uses ("Subtypes describe qualitative differences in need type, not duration").

**Business Blueprint alignment:** Blueprint §7 (Needs Model) lists exactly six
need areas — Food, Health, Education, Housing, Livelihood, Protection — which
map to the six existing category ids (`medical` realizes "Health Needs",
`shelter` realizes "Housing Needs", `psychosocial` realizes "Protection Needs"
— its existing subtypes `grief_and_bereavement`, `caregiver_burden`, and
`domestic_violence_aftermath` match the Blueprint's protection examples
"widow support," "elder care," and family-safety support). No renaming
proposed — this is stated as consistency, not a mapping to enforce.

**Duplicate-meaning check:** none — `need_duration` and `need_severity` are
temporal/urgency axes, not substantive-domain axes; already distinguished in
the file's existing `purpose:`.

**ADR-008 / ownership check:** `need_categories` is registration-owned,
undisputed elsewhere in the repository (no cross-domain match found in the
prior verification pass). No change.

---

## 3. `needs.yaml` — `need_duration` (scheme)

**Proposed description:**
> Classifies how long a need is expected to persist once addressed — a
> temporal dimension of the need, independent of its substantive domain
> (`need_categories`) and its urgency (`need_severity`). Ranges from a single
> intervention that fully resolves the need (`one_time`) to an ongoing
> condition with no foreseeable resolution (`long_term`). This describes the
> need's own expected duration; it is distinct from
> `support_intervention.requested_duration` (`registration/ontology/attributes.yaml`),
> which describes how long the *requested assistance* is expected to run and,
> per that attribute's own notes, typically but not always mirrors this value.

**Why this wording is correct:** states the axis, distinguishes it from its
two siblings in this file, and proactively resolves the one real
near-duplicate found in the repository (`support_intervention.requested_duration`
shares the identical four-value set) by citing that attribute's own existing
note rather than treating the match as an error.

**Business Blueprint alignment:** the Blueprint doesn't specify duration
categories directly; this is registration-process detail supporting its
"what will happen if the need is unmet" question — duration bears directly on
urgency and prioritisation.

**Duplicate-meaning check:** the near-duplicate (`requested_duration`) is
explicitly addressed above, not silently ignored; it is a distinct field on a
distinct entity (the intervention, not the need) that happens to share the
same value vocabulary, which the attribute's own pre-existing note already
acknowledges.

**ADR-008 / ownership check:** no ownership conflict; `need_duration` is
registration-owned and uncontested.

---

## 4. `needs.yaml` — `need_severity` (scheme)

**Proposed description:**
> Classifies the urgency and life-impact of a need, independent of its
> substantive domain (`need_categories`) or expected duration
> (`need_duration`). The four levels are classified using the deterministic,
> category-specific conditions in `registration/reasoning/severity-rules.yaml`
> — for example, a critical food need and a critical medical need have
> different concrete triggers, but both represent an immediate threat to
> survival or health within their category. This is a **temporary, local**
> scheme (architectural decision D5, `Registration_Migration_Plan.md`): the
> canonical, cross-domain definition of need severity is owned by
> `needs-assessment/taxonomy.yaml#need_severity`, and this scheme will be
> reconciled with it once that domain migrates and the repository's
> cross-domain reference mechanism exists. Until then, these four levels are
> the actual classification used by registration's case-closure and readiness
> rules.

**Why this wording is correct:** it states the axis, distinguishes it from its
two siblings, explains *why* the definition is phrased at the level of
"category-specific conditions apply a shared concept" rather than restating
any one category's exact wording, and is explicit about the scheme's
temporary, local status so no reader mistakes it for the eventual
cross-domain canonical definition.

**Business Blueprint alignment:** Blueprint §9 (Risk Model) frames urgency in
exactly this register — "Hunger," "Medical deterioration," "School dropout" as
current risks needing response now, versus longer-horizon future risks — the
four severity levels are registration's operational translation of that
urgency spectrum at intake.

**Duplicate-meaning check:** cross-checked against `case-management/taxonomy/#priority_level`,
which uses the identical value labels (`critical`/`high`/`medium`/`low`) but
is a **different concept** — that scheme's own description already states it
is "independent of vulnerability, risk, and need severity" (operational
workload sequencing, not need intensity). Also cross-checked against
`gaps/gap-types.yaml`'s `severity` field, which grades *missing-information*
severity, not need intensity — a different axis entirely. Neither is a
duplicate of this concept.

**ADR-008 / ownership check:** this is the case the prior verification pass
flagged explicitly. The proposed wording does **not** copy
`needs-assessment/taxonomy.yaml`'s text (which would violate ADR-008's
single-ownership rule) and does not claim to be the canonical definition — it
states plainly that it is a temporary local scheme pending reconciliation,
consistent with D5 as already approved.

---

## 5–8. `needs.yaml` — `need_severity` concepts: `critical`, `high`, `medium`, `low`

These four are synthesized from the shared pattern already present across all
six categories in `registration/reasoning/severity-rules.yaml` (no single
category's wording is copied verbatim; the commonality across categories is
described, which is authoring, not migration).

**`critical`:**
> The need threatens life, safety, or the collapse of the household's basic
> survival mechanisms if not addressed immediately. Across need categories
> this includes conditions such as a household with no food, a treatment
> delay that threatens life, no safe place to sleep, or a household with no
> income, savings, or family support (see `severity-rules.yaml` for the exact
> category-specific conditions). A critical need requires immediate response
> and, where it coincides with a risk to a person's safety, may also require
> the safety assessment recorded on the `situation` entity.

**`high`:**
> The need causes significant hardship or carries a firm, near-term deadline,
> but does not yet threaten life or safety directly. Across need categories
> this includes conditions such as a household eating fewer than two meals a
> day, a treatment with a deadline within days, or an eviction risk within the
> month (see `severity-rules.yaml`). A high-severity need is prioritised ahead
> of medium and low needs.

**`medium`:**
> The need represents a real but currently manageable gap — the household is
> coping, though strain is evident, and the gap should be addressed within a
> reasonable timeframe rather than immediately. Across need categories this
> includes conditions such as a household managing but struggling, or a
> confirmed condition with an existing treatment plan and no imminent
> deadline (see `severity-rules.yaml`).

**`low`:**
> The need is a quality-of-life or preventive concern rather than an active
> hardship — the household's basic standard is currently met, but a specific
> gap remains that should be scheduled for response. Across need categories
> this includes conditions such as food that is available but nutritionally
> inadequate, or preventive and monitoring care for an already-manageable
> condition (see `severity-rules.yaml`).

**Why this wording is correct:** each states the general pattern that
`severity-rules.yaml` already applies six times over (once per category)
without inventing a new criterion or contradicting any category's existing
condition — it names the shared thread and points to the existing file for
the operative detail, rather than duplicating that detail here.

**Business Blueprint alignment:** mirrors Blueprint §9's own framing of
current risk ("Hunger," "Medical deterioration") as the register for the most
urgent tier, versus the more measured, preventive register implied for lower
tiers.

**Duplicate-meaning check:** same as `need_severity` above — `priority_level`
(case-management) and gap `severity` (gap-types.yaml) are both distinct
concepts; not duplicated by these four value descriptions.

**ADR-008 / ownership check:** same as `need_severity` above — no text copied
from `needs-assessment/taxonomy.yaml`; explicitly local and temporary.

---

## 9. `claims.yaml` — `claim_types` (scheme)

**Proposed description:**
> Classifies the subject matter of an assertion made during registration —
> what kind of fact the registrant is asserting — independent of how much is
> known about it (`information_sufficiency`) or whether it holds together
> internally (`information_consistency`), both separate schemes in this file.
> The four types correspond to the four things a registration conversation
> must establish: who the beneficiary is (`identity_claim`), what
> circumstances created the vulnerability (`situation_claim`), what concrete
> need exists (`need_claim`), and who else in the household is affected
> (`household_claim`). A `situation_claim` is what the registrant *says* about
> their circumstances; it is distinct from the `situation` entity itself
> (`registration/ontology/entities.yaml`), which is the AI's structured record
> built from one or more claims.

**Why this wording is correct:** states the axis, cites the two sibling
schemes (sufficiency/consistency) this could be confused with — directly
matching the file's own `purpose:` framing of "two independent dimensions" —
and proactively separates `situation_claim` (an assertion) from `situation`
(an entity), the one genuine confusion risk in this file given they share a
root word.

**Business Blueprint alignment:** the four claim types map directly onto
Blueprint §2's four core questions — "What does this person need?" (`need_claim`),
"Why do they need it?" (`situation_claim`), "Who else is affected?"
(`household_claim`) — plus the beneficiary identity Blueprint §3 (Human Model)
requires before any of those questions can be answered.

**Duplicate-meaning check:** `situation_claim` vs. the `situation` entity and
its taxonomy (`trajectory`/`trigger_events`/`affected_domains` in
`situations.yaml`) are explicitly distinguished above — claims are what is
*said*; situations are the AI's structured understanding built from claims,
per `ADR-002`.

**ADR-008 / ownership check:** no conflict; registration-owned, uncontested.

---

## 10. `evidence.yaml` — `evidence_types` (scheme)

**Proposed description:**
> Classifies the broad form evidence takes when it may support or refute a
> claim during field verification: documents and official records
> (`documentary`), direct field observation of physical conditions
> (`physical`), and third-party corroboration (`testimonial`). Documentary
> subtypes are owned by `shared/taxonomy/document-types.yaml`, not duplicated
> here; physical and testimonial subtypes are registration-owned observation
> categories used during the volunteer field visit. This scheme classifies
> the *form* evidence takes, not how accessible a specific piece of it is
> (`availability_classifications`, a separate scheme in this file), and not
> which evidence types are expected for a given claim type (that mapping is
> `registration/reasoning/evidence-rules.yaml`, relocated from this file per
> architectural decision D3).

**Why this wording is correct:** states the axis, correctly attributes
`documentary`'s subtype ownership to `shared/taxonomy/document-types.yaml`
(matching the file's own existing note under the `documentary` concept),
distinguishes this scheme from its sibling (`availability_classifications`),
and correctly notes the claim-type mapping now lives elsewhere per the
already-approved D3 decision — avoiding restating content that has already
moved out of this file.

**Business Blueprint alignment:** supports Blueprint §2's requirement that
claims be verifiable ("what will happen if unmet" requires confirming the
claim is true); the Blueprint does not itself define evidence categories, so
this is registration-process detail in service of that requirement.

**Duplicate-meaning check:** cross-checked against
`verification-operations/taxonomy/verification-methods.yaml`, which
explicitly disclaims defining evidence types ("This file does not define
evidence types... does not redefine evidence vocabulary") — confirms
registration is the sole owner of `evidence_types` itself, with
`document-types.yaml` owning only the documentary subtype vocabulary.

**ADR-008 / ownership check:** consistent with the existing, undisputed split
between `evidence_types` (registration-owned) and document subtypes
(shared-owned).

---

## 11. `evidence.yaml` — `availability_classifications` (scheme)

**Proposed description:**
> Classifies how a specific piece of identified evidence can actually be
> accessed, independent of what form it takes (`evidence_types`). Ranges from
> evidence already uploaded digitally, through evidence a volunteer must
> inspect in person or retrieve through coordination, to evidence that is
> claimed to exist but cannot be produced. This scheme governs field-verification
> logistics; it does not affect whether the underlying claim is verifiable at
> all in principle (`claim.verifiable`, `registration/ontology/attributes.yaml`).

**Why this wording is correct:** states the axis, distinguishes it from its
sibling (`evidence_types`), and draws the one boundary a reader could
plausibly conflate — "not available" (this scheme, meaning a specific
instance can't currently be produced) versus "not verifiable" (a different,
existing attribute meaning the claim type itself cannot ever be confirmed).

**Business Blueprint alignment:** same as `evidence_types` — supports
verifiability of claims, which the Blueprint's questions depend on.

**Duplicate-meaning check:** the `claim.verifiable`/`not_available` boundary
above is the only plausible overlap and is explicitly resolved.

**ADR-008 / ownership check:** no conflict; registration-owned, uncontested.

---

## 12–19. `situations.yaml` — `trigger_events` concepts

Each of these already has a `label` and (for six of the eight) an
`inference_note`; the proposed description explains the event itself, using
the existing label and inference note as the boundary, and explicitly
resolves the one real duplicate-meaning risk each carries (a same-named or
similarly-named `need_categories` subtype that is the *consequence*, not the
*event*).

**`bereavement`** (label: "Death of Income Earner or Guardian"):
> The death of a household member who was the primary income earner,
> guardian, or caregiver, creating or worsening the household's vulnerability.
> This is the triggering event recorded on the situation; it is distinct from
> `need_categories.psychosocial.grief_and_bereavement`, which is the support
> need that may follow it. Per `ADR-002`, the situation contextualises the
> need rather than causing it — bereavement may explain an economic need, a
> psychosocial need, or both, without having caused either.

**`job_loss`** (label: "Job Loss or Business Failure"):
> The household's primary earner lost employment, or a household-run business
> failed, removing or reducing the household's income source. A triggering
> event on the situation, typically contextualising a `livelihood` need
> (`need_categories`), per `ADR-002`, without necessarily being its sole cause.

**`accident_or_injury`** (label: "Accident or Sudden Injury"):
> A sudden, unplanned physical injury or accident affecting a household
> member — distinct from a diagnosed illness (`illness_onset`) or a
> long-standing disability. Per its existing inference note, when the injury
> affects a working-age adult it typically contextualises a livelihood need;
> when it affects a child, an education disruption.

**`illness_onset`** (label: "Serious Illness Diagnosis"):
> The onset or diagnosis of a serious illness affecting a household member —
> distinct from a sudden accidental injury (`accident_or_injury`) and from a
> long-standing chronic condition with no new diagnostic event (better
> reflected in the `structural` trajectory than as a trigger event). Per its
> existing inference note, typically contextualises a medical need, and an
> economic need when the affected person is the primary earner.

**`displacement`** (label: "Displacement or Forced Relocation"):
> The household was forced to leave its home or place of residence — by
> conflict, disaster, eviction, or other compulsion. Per its existing
> inference note, typically contextualises a shelter need and a documentation
> gap, and requires a safety assessment.

**`domestic_violence`** (label: "Domestic Violence or Family Breakdown"):
> Violence or breakdown within the family or household that endangers a
> member's safety. Per its existing inference note, this always raises the
> situation's safety flag immediately, and questioning must not probe
> perpetrator detail — only whether a visit is safe. Distinct from
> `need_categories.psychosocial.domestic_violence_aftermath`, which is the
> support need that may follow this triggering event, not the event itself.

**`natural_disaster`** (label: "Natural Disaster or Environmental Event"):
> An environmental or weather-related event — such as flooding, storm damage,
> or drought — that has damaged the household's home, livelihood, or living
> conditions. Consistent with the Business Blueprint's Community Model
> (§6), which names flooding, the rainy season, heat waves, and drought as
> seasonal community risks; this concept records such an event once it has
> actually affected the household, as a situation trigger — not as a general
> community-level risk forecast.

**`legal_crisis`** (label: "Arrest, Detention, or Legal Crisis"):
> The arrest, detention, or other acute legal jeopardy of a household member.
> Per its existing inference note, typically contextualises a documentation
> gap, and an economic disruption when the affected person is the primary
> earner.

**Why this wording is correct (all eight):** each uses only the label and
inference note already present in the file, adds no new inference rule or
criterion, and resolves the one specific duplicate-meaning risk that exists
for that concept (mostly: a same-topic `need_categories` subtype that is the
consequence, not the event).

**Business Blueprint alignment:** `job_loss`→"Loss of income after injury"
and `natural_disaster`→its Community Model seasonal-risk list (§6, §9) are
direct Blueprint citations; the others align with the Blueprint's general
framing of situations as the "why" behind a need (§2) without a named
Blueprint example to cite verbatim.

**Duplicate-meaning check:** `bereavement`/`domestic_violence` each have an
explicit, named potential duplicate in `need_categories` (`grief_and_bereavement`,
`domestic_violence_aftermath`) and both are resolved by citing `ADR-002`
(situation contextualises, does not generate, the need). The other six have
no equivalently-named sibling elsewhere in the domain.

**ADR-008 / ownership check:** all eight are registration-owned, uncontested
elsewhere in the repository.

---

## Summary

| # | Record | Duplicate risk found? | Resolved how |
|---|---|---|---|
| 1 | `registrant_types` | Yes — `shared/taxonomy/persons.yaml#person_roles` | Distinguished identity (shared) from epistemic detail (registration), per D4 |
| 2 | `need_categories` | No | — |
| 3 | `need_duration` | Yes — `support_intervention.requested_duration` | Distinguished need duration from requested-assistance duration; cited existing note |
| 4–8 | `need_severity` + 4 concepts | Yes — `case-management#priority_level`, `gap-types#severity`; and `needs-assessment#need_severity` (ownership, not just meaning) | Confirmed distinct concepts for the first two; explicitly marked temporary/local and un-copied for the third (ADR-008) |
| 9 | `claim_types` | Yes — `situation_claim` vs. `situation` entity | Distinguished assertion from AI-built record, per ADR-002 |
| 10 | `evidence_types` | No (checked verification-operations, confirmed no overlap) | — |
| 11 | `availability_classifications` | Yes — `claim.verifiable` | Distinguished instance-availability from type-level verifiability |
| 12–19 | `trigger_events` (8 concepts) | 2 of 8 — `bereavement`, `domestic_violence` vs. matching `need_categories` subtypes | Distinguished event from consequence, per ADR-002 |

**Nothing has been written to any YAML file.** Awaiting your approval —
per-record or as a whole — before any file is modified.
