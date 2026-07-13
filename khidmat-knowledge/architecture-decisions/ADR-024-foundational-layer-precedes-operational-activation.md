# ADR-024

## Title
Foundational Knowledge Layer May Be Authored Before Operational Activation (Volunteer Operations Two-Tier Authoring)

## Status
Accepted

## Context

`Volunteer_Operations_Migration_Plan.md` Decision **D-VO1** recorded a blanket
conclusion: *no* canonical `ontology/`/`taxonomy/` content for Volunteer
Operations may be authored until the Stage-9 operational activation trigger
(*"a volunteer management workflow is defined with operations staff"*) fires.
Its two stated bases were:

1. **`Repository_Migration_Methodology.md` §1** — a *migration* "relocates,
   restructures, and re-serializes content that already exists. It never authors
   new descriptive or semantic text." Volunteer Operations has no prior content
   to re-serialize, so a *migration* has nothing to do.
2. **ADR-009 (Dependency-Driven Domain Activation)** — authoring a placeholder
   domain's content before its activation trigger risks it "inventing concepts
   it does not own."

D-VO1 is correct *for a migration*, and correct *for the operational layer*.
But it conflated two distinct bodies of knowledge under one deferral:

- **Tier 1 — the organization-invariant foundation.** The concepts every
  humanitarian volunteer-management system shares regardless of any single
  organization's processes: the *volunteer as a persistent qualified resource*
  (the profile behind `shared:actor`), and the stable vocabularies that qualify
  it — skills, certifications, languages, availability *kinds*, coverage
  *modes*, assignment-type *eligibility*, affiliation. These are not invented
  per organization; they are the canonical ontology/taxonomy the domain exists
  to hold. Authoring them requires **no** operations-staff workflow input and
  depends only on `shared:actor` and `shared/taxonomy/persons.yaml#volunteer`,
  both of which already exist (Stage-8 prerequisite met).
- **Tier 2 — the operational / runtime layer.** Scheduling, dispatch, workload
  balancing, optimization, trust/performance scoring, the assignment *act*, and
  the per-instance assignment/training *history*. These *do* require
  operations-staff-defined process, *are* organization-specific, and several
  (findings, scores, history) are runtime/instance state explicitly reserved out
  of ontology scope by `Canonical_Ontology_Schema.md` §19 (ADR-023).

D-VO1 deferred Tier 1 *and* Tier 2 identically. This ADR separates them.

## Problem Statement

Treating the entire domain as un-authorable until an operational trigger fires
leaves the repository without the one thing a placeholder is meant to protect:
a settled, canonical ownership surface for the domain's foundational concepts.
Every already-active domain (Verification Operations, Case Management) has
already deferred *actor qualification* to Volunteer Operations (FLAG-006); until
that qualification surface is authored, those deferrals point at an empty
domain. Meanwhile, authoring the *operational* layer now would indeed be premature
invention. The contract needs one rule that permits the first and still forbids
the second.

## Decision

**Foundational, organization-invariant ontology and taxonomy for a placeholder
domain MAY be authored ahead of the domain's operational activation trigger,
provided every authored concept is stable across humanitarian organizations and
no organization-specific process, policy, algorithm, score, or runtime finding
is authored.** The operational/runtime layer remains gated exactly as ADR-009
and Stage-9 require.

Applied to Volunteer Operations, this ADR:

1. **Refines D-VO1** from "author nothing" to "author Tier 1 now; keep Tier 2
   gated." D-VO1's methodology-§1 basis is satisfied because this is
   **foundational authoring of a placeholder domain**, a distinct activity from
   a *migration* (which §1 governs) — there is no prior content to re-serialize
   precisely because the domain was always intended to author its foundation on
   activation; this ADR moves the *foundational* slice of that authoring ahead of
   the *operational* trigger, and nothing more.
2. **Refines D-VO3** ("defer skills/certifications/languages to activation").
   The *top-level, universally-recognized categories* are authored now as
   extensible schemes; the *organization-specific decomposition* D-VO3 rightly
   protects (a specific skill catalogue, proficiency scoring, which skills map to
   which tasks) remains deferred to operations staff. Authoring the invariant
   category layer does not pre-commit the operational decomposition.
3. **Introduces a maturity state:** *Canonical (Foundational) — Operational
   Deferred*. It sits between ADR-004's `level_2_placeholder` and a fully active
   domain: the foundational ontology/taxonomy is canonical and single-owned; the
   operational layer is explicitly, governably absent.
4. **Preserves every boundary already ratified** (VO-6 / FLAG-006, ADR-008,
   ADR-018): the foundation attaches *behind* `shared:actor` via a reference
   relationship and never mints a second actor, never redefines the `volunteer`
   role label, and never authors the assignment *act* (owned by
   `verification-operations` / `case-management`).

## Scope Test (the rule a foundational concept must pass to be authored now)

A concept is Tier 1 (author now) **only if all** hold; if any fails it is Tier 2
(defer):

1. **Organization-invariant** — it is present in essentially every humanitarian
   volunteer-management system, not a product of one organization's process.
2. **No process/policy/algorithm** — it is a *what-exists* fact (a volunteer, a
   skill category, a proficiency band), not a *how-we-operate* rule (a schedule,
   a dispatch order, an optimization, a scoring formula).
3. **No runtime/instance finding** — it is stable domain structure, not a
   reasoning-produced score/flag/history (those are `Canonical_Ontology_Schema.md`
   §19 territory, deferred to the Runtime/Instance-State Schema).
4. **Owns, does not duplicate** — it is single-owned by Volunteer Operations
   (ADR-008); anything already owned by Shared or an active domain is referenced,
   never redefined.

## Alternatives Considered

- **Keep D-VO1 as-is (author nothing until Stage 9):** rejected. It leaves
  FLAG-006's deferrals pointing at an empty domain and treats invariant
  vocabulary (which needs no operational input) as if it needed operational
  input. It over-applies a *migration* rule to *foundational authoring*.
- **Author the whole domain now, including scheduling/dispatch/scoring:**
  rejected. That is exactly the premature-invention ADR-009 forbids and the task
  charter forbids — organization-specific process the knowledge layer must not
  invent.
- **Author the foundation but mint a new `volunteer` actor entity:** rejected —
  duplicates `shared:actor` and violates ADR-008 / ADR-018 / FLAG-006. The
  foundation references the shared actor.
- **Promote the whole VO vocabulary straight to `shared/`:** rejected. Only a
  concept used by two or more domains is promoted (`Canonical_Ontology_Schema.md`
  §11). These are single-owned by Volunteer Operations today; promotion (e.g. of
  a language vocabulary) happens under existing governance when a second domain
  needs it, and is flagged, not pre-emptively done.

## Consequences

- Volunteer Operations reaches **Canonical (Foundational) — Operational
  Deferred**: a settled, single-owned foundational surface, with the operational
  layer still gated by the Stage-9 trigger.
- `ontology_authority_matrix.md` gains a Volunteer Operations owned-concepts
  section (the matrix's own rule requires ownership be declared *at the time a
  concept is written* — now satisfied). FLAG-006 moves from "recorded, awaits
  activation" to "foundational side authored; assignment-act boundary held."
- The Stage-9 trigger is **narrowed** from "author the domain" to "author the
  operational layer": scheduling, dispatch, workload, optimization,
  trust/performance scoring, the assignment-history record, and any org-specific
  skill/certification decomposition.
- This ADR generalizes: any placeholder domain with a genuinely
  organization-invariant foundation (e.g. a future Organisations domain) may
  apply the same two-tier rule rather than deferring its whole self.

## Governance Impact

- `Repository_Migration_Methodology.md` is unaffected: it governs *migrations*;
  this ADR governs *foundational authoring*, a separately-named activity. No
  methodology text is altered.
- `Canonical_Ontology_Schema.md` / `Canonical_Taxonomy_Schema.md` are unaffected
  — this ADR authors *conformant content against them*, it does not amend them.
  §19's runtime/reasoning boundary is honored (no findings/scores authored).
- ADR-004 and ADR-009 stand; this ADR refines *how* a placeholder transitions —
  a foundational tier may precede the operational tier — without permitting
  operational invention.

## Repository Impact

- **Created:** `volunteer-operations/ontology/{entities,data-properties,relationships,semantic-constraints,lifecycle-constraints}.yaml`;
  `volunteer-operations/taxonomy/*.yaml` (9 files);
  `volunteer-operations/governance.md`; `volunteer-operations/discovery/foundation-report.md`.
- **Modified:** `volunteer-operations/README.md`, `volunteer-operations/_placeholder.yaml`
  (retained in ADR-004 shape per D-VO2; `status` and `do_not_implement_until`
  reworded to scope the deferral to the operational layer),
  `ontology_authority_matrix.md` (VO section + FLAG-006 update),
  `knowledge_layer_roadmap.md` (Stage-9 narrowed), `architecture-decisions/README.md`.
- **No already-active domain YAML is modified.** The foundation references shared
  and active-domain concepts; it redefines none.

## Future Work

- On the Stage-9 operational trigger: author Tier 2 (scheduling, dispatch,
  workload, trust/performance, assignment history) against operations-staff
  input, and the Runtime/Instance-State Schema (ADR-023 §19) for any
  reasoning-produced volunteer findings/scores.
- Resolve the cross-domain coverage link (`volunteer_profile` →
  `community-context:geographic_area`) at the repository-wide manifest / C-2
  CURIE phase, alongside Registration's and Community Context's parked Phase 5.
- Revisit promotion of the VO-local `language`/`language_proficiency` vocabulary
  to `shared/` if and when a second domain needs it (existing §11 governance).

## Related Documents
- `docs/architecture/Volunteer_Operations_Domain_Audit.md` (VO-6, §3–§7)
- `docs/architecture/Volunteer_Operations_Migration_Plan.md` (D-VO1, D-VO3, D-VO5)
- ADR-004, ADR-008, ADR-009, ADR-018, ADR-023
- `ontology_authority_matrix.md` (FLAG-006)
