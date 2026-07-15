# Phase 1.6 — Humanitarian Operational Validation

**Method:** each scenario below was traced through the actual current ontology and taxonomy
files — entities, relationships, cardinalities, and schemes as they exist today, after the
Phase 1.2–1.5 completion and cleanup work — not from memory of the original Phase 1 Freeze
Audit, much of which this validation confirms is now resolved. Several specific cardinalities
and relationships were directly re-checked against the files before scoring (documented inline
where the answer is non-obvious).

---

## 1. Executive Summary

The identity spine work (Person/Beneficiary/Household observation relationships), Organisation,
Referral-targets-Organisation, Follow-up, and Case/Family wiring completed since the original
Freeze Audit have closed the majority of what previously blocked longitudinal and identity-based
scenarios. **Returning beneficiary, duplicate registration, case reopening, and multi-year
history are now representable** — they were the headline blockers in the original audit and are
not blockers here.

What remains blocked is narrower and more structural: **household-level topology change**
(split, merge, migration, joint-family sub-structure) has no relationship to express it — every
fix this project made strengthened the *Person* and *Case* identity spine, but no pass ever
added a *Household*-to-*Household* relationship, and `beneficiary_is_member_of_household`
remains hard-capped at exactly one household. This is the one clear, single missing semantic
capability this validation identifies, and it recurs across five of the scenarios below rather
than being five separate problems.

**Decision: BUSINESS VALIDATION FAILED**, narrowly — on one recurring capability, not a broad
failure. Every other required scenario passes.

---

## 2. Scenario Validation Matrix

Legend: ✓ = yes, ⚠ = partial/representable-with-caveat, ✗ = not representable.

### Identity

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| First registration | ✓ | Correct | Correct | Yes | Yes | Yes |
| Returning beneficiary | ✓ | Correct — `beneficiary_observes_person {1,1}`; multiple Beneficiary snapshots may observe the same `person`, closing the gap the original audit found | Correct | Yes — "has this person been helped before" is now a direct traversal | Yes | Yes |
| Duplicate registration | ✓ | `case_statuses` includes `duplicate_suspected`; two Beneficiary snapshots observing the same Person is graph-detectable | Correct | Yes | Yes | Yes |
| Proxy registration | ✓ | Strong — `registrant_types`, `proxy_consent`, `claim_basis` inheritance, all enforced by `required_if` constraints | Correct | Yes | Yes | Yes |

### Household

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Household (baseline) | ✓ | `household_snapshot_observes_household {1,1}` | Correct | Yes | Yes | Yes |
| Joint family | ✗ | No sub-household/hearth concept; one `household_snapshot` per case forces a joint family into either one coarse household or disconnected cases | N/A | No | No | N/A |
| Household split | ✗ | No `household`-to-`household` relationship exists anywhere in the ontology (verified directly — `household_snapshot_observes_household`'s own note mentions "household reconfiguration" only in prose, no structural edge backs it) | N/A | No | No | N/A |
| Household merge | ✗ | Same gap as split | N/A | No | No | N/A |
| Migration | ✗ | `beneficiary_is_member_of_household` is `{min:1, max:1}` (verified directly, unchanged since the original audit) — a member split across an origin and destination household cannot be represented | N/A | No | No | N/A |

### Vital Events

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Death | ⚠ | No dedicated field on `household_member` (no `deceased`/status property), but `situation.trigger_event` includes `bereavement`, `evidence_type` includes `death_certificate`, and Family's support-role taxonomy has an extensively-modelled `deceased` concept, reachable via `case_informed_by_family`. The humanitarian need this produces is fully representable and reasonable-over through this combination; the specific fact "this named household member died on this date" is not a first-class structured field. | Adequate via composition | Yes, for the resulting need; not for a standalone vital-event query | Partial | Yes |
| Birth | ⚠ | No dedicated `trigger_events` value for birth; the resulting new `household_member` is representable in the next `household_snapshot`, but the event itself is not classified | Gap | Partial | Partial | Yes |
| Marriage | ⚠ | Same as birth — no dedicated trigger event; structural outcome (new/changed household composition) is representable, the event classification is not | Gap | Partial | Partial | Yes |

### Case

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Verification success | ✓ | Strong — the most complete domain in the repository | Correct | Yes | Yes | Yes |
| Verification failure | ✓ | `finding_status: contradicted`, escalation paths | Correct | Yes | Yes | Yes |
| Fraud suspicion | ✓ | `information_consistency: contradictory`, `duplicate_suspected`, escalation-reasons taxonomy | Correct | Yes | Yes | Yes |
| Case reopening | ✓ | `case_status` includes a distinct `reopened` value, not excluded by the `completed_case_immutable` lifecycle constraint (which only blocks transitions to `active`/`opened` from a resolved-closed case — verified directly) | Correct | Yes | Yes | Yes |
| Follow-up | ✓ | `follow_up` entity (status, due date, assignee, outcome), `case_has_follow_up`, `follow_up_status` taxonomy — all added since the original audit | Correct | Yes | Yes | Yes |

### Needs

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Food insecurity, Livelihood, Education, Health, Disability, Shelter | ✓ (all six) | `need_categories`, `capabilities.yaml`, `health-conditions.yaml` — rich, pre-existing | Correct | Yes | Yes | Yes |
| Cash assistance, Material assistance | ✓ | `support_intervention` entity; `requested_duration` now references `need_duration` (fixed this project) | Correct | Yes | Yes | Yes |
| Multi-need household | ✓ | `case_has_needs {min:1, max:unbounded}`, `need_severity` now present on both Registration's `need` and Needs Assessment's `need_assertion` (added Phase 1.3A) | Correct | Yes | Yes | Yes |

### Community

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Urban slum, Village, Tribal community | ✓ (all three) | `geographic-hierarchy.yaml`, `settlement-types.yaml` — correctly India-deployable and country-neutral | Correct | Yes | Yes | Yes |
| Flood, Fire, Earthquake, Drought | ✓ (all four) | `hazard-categories.yaml`, `community-hazards.yaml`, `seasonal-events.yaml` | Correct | Yes | Yes | Yes |
| Community intervention | ✓ | `community`, `local_collective` entities | Correct | Yes | Yes | Yes |

### Referrals

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Government referral | ✓ | `referral_targets_organisation {1,1}` (added this project) — the single highest-value Indian NGO workflow this repository previously could not represent | Correct | Yes | Yes | Yes |
| NGO referral | ✓ | Same relationship; `organisation` types taxonomy distinguishes them | Correct | Yes | Yes | Yes |
| Cross-program referral | ✗ | `referral` targets `organisation` only — there is no `referral`-to-`program` or `referral`-to-`enrollment` relationship, so a beneficiary referred from one Khidmat Program to another cannot be expressed as a Referral; it could only be inferred indirectly through two separate Enrollment records with no link between them | N/A | No | No | No |

### Longitudinal

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Repeated support | ✓ | Person identity spine + multiple Cases/Beneficiary snapshots observing the same Person | Correct | Yes | Yes | Yes |
| Changing vulnerabilities | ✓ | `risk_characterization` now addressable (added this project), `need_assertion.need_severity` | Correct | Yes | Yes | Yes |
| Household evolution | ✗ | Same gap as Household Split/Merge above — no structural way to link "household as it was" to "household as it is now" beyond both `household_snapshot`s observing the same canonical `household` | N/A | No | No | N/A |
| Multi-year history | ✓ | Person → Beneficiary snapshots, Household → household_snapshots, Case → Follow-up, all now identity-linked | Correct | Yes | Yes | Yes |

### Monitoring / Impact

| Scenario | Representable? | Ontology | Taxonomy | AI Reasoning | Graph Traversal | Cross-Domain |
|---|---|---|---|---|---|---|
| Monitoring | ✓ | `follow_up` entity, `operational_observation` (Support Delivery) | Correct | Yes | Yes | Yes |
| Impact | ✓ | `impact_evaluation`, `measurement` (baseline/endline), now correctly anchored to a persistent Person via the identity spine — the original audit's finding that Impact "can measure a case, not this person's trajectory" is resolved | Correct, except `outcome_indicator` taxonomy remains a documented Blueprint-scheduled deferral (§16), not a Phase 1 blocker | Yes | Yes | Yes |

---

## 3. AI Readiness

| Capability | Status | Basis |
|---|---|---|
| Knowledge Graph | Ready | 0 broken references (excluding 3 documented deferrals), 0 duplicate relationship/constraint/scheme IDs, acyclic at the ownership level |
| GraphRAG | Ready for everything except household-topology queries | Person/Household/Organisation/Case/Family are all now addressable and connected; a query like "has this household split since last registration" has no edge to traverse |
| Semantic Search | Ready | Rich, well-described taxonomy (1032 concepts) |
| RAG grounding | Ready for identity/case/needs queries; ungrounded for household-evolution queries | An LLM asked "is this the same household as before" can now answer correctly via the identity spine; asked "did this household split" it has nothing to ground on |
| Rule Engines | Ready for Registration and Verification Operations (the two domains with an authored reasoning layer); other domains have no reasoning layer, which is a pre-existing, already-documented condition, not new to this validation |
| Planning Systems | Ready — Follow-up gives planning systems a concrete, trackable action entity |
| Agentic AI | Ready for case-management and verification workflows; not ready for household-restructuring workflows |
| Case Recommendation | Ready | Case, Case Plan, Follow-up, Referral all present and connected |
| Volunteer Recommendation | Ready | Volunteer Profile correctly specializes Actor, referenced by Verification and Delivery |
| Programme Recommendation | Ready for enrollment eligibility; not ready for cross-program referral routing (§2) |

---

## 4. Graph Readiness

The graph is traversable end-to-end for every identity, case, verification, needs, community,
and single-household scenario. It has one systematic dead end: any traversal that needs to move
from one `household_snapshot` to a *different* `household_snapshot` representing the same
real-world household after a topology change (split, merge, migration, joint-family
decomposition) has no edge to follow. This is not a missing property on an existing node — it
is a missing edge type between `household` and itself (or between `household_snapshot` and
`household_snapshot`), the same class of gap the ownership freeze already solved for `case`
(`case_superseded_by_case`) and `human_review`
(`human_review_supersedes_human_review`) but never solved for `household`.

## 5. Humanitarian Readiness

Strong. The scenarios that matter most for day-to-day Indian NGO casework — repeat visits,
proxy registration, verification, fraud detection, government/NGO referral, multi-need
households, seasonal hazards — all pass cleanly, several of them newly so as a direct result of
this project's identity-spine and Organisation work. The gap is narrower than it might first
appear: it is specifically *household as a changing topology over time*, not household content,
composition classification, or vulnerability reasoning, all of which are strong.

## 6. Operational Gaps

Two genuine Phase 1 blockers, both traced to the same missing relationship type:

1. **No `household`-to-`household` relationship exists.** This single gap is the entire cause
   of five failing scenarios (Joint Family, Household Split, Household Merge, Migration,
   Household Evolution). It is not five separate defects — closing this one relationship
   (a household succession/composition edge, mirroring the pattern already used for
   `case_superseded_by_case`) would resolve all five.

2. **`referral` cannot target a Program or Enrollment, only an Organisation.** Blocks
   Cross-Program Referral specifically; Government and NGO referral are unaffected since both
   correctly resolve through Organisation.

Both are genuine Phase 1 scope — they block scenarios this validation was explicitly asked to
test, not Phase 2 enhancements, and both were already implicitly foreshadowed (household
succession was named as a missing concept in the Phase 1.1 Canonical Ontology Specification but
never carried into implementation; the Referral-to-Organisation decision never considered
Program as an alternate target).

No other scenario in the required list failed.

## 7. Repository Readiness

The repository itself is mechanically sound (confirmed in Phase 1.5) and ready to support these
two fixes without any other structural change — both are additive relationships, consistent
with the pattern already used successfully for Case, Human Review, and every other
identity-linked concept this project touched. Nothing found in this validation requires
reopening the ownership, taxonomy, or repository-cleanup freezes already certified.

---

## 8. Final Decision

# B.

## BUSINESS VALIDATION FAILED

Genuine operational blockers:

1. **Household topology change is unrepresentable.** No relationship links one `household` (or
   `household_snapshot`) to another. This blocks Joint Family, Household Split, Household
   Merge, Migration, and Household Evolution — five required scenarios, one missing capability.

2. **Cross-program referral is unrepresentable.** `referral` targets only `organisation`; no
   path exists from a Referral to a Program or Enrollment.

Every other required scenario — including several the original Phase 1 Freeze Audit had marked
as blocked (Returning Beneficiary, Duplicate Registration, Case Reopening, Government Referral,
Multi-Year History) — now passes.
