# Verification Operations Domain

## Purpose

Produces verification knowledge — confirming or refuting claims made during
registration — from field activities performed against registration outputs.
Turns "the registrant said X" into "X was confirmed / not confirmed / requires
re-verification."

## Scope

Everything from the moment a Verification Brief is issued to a volunteer through
to a recorded verification finding: assignment, field visit, observation,
confidence composition, contradiction detection, escalation, and re-verification
triggers. It does not decide what happens as a result of a finding (that is Case
Management's concern).

## Owns

- **Entities:** `verification_subject`, `verification_activity`,
  `field_observation`, `verification_finding`, `reverification_trigger`,
  `human_review`, `verification_assignment` (`ontology/entities.yaml`)
- **Data Properties:** scalar/coded properties for each entity above
  (`ontology/data-properties.yaml`)
- **Relationships:** structural relationships between the entities above,
  and semantic references to Registration, Case Management, Shared
  Ontology, Shared Risk, and Shared Time (`ontology/relationships.yaml`)
- **Constraints:** conditional-requirement structural facts
  (`ontology/semantic-constraints.yaml`) and descriptive lifecycle
  semantics (`ontology/lifecycle-constraints.yaml`)
- **Taxonomy:** escalation reasons, reverification triggers, review decisions,
  verification confidence, verification findings, verification methods,
  verification status (`taxonomy/`)
- **Reasoning:** verification rules, confidence composition, contradiction
  detection, escalation rules, reverification rules, completeness/sufficiency
  rules (`reasoning/`)

## Does Not Own

- The claims being verified, or the case they belong to (owned by
  `registration/`).
- What a confirmed/refuted finding means for case progression (owned by
  `case-management/`).
- Synthesis of verified facts into identified needs (owned by
  `needs-assessment/`, which explicitly references `VerificationFinding` from
  this domain rather than redefining it).

## Directory Structure

```
verification-operations/
├── ontology/
│   ├── entities.yaml
│   ├── data-properties.yaml
│   ├── relationships.yaml
│   ├── semantic-constraints.yaml
│   └── lifecycle-constraints.yaml
├── taxonomy/
│   ├── escalation-reasons.yaml
│   ├── reverification-triggers.yaml
│   ├── review-decisions.yaml
│   ├── verification-confidence.yaml
│   ├── verification-findings.yaml
│   ├── verification-methods.yaml
│   └── verification-status.yaml
└── reasoning/
    ├── verification-rules.yaml
    ├── confidence-composition-rules.yaml
    ├── contradiction-detection-rules.yaml
    ├── escalation-rules.yaml
    ├── reverification-rules.yaml
    └── completeness-and-sufficiency-rules.yaml
```

## Related Documents

- `ARCHITECTURE.md` — domain inventory and dependency rules
- `knowledge_layer_roadmap.md` — Stage 4 (this domain's activation stage)
- `ontology_authority_matrix.md` — Verification Operations concept ownership
- `GLOSSARY.md` — Verification Operations Terms section
- `registration/verification/` — the Verification Brief projection this domain
  consumes
