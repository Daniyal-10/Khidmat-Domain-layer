# Khidmat Knowledge Layer — Ontology Authority Matrix

**Authority:** Knowledge Layer Architect
**Governing ADR:** ADR-008: Single Ownership of Concepts
**Purpose:** Declares the authoritative owner for every concept in the
knowledge layer. This is the governance record of concept ownership.

---

## How to Use This Matrix

**Defining vs. referencing:**
A concept may be referenced by many files but may only be defined by one
owner. The owner file is listed in the `Authoritative File` column. All
other files that use the concept must reference it — they must not
redefine it.

**Adding a new concept:**
When a new concept is introduced to the knowledge layer, its owner must be
declared in this matrix before or at the time the concept is written.
No concept may be used in a reasoning rule if its ownership is undeclared.

**Changing ownership:**
If a concept is promoted from a domain file to shared ownership, the
`Authoritative File` and `Owner Domain` columns must be updated. The
change must be accompanied by a new ADR if it affects an established
design decision.

**Flagged boundary cases:**
Concepts with known overlap risks or pending alignment requirements are
listed separately in the Flagged Boundary Cases section at the end of
this file.

---

## Shared Human Model

### Lifecycle Stage Concepts

**Authoritative file:** `shared/human-model/lifecycle-stages.yaml`
**Owner domain:** Shared Human Model
**Introduced:** Phase 2.0
**Governing ADRs:** ADR-007, ADR-008

| Concept ID | Concept Name | Authoritative File | Owner Domain | Reference Constraint |
|---|---|---|---|---|
| `infant` | Infant | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `toddler` | Toddler | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `early_childhood` | Early Childhood | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `school_age_child` | School-Age Child | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `adolescent` | Adolescent | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `young_adult` | Young Adult | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `adult` | Adult | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `older_adult` | Older Adult | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |
| `elderly` | Elderly | `shared/human-model/lifecycle-stages.yaml` | Shared Human Model | May be referenced by any domain; must not be redefined elsewhere |

**What these concepts cover:**
Each lifecycle stage concept owns its complete definition including:
stage boundaries, characteristic dependencies, characteristic capabilities,
characteristic vulnerabilities, reasoning implications, and ontology notes.

**What these concepts do not cover:**
Risk factors associated with each stage are not owned here. Vulnerability
scoring, intervention recommendations, and outcome indicators associated
with stages are not owned here. These belong to the Risk Domain (Stage 3),
Case Management (Stage 5), and Outcome Measurement (Stage 6) respectively.

---

## Flagged Boundary Cases

The following are known areas where concept ownership requires future
alignment. They are not current conflicts but are recorded here so that
future domain designers do not create silent drift.

### FLAG-001: functional_capacity and capabilities.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/taxonomy/persons.yaml` |
| Concept | `functional_capacity` (enum: full, partial, dependent) |
| Situation | This is a proto-capability concept declared before the Shared Human Model existed. It functions as a placeholder for a capability model. |
| Risk | When `capabilities.yaml` is created in Phase 2.0, `functional_capacity` in persons.yaml must reference that file as its authority rather than defining its own capability vocabulary. |
| Resolution required | When `capabilities.yaml` is complete, update `shared/taxonomy/persons.yaml` to reference it. No silent modification — record in DECISIONS.md if the change is architectural. |
| Status | Pending `capabilities.yaml` creation |

### FLAG-002: Dependency type names and dependency.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/lifecycle-stages.yaml` |
| Concept | Dependency type labels (physiological, developmental, medical, safety, nutritional, protective, educational, situational, health, economic, physical, social, legal) |
| Situation | These type labels appear in `characteristic_dependencies` entries throughout lifecycle-stages.yaml. They are descriptive, not definitional — they describe the nature of each stage's dependencies without formally owning the dependency type vocabulary. |
| Risk | When `dependency.yaml` is created, it will formally own the dependency type taxonomy. The labels used in lifecycle-stages.yaml must align with that taxonomy. |
| Resolution required | When `dependency.yaml` is complete, verify that all dependency type labels in lifecycle-stages.yaml are consistent with the authoritative vocabulary. Update lifecycle-stages.yaml if any labels require standardisation. |
| Status | Pending `dependency.yaml` creation |

### FLAG-003: Health condition references and health-conditions.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/lifecycle-stages.yaml` |
| Concept | Health condition labels used descriptively (SAM, MAM, chronic illness, cognitive decline, frailty, polypharmacy) |
| Situation | These appear in `characteristic_vulnerabilities` entries as descriptive references. They are not defined here — they are named as examples of vulnerabilities characteristic to each stage. |
| Risk | When `health-conditions.yaml` is created, it will own the authoritative vocabulary for these conditions. The descriptive references in lifecycle-stages.yaml should remain consistent with that vocabulary. |
| Resolution required | When `health-conditions.yaml` is complete, verify descriptive references in lifecycle-stages.yaml align with authoritative terminology. |
| Status | Pending `health-conditions.yaml` creation |

### FLAG-004: Capability profile descriptions and capabilities.yaml

| Item | Detail |
|---|---|
| Existing location | `shared/human-model/lifecycle-stages.yaml` |
| Concept | Capability descriptions in `characteristic_capabilities` entries (e.g., independent mobility, emergent language, literacy, full economic productive capacity) |
| Situation | These are descriptive profiles of what each stage can do. They anticipate the capability vocabulary that `capabilities.yaml` will formally define. |
| Risk | When `capabilities.yaml` is created, the capability vocabulary it establishes must be consistent with the capability descriptions already recorded in lifecycle-stages.yaml. |
| Resolution required | When `capabilities.yaml` is complete, cross-check capability vocabulary against lifecycle-stages.yaml descriptive entries. Align terminology. |
| Status | Pending `capabilities.yaml` creation |
