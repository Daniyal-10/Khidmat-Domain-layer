# Provenance Statement

> **Added under remediation B7.** The accepted Foundation Readiness Assessment recorded that the seven original Stage 5 domains carried **no source, tier, confidence rating or corroboration count on any assertion**, and that under `ONTOLOGY_DESIGN.md` §6 — *"an assertion in any prior project artifact, including frozen ones, is not evidence for a design decision merely because it was recorded; its provenance must itself be evaluable"* — the corpus was therefore formally inadmissible as evidence for ontology design.
>
> This statement supplies the missing provenance. It does not add, remove or alter any finding.

**Evidence tier of this domain as a whole: Tier C** — project-internal derivation. The domain was authored by reasoning from `BUSINESS_ARCHITECTURE.md` (Stage 4, Frozen), `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` (Stage 3, Frozen) and the 20-section template in `STAGE_5_DISCOVERY_STANDARD.md`. It is evidence of this project's own reasoning about humanitarian practice, not independent evidence of humanitarian reality.

**Tier A (practitioner): not executed.** No practitioner elicitation channel exists for this discovery process — the standing constraint documented in `TD-01` Tier A Disposition and re-confirmed in every subsequent dossier. `STATUS.md` records `Client Validation: Pending` for this reason.

**Tier B / Tier D (sector standards, literature): not executed for this domain.** External collection was performed for TD-01 through TD-06 (approximately 45 cited sources) but not for the seven per-domain discoveries. Where a statement in this domain happens to be corroborated by a TD finding, that corroboration is noted below; the domain document itself was not authored from those sources.

**Confidence, declared at domain level: Medium.** The reasoning is internally coherent and consistent with the frozen upstream documents it derives from. It is uncorroborated by any source outside this project.

**Consequence for ontology design.** Statements in this domain may be weighed as Tier C evidence — sufficient to inform layer placement and concept admission, insufficient on their own to support a universal Constraint tag (`ONTOLOGY_DESIGN.md` §6 requires corroboration across contexts *and* a passed Ground Truth Review for that). Every universal tag derived from this domain remains marked *untested* until remediation B13 delivers a ground truth channel.

**Externally corroborated statements in this domain:** none directly. The recognition of informal and community-based actors as legitimate humanitarian actors, on which this domain's community-validation concepts depend, is corroborated by TD-01 BD-TD01-005 (Tier D, High confidence, ≥3 independent source families). The consent/necessity bounded exception restated in this domain's exceptions is corroborated by TD-02 BD-TD02-004 (Tier B, High confidence, ICRC Handbook on Data Protection in Humanitarian Action plus 3 secondary commentaries).

---

# 15. Discovery Evidence

## Established Facts
- Registration must precede Case Management assessment. Identity is the foundation upon which vulnerability is evaluated.
- Households are fluid temporal structures; Beneficiaries are permanent entities.
- Algorithmic deduplication creates false positives; human adjudication is a mandatory business reality.

## Reasonable Assumptions
- The definition of a "Household" will vary drastically depending on the cultural context of the crisis.
- Beneficiaries will occasionally attempt to register multiple times to secure additional rations.

## Open Questions
Refer to Section 14 (10-open-questions.md).

## Knowledge Gaps
- The specific legal constraints of storing biometric data on cloud servers versus local devices in high-risk conflict zones.
