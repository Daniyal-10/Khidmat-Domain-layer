# Volunteer Operations Domain — Migration Audit (Findings)

> **Companion to:** `Volunteer_Operations_Migration_Plan.md`.
> **Authorities:** `Canonical_Ontology_Schema.md`, `Canonical_Taxonomy_Schema.md`
> (frozen structural contracts), `Repository_Migration_Methodology.md` (frozen
> process contract), ADR-004 (Placeholder Domain Strategy), ADR-008 (Single
> Ownership), ADR-009 (Dependency-Driven Domain Activation).
> **Status:** Discovery complete. This audit records what Volunteer Operations
> *is* today, what it *must* own on activation, and where its boundaries fall —
> not a set of executable migration steps (those are in the plan).

---

## 1. Executive finding

Volunteer Operations is a **bare Level 2 placeholder**. Its entire on-disk
footprint is two files:

| File | Role |
|---|---|
| `volunteer-operations/_placeholder.yaml` | ADR-004 scope declaration (`maturity: level_2_placeholder`, `status: not_yet_active`) |
| `volunteer-operations/README.md` | Human-readable scope, Owns / Does Not Own, activation condition |

There is **no `ontology/` module, no `taxonomy/` module, and no governed
content of any kind.** This is the decisive difference from the two migration
references:

| Domain | Governed files at migration start | Migration was… |
|---|---|---|
| Registration | 9 taxonomy + 4 ontology + reasoning/readiness/questioning/verification | re-serialization of dense existing content |
| Community Context | 12 taxonomy + 5 ontology | re-serialization of dense existing content |
| **Volunteer Operations** | **0 governed ontology/taxonomy files** | **nothing to re-serialize** |

A migration, per `Repository_Migration_Methodology.md` §1, "relocates,
restructures, and re-serializes content that already exists. It never authors
new descriptive or semantic text." Volunteer Operations has no such content.
Its ontology/taxonomy is therefore, in the methodology's own vocabulary
(§5), a **genuine repository content gap** across the entire domain — and one
that is **deliberately deferred**, not overlooked (ADR-004, ADR-009).

**Conclusion:** the mechanical migration surface for Volunteer Operations is
empty. The correct deliverable at this stage is the *scaffolding* — the audit,
the boundary decisions, and the activation-gated migration plan — so that when
the domain's activation trigger fires, activation and canonical authoring
proceed against a settled boundary. See the plan's Phase 0.

---

## 2. Placeholder-state audit

### VO-1 — Placeholder declaration is conformant to the ADR-004 convention

`_placeholder.yaml` carries exactly the five keys ADR-004 prescribes and every
peer placeholder (`support-delivery`, `programs`, `impact`, `community-context`'s
retained `_placeholder.yaml`) uses: `domain`, `maturity`, `status`, `scope`,
`concepts_this_domain_will_own`, plus a `do_not_implement_until` condition.
**No change required.**

### VO-2 — The placeholder is *not* a governed ontology/taxonomy file

`_placeholder.yaml` deliberately does **not** carry the canonical four-key
header (`version`/`domain`/`file`/`status`) of `Canonical_Ontology_Schema.md`
§12 / `Canonical_Taxonomy_Schema.md` §4, and its `domain: volunteer-operations`
is kebab-case, and its `status: not_yet_active` is outside the closed
`active|placeholder|draft|deprecated` enum.

This is **correct, not a defect.** The four-key header + snake_case `domain` +
status-enum contract governs *governed ontology/taxonomy files*. A placeholder
scope declaration is an ADR-004 governance artifact that precedes the domain's
canonical file set. `community-context/_placeholder.yaml` — retained in the
repository *after* Community Context reached Canonical (Content Pending) —
demonstrates the placeholder convention and the canonical file contract coexist
as two distinct shapes. **Normalizing `_placeholder.yaml` to the four-key header
would misapply the contract and would read as a half-activation of the domain.
Do not do it.** (See plan Decision D-VO2.)

### VO-3 — README is consistent but under-specifies one active boundary

`README.md`'s "Does Not Own" correctly excludes the `volunteer` role label
(owned by `shared/taxonomy/persons.yaml`) and "anything in registration,
verification, or case management." It does **not** yet state the specific,
already-decided boundary with `verification-operations`'
`VerificationAssignment` (see VO-6). This is a documentation-sync gap, not a
content gap — addressed mechanically in the plan (Phase 1).

---

## 3. Business validation (against Blueprint V1 + humanitarian flow)

Cross-checked `_placeholder.yaml` and `README.md` against
`KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 (Actors), §14 (Operating Flow —
"Volunteer Assignment" stage), and §16 (Scope — "Volunteer Operations (full
volunteer profiles and dispatch)" is **Planned, not delivered**).

Blueprint §4 is explicit: *"detailed operational profiles — availability,
routing, performance — belong to the Volunteer Operations domain and are out of
V1 scope."* Every concept the task prompt listed to validate resolves cleanly:

| Concept to validate | Classification | Owner (current or future) |
|---|---|---|
| `volunteer_profile` | **Future (VO owns)** | Volunteer Operations, on activation |
| `volunteer_availability` | **Future (VO owns)** | Volunteer Operations, on activation |
| `volunteer_geographic_coverage` | **Future (VO owns)** | Volunteer Operations, on activation |
| `volunteer_trust_score` | **Future (VO owns)** | Volunteer Operations, on activation |
| `volunteer_assignment_history` | **Future (VO owns)** | Volunteer Operations, on activation |
| `volunteer_training_status` | **Future (VO owns)** | Volunteer Operations, on activation |
| skills / certifications / languages | **Future (VO owns)** — not yet in placeholder list | Volunteer Operations (candidate additions, D-VO3) |
| workloads / scheduling / field teams | **Future (VO owns)** | Volunteer Operations, on activation |
| verification capability / delivery capability | **Future (VO owns)** — the *actor's fitness* to verify/deliver | Volunteer Operations |
| escalation | **Belongs elsewhere** | `verification-operations/taxonomy/escalation-reasons.yaml` (already owned) |
| the `volunteer` **role label** | **Belongs elsewhere** | `shared/taxonomy/persons.yaml#person_roles.volunteer` (already owned) |
| the `Actor` **entity** | **Belongs elsewhere** | `shared/ontology/entities.yaml#actor` (already owned) |
| the **verification assignment act** | **Belongs elsewhere** | `verification-operations` `VerificationAssignment` (already owned) |
| the **case assignment act** | **Belongs elsewhere** | `case-management` `CaseAssignment` (already owned) |
| organizations / permissions / territories | **Split** — see VO-5 | partly shared, partly VO, partly community-context |

**No business concept that Volunteer Operations must own is currently
mis-located in another domain.** The already-active domains (Verification
Operations, Case Management) each took only the *assignment act* they needed and
explicitly deferred *actor qualification* to Volunteer Operations. There is no
drift to unwind — only future authoring to schedule.

---

## 4. What Volunteer Operations owns / must never own

### Owns (on activation)
The volunteer as a **persistent, qualified operational resource**: the profile
behind the `volunteer` role — identity-of-capacity (skills, certifications,
languages, training status), availability, geographic coverage, workload,
trust/performance, and the *history* of assignments as they pertain to the
volunteer's record.

### Must never own
- The `volunteer` **role label** — `shared/taxonomy/persons.yaml` (ADR-008).
- The `Actor` **entity** — `shared/ontology/entities.yaml` (ADR-018).
- The **act of assigning** a verification (`VerificationAssignment`,
  verification-operations) or a case (`CaseAssignment`, case-management). VO owns
  *who is fit to be assigned*; the operational domains own *the assignment
  event itself*. This is the single most important boundary and is already
  half-stated by verification-operations (VO-6).
- Registration claim epistemics, verification findings, case plans — all owned
  by their respective active domains.

---

## 5. Repository comparison — exposure surfaces

| Counterparty domain | VO exposes to it | It exposes to VO | Boundary status |
|---|---|---|---|
| Verification Operations | volunteer fitness/qualification to verify (future) | `VerificationAssignment`, `assigned_to` edge to `shared:Actor` | **Decided**, one-directional; VO-6 |
| Case Management | volunteer fitness to be a case assignee (future) | `CaseAssignment` | Decided by analogy to VO-6; not yet documented |
| Registration | the full profile behind `registrant_type: volunteer` | the `volunteer` role usage only | Decided; README states it |
| Shared (`persons`, `entities`) | nothing (references only) | `volunteer` role, `Actor` entity | Decided; reference-not-redefine |
| Community Context | volunteer's operating coverage may *reference* geographic hierarchy | `geographic-hierarchy` scheme (as `taxonomy_ref` on activation) | Deferred to activation + manifest (Phase 5) |
| Support Delivery (planned) | volunteer fitness/availability to deliver | delivery-task assignment (future) | Deferred; both planned |
| Programs (planned) | volunteer-to-program allocation (future) | program targeting (future) | Deferred; both planned |

The cross-domain reference mechanism (manifest + CURIE) does not yet exist for
*any* domain (Registration and Community Context are both parked at their
respective Phase 5). Volunteer Operations inherits that same external blocker;
it does not introduce a new one.

---

## 6. VO-6 — The one active, already-decided boundary (verification-operations)

`verification-operations/ontology/relationships.yaml` (`activity_conducted_by_actor`)
states verbatim: *"Verification Operations does not define actor qualification,
roles, or types — that remains a Volunteer Operations concern (Level 2
placeholder)."* `review-decisions.yaml` echoes it: *"actor qualification is a
Volunteer Operations [concern]."* And `entities.yaml`'s `VerificationAssignment`
records that it *"implements the 'Volunteer assignment model' identified as
pending… Stage 4"* while owning only the assignment, not the actor's fitness.

This boundary is therefore **already ratified in the repository, from the
verification side only.** Recording it reciprocally — in Volunteer Operations'
own README and in `ontology_authority_matrix.md`'s Flagged Boundary Cases — is
pure documentation synchronization of an existing decision (methodology's
"documentation synchronization" deterministic category), not a new architectural
decision. This is the audit's single actionable mechanical finding. See plan
Phase 1 and the added `FLAG-006`.

---

## 7. Content Gap Log

Per `Repository_Migration_Methodology.md` §5/§6, the entire ontology/taxonomy
body of Volunteer Operations is a genuine content gap — but a *deferred* one,
gated by a business/operational trigger, not an authoring task available now.

| Status | Scope | Nature | Resolution owner |
|---|---|---|---|
| **DEFERRED (gated)** | entire `ontology/` module (5 files) | genuine gap; no content to migrate; authoring now = premature activation (ADR-009) + content invention (methodology §1) | domain-knowledgeable author, **after** the Stage-9 activation trigger |
| **DEFERRED (gated)** | entire `taxonomy/` module | same as above | same |
| **OPEN (mechanical, now)** | README + authority-matrix reciprocal boundary (VO-6) | documentation sync of an already-decided boundary | this pass (Phase 1) |
| **OPEN (decision, now)** | placeholder concept-list completeness (skills/certifications/languages — D-VO3) | governance decision: add to `concepts_this_domain_will_own` or leave to activation | reviewer (Phase 0) |

The two DEFERRED rows are **not** blockers this migration can close — they are
the expected, correct stopping point.

---

## 8. Readiness

- **Structural readiness to activate:** its Stage-8 prerequisite (Community
  Context) is structurally canonical (Content Pending). ✔
- **Operational readiness to activate:** the Stage-9 trigger — *"a volunteer
  management workflow defined with operations staff… volunteer profile
  requirements emerging from operational experience"* — has **not** occurred.
  NOT MET (no workflow definition exists anywhere in the repository).
- **Migration readiness:** the boundary is settled and the plan is written, so
  activation is unblocked the moment the operational trigger fires. ✔

**The gate is a business/operational decision, not a knowledge-layer task** —
exactly the class of blocker the assigned task says to stop at.

*End of audit.*
