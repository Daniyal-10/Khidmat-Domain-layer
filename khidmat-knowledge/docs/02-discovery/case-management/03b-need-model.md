# Need and Intervention Fit — Case Altitude

> **Added under remediation B5**, closing the case-altitude portion of Foundation Gap FG-6.
> FG-6 recorded that TD-06 discovered intervention categorisation well but **at programme altitude only** (Sector × Modality × Temporal Phase), while `03-concepts.md` carried *Need* as a bare name with no categories, no severity model and no need-to-need relationships. This file supplies the case-altitude content by promoting existing repository knowledge. It does not restate TD-06.
>
> **Sources:** `98-archive/execution_cleanup/BUSINESS_ARCHITECTURE_BLUEPRINT.md` §§9, 12 (deprecated, re-entering through discovery as `ONTOLOGY_DESIGN.md`'s preamble requires); `GLOSSARY.md` Core Terms and Risk/Vulnerability Terms; `SHARED_CONCEPT_CATALOG.md` §3; client blueprint `direct-relief-architecture.html`.
> **Tier A, B and D were not executed.** Every statement below is Tier C unless marked otherwise.

---

## 1. What a Need Is

`GLOSSARY.md` defines a Need as *"a specific, concrete gap between a household member's current state and a basic standard of wellbeing,"* contextualised by situations but not synonymous with them. Blueprint §9 states the same shape independently: *"A need is a gap between current state and a basic standard of wellbeing."* Two independent internal sources agree, which makes this an **Established Fact** at Tier C.

`SHARED_CONCEPT_CATALOG.md` §3 adds the architectural consequence: a Need must be modelled distinctly from the Intervention that addresses it, so that *"a Need to exist even if no Programme or Resource currently exists to fulfil it"* — otherwise the system cannot see the gaps in its own response.

## 2. Need Categories

Blueprint §9 names seven categories. These are the case-altitude counterpart to TD-06's programme-altitude Sector dimension; TD-06 BD-TD06-002 established that sector categorisation operates at programme altitude while case-altitude decisions concern fit and modality.

| Category | Content as evidenced | Source |
|---|---|---|
| **Food** | daily food, nutrition, infant feeding, therapeutic nutrition | Blueprint §9 |
| **Health** | treatment, surgery, medication, rehabilitation, assistive devices, diagnosis | Blueprint §9; client blueprint Flow B (surgical need) |
| **Education** | school fees, supplies, transport, re-enrollment | Blueprint §9 |
| **Housing** | roof repair, shelter repair, rent support, emergency housing | Blueprint §9 |
| **Livelihood** | income support, employment, skills development, tools and equipment | Blueprint §9 |
| **Psychosocial** | grief, trauma, chronic stress, caregiver burden, domestic-violence aftermath | Blueprint §9 |
| **Protection** | widow support, child protection, elder care, safeguarding of people at risk of harm | Blueprint §9 |

**Corroboration note.** TD-06 §3 records that blueprint §9's list was reviewed during that dossier and that the blueprint's *Support* model (§12) mixes modality with sector. TD-06 BD-TD06-001 corrected that confusion at programme altitude. The **need** list above is not affected by that correction: it is a list of need kinds, not of delivery mechanisms.

**Recorded limitation.** These seven are a single-source decomposition. They are retained because they are coherent and because retiring them would discard knowledge the project produced once, but they are **not** externally corroborated and are recorded as AR-018.

## 3. Need Dynamics

Blueprint §9 states directly: *"Needs are dynamic, not static. A need opens, changes in severity, and resolves or expires as circumstances change — a job restored may close a food need while a new medical need opens. The system tracks needs across their lifetime, not as a single snapshot."*

The client blueprint independently evidences the same lifecycle in operation (Flow C): an employment life event causes an existing food need to be given an expiry date and its severity revised downward, while an unrelated medical need remains open. Two independent sources, one internal and one client-supplied, describe the same behaviour.

**Need states evidenced:** open; matched to an intervention; fulfilled; expired; resolved by circumstance change. *(Client blueprint uses `open | matched | fulfilled` and `circumstance_resolved`; blueprint §9 uses opens / changes severity / resolves / expires. The union is recorded; no repository source states a canonical enumeration, and none is invented here.)*

## 4. Need Severity

**Insufficient repository evidence for the determination method.** The repository consistently *uses* severity without ever stating how it is judged:

- `GLOSSARY.md` classifies Gap severity as critical / high / medium.
- `case-management/06-business-events.md` has "Risk Escalated: a vulnerability reaches a critical threshold" — threshold unstated.
- `resource-logistics/08-decision-points.md` §2 has Logistics consuming "Case Management vulnerability priority tags" — tags unstated.
- `SHARED_CONCEPT_CATALOG.md` §3 states "Priority is the business ranking applied to a Need" — ranking method unstated.
- The client blueprint uses a numeric `severity_index` (0.0–1.0). **This is not adopted.** `ONTOLOGY_DESIGN.md` Pillar P4 requires confidence and judgement to be qualitative and evidence-traceable rather than an unexplainable score, and the Vulnerability, Risk and Protection domain records that the repository states risk qualitatively seven times over. A numeric severity index would contradict both.

**Recorded as Open Question.** How need severity is determined, and what values it takes, is undiscovered. It is not invented here.

## 5. Need Relationships

`GLOSSARY.md` defines `need_influences_need` as *"a diagnosed connection between two confirmed needs within the same case, distinct from a situation contextualising a need,"* qualified by three types:

- **contributes_to** — the source need drives or worsens the target (income instability contributes_to food insecurity).
- **blocks** — the source must be resolved before the target can be effectively addressed (a documentation gap blocks an income_support need).
- **compounds** — the source increases the target's severity whenever both are present, without causing it (a disability compounds a caregiver_burden need).

`GLOSSARY.md` further states this is mirrored at the synthesized-finding level as `assertion_influences_assertion`.

**Evidence disposition: Carried unvalidated.** These are glossary-only. They are retained because they are the most ontologically consequential relationships in the repository — a foundation that cannot say one need blocks another cannot sequence support — and because discarding them destroys knowledge without replacing it. Recorded as AR-018.

## 6. Intervention Fit at Case Altitude

TD-06 BD-TD06-002 established that Sector is chosen at programme altitude while **Modality is chosen at case altitude**, on grounds of local market feasibility and household appropriateness. This file records what the repository knows about that case-altitude judgement.

- **Intervention Readiness** — `GLOSSARY.md` defines a structured qualitative judgement (ready / partially_ready / not_ready / not_assessed) of *"whether the actual context and capacity for a specific intervention are currently in place for a specific beneficiary or household,"* explicitly distinguished from eligibility (categorical, rule-based), vulnerability (latent susceptibility) and capability (general ability independent of any intervention). This is precisely the case-altitude fit concept FG-6 identified as missing. **Carried unvalidated** — glossary only.
- **Intervention Objective Category** — `GLOSSARY.md`: the underlying humanitarian purpose an intervention serves (survival and stabilization, restoration, capacity building, protective, connective, resilience building), independent of modality and thematic sector. **Carried unvalidated** — glossary only, though structurally consistent with TD-06 BD-TD06-001's insistence that categorisation dimensions are independent.
- **Intervention Relationship** — `GLOSSARY.md` names four: prerequisite, mutually exclusive, reinforces, substitutes. **Carried unvalidated** — glossary only. Structurally the intervention-side counterpart to need relationships.
- **Multi-sectoral fit** — TD-06 BD-TD06-003 (Tier B/D, High confidence) establishes that one intervention may satisfy multiple needs across sectors concurrently, so the need-to-intervention mapping is many-to-many. **This is the only externally corroborated statement in this file.**

## 7. Business Relationships Added

- A **Need** belongs to a **Case**. *(Already in `04-relationships.md`; referenced.)*
- A **Vulnerability** generates a **Need**. *(Already in `04-relationships.md`; referenced.)*
- An **Intervention** addresses a **Need**. *(Already in `04-relationships.md`; referenced. TD-06 BD-TD06-003 establishes the mapping is many-to-many.)*
- A **Need** influences another **Need**, qualified as contributes_to, blocks, or compounds.
- **Intervention Readiness** qualifies the fit between an **Intervention Offering** and a **Household**.
- An **Intervention Offering** is a prerequisite for, mutually exclusive with, reinforces, or substitutes another **Intervention Offering**.
- A **Life Event** causes a **Need** to open, change severity, resolve or expire. *(Blueprint §9; client blueprint Flow C. The Life Event concept is owned by the Human Reality domain.)*

## 8. Open Questions Added

1. How is need severity determined, and what values does it take?
2. What is the canonical set of need states?
3. Are the seven need categories complete, and are they the right cut for the stated applicability context?
4. How is Intervention Readiness assessed, and by whom?
5. Are `need_influences_need` relationships diagnosed by a case worker, or inferred?

## 9. Evidence Disposition Summary

| Statement | Disposition |
|---|---|
| Need is a gap between current state and a basic standard of wellbeing | **Established Fact (Tier C, 2 independent internal sources)** |
| Needs are dynamic — open, change severity, resolve, expire | **Established Fact (Tier C, blueprint §9 + client blueprint Flow C)** |
| Need must be modelled distinctly from Intervention | **Established Fact (Tier C, `SHARED_CONCEPT_CATALOG.md` §3)** |
| One intervention may address needs across multiple sectors | **Finding (Tier B/D, High — TD-06 BD-TD06-003)** |
| Modality is a case-altitude decision | **Finding (Tier B/D, Medium-High — TD-06 BD-TD06-002)** |
| The seven need categories | **Carried unvalidated (single internal source)** — AR-018 |
| Need relationships (contributes_to / blocks / compounds) | **Carried unvalidated (glossary only)** — AR-018 |
| Intervention Readiness, Objective Category, Relationships | **Carried unvalidated (glossary only)** — AR-018 |
| Need severity determination | **Insufficient repository evidence — open** |
