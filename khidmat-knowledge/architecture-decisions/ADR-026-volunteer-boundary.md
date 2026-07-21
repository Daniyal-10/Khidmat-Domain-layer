# ADR-026

## Title
Volunteer Boundary (Donor & Resource / Volunteer Operations)

## Status
Accepted

## Date
2026-07-17 (drafted HKMP Stage 8A; ratified and integrated HKMP Stage 8D)

## Context
The original Stage 8 brief listed volunteers, volunteer resources, capability, skills, availability,
assignment, capacity, specialization, certification, and deployment as in-scope for the Donor &
Resource domain. Every one of these is already owned, at foundational tier, by Volunteer Operations
(`ontology_authority_matrix.md`, Volunteer Operations Domain section), governed by FLAG-006 and
ADR-024.

## What Donor & Resource Owns
Nothing volunteer-related. No volunteer entity, taxonomy, relationship, or data property of any
kind, in either the Stage 8B (Donor & Funding) or Stage 8C (Material Resource & Logistics)
implementation.

## What Volunteer Operations Owns (Unchanged)
`volunteer_profile`, `volunteer_team`, `volunteer_status`, `volunteer_type`, `skill_category`,
`certification_type`, `availability_type`, `assignment_type` (eligibility only, per FLAG-006),
`coverage_type`, `language_proficiency`, `affiliation_type`, `training_status` — all foundational
tier (ADR-024 Tier 1). The operational layer (scheduling, dispatch, workload, trust/performance
scoring, the assignment act, assignment/training history) remains Volunteer Operations' Tier 2,
gated behind its own Stage-9 activation trigger, and is **not** reachable or ownable by Donor &
Resource at any point without a separate governance action on Volunteer Operations itself.

## Every Overlapping Concept Named in the Original Brief, and Why It Stays With Volunteer Operations
| Brief term | Owned by | Why it does not move |
|---|---|---|
| Volunteers | Volunteer Operations (`volunteer_profile`) | Attaches behind `shared:actor`; Donor & Resource has no actor-qualification concern |
| Volunteer resources | Volunteer Operations (`volunteer_profile`/`volunteer_team`) | "Resource" in the brief's sense here means *personnel*, a qualification concept, not a Donor & Resource material/financial resource |
| Volunteer capability | Volunteer Operations (`skill_category`, `capabilities.yaml` via Shared Human Model) | Capability is explicitly Shared Human Model + Volunteer Operations territory (FLAG-004 resolved this boundary already) |
| Volunteer skills | Volunteer Operations (`skill_category`) | Foundational tier, already authored |
| Volunteer availability | Volunteer Operations (`availability_type`) | Foundational tier, already authored |
| Volunteer assignment | Verification Operations (act) / Case Management (act) / Volunteer Operations (eligibility) | FLAG-006 already resolved this three-way split; Donor & Resource was never a party to it |
| Volunteer capacity | Volunteer Operations (Tier 2, deferred) | Capacity-as-workload is explicitly Tier 2 (ADR-024), not authorable by anyone yet, least of all a new domain |
| Volunteer specialization | Volunteer Operations (`skill_category`) | Same concept as skills, different word |
| Volunteer certification | Volunteer Operations (`certification_type`) | Foundational tier, already authored |
| Volunteer deployment | Volunteer Operations (Tier 2, deferred) / Case Management, Verification Operations (assignment act) | Deployment is the assignment act or its scheduling — never a Donor & Resource concern |

## Why Ownership Belongs Where It Does
Every one of these concepts is either (a) already canonically authored by Volunteer Operations at
foundational tier, making any Donor & Resource version a direct ADR-008 duplication, or (b)
explicitly deferred to Volunteer Operations' own Tier 2 / Stage-9 trigger, making any Donor &
Resource authoring of it a premature-invention violation of ADR-009 by a domain that isn't even the
one holding the deferral. Donor & Resource has no claim to either category. The only legitimate
touchpoint is a **downstream reference** — a `contribution` or `grant` may one day note that
volunteer labor was part of what a donor funded, but that reference would point *at*
`volunteer_profile`/`volunteer_team`, never redefine them.

## Decision
Donor & Resource authors **zero** volunteer-related content, at both Stage 8B and Stage 8C. Any
future donor-facing "contributed labor" reporting requirement is handled as a narrow,
explicitly-gated Phase 2 addition, reviewed on its own merits against this exact boundary table at
the time it is proposed — not folded into any Stage 8 sub-stage.

## Consequences
- **Positive:** Zero ADR-008 risk from Donor & Resource's implementation.
- **Positive:** This table is the canonical answer the next auditor needs, closing the ambiguity
  the original brief's volunteer section would otherwise have left open.
- **Constraint:** Any future "contributed labor" work must re-run this exact analysis, not assume
  the boundary is settled permanently — Volunteer Operations' own Tier 2 activation could change
  what's available to reference.

## Implementation Status
Fully implemented (as an absence): confirmed by explicit self-audit — no
volunteer-related concept appears anywhere in `donor-resource/`. Recorded as `donor-resource/governance.md`
Rule 3 and DR-FLAG-B.

## Related Documents
- `ontology_authority_matrix.md` (Volunteer Operations Domain section, FLAG-006), ADR-024,
  ADR-008, ADR-009
