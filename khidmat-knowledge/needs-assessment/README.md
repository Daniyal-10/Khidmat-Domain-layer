# Needs Assessment Domain

## Purpose

A synthesis layer: turns registration claims and verification findings into
`IdentifiedNeed`s with explicit, structured confidence — decoupled from case
orchestration so that "what does this person need, and how confident are we"
is answered independently of "what are we doing about it."

## Scope

Assessment events, the findings they produce, and the needs synthesized from
those findings. Covers assessment depth, urgency, scope, status, methodology, and
finding confidence.

## Owns

- **Taxonomy:** `assessment_depth`, `assessment_urgency`, `assessment_scope`,
  `assessment_status`, `assessment_methodology`, `finding_confidence`,
  `need_severity` (`taxonomy.yaml`)
- **Entities:** `Assessment`, `AssessmentFinding`, `IdentifiedNeed`
  (`ontology.yaml`)
- **Relationships:** `assesses`, `produces`, `belongs_to`, `synthesizes_into`,
  `synthesized_from`, `based_on_claim`, `based_on_verified_fact`, `affects`,
  `superseded_by`

## Does Not Own

- `Subject`, `HumanitarianSector`, `AssessmentTool` — referenced from the Shared
  domain, not redefined here.
- `RegistrationClaim` — referenced from `registration/`.
- `VerificationFinding` — referenced from `verification-operations/`.
- Case orchestration or intervention selection (owned by `case-management/`).

## Directory Structure

```
needs-assessment/
├── taxonomy.yaml                              # assessment_depth, urgency, scope, ...
├── ontology.yaml                              # Assessment, AssessmentFinding, IdentifiedNeed
├── needs_assessment_discovery_report.md       # boundary/architecture discovery
├── needs_assessment_taxonomy_review.md        # taxonomy validation
└── needs_assessment_ontology_review.md        # ontology validation
```

## Related Documents

- `ARCHITECTURE.md` — Stage 4.5 in the domain activation sequence
- `knowledge_layer_roadmap.md` — prerequisites (Verification Operations) and what
  this domain enables downstream (Case Management, Support Delivery, Programs)
- `ontology_authority_matrix.md` — Needs Assessment concept ownership
- `GLOSSARY.md` — Outcome Terms section
