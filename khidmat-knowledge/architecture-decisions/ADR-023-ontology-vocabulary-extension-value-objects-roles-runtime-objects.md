# ADR-023

## Title
Ontology Vocabulary Extension — Value Objects, Roles, Runtime/Reasoning Objects, and Future Entity Candidates

## Status
Proposed (pending reviewer ratification, per `Canonical_Ontology_Schema.md` §16)

## Context
`Canonical_Ontology_Schema.md` (the frozen ontology authoring contract) currently recognizes exactly
two citizens: **Entity** (§4) and **Data Property** (§5, `datatype` or `taxonomy_ref` only — "no
nested objects"). Registration's Phase 4 (Attribute Decomposition) is the first phase in the
repository to require decomposing composite attributes (`contact`, `location`, `guardian_status`,
`treatment_plan`, `cost_estimate`, `requested_amount`, `case.open_gaps`) into this vocabulary. Because
the contract offers no third option, its own D6 decision rule defaults to "promote every nested
object to its own Entity" — not as a deliberate modeling choice, but because it is the only move the
vocabulary leaves available.

A pre-Phase-4 architecture review evaluated this against the final system described in
`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` (Khidmat AI as a Humanitarian Operating System — Person →
Family → Household → Community → Needs → Capabilities → Health → Dependencies → Risks → Support →
Outcomes → Impact, with multi-agent reasoning, donor matching, and volunteer matching) and found:

- Promoting fact-bundles like `contact_point`, `location`-snapshot, `income`, `cost_estimate` to
  Entities creates nodes nothing in the final graph ever needs to reference, and compounds the
  already-flagged generic-`has`-predicate problem (Registration Domain Audit, O-R1) by adding more
  content-free edges at exactly the scale (10+ future domains) where the graph needs to stay legible
  to multi-agent reasoning.
- `guardian` is already modeled correctly elsewhere in the repository — `shared/human-model/ontology
  /family-structure.yaml` treats it as a kinship/support **role** held by an existing person, not as
  its own entity type. The Business Blueprint's own Family Model (§4) independently confirms this:
  Guardian is listed alongside Parent, Caregiver, and Spouse as a relationship type. Minting a
  `guardian` entity in Registration would duplicate this existing, correctly-modeled concept and
  violate ADR-008 (Single Ownership of Concepts) and `ARCHITECTURE.md`'s Reference-Not-Redefine rule.
- `case.open_gaps` is reasoning output (a finding produced by `reasoning/gap-detection-rules.yaml`
  against one case at one moment), not a stable domain fact. Modeling it as an `open_gap` entity with
  a `has_open_gap` relationship would put a reasoning *product* inside the model of *what exists in
  the world* — and the Business Blueprint's proactive-detection goals (§2, §13) guarantee more of
  these diagnostic artifacts are coming (risk flags, vulnerability scores, prioritization signals),
  making this a repository-wide problem, not a Registration-only one.
- Some composite attributes (`treatment_plan`) are correctly Value Objects *today* but plausible
  Entity candidates once Support Delivery / Outcome Tracking activate and need to reference and update
  them across time. The contract has no way to record that distinction as a deliberate, revisitable
  decision rather than a silent default.

Because at least ten further domains in the Business Blueprint (Family, Community, Needs,
Vulnerability, Risk, Support, Outcome, Donor Matching, Volunteer Matching, Impact) will each reach the
same fork Registration's Phase 4 has reached, resolving this once at the contract level is cheaper
than resolving it once per domain, and vastly cheaper than retrofitting it after several domains have
already baked in an entity-explosion pattern.

## Problem Statement
The ontology authoring contract's two-citizen vocabulary (Entity / Data Property) is insufficient to
correctly model the final Humanitarian Operating System. Without a third citizen for owned,
identity-less fact bundles; a documented pattern for roles; an explicit boundary against absorbing
reasoning output into the entity graph; and a way to flag deferred-but-anticipated entity promotions,
every future domain's attribute-decomposition phase will face the same fork Registration faces now,
and will resolve it inconsistently, at increasing cost the later it is caught.

## Decision
Extend `Canonical_Ontology_Schema.md` with four additive sections — §17 Value Objects, §18 Roles, §19
Runtime/Reasoning Objects, §20 Future Entity Candidate, and a closing §21 Amendment status — under the
same `[PROPOSED]`/ratification discipline the document already applies to §§3, 10–12. See the exact
amendment text in `docs/architecture/Canonical_Ontology_Schema.md` §§17–21.

**Summary of the four additions:**

1. **Value Objects (§17):** a structured, owner-scoped fact bundle with no independent identity and
   no referenceability — the missing citizen between scalar Data Property and Entity. Serialized as a
   composite `fields:` row within the existing `data-properties.yaml` file (no new file; the fixed
   five-file set in §2 is unchanged). Promoted to Entity only if it fails a four-part identity/
   referenceability/multiplicity/lifecycle test, replacing D6's blanket "promote to entity" default.
2. **Roles (§18):** a functional position an existing Entity holds relative to another Entity, never
   its own Entity type — expressed as a `taxonomy_ref` data property or a relationship row on the
   role-holder. Generalizes the pattern `shared/human-model` already uses correctly for `guardian` and
   `legal_guardian` into a repository-wide rule.
3. **Runtime/Reasoning Objects (§19):** reasoning-produced diagnostic findings (gaps, escalations,
   scores, flags) are permanently out of ontology scope. Their authoritative representation is
   reserved for a not-yet-written **Runtime/Instance-State Schema**, named here the same way
   `Canonical_Taxonomy_Schema.md` was named as a required peer document before it existed.
4. **Future Entity Candidate (§20):** an optional, non-normative annotation on a Value Object row
   recording that its promotion criteria may be met once a named dependent domain activates — turning
   a silent future surprise into a tracked governance fact (logged via `ontology_authority_matrix.md`'s
   existing Flagged Boundary Cases pattern).

**Nothing else changes.** §§2, 4–9, 13–15 (every existing Entity, Relationship, Cardinality,
Constraint, and domain rule) are untouched, unrenumbered, and remain exactly as previously ratified.

## Alternatives Considered
- **Freeze the contract as-is and let Registration's Phase 4 resolve D6 locally:** rejected. At least
  ten further Business-Blueprint domains will hit the identical fork; resolving it once per domain
  produces inconsistent graphs at the scale multi-agent reasoning needs consistency most.
- **Add a sixth `value-objects.yaml` file to the fixed module layout (§2):** rejected in favor of a
  composite row within the existing `data-properties.yaml`. A new file would touch §2 (RATIFIED) and
  every domain's minimum-conformance file set; a composite row extends §5's row shape additively and
  leaves §2 untouched.
- **Model roles as a new Entity subtype (e.g. `RoleAssignment`):** rejected. It reintroduces the exact
  entity-explosion problem this amendment exists to prevent, and duplicates identity that the
  role-holder already carries.
- **Resolve the Runtime/Reasoning boundary by inventing the Instance-State Schema now, in this same
  amendment:** rejected as out of scope for a bounded amendment. §19 reserves the boundary and names
  the peer document; authoring that document is separate, larger work, exactly as
  `Canonical_Taxonomy_Schema.md` was reserved before it was written.

## Consequences
- Registration's Phase 4 cannot execute against the current D6 decision table — D6 is superseded and
  must be re-authored against §§17–20 before Phase 4 resumes. (This ADR does not perform that
  re-authoring; it is a separate, subsequent action.)
- Every future domain's attribute-decomposition work has a consistent, pre-decided vocabulary to
  execute against, removing an entire class of per-domain re-litigation.
- The entity graph gains a documented discipline against explosion from fact-bundle promotion and
  from reasoning-output absorption — both identified as risks specifically because of the graph's
  scale under the final Business Blueprint (§13's Humanitarian Knowledge Graph).
- A Runtime/Instance-State Schema is now a named, tracked dependency (like the taxonomy peer document
  was) rather than an implicit gap.

## Governance Impact
- `ontology_authority_matrix.md` gains no new domain-owned concept entries — Value Object, Role,
  Runtime/Reasoning Object, and Future Entity Candidate are authoring-contract primitives owned by
  `Canonical_Ontology_Schema.md` itself, not domain concepts subject to the per-domain ownership
  table. Individual `future_entity_candidate` flags raised by domains going forward should be logged
  in the matrix's existing **Flagged Boundary Cases** section, using the pattern already established
  there (see FLAG-001–004).
- `Repository_Migration_Methodology.md` and `Registration_Migration_Plan.md` are unaffected by this
  ADR directly; however, `Registration_Migration_Plan.md`'s D6 decision table is now superseded and
  requires a follow-up Phase-0-equivalent re-approval pass before Phase 4 executes, re-authored under
  §§17–20.
- A **Runtime/Instance-State Schema** is added to the repository's list of required peer documents
  (alongside `Canonical_Taxonomy_Schema.md`), to be authored and ratified before any domain represents
  reasoning-produced findings as persistent, referenceable structure.

## Repository Impact
- **`docs/architecture/Canonical_Ontology_Schema.md`:** amended additively (§§17–21). No RATIFIED
  section altered or renumbered.
- **No domain ontology YAML is modified by this ADR** — `registration/`, `shared/`, `shared/human-
  model/`, `shared/risk/`, `community-context/`, `verification-operations/`, `case-management/`,
  `beneficiary-lifecycle/`, `needs-assessment/`, and all placeholder domains are untouched.
- **Migration impact on already-migrated domains:** none required. The amendment is additive — every
  existing scalar `data-properties.yaml` row remains valid (it is simply the `datatype`/`taxonomy_ref`
  branch of the now-richer row shape); every existing entity and relationship remains valid as
  authored. `shared/human-model/ontology/family-structure.yaml` already conforms to §18 (Roles) as
  written and needs no change — it is the reference example the section generalizes from.
- **Not yet verified in this pass:** a full conformance sweep of `community-context`,
  `verification-operations`, `case-management`, `beneficiary-lifecycle`, `needs-assessment`, and
  `shared/risk` against §§17–20 (i.e., confirming none of them already promoted a Value-Object-shaped
  concept to an Entity, or absorbed a reasoning finding into their entity graph, before this amendment
  existed). Recommended as a low-risk, fast follow-up: the amendment is additive, so any
  non-conformance found would be flagged for future cleanup, not a break requiring immediate action.
- **Domain requiring changes as a direct consequence of this ADR:** Registration only — and only its
  planning document (`Registration_Migration_Plan.md` D6), not any registration YAML file, since Phase
  4 has not executed. No other domain requires changes as a direct consequence of ratifying this ADR.

## Future Work
- Author and ratify the **Runtime/Instance-State Schema** referenced by §19 — the peer document
  needed before reasoning-produced findings (gaps, escalations, scores) can be given any persistent,
  referenceable representation.
- Re-author `Registration_Migration_Plan.md`'s D6 decision table against §§17–20 as a Phase-0-
  equivalent gate, before Phase 4 (Attribute Decomposition) resumes.
- Perform the conformance sweep noted above against already-migrated domains.
- Consider, once two or more domains have authored the same Value Object shape (e.g. `money`),
  promoting it to a shared reusable type per §17's cross-domain rule, mirroring §11's predicate-
  promotion governance.
