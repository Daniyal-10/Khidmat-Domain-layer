# Khidmat â€” Ontology Foundation

Repository reset 2026-07-29. Everything untraceable to an authoritative source was deleted.
**The foundation is complete and frozen. The current phase is ontology design.**

---

## Authority

Two tiers. They do different jobs and must not be confused.

### Tier 1 â€” Sources of fact (frozen, never edited)

| Document | Role |
|---|---|
| `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` | Primary authority on humanitarian facts. Where sources disagree, this wins. |
| `KHIDMAT_AI_BUSINESS_OVERVIEW.html` | Client First Draft. Vision and direction. |

Plus external humanitarian standards â€” OCHA, UNHCR, IASC, ICRC, Sphere/CHS, IOM, WHO â€” as
retrieved into `docs/01-evidence/`.

### Tier 2 â€” Source of derivation (frozen)

| Document | Role |
|---|---|
| `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | **The ontology derives from this document and nothing else.** |

The reference model does not outrank Tier 1 â€” it is built entirely from it, with every
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
| `docs/01-evidence/TD-01 â€¦ TD-06` | FROZEN | The only externally-sourced material in the project. Evidence, never structure. Tier A (practitioner) never executed; Tier C (internal comparisons) void since the reset deleted what they compared against. |
| `docs/02-understanding/MERGED_BUSINESS_UNDERSTANDING.md` | FROZEN â€” superseded in role | The two sources reconciled, six conflicts resolved, eleven gaps recorded. **Traceability record**, not a working input. |
| `docs/03-discovery/DOMAIN_DISCOVERY.md` | FROZEN â€” superseded in role | Evidence against those gaps. Established the programme/case altitude split. **Traceability record.** |
| `docs/03-discovery/SCOPE_COVERAGE.md` | FROZEN â€” decision recorded | Found BL V1 Â§17 excludes half the Lead's end-to-end flow. Decision taken: model reality fully, sequence implementation separately. |
| `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | **FROZEN â€” ACTIVE** | The conceptual reference. The ontology derives from this. |
| `CLIENT_CONTEXT_UNVERIFIED.md` | QUARANTINED | Deployment context sourced to a client file not present in this repository. Not authoritative. Unresolved. |
| `PRE-STAGE-5-OPEN-QUESTION-RESOLUTION-REGISTER.md` | **ACTIVE** | Final resolution pass closing all structural ontology-design questions prior to Stage 5. |
| `docs/05-ontology/01-DOMAIN-PRIMITIVES.md` | **DRAFT â€” ACTIVE** | Step 1. Seven primitive categories, derivation trace, coverage test. Structurally resolved; pending Stage 5/7. |
| `docs/05-ontology/02-ONTOLOGY-LAYERS.md` | **DRAFT â€” ACTIVE** | Step 2. Eight layers derived from the primitives. Structural tensions resolved; empirical dependencies marked. |
| `docs/05-ontology/03-ONTOLOGY-PILLARS.md` | **DRAFT â€” ACTIVE** | Step 3. Seven pillars derived from the layers |
| `docs/05-ontology/04-ARCHITECTURE-RULES.md` | **DRAFT â€” ACTIVE** | Step 4. Architecture rules governing ontology composition and extension. |

**Superseded in role** means: the content stands and is correct, but ontology work reads the
reference model, not these. They exist so any statement in the reference model can be traced
back to its source. Do not extend them.

---

## Phase sequence

```
âœ… Understand Business Logic V1
âœ… Understand Client First Draft
âœ… Merge into one coherent business understanding
âœ… Discover remaining domain knowledge
âœ… Domain Reference Model â€” what exists in humanitarian reality
   â†“
â–¶  ONTOLOGY DESIGN  â† current phase â€” docs/05-ontology/
      1. Domain Primitives          âœ… Structurally resolved; empirical validation and formal governance ratification pending
      2. Layers                     âœ… Structurally resolved; empirical validation and formal governance ratification pending
           Â· Facets   Â· Entities Â· Relationships Â· Constraints
           Â· States   Â· Events   Â· Cognition     Â· Coordination
      3. Pillars                    âœ… Structurally resolved; empirical validation and formal governance ratification pending
      4. Architecture Rules         âœ… UHR rules established for Stage 5/7 handling
      4a. Final Resolution Pass     âœ… All structural questions resolved (PRE-STAGE-5-OPEN-QUESTION-RESOLUTION-REGISTER.md)
      5. Ground Truth Reviews       (NOT YET GENERATED)
      6. Evidence
      7. Governance
   â†“
   Business Architecture
   â†“
   AI Architecture
   â†“
   Ontology Engineering
   â†“
   Implementation
```

**Domain boundaries are no longer a separate phase.** The reference model Â§16 already
separates humanitarian reality from ontology scope from V1 implementation scope from roadmap.
What remains â€” deciding which of Â§Â§3â€“15 falls inside ontology scope â€” is the first act of
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
   citations â€” it cited only itself. A document may not be its own warrant.

3. **No phase may be anticipated.** Design frameworks before the design phase, architecture
   before the ontology, vocabulary before primitives â€” all three happened, all three caused
   damage. Write things when the sequence reaches them.

4. **Structure follows reality, not process.** Registration, verification, case management
   and delivery are things actors *do*; they are not what exists. The previous foundation
   organised discovery around them and, in its own words, ended up where *"Registration &
   Identity holds a registry record; Case Management holds a workflow record. Neither holds a
   person."* Reference model Â§12 quarantines actions for this reason. **The ontology must not
   be organised around them.**

5. **Reality-membership does not imply scope-membership â€” and scope-exclusion does not imply
   unreality.** Donors are humanitarian actors; the Core Humanitarian Standard says so.
   Business Logic V1 Â§17 excludes them from V1 delivery. Both are true. The previous
   foundation collapsed these and opened a donor domain by overriding the source through an
   internal decision â€” the right instinct executed the wrong way. **Model reality fully;
   sequence implementation separately; change scope only by amending Tier 1.**

---

## Two things blocked outside this repository

**1. The primitive definition â€” RESOLVED from the lead's own sequence, open to reversal.**

A Domain Primitive is a **category of concept**, not a concrete irreducible. The prescribed
sequence builds a layer named *Entities* out of primitives; if *Person* were a primitive it
would be both the source of that layer and a member of it, and the derivation would be
circular. Reasoning and consequences: `docs/05-ontology/01-DOMAIN-PRIMITIVES.md` Â§1.

Stated here so it is visible and reversible. If the Project Lead intended the concrete
reading, step 1 must be redone and everything after it changes.

**2. Practitioner evidence â€” bounds what the ontology can honestly assert.**

Nothing in this repository has been validated by a humanitarian practitioner. Tier A was never
executed â€” structurally unavailable, not deferred. Sixteen questions are marked `[OPEN]` in
reference model Â§16.5; the load-bearing ones are identity resolution, how vulnerability
composes, family/household membership, and the values inside every dimension.

Business Logic V1's operational roles â€” Registrant, Proxy, Field Verifier, Human Reviewer,
Case Manager â€” are supported by nothing outside this project.

**Neither blocks ontology design from starting.** Both bound what it may claim.
