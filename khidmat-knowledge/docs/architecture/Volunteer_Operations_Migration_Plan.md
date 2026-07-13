# Volunteer Operations Domain — Migration Implementation Plan

> **Audience:** the executing agent. **Status:** Phase 0 (boundary decisions)
> recorded and approved-by-default below. **Phase 1 (documentation
> synchronization) executed in this pass.** Phases 2–5 (the canonical `ontology/`
> and `taxonomy/` authoring) are **gated by an external business/operational
> trigger** — the Stage-9 activation condition — and are correctly *not* executed:
> there is no content to migrate, and authoring it now would be both content
> invention (`Repository_Migration_Methodology.md` §1) and premature activation
> (ADR-009).
>
> **Authorities:** `Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`
> (frozen structural contracts), `Repository_Migration_Methodology.md` (frozen
> process contract), ADR-004, ADR-008, ADR-009. This plan states only what is
> specific to Volunteer Operations. **Companion:** `Volunteer_Operations_Domain_Audit.md`.

---

## Why this plan is shaped differently from Registration / Community Context

The two reference migrations re-serialized **dense existing content** onto the
frozen contracts. Volunteer Operations has **no governed ontology or taxonomy
content at all** (audit VO-1). A migration cannot re-serialize what does not
exist. Consequently:

- **There is no mechanical Phase 2/3/4 to run now.** Those phases in the
  reference plans converted existing taxonomy/ontology files. Volunteer
  Operations has none.
- **The whole ontology/taxonomy body is a deferred genuine content gap**
  (methodology §5), gated by the Stage-9 activation trigger — not an authoring
  task available today.
- **The value deliverable now is scaffolding:** settle the boundary (Phase 0),
  synchronize documentation of the one already-decided boundary (Phase 1), and
  pre-write the activation-time phase sequence so that when the trigger fires,
  activation is deterministic. This mirrors how the reference plans front-load
  every semantic decision into Phase 0 so later phases are mechanical.

This is the profile `Repository_Migration_Methodology.md` §9 describes as a
correct stop: *"a required field cannot be populated under §2/§4 and is not a §3
duplication — i.e. a genuine gap."* Here the gap is domain-wide and gated.

---

## Business Validation (Phase 2 of the assigned task)

Cross-checked `volunteer-operations/` against
`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` (§4 Actors, §14 Flow, §16 Scope) and
the humanitarian operating flow. Full table in the audit §3. Summary:

- **Volunteer profile, availability, geographic coverage, trust, assignment
  history, training status** — all declared in the placeholder; all **Future
  (VO owns on activation)**. Blueprint §4/§16 confirm they are deliberately
  out of V1 scope.
- **The `volunteer` role label, the `Actor` entity, the verification/case
  assignment acts, escalation reasons** — all **belong elsewhere** and are
  **already owned** by their domains (`shared/taxonomy/persons.yaml`,
  `shared/ontology/entities.yaml`, `verification-operations`, `case-management`).
  No mis-location to unwind.
- **Skills, certifications, languages, workload, scheduling, field teams** —
  Future (VO owns); the first three are *candidate additions* to the placeholder
  concept list (Decision D-VO3).
- **Conclusion:** Volunteer Operations requires **no ownership change in any
  active domain** to reach canonical maturity on activation. Its only current
  boundary that touches active content is the verification-assignment boundary,
  which is already decided (audit VO-6).

---

## Content Gap Log

| Status | Scope | Resolution |
|---|---|---|
| **DEFERRED (gated)** | entire `ontology/` module | authored by a domain-knowledgeable author *after* the Stage-9 activation trigger; authoring now violates methodology §1 + ADR-009 |
| **DEFERRED (gated)** | entire `taxonomy/` module | same |
| CLOSED (this pass) | reciprocal documentation of the verification-assignment boundary (VO-6) | README "Does Not Own" line added; `FLAG-006` added to `ontology_authority_matrix.md` |
| OPEN (decision) | placeholder concept-list completeness (D-VO3) | reviewer decision; default = defer to activation |

The two DEFERRED rows are the **correct, expected stopping point** — not a
failure of this migration. Per methodology §6/§10 (Content Completion Gate), the
canonical-authoring phases do not proceed while these are open, and they cannot
be closed until the activation trigger fires.

---

# PHASE 0 — Boundary & Scope Decisions (no ontology/taxonomy files changed)

### Decision Table

| ID | Decision | Contract / governance basis | Recommended default | Approved value |
|----|----------|------------------------------|---------------------|----------------|
| **D-VO1** | Can any canonical `ontology/`/`taxonomy/` content be authored now? | Methodology §1 (no content invention), §5 (genuine gap), ADR-004 (may not add concepts to placeholder domains), ADR-009 (dependency-driven activation). | **No.** The domain has no content to re-serialize and its activation trigger is unmet; authoring now is a double governance violation. Defer all canonical authoring to activation. | ☑ Approved (default) |
| **D-VO2** | Should `_placeholder.yaml` be normalized to the canonical four-key header (`version`/`domain`/`file`/`status`, snake_case `domain`, status enum)? | Ontology §12 / Taxonomy §4 govern *governed ontology/taxonomy files*; `_placeholder.yaml` is an ADR-004 scope artifact. `community-context/_placeholder.yaml` is retained un-normalized post-migration as precedent. | **No.** Leave the placeholder in its ADR-004 shape. Normalizing it would misapply the contract and read as a half-activation. | ☑ Approved (default) |
| **D-VO3** | Add `skills`, `certifications`, `languages` (and workload/scheduling) to `concepts_this_domain_will_own` now? | ADR-004 (placeholder declares intended ownership); methodology §1 (adding a *concept id to a scope list* is a governance declaration, not ontology content — but it is still an editorial scope choice). | **Defer to activation.** The existing six declared concepts are sufficient to lock the boundary; the exact concept decomposition (skills vs. certifications vs. training) is precisely what "requirements emerging from operational experience" (Stage 9) is meant to determine. Recording them now risks pre-committing a decomposition operations staff should drive. | ☑ Approved (default) |
| **D-VO4** | Reciprocally document the verification-assignment boundary (VO-6) now? | Methodology "documentation synchronization" deterministic category; the boundary is already stated by `verification-operations` (one-directional). | **Yes.** Mechanical doc-sync of an existing decision, not a new decision. Add a README "Does Not Own" line and `FLAG-006` to the authority matrix. | ☑ Approved (default) |
| **D-VO5** | Ownership of the `Actor` entity and `volunteer` role on activation. | ADR-008, ADR-018; both already single-owned (`shared/ontology/entities.yaml#actor`, `shared/taxonomy/persons.yaml#person_roles.volunteer`). | **No action.** VO references both; it never redefines them. The `actor` entity's authority-matrix note already reads "Placeholder for an operational participant" — VO will attach its profile *behind* that reference, via a `references`/relationship link authored at activation, not by minting a second actor. | ☑ Approved (default) |

### Phase 0 validation checklist
- [x] Every decision D-VO1–D-VO5 has an approved value (defaults; no overrides).
- [x] No default overrides a frozen-contract rule (each is *more* conservative than the contract requires).
- [x] Decision Table pasted into this plan.
- [x] No `ontology/`/`taxonomy/` file created or modified in Phase 0.

---

# PHASE 1 — Documentation Synchronization (mechanical, executed this pass)

**Objective.** Record the one already-decided boundary (VO-6) reciprocally, and
nothing more. **Files affected:** `volunteer-operations/README.md` (Does Not Own
line), `ontology_authority_matrix.md` (new `FLAG-006`). **No domain content is
authored.**

**Rules (deterministic):**
1. Add to README "Does Not Own": the verification-assignment act
   (`VerificationAssignment`) and case-assignment act (`CaseAssignment`) — VO
   owns *actor fitness to be assigned*, never *the assignment event*.
2. Add `FLAG-006` to `ontology_authority_matrix.md` Flagged Boundary Cases,
   recording the actor-qualification vs. assignment boundary, citing the
   verification-operations text that already states it. `Status: Recorded`
   (the boundary is decided; VO's side activates in Stage 9).
3. **Do not** add a "Volunteer Operations" owned-concepts section to the
   authority matrix — VO owns no concepts yet; recording owned concepts before
   they are authored would violate the matrix's own rule ("declared… at the
   time the concept is written").

### Phase 1 validation checklist
- [x] README "Does Not Own" names the assignment-act boundary.
- [x] `FLAG-006` added; cites the existing verification-operations statement.
- [x] No owned-concept row added to the matrix for VO (none exists to add).
- [x] No `ontology/`/`taxonomy/` file created.

---

# PHASE 2–5 — Canonical Authoring (GATED — not executed; awaits activation trigger)

**Precondition (external, business/operational):** the Stage-9 activation
trigger — *"a volunteer management workflow is defined with operations staff;
volunteer profile requirements emerging from operational experience"*
(`knowledge_layer_roadmap.md` Stage 9; `_placeholder.yaml`
`do_not_implement_until`). **This has not occurred.**

When it fires, activation proceeds mechanically in this order (each a gate):

- **Phase 2 — Scaffold the canonical file set.** Create
  `volunteer-operations/ontology/{entities,data-properties,relationships,semantic-constraints,lifecycle-constraints}.yaml`
  and `volunteer-operations/taxonomy/` per the domain template (Ontology §13,
  Taxonomy §13), headers per Ontology §12 / Taxonomy §4 (snake_case
  `domain: volunteer_operations`). Placeholders use empty lists until authored.
- **Phase 3 — Author taxonomy.** The controlled vocabularies operations staff
  define (e.g. skill types, certification types, availability states, coverage
  units, trust/performance bands, training statuses) as `schemes:`→`concepts:`
  lists. **Content authoring by a domain-knowledgeable author, not migration.**
- **Phase 4 — Author ontology.** `volunteer_profile` and any promoted entities;
  data properties (including Value Objects per Ontology §17 where a bundle is
  owner-scoped and non-referenceable); relationships — including the
  reference/link from the volunteer profile to `shared:Actor` and, where
  relational, to the operational domains' assignment entities (VO owns *fitness*,
  never the assignment act — D-VO5, VO-6). Classify every nested attribute
  against the §17 promotion test, exactly as Registration's D6-REV did.
- **Phase 5 — Cross-domain CURIE layer.** Blocked on the same repository-wide
  manifest + ratified base IRI (C-2/R-1) that parks Registration and Community
  Context at their Phase 5. VO adds no new external blocker.

Concurrent governance at activation: add a "Volunteer Operations" owned-concepts
section to `ontology_authority_matrix.md`; flip `_placeholder.yaml`
`status: not_yet_active` and the roadmap Stage-9 entry.

---

# Success Criteria

**For this pre-activation pass (achievable now):**
1. Boundary settled and recorded (Phase 0 + Phase 1). ✔
2. All future work classified as owns / belongs-elsewhere / deferred-gated
   (audit §3–§7). ✔
3. A complete, ordered activation-time phase sequence exists (Phase 2–5). ✔
4. No canonical content authored and no premature activation performed
   (D-VO1/D-VO2). ✔
5. Only a genuine business/operational decision (the activation trigger) and the
   future domain-authoring it unlocks remain. ✔

**For full canonical maturity (achievable only post-activation):** Phases 2–5
executed against operations-staff-defined content, conformant to both frozen
contracts, matrix updated, placeholder retired.

# Exit Criteria

- **Phase 0:** exits on approved Decision Table (done).
- **Phase 1:** exits when the two doc-sync edits land and validate (done).
- **Phase 2–5:** do **not** begin until the Stage-9 activation trigger fires.
  Until then this plan is correctly parked — the same valid end-state
  Registration/Community Context hold at their Phase 5, one phase earlier.

*End of plan.*
