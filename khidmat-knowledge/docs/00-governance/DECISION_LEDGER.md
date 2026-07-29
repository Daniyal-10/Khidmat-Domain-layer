---
id: DOC-GOV-004
title: Khidmat AI Governance Decision Ledger
version: 1.0
status: Active — the repository's decision ledger
owner: Governance
created: 2026-07-29
depends_on: docs/00-governance/CONSTITUTION.md (v1.0)
layer: 00-governance
domain: Foundation
tags: [governance, ledger, adr, decisions]
---

# Governance Decision Ledger

**Constitutional basis.** `CONSTITUTION.md` Article XVII requires the Domain Approval Authority to act "by formal written decision recorded in the repository's decision ledger (the governance ledger)." Article XIX requires amendments to be proposed "through a formal Request for Comments (RFC) stored in the governance ledger."

**Created under remediation B10.** The accepted Foundation Readiness Assessment recorded that this ledger did not exist, that the directory previously scoped for it had been deleted (per `HUMAN_OWNER_DECISION_BRIEF_01.md`), and that no ADR existed anywhere in the repository despite five having been formally recommended.

**What belongs here.** Formal written decisions of the Domain Approval Authority; Architectural Decision Records; RFCs proposing constitutional amendment; and Package approvals under Article XVI. Discovery findings, assumptions and contradictions do **not** belong here — they have their own registers in `docs/01-methodology/discovery/`.

**Status vocabulary.** `Ratified` (decided and binding) · `Open` (raised, awaiting decision) · `Superseded` · `Void`.

---

## Register

| ID | Title | Status | Decided | Raised under |
|---|---|---|---|---|
| ADR-001 | Khidmat's operating scope — understanding versus delivery | **Open** | — | B9 |
| ADR-002 | Canonical ownership of Location | **Open** | — | B10 (carried from `CONCEPT_OWNERSHIP.md` §7) |
| ADR-003 | Consent propagation and revocation across organisational boundaries | **Open** | — | B10 (carried from `CONCEPT_OWNERSHIP.md` §7) |
| ADR-004 | Standardised epistemic evidence grading | **Open** | — | B10 (carried from `DISCOVERY_HARMONIZATION_REPORT.md` §6) |
| ADR-005 | Immutable snapshots for MEAL | **Open** | — | B10 (carried from `DISCOVERY_HARMONIZATION_REPORT.md` §6) |
| ADR-006 | Cryptographic deduplication standards | **Open** | — | B10 (carried from `DISCOVERY_HARMONIZATION_REPORT.md` §6) |
| GOV-001 | Voidance of the Stage 5 Business Discovery Certification | **Ratified** | 2026-07-29 | B10 |
| GOV-002 | Package A (Khidmat Foundation) approval | **Open — awaiting Domain Approval Authority** | — | B12 |

---

## ADR-001 — Khidmat's operating scope: understanding versus delivery

**Status:** Open. **Raised:** 2026-07-29 under remediation B9. **Decision authority:** Project Lead / Domain Approval Authority.

### The contradiction requiring decision

`BUSINESS_MASTER_PLAN.md` §2 places outside scope: *"Building or replacing proprietary end-user case management workflows"* and *"Direct delivery of humanitarian aid or material resources."* §5 commits that *"Khidmat AI will never become a humanitarian aid-delivery organisation."*

Stage 5 then discovered, in depth, a full aid-delivery operating model — `resource-logistics` covers procurement, warehousing, dispatch, FSP cash execution and last-mile distribution — and a full case-management workflow.

Separately, the client blueprint (`direct-relief-architecture.html`) describes a peer-to-peer platform that performs donation matching, escrow, volunteer dispatch and last-mile delivery directly.

### Why this must be decided before ontology design

Pillar P1 and Rule AR-1 both turn on the Reality Knowledge / Operational Knowledge boundary, which distinguishes humanitarian reality from *how a particular organisation operates*. The test cannot be applied crisply while it is unclear whose operations are in view. Every concept admission decision inherits this ambiguity.

### Options

1. **Khidmat understands but does not deliver.** Ratifies the Business Master Plan as written. Stage 5's delivery discovery remains valid as Reality Knowledge about how the sector works — Khidmat models delivery without performing it. The client's platform becomes an application consuming the foundation, not the foundation itself.
2. **Khidmat understands and delivers.** Requires amending `BUSINESS_MASTER_PLAN.md` §2 and §5, and re-examining the neutrality commitments in §4 and §5 that depend on Khidmat not being an operational actor.
3. **Khidmat is the knowledge layer; a separate product delivers.** Two-entity model. Requires stating the relationship between them.

### Repository position

**No option is recommended here.** This is a decision about the project's own intent, which no amount of repository evidence can settle — the same reasoning `HUMAN_OWNER_DECISION_BRIEF_01.md` applied to CL-001 and CL-002. Note for the deciding authority: Option 1 requires no document change and is consistent with `PROJECT_OVERVIEW.md` Ch3.2's infrastructure framing (*"Organisations should not have to replace their existing systems"*). Options 2 and 3 require amendment to a Frozen document.

**Interim working position.** Until decided, Option 1 is treated as the operative reading, because it is what the frozen canonical document actually says. Remediation B4 was executed on this basis: giving is modelled as humanitarian reality, not as a Khidmat capability.

---

## ADR-002 — Canonical ownership of Location

**Status:** Open. **Raised:** carried into the ledger 2026-07-29 under B10; originally logged in `CONCEPT_OWNERSHIP.md` §7 following validation finding MAJ-02 and remediation REM-03.

**Issue.** `resource-logistics` manages operational locations (warehouses, distribution points, camps); `organisation-partner-management` manages administrative locations (field offices, geographic presence). Validation established that assigning canonical ownership to either without evidence was unsupported.

**Not resolved by this remediation phase.** It requires either evidence or an authority decision, and neither is available to an execution phase. It is moved from a bullet in a cross-domain document into the ledger so it is visible to the authority that can decide it.

---

## ADR-003 — Consent propagation and revocation across organisational boundaries

**Status:** Open. **Raised:** carried into the ledger 2026-07-29 under B10; originally logged in `CONCEPT_OWNERSHIP.md` §7.

**Issue.** Three domains independently record that consent revocation must propagate and that the mechanism is unknown: `registration-identity/10-open-questions.md`; `cross-organisational-coordination/10-open-questions.md`; `DISCOVERY_HARMONIZATION_REPORT.md` §2, which calls the flow of the "kill signal" across autonomous domains "highly ambiguous."

**Related change under B6.** The classification of Consent has been resolved — the person's act of authorising is Reality Knowledge; the organisational record is Operational (`CONCEPT_OWNERSHIP.md` §8). That resolves *what consent is*. It does not resolve *how revocation propagates*, which remains open.

---

## ADR-004 — Standardised epistemic evidence grading

**Status:** Open. **Raised:** carried into the ledger 2026-07-29 under B10; originally recommended in `DISCOVERY_HARMONIZATION_REPORT.md` §6.

**Issue.** The harmonization report recommended that all critical data payloads carry an evidence-level wrapper (e.g. Claimed, Community Validated, Document Verified). `PROJECT_OVERVIEW.md` Ch5.2 supplies the seven strength factors; `registration-identity/05-business-rules.md` supplies one concrete organisational rule (two distinct points of evidence to reach Verified). No repository source states the grading scheme practitioners actually recognise.

**Boundary note for the deciding authority.** The *representation* of evidence grading is ontology-design work (`ONTOLOGY_DESIGN.md` §2.7) and should not be pre-empted here. What this ADR needs to settle is the business question: what grades exist in practice, and what threshold is treated as sufficient to act. That is gated on B13.

---

## ADR-005 — Immutable snapshots for MEAL

**Status:** Open. **Raised:** carried into the ledger 2026-07-29 under B10; originally recommended in `DISCOVERY_HARMONIZATION_REPORT.md` §6.

**Issue.** `accountability-evaluation` must consume Case Management and Logistics data to evaluate impact, while remaining structurally independent of both (`accountability-evaluation/12-domain-invariants.md`, "The Principle of Independence"). The harmonization report proposed that Accountability operate on read-only point-in-time snapshots with no write access.

**Scope caution.** As phrased in the harmonization report this edges toward implementation architecture, which Stage 5 prohibits. The business question — whether an evaluator may alter operational records — is already answered by the independence invariant. What remains open is whether the business requires *historical* state to be preserved for evaluation, which is a Reality Knowledge question about auditability.

---

## ADR-006 — Cryptographic deduplication standards

**Status:** Open. **Raised:** carried into the ledger 2026-07-29 under B10; originally recommended in `DISCOVERY_HARMONIZATION_REPORT.md` §6.

**Issue.** Deduplication across organisational boundaries must reconcile `cross-organisational-coordination`'s need to detect duplicate aid against `registration-identity`'s data-minimisation mandate. Discovery already establishes the business rule: *"Deduplication alerts must preserve privacy (e.g., verifying a cryptographic hash of an identity rather than broadcasting a name)"* (`cross-organisational-coordination/05-business-rules.md`).

**Scope caution.** The specific cryptographic mechanism is implementation, not business architecture, and is out of scope for the foundation. The business decision is narrower: what minimum information may cross an organisational boundary for the purpose of duplicate detection.

---

## GOV-001 — Voidance of the Stage 5 Business Discovery Certification

**Status:** Ratified. **Decided:** 2026-07-29 under remediation B10.

### Decision

`docs/03-cross-domain/STAGE5_CERTIFICATION.md` is **VOID** and carries no authority. It is retained in place with a voidance banner rather than deleted, for institutional memory.

### Grounds

1. **Article XVI.** *"A certification issued for a document whose content does not exist or has skipped a gate is void."* The certification declared the project *"cleared to commence Stage 6"* while Stage 6.1 (Stable Core Alignment) — the pipeline's own prerequisite gate — had not been performed. It certified past a gate.

2. **Direct contradiction by the repository's own validation.** `docs/03-cross-domain/VALIDATION/CERTIFICATION.md` records **NOT CERTIFIED** for the same body of work, with two FAILED and two INCOMPLETE assessment areas. `REMEDIATION_REPORT.md` states the layer became *"eligible for an independent re-validation to achieve final certification."* That re-validation was never performed. Two contradictory certifications cannot both stand.

3. **Methodological unsoundness.** §2.6 of the certification states that *"the 'Reality Knowledge' and 'Operational Knowledge' concepts within each domain directly map to ontological classes"* and that *"the 'Business Relationships' explicitly define the object properties."* Reality/Operational is an admission test under Article IV, not a class hierarchy. This is the schema-first inversion the Project Lead identified, asserted inside a certifying document, and it violates the same Concept Purity rule (`STAGE_5_DISCOVERY_STANDARD.md` §5 item 3) that validation finding CRIT-01 enforced against `SHARED_CONCEPT_CATALOG.md`.

### Consequence

No valid certification of Stage 5 exists. The standing state of the cross-domain layer is **NOT CERTIFIED**, per `VALIDATION/CERTIFICATION.md`, until an independent re-validation is performed. This remediation phase does not perform it — an execution phase cannot certify its own output.

---

## GOV-002 — Package A (Khidmat Foundation) approval

**Status:** Open — awaiting the Domain Approval Authority. **Raised:** 2026-07-29 under remediation B12.

### What is required

`CONSTITUTION.md` Article XVI: *"Package A (Khidmat Foundation): Must be complete and approved before Ontology Design can begin."* Article XVII: the Domain Approval Authority — the Project Lead and the designated human owners of the architectural review board — *"acts by formal written decision recorded in the repository's decision ledger."*

### Why this remediation phase cannot close it

Approval is an act of a constituted authority. No agent, and no execution phase, may grant it on that authority's behalf. This entry exists so the decision has somewhere to be recorded.

### State of the package at the time of raising

| Item | State |
|---|---|
| Project Overview (Stage 1) | Frozen, v1.0 |
| Business Master Plan (Stage 2) | Frozen, v1.3 (amended under B1) |
| HBRM (Stage 3) | Frozen, v1.0 |
| Business Architecture (Stage 4) | Frozen, v1.0; the pipeline's reconciliation step performed retrospectively under B2 |
| Domain Discovery (Stage 5) | Ten domains. Seven original with provenance retrofitted (B7); three added (B2, B3, B4). Three marked REQUIRES FURTHER DISCOVERY; all ten record `Client Validation: Pending` |
| Stable Core Definitions (Stage 6.1) | Produced under B8 (`FOUNDATION_CONCEPTS.md` Part II) |
| Governance | Constitution v1.0 normative; this ledger established; Stage 5 certification voided (GOV-001) |
| Ground truth validation | **Absent.** Tier A executed zero times across six dossiers and ten domains |

### Matters the Authority should have before it

- Six open ADRs above, of which **ADR-001 is load-bearing** — it settles the scope question on which the Article IV admission test depends.
- The absence of any ground truth channel (remediation B13), which `ONTOLOGY_DESIGN.md` §5 states prevents any Ground Truth Review from passing and leaves every universal Constraint tag untested.
- Four assumption-register entries opened by this remediation (AR-015 to AR-018), recording knowledge carried on single unevidenced internal sources.
- AR-011 and AR-013, which remain open and cannot be closed from repository evidence.
