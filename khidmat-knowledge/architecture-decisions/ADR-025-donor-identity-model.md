# ADR-025

## Title
Donor Identity Model

## Status
Accepted

## Date
2026-07-17 (drafted HKMP Stage 8A; ratified and integrated HKMP Stage 8D)

## Context
Stage 8 needs to represent who gives to Khidmat's operations — individuals, institutions,
corporations, governments, foundations, faith-based bodies, community collectives, and anonymous
givers. No such concept existed prior to Stage 8; the closest was the generic `shared:organisation`,
which conflates funder, implementer, infrastructure operator, and referral target into one entity
with no donor-specific structure.

## Alternatives Considered
1. **Independent Entity** — a standalone `donor` entity unrelated to `person`/`organisation`.
2. **Role Profile** — a `donor_profile` entity attached behind existing `person`/`organisation`
   entities via reference relationships (this ADR's decision).
3. **Specialized Person** — `donor` modeled as a subtype/specialization of `person` only.
4. **Specialized Organisation** — `donor` modeled as a subtype/specialization of `organisation`
   only.
5. **Hybrid Pattern** — a narrow shared supertype (`funding_source_party`) specializing both
   `person` and `organisation`, with `donor_profile` attaching to the supertype.

Alternatives 3 and 4 are rejected together: donors are demonstrably both individuals *and*
institutions in the original brief itself ("Individual donors... Institutional donors... Corporate
donors..."), so specializing only one of `person`/`organisation` cannot represent the other half of
the requirement without a second, parallel specialization anyway — collapsing back into needing
both, i.e. effectively Alternative 2 or 5 with extra steps and two inheritance edges to maintain
instead of two reference edges. Alternative 1 (Independent Entity) is rejected as a repeat of the
already-resolved FLAG-005 failure mode (`household` vs. `household_snapshot`). Alternative 5
(Hybrid/shared supertype) is rejected for now as disproportionate governance cost for a
single-consumer need — revisit if a second domain independently needs a Person-or-Organisation
abstraction.

## Decision
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
relationships (`min: 0`), not an error state.

## Consequences
- **Positive:** No identity fork; a donor who is also a referral source, community representative,
  or registrant is discoverable via existing identity, not a bespoke reconciliation.
- **Positive:** Reuses a certified pattern, lowering review risk.
- **Constraint:** `donor_profile` must never redefine any `person`/`organisation` field (name,
  contact, demographic data) — donor-specific structure only.
- **Constraint:** A `donor_profile` must attach to at most one of `person`/`organisation`, never
  both simultaneously (enforced: `donor-resource/ontology/semantic-constraints.yaml#donor_profile_attachment_exclusive`).
- **Open item carried forward:** if a second future domain needs a generic Person-or-Organisation
  abstraction, revisit whether to promote to Alternative 5's shared supertype at that time — not
  pre-emptively (`donor-resource/governance.md` DR-FLAG-A).

## Implementation Status
Fully implemented: `donor_profile` (`donor-resource/ontology/entities.yaml`),
`donor_profile_of_person` / `donor_profile_of_organisation`
(`donor-resource/ontology/relationships.yaml`, relationship verbs
`profile_of_person` / `profile_of_organisation` — renamed from a shared
`profile_of` per HKMP Stage 8R Certification Remediation to comply with
`Canonical_Ontology_Schema.md` §9; no semantic change), the mutual-exclusivity
constraint (`donor-resource/ontology/semantic-constraints.yaml`). See
`HKMP_STAGE8B_IMPLEMENTATION_REPORT.md` and
`HKMP_STAGE8R_CERTIFICATION_REMEDIATION_REPORT.md`.

## Related Documents
- ADR-008 (Single Ownership), ADR-018 (Shared Subject Supertype — structural precedent),
  ADR-024 (`volunteer_profile`/`profile_of` — direct pattern precedent), FLAG-005, FLAG-006
  (`ontology_authority_matrix.md`)
- `HKMP_STAGE8_DONOR_RESOURCE_DOMAIN_DISCOVERY_REPORT.md`,
  `HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md` (Part 1 Decision 1, Part 2 — original draft)
