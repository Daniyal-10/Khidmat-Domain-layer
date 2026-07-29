# Khidmat — Ontology Foundation

Repository reset 2026-07-29. Everything untraceable to an authoritative source was deleted.
**The foundation is complete and frozen. The current phase is ontology design.**

---

## Authority

Two tiers. They do different jobs and must not be confused.

### Tier 1 — Sources of fact (frozen, never edited)

| Document | Role |
|---|---|
| `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` | Primary authority on humanitarian facts. Where sources disagree, this wins. |
| `KHIDMAT_AI_BUSINESS_OVERVIEW.html` | Client First Draft. Vision and direction. |

Plus external humanitarian standards — OCHA, UNHCR, IASC, ICRC, Sphere/CHS, IOM, WHO — as
retrieved into `docs/01-evidence/`.

### Tier 2 — Source of derivation (frozen)

| Document | Role |
|---|---|
| `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | **The ontology derives from this document and nothing else.** |

The reference model does not outrank Tier 1 — it is built entirely from it, with every
statement cited. It is the *only* document ontology work reads. If the ontology needs a fact,
it comes from here; if it is not here, it is an open question, not a licence to invent.

**To change a fact, amend Tier 1 and re-derive.** No downstream document may override a
source. That single rule is why this repository was reset.

---

## Document map

Everything below is **FROZEN**. No further foundation documents are to be created.

| Document | Status | What it is |
|---|---|---|
| `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` | FROZEN | Authority |
| `KHIDMAT_AI_BUSINESS_OVERVIEW.html` | FROZEN | Authority |
| `docs/01-evidence/TD-01 … TD-06` | FROZEN | The only externally-sourced material in the project. Evidence, never structure. Tier A (practitioner) never executed; Tier C (internal comparisons) void since the reset deleted what they compared against. |
| `docs/02-understanding/MERGED_BUSINESS_UNDERSTANDING.md` | FROZEN — superseded in role | The two sources reconciled, six conflicts resolved, eleven gaps recorded. **Traceability record**, not a working input. |
| `docs/03-discovery/DOMAIN_DISCOVERY.md` | FROZEN — superseded in role | Evidence against those gaps. Established the programme/case altitude split. **Traceability record.** |
| `docs/03-discovery/SCOPE_COVERAGE.md` | FROZEN — decision recorded | Found BL V1 §17 excludes half the Lead's end-to-end flow. Decision taken: model reality fully, sequence implementation separately. |
| `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | **FROZEN — ACTIVE** | The conceptual reference. The ontology derives from this. |
| `CLIENT_CONTEXT_UNVERIFIED.md` | QUARANTINED | Deployment context sourced to a client file not present in this repository. Not authoritative. Unresolved. |
| `docs/05-ontology/01-DOMAIN-PRIMITIVES.md` | **DRAFT — ACTIVE** | Step 1. Eight primitive categories, derivation trace, coverage test, ontology scope decision (§5A). Set **not closed**. |
| `docs/05-ontology/01a-PRIMITIVE-EVIDENCE-AUDIT.md` | **ACTIVE** | Evidence traceability audit for the primitive set. Defines the rating scale authoritative for both ontology phases. |
| `docs/05-ontology/02-ONTOLOGY-LAYERS.md` | **DRAFT — ACTIVE** | Step 2. Eight layers derived from the primitives. Five tensions carried open. |

**Superseded in role** means: the content stands and is correct, but ontology work reads the
reference model, not these. They exist so any statement in the reference model can be traced
back to its source. Do not extend them.

---

## Phase sequence

```
✅ Understand Business Logic V1
✅ Understand Client First Draft
✅ Merge into one coherent business understanding
✅ Discover remaining domain knowledge
✅ Domain Reference Model — what exists in humanitarian reality
   ↓
▶  ONTOLOGY DESIGN  ← current phase — docs/05-ontology/
      1. Domain Primitives          ◐ DRAFT — set not closed
      2. Layers                     ◐ DRAFT — 5 tensions carried open
           · Facets   · Entities · Relationships · Constraints
           · States   · Events   · Cognition     · Coordination
      3. Pillars
      4. Architecture Rules
      5. Ground Truth Reviews
      6. Evidence
      7. Governance
   ↓
   Business Architecture
   ↓
   AI Architecture
   ↓
   Ontology Engineering
   ↓
   Implementation
```

**Domain boundaries are no longer a separate phase.** The reference model §16 already
separates humanitarian reality from ontology scope from V1 implementation scope from roadmap.
What remains — deciding which of §§3–15 falls inside ontology scope — is the first act of
ontology design, performed as ontology work, not as another narrative document.

**From here, every artifact must become part of the ontology.** No narrative, explanatory,
philosophical, governance or summary documents.

---

## Standing rules

Five rules, each earned by a specific failure of the previous foundation.

1. **No document becomes authoritative by being written.** The previous repository promoted
   its own summaries to canonical status and derived 176,000 words from them without
   re-checking source. Authority is Tier 1; derivation is the reference model; nothing else
   acquires either by existing.

2. **No self-citation as evidence.** The deleted corpus was 171 files with zero external
   citations — it cited only itself. A document may not be its own warrant.

3. **No phase may be anticipated.** Design frameworks before the design phase, architecture
   before the ontology, vocabulary before primitives — all three happened, all three caused
   damage. Write things when the sequence reaches them.

4. **Structure follows reality, not process.** Registration, verification, case management
   and delivery are things actors *do*; they are not what exists. The previous foundation
   organised discovery around them and, in its own words, ended up where *"Registration &
   Identity holds a registry record; Case Management holds a workflow record. Neither holds a
   person."* Reference model §12 quarantines actions for this reason. **The ontology must not
   be organised around them.**

5. **Reality-membership does not imply scope-membership — and scope-exclusion does not imply
   unreality.** Donors are humanitarian actors; the Core Humanitarian Standard says so.
   Business Logic V1 §17 excludes them from V1 delivery. Both are true. The previous
   foundation collapsed these and opened a donor domain by overriding the source through an
   internal decision — the right instinct executed the wrong way. **Model reality fully;
   sequence implementation separately; change scope only by amending Tier 1.**

---

## Two things blocked outside this repository

**1. The primitive definition — RESOLVED from the lead's own sequence, open to reversal.**

A Domain Primitive is a **category of concept**, not a concrete irreducible. The prescribed
sequence builds a layer named *Entities* out of primitives; if *Person* were a primitive it
would be both the source of that layer and a member of it, and the derivation would be
circular. Reasoning and consequences: `docs/05-ontology/01-DOMAIN-PRIMITIVES.md` §1.

Stated here so it is visible and reversible. If the Project Lead intended the concrete
reading, step 1 must be redone and everything after it changes.

**2. Practitioner evidence — bounds what the ontology can honestly assert.**

Nothing in this repository has been validated by a humanitarian practitioner. Tier A was never
executed — structurally unavailable, not deferred. Sixteen questions are marked `[OPEN]` in
reference model §16.5; the load-bearing ones are identity resolution, how vulnerability
composes, family/household membership, and the values inside every dimension.

Business Logic V1's operational roles — Registrant, Proxy, Field Verifier, Human Reviewer,
Case Manager — are supported by nothing outside this project.

**Neither blocks ontology design from starting.** Both bound what it may claim.
