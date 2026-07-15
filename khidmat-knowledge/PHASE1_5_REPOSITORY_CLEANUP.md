# Phase 1.5 — Canonical Repository Cleanup

**Basis:** the current on-disk repository, mechanically re-scanned from scratch — every YAML
file, every entity, relationship, constraint, taxonomy scheme, `taxonomy_ref`, and namespace
declaration. No prior audit's claims were trusted without re-derivation.

**Note on repository state:** as of this pass, the Phase 1.2–1.4 changes remain uncommitted in
the working tree (confirmed via `git status`), consistent with every prior phase in this
sequence — none of my own changes across this entire multi-phase effort have been committed by
me, since committing was never explicitly requested. This does not affect the mechanical
validation below, which evaluates the repository as it currently stands on disk.

---

## 1. Repository Cleanup Report

A full mechanical scan across 170 YAML files found the repository already in strong mechanical
condition, consistent with the ontology/ownership/taxonomy freezes certified in Phases 1.3B and
1.4: zero duplicate relationship IDs, zero duplicate constraint IDs, zero duplicate taxonomy
scheme IDs, zero broken `imports:`, and only the pre-existing, explicitly-governed exceptions
remaining unresolved (1 documented entity-ID duplicate, 3 documented deferred `taxonomy_ref`
values).

The one class of genuine, previously-undetected mechanical defect found was **unused namespace
aliases** — declarations left in a file's `namespaces:` block after the relationship(s) that
used them were retargeted or never existed in that file to begin with. A broad regex-based first
pass over-reported 22 candidates; individually verifying each against the file's actual content
(not just field-name pattern matching, since several files reference cross-domain concepts
through a `- scheme:` list style my first pass missed) narrowed this to 5 genuine cases and 1
deliberately-documented exception, detailed in §2.

A repository dependency-graph scan also surfaced one 3-domain reference cycle
(Case Management → Needs Assessment → Verification Operations → Case Management). This is
**not treated as a mechanical defect** and was not touched: it is composed of three legitimate,
independently-justified reference relationships (not an ownership or aggregate cycle), and
breaking it would require redirecting or removing one of those relationships — an ontology
change, explicitly out of scope for a repository-engineering pass. It is reported in §5 as a
finding for a future architecture decision, not corrected here.

---

## 2. Mechanical Issues Found and Fixed

| Issue | Location | Fix |
|---|---|---|
| Unused namespace alias `registration` | `beneficiary-lifecycle/ontology/relationships.yaml` | Removed. Orphaned by the Phase 1.3A retarget of this file's two case-referencing relationships from `registration:case` to `case_management:case`; nothing else in the file used it. |
| Unused namespace aliases `shared_org`, `shared_human` | `community-context/ontology/entities.yaml` | Removed. This file's own entities never declared a cross-domain `parent:`; the same aliases are correctly declared and used in this domain's own `relationships.yaml`. |
| Unused namespace aliases `shared_core`, `shared_org` | `volunteer-operations/ontology/entities.yaml` | Removed. Same reasoning as above. |
| Unused namespace alias `core` | `consent-and-privacy/ontology.yaml` | Removed. The file's entity id is bare (`consent`), never `core:consent`; no consumer ever used the `core:` prefix. |

## Mechanical Issues Found and Deliberately Not Fixed

| Item | Why not a defect |
|---|---|
| Unused namespace alias `shared_time` in `verification-operations/ontology/relationships.yaml` | The file's own `cross_domain_references` prose explicitly documents this as a deliberate reference-by-value pattern ("waiting_and_grace_periods is carried as the scheduled_window data property... not as a relationship"), not an oversight. Per the Special Rule, documented governance patterns are frozen. |
| Duplicate entity id `case` | Governed by ADR-021 and `ADR_RECONCILIATION_CASE.md`; certified as the correct, intentional frozen state in `PHASE1_3B_FINAL_OWNERSHIP_FREEZE_CERTIFICATION.md`. |
| 3 unresolved `taxonomy_ref` values (`outcome_indicator`, `functional_capacity`, `evidence_subtype`) | Certified as correctly deferred in `PHASE1_4_CANONICAL_TAXONOMY_COMPLETION.md` — Blueprint-scheduled or structurally blocked pending a taxonomy-design decision, not missing content a mechanical pass could safely add. |
| Empty `registration/taxonomy/support-interventions.yaml` | Blocked on programme-staff operational input per the file's own header; a standing, documented deferral, not a mechanical gap. |
| 3-domain reference cycle (Case Management ↔ Needs Assessment ↔ Verification Operations) | Composed of independently-justified reference edges, not an ownership cycle; resolving it requires an ontology decision, out of scope this phase. |

---

## 3. Files Modified

`beneficiary-lifecycle/ontology/relationships.yaml`, `community-context/ontology/entities.yaml`,
`volunteer-operations/ontology/entities.yaml`, `consent-and-privacy/ontology.yaml` — 4 files, all
namespace-block trims with an inline note explaining the removal. No entity, relationship,
constraint, or taxonomy content was altered in any of the four.

---

## 4. Validation Statistics

| Metric | Count |
|---|---|
| YAML files | 170 |
| Parse errors | 0 |
| Entities | 75 (74 unique IDs; 1 documented duplicate — `case`) |
| Relationships | 149 (149 unique IDs — 0 duplicates) |
| Constraints (semantic + lifecycle, combined) | 52 (52 unique IDs — 0 duplicates) |
| Taxonomy schemes | 210 (210 unique IDs — 0 duplicates) |
| Taxonomy concepts | 1032 |
| Namespace declarations (before this pass) | 63 |
| Namespace declarations (after this pass) | 57 (6 removed — 5 fixed + the `registration` alias was one of the 6 raw regex hits later confirmed genuinely unused, `shared_time` retained) |
| `taxonomy_ref` usages | 167 |
| Resolved references | 164 |
| Unresolved references | 3, all documented deferrals |
| `imports:` declarations | 2 (`registration/taxonomy/actors.yaml`, `registration/taxonomy/evidence.yaml`) — both targets confirmed to exist |
| Broken imports | 0 |
| Unused namespace aliases (after fix) | 0 undocumented; 1 documented and retained (`shared_time`) |
| Duplicate entity IDs | 1, documented and frozen |
| Duplicate relationship IDs | 0 |
| Duplicate constraint IDs | 0 |
| Duplicate taxonomy scheme IDs | 0 |
| Broken relationship targets | 0 (3 flagged by a coarse automated heuristic are confirmed-correct by direct substance-check — a bare single-word namespace convention the heuristic can't resolve into a nested subdirectory, not an actual broken reference; documented and unchanged since Phase 1.3B) |
| Repository DAG | Acyclic at the ownership/aggregate level; 1 reference-level cycle found among 3 domains (reported, not corrected — see §1, §5) |

---

## 5. Final Repository Validation

Every check in the validation scope was run to completion:

- ✅ Every YAML file parses.
- ✅ Every namespace alias that remains is used at least once, or is a documented exception.
- ✅ Every CURIE/namespace value was traced to a real file or a documented bare-word convention.
- ✅ Every `taxonomy_ref` resolves, except 3 documented deferrals.
- ✅ Every relationship target resolves by direct substance-check.
- ✅ Every entity id is unique, except 1 documented, ADR-governed exception.
- ✅ Every relationship id is unique.
- ✅ Every constraint id is unique.
- ✅ Both `imports:` declarations point at real files.
- ⚠️ The repository DAG is acyclic at the domain-ownership level; one 3-domain **reference**
  cycle exists (Case Management ↔ Needs Assessment ↔ Verification Operations). Not a mechanical
  defect — flagged for a future architecture review, not corrected here, since correction would
  require an ontology change.

---

## 6. Final Decision

# A.

## REPOSITORY CLEAN

The repository has reached canonical mechanical integrity within the scope of this phase. The
one open item (the reference-level DAG cycle) is a legitimate architecture question, not a
mechanical defect — it does not block "clean" under this phase's own validation scope, which
distinguishes mechanical issues from ontology-level questions and explicitly excludes the latter
from this phase's authority to correct.
