# Khidmat — Ontology Foundation

This repository was reset on 2026-07-29. Everything that could not be traced to an
authoritative source was deleted. It is being rebuilt from first principles.

---

## Authoritative sources

Exactly two documents carry authority. Where anything disagrees with them, they win.
Where they disagree with each other, **Business Logic V1 wins**.

| Document | Role |
|---|---|
| `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` | Primary authority. The business specification. |
| `KHIDMAT_AI_BUSINESS_OVERVIEW.html` | Client First Draft. Vision and direction. |

These two files are **frozen**. They are inputs, not working documents. Do not edit them.

No other document in this repository has authority. Nothing may be cited as a warrant
unless it traces to one of the two above, or to an external source named in the evidence
dossiers below.

---

## What else is here, and why

### `docs/01-methodology/discovery/TD-01` … `TD-06`

Six evidence dossiers. These are the **only material in the project sourced from outside
the project itself** — OCHA, UNHCR, Sphere / Core Humanitarian Standard, IASC cluster
documentation, and peer-reviewed humanitarian-studies literature, each with citations,
confidence levels, corroboration counts, and honest single-source flags.

They are retained as **evidence, never as structure**. They record what the humanitarian
sector says. They do not decide how Khidmat models it, and no conclusion in them may be
promoted into the ontology without re-entering through the phase sequence below.

Their Tier A layer (practitioner elicitation) was never executed. That limitation is
stated in each dossier and still stands.

### `CLIENT_CONTEXT_UNVERIFIED.md`

Deployment context that appears in neither authoritative source. **Not authoritative.**
See the file for the open question attached to it.

---

## Phase sequence

No phase may start before the previous one is complete.

```
Phase 0   Understand Business Logic V1
          Understand Client First Draft
          Merge both into one coherent business understanding
             ↓
          Discover remaining domain knowledge
             ↓
          Freeze domain boundaries
             ↓
          Discover Domain Primitives
             ↓
          Validate primitives
             ↓
          Design Ontology Map
             · Facets      · Entities   · Relationships  · Constraints
             · States      · Events     · Cognition      · Coordination
             ↓
          Business Architecture
             ↓
          AI Architecture
             ↓
          Ontology Engineering
             ↓
          Implementation
```

**Current position: Phase 0, not started.**

---

## Standing rules

These exist because the previous foundation failed by violating them.

1. **No document becomes authoritative by being written.** The previous repository
   promoted its own derived summaries to canonical status and then derived 176,000 words
   from them without re-checking source. Authority comes from the two files above and
   nowhere else.
2. **No self-citation as evidence.** The deleted discovery corpus contained 171 files and
   zero external citations — it cited only itself. A document may not be its own warrant.
3. **No phase may be anticipated.** Design frameworks written before the design phase,
   architecture written before the ontology, and vocabulary written before primitives all
   caused the previous failure. Write things when the sequence reaches them.
4. **Structure follows reality, not process.** Business Logic V1 organises humanitarian
   reality by model — Human, Family, Household, Community, Needs, Vulnerability, Risk,
   Support, Outcome. The previous foundation reorganised it by operational function
   (registration, casework, logistics, evaluation) and consequently described the
   processes applied to people without ever describing the people.
5. **Scope exclusions are binding.** Business Logic V1 §17 excludes the donor and
   resource-supply side, resource allocation at scale, predictive engines, and runtime
   orchestration. The previous foundation built discovery domains for several of these
   anyway, via internal decisions that overrode the source document.

---

## Open ruling required before primitives

"Domain Primitive" has been used two incompatible ways, and the entire ontology derives
from which is meant:

- **as a concrete irreducible of reality** → admits *Person*, *Household*, *Need*
- **as a category of concept** → admits *Identity*, *Relation*, *Condition*, and rejects
  *Person* as too concrete to sit above a layer named Entities

This was previously decided unilaterally inside a working document. It needs an explicit
ruling from the Project Lead before primitive discovery begins.
