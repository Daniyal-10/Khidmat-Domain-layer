# Repository Migration Methodology

> **Status:** approved, in effect for all domain migrations from this point forward.
> **Relationship to the frozen contracts:** this document is a **peer**, not a
> subset, of `Canonical_Ontology_Schema.md` and `Canonical_Taxonomy_Schema.md`.
> Those two contracts define **what a conformant `ontology/`/`taxonomy/` module
> looks like** — the structural target. This document defines **how a legacy
> domain gets there** — the migration process. It changes neither contract, adds
> no new field, value, or governance to either, and must never be used to justify
> deviating from what they require. Where this document is silent, the two
> contracts remain the sole authority on structure.
>
> **Scope:** every current and future domain migration (Registration first;
> then Needs Assessment, Case Management, Community Context, Verification
> Operations, and any domain after) is expected to cite this document as its
> process authority and to contain, in its own migration plan, only
> domain-specific material — file inventories, concept lists, domain-specific
> decisions, and that domain's own content-gap log. No migration plan should
> restate a principle, source-authority rule, or validation requirement already
> stated here.

---

## 1. Migration Principles

- **Mechanical by default.** Once a domain's semantic decisions are identified,
  given a recommended default, and explicitly approved (that domain plan's own
  "Phase 0"), every later phase applies fixed, deterministic rules. No further
  judgment calls are made during execution.
- **No content invention.** A migration relocates, restructures, and
  re-serializes content that already exists in the repository. It never
  authors new descriptive or semantic text — not even a clearly-labeled
  placeholder or disclaimer — as a matter of expedience.
- **No status inference.** A file's lifecycle `status` (`active` / `placeholder`
  / `draft` / `deprecated`) is set deliberately, as an editorial decision by the
  domain owner or reviewer. A migration process never changes it automatically
  as a side effect of discovering incomplete content.
- **Structural change only; meaning unchanged.** Identifiers are frozen and
  never renamed. Concepts are neither added nor removed except where an
  approved domain decision explicitly authorizes new content. Every relocation
  must be independently verifiable, byte-for-byte, against the pre-migration
  source.
- **One phase, one reviewable unit.** Mechanical work proceeds in discrete
  phases with an explicit approval gate between them. A phase never mixes
  mechanical re-serialization with a semantic or judgment-bearing change.

---

## 2. Migration Source Authority

Canonical for a domain's migration is limited to **that domain's own governed
`ontology/` and `taxonomy/` files**, and within them, only **existing
authoritative content already present within the governed source file**.

This is a general test, not a closed hierarchy — for example (not an exhaustive
or ordered list): an already-populated field of the same kind being migrated
(e.g. an existing `description`), a whole-file `purpose:` when it unambiguously
describes exactly one record, or an adjacent comment that describes only that
one record and no other. Future migrations may recognize other forms of
already-present authoritative content without amending this rule, provided
each new form meets the same underlying test: content that already exists,
inside the governed file, unambiguously attributable to the single record
being migrated.

**Not canonical for migration purposes, regardless of how authoritative it
appears:**
- General repository documentation — READMEs, glossaries, discovery reports,
  business-logic documents, ADRs, inventories, roadmaps, and similar prose.
  These *describe* the taxonomy/ontology; they do not *constitute* it, and they
  are not subject to the same single-ownership or versioning discipline the
  governed files carry. Copying from them turns an informal, driftable
  secondary artifact into a de facto source of truth, and makes the outcome of
  a migration depend on which document a particular migrator happened to
  search — the opposite of deterministic.
- **A domain's own non-`ontology`/`taxonomy` folders** (`reasoning/`,
  `readiness/`, `questioning/`, `verification/`, `gaps/`, and equivalents).
  These encode logic and process, not vocabulary. Treating them as a
  description source blurs a separation the domain architecture already draws
  deliberately, and their content is frequently fragmented or context-specific
  rather than a single general definition.
- **Another domain's governed files, by direct copy.** See §3.

---

## 3. Duplicated-Content Handling

A gap is a **duplication risk**, not a content gap, when the repository's
**canonical ownership registry** shows the concept is already owned by a
different domain (the single-ownership discipline ADR-008 already
establishes repository-wide, restated by `Canonical_Taxonomy_Schema.md` §9 for
the taxonomy layer).

When this is the case:
- The other domain's text is **never copied**, even if it is complete,
  correct, and would satisfy the required field byte-for-byte. Copying it
  mints a second, unsynchronized copy of a single-owned concept — a
  duplication the repository's own governance already forbids.
- The dependency is recorded only as a **plain, non-structural comment**
  noting the eventual cross-domain relationship, until the repository's formal
  cross-domain reference mechanism (manifest + CURIE resolution) is available.
  No reference is fabricated in the interim, and no CURIE is invented ahead of
  that mechanism existing.
- Once the formal mechanism exists, the deferred comment is replaced by a real,
  manifest-resolved reference — never before.

---

## 4. What Is Mechanically Recoverable

A gap is **mechanically recoverable** when, and only when, §2's test is
satisfied by the record's own domain. Recovery is a pure relocation: the
existing text is copied verbatim, its exact source (file and section/line) is
cited in the migration's report, and no wording is added, removed, or altered
in the process.

---

## 5. Genuine Repository Content Gaps

If neither §2 nor §3 applies — no governed file, in this domain or in whichever
domain legitimately owns the concept, contains the required content — the gap
is **genuine**: the repository itself does not yet hold the knowledge the
frozen contract requires. A migration process does not fabricate a
description, a placeholder, a disclaimer, or a lifecycle-status change to
paper over this. It stops there and reports it. See §6.

---

## 6. Content Completion Policy

- Genuine gaps are closed by a **human, domain-knowledgeable author** writing
  the real description directly into the governed source file — never by the
  migration process, and never as an implicit byproduct of running one.
- Once written, the record satisfies §2/§4 and becomes mechanically
  recoverable on the next migration pass. No special-casing is needed at that
  point; the same mechanical rules apply cleanly.
- A domain's migration is **not** considered complete while any identified
  genuine gap remains open. Each domain's migration plan maintains an
  explicit, dated **Content Gap Log** so the pause is visible and trackable,
  never silent.

---

## 7. Separation of Migration vs. Content Authoring

- **Migration** is a structural operation: re-serializing content that already
  exists into the shape the frozen contracts require.
- **Content authoring** is an editorial operation: writing domain knowledge
  that did not previously exist.
- These are different activities with different authorities — mechanical
  execution versus domain-expert review — and are never merged into a single
  step. A migration plan may *identify* that authoring is needed (via its
  Content Gap Log); it does not perform the authoring itself.

---

## 8. Migration Validation Requirements

Before any phase of any domain migration is marked complete:
- Confirm, by diff against the pre-migration source, that no content outside
  the intended change set was touched — a byte-level check, not a visual read.
- Confirm every identifier (scheme, concept, entity, property, relationship)
  present before migration is still present after, under the same id
  (frozen-id rule).
- Confirm no new concept, scheme, or entity exists unless an approved
  domain-specific decision explicitly authorized it.
- Confirm the result parses and satisfies the frozen contracts' structural
  rules.
- Confirm line-ending and formatting conventions match the surrounding
  repository — a mechanical, not semantic, check, but one that has already
  produced a real defect in this process and must not be skipped.
- Treat any anomaly an automated diff surfaces as requiring byte-level
  re-verification before being dismissed, even when it looks like a display or
  encoding artifact (e.g. an em-dash rendering oddly) — never assume it benign
  from a printed diff alone.

---

## 9. Stopping Criteria

A migration phase stops and returns to review, rather than proceeding, when:
- A required field cannot be populated under §2/§4 and is not a §3 duplication
  — i.e. a genuine gap (§5) is discovered mid-phase.
- A domain-specific decision the phase depends on has not been explicitly
  approved.
- Two sections of the frozen contracts, or a contract and the domain's own
  migration plan, appear to require incompatible actions for the same record.
- Any check in §8 fails.

In every stopping case, the process reports exactly what blocked it and why,
and does not choose a resolution on its own.

---

## 10. Approval Gates

- **Gate 0 — Decisions.** Every domain-specific semantic decision a migration
  depends on is enumerated, given a recommended default, and explicitly
  approved (or overridden) before any file is touched.
- **Gate per phase.** Each phase's validation checklist must pass in full
  before the next phase begins. A partial pass does not unlock the next phase.
- **Content Completion Gate.** If a domain's Content Gap Log (§6) is
  non-empty, the phase that depends on the missing content does not proceed —
  regardless of how much other mechanical work is ready — until the log is
  empty.
- **Final Gate.** A domain is declared migrated only when every phase's
  checklist has passed and that domain's own Success Criteria (defined in its
  migration plan) all hold.

---

## 11. Reuse

Every future domain migration plan is expected to:
- Cite this document, alongside the two frozen structural contracts, as its
  process authority.
- Contain only domain-specific material: file inventories, concept lists,
  that domain's own Phase 0 decisions, and its Content Gap Log.
- Leave every cross-cutting principle, source-authority rule, and validation
  requirement to this document rather than restating it.

This is what makes the methodology reusable: a new domain's migration plan is
expected to be short, because everything that doesn't vary by domain already
lives here.
