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
| Tier 1 Authority Status | The prior rule collapsing them (`BL V1 §4`, `Q6`) is formally **AMENDED** by this Stage 7 ruling. Field evidence demonstrates that Context, Norms, and Need derivation cannot function structurally if the Organisation is the only boundary. |
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
