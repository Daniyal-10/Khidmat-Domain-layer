# HKMP Stage 8E — Independent Repository Semantic Integrity Audit

**Posture:** Independent certification audit. No prior Stage 8 document (Discovery, 8A Architecture,
8B/8C Implementation, 8D Governance) is treated as evidence of correctness — every claim below was
re-derived directly from the current repository content using direct file reads and greps executed
during this audit. Where a prior report's narrative is cited, it is cited as a claim being checked,
not as a fact. No repository file was modified to produce this report.

---

## 1. Executive Summary

The Donor & Resource domain is structurally sound at the top level — no duplicate entity or
taxonomy-concept IDs exist anywhere in the repository, no cyclic cross-domain dependency was found,
and the major boundary claims (no volunteer content, no custody-chain modeling, additive-only
cross-domain edges) hold up under direct verification.

However, this audit found **one Critical, ratified-schema-contract violation** repeated three times,
and **six Major findings** spanning incorrect inheritance placement, an incomplete/unenforceable
core invariant, a type-safety gap in a semantic constraint, an unaddressed taxonomy reconciliation
gap, systematic misuse of the `required_if` constraint type, and a governance-process gap (certified
domains modified without the re-certification discipline the repository's own Stage 7 precedent
established). None of the prior Stage 8 reports (8B, 8C, 8D) disclosed any of these — each was found
by reading the actual YAML and cross-checking it against the repository's own written contract
(`Canonical_Ontology_Schema.md`) and its own precedent files, not by trusting the implementation
reports' self-description.

**Recommendation: Certification Deferred.** The domain's architecture is sound and none of the
findings requires a redesign — but a Critical schema-contract violation and multiple Major
correctness/completeness gaps must be remediated, and the two certified domains touched by Stage 8D
(Programs, Support Delivery) should receive the same independent re-verification the repository gave
itself after Stage 7B, before this domain is marked fully certified.

---

## 2. Audit Methodology

Every finding below was produced by one of the following direct actions during this audit session,
not by summarizing a prior report:

1. Direct `Read`/`grep` of every file under `donor-resource/` (`ontology/*.yaml`, `taxonomy/*.yaml`,
   `README.md`, `governance.md`, `PREPARED_GOVERNANCE_ADDITIONS.md`).
2. Direct comparison of `donor-resource/ontology/semantic-constraints.yaml` against the literal,
   ratified rule text in `docs/architecture/Canonical_Ontology_Schema.md` §9.
3. Direct comparison of `donor-resource/ontology/entities.yaml` and `data-properties.yaml` against
   the repository's own precedent for abstract-supertype/concrete-subtype identity placement
   (`shared/ontology/data-properties.yaml` — `person_id`, `household_id`, `organisation_id`).
4. Direct `grep` for entity-ID and taxonomy-concept-ID collisions across the **entire** repository
   (not just `donor-resource/`), to independently verify the "no duplicates" claims made in 8B/8C.
5. Direct inspection of the five existing-repository files Stage 8D modified
   (`programs/ontology/entities.yaml`, `programs/taxonomy/funding-and-compliance.yaml`,
   `support-delivery/ontology/relationships.yaml`, `support-delivery/ontology/entities.yaml`,
   `support-delivery/taxonomy/delivery-modalities.yaml`), including their version headers, both
   before and after Stage 8D's stated changes.
6. Direct YAML-load validation of every touched file (via a standard YAML parser) to catch structural
   defects a narrative review would miss.
7. Direct comparison of `architecture-decisions/ADR-025` through `ADR-028` against the formatting of
   two pre-existing, independently-reviewed ADRs (`ADR-018`, `ADR-024`) for structural consistency.

No claim in this report rests on "the Stage 8B/8C/8D report says X" without an independent check of
X against the actual file.

---

## 3. Repository Statistics (Independently Verified)

| Metric | Count | Verification method |
|---|---|---|
| `donor-resource/` entities | 9 | `grep -c "^  - id:" ontology/entities.yaml` |
| `donor-resource/` relationships | 17 | `grep -c "^  - id:" ontology/relationships.yaml` |
| `donor-resource/` data properties | 37 | `grep -c "^  - id:" ontology/data-properties.yaml` |
| `donor-resource/` semantic constraints | 15 | `grep -c "^  - id:" ontology/semantic-constraints.yaml` |
| `donor-resource/` taxonomy schemes | 16 (across 7 files) | per-file `grep -c` |
| `donor-resource/` taxonomy concepts | 95 (across 7 files) | per-file `grep -c` |
| Existing repository files modified (Stage 8D) | 9 (`GLOSSARY.md`, `architecture-decisions/README.md`, `knowledge_layer_roadmap.md`, `ontology_authority_matrix.md`, and 5 domain files) | `git status --porcelain` |
| New ADRs | 4 (ADR-025–028) | `architecture-decisions/` directory listing |
| Duplicate entity/taxonomy IDs found repository-wide | 0 | full-repository `grep` per ID (§5.1) |
| Cyclic cross-domain dependencies found | 0 | manual edge-by-edge trace (§7.4) |

All counts match what the Stage 8B/8C/8D reports claimed — this audit found no numerical
misrepresentation in the prior reports' self-reported statistics. The defects found are structural
and semantic, not accounting errors.

---

## 4. Ontology Findings

### 4.1 [CRITICAL] `property` field in three `mutually_exclusive` constraints violates the ratified constraint-schema contract

**Evidence:** `docs/architecture/Canonical_Ontology_Schema.md` §9 (marked `[RATIFIED]`) states, in
its own constraint-row field table:

> `property` | yes | The **canonical reusable property name** the constraint binds (the
> `relationship` value from §6, or a `data_properties` `id` from §5) — **never a per-row
> relationship `id`**.

Three constraints in `donor-resource/ontology/semantic-constraints.yaml` use a per-row relationship
`id` as `property`, directly contradicting this rule:

- `donor_profile_attachment_exclusive` — `property: donor_profile_of_person`. The relationship's
  actual canonical verb (`relationship:` field in `relationships.yaml`) is `profile_of`, not
  `donor_profile_of_person` (that is the row's `id`).
- `resource_allocation_target_exclusive` — `property: resource_allocation_allocated_to_program`.
  The canonical verb is `allocated_to`.
- `resource_allocation_funding_source_exclusive` — `property: resource_allocation_funded_by_grant`.
  The canonical verb is `funded_by`.

The `parameters.with:` lists in all three constraints repeat the same error
(`donor_profile_of_organisation`, `resource_allocation_allocated_to_case_plan`,
`resource_allocation_funded_by_contribution` are all row `id`s, not verbs).

**Root cause (not disclosed in any Stage 8 report):** in each of these three cases, the domain
deliberately authored **two relationship rows sharing one relationship verb** pointing at two
different target types (`profile_of` → `person` / `organisation`; `allocated_to` → `program` /
`case_plan`; `funded_by` → `grant` / `contribution`). The schema's own precedent for
`mutually_exclusive` (`community-context/ontology/semantic-constraints.yaml`) only covers the case
of mutually exclusive **data properties**, each with its own unique id — it has no precedent for
disambiguating two **relationship rows that share a verb**. Using the bare verb (`profile_of`) as
`property` would be schema-compliant but referentially ambiguous (it wouldn't say which target the
constraint is about); using the row `id` disambiguates but breaks the explicit, ratified rule. This
is a genuine, unresolved gap in how the schema's constraint mechanism composes with the domain's own
identity-attachment design pattern (ADR-025) — not a typo, and not fixable by find-and-replace
without either renaming relationships or amending the schema.

**Affected files:** `donor-resource/ontology/semantic-constraints.yaml` (3 of 15 constraints, 20%),
`docs/architecture/Canonical_Ontology_Schema.md` §9 (the contract being violated).

**Severity:** Critical. This is not a style nit — it is a direct, verifiable violation of a document
explicitly marked `[RATIFIED]`, the repository's own definition of a binding contract. A generator
consuming `semantic-constraints.yaml` mechanically (the entire stated purpose of that file's
target-neutral design, per §9) cannot resolve `donor_profile_of_person` as a "canonical reusable
property name" — it is not one.

**Recommended remediation:** Either (a) rename the relationship pairs so each row has a distinct
canonical verb (e.g. `profile_of_person` / `profile_of_organisation` as the `relationship:` value,
not just the `id:`), making the existing `property:` values schema-compliant without further
change, or (b) propose and ratify a schema amendment to §9 permitting a `to:`-qualified disambiguator
when two rows share a verb. Option (a) is lower-risk and does not require touching
`Canonical_Ontology_Schema.md`.

---

### 4.2 [MAJOR] Identity properties (`resource_id`, `resource_name`) placed on the abstract `resource` entity, inverting the repository's own established inheritance pattern

**Evidence:** `donor-resource/ontology/entities.yaml` describes `resource` as: *"Abstract supertype
... owns no allocatable/trackable data itself (mirrors `subject`'s 'owns no demographic data'
discipline exactly)"* and *"Owns nothing beyond the identity fields common to every resource kind
(resource_id, resource_name)."* But `donor-resource/ontology/data-properties.yaml` then declares:

```yaml
- id: resource_id
  domain: resource
- id: resource_name
  domain: resource
```

Checked directly against the repository's own actual precedent
(`shared/ontology/data-properties.yaml`), the abstract `subject` entity has **zero** data properties
of its own — no `subject_id` exists anywhere. Instead, each **concrete specialization** owns its own
identifier: `person_id` (`domain: person`), `household_id` (`domain: household`),
`organisation_id`/`organisation_name` (`domain: organisation`). This is the literal, checked pattern
`resource.entities.yaml`'s own text claims to mirror — and does not.

**Consequence:** the entity's own stated design intent ("owns no allocatable/trackable data itself")
is self-contradicted by declaring `resource_id`/`resource_name` as belonging to `resource` rather
than to `financial_resource`/`material_resource` individually (each of which would need its own
`financial_resource_id`/`financial_resource_name` and `material_resource_id`/`material_resource_name`
under the actual repository precedent — which the repository has never had cause to do inconsistently
before this domain).

**Affected files:** `donor-resource/ontology/entities.yaml` (the `resource` entity's own
`ownership_boundary` text), `donor-resource/ontology/data-properties.yaml` (lines declaring
`resource_id`, `resource_name`).

**Severity:** Major — an "incorrect inheritance" defect, explicitly one of the categories this audit
was asked to check for, with a direct, checkable repository precedent it contradicts.

**Recommended remediation:** Move `resource_id`/`resource_name` (or an equivalent identity pair) down
to `financial_resource` and `material_resource` individually, matching the `person_id`/`household_id`
precedent, and update `resource`'s `ownership_boundary` text to no longer claim an identity field it
should not own — or, if a shared identity field across both specializations is genuinely desired,
document this as a deliberate, disclosed deviation from the `subject` precedent with an explicit
rationale (neither is currently done).

---

### 4.3 [MAJOR] `allocated_quantity_not_exceed_available` cannot detect over-allocation across multiple `resource_allocation` instances

**Evidence:** `donor-resource/ontology/semantic-constraints.yaml`:

```yaml
- id: allocated_quantity_not_exceed_available
  type: cardinality
  property: allocated_quantity
  entities: [resource_allocation, inventory_item]
  parameters:
    expression: "allocated_quantity <= inventory_item.quantity_on_hand"
```

`inventory_item` has exactly one quantity property, `quantity_on_hand` — there is no
`reserved_quantity`, `available_quantity`, or any field tracking how much of an `inventory_item` is
already committed by *other* `resource_allocation` instances. `resource_allocation_allocates_
inventory_item` (`relationships.yaml`) permits unlimited `resource_allocation` rows to target the
same `inventory_item` (cardinality on the `inventory_item` side is `{min: 0, max: unbounded}` via
the relationship's directionality). This means N separate `resource_allocation` instances can each
individually satisfy `allocated_quantity <= quantity_on_hand`, while their **sum** exceeds
`quantity_on_hand` — the exact "allocated quantity cannot exceed available quantity" invariant the
originating brief explicitly required is not actually enforceable by this constraint in the
realistic multi-allocation case, which is the normal case for any inventory item drawn on by more
than one case plan or program.

**Affected files:** `donor-resource/ontology/semantic-constraints.yaml`,
`donor-resource/ontology/data-properties.yaml` (missing the field needed to make this checkable),
`donor-resource/ontology/relationships.yaml` (`resource_allocation_allocates_inventory_item`).

**Severity:** Major — a named, explicitly-required invariant is incompletely modeled such that it is
satisfied vacuously in the common multi-allocation case, not just an edge case.

**Recommended remediation:** Either add a derived/tracked `available_quantity` (or
`reserved_quantity`) property to `inventory_item` that nets out all non-cancelled
`resource_allocation`s against it, with the constraint checking against that field instead of raw
`quantity_on_hand`; or explicitly document (if intentional) that aggregate stock accounting is
out of ontology scope and reserved for a runtime/reasoning layer (per ADR-023 §19), rather than
presenting the current constraint as satisfying the brief's invariant.

---

### 4.4 [MAJOR] `cold_chain_integrity_constraint` references a property that does not exist on one branch of its own polymorphic target

**Evidence:**

```yaml
- id: cold_chain_integrity_constraint
  type: required_if
  parameters:
    condition: "inventory_item.instance_of.cold_chain_required is true"
```

`inventory_item_instance_of_resource` (`relationships.yaml`) targets the **abstract** `resource`
entity polymorphically — an `inventory_item` may instantiate either `financial_resource` or
`material_resource`. `cold_chain_required` (`data-properties.yaml`) is declared with
`domain: material_resource` only; `financial_resource` has no such property. The constraint's
condition, `inventory_item.instance_of.cold_chain_required`, is therefore undefined/unresolvable for
any `inventory_item` instantiating a `financial_resource` — the constraint does not guard against
this case (e.g. with a type-check first), it simply assumes the property exists on whatever
`instance_of` resolves to.

**Affected files:** `donor-resource/ontology/semantic-constraints.yaml`,
`donor-resource/ontology/data-properties.yaml`.

**Severity:** Major — a type-safety gap in a hand-authored cross-entity expression, in a file whose
own header states these expressions must be "target-neutral structural facts" a generator can render
mechanically; an unresolvable property path on one branch of a polymorphic type is not
mechanically renderable without additional type-narrowing logic this constraint does not supply.

**Recommended remediation:** Either scope the constraint's `entities:`/condition explicitly to
`material_resource` (via an intermediate check that `instance_of` resolves to that specific
subtype), or restate the condition defensively (e.g. `inventory_item.instance_of.cold_chain_required
is true` only evaluated when applicable, with financial-resource-backed inventory items implicitly
and explicitly exempted in the constraint's own text, not just in prose elsewhere).

---

## 5. Taxonomy Findings

### 5.1 [Verified — no defect] No duplicate entity or taxonomy-concept IDs anywhere in the repository

Independently re-checked (not assumed from the 8B/8C reports): every entity ID
(`donor_profile`, `grant`, `contribution`, `resource`, `financial_resource`, `material_resource`,
`inventory_item`, `storage_location`, `resource_allocation`) and every taxonomy scheme ID
(`donor_type`, `donor_engagement_pattern`, `anonymity_level`, `islamic_giving_type`,
`zakat_eligible_category`, `grant_status`, `contribution_status`, `renewal_status`,
`material_resource_category`, `financial_resource_category`, `resource_condition`,
`stock_movement_type`, `storage_location_type`, `allocation_priority`, `allocation_status`,
`reservation_state`) was grepped against the full repository. Every match occurs only within
`donor-resource/`. No collision found.

### 5.2 [MAJOR] `financial_resource_category` has no `distinct_from` reconciliation against `intervention_modality` / `delivery_modality`, despite direct semantic overlap

**Evidence:** `donor-resource/taxonomy/resource-classification.yaml`'s `references:` block contains
exactly two entries, both scoped to `material_resource_category`:

```yaml
references:
  - scheme: programs:intervention_modality
    relation: distinct_from
  - scheme: support_delivery:delivery_modality
    relation: distinct_from
```

`financial_resource_category` (concepts: `unrestricted_cash`, `restricted_cash`, `voucher_value`,
`revolving_fund`, `emergency_reserve`) is never mentioned. Yet `programs:intervention_modality`
includes `cash` and `voucher` values, and `support_delivery:delivery_modality` includes
`digital_cash_voucher` and `physical_cash_voucher` — a direct, unreconciled terminology overlap with
`financial_resource_category#voucher_value` and the two cash categories. `HKMP_STAGE8A_
ARCHITECTURE_AND_GOVERNANCE.md` Part 5 explicitly named "resource_category vs. intervention_modality"
and "resource_category vs. delivery_modality" as requiring reconciliation — this was only half-done.

**Affected files:** `donor-resource/taxonomy/resource-classification.yaml`.

**Severity:** Major — a named collision-review requirement from the domain's own architecture
document was left half-complete, and no prior implementation or integration report (8B, 8C, 8D)
disclosed the gap; all three described the reconciliation as complete.

**Recommended remediation:** Add a `references:` entry (or extend the existing two) explicitly
covering `financial_resource_category`'s relationship to both schemes' cash/voucher values.

### 5.3 [Verified — no defect] Islamic Giving taxonomy is internally consistent and correctly excluded from ADR-022 localization discipline

Checked `donor-resource/taxonomy/islamic-giving.yaml` directly: all 7 `islamic_giving_type` concepts
and 8 `zakat_eligible_category` concepts are distinctly defined with no internal overlap, and the
file's own purpose note explains the ADR-022 exclusion accurately against the actual text of ADR-022
(checked against `architecture-decisions/ADR-022-canonical-concepts-and-regional-localization-strategy.md`).
No localization-discipline violation found.

### 5.4 [MINOR] Namespace-declaration convention inconsistency within the domain's own files

**Evidence:** `donor-resource/ontology/data-properties.yaml`:

```yaml
namespaces:
  programs_tax: "programs/taxonomy/funding-and-compliance.yaml"
```

This is a file-path-string namespace value — the exact form `Canonical_Ontology_Schema.md` §10
names as the anti-pattern being phased out (*"The current file-path namespace values ... are the
anti-pattern C-2 removes"*), and the exact form `volunteer-operations/ontology/relationships.yaml`'s
own comment records having been *retargeted away from* for that domain. Meanwhile
`donor-resource/ontology/relationships.yaml` and every `donor-resource/taxonomy/*.yaml` file with a
`namespaces:` block use the newer domain-name-only convention (`programs: programs`). This is an
internal inconsistency within one domain's own module set, introduced in this domain from scratch
(not inherited from a prior era of the repository).

**Affected files:** `donor-resource/ontology/data-properties.yaml`.

**Severity:** Minor — does not break resolution (the file-path form is still a valid, if deprecated,
form used elsewhere in the repository), but is an avoidable inconsistency in newly-authored content.

**Recommended remediation:** Change to `programs_tax: programs` (or the appropriate domain-name-only
form) to match the rest of the domain's own files.

---

## 6. Relationship Findings

### 6.1 [Verified — no defect] Inverse pairs are complete and correctly reciprocal

Every relationship row with an `inverse:` field was checked against its named counterpart:
`grant_issued_by_donor_profile` ↔ `donor_profile_issues_grant`,
`contribution_given_by_donor_profile` ↔ `donor_profile_gives_contribution`,
`contribution_contributes_to_grant` ↔ `grant_receives_contribution`,
`inventory_item_stored_at_storage_location` ↔ `storage_location_holds_inventory_item`. All four
pairs exist, and each pair's cardinalities are consistent with each other (e.g. a `1..1` forward edge
paired with a `0..unbounded` reverse edge, not a contradictory pairing).

### 6.2 [Verified — no defect] No orphan relationships; polymorphic references follow established precedent

`inventory_item_instance_of_resource` targets the abstract `resource` entity directly rather than
requiring a row per concrete subtype. This was checked against
`beneficiary_lifecycle_tracks_journey_of_subject`
(`beneficiary-lifecycle/ontology/relationships.yaml`), which does the identical thing for
`shared:subject` — confirmed as an established, correct repository pattern, not an ontology smell.
`financial_resource`/`material_resource` are never a direct `from`/`to` target of any relationship
row — this is expected and correct under the same precedent (subtypes are reached via
type-narrowing on the polymorphic edge, not via separate edges).

### 6.3 [Verified — no defect] No cyclic cross-domain dependency

Traced every cross-domain edge `donor-resource/` authors (`→ shared:person`, `→
shared:organisation`, `→ programs:program`, `→ case_management:case_plan`) and the one edge added
into `donor-resource/` from outside (`support-delivery:delivery_event →
donor_resource:resource_allocation`). None of Programs, Case Management, or Shared Ontology's own
files reference anything in `donor-resource/`. Support Delivery's one new edge is the sole inbound
reference, and `donor-resource/` does not reference Support Delivery anywhere, so no cycle is formed
either directly or transitively through a third domain.

### 6.4 [MAJOR] Systematic misuse of the `required_if` constraint type for cross-entity comparison invariants

**Evidence:** Every existing `required_if` constraint in the repository (checked in
`registration/ontology/semantic-constraints.yaml`, `case-management`, `programs`,
`needs-assessment`) follows one shape: a property that is normally **optional** (`min: 0`) becomes
**required** when a condition holds (e.g. `situation.safety_notes` becomes required
`if safety_flag is true`). Two of this domain's `required_if` constraints do not follow this shape:

- `contribution_date_not_before_grant_window` — `property: contribution_date`, but
  `contribution_date` is **already unconditionally required** (`cardinality: {min: 1, max: 1}` in
  `data-properties.yaml`). The constraint isn't making an optional field required; it's asserting a
  date-ordering invariant (`contribution_date >= grant.funding_window.window_start_date`), smuggled
  into the `required_if` type via an added, non-standard `expression` parameter alongside
  `condition`.
- `cold_chain_integrity_constraint` — `property: storage_location_type`, also already
  unconditionally required on `storage_location` (`{min: 1, max: unbounded}`). Same pattern: a
  membership-check invariant (`cold_chain_storage IN storage_location.storage_location_type`)
  expressed through `required_if`'s `condition`+`expression` combination rather than the type's
  documented meaning.

**Affected files:** `donor-resource/ontology/semantic-constraints.yaml` (2 of 15 constraints).

**Severity:** Major — `Canonical_Ontology_Schema.md` §9 states the constraint-`type` vocabulary "is
closed and extended only by amending this document." No new `type` value was invented, but the
*meaning* of `required_if` was silently repurposed for a use its own established precedent
(consistently, across four other domains) never covers, without disclosing this as a deviation.

**Recommended remediation:** Reclassify these two constraints under `type: cardinality` with an
`expression` parameter — the pattern this domain's own `allocated_quantity_not_exceed_available`
and `inventory_quantity_non_negative` already correctly use for cross-entity/general boolean
invariants — rather than `required_if`, which should be reserved for its established meaning.

---

## 7. Governance Findings

### 7.1 [MAJOR] Two independently-certified domains were modified without a corresponding independent re-certification pass

**Evidence:** `programs/ontology/entities.yaml`, `programs/taxonomy/funding-and-compliance.yaml`,
`support-delivery/ontology/relationships.yaml`, `support-delivery/ontology/entities.yaml`, and
`support-delivery/taxonomy/delivery-modalities.yaml` were all modified by HKMP Stage 8D (confirmed
via `git status --porcelain` and direct diff inspection). Both Programs and Support Delivery
previously underwent an explicit certification process: `HKMP_STAGE7_REPOSITORY_SEMANTIC_INTEGRITY_
AUDIT.md` → `HKMP_STAGE7B_REPOSITORY_REMEDIATION_REPORT.md` → `HKMP_STAGE7C_CERTIFICATION_REVIEW.md`
(the last being explicitly described as *"Independent re-verification ... treated as an unverified
claim, not a fact, until each assertion in it is checked directly"*). The repository's own precedent
is therefore that certified-content modification warrants an independent re-verification pass. No
equivalent pass occurred for Programs or Support Delivery after Stage 8D modified their files — Stage
8D's own report (`HKMP_STAGE8D_INTEGRATION_REPORT.md`) self-certifies its own changes, which is not
independent verification by the repository's own standard.

**Affected files:** `programs/ontology/entities.yaml`, `programs/taxonomy/funding-and-compliance.yaml`,
`support-delivery/ontology/relationships.yaml`, `support-delivery/ontology/entities.yaml`,
`support-delivery/taxonomy/delivery-modalities.yaml`.

**Severity:** Major — a process/governance gap, not an ontology defect in the changes themselves
(this audit's own independent check of those five files, per §4 and §5, found the changes to be
additive and non-redefining as claimed). Recorded as Major because the *absence* of independent
re-verification is itself the finding, consistent with how the repository has treated this class of
gap before (`HKMP_STAGE7C` itself was commissioned for exactly this reason).

**Recommended remediation:** Commission a short, scoped independent re-verification of the five
touched files (this audit constitutes a first pass at that for the Donor & Resource-authored content,
but a dedicated Programs/Support Delivery-side reviewer check is still advisable for completeness).

### 7.2 [MINOR] ADR-025–028 introduce structural elements absent from prior ADRs

**Evidence:** Checked directly against `ADR-018-shared-subject-supertype.md` (uses a single bold
`**Date**: ...` line, no `## Date` heading) and `ADR-024-foundational-layer-precedes-operational-
activation.md` (no date field at all). ADR-025 through ADR-028 each introduce a `## Date` heading and
a `## Implementation Status` section, neither pattern used by either precedent ADR.

**Severity:** Minor — a documentation-consistency issue, not a substantive defect; arguably an
improvement, but not consistent with the two ADRs checked.

**Recommended remediation:** Either retrofit `## Implementation Status` sections onto a sample of
older ADRs for consistency, or note in `architecture-decisions/README.md` that this is an
intentionally evolving template.

### 7.3 [MINOR] Version metadata not incremented on any modified file

**Evidence:** Directly inspected the `version:` header of all five Stage-8D-modified existing files
and all four `donor-resource/ontology/*.yaml` files. `programs/ontology/entities.yaml`,
`programs/taxonomy/funding-and-compliance.yaml`, `support-delivery/ontology/relationships.yaml`, and
`support-delivery/ontology/entities.yaml` all remain at `"1.0.0"` — their pre-Stage-8D version — despite
content changes. `support-delivery/taxonomy/delivery-modalities.yaml` remains at `"1.1.0"` (its
pre-existing, already-bumped-once version) despite a third `references:` entry being added in Stage
8D. Within `donor-resource/` itself, `ontology/entities.yaml` remained `"1.0.0"` across both the
Stage 8B (3 entities) and Stage 8C (+6 entities, a 300% increase) content additions. Checked against
repository convention: `case-management/ontology/relationships.yaml` is at `"1.3.0"`,
`volunteer-operations/ontology/entities.yaml` is at `"1.1.0"` — version increments on content change
are the observed norm elsewhere in the repository.

**Severity:** Minor — a metadata/hygiene gap, not a semantic defect, but it means the `version:`
field can no longer be trusted repository-wide as a signal of "this file changed," undermining its
own stated purpose.

**Recommended remediation:** Bump version strings on all nine files modified across Stage 8B–8D to
reflect their actual change history.

### 7.4 [Verified — no defect] Authority Matrix and Glossary integration are structurally sound and non-duplicating

Checked `ontology_authority_matrix.md`'s Donor & Resource Domain section directly: 15 table rows,
correctly pipe-delimited, positioned between Consent & Privacy and Flagged Boundary Cases as claimed.
Checked `GLOSSARY.md`'s Donor & Resource Terms section: 8 new terms, none colliding with an existing
term name (independently grepped `**Grant**`, `**Contribution**`, `**Resource**`, `**Inventory
Item**` against the full file — each occurs exactly once). The **Resource** entry does cross-reference
**Recovery Resources**, avoiding the exact duplication defect `HKMP_STAGE7C_CERTIFICATION_REVIEW.md`
found in a prior remediation pass (the unreconciled "Case" duplicate). No governance-integration
duplication defect found.

---

## 8. Cross-Domain Findings

| Domain | Reference direction | Verified additive-only? | Findings |
|---|---|---|---|
| Shared Ontology | `donor_profile → person/organisation` | Yes — zero lines changed in `shared/` | See §4.1 (constraint-level issue, not a boundary violation) |
| Programs | `grant/resource_allocation → program`; `funding_source_type/funding_restriction ← programs_tax` | Yes for relationships; two `notes:`/`references:` additions confirmed documentation-only | §5.4 (namespace style), §7.1 (no re-certification), §5.2 (financial_resource_category gap touches this boundary) |
| Support Delivery | `resource_allocation ← delivery_event` (inbound, authored by Support Delivery) | Yes — one new row, correctly authored on the referencing side | §7.1 (no re-certification), §5.2 |
| Case Management | `resource_allocation → case_plan` | Yes — zero lines changed in `case-management/` | None |
| Volunteer Operations | None | Confirmed zero references anywhere in `donor-resource/` (independently grepped for `volunteer_profile`, `volunteer_team`, `skill_category`, `certification_type` — zero matches) | None — ADR-026's exclusion claim holds under direct verification |
| Community Context | None (typing reference only, in prose) | Confirmed zero relationship rows reference `community-context` | None |

---

## 9. AI Reasoning Assessment

An LLM reasoning over this ontology by relationship **verb** alone (a plausible naive traversal
strategy — e.g. "find all `profile_of` edges," "find all `funded_by` edges," "find all `allocated_to`
edges") would be unable to disambiguate target type without also inspecting each row's `to:` field
individually, because this domain reuses one relationship verb across two rows with different targets
in three separate places (`profile_of` → person/organisation; `funded_by` → grant/contribution;
`allocated_to` → program/case_plan). This is the same root design pattern that produced the §4.1
Critical finding — the schema-compliance problem and the AI-reasoning-ambiguity problem share one
cause. A reasoning system that trusts `property:`/`relationship:` as a stable disambiguator (which
the schema's own "canonical reusable property name" framing invites) would need row-level
disambiguation logic the current relationship naming does not provide by itself.

Separately, `grant_islamic_giving_type` and `contribution_islamic_giving_type` are two differently-
named data properties referencing the identical taxonomy scheme (`islamic_giving_type`). This is
correctly disambiguated in both properties' own `notes:` fields, but a system indexing property names
rather than reading notes could plausibly treat these as two different classification schemes rather
than one scheme applied to two entities — a minor terminology-consistency risk, not a defect, since
the underlying data is correctly reconciled.

No confusion risk was found between `donor_type` and `funding_source_types`, or between the Islamic
Giving taxonomy and ADR-022 localization concerns — both carry sufficiently explicit `distinct_from`
notes and purpose statements that a reasoning system reading the taxonomy files directly (not just
concept labels) would resolve correctly.

---

## 10. Boundary Assessment

The Support Delivery boundary ("inventory ends where custody begins") was checked by grepping
`donor-resource/` for `custody_transfer`, `delivery_event`, `proof_of_delivery`, and `custodian` —
zero matches as relationship targets or entity references (the terms appear only in explanatory
prose describing where the boundary sits, never as a `from:`/`to:` value). The boundary holds under
direct verification.

The Volunteer Operations exclusion (ADR-026) was checked by grepping for every Volunteer Operations
taxonomy/entity name — zero matches. The exclusion holds under direct verification.

The one boundary this audit found **not** fully closed is the taxonomy-reconciliation boundary
between `financial_resource_category` and Programs'/Support Delivery's own cash/voucher vocabulary
(§5.2) — the *entity-relationship* boundary is respected (no wrongful ownership), but the
*documentation* boundary (preventing terminology confusion) is incomplete for the financial side of
the resource model.

---

## 11. Risk Assessment

| Risk | Likelihood | Impact | Driving finding(s) |
|---|---|---|---|
| A generator/reasoner mechanically consuming `semantic-constraints.yaml` fails or produces incorrect output on the 3 non-compliant `mutually_exclusive` rows | High if a generator is ever built against this file | Medium — affects 3 of 15 constraints in one domain | §4.1 |
| Silent over-allocation of scarce humanitarian stock across multiple case plans/programs | Medium — depends on whether multi-allocation against one inventory_item is common in practice | High — a resource-integrity failure with real-world consequence | §4.3 |
| A future author reading `resource`'s `ownership_boundary` text takes "owns no allocatable data" at face value and is misled about where identity actually lives | Low-Medium | Low — self-correcting on first close read | §4.2 |
| Terminology confusion between `financial_resource_category` and Programs/Support Delivery's cash/voucher vocabulary in future authoring | Medium | Medium | §5.2 |
| Certified-domain drift going unnoticed without a Stage-8D-equivalent re-certification pass | Low (this audit itself substantially closes the gap for this round) | Medium if it becomes a repeated pattern across future stages | §7.1 |

---

## 12. Certification Recommendation

**Certification Deferred.**

**Evidence supporting this outcome over the alternatives:**

- **Not "Certified"** or **"Certified with Minor Findings"** — one Critical finding exists (§4.1), a
  direct, verifiable violation of a document the repository itself marks `[RATIFIED]`, repeated in 3
  of 15 constraints (20% of this domain's semantic constraints). A Critical finding by this audit's
  own required classification ("Repository integrity failure. Must fix.") is incompatible with either
  "Certified" outcome regardless of how sound the surrounding architecture is.
- **Not "Certification Rejected"** — the architecture itself (the entity hierarchy, the
  role/profile pattern, the additive-only cross-domain discipline, the boundary with Support Delivery
  and Volunteer Operations) was independently verified sound in every check this audit performed (§4,
  §6.1–6.3, §7.4, §8, §10). Every finding is a scoped, nameable, independently-fixable defect — a
  constraint's `property` field, a missing taxonomy note, a misplaced data property, a missing
  aggregation field, a version string — not a structural flaw requiring the domain to be re-designed
  or re-scoped. Rejection would be disproportionate to defects of this shape.
- **"Certification Deferred"** is the correct outcome: remediate the Critical finding (§4.1) and the
  six Major findings (§4.2, §4.3, §4.4, §5.2, §6.4, §7.1) — none of which requires architectural
  redesign — then this domain is a strong candidate for full certification. The Minor findings
  (§5.4, §7.2, §7.3) are advisable to close in the same pass but do not by themselves block
  certification.
