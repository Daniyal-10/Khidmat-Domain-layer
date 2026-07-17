# HKMP Stage 8A — Architecture & Governance Decisions

**Status:** Architecture and governance design only. No ontology, taxonomy, relationship,
glossary, authority-matrix, or other repository file has been created or modified to produce this
document. All ADRs below are **drafts** — none is numbered into `architecture-decisions/`, none is
`Accepted`, none is referenced from `ontology_authority_matrix.md`. Numbering (`ADR-025` etc.) is
proposed, not reserved, since only the Knowledge Layer Architect assigns real ADR numbers at
ratification time.

**Predecessor:** `HKMP_STAGE8_DONOR_RESOURCE_DOMAIN_DISCOVERY_REPORT.md`. This document does not
take that report's conclusions on faith — Part 1 re-opens and stress-tests each one before
recommending it.

---

# Part 1 — Architecture Review

## Decision 1: Donor Identity Model

### Alternative A — Independent `donor` Entity

A standalone entity, unrelated to `shared:person`/`shared:organisation`, with its own identity,
name, and contact fields.

- **Advantages:** Simplest to author in isolation; no dependency on getting the `profile_of`
  pattern right; donor-specific fields (e.g. tax-exemption status, giving history) live in one
  place with no indirection.
- **Disadvantages:** Duplicates identity data already owned by `person`/`organisation`. A donor
  who is also, say, a community leader (`community_representative`, Support Delivery) or a
  registered `organisation` now has two disconnected identity records for the same real-world
  actor — no way to know "this donor and this NGO partner are the same entity" without an ad hoc
  reconciliation relationship invented later.
- **Repository impact:** New entity file section; no changes required to `shared/ontology/entities.yaml`.
- **Future scalability:** Poor. Every future cross-reference from Donor to Person/Organisation
  (e.g. "this major donor is also a board member," "this institutional donor is also a referral
  source") requires a bespoke reconciliation relationship, compounding over time.
- **Governance implications:** This is the exact failure mode FLAG-005 (`household` vs.
  `household_snapshot`) already occurred and had to be fixed under ADR-008 after the fact — two
  independent definitions of overlapping real-world identity. Recommending this pattern *again*
  after the repository already paid the cost of fixing it once would be a governance regression,
  not a fresh choice made in ignorance.
- **Graph implications:** Creates an identity fork. Any AI reasoning process trying to answer "what
  do we know about this person" must query two disjoint subgraphs and manually correlate them,
  since nothing formally states a `donor` and a `person` can be the same real-world individual.
- **AI reasoning implications:** A reasoning system asked "has this beneficiary's own household ever
  also been a donor" (a real, if unusual, humanitarian scenario — e.g., a graduated household
  making an in-kind zakat contribution back to the community) has no path to answer without a
  hand-authored bridge.
- **Cross-domain effects:** None immediately, but every future domain that touches identity now has
  a third identity concept to consider alongside `person`/`organisation`.

### Alternative B — Role/Profile Attached Behind `shared:person` / `shared:organisation`

A `donor_profile` entity, structurally identical in pattern to `volunteer_profile` (which attaches
behind `shared:actor` via `profile_of`), attaching behind whichever of `shared:person` or
`shared:organisation` applies to a given donor, via a new `donor_profile_of` relationship.

- **Advantages:** Reuses an already-ratified, already-implemented pattern (`volunteer_profile` /
  FLAG-006's resolution) rather than inventing a new one — lower governance risk, since the
  reviewers who will certify this domain already accepted this exact shape once. A person or
  organisation that happens to also be a donor is trivially discoverable: walk the
  `donor_profile_of` edge outward from the existing `person`/`organisation` node. No identity
  fork.
- **Disadvantages:** Requires two possible attachment targets (`person` *or* `organisation`)
  rather than one (`volunteer_profile` only ever attaches to `actor`). This is a genuine
  complication `volunteer_profile` did not have to solve — either the relationship needs two rows
  (`donor_profile_of_person`, `donor_profile_of_organisation`) or a shared supertype must be
  introduced (see Alternative C below, which resolves this cleanly). Anonymous donors (a named
  requirement in the original brief) do not cleanly attach to either `person` or `organisation` —
  requires an explicit nullable-identity carve-out, documented, not silently handled.
- **Repository impact:** New `donor_profile` entity; two new relationship rows (or one, if
  Alternative C's supertype is adopted); no changes to `person`/`organisation` entity definitions
  themselves.
- **Future scalability:** Good — matches the repository's own established idiom, so future domains
  extending Donor follow a pattern already proven twice (Volunteer Operations, and now this).
- **Governance implications:** Directly consistent with ADR-008 and the FLAG-006 precedent; least
  friction at certification/audit time, since auditors (per HKMP_STAGE7C's own method) will check
  new patterns against precedent first.
- **Graph implications:** Clean — one additional hop from existing identity nodes, not a parallel
  identity subgraph.
- **AI reasoning implications:** A reasoning system can answer "is this person also a donor" with a
  single edge traversal, and can correlate donor identity with every other role a person/
  organisation already holds (registrant, referral source, community representative, etc.)
  without new bridging logic.
- **Cross-domain effects:** None beyond the new relationship rows; Programs' `program_funded_by`
  can be extended or left alone (see Decision 3, Grant Ownership) independent of this choice.

### Alternative C — Hybrid: `donor_profile` Attaches to a New Minimal `giving_party` Supertype (parented by `subject`-style pattern, but distinct from `subject` itself)

Introduce a narrow shared supertype — call it `funding_source_party` — with exactly two
specializations pre-declared: `person` and `organisation` (both already existing), each gaining
a `can_be_donor` characteristic rather than the graph needing two attachment relationships.
`donor_profile` then attaches to `funding_source_party` with a single relationship row, and
`funding_source_party` resolves at runtime to whichever concrete entity applies.

- **Advantages:** Solves Alternative B's two-attachment-target problem with a single relationship
  row, mirroring exactly how `subject` (ADR-018) already solves the identical structural problem
  for `person`/`household` under Beneficiary Lifecycle. Reuses a pattern the repository has now
  validated twice (`subject` for Person/Household, this for Person/Organisation).
- **Disadvantages:** Introduces a new shared abstraction for a fairly narrow purpose (only Donor
  needs it today) — risks being seen as over-engineering a two-case problem into a supertype, when
  ADR-018's `subject` supertype was justified by Beneficiary Lifecycle needing to reason over
  *either* Person or Household *generically*, a broader need than Donor's. `organisation` is not
  currently a specialization of `subject` (only `person` and `household` are, per
  `shared/ontology/entities.yaml`), so this cannot simply reuse `subject` itself — it requires
  either widening `subject`'s specialization set (a change to an already-frozen, `must not be
  redefined` shared concept, explicitly prohibited by the authority matrix) or authoring a
  genuinely new, narrower supertype parallel to it.
- **Repository impact:** Highest of the three — a new shared-layer entity plus its two
  specialization relationships, in addition to `donor_profile` itself.
- **Future scalability:** Best in the abstract (any future "can this be a funding party" question
  reuses the supertype), but speculative — no second consumer of `funding_source_party` exists
  today, so this is scalability paid for before it's needed.
- **Governance implications:** Would require its own ADR justifying a new shared supertype (a
  Shared Ontology change, the highest-scrutiny category per the authority matrix's own structure),
  on top of the Donor-model ADR — two governance artifacts where Alternative B needs one.
- **Graph implications:** Cleanest possible shape, but adds one extra hop (`donor_profile` →
  `funding_source_party` → concrete entity) versus Alternative B's direct two-row attachment.
- **AI reasoning implications:** Marginally better than B for a hypothetical future "is X eligible
  to be a funding source" query, but no current requirement exercises this advantage.
- **Cross-domain effects:** Touches Shared Ontology, which every domain depends on — the widest
  blast radius of the three alternatives for a decision only Stage 8 currently needs.

### Recommendation

**Alternative B (Role/Profile Attached Behind `shared:person` / `shared:organisation`)**, with its
disadvantage (two attachment targets) accepted and handled explicitly by two relationship rows
(`donor_profile_of_person`, `donor_profile_of_organisation`) rather than solved by inventing a new
shared supertype. Alternative C is not without merit but pays a Shared Ontology governance cost
disproportionate to a need only one domain currently has; if a second future domain independently
needs a Person-or-Organisation abstraction, that is the moment to revisit C — not now, speculatively.
Alternative A is rejected outright: it re-creates a failure mode this repository has already paid
down once (FLAG-005) with full knowledge of the cost.

This becomes **ADR-DRAFT-A** in Part 2.

---

## Decision 2: Volunteer Operations Boundary

### Alternative A — Full Exclusion (Stage 8 references `volunteer_profile`/`volunteer_team` only, owns nothing volunteer-related)

Stage 8 never authors a volunteer concept. If donor-facing reporting needs "volunteer hours
contributed," it is modeled as a relationship from a Stage 8 entity (e.g. `contribution`) to the
existing `volunteer_team`/`volunteer_profile`, with no new taxonomy.

- **Advantages:** Zero ADR-008 risk. Zero duplication. Matches the discovery report's
  recommendation exactly and requires no new Volunteer Operations concept at all.
- **Disadvantages:** If a genuine donor-facing need exists to *quantify* volunteer contribution as
  a resource (e.g., "this grant funded 200 volunteer-hours of distribution labor"), there is no
  natural place to record the *quantity* — `volunteer_profile`/`volunteer_team` are structural
  entities (who/what team), not time-logging entities, and Volunteer Operations' own foundational
  tier explicitly defers "assignment history" (a Tier 2 / Stage-9 concept per ADR-024) that would
  be the natural home for hours-logged data.
- **Repository impact:** Minimal — one new relationship row referencing existing Volunteer
  Operations entities, if and when needed.
- **Future scalability:** Good for avoiding duplication; weak for donor reporting that needs
  quantified labor contribution, which has no owner under this alternative until Volunteer
  Operations' Tier 2 activates.
- **Governance implications:** Cleanest possible reading of ADR-008 and FLAG-006.
- **Graph implications:** No new nodes in volunteer-adjacent territory; a thin new edge only if
  needed.
- **AI reasoning implications:** A reasoning system can state "this team was engaged by this
  contribution" but cannot currently answer "how many volunteer-hours did this grant fund" without
  Tier 2 data that doesn't exist yet — an honest limitation, not a modeling gap.
- **Cross-domain effects:** None beyond one optional reference row.

### Alternative B — Stage 8 Owns a Thin "Contributed Labor" Value, Referencing but Not Redefining Volunteer Entities

Stage 8 authors a narrow value object (not an entity) — e.g. a `contributed_labor` field/value
object on `contribution`, holding a quantity and a reference to `volunteer_team`/`volunteer_profile`
— without touching skills, certifications, availability, or the assignment act.

- **Advantages:** Solves Alternative A's quantification gap without touching Volunteer Operations'
  owned entities, if modeled strictly as a value object per ADR-023's existing value-object/entity
  distinction (the same discipline already used for `case_note` as a nested field rather than a
  full entity).
- **Disadvantages:** Sits close to the line Volunteer Operations' Tier 2 (assignment history) is
  reserved for — a future Tier 2 author could reasonably ask "isn't hours-logged our concept?" This
  requires explicit disclosure in the ADR (see Part 2) so it is not mistaken for silent scope
  creep when Tier 2 eventually activates.
- **Repository impact:** One value object, on a Stage 8-owned entity, referencing Volunteer
  Operations by CURIE only.
- **Future scalability:** Reasonable, provided the ADR explicitly reserves the *authoritative*,
  ongoing hours-tracking record for Volunteer Operations' Tier 2 when it activates, and frames
  Stage 8's version as donor-reporting-only, non-authoritative, and superseded once Tier 2 exists.
- **Governance implications:** Requires an explicit forward-looking disclosure (learning from the
  HKMP_STAGE7C finding that an undisclosed forward-stage reference is itself a defect, even when
  not a violation) — this ADR must name the Tier 2 collision risk itself, not leave it for a future
  audit to discover.
- **Graph implications:** One shallow value object; no new entity-level node.
- **AI reasoning implications:** Enables the donor-hours query Alternative A cannot answer, at the
  cost of a value that will need reconciliation (not necessarily removal) once Tier 2 exists.
- **Cross-domain effects:** Narrow, but real — the first content a non-Volunteer-Operations domain
  would author that is adjacent to volunteer *contribution accounting* rather than pure
  qualification data.

### Alternative C — No Volunteer Reference at All (Volunteers Entirely Out of Scope, Including by Reference)

Stage 8 does not reference volunteers in any form; donor-facing "in-kind" reporting is limited to
material goods and financial contributions only.

- **Advantages:** Maximally conservative; zero surface area for boundary disputes.
- **Disadvantages:** Understates real humanitarian practice — donor reports routinely include
  volunteer contribution as an in-kind valuation (a standard, not exotic, nonprofit accounting
  practice). Ignoring it entirely is a scope loss, not a scope discipline.
- **Repository impact:** None.
- **Future scalability:** Poor — this gap would likely resurface as a change request soon after
  implementation, forcing a second governance pass.
- **Governance implications:** Avoids risk by avoiding value; not a genuine architectural
  recommendation, more a null option included for completeness.
- **Graph implications / AI reasoning implications / Cross-domain effects:** None — by design.

### Recommendation

**Alternative A for the initial 8A/8B implementation, with Alternative B explicitly named as a
Phase 2 candidate, gated on its own governance review at the time it's needed** — not authored
speculatively now. This avoids Alternative B's forward-collision risk today while not foreclosing
it, and avoids Alternative C's real scope loss by keeping a documented path forward. This becomes
**ADR-DRAFT-B** in Part 2.

---

## Decision 3: Grant Ownership / Relationship to Program, Organisation, Contribution, Funding Restriction, Funding Source

### Alternative A — Grant as Mandatory Intermediary (all Program funding flows through Grant)

`program_funded_by` (organisation) is deprecated/superseded; every funded Program must reference at
least one `grant`, and `grant` alone connects to `organisation`.

- **Advantages:** Single, uniform funding model; every Program's funding is fully traceable to a
  specific grant instance with its own lifecycle, restrictions, and reporting cadence.
- **Disadvantages:** Forces informal, unrestricted, or non-institutional giving (e.g. a single
  public donation, a community `local_philanthropic_trust` contribution) through the same
  heavyweight `grant` structure a multi-year institutional funding agreement needs — a scale
  mismatch. Also requires **modifying** `programs/ontology/relationships.yaml`'s existing
  `program_funded_by` row (deprecating/removing a relationship a mature, certified domain already
  owns) — a materially higher-risk repository change than adding a new reference row, and one this
  phase does not have authority to make (no repository file may be modified in this phase; if
  ratified, it would still be the highest-impact single change this ADR could propose).
- **Repository impact:** Modifies an existing, certified relationship row in an active domain
  (Programs) — the highest-impact option among the three.
- **Future scalability:** Rigid — every future small/informal funding case must be shoehorned into
  `grant`.
- **Governance implications:** Touches a Stage-7-certified file; would need explicit sign-off
  beyond Stage 8's own governance, likely its own dedicated review given the file's certification
  history.
- **Graph implications:** Simplifies the graph to one funding path, at the cost of overfitting
  small cases to a heavyweight shape.
- **AI reasoning implications:** Simpler queries ("all Program funding traces to a Grant") at the
  cost of misrepresenting genuinely grant-less funding as if it had grant structure.
- **Cross-domain effects:** Forces Programs to change how it's queried by every existing consumer
  of `program_funded_by`.

### Alternative B — Grant as Optional Abstraction Layered Over the Existing Edge (both `program_funded_by` and `program_funded_by_grant` coexist)

`program_funded_by → organisation` is left untouched (informal/direct/unrestricted funding
continues to use it). A new, additive relationship `program_funded_by_grant → grant` is introduced
for funding that is grant-structured. `grant → funded_by → donor_profile` (or `organisation`
directly) closes the chain on the grant side only.

- **Advantages:** Zero modification to certified Programs content — purely additive, matching the
  exact pattern already used for `case_plan_addressed_by_intervention` (Case Management adding a
  reference row into Registration without touching Registration). Naturally represents the real
  humanitarian variance: a single public donation needs no grant record; a multi-year institutional
  agreement does.
- **Disadvantages:** Two parallel paths to "how is this Program funded" — a query must check both
  edges, and documentation must be explicit that they represent different funding shapes, not
  redundant paths to the same fact (this needs its own reconciliation note, in the same spirit as
  `delivery_modality`'s note against `intervention_modality`).
- **Repository impact:** Additive only — new entity (`grant`), new relationship rows; no existing
  row is touched.
- **Future scalability:** Best of the three — accommodates both informal and formal funding without
  forcing either into the other's shape, and a Program can have any mix of both.
- **Governance implications:** Lowest risk — consistent with the additive-reference pattern already
  twice certified in this repository (Case Management → Registration; Verification Operations →
  Programs via `offering_verified_by`).
- **Graph implications:** Two funding paths into `program`, clearly distinguished by which edge is
  traversed — no ambiguity if the reconciliation note is authored.
- **AI reasoning implications:** A reasoning system can distinguish "directly organisation-funded"
  from "grant-structured" programs, which is a real and useful distinction for compliance/reporting
  reasoning, not a leak of the graph's construction.
- **Cross-domain effects:** None to existing Programs consumers; new consumers opt in to the grant
  edge only when relevant.

### Alternative C — No Grant Entity at All; Extend `funding_source_types`/`funding_restrictions` With Instance-Level Fields Directly on `program_funded_by`

Rather than a new entity, add data properties (funding amount, restriction reference, cycle dates)
directly onto the existing `program_funded_by` relationship or onto `program` itself.

- **Advantages:** No new entity; smallest possible footprint.
- **Disadvantages:** Cannot represent a grant that funds *multiple* Programs (a common institutional
  pattern — one grant, several Program variants) or a grant with multiple `contribution` tranches
  over time — a relationship-level or Program-level property can't hold a many-to-many funding
  instance's own lifecycle. This directly contradicts the discovery report's core justification
  for this domain (Programs' own gap report named *"tracking the lifecycle of the funding
  proposal"* as requiring something Program-level fields cannot express). Effectively fails to
  close the gap this stage exists to close.
- **Repository impact:** Smallest, but for the wrong reason — it under-delivers the domain's
  purpose rather than minimizing risk.
- **Future scalability:** Poor — cannot express grant-to-many-programs or grant-to-many-
  contributions without a real entity.
- **Governance implications:** Would likely fail its own certification review for not actually
  solving the named gap.
- **Graph implications / AI reasoning implications / Cross-domain effects:** Minimal, because the
  concept it would need to express (a grant with its own identity and lifecycle) simply isn't
  represented.

### Recommendation

**Alternative B — Grant as an optional, additive abstraction.** It is the only option that neither
touches certified Programs content nor fails to deliver the actual gap the domain exists to close.
`contribution` relates to `grant` as a tranche (`contribution → contributes_to → grant`) or stands
alone as an unrestricted one-off gift referencing `donor_profile`/`organisation` directly (mirroring
the same "both paths valid" shape at one level down). `funding_restriction`/`funding_source_type`
(Programs, existing) are **referenced by** `grant`, not redefined — a grant's restriction shape
reuses Programs' existing `funding_restrictions` scheme rather than a new one (per the discovery
report's §16 recommendation, upheld here after re-evaluation). This becomes **ADR-DRAFT-C** in
Part 2.

---

## Decision 4: Resource Model — Resource / Inventory Item / Asset / Consumable / Equipment

### Alternative A — Flat, Independent Entities (each is its own unrelated entity)

`resource`, `inventory_item`, `asset`, `consumable`, `equipment` each authored as separate,
unrelated entities.

- **Advantages:** No inheritance complexity; each entity's schema is exactly what it needs, nothing
  inherited.
- **Disadvantages:** No way to ask "what does this Storage Location hold" generically across
  types — a query or reasoning rule must separately handle four/five entity types with duplicated
  shared fields (quantity, location, condition) copy-pasted across each. Directly contradicts the
  Canonical Ontology Schema's own preference (evidenced by `subject`, ADR-018) for a shared
  supertype wherever multiple domain concepts need common generic treatment.
- **Repository impact:** Five flat entities, four of them duplicating near-identical shared fields.
- **Future scalability:** Poor — every future resource subtype (e.g. "medicine" as a subtype of
  consumable with cold-chain fields) has nowhere to inherit from.
- **Governance implications:** Would likely draw the same criticism ADR-018 was written to resolve
  for Person/Household — a missed opportunity for a supertype where one clearly belongs.
- **Graph implications:** Fragmented; five disconnected entity types with no common traversal point.
- **AI reasoning implications:** A reasoning system asked "what is available at this warehouse"
  must union five separate entity queries rather than one.
- **Cross-domain effects:** Support Delivery's `custody_transfer`/`delivery_event` would need to
  reference up to five entity types individually rather than one common one.

### Alternative B — Single `resource` Entity With a `resource_category` Taxonomy Distinguishing Financial/Material/Consumable/Equipment/Asset

One entity (`resource`, or better, `inventory_item` as the trackable-stock entity — see naming note
below), with a `resource_category` taxonomy value distinguishing the subtypes, rather than separate
entities per subtype.

- **Advantages:** Matches the pattern this repository already uses successfully elsewhere:
  `intervention_modality` and `delivery_modality` are both single taxonomy schemes distinguishing
  fundamentally different assistance forms (cash vs. in-kind vs. service) without minting a
  separate entity per form. A financial resource, a consumable, and a piece of equipment share
  enough common structure (quantity/value, condition, location, allocation status) that one entity
  with a category value is proportionate, not reductive.
- **Disadvantages:** A financial resource (money) and a physical consumable (food) genuinely have
  different property sets (currency/amount vs. unit-of-measure/expiry-date) that a single flat
  entity handles awkwardly — either every property is optional-per-category (schema noise) or the
  entity needs sub-schemas (approaching Alternative C without naming it).
- **Repository impact:** One entity, one taxonomy; smallest footprint that still closes the gap.
- **Future scalability:** Good for taxonomy growth (new categories are new taxonomy values, not new
  entities) but weaker for category-specific property growth (a new consumable-only field pollutes
  the shared entity's schema for all categories).
- **Governance implications:** Matches existing precedent closely; low review friction.
- **Graph implications:** Single node type, filtered by category — clean traversal.
- **AI reasoning implications:** "What is available at this location" is one query; "what
  categories of resource does this location hold" is a trivial group-by.
- **Cross-domain effects:** Support Delivery references one entity type, simplifying its own
  reference surface.

### Alternative C — Shared `resource` Supertype With Specialized Subtypes (`financial_resource`, `material_resource` → `consumable`/`equipment`/`asset`)

A shallow inheritance hierarchy: `resource` (abstract supertype, owns no allocatable data itself,
exactly mirroring how `subject` "owns no demographic data") with `financial_resource` and
`material_resource` as its two immediate children, and `material_resource` further specialized by
`consumable`, `equipment`, and `asset` where genuinely distinct property sets justify it.

- **Advantages:** Directly mirrors the `subject`/`person`/`household` pattern this repository has
  already ratified (ADR-018) for exactly this situation — a common abstraction needed for generic
  reasoning (`resource`), with real property divergence pushed down to specializations rather than
  either flattened away (Alternative A) or crammed into one schema (Alternative B). `inventory_item`
  becomes the trackable-stock *instance* of any `resource` subtype at a `storage_location` — the
  entity/instance-of-a-type split is explicit rather than conflated the way Alternative B's single
  entity would conflate "the type of thing" with "a tracked unit of it."
- **Disadvantages:** Highest authoring cost of the three — most entities to define and reconcile
  before implementation. Risks over-engineering if the actual property divergence between
  `consumable`/`equipment`/`asset` turns out to be small in practice (a risk to validate during 8B
  authoring, not resolve here).
- **Repository impact:** A supertype plus 2–4 specializations plus `inventory_item` as the tracked-
  instance entity distinct from the type entities — the most files, but each with a narrow, clear
  purpose.
- **Future scalability:** Best — new resource subtypes (e.g. `medical_supply` under `consumable`)
  attach without disturbing the supertype or siblings, exactly as `capabilities.yaml`/
  `health-conditions.yaml` attach beneath the Shared Human Model without disturbing
  `lifecycle-stages.yaml`.
- **Governance implications:** Requires the clearest ADR of the three (justifying the depth of the
  hierarchy), but once ratified, is the least likely to need revision later — the `subject`
  precedent suggests reviewers will find this the most defensible shape, not the most exotic one.
- **Graph implications:** A shallow, well-typed hierarchy; `inventory_item` is the single
  traversal point for "what is on hand," typed by which `resource` subtype it instantiates.
- **AI reasoning implications:** Supports both generic reasoning ("total resource value at this
  location, across all types") and type-specific reasoning ("expiring consumables in the next 7
  days") without schema contortion.
- **Cross-domain effects:** Support Delivery references `inventory_item` (the tracked instance),
  never the type hierarchy directly — cleanest possible boundary with the custody chain.

### Recommendation

**Alternative C**, but with the hierarchy depth kept shallow and empirically justified: author
`resource` (abstract) → `financial_resource` | `material_resource` now, and defer
`consumable`/`equipment`/`asset` as full specializations *unless* 8B implementation concretely
finds their property sets diverge enough to justify separate entities rather than a single
`material_resource` with a `material_resource_category` taxonomy value (i.e., apply Alternative B's
category-taxonomy discipline *within* `material_resource`, rather than forcing three-way entity
specialization pre-emptively). `inventory_item` is the trackable-stock instance of any `resource`
subtype at a `storage_location`, distinct from the type entities themselves — this instance/type
separation is non-negotiable regardless of how deep the type hierarchy ultimately goes, because
without it there is no way to represent "200kg of this specific food type currently in this
specific warehouse" as distinct from "food, as a category of resource." This becomes
**ADR-DRAFT-D** in Part 2.

---

# Part 2 — ADR Drafts

> **Numbering note:** The repository's real next available ADR number is ADR-025 (ADR-024 is the
> last `Accepted` entry in `architecture-decisions/README.md`'s index as of this review). The
> drafts below are written in that number range for readability, but final numbering, filenames,
> and integration into `architecture-decisions/README.md` are acts of ratification outside this
> phase's authority.

## ADR-DRAFT-025 — Donor Identity Model

**Status:** Proposed (drafted for review; not integrated)

### Context
Stage 8 needs to represent who gives to Khidmat's operations — individuals, institutions,
corporations, governments, foundations, faith-based bodies, community collectives, and anonymous
givers. No such concept exists today; the closest is the generic `shared:organisation`, which
conflates funder, implementer, infrastructure operator, and referral target into one entity with no
donor-specific structure.

### Alternatives Considered
1. **Independent Entity** — a standalone `donor` entity unrelated to `person`/`organisation`.
2. **Role Profile** — a `donor_profile` entity attached behind existing `person`/`organisation`
   entities via reference relationships (this ADR's recommendation).
3. **Specialized Person** — `donor` modeled as a subtype/specialization of `person` only.
4. **Specialized Organisation** — `donor` modeled as a subtype/specialization of `organisation`
   only.
5. **Hybrid Pattern** — a narrow shared supertype (`funding_source_party`) specializing both
   `person` and `organisation`, with `donor_profile` attaching to the supertype.

Alternatives 3 and 4 are rejected together: donors are demonstrably both individuals *and*
institutions in the source brief itself ("Individual donors... Institutional donors... Corporate
donors..."), so specializing only one of `person`/`organisation` cannot represent the other half of
the requirement without a second, parallel specialization anyway — collapsing back into needing
both, i.e. effectively Alternative 2 or 5 with extra steps and two inheritance edges to maintain
instead of two reference edges. Alternative 1 (Independent Entity) is rejected as a repeat of the
already-resolved FLAG-005 failure mode (see Part 1, Decision 1, Alternative A). Alternative 5
(Hybrid/shared supertype) is rejected for now as disproportionate governance cost for a
single-consumer need (see Part 1, Decision 1, Alternative C) — revisit if a second domain
independently needs a Person-or-Organisation abstraction.

### Decision
**Donor is modeled as a role/profile (`donor_profile`) attached behind `shared:person` (individual,
faith-based-individual, community, anonymous-with-disclosed-identity-internally donors) or
`shared:organisation` (institutional, corporate, government, foundation donors), via two explicit
reference relationships (`donor_profile_of_person`, `donor_profile_of_organisation`) — never both
for the same `donor_profile` instance.** This mirrors the already-ratified `volunteer_profile`
pattern (`profile_of` → `shared:actor`, FLAG-006's resolution) applied to a two-target case instead
of a one-target case. `donor_profile` owns donor-specific structure (segmentation, giving history
aggregation, anonymity level) and redefines no field already owned by `person`/`organisation`.

**Anonymous donors:** an anonymous donor is represented as a `donor_profile` whose
`anonymity_level` data property is set accordingly, still attached to a real (internally-known)
`person`/`organisation` record when one exists, or, for genuinely untraceable giving (e.g. cash
collection box contributions with no recorded giver), as a `donor_profile` with **no** attachment
relationship populated at all — an explicitly allowed zero-cardinality case on both reference
relationships, not an error state. This must be stated explicitly in the relationship's
cardinality (`min: 0`) rather than left implicit.

### Consequences
- **Positive:** No identity fork; a donor who is also a referral source, community representative,
  or registrant is discoverable via existing identity, not a bespoke reconciliation.
- **Positive:** Reuses a certified pattern, lowering review risk.
- **Constraint:** `donor_profile` must never redefine any `person`/`organisation` field (name,
  contact, demographic data) — donor-specific structure only.
- **Constraint:** A `donor_profile` must attach to at most one of `person`/`organisation`, never
  both simultaneously.
- **Open item carried forward:** if a second future domain needs a generic Person-or-Organisation
  abstraction, revisit whether to promote to Alternative 5's shared supertype at that time — not
  pre-emptively.

### Related Documents
- ADR-008 (Single Ownership), ADR-018 (Shared Subject Supertype — structural precedent),
  ADR-024 (`volunteer_profile`/`profile_of` — direct pattern precedent), FLAG-005, FLAG-006
  (`ontology_authority_matrix.md`)

---

## ADR-DRAFT-026 — Volunteer Boundary

**Status:** Proposed (drafted for review; not integrated)

### Context
The Stage 8 brief lists volunteers, volunteer resources, capability, skills, availability,
assignment, capacity, specialization, certification, and deployment as in-scope. Every one of these
is already owned, at foundational tier, by Volunteer Operations (`ontology_authority_matrix.md`,
Volunteer Operations Domain section), governed by FLAG-006 and ADR-024.

### What Stage 8 Owns
Nothing volunteer-related, at initial implementation (8A/8B). No volunteer entity, taxonomy,
relationship, or data property of any kind.

### What Volunteer Operations Owns (Unchanged)
`volunteer_profile`, `volunteer_team`, `volunteer_status`, `volunteer_type`, `skill_category`,
`certification_type`, `availability_type`, `assignment_type` (eligibility only, per FLAG-006),
`coverage_type`, `language_proficiency`, `affiliation_type`, `training_status` — all foundational
tier (ADR-024 Tier 1). The operational layer (scheduling, dispatch, workload, trust/performance
scoring, the assignment act, assignment/training history) remains Volunteer Operations' Tier 2,
gated behind its own Stage-9 activation trigger, and is **not** reachable or ownable by Stage 8 at
any point without a separate governance action on Volunteer Operations itself.

### Every Overlapping Concept Named in the Brief, and Why It Stays With Volunteer Operations
| Brief term | Owned by | Why it does not move |
|---|---|---|
| Volunteers | Volunteer Operations (`volunteer_profile`) | Attaches behind `shared:actor`; Stage 8 has no actor-qualification concern |
| Volunteer resources | Volunteer Operations (`volunteer_profile`/`volunteer_team`) | "Resource" in the brief's sense here means *personnel*, a qualification concept, not a Stage 8 material/financial resource |
| Volunteer capability | Volunteer Operations (`skill_category`, `capabilities.yaml` via Shared Human Model) | Capability is explicitly Shared Human Model + Volunteer Operations territory (FLAG-004 resolved this boundary already) |
| Volunteer skills | Volunteer Operations (`skill_category`) | Foundational tier, already authored |
| Volunteer availability | Volunteer Operations (`availability_type`) | Foundational tier, already authored |
| Volunteer assignment | Verification Operations (act) / Case Management (act) / Volunteer Operations (eligibility) | FLAG-006 already resolved this three-way split; Stage 8 was never a party to it |
| Volunteer capacity | Volunteer Operations (Tier 2, deferred) | Capacity-as-workload is explicitly Tier 2 (ADR-024), not authorable by anyone yet, least of all a new domain |
| Volunteer specialization | Volunteer Operations (`skill_category`) | Same concept as skills, different word |
| Volunteer certification | Volunteer Operations (`certification_type`) | Foundational tier, already authored |
| Volunteer deployment | Volunteer Operations (Tier 2, deferred) / Case Management, Verification Operations (assignment act) | Deployment is the assignment act or its scheduling — never a Stage 8 concern |

### Why Ownership Belongs Where It Does
Every one of these concepts is either (a) already canonically authored by Volunteer Operations at
foundational tier, making any Stage 8 version a direct ADR-008 duplication, or (b) explicitly
deferred to Volunteer Operations' own Tier 2 / Stage-9 trigger, making any Stage 8 authoring of it
a premature-invention violation of ADR-009 by a domain that isn't even the one holding the
deferral. Stage 8 has no claim to either category. The only legitimate touchpoint is a **downstream
reference** — a `contribution` or `grant` may note that volunteer labor was part of what a donor
funded, but that reference points *at* `volunteer_profile`/`volunteer_team`, never redefines them,
and per Part 1 Decision 2, is deferred to a gated Phase 2 addition rather than authored now.

### Decision
Stage 8 (8A and 8B) authors **zero** volunteer-related content. Any future donor-facing
"contributed labor" reporting requirement is handled as a narrow, explicitly-gated Phase 2 addition
(Part 1, Decision 2, Alternative B), reviewed on its own merits against this exact boundary table
at the time it is proposed — not folded into 8A/8B.

### Consequences
- **Positive:** Zero ADR-008 risk from Stage 8 at initial implementation.
- **Positive:** This table becomes the canonical answer the next auditor needs, closing the
  ambiguity the original brief's volunteer section would otherwise have left open.
- **Constraint:** Any future Phase 2 "contributed labor" work must re-run this exact analysis, not
  assume the boundary is settled permanently — Volunteer Operations' own Tier 2 activation could
  change what's available to reference.

### Related Documents
- `ontology_authority_matrix.md` (Volunteer Operations Domain section, FLAG-006), ADR-024,
  ADR-008, ADR-009

---

## ADR-DRAFT-027 — Grant Ownership

**Status:** Proposed (drafted for review; not integrated)

### Context
Programs already owns program-level funding classification (`funding_source_types`,
`funding_restrictions`, `quota_types`, `compliance_checkpoints`, `audit_findings`) and the only
funding relationship in the graph (`program_funded_by → shared_org:organisation`). Programs' own
gap report names "Grant Management: Tracking the lifecycle of the funding proposal that created the
program" as an explicitly deferred gap. No entity today can represent a grant that funds multiple
Programs, or receives multiple `contribution` tranches over time.

### How Grant Relates to Each Adjacent Concept
- **Program:** `grant` optionally funds one or more `program` instances, via a new, additive
  relationship (`program_funded_by_grant`), coexisting with — not replacing — the existing
  `program_funded_by → organisation` edge for informal/direct funding.
- **Organisation:** `grant` is issued by a `donor_profile` (see ADR-DRAFT-025), which in turn
  attaches to `organisation` for institutional donors. `grant` does not reference `organisation`
  directly — it goes through `donor_profile`, keeping the donor-identity indirection consistent
  everywhere funding touches an identity.
- **Contribution:** a `contribution` is a single tranche/gift; it may `contribute_to` a `grant`
  (multi-tranche institutional funding) or stand alone with no `grant` reference (a single
  unrestricted gift). A `contribution` is never itself the funding-lifecycle object — that role is
  `grant`'s alone.
- **Funding Restriction:** `grant` **references** Programs' existing `funding_restrictions` scheme
  (`unrestricted`, `earmarked_geographic`, `earmarked_demographic`, `tied_procurement`) rather than
  authoring a new one — the same restriction vocabulary applies one level up the funding chain from
  where it's used today.
- **Funding Source (Type):** likewise, `grant.funding_source_type` references Programs' existing
  `funding_source_types` scheme. `donor_type` (Stage 8's own, new taxonomy — see Part 5) is a
  distinct axis describing the donor's own segmentation, not the funding instance's category; a
  `grant` from a `private_foundation`-type donor still separately carries `funding_source_types:
  private_foundation` on itself for continuity with how Programs already reads this field, but the
  two are reconciled by note (Part 5), not merged.

### Should Grant Become an Intermediary, Primary Funding Object, or Optional Abstraction?
Evaluated in Part 1, Decision 3. **Optional abstraction is recommended** — mandatory intermediary
(all funding must route through Grant) forces informal/small giving through unnecessary structure
and requires modifying certified Programs content; a primary-funding-object model without an
optional/direct path has the same forcing problem under a different name. Optional abstraction
lets both shapes coexist truthfully.

### Decision
`grant` is authored as an **optional abstraction**: a `program` may be funded directly by an
`organisation` (existing edge, untouched) or by a `grant` (new edge, additive), or both
simultaneously for different funding streams. `grant` is issued by `donor_profile`, references
Programs' existing `funding_source_types`/`funding_restrictions` schemes rather than duplicating
them, and is the aggregation point for multiple `contribution` tranches over time.

### Consequences
- **Positive:** Zero modification to certified Programs relationship rows.
- **Positive:** Closes the exact gap Programs' own audit named, without Programs having to
  re-open its own certified scope.
- **Constraint:** Documentation must carry an explicit reconciliation note (Part 5) so
  "directly-funded" vs. "grant-funded" Programs are understood as two valid shapes, not redundant
  or conflicting paths to the same fact.

### Related Documents
- `programs/ontology/relationships.yaml` (`program_funded_by`, referenced not modified),
  `programs/taxonomy/funding-and-compliance.yaml` (referenced not modified),
  `programs/Programs_Repository_Gap_Report.md` (Type D gap this ADR closes), ADR-DRAFT-025

---

## ADR-DRAFT-028 — Resource Model

**Status:** Proposed (drafted for review; not integrated)

### Context
No material or financial resource concept exists anywhere in the repository.
Support Delivery's own gap report names warehouse/inventory tracking as an explicitly deferred
gap, and its existing `custody_transfer`/`custodian` entities already model movement of goods
*after* they exist in some stock — nothing today models the stock itself.

### Decision
A shallow type hierarchy, not a flat set and not a deep taxonomy-only model:

- `resource` — abstract supertype, owns no allocatable/trackable data itself (mirrors `subject`'s
  "owns no demographic data" discipline exactly).
  - `financial_resource` — money, vouchers-as-value (not vouchers-as-delivery-modality, which
    Support Delivery already owns; this is the *funded value*, not the *handover mechanism*).
  - `material_resource` — physical goods, with a `material_resource_category` taxonomy value
    (analogous discipline to `intervention_modality`) distinguishing food/medicine/shelter
    materials/clothing/educational materials/medical equipment/vehicles at the taxonomy level
    rather than the entity level, **unless** 8B implementation concretely finds a subtype's
    property set diverges enough to warrant its own entity (e.g. cold-chain-tracked medicine might
    justify `consumable` as a true entity if temperature/expiry fields prove structurally
    different enough from, say, `equipment`'s maintenance/serviceable-life fields) — that
    determination is explicitly deferred to 8B authoring, not pre-decided here.
- `inventory_item` — the trackable **instance** of a `resource` (of either subtype) held at a
  `storage_location`, in a given quantity and condition. This entity/instance split is
  non-negotiable: `resource`/`financial_resource`/`material_resource` describe *what kind of thing
  this is*; `inventory_item` describes *how much of it exists, where, right now*.
- `storage_location` — a warehouse, distribution point, or cold-chain facility holding
  `inventory_item`s.

`equipment` and `asset` are **not** pre-committed as separate entities in this ADR — they remain
open, to be resolved as taxonomy values under `material_resource_category` unless 8B's authoring
finds genuine structural divergence, per the note above. This ADR commits to the *shape of the
decision process*, not to a premature answer on the deepest two tiers.

### Consequences
- **Positive:** Mirrors the repository's own most successful precedent (`subject`/ADR-018) for
  exactly this kind of common-abstraction-plus-specialization need.
- **Positive:** The `resource` type / `inventory_item` instance split gives Support Delivery a
  single, stable entity (`inventory_item`) to reference from `delivery_event`/`custody_transfer`,
  regardless of how deep the type hierarchy under `resource` eventually grows.
- **Constraint:** `resource` itself must never be allocated, delivered, or transferred directly —
  only `inventory_item` (a concrete instance) can be. This mirrors `subject` never itself appearing
  in a case, only its specializations doing so.
- **Deferred:** Whether `consumable`/`equipment`/`asset` become full entities or remain taxonomy
  values under `material_resource_category` is explicitly left to 8B implementation to determine,
  against the evidence of actual property divergence — recorded here as an open item, not silently
  decided.

### Related Documents
- ADR-018 (Shared Subject Supertype — structural precedent), `support-delivery/ontology/entities.yaml`
  (`custody_transfer`, `custodian` — referenced not modified), `support-delivery/Support_Delivery_Repository_Gap_Report.md`
  (Type D gap this ADR closes), ADR-023 (value object vs. entity discipline, informing the deferred
  `consumable`/`equipment`/`asset` decision)

---

# Part 3 — Domain Context Diagram

Conceptual ontology graph only — no software, no data flow, no implementation. Arrows show
reference direction (A → B reads "A references B"), not data flow or chronological sequence.
Ownership boundaries are marked by domain; every cross-domain arrow is a **reference**, never a
redefinition, per ADR-008.

```
┌─────────────────────────────── SHARED ONTOLOGY (existing, unmodified) ───────────────────────────────┐
│  person          organisation          actor                                                          │
└──────┬──────────────────┬───────────────────────────────────────────────────────────────────────────┘
       │                  │
       │ donor_profile_of_person      donor_profile_of_organisation
       ▼                  ▼
┌─────────────────────────────────────── STAGE 8A — DONOR & FUNDING (new) ──────────────────────────────┐
│                                                                                                          │
│   donor_profile ──issues──▶ grant ◀──references── programs:funding_source_types                        │
│        │                     │  ▲                 programs:funding_restrictions   (Programs, existing) │
│        │                     │  │                                                                       │
│        │                contributes_to                                                                  │
│        │                     │                                                                          │
│        └───(direct, unrestricted)───▶ contribution                                                      │
│                                                                                                          │
│   islamic_giving_type (taxonomy) ── qualifies ──▶ grant / contribution                                  │
│   zakat_eligible_category (taxonomy) ── references ──▶ programs:eligibility_rule (Programs, existing)   │
└──────────────────────────────────────────┬─────────────────────────────────────────────────────────────┘
                                            │ program_funded_by_grant (new, additive)
                                            ▼
┌─────────────────────────────────────── PROGRAMS (existing, unmodified) ──────────────────────────────┐
│  program ◀──program_funded_by (existing, untouched)── organisation                                    │
│  program ◀──program_funded_by_grant (new row)──────── grant                                            │
│  intervention_modality  (existing — distinct_from resource_category, see Part 5)                        │
└──────────────────────────────────────────┬─────────────────────────────────────────────────────────────┘
                                            │ (no direct edge to Resource — Resource is
                                            │  consumed via allocation, not via Program directly)
                                            ▼
┌─────────────────────────────────────── STAGE 8B — MATERIAL RESOURCE & LOGISTICS (new) ─────────────────┐
│                                                                                                          │
│   resource (abstract) ─┬─▶ financial_resource                                                           │
│                         └─▶ material_resource ──(material_resource_category taxonomy)                   │
│                                                                                                          │
│   inventory_item ──instance_of──▶ resource                                                              │
│   inventory_item ──stored_at──▶ storage_location                                                        │
│                                                                                                          │
│   resource_allocation ──allocates──▶ inventory_item                                                     │
│   resource_allocation ──funded_by──▶ grant / contribution   (references Stage 8A, above)                │
│   resource_allocation ──allocated_to──▶ case_plan (Case Management, existing) / program (Programs)      │
└──────────────────────────────────────────┬─────────────────────────────────────────────────────────────┘
                                            │ delivery_event fulfilled_from resource_allocation (new row,
                                            │ authored IN Support Delivery, referencing Stage 8B inward —
                                            │ matches the case_plan_addressed_by_intervention precedent)
                                            ▼
┌─────────────────────────────────────── SUPPORT DELIVERY (existing, unmodified) ──────────────────────┐
│  delivery_event ──fulfills──▶ case_plan (existing)                                                     │
│  delivery_event ──fulfilled_from──▶ resource_allocation (new row, points INTO Stage 8B)                │
│  custody_transfer / custodian  (existing — inventory sits strictly upstream, never duplicated)          │
│  delivery_modality (existing — distinct_from resource_category, see Part 5)                             │
└──────────────────────────────────────────┬─────────────────────────────────────────────────────────────┘
                                            │ delivery_event resolves case_plan (existing chain,
                                            │ unaffected by Stage 8)
                                            ▼
┌─────────────────────────────────────── BENEFICIARY (Registration / Case Management, existing) ────────┐
│  beneficiary ◀── case_plan ◀── case (existing chain, entirely unmodified by Stage 8)                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Ownership boundaries shown:** each box is one owning domain; every arrow crossing a box boundary
is a reference (CURIE-qualified in eventual implementation), never a redefinition. **Dependency
direction:** Stage 8A depends on Shared Ontology and (loosely, via reference only) Programs' taxonomy
schemes; Stage 8B depends on Stage 8A (funding source for allocation) and is depended upon by Support
Delivery (which gains one new reference row); Support Delivery's existing chain into Beneficiary is
completely untouched. This satisfies ADR-009: no domain earlier in the roadmap than Stage 8 is made
to depend on Stage 8.

---

# Part 4 — Boundary Analysis

| Domain | What Stage 8 references | What Stage 8 owns | What Stage 8 must never own |
|---|---|---|---|
| **Shared Ontology** | `person`, `organisation` (attachment targets for `donor_profile`) | `donor_profile` and its two attachment relationships | `person`, `organisation`, `actor`, `subject` themselves — never redefined, never re-specialized outside the declared `donor_profile_of_*` relationships |
| **Programs** | `funding_source_types`, `funding_restrictions` (referenced by `grant`); `program` (target of `program_funded_by_grant`); `intervention_modality`, `eligibility_rule`, `eligibility_categories` (referenced for reconciliation, not redefinition) | `grant`, `contribution`, `program_funded_by_grant` relationship | `program`, `program_version`, `program_variant`, `enrollment`, `eligibility_rule` mechanics, `intervention_modality`, `funding_source_types`, `funding_restrictions` — all stay Programs-owned, referenced only |
| **Support Delivery** | `inventory_item` is referenced *from* Support Delivery (`delivery_event fulfilled_from resource_allocation`); Stage 8B does not itself reference Support Delivery entities inbound | `resource`, `inventory_item`, `storage_location`, `resource_allocation` | `delivery_event`, `delivery_window`, `delivery_attempt`, `proof_of_delivery`, `custody_transfer`, `custodian`, `community_representative`, `delivery_modality`, `delivery_status` — the entire execution/handover layer stays Support Delivery's; Stage 8B stops strictly upstream of the first `custody_transfer` |
| **Volunteer Operations** | Nothing, at 8A/8B (see ADR-DRAFT-026); a future gated Phase 2 might reference `volunteer_profile`/`volunteer_team` | Nothing | `volunteer_profile`, `volunteer_team`, any skill/certification/availability/coverage/affiliation/training taxonomy, the assignment act, assignment history — all fully excluded, no exceptions at this phase |
| **Community Context** | `local-organizations.yaml` (`local_philanthropic_trust`, `faith_based_organization`, etc.) — referenced when typing a community/faith-based `donor_profile`'s underlying `organisation` | Nothing | The community-organisation typology itself; Stage 8 types a donor's *organisation*, it never re-derives or extends `local-organizations.yaml`'s own scheme |
| **Shared Ontology → `shared/taxonomy/organisations.yaml`** | Referenced for institutional donor typing (a `donor_profile`'s underlying `organisation` already carries an `organisation_types` value) | Nothing new here | The `organisation_types` scheme itself |
| **Needs Assessment** | None — no funding, resource, or donor concept intersects Needs Assessment's evidence/finding/session model | Nothing | Nothing — no boundary risk identified; domains are structurally disjoint |
| **Case Management** | `case_plan` (target of `resource_allocation.allocated_to`) | Nothing | `case`, `case_plan`, `referral`, `follow_up`, `case_note`, `objective_status` — Stage 8 supplies the funded resource a `case_plan` may draw on, never the plan or case itself |
| **Beneficiary Lifecycle** | None directly — Stage 8's chain reaches `case_plan` (Case Management), not Beneficiary Lifecycle's `engagement_stage`/`human_development_stage` | Nothing | Nothing — no direct edge is proposed; if a future need arises (e.g. "this donor's funding contributed to this beneficiary's lifecycle transition"), it must be a new, separately-governed reference, not assumed by this phase |

**Verification note on "Needs Assessment" and "Beneficiary Lifecycle":** both were checked and found
to have **no** structural intersection with Stage 8's proposed scope. This is stated explicitly
(rather than omitted) because the brief asked for all eight domains to be verified, not only the
ones with findings — a clean "no boundary risk" result is itself a governance-relevant finding, not
a non-answer.

---

# Part 5 — Semantic Collision Review

| Collision | Same concept? | Related concept? | Independent concept? | Requires `distinct_from` note? | Requires shared predicate? | Requires glossary reconciliation? |
|---|---|---|---|---|---|---|
| `donor_type` vs. `funding_source_types` | No | **Yes** | No | **Yes** | No | **Yes** — Glossary must state one classifies the *giver's own segment*, the other classifies *a program's funding category*; a private-foundation donor's grant still separately carries `funding_source_types: private_foundation` on the grant, and this dual-tagging must be explained, not left implicit |
| `resource_category` (i.e. `material_resource_category`/`financial_resource`) vs. `intervention_modality` | No | **Yes** | No | **Yes** | No | **Yes** — must extend the existing note pattern already authored in `delivery-modalities.yaml` to include this third axis, not merely restate it |
| `resource_category` vs. `delivery_modality` | No | **Yes** | No | **Yes** | No | **Yes** — same extension as above; all three (`intervention_modality`, `delivery_modality`, `resource_category`) need one shared reconciliation note, not three pairwise ones, to avoid drift between two separately-authored two-way notes |
| Zakat eligibility vs. `eligibility_rule` | No | **Yes** | No | **Yes** | **Yes** — `zakat_eligible_category` should be consumable *as* a value an `eligibility_rule` instance can reference, not a parallel rule-evaluation mechanism | **Yes** — Glossary must state zakat eligibility is a *classification a Program's eligibility rule may draw on*, not a second eligibility engine |
| `donor` vs. `organisation` | No | **Yes** (via `donor_profile_of_organisation`) | No | Not a new taxonomy pair, so no `distinct_from` note; the relationship itself carries the semantics | No | **Yes** — Glossary must state a `donor_profile` is a role an `organisation` (or `person`) holds, not a new kind of institution, echoing the `volunteer_profile`/`actor` precedent's own Glossary entry style |
| `donor` vs. `person` | No | **Yes** (via `donor_profile_of_person`) | No | No | No | **Yes** — same reasoning as above |
| Inventory vs. custody | No | **Yes** | No | **Yes** — a short note stating `inventory_item` covers pre-custody stock and `custody_transfer` covers movement once dispatched, with the exact handoff point (`resource_allocation` → `delivery_event`) named | No | **Yes** — the discovery report already flagged the word "inventory" appearing informally in `delivery-lifecycle.yaml`'s `returned` state; the Glossary entry must reconcile that pre-existing informal usage with the new formal `inventory_item` entity, not silently supersede it |
| Allocation vs. delivery | No | **Yes** | No | **Yes** — `resource_allocation` is the pre-execution commitment decision; `delivery_event` is the execution — same category of distinction as `intervention_modality` (catalog form) vs. `delivery_modality` (handover requirements), and should cite that existing note as its stylistic precedent | No | **Yes** |

**Pattern observed across the table:** every collision resolves to "related, not same, not fully
independent" — none of the eight pairs is a true duplicate requiring merge, and none is safely
independent enough to skip reconciliation. This is consistent with the discovery report's §16
finding and is not weakened by this closer, adversarial re-examination — if anything, this pass
found **two additional** reconciliation needs the discovery report did not itemize as separately
(the three-way `intervention_modality`/`delivery_modality`/`resource_category` note needing to be
one shared note rather than pairwise ones, and the pre-existing informal "inventory" word usage in
`delivery-lifecycle.yaml` needing explicit reconciliation, not just a new entity arriving quietly
alongside it).

---

# Part 6 — Stage 8 Repository Impact (Predicted, Not Executed)

This section predicts every file Stage 8 implementation will eventually touch. **No file listed
below has been created or modified by this phase.**

### New Files
- `donor-resource/README.md`
- `donor-resource/governance.md` (mirroring `volunteer-operations/governance.md`'s pattern)
- `donor-resource/ontology/entities.yaml` (`donor_profile`, `grant`, `contribution`, `resource`,
  `financial_resource`, `material_resource`, `inventory_item`, `storage_location`,
  `resource_allocation`)
- `donor-resource/ontology/relationships.yaml` (`donor_profile_of_person`,
  `donor_profile_of_organisation`, `grant_contributes_to` inverse, `program_funded_by_grant`,
  `resource_allocation_allocates`, `resource_allocation_allocated_to`, `inventory_item_stored_at`)
- `donor-resource/ontology/data-properties.yaml`
- `donor-resource/ontology/semantic-constraints.yaml` (including the non-negative-stock invariant
  and the zakat-restriction constraint named in the discovery report §12)
- `donor-resource/ontology/lifecycle-constraints.yaml` (grant/contribution/allocation state
  machines, if warranted)
- `donor-resource/taxonomy/islamic-giving.yaml` (`islamic_giving_type`, `zakat_eligible_category`)
- `donor-resource/taxonomy/donor-classification.yaml` (`donor_type`, `anonymity_level`)
- `donor-resource/taxonomy/resource-classification.yaml` (`material_resource_category`,
  `resource_condition`)
- `donor-resource/taxonomy/stock-movement.yaml` (`stock_movement_type`)
- `donor-resource/discovery/` (this report and this document, or their successors, archived here
  per the pattern `volunteer-operations/discovery/foundation-report.md` already establishes)

### Modified Files
- `support-delivery/ontology/relationships.yaml` — **one new additive row**
  (`delivery_event fulfilled_from resource_allocation`), no existing row changed
- `programs/ontology/relationships.yaml` — **one new additive row** (`program_funded_by_grant`),
  no existing row changed
- `support-delivery/taxonomy/delivery-modalities.yaml` — extend the existing `distinct_from` note
  block to include `resource_category` as a third reconciled axis (append, not rewrite)

### Governance Files
- `ontology_authority_matrix.md` — new "Donor & Resource Domain" section, in the same format as
  the Programs/Case Management/Volunteer Operations sections; no existing row edited
- `architecture-decisions/README.md` — four new index rows (ADR-025 through ADR-028, final
  numbers/titles to be confirmed at ratification)
- `architecture-decisions/ADR-025-donor-identity-model.md` through
  `architecture-decisions/ADR-028-resource-model.md` (or final ratified numbers/titles) — the four
  drafts in Part 2, ratified and integrated
- `knowledge_layer_roadmap.md` — a new stage entry, explicitly disambiguated from the existing
  "Stage 8: Community Context" per the numbering-collision note in the discovery report §7

### Shared Files
- `shared/ontology/entities.yaml` — **not modified** under the recommended architecture (Decision 1,
  Alternative B was chosen specifically to avoid this); would only be touched if a future
  governance review revisits Alternative C (the `funding_source_party` supertype)
- `shared/taxonomy/organisations.yaml` — **not modified**; referenced only

### Documentation
- `GLOSSARY.md` — new entries for Donor, Grant, Contribution, Resource, Inventory Item, Storage
  Location, Resource Allocation, Zakat/Islamic Giving terms, each cross-referencing
  `recovery_resources` (Risk Domain), `organisation`, `intervention_modality`, `delivery_modality`
  per Part 5's reconciliation requirements — learning explicitly from the Stage 7C-identified
  Glossary "Case" duplication defect
- A `Donor_Resource_Business_Architecture.md` / `Donor_Resource_Domain_Audit.md` /
  `Donor_Resource_Concept_Inventory.md` set, matching the discovery-document pattern already
  established by Programs, Support Delivery, Case Management, and Community Context before their
  own implementation passes

### Relationship Files
Covered above (`donor-resource/ontology/relationships.yaml` new; two additive rows in
Programs/Support Delivery).

### Taxonomies
Covered above (`islamic-giving.yaml`, `donor-classification.yaml`, `resource-classification.yaml`,
`stock-movement.yaml`).

### Authority Matrix
Covered above — new section only; per ADR-008's own rule, ownership must be declared *before or at*
authoring time, meaning this file's update is not optional follow-up but a prerequisite step within
implementation itself, sequenced first.

### README Files
- `donor-resource/README.md` (new)
- No existing domain's `README.md` requires modification — each new cross-domain reference is
  additive and does not change any existing domain's own description of its scope

---

# Part 7 — Readiness Assessment

### Evidence For Readiness
- All concepts named in the original Stage 8 brief have been traced to an owner (existing or
  proposed) with no remaining "unknown" category.
- Four architectural decisions (Donor identity, Volunteer boundary, Grant ownership, Resource
  model) have each been evaluated against three genuine alternatives, stress-tested against this
  repository's own precedents (FLAG-005, FLAG-006, ADR-018, ADR-024), and resolved to a single
  recommendation with disclosed trade-offs, not asserted without challenge.
- Every semantic collision named in the brief (Part 5) has been classified, and every one requiring
  a `distinct_from` note or Glossary reconciliation has that requirement explicitly recorded for
  implementation to satisfy — including two reconciliation needs this pass found beyond the
  discovery report's original list.
- The domain context diagram (Part 3) shows a fully connected, acyclic dependency graph consistent
  with ADR-009 — no domain earlier in the roadmap is made to depend on Stage 8.
- The recommended architecture (Alternative B for Donor identity; Alternative A for Volunteer
  boundary; Alternative B for Grant; Alternative C, shallow, for Resource) is, in every one of the
  four decisions, the option that **modifies zero certified/active-domain content** — the entire
  recommended design is additive-only against everything that already exists.

### Evidence Against Immediate Implementation
- The four ADRs in Part 2 are **drafts** — none is `Accepted`. Per this repository's own ADR
  lifecycle (`architecture-decisions/README.md`: Draft → Proposed → Accepted), they require actual
  ratification by the Knowledge Layer Architect before implementation may cite them as binding,
  exactly as ADR-023 in the real repository currently sits at `Proposed (pending reviewer
  ratification)` rather than `Accepted` — this repository does not treat drafting as equivalent to
  ratifying, and this phase should not either.
- The Resource model decision (ADR-DRAFT-028) explicitly defers one sub-decision (whether
  `consumable`/`equipment`/`asset` become entities or taxonomy values) to be resolved empirically
  during 8B authoring — this is a disclosed, bounded open item, not a blocking unknown, but it
  means 8B implementation must resolve it as its first act, not treat the ADR as fully closing the
  question.
- No numbering has been reserved in `architecture-decisions/README.md` — a real Stage 8B
  implementer must confirm ADR-025 through ADR-028 are still the next free numbers at the time of
  ratification (a different Stage 8-adjacent effort could plausibly claim ADR-025 first).

### Outcome

**Requires Additional ADRs** — specifically, ratification of the four drafts in Part 2 (not their
re-drafting; their content is considered settled by this review) — followed immediately by
**Ready for Stage 8B Implementation**. This is not a "Requires Governance Review" outcome in the
open-ended sense (no unresolved architectural ambiguity remains for a reviewer to adjudicate — Part
1 already stress-tested every alternative), and it is not "Requires Repository Changes" (the
recommended architecture is additive-only and requires no pre-implementation repair of existing
content, unlike the Phase 1 freeze audit's earlier, unrelated findings about pre-existing repository
defects). The only remaining gate is procedural ratification of already-substantively-resolved
decisions, not further design work.

**Recommended next step:** ratify ADR-DRAFT-025 through ADR-DRAFT-028 (assign real numbers, move to
`architecture-decisions/`, update the ADR index and `ontology_authority_matrix.md`'s prerequisite
declarations), then proceed directly to 8A implementation (Donor & Funding) followed by 8B
(Material Resource & Logistics), per the sequencing recommended in the discovery report §17 and
reaffirmed here.
