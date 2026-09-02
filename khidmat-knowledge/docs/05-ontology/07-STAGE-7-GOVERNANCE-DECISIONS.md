# STAGE 7 — GOVERNANCE DECISIONS

This register records formal governance rulings on structural conflicts and unresolved items identified during Stage 6 Evidence Integration, following the resolution conventions of the domain.

---

### G1 — Organisation vs Programme (Resolution of Q6 / C2)
| Field | Value |
| --- | --- |
| ID | G1 (Supersedes Q6) |
| Domain Question | Are Organisation and Programme distinct entities? |
| Source Evidence | `BL V1 §4`, `GT-OQ6`, `GT-PL5` |
| Established Domain Facts | Practitioner evidence overwhelmingly requires tracking distinct programmatic constraints. |
| Existing Authoritative Position | `BL V1 §4` explicitly collapses Organisation and Programme into a single Entity (P4). Reference Model resolved earlier tensions by adopting this collapse (`Q6`). |
| Exact Conflict | Tier 1 authority explicitly collapses them. Grounded field practice explicitly requires separating them to track distinct programmatic constraints. |
| Options Evaluated | **Opt 1**: Preserve Tier 1 (Collapsed).<br>**Opt 2**: Split into two distinct Entities. |
| Ontological Consequences | Opt 1 fails to model distinct programmatic bounds on constraints/eligibility. Opt 2 adds a new Entity (`Programme`), requires `Relation` between Org and Prog. |
| Architectural Consequences | Opt 1 conflates Org and Prog IDs. Opt 2 requires tracking two distinct IDs and APIs. |
| Breakage | Opt 1 breaks the ability to properly model "Funding Restrictions" (Q8) and "Context" (P2), which depend on Programme rules. Opt 2 formally amends Tier 1 authority. |
| Formal Ruling | **Opt 2 is SELECTED.** Organisation and Programme ARE distinct entities. |
| Tier 1 Authority Status | The prior rule collapsing them (`BL V1 §4`, `Q6`) has been amended directly at source in `KHIDMAT_BUSINESS_LOGIC_BLUEPRINT_V1.md` §4 (dated 2026-09-02), per this document's own XCR-2 requirement. This Stage 7 entry records the ruling; the source document itself now reflects it. Field evidence demonstrates that Context, Norms, and Need derivation cannot function structurally if the Organisation is the only boundary. |
| Downstream Ontology Changes | L2 (Entities) must explicitly list Programme as a distinct Entity. P4 (Entity) description updated. |
| Architecture Rule Changes | None fundamentally, but schema representations must split them. |
| Status | **RESOLVED** |

---

### G2 — CCR-7 Dual-clock rule (Resolution of C8)
| Field | Value |
| --- | --- |
| ID | G2 |
| Domain Question | Does the Dual-clock rule (CCR-7) require mandatory architectural enforcement? |
| Source Evidence | `GT-AR3` |
| Existing Authoritative Position | CCR-7 Dual-clock rule suggests separating a person's life circumstances from their administrative status. |
| Exact Conflict | Evidence supports separating the Person from the administrative record, but is insufficient to prove a universal architectural requirement for two strictly separated temporal clocks across all deployments. |
| Options Evaluated | **Opt 1**: Enforce CCR-7 unconditionally.<br>**Opt 2**: Treat CCR-7 as unresolved/optional until further evidence. |
| Ontological Consequences | None directly (this is an architectural rule). |
| Architectural Consequences | Opt 1 forces complex dual temporal tables/event sourcing on implementations. Opt 2 leaves temporal tracking slightly ambiguous. |
| Breakage | Opt 1 forces over-engineering if not universally true. |
| Formal Ruling | **Opt 2 is SELECTED.** Do not force a ruling. |
| Tier 1 Authority Status | Retained as a theoretical guideline, not a mandatory constraint. |
| Status | **UNRESOLVED** |

---

### G3 — Domain Primitive Definition (Resolution of R-1)
| Field | Value |
| --- | --- |
| ID | G3 |
| Domain Question | Is a Domain Primitive a category of concept (Identity, Relation, Condition) or a concrete irreducible of reality (Person, Household, Need)? |
| Source Evidence | - `01-DOMAIN-PRIMITIVES.md` §1 — circularity argument: Person cannot be both source and member of the Entities layer.<br>- `01-DOMAIN-PRIMITIVES.md` §5.2 — giving-side coverage test.<br>- `docs/06-review-package/02-ontology-design-review-phase-1.html` — R-1. |
| Established Domain Facts | The category reading is the only reading under which Stage 2's eight layers, including the Entities layer, can be derived without circularity. The concrete reading was tested and produces an unbounded/non-converging candidate list. |
| Options Evaluated | - **Opt 1** — Ratify category-of-concept reading as already implemented in Stages 1–2.<br>- **Opt 2** — Reject it and require concrete-irreducible re-derivation of the entire primitive/layer stack. |
| Formal Ruling | **Opt 1 is SELECTED.**<br><br>Domain Primitive = category of concept.<br><br>This is the governing definition project-wide. |
| Tier 1 Authority Status | No Tier 1 conflict. This is a methodological/design-primitive definition, not a business fact. |
| Downstream Ontology Changes | None. Stages 1–2 already reflect this interpretation. This ruling makes the interpretation formally authoritative. |
| Status | **RESOLVED** |

---

### G4 — Option A Closure Ratification (Need-Interactions, Service Providers, Outcome/Impact Ownership, Funder Altitude, Case Orchestration)
| Field | Value |
| --- | --- |
| ID | G4 |
| Domain Question | Are the single-source "Option A Closure" resolutions for these five items formally adopted? |
| Source Evidence | `GT-OQ16`, `GT-OQ15`, `GT-OQ5`, `GT-OQ17`, `GT-OQ19` |
| Established Domain Facts | Each item rests on exactly one practitioner record (Finding classification REFINED, not CONFIRMED) and has not been independently corroborated. |
| Formal Ruling | **Governance decision**: The project adopts "Option A" (the treatment described for each item in `06-STAGE-6-EVIDENCE-INTEGRATION-REPORT.md` §9 / the closure reports) for current modeling purposes.<br><br>**Ontological status**: UNRESOLVED. The underlying domain propositions are NOT ontologically closed. For example, regarding Need-Interactions, the current evidence is insufficient to justify introducing a formal ontology-level relation type, but this does not mean such a relation does not exist in humanitarian reality.<br><br>**Evidence status**: Weak/Single-source. Each item rests on exactly one practitioner record and lacks independent corroboration.<br><br>Reopening requires new practitioner evidence or an explicit superseding governance ruling. |
| Status | **GOVERNED PROVISIONAL — single-source evidence acknowledged** |

---

### G5 — Risk and Need Primitive Classification
| Field | Value |
| --- | --- |
| ID | G5 |
| Domain Question | Are Risk and Need classified as Condition (P1) or some other primitive? |
| Source Evidence | `01-DOMAIN-PRIMITIVES.md` §6.1 (Risk), §6.2 (Need); `04-ARCHITECTURE-RULES.md` §1 (Need synchronization correction). |
| Established Domain Facts | Risk is a dispositional-future-oriented Condition; Need is a Condition with a lifecycle, not a Relation, because its Norm-based comparator forecloses the Relation reading. |
| Formal Ruling | Risk = Condition (P1); confidence about Risk = Epistemic Stance (P3). Need = Condition (P1); the wellbeing standard it is measured against = Norm (P5). |
| Status | **RESOLVED** |
