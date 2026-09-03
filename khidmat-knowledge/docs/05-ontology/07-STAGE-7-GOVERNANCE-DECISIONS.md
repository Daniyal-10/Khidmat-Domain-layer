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

### G2 — CCR-7 Temporal Perspectives (Resolution of C8)
| Field | Value |
| --- | --- |
| ID | G2 |
| Original Domain Question | Whether human/life-trajectory temporality and organisational/programme engagement temporality require two formally independent temporal clocks. |
| Source Evidence | `GT-AR3`; subsequent Stage 7 ontological analysis comparing a unified temporal model, two independent clocks, and one temporal foundation with multiple temporal perspectives. |
| Established Domain Facts | The Reference Model and Ground Truth establish that a person's human/life/situation trajectory exists and persists independently of organisational engagement. Case closure does not imply need resolution. The evidence does not establish a universal requirement for two independent mechanical temporal systems. |
| Exact Conflict | Ground Truth supported separation between the person and administrative engagement but did not justify a universal mandatory dual-clock architecture, originally leaving this parameter UNRESOLVED. |
| Formal Ruling | They are semantically distinct temporal perspectives, but the ontology does not require two formally independent clocks.<br><br>A person's life/situation states and organisational/programme engagement states MUST NOT collapse into a single combined status or be treated as semantically equivalent. Therefore: Case Closed ≠ Need Resolved; Programme Ended ≠ Vulnerability Ended; No Active Case ≠ No Humanitarian Need; Support Delivered ≠ Outcome Achieved.<br><br>The distinction is represented through existing ontology semantics: temporally valid States and Occurrences interpreted relative to their relevant semantic Context (which can provide the frame/perspective relative to which a temporal state or occurrence is understood).<br><br>Both kinds of temporal facts share the same underlying temporal foundation.<br><br>The ontology does not prescribe a fixed number of temporal perspectives (e.g., Life/situation, Programme/engagement, Legal, Funder, or other legitimate future contexts) and does NOT introduce a Clock entity, Timeline primitive, or Process primitive, nor any new primitive, layer, or pillar. |
| Rationale | The existing ontology (`Condition` + `Context`) is sufficient to preserve the distinction without semantic loss. This resolves the semantic problem without requiring independent clocks. |
| Architectural Consequences | CCR-7 is no longer an unresolved foundational question. Architecture MUST preserve the semantic distinction and prevent conflation, while remaining free to determine the appropriate technical representation. |
| Future Evolution | Additional temporal perspectives may be supported if later domain evidence or scope requires them. Such evolution does not imply the existence of independent clocks or require reopening the foundational ontology unless genuine semantic loss is demonstrated. |
| Status | **RESOLVED — ONE TEMPORAL FOUNDATION WITH MULTIPLE TEMPORAL PERSPECTIVES** |

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
