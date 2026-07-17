# HKMP Stage 8 — Donor & Resource Intelligence Domain Discovery Report

**Status:** Research only. No ontology, taxonomy, or governance file was modified to produce this
report. This document is the sole deliverable of the discovery pass; implementation begins only
after this report is reviewed.

**Method:** Direct inspection of the repository as it exists today (post Stage 7C certification),
not reliance on prior summaries. Every existing-concept claim below cites the file it was found
in.

---

## 1. Executive Summary

The repository has never modeled a Donor, a Grant, a Contribution, a material Resource, an
Inventory Item, a Storage Location, or any Islamic-giving concept. These are genuine gaps — no
domain currently owns them, and no domain currently claims to.

But the repository is **not** a blank canvas for Stage 8. Two prior domains — Programs and
Support Delivery — already anticipated this exact territory during their own discovery passes and
explicitly deferred it as a named, disclosed future gap rather than an oversight:

- `programs/Programs_Repository_Gap_Report.md` (Type D): *"Detailed Financial Ledgers... Grant
  Management: Tracking the lifecycle of the funding proposal that created the program."*
- `support-delivery/Support_Delivery_Repository_Gap_Report.md` (Type D): *"Logistics &
  Warehousing: Real-time fleet tracking, temperature logging sensors, warehouse inventory
  counts."*

This means Stage 8 is not discovering new scope so much as **occupying scope that was already
reserved for it**, adjacent to two mature domains (Programs, Support Delivery) that already own
the *consumption* side of funding and resources (a Program is `funded_by` an Organisation; a
`delivery_event` moves goods through `custody_transfer`/`custodian`). Stage 8's job is to own the
*supply* side: who gives, what is given, under what constraint, and what exists in stock before it
is committed to a Program or a Delivery Event.

The single largest risk is not a missing concept — it is scope overlap with **Volunteer
Operations**, whose foundational (Tier 1) layer already fully owns volunteer skills,
certifications, availability, coverage, assignment eligibility, and affiliation, governed by a
named boundary flag (FLAG-006) that a prior domain (Verification Operations) already tripped over
once. The Stage 8 brief's "Volunteers / Volunteer resources / capacity / allocation" list
re-enters that exact territory. This report recommends excluding volunteer *capability* modeling
from Stage 8 entirely (see §13).

A second material risk is silent duplication of an axis that already exists three times in
different shapes across the repo (funder macro-category, delivery form, and now proposed donor
type / resource type) — see §13 and §16.

**Readiness verdict:** Research complete. Not ready for YAML implementation until two governance
items are resolved first: (1) an ADR deciding whether `donor` is a new entity or a role-profile
attached behind `shared:person`/`shared:organisation` (mirroring the precedent already set for
`volunteer_profile` behind `shared:actor`), and (2) an explicit, written scope carve-out excluding
volunteer capability/assignment concepts from this domain. See §17.

---

## 2. Current Repository Coverage

| Concern | Owned today by | Depth |
|---|---|---|
| Who funds a Program | Programs (`program_funded_by` → `shared:organisation`) | Relationship only — no Donor entity, no funding instance |
| Funder macro-category | Programs (`funding_source_types`) | Taxonomy on the *Program*, not on a donor instance |
| Funding restriction mechanics | Programs (`funding_restrictions`, `quota_types`) | Program-level envelope rules |
| Compliance/audit of funding | Programs (`compliance_checkpoints`, `audit_findings`, `donor_waiver`, `donor_mandate`, `funding_shortfall`) | Program-governance events referencing "the funder" only informally |
| Form of assistance (cash/voucher/in-kind/service/asset) | Programs (`intervention_modality`), Support Delivery (`delivery_modality`) | Two deliberately reconciled, non-duplicating axes already exist here |
| Physical handover / custody | Support Delivery (`custody_transfer`, `custodian`, `community_representative`, `delivery_status`) | Execution-time movement only; nothing upstream of "goods enter custody" |
| Organisation as institution | Shared Ontology (`organisation`), Shared Taxonomy (`organisation_types`) | Generic institutional entity/typology; not donor-specific |
| Community-native collectives | Community Context (`local-organizations.yaml`) | Includes `local_philanthropic_trust`, `burial_or_bereavement_society`, `faith_based_organization` as *civic body types*, explicitly not overlapping `shared/taxonomy/organisations.yaml` |
| Volunteers | Volunteer Operations (foundational tier, fully built) | Comprehensive: profile, team, status, type, skills, certifications, availability, assignment-type eligibility, coverage, affiliation, training |
| Islamic giving (zakat, sadaqah, waqf, etc.) | Nobody | Zero references anywhere in the repository |
| Grant / funding commitment as an instance | Nobody | Explicitly named and deferred by Programs' own gap report |
| Material resource / inventory / warehouse | Nobody | Explicitly named and deferred by Support Delivery's own gap report |
| Resource allocation (deciding what goes where before delivery) | Nobody | No entity between Program eligibility and `delivery_event` |

---

## 3. Existing Related Concepts (with citations)

**`shared:organisation`** (`shared/ontology/entities.yaml:63-75`) — "A government body, NGO,
institution, or partner that funds, implements, operates infrastructure for, affiliates volunteers
with, or receives a Referral." This is the closest existing concept to Donor, but it is
deliberately generic — it is the single entity standing in for funder, implementer, infrastructure
operator, and referral target all at once. It carries no donor segmentation (individual vs.
institutional vs. major vs. recurring), no giving-instance history, and no religious-giving
semantics.

**`shared/taxonomy/organisations.yaml`** — classifies organisation *types*
(`hospital_or_clinic`, `ngo_or_charity`, `government_office`, etc.), explicitly reserving "detailed
organisation ontology (relationships, accountability, program participation)... for a future
organisations domain" (file purpose statement, lines 10-12). This is a second piece of evidence
that a dedicated domain in this territory was anticipated, not accidental.

**`programs/taxonomy/funding-and-compliance.yaml`** — owns `funding_source_types`
(government_statutory, multilateral_agency, private_foundation, corporate_csr, public_donations),
`funding_restrictions` (unrestricted, earmarked_geographic, earmarked_demographic,
tied_procurement), `quota_types`, `reporting_periods`, `compliance_checkpoints`, `audit_findings`.
All of these classify properties **of a Program's funding envelope**, evaluated at authoring time
of the Program — none of them is a record of an actual gift, grant, or donor relationship.
`governance-and-exceptions.yaml` additionally has `donor_waiver` and `lifecycle-and-status.yaml`
has `donor_mandate` / `funding_shortfall` — all treat "the donor" as an unmodeled external party
referenced only in prose.

**`programs:program_funded_by`** (`programs/ontology/relationships.yaml:59-63`) — `program
funded_by shared_org:organisation`, cardinality `{0, unbounded}`. The only funding *relationship*
edge in the graph today. A new Donor/Grant domain would either extend this edge's target or
interpose a `grant` entity between `organisation` and `program` (see §9).

**`programs:intervention_modality`** (`programs/taxonomy/interventions.yaml`) — cash, voucher,
in-kind, service, asset — classifies the *catalogued offering's* form. Already carries
`in_kind_goods` and `asset_transfer` concepts at a shallow level.

**`support_delivery:delivery_modality`** (`support-delivery/taxonomy/delivery-modalities.yaml`) —
physical_goods, digital/physical cash-voucher, and four service subtypes — classifies the
*handover event's* handling requirements. The file carries an explicit, carefully-written
`distinct_from` note reconciling it against `intervention_modality` and `thematic_sectors`
(lines 12-39). This is the repository's existing worked example of how to reconcile a
near-duplicate axis — Stage 8 will need at least two more such notes (see §16).

**`support-delivery/ontology/entities.yaml`** — `custody_transfer` ("a single link in the Chain of
Custody, tracking the transfer of goods between custodians before reaching the final
beneficiary"), `custodian`, `community_representative`, and `delivery_status` including a
`returned` state ("goods were successfully returned to inventory" — `delivery-lifecycle.yaml:32`).
The word "inventory" is already used descriptively here, with no entity behind it. This is the
clearest single seam where a new Resource/Inventory domain attaches: goods flow *out of* inventory
into `custody_transfer`/`delivery_event`, and flow *back into* inventory on `returned`.

**`community-context/taxonomy/local-organizations.yaml`** — `local_philanthropic_trust`,
`burial_or_bereavement_society`, `faith_based_organization`, `micro_savings_and_credit_collective`
are community-native giving/mutual-aid bodies. The file is explicit (line 103) that this is "a
genuinely separate concept space" from `shared/taxonomy/organisations.yaml` because it models
informal, community-native collectives rather than formally registered institutions. A community
or faith-based *donor* segment in the new domain would need to reference this taxonomy for
donor-organisation typing rather than re-deriving it.

**Volunteer Operations** — `volunteer_profile`, `volunteer_team`, `volunteer_status`,
`volunteer_type`, `skill_category`, `certification_type`, `availability_type`, `assignment_type`,
`coverage_type`, `language_proficiency`, `affiliation_type`, `training_status` are all fully
authored (`volunteer-operations/ontology/`, `volunteer-operations/taxonomy/`). Per
`ontology_authority_matrix.md`'s Volunteer Operations section, this is explicitly "Foundational
(Tier 1) concepts only" — the operational layer (scheduling, dispatch, workload, trust/performance
scoring, the assignment act itself) is deferred to what that section calls "the Stage-9 activation
trigger" (ADR-024 numbering — see §7 on the numbering collision this creates against the current
HKMP Stage numbering).

**`GLOSSARY.md`** carries no donor, funding, resource, inventory, or Islamic-giving terms at all
under Core Terms. It does carry a "Recovery Resources" term (line 158) — but this is a Risk-Domain
concept ("existing household-accessible assets... that can be mobilized to restore household
functioning") describing a household's *own* coping assets, not humanitarian resources supplied to
it. These must not be confused; a new `resource` entity in Stage 8 is unrelated to Risk's
`recovery_resources` and should not reuse the bare term "resource" without a qualifier that
disambiguates from it.

---

## 4. Missing Canonical Concepts

None of the following exist anywhere in the repository today:

- **Donor** as an entity or role (individual, institutional, corporate, government, foundation,
  faith-based, community, anonymous, recurring, major, emergency donor segmentation)
- **Islamic Giving** concepts of any kind — zakat, sadaqah, sadaqah jariyah, waqf, fidya, kaffarah,
  qurbani, zakat eligibility (the classical asnaf categories), restricted religious fund handling
- **Grant** / **Funding Commitment** as an instance (as opposed to `funding_source_types`, which
  classifies a Program's funding category, not a specific grant agreement)
- **Contribution / Gift / Donation transaction** — a discrete record of a specific act of giving
- **Funding cycle mechanics as instances**: funding window, funding renewal, funding expiration,
  matching funds, co-funding commitments (only `reporting_periods`, an unrelated cadence concept,
  currently exists)
- **Resource** as a canonical entity spanning financial, material, and consumable categories
- **Inventory Item**, **Asset**, **Consumable**, **Equipment** as tracked stock
- **Storage Location / Warehouse**
- **Resource Allocation** as an entity distinct from `delivery_event` (a decision/record binding a
  resource unit to a Program or Case Plan *before* execution)
- **Stock movement vocabulary**: receiving, dispatch, loss, damage, spoilage, replenishment (as
  entities/taxonomy — the *word* "inventory" appears once, descriptively, in Support Delivery, per
  §3)
- **Transportation / delivery route / cold chain** as first-class concepts (Support Delivery owns
  the handover event, not the logistics chain feeding it)
- **In-kind donation** as a resource-intake concept — `in_kind_goods` exists only as an
  *intervention modality* value (the form assistance takes when delivered), not as a donation
  intake record

---

## 5. Proposed Domain Scope

Recommend splitting Stage 8 into two cohesive sub-domains sharing a `donor_resource` shared
vocabulary root, rather than one monolithic domain — they have different owners in real
humanitarian operations (fundraising/grants desk vs. logistics/warehouse desk) and different
cross-domain dependents:

**8A — Donor & Funding Intelligence**
Donor (as role-profile, see §6), Islamic Giving taxonomy, Grant, Contribution/Gift, funding
lifecycle (window, renewal, expiration, matching/co-funding). Primary dependent: Programs
(extends `program_funded_by`).

**8B — Material Resource & Logistics Intelligence**
Resource, Inventory Item, Storage Location, stock movement taxonomy (receiving, dispatch, loss,
damage, spoilage, replenishment), Resource Allocation. Primary dependent: Support Delivery
(feeds `delivery_event` / `custody_transfer`).

**Explicitly excluded from both** (see §13): volunteer skills, certifications, availability,
capacity, deployment, or assignment — these remain 100% Volunteer Operations' concern. If Stage 8
needs to represent "a volunteer's time as a contributed resource" for donor-facing reporting
purposes, that must be modeled as a *reference* to `volunteer_profile`/`volunteer_team`, never as a
redefinition of volunteer capability.

---

## 6. Ownership Analysis

**Should `donor` be a new entity, or a role/profile behind an existing entity?**
This is the single most consequential open question and should not be silently decided by whoever
writes the first YAML file. The repository has a clear, already-litigated precedent for this
exact shape of question: FLAG-006 in `ontology_authority_matrix.md` (the volunteer
qualification-vs.-assignment boundary), resolved by attaching `volunteer_profile` *behind*
`shared:actor` via a `profile_of` relationship rather than minting a new actor entity. The same
pattern fits here: an institutional donor is already representable as `shared:organisation`; an
individual donor is already representable as `shared:person`. A new `donor_profile` entity
attaching behind whichever of the two applies (mirroring `profile_of`) would avoid duplicating
Person/Organisation identity, in the same way `volunteer_profile` avoids duplicating Actor
identity. The alternative — a standalone `donor` entity independent of Person/Organisation — risks
recreating the exact `household`/`household_snapshot` duplicate-entity conflict that FLAG-005 had
to resolve after the fact. **Recommend resolving this via ADR before implementation**, not during
it.

**Who should own Grant vs. Program's existing funding taxonomy?**
Programs already owns *program-level* funding classification (`funding_source_types`,
`funding_restrictions`). A new `grant` entity should not redefine these — it should be the missing
link Programs' own gap report named ("tracking the lifecycle of the funding proposal that created
the program"), i.e. `grant` is authored in the new domain and *referenced* by
`program_funded_by` (or a new `program_funded_by_grant` relationship supplementing it), exactly as
`case_plan_addressed_by_intervention` referenced `registration:support_intervention` rather than
Case Management re-declaring Intervention.

**Who should own Resource/Inventory vs. Support Delivery's custody chain?**
Support Delivery owns everything from the moment goods enter `custody_transfer` through
`delivery_event` to handover. The new domain should own everything *before* that boundary: what
exists, in what quantity, in what condition, at what storage location, and the decision
(`resource_allocation`) to commit a unit of it to a Program/Case Plan. `delivery_event` would
reference the new domain's `inventory_item`/`resource_allocation` as its source, the same way it
already references `case_plan` — Support Delivery does not need to redefine anything, only add a
reference row.

**Who should own the Islamic Giving taxonomy?**
Cleanly new — no existing domain touches religious-giving semantics. Zakat eligibility categories
(the classical asnaf) are a distinct concern from Programs' `eligibility_rule` (which evaluates a
beneficiary's profile generically for program qualification) and must not be modeled as another
`eligibility_rule` subtype; it should be a `zakat_eligible_category` taxonomy that a Program's
`eligibility_rule` may optionally *reference* when a Program is zakat-restricted, not a rule the
new domain evaluates itself. Note also: per ADR-022 (canonical concepts and regional localization
strategy), zakat/sadaqah/waqf/etc. are **not** regional synonyms subject to the "use the canonical
global term, not the local alias" discipline that produced e.g. `micro_savings_and_credit_
collective` replacing "SHG"/"Chama"/"Stokvel" — they are distinct religious-legal categories with
no canonical non-religious equivalent, and should be modeled as first-class concepts, not
normalized away. This distinction should be stated explicitly in the eventual taxonomy file so a
future auditor does not flag it as an ADR-022 violation by mistake.

---

## 7. Cross-Domain Dependencies

Per ADR-009 (Dependency-Driven Domain Activation), a new domain's dependency chain must be
declared before activation. Stage 8 requires:

- **Programs** (active) — target of `program_funded_by` / prospective `grant`-mediated funding
- **Support Delivery** (active) — target of resource consumption via `delivery_event`
- **Shared Ontology** (active) — `organisation`, `person` as the donor role-profile's targets
- **Community Context** (active) — `local-organizations.yaml` as a donor-typing reference for
  community/faith-based donors

No circular dependency is introduced: Programs and Support Delivery would each gain one new
*reference* row pointing into the new domain, matching the existing pattern of
`case_plan_addressed_by_intervention` (Case Management → Registration) and `offering_verified_by`
(Verification Operations → Programs) — cross-domain reference without redefinition.

**Numbering collision to flag for governance, not a defect:** `knowledge_layer_roadmap.md` already
has its own "Stage 8: Community Context" (requires Stages 3 + 7, already fully implemented) and
"Stage 9: Remaining Domain Activations." That numbering is unrelated to the "HKMP Stage N"
numbering used by the current handoff and by `STAGE6_*`/`HKMP_STAGE7*` documents — the two schemes
happen to collide at the digit 8 while referring to different work. This report uses "HKMP Stage
8" throughout per the current handoff's terminology; whoever authors the eventual ADR/roadmap
entry for this domain should explicitly disambiguate the two numbering systems so a future reader
does not conflate "HKMP Stage 8: Donor & Resource" with the roadmap's already-complete "Stage 8:
Community Context."

---

## 8. Candidate Entities

*(Candidates only — not implemented, not ratified. Final entity shape depends on the ADR in §6.)*

**8A — Donor & Funding**
- `donor_profile` (role-profile behind `shared:person` or `shared:organisation`, per §6)
- `grant` (a funding commitment instance — proposal, agreement, cycle)
- `contribution` (a discrete act of giving — one gift, one disbursement tranche)
- `funding_commitment` (possibly folded into `grant`; kept separate if institutional multi-tranche
  commitments need to be distinguished from single-gift `contribution`)

**8B — Material Resource & Logistics**
- `resource` (abstract: financial / material / human-adjacent — see §13 boundary caveat)
- `inventory_item` (a trackable unit or batch of a resource at a location)
- `storage_location` (warehouse, distribution point, cold-chain facility)
- `resource_allocation` (the decision binding an `inventory_item`/quantity to a Program or Case
  Plan, prior to `delivery_event`)
- `stock_movement` (receiving, dispatch, transfer, loss, damage, spoilage — possibly a value object
  rather than an entity, pending the same kind of decision ADR-023 already made for other
  vocabulary extensions)

---

## 9. Candidate Taxonomies

- `donor_type` (individual, institutional, corporate, government, foundation, faith_based,
  community, anonymous, recurring, major, emergency) — **must** carry a `distinct_from`
  reconciliation note against `programs:funding_source_types` (see §16)
- `islamic_giving_type` (zakat, sadaqah, sadaqah_jariyah, waqf, fidya, kaffarah, qurbani)
- `zakat_eligible_category` (the classical asnaf-derived eligible-recipient categories) —
  referenced by, not merged into, Programs' `eligibility_rule`
- `funding_restriction_type` — **only if** genuinely distinct from Programs' existing
  `funding_restrictions` scheme (unrestricted, earmarked_geographic, earmarked_demographic,
  tied_procurement); initial read suggests this scheme should be *reused by reference*, not
  duplicated — Programs already owns this axis at the program level, and a `grant`'s restriction
  shape is naturally the same vocabulary applied one level up the chain
- `resource_category` (financial, material, consumable, equipment, asset) — **must** carry a
  `distinct_from` note against `programs:intervention_modality` and
  `support_delivery:delivery_modality` (see §16)
- `resource_condition` / `resource_quality` (new — no existing analog)
- `stock_movement_type` (received, dispatched, transferred, lost, damaged, spoiled, replenished)
- `allocation_priority` / `allocation_criteria` (new — no existing analog; must not duplicate
  Programs' `eligibility_rule` or `waitlist_priority` — see §16)

---

## 10. Candidate Relationships

- `grant` → `funds` → `program` (supplements or eventually supersedes the direct
  `program_funded_by → shared_org:organisation` edge; both can coexist — direct organisational
  funding for informal/unrestricted giving, grant-mediated for formal institutional funding)
- `donor_profile` → `commits` → `grant` / `contribution`
- `contribution` → `contributes_to` → `grant` (a single gift as one tranche of a larger commitment)
- `resource_allocation` → `allocates` → `inventory_item`
- `resource_allocation` → `allocated_to` → `case_plan` (Case Management) / `program` (Programs)
- `delivery_event` (Support Delivery, referencing inward) → `fulfilled_from` →
  `resource_allocation` — authored as a Support Delivery relationship row referencing the new
  domain, matching the existing `case_plan_addressed_by_intervention` pattern, **not** authored as
  a new-domain row redefining `delivery_event`
- `inventory_item` → `stored_at` → `storage_location`
- `grant` → `restricted_by` → *(reused)* `programs:funding_restrictions` scheme, not a new one

---

## 11. Candidate Data Properties

- `donor_profile.anonymity_level` (named, disclosed_internally_only, fully_anonymous)
- `grant.funding_window_start` / `funding_window_end`
- `grant.renewal_status`
- `contribution.contribution_date`, `contribution.designated_purpose` (free-text/earmark reference)
- `inventory_item.quantity_on_hand`, `inventory_item.unit_of_measure`, `inventory_item.expiry_date`
  (for perishables — cold-chain relevant)
- `resource_allocation.allocation_date`, `resource_allocation.reserved_quantity`
- `zakat_eligible_category` as a qualifying property on `resource_allocation` or `grant`, mirroring
  how `need_severity` is referenced cross-domain rather than redefined (see Needs Assessment's
  authority-matrix pattern)

*(Illustrative only — exact property set is an implementation-phase decision, not this report's.)*

---

## 12. Candidate Semantic Constraints

- A zakat-restricted `grant`/`contribution` must only fund a `resource_allocation` whose
  beneficiary qualifies under a referenced `zakat_eligible_category` — analogous in shape to the
  existing (currently *unenforced*, per HKMP_STAGE7C's Section 2 finding) same-case constraint gap
  on `case_plan_addressed_by_intervention`. This report recommends the new domain **not repeat**
  that known gap: any zakat-restriction relationship should carry an explicit semantic constraint
  from the outset, not defer it the way the pre-existing pattern did.
- An `inventory_item` cannot be allocated (`resource_allocation`) in a quantity exceeding
  `quantity_on_hand` (basic non-negative-stock invariant).
- A `contribution` must reference exactly one `grant` or stand alone as an unrestricted one-off
  gift — must not simultaneously be both.

---

## 13. Boundary Notes

**Volunteer resources — the primary risk of this discovery pass.** The Stage 8 brief's
"Volunteers / Volunteer resources / volunteer capability / volunteer skills / volunteer
availability / volunteer assignment / volunteer capacity / volunteer specialization / volunteer
certification / volunteer deployment" list is, concept-for-concept, already owned by Volunteer
Operations (`volunteer_profile`, `skill_category`, `certification_type`, `availability_type`,
`assignment_type`, `coverage_type`, `training_status` — all foundational-tier, fully authored).
Re-authoring any of this in a Donor & Resource domain would be a direct ADR-008 (Single Ownership)
violation and would recreate exactly the kind of conflict FLAG-005 (`household` /
`household_snapshot`) had to resolve after the fact, and FLAG-006 was written specifically to
pre-empt. **Recommendation: exclude volunteer capability modeling from Stage 8 entirely.** If
donor-facing reporting genuinely needs "volunteer hours as a contributed resource" as a concept,
model it as a thin reference relationship (e.g., `contribution` → `in_kind_form` → *reference to*
`volunteer_team`/`volunteer_profile` engagement, not a redefinition) — and flag that reference for
governance review before authoring, the same way `case_plan_addressed_by_intervention` was.

**Resource vs. Recovery Resources (Risk Domain).** `shared/risk/ontology/household-resilience.yaml`
already owns `recovery_resources` — a household's own internally-mobilizable coping assets. This is
semantically unrelated to a humanitarian `resource` supplied by Khidmat, but the term collision is
real (GLOSSARY.md line 158). The new domain's entity should be named to avoid bare "resource" ambiguity
in the Glossary — e.g. `humanitarian_resource` or a clearly scoped `resource` with a Glossary
cross-reference note to `recovery_resources`, learning directly from the Stage 7C-identified
Glossary "Case" duplication (§4 of that review) rather than repeating it.

**Delivery Modality / Intervention Modality vs. Resource Category.** Three near-synonymous axes
(cash/voucher/in-kind/service/asset) would exist if Stage 8 authors a naive `resource_category`
scheme without reconciliation. `support-delivery/taxonomy/delivery-modalities.yaml` already models
the *exact* discipline needed here (an explicit `references:` block with `relation: distinct_from`
and a prose note explaining the different question each scheme answers) — Stage 8 must produce the
same for its own resource-type scheme against both existing axes before implementation, not after.

**Custody chain.** `custody_transfer`/`custodian` (Support Delivery) already model goods moving
between intermediate handlers before reaching the beneficiary. The new domain's `inventory_item`
and `storage_location` should sit strictly upstream of the first `custody_transfer`, never
duplicating or re-modeling movement once goods are in the delivery chain.

**Organisation types vs. Donor types vs. Community organisation types.** Three organisation-typing
schemes will coexist: `shared/taxonomy/organisations.yaml` (formal institution type),
`community-context/taxonomy/local-organizations.yaml` (informal community collective type,
explicitly reconciled against the first), and the proposed `donor_type` (this domain — a *funding
relationship* classification orthogonal to institution type: any of the above institution types
can *also* be a donor). This is not a conflict if `donor_type` is authored as a role/relationship
axis rather than a third organisation-type taxonomy — see §6.

---

## 14. Risks

1. **Donor entity duplication risk** — building `donor` as an independent entity rather than a
   role-profile would duplicate `person`/`organisation` identity data, the FLAG-005 failure mode.
2. **Volunteer-scope creep** — see §13; the single highest-probability governance violation if the
   Stage 8 brief's volunteer section is implemented literally.
3. **Triple-axis modality duplication** — `intervention_modality` / `delivery_modality` /
   `resource_category` all describing "cash vs. in-kind vs. service" without reconciliation notes.
4. **Zakat eligibility conflated with Programs' `eligibility_rule`** — if the new domain evaluates
   zakat eligibility itself rather than exposing a referenceable taxonomy, it duplicates rule-engine
   territory Programs already owns.
5. **Repeating the Glossary cross-reference failure** — HKMP_STAGE7C's certification review found
   exactly one new defect introduced by the last remediation pass: two unreconciled Glossary
   entries for "Case." Any new Glossary terms this domain adds (Donor, Grant, Resource, Zakat, etc.)
   must be cross-referenced against `recovery_resources`, `organisation`, and `intervention_modality`
   at authoring time, not after.
6. **ADR-009 activation-order disclosure gap** — HKMP_STAGE7C also found that a prior domain
   authored a forward-pointing relationship across activation stages without disclosing it as a
   precedent. Stage 8's dependency on Programs/Support Delivery/Community Context should be
   declared explicitly in whatever roadmap or ADR entry activates it, to avoid the same
   undisclosed-precedent finding recurring a third time.
7. **Numbering collision** (§7) — cosmetic, but worth a one-line disambiguation in governance docs
   to prevent a future reader confusing this "HKMP Stage 8" with the roadmap's already-complete
   "Stage 8: Community Context."

---

## 15. Governance Review

Per ADR-008 (Single Ownership of Concepts), no concept below may be authored until its ownership is
declared in `ontology_authority_matrix.md`. This report does not declare ownership — it identifies
what a future authority-matrix entry must decide. Two items require a new ADR before any YAML is
written, not merely a matrix entry:

- **Donor-as-role-vs-entity** (§6) — same class of decision as ADR-018 (Shared Subject Supertype)
  and the FLAG-006 resolution; deserves the same ADR-level treatment, not an informal choice made
  during implementation.
- **Volunteer-resource exclusion** (§13) — should be recorded explicitly, even though it is a
  negative decision (what the domain does *not* own), because the brief that initiated this stage
  explicitly listed volunteer concepts in scope. An unrecorded silent exclusion risks someone
  re-proposing it later without knowing it was already considered and declined.

Everything else in this report (Grant, Contribution, Resource, Inventory Item, Storage Location,
Resource Allocation, Islamic Giving taxonomy) fits the existing single-ownership pattern cleanly
and can be declared via ordinary authority-matrix entries at implementation time, following the
same template already used for Programs and Case Management's own sections.

---

## 16. Boundary Reconciliation Notes Required Before Implementation

These three near-duplicate axes must each receive a `distinct_from` note (in the style of
`delivery-modalities.yaml`'s existing note) authored *alongside* the new scheme, not retrofitted
after a Stage 7-style integrity audit finds them:

1. `donor_type` vs. `programs:funding_source_types`
2. `resource_category` vs. `programs:intervention_modality` and `support_delivery:delivery_modality`
3. `zakat_eligible_category` vs. `programs:eligibility_rule` / `programs:eligibility_categories`

---

## 17. Implementation Recommendation

1. Resolve the two ADR-level questions in §15 first (donor-as-role decision; volunteer-resource
   exclusion, recorded even though it's a non-scope decision).
2. Implement 8A (Donor & Funding) before 8B (Material Resource & Logistics) — 8A has a cleaner,
   narrower dependency surface (Programs + Shared Ontology only) while 8B additionally depends on
   Support Delivery's custody-chain concepts, which benefits from 8A's `grant`/`contribution`
   vocabulary already existing to allocate *from*.
3. Author the three §16 reconciliation notes in the same YAML change that introduces each
   colliding scheme — not as a follow-up.
4. Add authority-matrix and Glossary entries in the same pass as the entities they describe,
   cross-referencing `recovery_resources`, `organisation`, `intervention_modality`, and
   `delivery_modality` explicitly, to avoid repeating the Stage 7C-identified Glossary duplication
   failure mode.
5. Do not author any volunteer-capability concept under this domain.

---

## 18. Final Readiness Assessment

**Research: complete.** Every concept named in the Stage 8 brief has been checked against the
current repository state (not a prior audit's claims) and classified as either already owned
elsewhere (volunteers — full overlap risk), partially anticipated but not implemented (funding,
logistics — explicitly named in two domains' own gap reports), or genuinely absent (Islamic
giving, Grant, Resource, Inventory, Storage Location).

**Implementation: not ready to begin.** Two governance decisions (§6, §13/§15) are prerequisites,
not parallelizable with authoring. Once those are resolved, the domain scope, boundaries, and
reconciliation notes in this report give implementation a clear, non-duplicating path — the
domain's entities, taxonomies, and relationships are well-defined enough to author directly from
§§8–12 once the two ADR-level questions are closed.

**Recommended next step:** produce the two ADRs named in §15, then proceed to 8A implementation
per §17.
