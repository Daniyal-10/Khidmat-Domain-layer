# HKMP Stage 8D — Governance Integration & Repository Adoption Report

**Scope:** Governance integration only. No ontology was redesigned, and no
entity, taxonomy, or relationship was added beyond what Stage 8B/8C's
`PREPARED_GOVERNANCE_ADDITIONS.md` had already explicitly staged. This
report is the record of that integration, executed line-for-line against the
staged content.

**Authoritative source:** `donor-resource/PREPARED_GOVERNANCE_ADDITIONS.md`,
treated as the sole source of what to integrate, exactly as instructed. Every
edit below traces to a specific numbered item in that document.

---

## 1. ADRs Ratified

Four ADRs, drafted in full in `HKMP_STAGE8A_ARCHITECTURE_AND_GOVERNANCE.md`
Part 2 as ADR-DRAFT-025 through ADR-DRAFT-028, were ratified as:

| ADR | Title | File |
|---|---|---|
| ADR-025 | Donor Identity Model | `architecture-decisions/ADR-025-donor-identity-model.md` |
| ADR-026 | Volunteer Boundary (Donor & Resource / Volunteer Operations) | `architecture-decisions/ADR-026-volunteer-boundary.md` |
| ADR-027 | Grant Ownership | `architecture-decisions/ADR-027-grant-ownership.md` |
| ADR-028 | Resource Model | `architecture-decisions/ADR-028-resource-model.md` |

Each carries the original Context/Alternatives/Decision/Consequences content
from its draft, `Status: Accepted`, and a new "Implementation Status"
section pointing at the actual entities/relationships/taxonomies that realize
it. Two ADRs required a disclosed correction, not a redesign:

- **ADR-027** — its draft used the illustrative relationship name
  `program_funded_by_grant`, implying authorship on the Programs side. The
  as-built relationship, `grant_funds_program` (authored entirely within
  `donor-resource/ontology/relationships.yaml`, per the Stage 8B
  implementation report's own disclosed deviation), is now recorded as this
  ADR's actual, ratified decision. The *substance* of the decision (grant as
  an optional abstraction) is unchanged.
- **ADR-028** — its draft deferred the `consumable`/`equipment`/`asset`
  entity-vs-taxonomy-value question to "8B implementation" (a drafting-time
  slip — the resource entities are Stage 8C's, not 8B's). The ratified text
  corrects the stage reference and records the resolution Stage 8C's
  implementation actually reached (taxonomy values, not entities;
  `cold_chain_required` as the sole structural property difference found).

`architecture-decisions/README.md`'s index was extended with four new rows
(ADR-025 through ADR-028), matching the table's existing format exactly. No
existing index row was altered.

## 2. Authority Matrix Integration

`ontology_authority_matrix.md` gained a new **Donor & Resource Domain**
section, inserted after the existing Consent & Privacy Domain section and
before Flagged Boundary Cases — the same position new domain sections have
occupied in every prior stage's remediation. Copied verbatim from
`PREPARED_GOVERNANCE_ADDITIONS.md` §1, with two corrections applied during
integration:

- ADR references updated from `ADR-DRAFT-0NN` to the now-real `ADR-0NN`.
- `PREPARED_GOVERNANCE_ADDITIONS.md` §1 was itself extended in place during
  the Stage 8C implementation pass (not re-drafted from scratch) to add the
  six Stage 8C entity rows and four Stage 8C taxonomy-scheme rows alongside
  the original Stage 8B rows. This integration copied that already-combined
  §1 verbatim into the Authority Matrix — the original Stage 8B-only draft's
  now-superseded "Explicitly Not Owned (Stage 8C, deferred)" placeholder
  language does not appear in the integrated section at all, because §1 had
  already moved past it before this phase began.

No existing row in any other domain's section was modified.

## 3. Glossary Integration

`GLOSSARY.md` gained a new **Donor & Resource Terms** section, inserted
after the existing Volunteer Operations Terms section and before Governance
Terms — copied from `PREPARED_GOVERNANCE_ADDITIONS.md` §2, with the
**Resource** entry's cross-reference to **Recovery Resources** verified
against the live Glossary (confirmed present under Risk and Vulnerability
Terms) rather than assumed. This is the discipline
`HKMP_STAGE7C_CERTIFICATION_REVIEW.md` §4 found missing when a prior
remediation pass added a Glossary term without cross-referencing its
near-namesake — checked explicitly here to avoid repeating that exact
defect. No existing Glossary entry was modified.

## 4. Boundary Notes and the One Staged Relationship

All five items from `PREPARED_GOVERNANCE_ADDITIONS.md` §3 were integrated:

| § | Target file | What was added | Nature |
|---|---|---|---|
| 3.1 | `programs/taxonomy/funding-and-compliance.yaml` | `references:` block: `donor_resource:donor_type` `distinct_from` note | Documentation-only |
| 3.2 | `support-delivery/taxonomy/delivery-modalities.yaml` | Extended existing `references:` block with a third entry: `donor_resource:material_resource_category` `distinct_from` note | Documentation-only (extends a two-way note to three-way, as anticipated in Stage 8A Part 5) |
| 3.3 | `programs/ontology/entities.yaml` | `notes:` field added to `eligibility_rule` describing the optional `zakat_eligible_category` reference | Documentation-only |
| 3.4 | `support-delivery/ontology/relationships.yaml` | New row: `delivery_event_fulfilled_from_resource_allocation` (`from: delivery_event`, `to: donor_resource:resource_allocation`) | **The one relationship explicitly staged and now added** — authored on the Support Delivery side, per the "domain owning the `from` entity authors the edge" discipline used throughout `donor-resource/` |
| 3.5 | `support-delivery/ontology/entities.yaml` | `notes:` field added to `delivery_event` cross-referencing `resource_allocation` | Documentation-only |

A `donor_resource: donor_resource` namespace alias was added to both
`support-delivery/ontology/relationships.yaml` and
`support-delivery/taxonomy/delivery-modalities.yaml`'s `namespaces:` blocks —
required for the CURIE references above to resolve; not itself new ontology
content.

**This is the only new relationship row added anywhere in this phase**,
matching the rule "do NOT add new relationships except those explicitly
staged during Stage 8." No entity and no taxonomy scheme was added to any
file outside `donor-resource/` — every other change in this section is a
`notes:`/`references:` field, never a new `id:`.

## 5. Roadmap Entry

`knowledge_layer_roadmap.md` gained a new section, "HKMP Stage 8 — Donor &
Resource Domain (Distinct Numbering Track)," inserted after the existing
Stage 9 section and before Stage 10 — copied and lightly restructured from
`PREPARED_GOVERNANCE_ADDITIONS.md` §4 to additionally record 8D's own
completion (the draft only anticipated 8B/8C at the time it was written).
Explicitly disambiguates the "HKMP Stage 8" numbering from this document's
own pre-existing "Stage 8: Community Context" / "Stage 9: Activate Remaining
Placeholder Domains," per the discovery report's original finding. Neither
existing "Stage 8" nor "Stage 9" section text was altered.

## 6. `donor-resource/` Documentation Updated to Reflect Integration

Not governance files in the repository-wide sense, but the domain's own
documentation was brought into agreement with the now-integrated state
(otherwise it would itself become stale and inaccurate the moment this phase
completed):

- `README.md` — maturity statement updated to include Stage 8D; "Related
  Documents" and a new "Stage 8 Status" section replace the prior "Remaining
  Stage 8 Work" list (now empty); the Support Delivery boundary note updated
  from "future reference row" to the actual, now-authored row.
- `governance.md` — header ADR references updated from draft to ratified
  numbers; Rule 8 rewritten from "no modification to certified domains" (no
  longer accurate) to "modification is additive-only, and limited to Stage
  8D" with the five items enumerated; Rule 9's closing sentence updated from
  "not authored... not in this pass" to reflect the row now existing; the
  Flagged Boundary Cases heading updated from "staged for" to "integrated
  into."
- `PREPARED_GOVERNANCE_ADDITIONS.md` — status banner changed from "drafted
  for a future integration pass" to "INTEGRATED (HKMP Stage 8D)," explicitly
  naming every target file and stating the document is now a historical
  staging record, not a live source of truth.
- All `ADR-DRAFT-0NN` references across `donor-resource/*.yaml` and
  `donor-resource/*.md` were mechanically updated to `ADR-0NN`, matching the
  now-real ADR numbers. No other text in these files was altered by this
  substitution — verified by reviewing every match after the substitution
  ran, and by re-checking one line that was structurally ambiguous
  (`volunteer-operations/governance.md Rule 8`, which the substitution
  correctly did not touch because it wraps across two lines in the source
  and is a reference to a *different* domain's own Rule 8, not this one's).

## 7. Validation Results

| Check | Result |
|---|---|
| **No ontology redesign** | Confirmed. Zero entity, taxonomy, or relationship `id:` was changed in any file this phase touched, in `donor-resource/` or elsewhere. Every YAML edit outside `donor-resource/` added only a `notes:`/`references:` field or (in exactly one case, explicitly staged) a new relationship row. |
| **No new entities** | Confirmed — none added anywhere. |
| **No new taxonomies** | Confirmed — none added anywhere. |
| **No relationships beyond those staged** | Confirmed — exactly one new relationship row was added (`delivery_event_fulfilled_from_resource_allocation`), and it is the exact row staged in `PREPARED_GOVERNANCE_ADDITIONS.md` §3.4. |
| **YAML validity** | Every modified/created YAML file (`programs/taxonomy/funding-and-compliance.yaml`, `support-delivery/taxonomy/delivery-modalities.yaml`, `support-delivery/ontology/relationships.yaml`, `support-delivery/ontology/entities.yaml`, `programs/ontology/entities.yaml`, and all `donor-resource/` files) parsed successfully with a standard YAML loader after every edit. One structural mistake was caught and fixed during this pass: an initial edit to `funding-and-compliance.yaml` inserted a `references:` block in the middle of the `schemes:` list, which would have corrupted the file's structure; this was caught by re-reading the file, corrected by moving the block to the true end of the file, and re-validated. |
| **Single Ownership (ADR-008)** | Every concept added to `ontology_authority_matrix.md` for Donor & Resource is owned exclusively by `donor-resource/`; every reference added to another domain's file points outward by CURIE and redefines nothing. |
| **Repository boundary discipline** | `git status --porcelain`, checked before and after this phase: 9 existing files modified (all governance/documentation, listed in §2–§5 above), 4 new ADR files created, plus the pre-existing `donor-resource/` tree and prior stage reports left untouched in substance (only their cross-references to ADR numbers were mechanically updated, per §6). No file belonging to Case Management, Shared Ontology, Volunteer Operations, or Community Context was touched — this phase's staged additions only ever targeted Programs and Support Delivery. |
| **Glossary duplication check** | No duplicate term introduced (checked explicitly against the Stage 7C-identified "Case" duplication failure mode) — **Resource** is a genuinely new term, cross-referenced against the pre-existing **Recovery Resources** entry, not a second definition of an existing term. |
| **ADR index consistency** | `architecture-decisions/README.md`'s table now lists 28 ADRs in strict numeric order, ADR-025 through ADR-028 appended after ADR-024 with no gap or renumbering of any existing entry. |

**Validation outcome: no defect found.**

## 8. Remaining Stage 8 Work

**None.** HKMP Stage 8 (Donor & Resource Intelligence) — discovery (§8),
architecture (§8A), Donor & Funding implementation (§8B), Material Resource &
Logistics implementation (§8C), and governance integration (§8D) — is
complete. The domain is a fully certified, canonical part of the Khidmat
Knowledge Layer: its ADRs are ratified and indexed, its ownership is
declared in `ontology_authority_matrix.md`, its terms are in `GLOSSARY.md`,
its cross-domain boundary notes are authored in every file the Stage 8
process identified a reconciliation need for, and the one relationship
Support Delivery needed to complete the full donor-to-delivery chain is in
place.

Any further work (the DR-FLAG-A shared-supertype question, the DR-FLAG-B
contributed-labor Phase 2 candidate, or a future `consumable`/`equipment`
entity split if evidence later warrants it — see `donor-resource/governance.md`)
is, by this phase's own explicit design, new and separately-governed
proposal work, not outstanding Stage 8 scope.
