# Needs Assessment Domain

## Purpose

A synthesis layer: assessment sessions yield raw observations, which are
synthesized into need assertions with explicit, structured confidence —
decoupled from case orchestration so that "what does this person need, and
how confident are we" is answered independently of "what are we doing about
it." A governance layer (supervisor review, assessor calibration, finding
consensus, reassessment triggers) wraps this synthesis process to catch bias,
resolve disputes, and mandate reassessment.

## Scope

Assessment instruments and their indicators, assessment sessions, the
observations they yield, the need assertions synthesized from those
observations, and the quality-assurance processes governing all of the
above. Covers assessment depth, urgency, methodology, and modality; evidence
type, confidence, and conflict status; finding status, invalidation, and
need urgency; and review/calibration/consensus/trigger status and outcomes.

## Owns

- **Ontology** (`ontology/`): entities (`assessment_instrument`,
  `assessment_indicator`, `assessment_session`, `observation`,
  `need_assertion`, `finding_consensus`, `supervisor_review`,
  `assessor_calibration`, `reassessment_trigger`), their relationships —
  including `assertion_influences_assertion`, the synthesized-finding
  mirror of Registration's `need_influences_need` — data properties,
  lifecycle constraints, and semantic constraints.
- **Taxonomy** (`taxonomy/`):
  - `evidence.yaml` — `evidence_type`, `confidence_level`, `conflict_status`
  - `finding.yaml` — `finding_status`, `invalidation_reason`, `need_urgency`
  - `session.yaml` — `session_status`, `assessment_modality`,
    `missing_data_reason`, `assessment_depth`, `assessment_urgency`,
    `assessment_methodology`
  - `governance.yaml` — `review_status`, `rejection_reason`,
    `calibration_status`, `calibration_outcome`, `consensus_status`,
    `consensus_outcome`, `trigger_status`, `trigger_type`

## Does Not Own

- `person`, `household`, `actor`, `assessment_tool` — referenced from the
  Shared domain (`shared:`), not redefined here. `assessment_instrument`
  specializes `shared:assessment_tool` via `parent`.
- `geographic_area` — referenced from `community-context/`.
- `claim` — referenced from `registration/`.
- `verification_finding` — referenced from `verification-operations/`.
- Case orchestration or intervention selection (owned by `case-management/`).
- **Open item:** `humanitarian_sector` is reserved for this domain in
  `shared/ontology/entities.yaml` (see `ontology_authority_matrix.md`), but
  `thematic_sector` currently sources its vocabulary from
  `programs_tax:thematic_sectors` instead. Reassignment to the Shared
  placeholder is pending a Shared-promotion ADR and is not yet implemented
  — see `Needs_Assessment_Canonical_Migration_Plan.md` §10.1.

## Directory Structure

```
needs-assessment/
├── ontology/
│   ├── entities.yaml
│   ├── relationships.yaml
│   ├── data-properties.yaml
│   ├── lifecycle-constraints.yaml
│   └── semantic-constraints.yaml
├── taxonomy/
│   ├── evidence.yaml
│   ├── finding.yaml
│   ├── session.yaml
│   └── governance.yaml
├── ontology.yaml                              # legacy monolith — superseded, pending retirement
├── taxonomy.yaml                              # legacy monolith — superseded, pending retirement
├── Needs_Assessment_Canonical_Migration_Plan.md
└── Needs_Assessment_Canonical_Migration_Plan_VALIDATION_REPORT.md
```

No `reasoning/` directory exists for this domain yet.

## Related Documents

- `ARCHITECTURE.md` — Stage 4.5 in the domain activation sequence
- `knowledge_layer_roadmap.md` — prerequisites (Verification Operations) and what
  this domain enables downstream (Case Management, Support Delivery, Programs)
- `ontology_authority_matrix.md` — Needs Assessment concept ownership
- `Needs_Assessment_Canonical_Migration_Plan.md` — legacy-to-canonical mapping,
  architectural decisions (D1–D14), and open items
- `GLOSSARY.md` — Outcome Terms section
