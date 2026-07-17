# HKMP Stage 8F — Certification Review (Audit of the Audit)

**Posture:** Independent review board. `HKMP_STAGE8E_SEMANTIC_INTEGRITY_AUDIT.md` is treated as an
unverified claim set, not a fact, until each of its findings is checked directly against the current
repository — the same posture 8E itself claimed to take toward the implementation reports. No
repository file was modified to produce this review. Every conclusion below cites the specific
command or read used to verify it during this session.

---

## 1. Executive Summary

Stage 8E's findings hold up well under independent re-verification: every finding this review checked
against the actual files was **factually accurate** — no false positive was found among the ten
findings 8E raised. However, 8E's **root-cause analysis of its own Critical finding is incomplete**:
it characterized the `mutually_exclusive` constraint violation as possibly an "unresolved gap" in
`Canonical_Ontology_Schema.md` requiring either a rename or a schema amendment, without checking
whether the repository already contains a working, compliant precedent for exactly this situation. It
does — `needs-assessment/ontology/relationships.yaml` gives three sibling relationships three
distinct verbs (`evaluates_person`, `evaluates_household`, `evaluates_community`) specifically so its
own `mutually_exclusive` constraint can reference them compliantly. This review reclassifies the
Critical finding's root cause from "schema limitation, possibly both" to **primarily a repository
implementation defect with a low-risk, already-precedented fix** — which changes the recommended
remediation path but not the underlying severity.

This review also independently re-verified the actual `git diff` of the five certified files Stage 8D
touched (§7.1 in 8E) and found the changes to be as trivial as claimed (90 insertions, 2
whitespace-only deletions, zero redefinitions) — de-risking that finding enough to downgrade it. Two
other findings (§6.4, §7.2) are downgraded on the same basis: verified accurate, but lower-consequence
than 8E's classification implied once checked against actual repository-wide precedent and practical
rule-evaluation semantics.

**Recommendation: Certification Deferred — narrowly.** One Critical finding remains open, and it is a
genuine, repeated violation of a document the repository marks `[RATIFIED]`. But this review found the
remediation to be small, mechanical, and already proven to work elsewhere in this exact repository —
this is not an open architectural question. Deferral should be understood as gating on a short,
well-defined fix, not a broader reconsideration of the domain's design.

---

## 2. Review Methodology

Every finding in `HKMP_STAGE8E_SEMANTIC_INTEGRITY_AUDIT.md` was checked using one or more of:

1. Direct `grep`/`Read` of the exact YAML lines 8E cited, to confirm the citation is accurate and not
   paraphrased in a misleading way.
2. Direct `grep` of `docs/architecture/Canonical_Ontology_Schema.md` §9 to confirm the ratified-rule
   text 8E quoted is verbatim, not summarized.
3. **A repository-wide search for precedent 8E did not check** — specifically, whether any other
   domain already solves the "two sibling relationships, one shared verb, needs mutual exclusivity"
   problem 8E's Critical finding describes. This is the single highest-value check in this review; see
   §4.
4. Direct `git diff --stat` and full `git diff` of the five certified files Stage 8D modified, to
   independently verify 8E's §7.1 claim that the changes were "additive and non-redefining."
5. Direct `grep` across the repository for prior use of `required_if` with an `expression` parameter,
   to check whether 8E's §6.4 "systematic misuse" claim is really novel to this domain or a broader,
   pre-existing pattern.
6. Direct `grep` for `## Date` / `## Implementation Status` headings and `**Date**` bold lines across
   every pre-existing ADR, to verify 8E's §7.2 formatting claim against more than the two ADRs 8E
   checked.

Findings 8E marked "Verified — no defect" were spot-checked rather than exhaustively re-derived, since
re-deriving a negative claim from scratch has much lower value than checking a positive one; where
spot-checked, the negative finding held.

---

## 3. Finding-by-Finding Assessment

| 8E § | Finding | Factually correct? | Evidence correct? | Severity as-is appropriate? | This review's disposition |
|---|---|---|---|---|---|
| 4.1 | Three `mutually_exclusive` constraints use per-row relationship IDs as `property`, violating `Canonical_Ontology_Schema.md` §9 | **Yes** — verified verbatim against both the schema text and the three constraint rows | Yes, exact | **Root cause incomplete** — see §4 below | **Uphold Critical; correct the root-cause analysis** |
| 4.2 | `resource_id`/`resource_name` placed on abstract `resource`, contradicting `person_id`/`household_id`/`organisation_id` precedent | **Yes** — confirmed `subject` has zero data properties; confirmed `resource_id`/`resource_name` declared with `domain: resource` | Yes, exact | Yes | **Uphold Major** |
| 4.3 | `allocated_quantity_not_exceed_available` cannot detect over-allocation across multiple `resource_allocation`s against one `inventory_item` | **Yes** — confirmed no `available_quantity`/`reserved_quantity` field exists; confirmed no inverse cardinality constrains how many allocations may target one inventory_item | Yes, though the phrasing "cardinality on the inventory_item side is `{min:0, max:unbounded}` via the relationship's directionality" overstates precision — no such cardinality is *declared* at all; it is simply *absent* | Yes | **Uphold Major**, with the evidentiary correction that the unbounded exposure is an absence of a constraint, not a declared one |
| 4.4 | `cold_chain_integrity_constraint` accesses a property (`cold_chain_required`) that doesn't exist on one branch (`financial_resource`) of its polymorphic target | **Yes** — confirmed `cold_chain_required` is declared only on `material_resource` | Yes, exact | **No — overstated** | **Downgrade to Minor** — see §5 |
| 5.2 | `financial_resource_category` has no `distinct_from` note against `intervention_modality`/`delivery_modality`, unlike `material_resource_category` | **Yes** — confirmed the `references:` block names only `material_resource_category` in both entries | Yes, exact | Yes | **Uphold Major** |
| 6.1–6.3 | Inverse pairs complete; polymorphic reference follows precedent; no cyclic dependency | **Yes** (spot-checked) | Yes | N/A (no-defect findings) | **Confirmed** |
| 6.4 | `required_if` misused twice for cross-entity comparisons on already-mandatory fields | **Yes** — confirmed both `contribution_date` and `storage_location_type` are already `min:1`; confirmed no other domain combines `condition`+`expression` under `required_if` | Yes, exact | **No — overstated** | **Downgrade to Minor** — see §5 |
| 7.1 | Programs and Support Delivery modified without an independent re-certification pass | **Yes** — confirmed via `git status`/`git diff` that both were modified post-Stage-7C certification | Yes | **No — overstated given verified-safe diff** | **Downgrade to Minor** — see §5 |
| 7.2 | ADR-025–028 introduce `## Date`/`## Implementation Status` sections absent from prior ADRs | **Yes** — confirmed against *all* prior ADRs, not just the two 8E checked (only ADR-018–020 use even a bold `**Date**` line; none use these headings) | Yes, and this review's broader check strengthens rather than weakens it | Roughly | **Reclassify to Observation** — see §5 |
| 7.3 | No version string incremented on any of the 9 files touched Stage 8B–8D | **Yes** — confirmed all four re-checked files remain at their pre-change version | Yes, exact | Yes | **Uphold Minor** |
| 5.4 | Namespace-style inconsistency (`data-properties.yaml` uses a file-path string, other files in the domain use domain-name style) | **Yes** — confirmed exact text | Yes, exact | Yes | **Uphold Minor** |
| 5.1, 6.1–6.3, 7.4, §8, §10 boundary claims | No-defect / verified claims | **Yes** (spot-checked) | Yes | N/A | **Confirmed, no correction** |

**No false positive was found.** Every finding 8E raised corresponds to a real, checkable discrepancy
in the repository. The corrections this review makes are entirely about **severity calibration** and
**root-cause completeness**, not about factual accuracy.

---

## 4. Validating the Critical Finding

**Does the implementation violate `Canonical_Ontology_Schema.md`?** Yes, unambiguously. The schema
text (§9) states `property` must be "the `relationship` value from §6 ... never a per-row relationship
`id`." `donor_profile_attachment_exclusive`, `resource_allocation_target_exclusive`, and
`resource_allocation_funding_source_exclusive` all set `property:` to a relationship row's `id:`
(`donor_profile_of_person`, `resource_allocation_allocated_to_program`,
`resource_allocation_funded_by_grant` respectively), not to the row's actual `relationship:` verb
(`profile_of`, `allocated_to`, `funded_by` respectively). This is confirmed directly against both
files, not inferred.

**Does `Canonical_Ontology_Schema.md` itself lack an expressive mechanism for this case?** This is
where this review's independent check goes further than 8E's. 8E's own text speculated this "might"
require a schema amendment, because the schema's one worked example for `mutually_exclusive`
(`community-context/ontology/semantic-constraints.yaml`) only covers **sibling data properties**, not
**sibling relationships that share one verb**. But a repository-wide search finds
`needs-assessment/ontology/relationships.yaml` already solves the structurally identical problem
correctly:

```yaml
- id: session_evaluates_person
  relationship: evaluates_person
  to: shared:person
- id: session_evaluates_household
  relationship: evaluates_household
  to: shared:household
- id: session_evaluates_community
  relationship: evaluates_community
  to: community_ctx:geographic_area
```

paired with a fully schema-compliant constraint:

```yaml
type: mutually_exclusive
property: evaluates_community
entities: [assessment_session]
parameters: { with: [evaluates_person, evaluates_household] }
```

Needs Assessment gave each sibling relationship its **own distinct verb** (not one shared verb across
rows), which makes the verb itself a valid, unambiguous, canonical disambiguator — exactly what §9
requires, and exactly the situation Donor & Resource faced with `donor_profile_of_person`/
`donor_profile_of_organisation` (both using the shared verb `profile_of`),
`resource_allocation_allocated_to_program`/`_case_plan` (both `allocated_to`), and
`resource_allocation_funded_by_grant`/`_contribution` (both `funded_by`).

**Conclusion: this is primarily a repository implementation defect, not a schema limitation.** The
schema's general rule is sufficient and was already followed correctly elsewhere in this repository at
the time Donor & Resource was authored. Donor & Resource chose a different, non-compliant relationship-
naming pattern (shared verb, disambiguated only by the row `id` and the `to:` target) and then had no
compliant way to reference it in a constraint — a problem it created for itself by not following
available precedent, not a problem the schema failed to anticipate. The "both" classification 8E left
open is not supported once the precedent search is done; this review assigns it to **repository
implementation defect**, full stop, with the observation that the schema's own §9 worked example could
be improved by adding a second example covering the relationship case (a documentation enhancement,
not a contract change — filed as an Observation, not a finding against Donor & Resource).

**Severity:** Confirmed **Critical**. A ratified-contract violation repeated three times is not
downgraded by the existence of an easy fix — but the existence of an easy, precedented fix does change
how long deferral should reasonably take (see §6).

---

## 5. Severity Reclassification

| Finding | 8E severity | This review's severity | Reasoning for change |
|---|---|---|---|
| §4.1 Constraint `property` field violation | Critical | **Critical (unchanged)** | Confirmed accurate; root cause reclassified (§4) but severity stands — a ratified-contract violation is Critical regardless of fix cost |
| §4.2 `resource_id`/`resource_name` on abstract entity | Major | **Major (unchanged)** | Confirmed accurate, no basis to change |
| §4.3 Multi-allocation over-commitment gap | Major | **Major (unchanged)** | Confirmed accurate; this is arguably the most operationally consequential finding in the set (real-world resource integrity), but remains an ontology-completeness gap, not a contract violation, so Critical is not warranted — Major is correct |
| §4.4 Cold-chain constraint type-safety gap | Major | **Downgraded to Minor** | Confirmed the property path is genuinely unresolvable for a `financial_resource`-backed instance, but under standard rule-evaluation semantics (used throughout this repository's constraint model — an undefined/absent property in a boolean condition evaluates as not-satisfied, not as an error), the constraint simply never fires for that branch rather than producing an incorrect result. The defect is a type-safety/generator-purity concern, not a live logic error. Worth cleaning up, not blocking. |
| §5.2 `financial_resource_category` reconciliation gap | Major | **Major (unchanged)** | Confirmed accurate against an explicitly named architecture-phase requirement that was only half-completed — this is a real, disclosed-requirement miss, not a nice-to-have |
| §6.4 `required_if` type misuse | Major | **Downgraded to Minor** | Confirmed accurate and confirmed novel to this domain (no other `required_if` in the repo combines `condition`+`expression`). But the remediation is a one-line `type:` relabel to `cardinality` — the exact mechanism this domain's own compliant constraints already use for the identical `condition`+`expression` shape. This is a taxonomy-of-constraint-types labeling error, not a constraint-logic error; the enforced invariant itself is correct either way. |
| §7.1 No independent re-certification of Programs/Support Delivery | Major | **Downgraded to Minor** | Confirmed the process gap is real, but this review's own `git diff` of all five files found 90 insertions / 2 whitespace-only deletions, zero redefinitions, entirely consistent with the "additive-only" claim. The risk the re-certification discipline exists to catch (silent redefinition of certified content) is independently confirmed absent. The process gap is worth naming for governance hygiene, but the risk it flags has already been checked and closed by this review. |
| §5.4 Namespace-style inconsistency | Minor | **Minor (unchanged)** | Confirmed accurate, correctly scoped |
| §7.2 ADR formatting deviation | Minor | **Reclassified to Observation** | Confirmed accurate and, on a broader check than 8E performed, even more clearly a new-but-consistently-applied pattern (all four new ADRs use it the same way) rather than an inconsistency within the new content itself — it only differs from *older* ADRs. Since the new pattern (`## Implementation Status`) is arguably a genuine documentation improvement and the repository has no rule against ADR template evolution, this is better classified as an improvement opportunity than a defect. |
| §7.3 Version strings not incremented | Minor | **Minor (unchanged)** | Confirmed accurate, correctly scoped |

**Net effect of this reclassification:** 1 Critical (unchanged), 3 Major (down from 6), 4 Minor (up
from 3, net of the one moved to Observation), 1 additional Observation. The overall defect count is
unchanged (every 8E finding survives as *something*); what changes is that three of 8E's six Major
findings, once checked against practical evaluation semantics and actual git history rather than
theoretical worst cases, resolve to lower-consequence issues.

---

## 6. Repository vs. Framework Issues

| Finding | Repository (implementation) issue | Framework (schema) issue |
|---|---|---|
| §4.1 constraint `property` violation | **Primary classification.** An available, working, same-repository pattern (distinct verbs per sibling relationship) was not followed. | Secondary, documentation-only: §9's worked example could usefully show the relationship case alongside the data-property case it currently shows. Not a blocking gap — the *rule* itself is sufficient; only the *illustration* is incomplete. |
| §4.2 `resource_id` placement | Repository issue — contradicts existing precedent (`person_id`/`household_id`) the entity's own text claims to follow. | None. |
| §4.3 multi-allocation gap | Repository issue — a modeling completeness gap in this domain specifically. | Arguably touches a framework question: the schema has no established pattern anywhere in the repository for "aggregate/derived quantity across multiple referencing instances" invariants (this would be a novel need, not a precedented one). Worth flagging as a possible future schema extension, but does not excuse the specific gap here, since even a simpler fix (an explicit `available_quantity` field with manual bookkeeping) would close it without any schema change. |
| §4.4 cold-chain type safety | Repository issue — narrow, in this domain's own constraint authoring. | None — this is squarely an authoring-discipline issue, not a schema gap. |
| §5.2 reconciliation gap | Repository issue — an explicitly-required task left incomplete. | None. |
| §6.4 `required_if` misuse | Repository issue — mislabeled `type:`, not a schema gap (the `cardinality` type already supports the exact shape needed). | None. |
| §7.1 re-certification gap | Repository governance-process issue. | None — this is about process discipline, not the ontology contract. |

**Overall:** every substantive finding in this audit is a repository-side issue. The one place this
review found a genuine (very narrow) framework-side observation — §9's example coverage — is
documentation-only and does not itself block anything; it is filed as an Observation, not folded into
the Critical finding's severity.

---

## 7. Certification Decision Review

8E recommended **Certification Deferred**, reasoning that the Critical finding's status as a ratified-
contract violation is "incompatible with either 'Certified' outcome regardless of how sound the
surrounding architecture is," while the architecture itself was independently sound enough to rule out
"Rejected."

This review agrees with both halves of that reasoning independently — but adds a consideration 8E did
not have available: **the remediation for the Critical finding is now known to be small, mechanical,
and already proven to work in this exact repository** (§4). This matters for *how* deferral should be
scoped, even if it does not change *whether* deferral is the right category:

- **Repository risk:** Low. Every finding in this review is either non-live (no generator exists to
  actually choke on §4.1 today) or independently verified low-blast-radius (§7.1's underlying diffs are
  trivial; §4.4's failure mode is a silent no-op, not a wrong answer).
- **Ontology correctness:** High, with one real completeness gap (§4.3) worth closing before the
  domain is used for anything resembling real allocation tracking across multiple concurrent claims on
  one stock item.
- **Governance maturity:** Adequate — Authority Matrix and Glossary integration verified clean (§6.1 of
  8E, spot-checked here and confirmed); the one process gap (§7.1) is now understood to be about
  discipline, not about an actual undetected defect slipping through.
- **Implementation completeness:** High — 9 entities, 17 relationships, 37 data properties, 15
  constraints, 95 taxonomy concepts, all independently counted and matching prior reports exactly; no
  scope gap was found anywhere in this review.
- **Schema maturity:** Adequate for this case — §4 found the schema itself did not need to change; it
  was already sufficient, just not followed.

Given all five factors, **outright "Certification Approved with Conditions" was seriously considered**
by this review as an alternative to "Deferred" — the case for it is that none of the findings are live,
data-corrupting, or cross-domain-risk-bearing, and the fixes are cheap. It was set aside because this
repository has an established precedent (Stage 7B → Stage 7C) of treating a confirmed contract
violation as something that gates certification until re-verified fixed, not something certification
proceeds around with a promise to fix later — and a Critical finding, by this review's own confirmation
above, remains open. Consistency with that precedent is a defensible reason on its own to hold this
domain to the same standard, even though the specific defect here is narrower in practice than the
Stage 7 findings that originally established the precedent.

---

## 8. Final Recommendation

**Certification Deferred.**

**Scope of deferral (explicit, to avoid the open-endedness 8E's report did not rule out):** deferred
pending remediation of the one Critical finding (§4.1) and, in the same pass, the two Major findings
that remain Major after this review's reclassification (§4.2, §4.3, §5.2). The three findings this
review downgraded to Minor or Observation (§4.4, §6.4, §7.1, §7.2) do not need to be resolved before
re-certification, though closing them in the same pass is efficient and low-cost.

**Recommended remediation, in priority order:**
1. Rename the three shared-verb relationship pairs to distinct verbs, following the
   `session_evaluates_person`/`_household`/`_community` precedent exactly (e.g. `profile_of_person`/
   `profile_of_organisation`; `allocated_to_program`/`allocated_to_case_plan`; `funded_by_grant`/
   `funded_by_contribution`), then update the three `mutually_exclusive` constraints' `property`/`with`
   values to the new verbs. This closes §4.1 without any schema change.
2. Move `resource_id`/`resource_name` (or equivalents) from `resource` down to `financial_resource` and
   `material_resource`, matching the `person_id`/`household_id` precedent, and correct `resource`'s
   `ownership_boundary` text. Closes §4.2.
3. Add an `available_quantity` (or `reserved_quantity`) property to `inventory_item` and rewrite
   `allocated_quantity_not_exceed_available` to check against it, netting out existing non-cancelled
   allocations — or explicitly document the aggregate-accounting limitation as an intentional,
   disclosed ontology-scope boundary if a full fix is out of scope for this pass. Closes §4.3.
4. Add the missing `financial_resource_category` `distinct_from` note to
   `resource-classification.yaml`'s `references:` block. Closes §5.2.

**A second, brief independent check** (not a full Stage 8E/8F-style audit — a targeted diff review) of
whichever remediation pass closes items 1–4 is sufficient to move this domain to full certification;
this review does not anticipate finding new issues in that follow-up given how narrow and mechanical
the required changes are.
