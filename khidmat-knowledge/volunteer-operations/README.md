# Volunteer Operations Domain

## Purpose

Governs the volunteer as a **persistent, qualified operational resource** — the
identity-of-capacity behind the `volunteer` role. Entirely separate from the
registration domain: a volunteer appears in registration only as a
`registrant_type`; their full profile lives here.

## Maturity: Canonical (Foundational) — Operational Deferred

Authored in two tiers under **ADR-024**:

- **Tier 1 — Foundational (authored):** the organization-invariant ontology and
  taxonomy. Present now as a canonical, single-owned foundation.
- **Tier 2 — Operational / runtime (deferred):** scheduling, dispatch, routing,
  workload balancing, optimization, trust/performance scoring, the assignment
  ACT, per-instance assignment/training history, and organization-specific
  decomposition of the foundational vocabularies. Gated by the Stage-9 activation
  trigger (a volunteer management workflow defined with operations staff).

See `discovery/foundation-report.md` for the full design summary and
`governance.md` for the boundary rules.

## Owns (foundational)

**Entities**
- `volunteer_profile` — the qualification/capacity record attached behind
  `shared:actor`.
- `volunteer_team` — a structural grouping of volunteer profiles.

**Foundational vocabularies (taxonomy)**
- `volunteer_status`, `volunteer_type` — `taxonomy/volunteer-classification.yaml`
- `skill_category` — `taxonomy/skills.yaml`
- `certification_type` — `taxonomy/certifications.yaml`
- `availability_type` — `taxonomy/availability.yaml`
- `assignment_type` (eligibility) — `taxonomy/assignment-types.yaml`
- `coverage_type` — `taxonomy/coverage.yaml`
- `language_proficiency` — `taxonomy/languages.yaml`
- `affiliation_type` — `taxonomy/affiliation.yaml`
- `training_status` — `taxonomy/training.yaml`

## Does Not Own

- The `volunteer` **role label** — owned by `shared/taxonomy/persons.yaml`. This
  domain owns the full profile behind that role, not the label.
- The `Actor` **entity** — owned by `shared/ontology/entities.yaml`. This domain
  attaches the profile *behind* that reference (`profile_of`), never redefining
  the actor.
- The **assignment act** — issuing a `VerificationAssignment`
  (`verification-operations`) or a `CaseAssignment` (`case-management`). This
  domain owns *who is fit to be assigned* (eligibility, skills, availability,
  coverage), never *the assignment event itself*. Stated from the verification
  side in `verification-operations/ontology/relationships.yaml` and recorded
  reciprocally as `FLAG-006` in `ontology_authority_matrix.md`.
- The **organisation** vocabulary — owned by `shared/taxonomy/organisations.yaml`;
  referenced via `affiliated_with`.
- **Operational / runtime behavior** (Tier 2): scheduling, dispatch, workload,
  optimization, trust/performance scoring, assignment/training history — deferred.
- Anything in registration, verification, or case management.

## Directory Structure

```
volunteer-operations/
├── _placeholder.yaml            # ADR-004 scope declaration (retained; operational tier deferred)
├── README.md                    # this file
├── governance.md                # boundary rules, tier split, flagged cases
├── ontology/
│   ├── entities.yaml
│   ├── data-properties.yaml
│   ├── relationships.yaml
│   ├── semantic-constraints.yaml
│   └── lifecycle-constraints.yaml
├── taxonomy/
│   ├── volunteer-classification.yaml
│   ├── skills.yaml
│   ├── certifications.yaml
│   ├── availability.yaml
│   ├── assignment-types.yaml
│   ├── coverage.yaml
│   ├── languages.yaml
│   ├── affiliation.yaml
│   └── training.yaml
└── discovery/
    └── foundation-report.md     # Phase 2 foundation design report
```

## Related Documents

- `discovery/foundation-report.md` — foundation design summary, decisions, validation
- `governance.md` — boundary enforcement and flagged boundary cases
- `docs/architecture/Volunteer_Operations_Domain_Audit.md` — discovery audit (VO-6)
- `docs/architecture/Volunteer_Operations_Migration_Plan.md` — decisions D-VO1…D-VO5
- `architecture-decisions/ADR-024` — Foundational Layer Precedes Operational Activation
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy
- `architecture-decisions/ADR-008` — Single Ownership of Concepts
- `ontology_authority_matrix.md` — FLAG-006 and the VO owned-concepts section
- `knowledge_layer_roadmap.md` — Stage 9 (operational activation trigger)
