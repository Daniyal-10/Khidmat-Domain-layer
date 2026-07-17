# HKMP Stage 8B — Donor & Funding Intelligence Implementation Report

**Scope implemented:** Donor & Funding Intelligence only (`donor_profile`,
`grant`, `contribution`, Islamic Giving taxonomy, funding lifecycle). Material
Resource & Logistics (`resource`, `inventory_item`, `storage_location`,
`resource_allocation`) is **not** implemented — reserved for Stage 8C per
ADR-DRAFT-028.

**Architecture followed:** `HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md`,
treated as frozen. No decision in that document was revisited; one
implementation-level refinement was made within its bounds (see §3, Deviation
Note).

---

## 1. Files Created

### `donor-resource/` (new domain directory)

| File | Contents |
|---|---|
| `README.md` | Domain purpose, maturity (8B implemented / 8C deferred), owns/does-not-own, directory structure |
| `governance.md` | Boundary-enforcement rules, cross-domain reference patterns, flagged boundary cases (mirrors `volunteer-operations/governance.md`'s structure) |
| `PREPARED_GOVERNANCE_ADDITIONS.md` | Drafted, **not integrated**: Authority Matrix section, Glossary entries, boundary notes for existing files, roadmap entry |
| `ontology/entities.yaml` | `donor_profile`, `grant`, `contribution` |
| `ontology/relationships.yaml` | 9 relationship rows (see §4) |
| `ontology/data-properties.yaml` | 17 data properties across the three entities, including one Value Object (`funding_window`) |
| `ontology/semantic-constraints.yaml` | 6 constraints |
| `taxonomy/donor-classification.yaml` | `donor_type` (8 concepts), `donor_engagement_pattern` (3 concepts), `anonymity_level` (3 concepts) |
| `taxonomy/islamic-giving.yaml` | `islamic_giving_type` (7 concepts), `zakat_eligible_category` (8 concepts) |
| `taxonomy/funding.yaml` | `grant_status` (8 concepts), `contribution_status` (5 concepts), `renewal_status` (5 concepts) |

**Total: 10 new files, 1 new directory tree.** No `lifecycle-constraints.yaml`
was created — the required file list in the implementation brief did not
name one, and funding lifecycle is fully expressed through the taxonomy
schemes plus `semantic-constraints.yaml`'s hard invariants (see
`README.md`'s note on this decision).

No `discovery/` subdirectory was created inside `donor-resource/`; the Stage
8 discovery and architecture documents remain at the repository root
(`HKMP_STAGE8_DONOR_RESOURCE_DOMAIN_DISCOVERY_REPORT.md`,
`HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md`), consistent with where this
conversation already produced them, and are cross-referenced from
`donor-resource/README.md` rather than duplicated.

## 2. Files Modified

**None.** `git status --porcelain` was checked before and after this pass:
the only changes are new, untracked files (`donor-resource/` and this
report). No existing repository file — certified or otherwise — was opened
for writing at any point in this implementation.

This is a stricter outcome than the brief's own allowance ("do not modify
existing certified domains except for additive cross-domain references
explicitly required by the architecture") required: every cross-domain
reference this domain needs was achievable by authoring the edge from this
domain's own `relationships.yaml`/`data-properties.yaml`, referencing the
target by CURIE, with zero lines added to Programs, Support Delivery,
Volunteer Operations, Shared Ontology, or Community Context files. See §3 for
why this was possible even for the one relationship
(ADR-DRAFT-027's `grant`↔`program` edge) whose illustrative ADR draft
described it as if it belonged on the Programs side.

## 3. Architectural Decisions Followed (and one Deviation Note)

| ADR draft | Followed as | Deviation? |
|---|---|---|
| ADR-DRAFT-025 (Donor Identity Model) | `donor_profile` attaches behind `shared:person`/`shared:organisation` via two mutually-exclusive, both-optional relationship rows; zero-attachment permitted for untraceable donors | None |
| ADR-DRAFT-026 (Volunteer Boundary) | Zero volunteer-related content authored anywhere in this domain | None |
| ADR-DRAFT-027 (Grant Ownership) | `grant` is an optional abstraction; `funding_source_type`/`funding_restriction` reference Programs' existing schemes by `taxonomy_ref`, not duplicated | **One deviation, within the ADR's own intent — see below** |
| ADR-DRAFT-028 (Resource Model) | Not applicable — Stage 8C is out of scope for this pass; no entity or reference to `resource`/`inventory_item`/etc. was authored | None (correctly deferred) |

**Deviation note on ADR-DRAFT-027:** the ADR draft's illustrative decision
text names the additive relationship `program_funded_by_grant` and describes
it as a row added to `programs/ontology/relationships.yaml`, "coexisting
with... the existing `program_funded_by` edge." This implementation instead
authors the identical graph edge as `grant_funds_program` — `from: grant`,
`to: programs:program` — entirely within
`donor-resource/ontology/relationships.yaml`, adding **zero** lines to any
Programs file. This is not a redesign of the ADR's decision (Grant remains an
optional abstraction; Programs' funding classification and existing
`program_funded_by` edge remain untouched and unduplicated) — it is a more
conservative choice of *which side authors the edge*, made because:

1. HKMP_STAGE7C's own certification review already established, for the
   structurally identical `case_plan_addressed_by_intervention` edge, that a
   graph is traversable from either end regardless of which end is labeled
   `from` — direction of authorship does not change the resulting graph's
   connectivity or semantics.
2. Authoring from the `grant` side achieves the ADR's stated goal (an
   additive funding path coexisting with the direct edge) while requiring
   *zero* modification to a Stage-7-certified file, which is strictly safer
   than the ADR draft's own illustrative direction under this phase's rule
   "do not modify existing certified domains."
3. It is the same discipline already used twice in this repository
   (`volunteer_profile_affiliated_with_organisation`,
   `case_plan_addressed_by_intervention`): the domain that owns the `from`
   entity authors and owns the edge; the referenced domain's files are read,
   never written.

This choice is documented in `donor-resource/ontology/relationships.yaml`'s
own notes on `grant_funds_program`, in `governance.md`, and here — it is not
a silent substitution. If a future reviewer prefers the ADR draft's literal
direction, ratifying ADR-DRAFT-027 with that preference stated explicitly
would require a follow-up pass adding one row to
`programs/ontology/relationships.yaml`; nothing in this implementation
forecloses that.

## 4. Cross-Domain References Added

All authored entirely within `donor-resource/`, zero modification to the
referenced domain's own files:

| Reference | From (owned here) | To (referenced, not modified) | Row location |
|---|---|---|---|
| `donor_profile_of_person` | `donor_profile` | `shared:person` | `donor-resource/ontology/relationships.yaml` |
| `donor_profile_of_organisation` | `donor_profile` | `shared:organisation` | `donor-resource/ontology/relationships.yaml` |
| `grant_funds_program` | `grant` | `programs:program` | `donor-resource/ontology/relationships.yaml` |
| `funding_source_type` (data property) | `grant` | `programs_tax:funding_source_types` | `donor-resource/ontology/data-properties.yaml` |
| `funding_restriction` (data property) | `grant` | `programs_tax:funding_restrictions` | `donor-resource/ontology/data-properties.yaml` |

**Not yet added (staged, per §Governance instruction):**
- Authority Matrix entry (`PREPARED_GOVERNANCE_ADDITIONS.md` §1)
- Glossary entries (`PREPARED_GOVERNANCE_ADDITIONS.md` §2)
- Boundary notes for `programs/taxonomy/funding-and-compliance.yaml`,
  `support-delivery/taxonomy/delivery-modalities.yaml`, and
  `programs/ontology/entities.yaml#eligibility_rule`
  (`PREPARED_GOVERNANCE_ADDITIONS.md` §3)
- Roadmap entry disambiguating this stage from the roadmap's own "Stage 8:
  Community Context" (`PREPARED_GOVERNANCE_ADDITIONS.md` §4)

**Community Context reference (declared but not authored as a relationship):**
`donor_type#community` and `donor_type#faith_based`'s descriptions note that
a community/faith-based donor's underlying `organisation` may itself be typed
via `community-context/taxonomy/local-organizations.yaml`. This is descriptive
text only — no relationship row in this domain references Community Context,
consistent with the boundary analysis in
`HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 4 (Stage 8 references
Community Context's typology only through the `organisation` it already
points at, not directly).

## 5. Validation Results (Self-Audit)

| Check | Result |
|---|---|
| **Duplicate entities** | None. `donor_profile`, `grant`, `contribution` were grepped against the full repository — no prior occurrence of any of the three ids anywhere outside `donor-resource/`. |
| **Duplicate taxonomies** | None. `donor_type`, `donor_engagement_pattern`, `anonymity_level`, `islamic_giving_type`, `zakat_eligible_category`, `grant_status`, `contribution_status`, `renewal_status` are all new scheme ids; `funding_source_types`/`funding_restrictions` are explicitly *referenced* via `taxonomy_ref`, never re-declared. |
| **Ownership violations** | None found. Every entity/taxonomy new in this pass is owned by Donor & Resource; every existing concept touched (`person`, `organisation`, `program`, `funding_source_types`, `funding_restrictions`, `eligibility_rule`) is referenced by CURIE/`taxonomy_ref`, never redefined, and no existing file was written to (§2). |
| **Semantic collisions** | The three collisions flagged in `HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 5 that apply to Stage 8B's scope (`donor_type` vs. `funding_source_types`; zakat eligibility vs. `eligibility_rule`; Islamic Giving vs. ADR-022) all carry an explicit reconciliation note in the authored files (`donor-classification.yaml`'s `references:` block, `islamic-giving.yaml`'s two `references:`/purpose-note blocks, `governance.md` Rules 4–6). The two collisions scoped to Stage 8C (`resource_category` vs. `intervention_modality`/`delivery_modality`; inventory vs. custody) are correctly left unaddressed, since no `resource_category` or `inventory_item` concept exists yet to collide with anything. |
| **Relationship consistency** | Every relationship with an `inverse:` field has its inverse row present and reciprocally cross-referenced (`grant_issued_by_donor_profile` ↔ `donor_profile_issues_grant`; `contribution_given_by_donor_profile` ↔ `donor_profile_gives_contribution`; `contribution_contributes_to_grant` ↔ `grant_receives_contribution`). The two `profile_of` rows and `grant_funds_program` correctly have no inverse authored, per the same no-inverse-into-a-non-owned-file discipline already used for `volunteer_profile_profile_of_actor` and `volunteer_profile_affiliated_with_organisation`. All `taxonomy_ref` values in `data-properties.yaml` resolve to a scheme actually defined in this domain's `taxonomy/` files or to a correctly CURIE-qualified external scheme (`programs_tax:funding_source_types`, `programs_tax:funding_restrictions`) — cross-checked by hand against `taxonomy/donor-classification.yaml`, `taxonomy/islamic-giving.yaml`, and `taxonomy/funding.yaml`. |
| **Property ID uniqueness** | One collision was caught and fixed during authoring: `islamic_giving_type` was initially declared as a data-property id on both `grant` and `contribution` within the same file. Repository convention (checked against `case-management/ontology/data-properties.yaml`, which entity-qualifies every property name — `plan_status`, `ref_status`, `follow_up_status`, never a bare reused `status`) requires unique ids per file. Renamed to `grant_islamic_giving_type` and `contribution_islamic_giving_type`. |
| **Glossary consistency** | Not applicable to the live `GLOSSARY.md` (untouched, per §2). The *drafted* Glossary entries (`PREPARED_GOVERNANCE_ADDITIONS.md` §2) were checked against the existing `GLOSSARY.md` for the exact failure mode HKMP_STAGE7C found (an added term that doesn't cross-reference a near-namesake): the drafted `Resource` entry explicitly cross-references `Recovery Resources` rather than risk that ambiguity if added later; the drafted `Donor Profile` entry cross-references the existing `Volunteer Profile` entry's own pattern rather than introducing an unexplained new shape. |
| **ADR compliance** | ADR-008 (Single Ownership): satisfied — see Ownership Violations row. ADR-009 (Dependency-Driven Activation): satisfied — this domain depends only on already-active domains (Shared Ontology, Programs, Community Context by reference), and no already-active domain is made to depend on it (no file outside `donor-resource/` was touched). ADR-018 (Shared Subject precedent): the `donor_profile` two-target attachment pattern is structurally consistent with, though not a literal reuse of, `subject` — recorded as a live open item (DR-FLAG-A) rather than silently resolved. ADR-022 (Regional Localization): explicitly addressed — `islamic-giving.yaml`'s purpose note and `governance.md` Rule 5 state why the seven giving-type concepts are not subject to synonym-collapse. ADR-023 (Value Objects): `funding_window` passes the §17 promotion test and is correctly modeled as a Value Object, not an entity, mirroring `language_competency`. ADR-024 (Foundational/Operational tiering — structural precedent): this domain's own 8B/8C split explicitly mirrors ADR-024's Tier 1/Tier 2 discipline, recorded in `governance.md`'s Maturity section. |

**Self-audit outcome: no unresolved defect found.** The one issue caught
(property ID collision) was fixed within this pass, not merely noted.

## 6. Remaining Work for Stage 8C

1. **Ratify ADR-DRAFT-025 through ADR-DRAFT-028** (or at minimum
   ADR-DRAFT-028 before 8C begins) — numbering, `Accepted` status, and
   integration into `architecture-decisions/README.md` remain outstanding
   for all four, per `HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` Part 7.
2. **Integrate `PREPARED_GOVERNANCE_ADDITIONS.md`** into
   `ontology_authority_matrix.md`, `GLOSSARY.md`, and the three named
   existing files' boundary notes — a governance action explicitly deferred
   by this phase's own instructions, not an oversight.
3. **Author Stage 8C** (`resource`, `financial_resource`, `material_resource`,
   `inventory_item`, `storage_location`, `resource_allocation`, stock
   movement taxonomy) per ADR-DRAFT-028, resolving the deferred
   `consumable`/`equipment`/`asset` entity-vs-taxonomy-value question
   empirically during that authoring (DR-FLAG-C).
4. **Author the Support Delivery reference row** (`delivery_event
   fulfilled_from resource_allocation`) — cannot be authored until Stage 8C's
   `resource_allocation` entity exists; correctly not attempted in this pass.
5. **Extend the `distinct_from` note** in
   `support-delivery/taxonomy/delivery-modalities.yaml` to a three-way note
   once Stage 8C's `resource_category` exists (staged in
   `PREPARED_GOVERNANCE_ADDITIONS.md` §3.2).
6. **Revisit DR-FLAG-A** (donor-as-role vs. a shared `funding_source_party`
   supertype) only if a second future domain independently needs a generic
   Person-or-Organisation abstraction — not before.
7. **Revisit DR-FLAG-B** (contributed labor as a donor-reported resource) only
   as its own separately-governed Phase 2 proposal, re-running the
   ADR-DRAFT-026 analysis against Volunteer Operations' state at that time.

---

**Net result:** Donor & Funding Intelligence is implemented as a standalone,
self-consistent canonical domain — 3 entities, 9 relationship rows (including
1 cross-domain reference into Programs), 17 data properties, 6 semantic
constraints, and 3 taxonomy files totaling 14 concepts across 3 schemes on
the donor-classification side, 15 concepts across 2 schemes on the Islamic
Giving side, and 18 concepts across 3 schemes on the funding-lifecycle
side — with zero modification to any existing repository file and every
governance-facing addition staged for review rather than silently
integrated.
