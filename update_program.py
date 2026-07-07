import re
import os

filepath = r'D:\CODINGGGGGGG\AI Research\PROJECTTTTSSSSS\Khidmat Domain layer\khidmat-knowledge\docs\architecture\Repository_Architecture_Improvement_Program.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

dashboard_and_more = """# Repository Architecture Improvement Program

## Executive Dashboard

| Metric | Status / Value |
|--------|----------------|
| **Repository Health** | ⚠️ Needs Remediation |
| **Current Architecture Status** | Conceptually strong, mechanically inconsistent |
| **Current Implementation Phase** | Phase 1 (Critical) |
| **Critical Findings Remaining** | 3 |
| **Required Findings Remaining** | 4 |
| **Design Findings Remaining** | 7 |
| **Future Recommendations Remaining** | 5 |
| **Domains Completed** | 0 |
| **Domains Remaining** | 12 |
| **OWL Readiness** | ❌ Blocked |
| **RDF Readiness** | ❌ Blocked |
| **SHACL Readiness** | ❌ Blocked |
| **Knowledge Graph Readiness** | ❌ Blocked |
| **Current Milestone** | Baseline Establishment |
| **Next Milestone** | Repository v1.0 |
| **Overall Repository Status** | 🚧 In Progress |

## Progress Tracking

### Overall Completion
- **Total Progress:** 0% [□□□□□□□□□□]
- **Findings Resolved:** 0 / 19

### Per-Phase Completion
- **Phase 1 (Critical):** 0% [□□□□□□□□□□] (0/3)
- **Phase 2 (Required):** 0% [□□□□□□□□□□] (0/4)
- **Phase 3 (Design):** 0% [□□□□□□□□□□] (0/7)
- **Phase 4 (Future):** 0% [□□□□□□□□□□] (0/5)

## Purpose
"""

after_target_vision = """## Success Metrics
- **Parser Success Rate:** 100% single-code-path parsing.
- **Broken References:** 0 across all domains.
- **Schema Compliance:** 100% of YAML files passing meta-schema validation.
- **OWL Readiness:** 100% of domains exporting OWL.
- **SHACL Readiness:** 100% of domains exporting SHACL.
- **Namespace Consistency:** 100% CURIE alignment.
- **IRI Coverage:** 100% stable IRIs for all entities.
- **Automation Coverage:** 100% CI automated execution.
- **Cross-Domain Validation:** 100% DAG acyclic rule compliance via tooling.
- **Repository Health Score:** 10/10.

## Implementation Principles
"""

before_repo_standards = """## Migration Order
An official sequence ensures dependent domains are migrated only after their foundational dependencies are stable.

1. **Shared Human / Shared Risk:** Foundational base models. Must be standardized first.
2. **Community Context:** The flagship template. Refinements here propagate outwards.
3. **Registration:** Relies on Shared concepts.
4. **Needs Assessment / Case Management:** Legacy domains requiring heavy refactoring, built on foundational data.
5. **Beneficiary Lifecycle / Verification Operations:** Operational domains spanning multiple lower-level contexts.
6. **Consent & Privacy:** Cross-cutting domain, best stabilized last once entity IRIs are firm across all subjects.
7. **Programs / Support Delivery / Volunteer Operations:** Upper ontologies and operations that depend on the rest of the stack.

## Architecture Freeze Gates
Work proceeds through explicit gates to prevent regression:
- **Design Complete:** Concept is drafted and reviewed.
- **Architecture Approved:** ADR is signed off, schema is published.
- **Implementation Complete:** Domain YAML files updated.
- **Verification Passed:** CI passes against the new schema.
- **Repository Freeze:** Standard becomes immutable for the current release.
- **Release Ready:** Automation pipelines confirm artifacts are generated successfully.

## CI / Validation Roadmap
Future automated validations (to be implemented incrementally):
- **Schema Validation:** JSON Schema/meta-SHACL enforcing YAML structure.
- **Reference Integrity:** Ensure no dangling `attributes_ref` or file references.
- **Namespace Validation:** Enforce CURIE structure globally.
- **IRI Validation:** Ensure stable IRI minting rules are respected.
- **OWL Generation:** CI test for deterministic OWL output.
- **SHACL Validation:** CI test for deterministic SHACL output.
- **Cross-Domain Imports:** Validating cross-domain references.
- **Ontology DAG Validation:** Ensure no cyclic dependencies across domains.
- **Broken Links:** Generic check for file references.
- **Markdown Links:** Governance documentation link checks.
- **Directory Structure:** Folder layout compliance (`ontology/`, `reasoning/`, `discovery/`).
- **Repository Standards:** Validation of headers, metadata, and versioning.

## Release Roadmap
- **Repository v1.0:** Schema & IRI Freeze (Resolves Phase 1 & 2).
- **Repository v1.1:** Template unifications and CI validations (Resolves Phase 3).
- **Repository v1.2:** Migration of all legacy domains to new schemas.
- **Repository v2.0:** Physical RDF/OWL/SHACL artifact generation pipelines (Resolves Phase 4).

## Wave-based Execution Plan
- **Wave 1: Repository Foundation** (C-1, C-2, C-3) - Establishing the identity and entity schemas.
- **Wave 2: Semantic Infrastructure** (R-1, R-2) - Manifests and mapping foundations.
- **Wave 3: Repository Standardization** (R-3, R-4, D-1, D-2, D-3, D-4, D-5, D-6, D-7) - Clean up of taxonomy, metadata, and folders.
- **Wave 4: Automation** (F-2) - Meta-validation to enforce the standards.
- **Wave 5: Generator Pipeline** (F-3, F-4, F-5) - Generating OWL/SHACL/RDF and versioning.
- **Wave 6: Enterprise Release** (F-1) - Moving legacy domains onto the completed pipeline.

## Decision Log
| Decision ID | Description | Status | ADR References | Reason | Dependencies | Date | Owner | Verification |
|-------------|-------------|--------|----------------|--------|--------------|------|-------|--------------|
| DEC-001 | Base schema adoption | Proposed | TBD | Resolves C-1 | None | TBD | Architect | CI Schema Check |

## Repository-wide Standards
"""

text = text.replace("# Repository Architecture Improvement Program\n\n## Purpose\n", dashboard_and_more)
text = text.replace("## Implementation Principles\n", after_target_vision)
text = text.replace("## Repository-wide Standards\n", before_repo_standards)

def finding_replacement(match):
    finding_text = match.group(0)
    domain_injection = """- **Affected Domains:**
  - [ ] Registration
  - [ ] Verification Operations
  - [ ] Community Context
  - [ ] Shared Human
  - [ ] Risk
  - [ ] Needs Assessment
  - [ ] Case Management
  - [ ] Programs
  - [ ] Support Delivery
  - [ ] Volunteer Operations
  - [ ] Consent & Privacy
  - [ ] Beneficiary Lifecycle
- **Risk Assessment:**
  - Breaking Change: Yes
  - Safe Refactor: No
  - Migration Risk: High
  - Implementation Risk: High
  - Verification Risk: Medium
  - Repository Risk: High
  - Overall Risk: High
  - Mitigation Strategy: Validate thoroughly before committing.
- **Finding Completion:** 0% [□□□□□□□□□□]"""
    finding_text = re.sub(r'- \*\*Status:\*\* [^\n]+', domain_injection, finding_text)
    
    finding_text = finding_text.replace('- [ ] Migration completed', '- [ ] Implementation Complete')
    finding_text = finding_text.replace('- [ ] Verification passed', '- [ ] Verification Passed')
    finding_text = finding_text.replace('- [ ] Frozen', '- [ ] Repository Freeze\n  - [ ] Release Ready')
    finding_text = finding_text.replace('Design completed', 'Design Complete')
    finding_text = finding_text.replace('Architecture approved', 'Architecture Approved')
    
    return finding_text

phases_part_match = re.search(r'(### Phase 1: Critical Findings.*?)(?=\n## Checklist)', text, flags=re.DOTALL)
if phases_part_match:
    phases_part = phases_part_match.group(1)
    updated_phases = re.sub(r'(#### [CRDF]-\d[\s\S]+?)(?=\n#### |\n### Phase |\Z)', finding_replacement, phases_part)
    text = text.replace(phases_part, updated_phases)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
