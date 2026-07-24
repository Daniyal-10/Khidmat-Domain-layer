# Blueprint: Humanitarian Business Reference Model (HBRM)

**Type:** Discovery & authoring blueprint (not the Reference Model itself)
**Governs the future authoring of:** `docs/01-methodology/HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md`
**Depends on:** `BUSINESS_MASTER_PLAN.md` (frozen, all 9 chapters), `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md`, `BUSINESS_MASTER_PLAN_RESOLUTION.md`, `BUSINESS_MASTER_PLAN_RESEARCH_BACKLOG.md`, `BUSINESS_MASTER_PLAN_FREEZE_CERTIFICATION.md`
**Status:** Draft — architecture-review Required Changes applied per `HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT_RESOLUTION.md`; pending freeze decision

---

## 1. Purpose

### Why the HBRM exists

The Business Master Plan (BMP) answers *how humanitarian work functions as a business domain* — nine chapters of continuous, reasoned narrative in which every concept is introduced in the context of the question it answers, cross-referenced against neighboring concepts, and explained through "why it exists" reasoning. That narrative form is exactly right for building shared understanding once. It is the wrong form for repeated citation. A Business Architecture author who needs the precise definition of "Household" has to locate it inside Chapter 1's prose about the person or household in need; a Domain Discovery author checking whether a proposed new domain duplicates an existing concept has to re-read relevant fragments of up to nine chapters to be sure. As the number of documents depending on the BMP grows — Business Architecture, Domain Discovery, Ontology Design, and eventually the ontology layer itself — re-deriving definitions from narrative each time is exactly the failure mode this repository's own `ontology_authority_matrix.md` and ADR-008 (Single Ownership of Concepts) already exist to prevent, one layer down. The HBRM exists to prevent the same failure one layer up: it is the *first* place in the documentation stack where "define exactly once, reference everywhere else" becomes an enforced discipline for business concepts, not just ontology concepts.

### What questions the HBRM must answer

- What stable business concepts does the BMP's narrative already establish?
- What is the single, canonical, citable definition of each one?
- How does each concept relate to the others — what is broader, narrower, related, or dependent?
- What structural business facts (not ontology cardinality, not eligibility rules) does the BMP already state about each concept, that a downstream author needs without re-deriving?
- Where the BMP itself drifted in terminology for the same underlying idea (flagged in `BUSINESS_MASTER_PLAN_RESEARCH_BACKLOG.md`, Workstream F), what is the one canonical term, and what are its recorded aliases?

### What the HBRM must never do

Invent a business concept the BMP did not already establish. Resolve a business question the BMP or the Research Backlog left open. Assign a concept to an organization, actor, or system. Sequence concepts into a process, workflow, or lifecycle narrative. Any of these would either duplicate a downstream document's job (Business Architecture, Domain Discovery) or duplicate the BMP's own already-frozen narrative job.

### Audience

- **Primary:** authors of Business Architecture and Domain Discovery, who need to cite precise, stable concept definitions without re-reading BMP narrative.
- **Secondary:** the eventual author of Ontology Design, for whom every HBRM entry is a candidate input to the promotion test that decides whether a business concept becomes an ontology entity, value object, role, or taxonomy concept.
- **Tertiary:** any future reviewer or AI collaborator (per `AI_WORKFLOW.md`'s roles) needing to check whether a proposed new concept already exists under a different name before proposing it as new.

### How future documents depend on it

Business Architecture cannot responsibly assign capabilities, governance authority, or actor responsibilities without a stable list of exactly what those capabilities, authorities, and actors *are* — the HBRM supplies that list so Business Architecture's job is assignment, not re-definition. Domain Discovery cannot decide whether a newly proposed humanitarian domain is genuinely new without a canonical concept boundary to test against — the HBRM is that boundary. Ontology Design cannot begin selecting candidate concepts for formal modeling without a deduplicated, business-pure list to select from — the HBRM is the raw material Ontology Design applies its own promotion test to, exactly as `Canonical_Ontology_Schema.md` §17 already applies a promotion test to distinguish Value Objects from Entities one layer further downstream.

---

## 2. Scope

### What belongs inside the HBRM

- Exactly one canonical entry for every stable, named business concept already established across BMP Chapters 1–9: actor and role types (Ch1), stakeholder interests and named tensions (Ch2), lifecycle-stage concepts (Ch3, as named stopping points — not the sequence itself), capabilities (Ch4), business-service and value-stream concepts (Ch5), intervention categories (Ch6), operational objectives (Ch7), governance and authority-boundary concepts (Ch8), and the universal/variable discipline and named variation dimensions (Ch9).
- The relationships already stated or clearly implied between these concepts in BMP narrative (e.g., Chapter 4's explicit statement that Verification is "narrower than Situational Understanding").
- Business-level structural facts already stated in the BMP (e.g., "a household may have more than one concurrent need," Chapter 1 §1.1) — recorded as business rules, not as ontology cardinality.
- A resolved, single canonical term for any concept the BMP itself named inconsistently (the terminology-reconciliation items in Research Backlog Workstream F, notably RB-F7), with the alternate terms recorded as aliases.
- For Tension concepts (Chapter 2) and Business Service concepts (Chapter 5) specifically: both remain first-class, standalone Concept Types — each is independently named and reasoned about in the BMP text — but because both are inherently relational (a tension is a pull between two interests; a service is a handoff between two capabilities), each entry of these two types must structurally record that relational nature rather than leave it implicit. A Tension entry must populate its Related Concepts field with exactly the interests or objectives it names as being in tension, labeled "in tension with." A Business Service entry must populate the Type-Specific Handoff field (§6). This is mandatory for these two Concept Types, not optional.

### What does NOT belong inside the HBRM

- Any concept not traceable to specific, already-ratified BMP content. If a downstream author believes a concept is missing — e.g., "Consent," flagged as RB-F2 — the correct action is to route that back to a future BMP amendment; only once that amendment is itself governance-approved does the concept become eligible for an HBRM entry. The HBRM formalizes; it does not invent, and no "Provisional" entry may be added as a workaround while a concept's BMP amendment is still pending.
- Narrative reasoning of *why* a concept exists or matters — that reasoning stays in the BMP and is cited by section reference, not reproduced.
- The lifecycle sequence itself (BMP Chapter 3's stage-to-stage flow), any workflow, process diagram, or state machine.
- Priority ordering, eligibility rules, decision-rights assignment, or actor-to-capability assignment — every one of these was deliberately deferred by the BMP itself (Research Backlog Workstream D) and remains deferred to Business Architecture.
- Implementation, software, database, API, UI, AI, or engineering-architecture content of any kind.
- Ontology terminology or ontology-shaped structure: no entity/class syntax, no `cardinality: {min, max}` notation, no datatype declarations, no CURIEs, no YAML. An HBRM concept is a candidate for later ontology modeling, not a pre-formatted ontology row.
- Localization strategy or regional/cultural aliasing mechanics — BMP Chapter 9 already establishes the discipline for recognizing variation; encoding *how* that variation is technically represented is Ontology Design's and the existing `ADR-022` canonical-concepts-and-regional-localization pattern's job, not the HBRM's.

### Relationship to the Research Backlog

The Research Backlog (`BUSINESS_MASTER_PLAN_RESEARCH_BACKLOG.md`) is the canonical record of unresolved business questions. The HBRM's relationship to it is strictly one of **citation, not resolution**:

- **Blocking items:** none. No backlog item blocks HBRM authoring from starting or finishing, because the HBRM's job is to formalize concepts the BMP *already* states, and no backlog item withholds content the BMP already contains. Even RB-C1 (the missing programme-validated intervention catalogue, Critical priority) does not block the HBRM — Chapter 6's eight intervention *categories* are fully stated in the BMP and can be formalized now; the missing catalogue is what would sit *inside* each category operationally, which is Business Architecture/Programs-domain content, not an HBRM concept.
- **Cited, not consumed:** where an HBRM entry corresponds to a concept with an open backlog item (e.g., the entry for "Intervention Category" cites RB-C1; entries touching religiously-obligated giving cite RB-B1–B3), the entry must reference the backlog ID and carry a **Provisional** status (see §6), signaling to downstream readers that the concept is stable enough to define but not yet validated to the depth the backlog item calls for.
- **Terminology items are the one exception, and are consumed, not merely cited:** Workstream F's terminology-reconciliation items (chiefly RB-F7 — "capacity" overloading, "resilience" vs. "capacity to cope," lifecycle-stage/capability naming mismatch) are exactly the kind of decision the HBRM exists to make. Resolving *which term is canonical* is a naming decision internal to building a reference catalog, not a business-content decision requiring the BMP to be reopened. The HBRM is the correct and intended place to close these items — but closing one requires an individual verification pass, not a blanket presumption of synonymy. Re-reading the actual BMP text for each candidate must produce exactly one of three outcomes: **Alias** (confirmed, the two terms name the same concept — record one canonical name, the other as an alias), **Broader/Narrower** (the terms name related but distinct concepts, one specializing or building on the other — record both as separate entries, linked), or **Unrelated** (no merge or link warranted). "Resilience" (BMP Ch7 §7.7) and "capacity to cope" (BMP Ch1 §1.1, Ch3 §3.1) are a caution against assuming Alias too quickly, not a confirmed example of one: Chapter 7's usage explicitly adds a forward-looking, comparative dimension ("requires less external assistance than it did before") that Chapter 1's present-tense framing never asserts — on the evidence in the BMP text, this pair is more likely Broader/Narrower (capacity to cope as the base concept; resilience as the narrower, improvement-trajectory concept built on it) than a simple Alias.
- **Explicitly deferred to later documents:** Workstream D (deliberately-deferred items: priority ordering, eligibility, decision-rights, actor-to-capability assignment) and Workstream E (process-trigger mechanisms) are not the HBRM's concern at all — they are Business Architecture's inputs, and the HBRM should not attempt to anticipate their resolution even by implication (e.g., an HBRM relationship must never imply a priority ordering between two concepts that the BMP left unranked).

---

## 3. Responsibilities

The HBRM is responsible for:

1. **Extraction** — identifying every stable, named concept in BMP Chapters 1–9.
2. **Deduplication** — recognizing where the BMP used more than one term for the same underlying concept, and resolving each Workstream F candidate individually to one of Alias, Broader/Narrower, or Unrelated (per §2 above), never presuming synonymy by default.
3. **Definition** — stating each concept's meaning exactly once, in business language, traceable to its BMP origin.
4. **Relationship mapping** — recording the broader/narrower, related, and dependency relationships the BMP already states or clearly implies between concepts.
5. **Business-rule capture** — recording structural business facts the BMP already states (e.g., cardinality-like facts, mutual-exclusivity facts, combination facts) in business language, without pre-empting how a later ontology might formally encode them.
6. **Traceability maintenance** — ensuring every entry cites its BMP origin and, where relevant, its Research Backlog cross-reference.
7. **Status honesty** — marking which entries are stable versus provisional, so the catalog's format (which looks authoritative) never overstates the underlying content's maturity (a specific, named risk in §11).

The HBRM is explicitly **not** responsible for: assigning concepts to actors or organizations; sequencing concepts into process; ranking, prioritizing, or resolving any tension or trade-off; inventing concepts absent from the BMP; or producing ontology-shaped output.

---

## 4. Relationship to Existing Documents

### The full dependency chain and the contract at each boundary

```
Project Overview
   (informal, evolving statement of current understanding — no concept authority)
        ↓
Business Master Plan
   (canonical narrative description of humanitarian business reality — concepts
    established informally, in prose, with reasoning and cross-reference)
        ↓
Humanitarian Business Reference Model  ← this blueprint's subject
   (canonical, deduplicated, structured catalog of the stable business concepts
    the BMP establishes — each defined exactly once, related to the others, with
    no reasoning reproduced and no organizational or ontological assignment made)
        ↓
Business Architecture
   (maps HBRM concepts onto organizational structures, roles, and operational
    responsibility — decides who/what exercises a capability, holds an authority
    boundary, or is accountable for a governance decision)
        ↓
Domain Discovery
   (the methodology for recognizing when a new humanitarian business domain is
    genuinely new, using HBRM's concept boundaries as the test for "already
    covered" versus "genuinely novel")
        ↓
Ontology Design
   (the methodology for deciding which HBRM concepts, and in what shape —
    Entity, Value Object, Role, taxonomy concept, per `Canonical_Ontology_
    Schema.md` §§17–20 — become candidates for formal ontology modeling)
        ↓
Ontology Engineering
   (the actual authoring of entities.yaml, taxonomy files, and reasoning rules —
    already substantially mature in this repository; HBRM concepts become
    candidate inputs here, subject to further splitting, merging, or
    specialization as ontology-modeling discipline requires)
```

### The specific contract between the BMP and the HBRM

The BMP is the *source*; the HBRM is a *derived index* over it. Every HBRM entry must be traceable to specific BMP content. The HBRM never contains a claim the BMP does not already support, with the single named exception of terminology reconciliation (§2, §6), which changes labels, not meaning. The HBRM never re-argues *why* something exists — it cites the BMP section that already made that argument.

### The specific contract between the HBRM and Business Architecture

The HBRM defines *what exists as a concept and how concepts relate*. Business Architecture defines *who or what organizational structure performs, owns, holds authority for, or is accountable for it*. Business Architecture must reference HBRM concepts by their canonical name; it must never redefine one, mirroring the "Reference-Not-Redefine" rule this repository's `ARCHITECTURE.md` already enforces between ontology domains.

### The specific contract between the HBRM and Ontology Design

The relationship mirrors the one this repository already has internally between the Business Master Plan / Reference Model layer and the ontology layer's own Value-Object/Entity/Role promotion test (`Canonical_Ontology_Schema.md` §§17–20): the HBRM supplies well-defined, deduplicated candidate concepts; Ontology Design decides, concept by concept, what formal shape (if any) each one takes. An HBRM concept is not entitled to become an ontology entity merely by existing in the HBRM — that determination belongs entirely to Ontology Design, exactly as a Value Object is not entitled to become an Entity merely by having attributes.

---

## 5. Architectural Principles

1. **Define exactly once.** Every concept has exactly one canonical entry. This is the HBRM's central discipline, and the direct business-layer analogue of ADR-008 (Single Ownership of Concepts) at the ontology layer.
2. **Reference, don't narrate.** Every entry cites its BMP origin instead of reproducing the reasoning found there. If an entry's "Business Meaning" field starts to read like a chapter summary, it has drifted out of scope.
3. **No storytelling, no workflow, no sequence.** The HBRM catalogs the *stopping points* BMP Chapter 3 named (as concepts) without reproducing the *flow between* them (which stays Chapter 3's job, cited not repeated).
4. **No assignment.** No concept is linked to an actor, organization, or system. That is Business Architecture's exclusive responsibility.
5. **No ontology shape.** No entry uses cardinality notation, datatype declarations, CURIEs, or any structure that anticipates a specific ontology-engineering encoding. Business rules are stated in plain business language.
6. **Stability over completeness.** The template and chapter structure must accommodate new concepts (from a future BMP amendment or a newly-discovered domain) without reorganization. Completeness of the *current* catalog is explicitly not claimed anywhere (§9, §11).
7. **Status honesty.** A reference document's format tends to read as more authoritative than a narrative document's, regardless of actual content maturity. The HBRM must counteract this actively (via the Status field, §6) rather than let its format oversell its content.
8. **The litmus test carries forward unchanged.** Every HBRM entry must remain true in a world where Khidmat AI never existed — the same test the BMP blueprint established, applied one layer up.

---

## 6. Canonical Concept Template

The example field list in the task prompt (Name, Definition, Purpose, Business Meaning, Relationships, Parent Concepts, Child Concepts, Inputs, Outputs, Constraints, Business Rules, Dependencies, Related Concepts, Notes) was evaluated field by field rather than adopted wholesale. The reasoning:

- **"Purpose" and "Business Meaning" are redundant with each other** once "Definition" is precise — a single "Business Meaning" field (a short, one-to-two-sentence *why this matters*, citing the BMP rather than re-arguing it) replaces both.
- **"Inputs" and "Outputs" are not universal.** They are meaningful for Business Services and Capabilities (Chapter 5's entire framing is input/output handoffs) but meaningless for an Actor, a Tension, or an Operational Objective. Rather than force every entry to carry empty Inputs/Outputs fields, this blueprint proposes a **type-specific field**, populated only for concept types where it is meaningful, and folded into Related Concepts otherwise.
- **"Constraints" and "Business Rules" are the same thing under two names** — merged into one field, "Business Rules," to avoid an artificial distinction.
- **"Relationships" as a generic field is too coarse** given the BMP itself distinguishes several relationship kinds (broader/narrower, distinct-from, depends-on) — these are separated into distinct fields below so the distinction is queryable, not buried in prose.
- **A field the example list omits but the BMP's own writing pattern requires: "Distinct From."** Nearly every BMP chapter explicitly states what a concept is *not* (e.g., Chapter 4's "distinct from neighboring capabilities" subsections). This is load-bearing content, not incidental — it gets its own field rather than being folded into Notes.
- **A field the example list omits but this blueprint's own traceability requirement demands: "Origin" and "Backlog Cross-Reference."** Without these, the HBRM cannot honor its own architectural principle of citing rather than re-arguing.
- **A field this blueprint adds for status honesty: "Status."**

### Proposed template

| Field | Required? | Meaning |
|---|---|---|
| **Concept ID** | Yes | A stable, human-readable short identifier (not an ontology-style machine identifier) used for cross-referencing within the HBRM and by downstream documents. Must be globally unique across the entire HBRM catalog, not merely unique within its own chapter — no CURIE or namespace-prefix mechanism is used at this layer, a flat global-uniqueness rule is sufficient. Checked continuously against a running Concept ID registry maintained throughout authoring (§12), not only in the end-of-document duplication pass (§9). |
| **Canonical Name** | Yes | The one name this concept is known by throughout the HBRM and all documents that cite it. |
| **Concept Type** | Yes | Which of the nine BMP-chapter-derived categories (or the Core/Foundational category, §7) this concept belongs to — itself a stable, closed vocabulary (see §7). |
| **Definition** | Yes | One precise, business-level statement of what this concept is. The single canonical statement a downstream document should quote. |
| **Business Meaning** | Yes | One to two sentences on why this concept matters, citing (not repeating) the BMP section that argues it. |
| **Origin** | Yes | The specific BMP chapter and section this concept is drawn from. Mandatory — an entry with no origin cannot exist in the HBRM per §2. |
| **Broader Concept** | Optional | The concept, if any, that this one specializes (e.g., a specific funder category specializing "Donor and Funder"). |
| **Narrower Concepts** | Optional | The concepts, if any, that specialize this one — the inverse of Broader Concept, recorded on the broader entry rather than duplicated. |
| **Related Concepts** | Optional in general; **mandatory for Tension entries** (§2) | Concepts commonly discussed alongside this one in the BMP, without a broader/narrower relationship. For a Tension entry, this field must name exactly the interests or objectives it describes as being in tension, labeled "in tension with." |
| **Depends On** | Optional | Concepts that must be understood before this one is meaningful, mirroring the dependency logic every BMP chapter's own "why this chapter exists" section already used. |
| **Distinct From** | Optional but recommended | Explicit statements of non-equivalence, drawn from the BMP's own "distinct from neighboring X" pattern — prevents future conflation. |
| **Business Rules** | Optional | Structural business-level facts the BMP states about this concept (e.g., cardinality-like or combination facts), stated in plain language with no ontology notation. |
| **Type-Specific Handoff** (Inputs/Outputs) | **Mandatory for Business Service entries** (§2); optional for Capability entries; not applicable to other concept types | What this concept depends on receiving, and what it produces for another concept to depend on — directly derived from Chapter 5's business-service framing, not a generic field. |
| **Aliases** | Optional | Alternate terms the BMP itself used for this concept, recorded here as the terminology-reconciliation resolution (§2). |
| **Status** | Yes | `Stable` or `Provisional` (see below). |
| **Backlog Cross-Reference** | Optional | The Research Backlog ID(s), if any, bearing on this concept — cited, never resolved. |
| **Notes** | Optional | Minimal, non-narrative clarifications that do not fit any field above. |

**Status values, defined:**
- **Stable** — the concept is clearly and singularly defined in the BMP, with no open backlog item bearing directly on its definition or boundaries.
- **Provisional** — the concept is defined well enough to catalog, but a Research Backlog item (most commonly from Workstream A, the domain-expert validation program, or Workstream C, the intervention catalogue) bears directly on its completeness or boundaries. A Provisional entry is not a lesser-quality entry — it is an honestly-flagged one.

---

## 7. Proposed Chapter Structure

The BMP's own nine chapters, each producing one recognizable "kind" of concept, are the natural basis for the HBRM's chapter structure — but one addition is warranted and is proposed here on the strength of a direct architectural analogy already present in this repository.

**Proposed addition: a Chapter 0, "Core and Foundational Concepts."** Several concepts recur across nearly every BMP chapter without being "owned" by any single one — Person, Household, Need, Community, Assistance. This is structurally the same problem this repository's own ontology layer already solved with its `shared/` bounded context (ADR-007, ADR-018): concepts used by many domains, owned exclusively by none, are given their own first-class home rather than being duplicated or arbitrarily attached to whichever domain happens to use them most. Chapter 0 is the HBRM's business-layer equivalent of `shared/`.

| Chapter | Purpose | Scope | Dependencies | Inputs | Outputs | Relationship to BMP | Relationship to later documents |
|---|---|---|---|---|---|---|---|
| **0 — Core and Foundational Concepts** | Catalog the primitive nouns referenced throughout the BMP that no single chapter exclusively owns | Person, Household, Need, Community, Assistance, and any concept that the already-frozen BMP itself references by name across three or more of its own nine chapters — a fact checkable in full, today, by rereading the BMP, since the BMP (unlike the still-being-authored HBRM) is complete and will not change | None (entry point) | BMP Chapters 1, 3 (primary sources for these nouns) | Foundational entries every later chapter references | Formalizes recurring nouns, does not narrate them | Every downstream document's most-cited entries |
| **1 — Actors and Roles** | Catalog actor and role-type concepts | BMP Chapter 1's actor categories | Chapter 0 (Person, Household) | BMP Ch1 | Actor/role concept entries | Direct formalization of Ch1 | Business Architecture's assignment targets |
| **2 — Interests and Tensions** | Catalog stakeholder interests and named tensions | BMP Chapter 2's interests and the eight named tensions | Chapter 1 (interests belong to actors) | BMP Ch2 | Interest and tension concept entries | Direct formalization of Ch2 | Input to Business Architecture's (still-deferred) prioritization work |
| **3 — Lifecycle Concepts** | Catalog the named lifecycle stopping-points as concepts, not as a sequence | BMP Chapter 3's ten named stages, as concepts | Chapter 0 (Need) | BMP Ch3 | Lifecycle-stage concept entries (no flow) | Formalizes stage *names and meanings*; the *sequence itself* stays in Ch3, cited not reproduced | Domain Discovery (checking whether a new domain introduces a genuinely new stage) |
| **4 — Capabilities** | Catalog the thirteen business capabilities | BMP Chapter 4 | Chapter 3 (capabilities enable lifecycle stages) | BMP Ch4 | Capability concept entries, including Type-Specific Handoff fields | Direct formalization of Ch4 | Business Architecture's assignment targets; Ontology Design's candidate list |
| **5 — Business Services and Value Streams** | Catalog named business services and the five value-stream patterns | BMP Chapter 5 | Chapter 4 (services are capability handoffs) | BMP Ch5 | Service and value-stream concept entries | Direct formalization of Ch5 | Domain Discovery (checking whether a proposed domain's value creation is already covered) |
| **6 — Intervention Categories** | Catalog the eight intervention categories | BMP Chapter 6 | Chapter 5 (categories align with value-stream outcomes) | BMP Ch6 | Intervention-category concept entries, marked Provisional per RB-C1 | Direct formalization of Ch6 | Business Architecture / Programs domain (still awaiting the operational catalogue) |
| **7 — Operational Objectives** | Catalog the ten operational objectives and named trade-offs | BMP Chapter 7 | Chapters 4, 6 (objectives are what capabilities/categories exist to achieve) | BMP Ch7 | Objective concept entries | Direct formalization of Ch7 | Future outcome-indicator vocabulary (explicitly out of scope here, per BMP Ch7's own constraint) |
| **8 — Governance and Authority Concepts** | Catalog the seven governance boundaries | BMP Chapter 8 | Chapters 1, 2 (boundaries reflect actor interests) | BMP Ch8 | Authority-boundary concept entries | Direct formalization of Ch8 | Business Architecture's primary input |
| **9 — Cross-Cutting Principles and Variation Discipline** | Catalog the universal/variable test itself as a reusable concept, and the eight named variation dimensions | BMP Chapter 9 | All prior chapters (a cross-cutting check) | BMP Ch9 | The discipline itself as a citable concept; variation-dimension entries | Direct formalization of Ch9 | Ontology Design's regional-localization work (building on, not duplicating, `ADR-022`) |

**Extensibility check:** a plausible future addition — for example, a new concept surfaced once Domain Discovery activates a new humanitarian domain — has a clear home under this structure without reorganization: it either extends an existing chapter's catalog (most likely) or, if genuinely foundational and cross-cutting, is added to Chapter 0. No chapter boundary needs to shift to accommodate growth.

Two non-concept-catalog sections are also required, sitting outside this numbered structure: a short front-matter **"How to Use This Reference"** section (not a concept chapter — a usage guide, analogous to the BMP's own opening authoring-status note), and a closing **alphabetical Concept Index** cross-referencing every Concept ID and Canonical Name across all ten chapters, since a reference document without an index defeats its own purpose.

---

## 8. Dependency Chain

Restated concisely from §4, with the specific gating condition at each boundary:

```
Business Master Plan (frozen, Ch1–9)
   ↓  [gate: every HBRM entry must trace to specific BMP content]
Humanitarian Business Reference Model
   ↓  [gate: Business Architecture may cite HBRM entries by Concept ID; may not redefine them]
Business Architecture
   ↓  [gate: Domain Discovery tests new-domain proposals against HBRM's existing concept boundaries]
Domain Discovery
   ↓  [gate: Ontology Design applies its own promotion test to HBRM entries as candidates, per
        Canonical_Ontology_Schema.md §§17–20]
Ontology Design
   ↓  [gate: Ontology Engineering implements only what Ontology Design has approved]
Ontology Engineering
```

No dependency in this chain is circular: the HBRM depends only on the BMP (already frozen); nothing later in the chain is permitted to modify an earlier document, mirroring the acyclic-dependency rule this repository's `ARCHITECTURE.md` already enforces between ontology domains.

---

## 9. Definition of Done

The HBRM is complete when:

1. Every concept named across BMP Chapters 1–9 has exactly one HBRM entry, or is explicitly recorded as an Alias of another entry (terminology reconciliation).
2. No two entries define the same underlying concept under different Concept IDs (checked via a deliberate duplication pass across the whole catalog, not chapter by chapter).
3. Every entry's Origin field cites specific, already-ratified BMP chapter/section content; no entry exists without one, and no entry cites a pending or hypothetical future BMP amendment as its Origin.
4. No entry contains ontology notation, software/implementation language, workflow/process sequencing, or organizational assignment (a purity scan equivalent to the one `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md` ran against the BMP must be run against the HBRM before it is considered done).
5. Every entry bearing on an open Research Backlog item cites that item's ID and carries `Status: Provisional`; no Provisional entry is presented with the same apparent authority as a Stable one without the status marker visible.
6. The terminology-reconciliation items in Research Backlog Workstream F (specifically RB-F7) are resolved within the HBRM's Aliases fields, with both/all prior terms retained as cross-referenced aliases rather than silently dropped.
7. The closing Concept Index is complete and every Concept ID in it resolves to exactly one entry.
8. A reviewer who has read the BMP once can locate any concept's precise definition in the HBRM without re-reading BMP narrative, and confirm that definition's Origin traces back correctly.
9. Every finalized Canonical Name has been checked against `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`'s named vocabulary (its Human, Family, Household, Needs, Risk, Support, and Outcome Models) for label collision. Where a collision exists, the HBRM entry is disambiguated (a more specific Canonical Name, or an explicit Notes-field cross-reference clarifying the distinction). V1 Blueprint is consulted only for this collision check — it is never treated as a source from which the HBRM derives new concepts, and it is not added to the dependency chain in §4/§8.

---

## 10. Open Questions

1. **Status-and-versioning depth.** Should HBRM entries eventually adopt a fuller status/versioning discipline analogous to the ontology layer's `status: active | placeholder | draft | deprecated` and `owl_version_iri` conventions (`Canonical_Ontology_Schema.md` §12), or does the lighter Stable/Provisional distinction proposed in §6 suffice at the business-reference layer? This affects how much governance overhead the HBRM carries before Ontology Design even begins.
2. **Ratification of terminology reconciliation.** Should the specific terminology choices made under §2/§6 (e.g., "resilience" vs. "capacity to cope" as the canonical term) be treated as purely editorial HBRM-internal decisions, or should each be recorded as a small governance decision (in the style of an ADR) given the BMP itself is frozen and cannot be edited to match retroactively? This blueprint leans toward "editorial, recorded as Aliases" but flags the question rather than deciding it, since it touches the same frozen-document boundary `BUSINESS_MASTER_PLAN_RESOLUTION.md` already had to navigate once.
3. **Chapter 0's status as a genuinely new structural element.** This blueprint proposes a Core/Foundational Concepts chapter not explicitly requested in the task's example structure, justified by direct analogy to this repository's own `shared/` bounded context. Should this addition be ratified as-is, or should foundational concepts instead be distributed into whichever existing chapter uses them most, to keep the HBRM's structure a stricter mirror of the BMP's own nine chapters?
4. **Granularity of the Type-Specific Handoff field.** §6 proposes limiting Inputs/Outputs-style content to Business Service and Capability concept types. Should Governance and Authority concepts (Chapter 8) also carry a comparable field, given each governance boundary in BMP Chapter 8 explicitly states "what belongs here" and implicitly what it hands upward on escalation? This blueprint leans toward "no, fold into Business Rules" but the question is open.

**Resolved:** Whether mid-authoring concept requests (e.g., Business Architecture identifying a concept the BMP implies but never names, such as Research Backlog items RB-F2 "Consent" or RB-F3 "Voluntary Withdrawal") may bypass the BMP and enter the HBRM directly is no longer open. Per `HUMANITARIAN_BUSINESS_REFERENCE_MODEL_BLUEPRINT_RESOLUTION.md`, such a request must always route back through a formal, governance-approved BMP amendment first; the HBRM may never add an entry — Provisional or otherwise — lacking a traceable, already-ratified BMP origin (see §2, §9).

---

## 11. Risks

1. **Ontology creep.** The HBRM's structured template (IDs, typed relationship fields, business rules) structurally resembles the ontology layer's `entities.yaml`/`data-properties.yaml` shape. An author under time pressure could drift toward encoding disguised cardinalities or datatype-like distinctions as "Business Rules." *Mitigation:* the Definition of Done's purity scan (§9, item 4) must specifically check for cardinality-notation-shaped language, not only for the word "ontology" itself.
2. **Narrative leakage.** "Business Meaning" fields could balloon into chapter summaries, recreating the BMP inside the HBRM. *Mitigation:* an explicit length/content discipline at authoring time (§12), checked in the purity scan.
3. **Premature completeness claims.** A reference-document format reads as more authoritative than narrative prose, even when the underlying content (per Research Backlog Workstream A) is explicitly non-exhaustive. A reader could mistake "the HBRM has ten operational-objective entries" for "there are exactly ten operational objectives in humanitarian work." *Mitigation:* the Status field (§6) plus a prominent front-matter disclaimer in the "How to Use This Reference" section (§7), stated as plainly as the BMP's own chapter-level non-exhaustiveness flags.
4. **Silent concept invention.** An author trying to make the catalog feel complete could add a concept that "seems obviously needed" (Consent, fraud/misrepresentation — both already identified in Research Backlog Workstream F) without it actually tracing to BMP content. *Mitigation:* the mandatory Origin field (§6) makes this mechanically difficult — an entry with no traceable Origin is a Definition-of-Done failure, not a judgment call.
5. **Terminology reconciliation overreach.** A reconciliation decision (e.g., choosing "resilience" over "capacity to cope") could subtly shift meaning rather than merely standardize a label, especially if the two BMP terms were not perfectly synonymous to begin with. *Mitigation:* Open Question 2 flags this for explicit ratification rather than silent authoring-time judgment.
6. **Bypass risk.** Business Architecture or Domain Discovery authors could simply go back to BMP narrative directly instead of citing the HBRM, recreating the exact redundancy problem the HBRM exists to prevent. *Mitigation:* the dependency-chain contract (§4, §8) must be stated as a hard requirement in both of those documents' own future blueprints, not left as a convention.

---

## 12. Authoring Strategy

- **Author Chapter 0 first.** Every later chapter's entries will reference Person, Household, Need, Community, and Assistance; drafting these first avoids forward-references to not-yet-written entries.
- **Then proceed in BMP chapter order (1 through 9).** This mirrors the dependency order the BMP itself already validated (per `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md` §8's confirmation that the BMP's own chapter sequence has no circular dependency), so the HBRM's authoring order inherits that already-checked soundness rather than re-deriving a new one.
- **Within each chapter:** first extract every named concept from the source BMP chapter; then draft one template entry per concept, minting each new Concept ID against a running Concept ID registry maintained continuously throughout authoring (checked at the moment each ID is minted, not only in a later pass) to guarantee global uniqueness; then perform the terminology-reconciliation pass for that chapter's concepts specifically (checking Research Backlog Workstream F, using the three-outcome verification rule in §2 — Alias, Broader/Narrower, or Unrelated); only after every entry in the chapter exists, fill in cross-chapter relationship fields (Broader/Narrower/Related/Depends On), to avoid dangling references to entries not yet drafted.
- **Before closing each chapter:** perform a lightweight, incremental name-search of every new entry in that chapter against the running Concept Index built so far from all previously-closed chapters, to catch obvious cross-chapter duplication early (e.g., a later chapter naming a concept a prior chapter already catalogued under a different label). This is a quick check, not a full audit, and does not replace the heavier document-wide pass below.
- **Do not resolve any Research Backlog item during authoring**, per §2's citation-not-consumption rule — the one exception being the Workstream F terminology items, which are authored, not merely cited, as part of this same pass.
- **After all ten chapters are drafted:** run a document-wide duplication check (searching for near-duplicate definitions across chapters, not just within one — the authoritative final gate, retained regardless of the incremental per-chapter check above), a document-wide purity scan (the same grep-style method `BUSINESS_MASTER_PLAN_ARCHITECTURE_REVIEW.md` used against the BMP, re-run against the HBRM), a label-collision check against `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md`'s named vocabulary (§9), and a traceability audit (confirming every entry's Origin field resolves to real, already-ratified BMP content). Where the document-wide duplication check finds that two already-closed chapters' entries are genuine duplicates, correct by adding a forward Alias pointer from the later-discovered entry to the earlier, established one — an already-published Concept ID is never retroactively deleted or merged away.
- **Build the Concept Index last**, once every entry's final Concept ID is stable.
- **Close with the Definition of Done checklist (§9)** before declaring the HBRM complete, mirroring exactly how the BMP's own chapters were each closed with a Flagged Open Items pass before the whole document was frozen.
