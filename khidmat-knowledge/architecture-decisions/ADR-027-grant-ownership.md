# ADR-027

## Title
Grant Ownership

## Status
Accepted

## Date
2026-07-17 (drafted HKMP Stage 8A; ratified and integrated HKMP Stage 8D)

## Context
Programs already owns program-level funding classification (`funding_source_types`,
`funding_restrictions`, `quota_types`, `compliance_checkpoints`, `audit_findings`) and the only
funding relationship in the graph (`program_funded_by → shared_org:organisation`). Programs' own
gap report names "Grant Management: Tracking the lifecycle of the funding proposal that created the
program" as an explicitly deferred gap. No entity could represent a grant that funds multiple
Programs, or receives multiple `contribution` tranches over time.

## How Grant Relates to Each Adjacent Concept
- **Program:** `grant` optionally funds one or more `program` instances, via a new, additive
  relationship (`grant_funds_program`), coexisting with — not replacing — the existing
  `program_funded_by → organisation` edge for informal/direct funding.
- **Organisation:** `grant` is issued by a `donor_profile` (ADR-025), which in turn attaches to
  `organisation` for institutional donors. `grant` does not reference `organisation` directly — it
  goes through `donor_profile`, keeping the donor-identity indirection consistent everywhere
  funding touches an identity.
- **Contribution:** a `contribution` is a single tranche/gift; it may `contributes_to` a `grant`
  (multi-tranche institutional funding) or stand alone with no `grant` reference (a single
  unrestricted gift). A `contribution` is never itself the funding-lifecycle object — that role is
  `grant`'s alone.
- **Funding Restriction:** `grant` **references** Programs' existing `funding_restrictions` scheme
  (`unrestricted`, `earmarked_geographic`, `earmarked_demographic`, `tied_procurement`) rather than
  authoring a new one — the same restriction vocabulary applies one level up the funding chain from
  where it's used today.
- **Funding Source (Type):** likewise, `grant.funding_source_type` references Programs' existing
  `funding_source_types` scheme. `donor_type` (Donor & Resource's own taxonomy) is a distinct axis
  describing the donor's own segmentation, not the funding instance's category; a `grant` from a
  `private_foundation`-type donor still separately carries `funding_source_types: private_foundation`
  on itself for continuity with how Programs already reads this field, but the two are reconciled
  by note (`donor-resource/taxonomy/donor-classification.yaml`), not merged.

## Should Grant Become an Intermediary, Primary Funding Object, or Optional Abstraction?
**Optional abstraction was chosen.** Mandatory intermediary (all funding must route through Grant)
forces informal/small giving through unnecessary structure and requires modifying certified
Programs content; a primary-funding-object model without an optional/direct path has the same
forcing problem under a different name. Optional abstraction lets both shapes coexist truthfully.

## Decision
`grant` is authored as an **optional abstraction**: a `program` may be funded directly by an
`organisation` (existing edge, untouched) or by a `grant` (additive edge), or both simultaneously
for different funding streams. `grant` is issued by `donor_profile`, references Programs' existing
`funding_source_types`/`funding_restrictions` schemes rather than duplicating them, and is the
aggregation point for multiple `contribution` tranches over time.

**Implementation note on relationship direction:** this ADR's original draft used the illustrative
name `program_funded_by_grant`, implying a row authored on the Programs side. The as-built
relationship is `grant_funds_program` (`from: grant`, `to: programs:program`), authored entirely
within `donor-resource/ontology/relationships.yaml`. This achieves the identical graph connectivity
(a graph is traversable from either end regardless of which end is labeled `from` — per
`HKMP_STAGE7C_CERTIFICATION_REVIEW.md` §1's finding on `case_plan_addressed_by_intervention`) while
requiring zero modification to Programs' certified relationship file, which this ADR's underlying
goal (avoid reopening Programs' certified scope) favors over the illustrative naming. The decision
this ADR ratifies is the *optional abstraction*, not the specific row direction; the direction was
correctly left to implementation discretion and resolved conservatively.

## Consequences
- **Positive:** Zero modification to certified Programs relationship rows.
- **Positive:** Closes the exact gap Programs' own audit named, without Programs having to re-open
  its own certified scope.
- **Constraint:** Documentation carries an explicit reconciliation note so "directly-funded" vs.
  "grant-funded" Programs are understood as two valid shapes, not redundant or conflicting paths to
  the same fact.

## Implementation Status
Fully implemented: `grant`, `contribution` (`donor-resource/ontology/entities.yaml`),
`grant_issued_by_donor_profile`, `contribution_contributes_to_grant`, `grant_funds_program`
(`donor-resource/ontology/relationships.yaml`), `funding_source_type` / `funding_restriction`
`taxonomy_ref` properties (`donor-resource/ontology/data-properties.yaml`). See
`HKMP_STAGE8B_IMPLEMENTATION_REPORT.md` §3 for the disclosed direction deviation and
`HKMP_STAGE8R_CERTIFICATION_REMEDIATION_REPORT.md` for the relationship-verb
naming fixes applied to `resource_allocation_funded_by_grant` /
`_contribution` (a Stage 8C relationship, not owned by this ADR, but renamed
under the same Stage 8R remediation pass — see ADR-028's Implementation
Status).

## Related Documents
- `programs/ontology/relationships.yaml` (`program_funded_by`, referenced not modified),
  `programs/taxonomy/funding-and-compliance.yaml` (referenced not modified, extended with a
  `distinct_from` note per HKMP Stage 8D), ADR-025
