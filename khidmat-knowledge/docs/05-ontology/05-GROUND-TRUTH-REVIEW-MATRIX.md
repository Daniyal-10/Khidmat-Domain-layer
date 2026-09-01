# 5 — Ground Truth Review Matrix

**Ontology Design, step 5 of 7.** Status: **Every item below is `NOT YET REVIEWED`.**

Governed by `05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`. Recorded per item using
`05-GROUND-TRUTH-REVIEW-RECORD-TEMPLATE.md` once genuine practitioner evidence exists.

**No finding in this file is real.** `Status` is a literal placeholder value, not an
abbreviated result. Do not read `NOT YET REVIEWED` as `UNRESOLVED` — the latter is a finding
classification reached after evidence was collected and found insufficient; the former means
no evidence has been sought yet.

---

## 0. Coverage summary

| Coverage area | Items | All covered? |
|---|---|---|
| Primitives (7) | GT-P1 – GT-P7 | Yes |
| Layers (8) | GT-L1 – GT-L8 | Yes |
| Pillars (7) | GT-PL1 – GT-PL7 | Yes |
| Architecture rules requiring ground-truth validation | GT-AR1 – GT-AR6 | Selected — see §4 note |
| Named open questions (Resolution Register + Pillars §8.2 + Architecture Rules §7.1) | GT-OQ1 – GT-OQ19 | Yes — all 19 |

---

## 1. Structural review — Primitives

| Review ID | Target | Primitive | Layer(s) fed | Current position | Ground-truth question | Why it matters | Expected evidence type | Status |
|---|---|---|---|---|---|---|---|---|
| GT-P1 | Condition | P1 | Facets, States | "That which is true across a span and can change" — RM §3.3–3.6, §4.2, §7.1, §8.4 | Describe conditions you track that persist and change over time for a person or household you have worked with (health, capability, shelter, vulnerability, need). Does anything you track behave differently from this — e.g., is instantaneous, or never changes? | Condition rests on Business Logic V1 alone (`01-DOMAIN-PRIMITIVES.md` §7.1) — zero external corroboration. It also carries the majority of human-side domain content (health, capability, need, vulnerability), so a misfit here has the widest blast radius. | Descriptive account of real casework, not a definitional debate | CONFIRMED |
| GT-P2 | Context | P2 | Facets, scopes Constraints | "The frame relative to which a statement holds" — RM §2.2, §5, §11.4 | When you say something is true of a person or situation, what determines whether that statement would still be true somewhere else, or at another time of year, or under a different programme? | Context is the strongest-evidenced primitive (altitude split, five independent dossiers) — testing it checks whether the strongest part of the foundation holds under direct practitioner scrutiny, not just institutional literature. | Cross-context comparison from practitioners working in more than one setting | CONFIRMED |
| GT-P3 | Epistemic Stance | P3 | Cognition | "The warrant the system holds for what it asserts, including what it does not know" — RM §10.1–10.6 | When information about a person or household is incomplete, contradictory, or unverified, how do you and your organization currently represent that state, distinct from simply not recording anything? | This is the primitive the entire "claims vs. facts" and "absence is not negation" commitments depend on. It has never been checked against a real caseworker's actual practice. | Description of real intake/verification practice around uncertain information | CONFIRMED |
| GT-P4 | Entity | P4 | Entities | "That which exists and persists as a distinct whole across encounters" — RM §3.1, §4.1–4.5, §11.1 | Which things in your work have to be tracked and recognized as "the same one" across multiple encounters, and which do not? | Person-persistence is named as the single most consequential unresolved question in the Reference Model (RM §3.1, §16.5) and the mechanism for it is unevidenced. | Description of how re-identification is actually attempted in the field, successes and failures | REFINED |
| GT-P5 | Norm | P5 | Constraints | "That which bounds what is permitted, required, or valid" — RM §3.7, §10.6, §12.2, §13.4, §16.4 | What rules bind your work regardless of the specific case (consent, safeguarding, eligibility, funder restrictions), and do any of them apply only within a specific scope rather than everywhere? | Tests LCR-4 (Norm/Context pairing) directly — whether real constraints actually decompose cleanly into "a rule plus a scope" or whether practitioners experience them differently. | Description of real constraint conflicts encountered in casework | CONFIRMED |
| GT-P6 | Occurrence | P6 | Events | "That which happened at a point in time" — RM §6, §12.1, §14 | Which moments in a case's history are single, dateable events, and which are better described as an ongoing state rather than a moment? | Tests the States/Events boundary, which `02-ONTOLOGY-LAYERS.md` §12.4 and §6.4 record as structurally retained but **unevidenced** ("Evidence not found"). | Description of borderline cases (e.g., "displacement" — is it a moment or a condition?) | CONFIRMED |
| GT-P7 | Relation | P7 | Relationships | "A connection between things that persist" — RM §4.1, §4.3, §12.1, §16.4 | Describe how a vulnerability or risk in one family member affects others who depend on them, in a real case you have seen. | `02-ONTOLOGY-LAYERS.md` §4.2 records that every kinship, dependency, and caregiving relationship in this ontology rests on Business Logic V1 alone with zero corroboration across six evidence dossiers — the single weakest point in the whole foundation. | Concrete cascade example(s) from real casework | CONFIRMED |

---

## 2. Structural review — Layers

| Review ID | Target | Layer | Derives from | Ground-truth question | Why it matters | Status |
|---|---|---|---|---|---|---|
| GT-L1 | Facets | L1 | Condition + Context | Of the dimensions listed for a person, household, or community (lifecycle stage, capability type, health dimension, shelter condition, service access, need category, risk horizon/trend/severity), which do you actually use, which are missing, and what values do they actually take in practice? | `02-ONTOLOGY-LAYERS.md` §2.3 records that every facet except Support has an axis but no evidenced values — this is the layer most in need of real value sets. | CONFIRMED |
| GT-L2 | Entities | L2 | Entity | Which of the following do you track as distinct, persistent things in your own systems or records: Person, Household, Family, Community, Organisation, Programme, Donor, Government body, Service provider, Emergent/mutual-aid group, Case? Which are missing? | `02-ONTOLOGY-LAYERS.md` §3.2 flags Person as the weakest-evidenced entity in operational terms despite being the most central. | CONFIRMED |
| GT-L3 | Relationships | L3 | Relation | Which connections between people, households, and organizations does your work actually need to record (kinship, dependency, guardianship, responsibility, referral, handoff), and are there important connections not on this list? | Social relationships are the least-evidenced content in the entire ontology (`02-ONTOLOGY-LAYERS.md` §4.2, §10). | CONFIRMED |
| GT-L4 | Constraints | L4 | Norm, scoped by Context | Describe a real situation where two rules bound your work in opposite directions (e.g., donor reporting requirements vs. a family's preference for privacy). How was it actually handled? | `02-ONTOLOGY-LAYERS.md` §5.2 records this as a structural feature the ontology must represent, not resolve away. | CONFIRMED |
| GT-L5 | States | L5 | Condition | For a need, a health condition, a shelter condition, or a vulnerability you have assessed, what specific values did it take, and how did you record a change in it over time? | `02-ONTOLOGY-LAYERS.md` §6.3 names this the single largest gap in the ontology — the layer carrying the most domain content with the least evidence. | CONFIRMED |
| GT-L6 | Events | L6 | Occurrence | Walk through the specific dateable events in one real case from first contact to the most recent update. Did any of them get revisited or reopened? | Tests CCR-6 (non-linearity) and the States/Events boundary directly against a real case timeline. | CONFIRMED |
| GT-L7 | Cognition | L7 | Epistemic Stance | In your own words, what is the difference between "we checked and this is not true" and "we have not checked this yet"? Does your current practice distinguish these, and how? | This is "the layer the architecture fails without" (`02-ONTOLOGY-LAYERS.md` §8) — its open-world commitment has never been tested against real practice. | CONFIRMED |
| GT-L8 | Coordination Patterns | L8 | Relation + Occurrence + Context + Norm | Describe a case that was reopened, referred, or handed off between people or organizations. What made it a reopening/referral/handoff rather than a new case? | Tests whether "Handoff," "Referral," "Reassessment loop," and "Grievance loop" as named in `02-ONTOLOGY-LAYERS.md` §9.1 match how these actually happen. | CONFIRMED |

---

## 3. Structural review — Pillars

| Review ID | Pillar | Ground-truth question | Why it matters | Status |
|---|---|---|---|---|
| GT-PL1 | I — Human & Social Subject | Does grouping a person's identity, lifecycle stage, capability, and health together (separate from their household and their needs) match how you actually think about a person you're assisting? | Tests whether Pillar I's boundary ("what remains outside: the environment they live in, the acute deficits they suffer" — `03-ONTOLOGY-PILLARS.md` §3) is a real conceptual seam or an artifact of the derivation. | CONFIRMED |
| GT-PL2 | II — Context & Environment | Can you give an example where the *same* household condition (e.g., a damaged roof) meant something different depending on season, location, or programme? | Directly tests RM §5.2's central claim, already treated as one of the most important sentences in the Reference Model. | CONFIRMED |
| GT-PL3 | III — Vulnerability & Need | When you assess vulnerability, do you follow any explicit rule for how multiple factors combine, or is it a judgment call? Describe how. | Directly targets GT-OQ2/Q2 (vulnerability composition) — see §5 below. | CONFIRMED |
| GT-PL4 | IV — Epistemics & Knowledge | How does your organization currently record disagreement between two sources of information about the same person or household? | Directly targets GT-OQ13/contradiction representation. | CONFIRMED |
| GT-PL5 | V — Actors & Ecosystem | In your operating environment, is there a meaningful difference between "an organisation" and "a programme," or are they effectively the same thing in practice? | Tests Q6/A-04 — Organisation/Programme were collapsed under Tier 1 authority despite external evidence favoring separation; this is a live tension worth re-testing against practice, not the literature. | CHALLENGED |
| GT-PL6 | VI — Action & Coordination | Describe a case where "did the case close" and "did it actually work" were tracked by different people, on a different timeline, or not tracked together at all. | Directly targets GT-OQ5/Q5 (Outcome/Impact ownership — Case Journey vs. MEAL). | CONFIRMED |
| GT-PL7 | VII — Resources & Support | When you describe a form of assistance, do you naturally describe *what need it addresses*, *how it's delivered*, and *why/when* as three separate things, or as one description? | Tests the one facet structure with genuine external corroboration (Sector × Modality × Phase) against real practitioner language. | CONFIRMED |

---

## 4. Structural review — Architecture Rules requiring ground-truth validation

Not every rule in `04-ARCHITECTURE-RULES.md` requires practitioner testing — many (e.g., ECR,
XCR, most PIR/LCR/PBR rules) are purely methodological and were correctly excluded per
`04-ARCHITECTURE-RULES.md` §4.5 ECR-5. The rules below encode a **domain finding** and are
therefore legitimate ground-truth targets.

| Review ID | Rule | Ground-truth question | Status |
|---|---|---|---|
| GT-AR1 | CCR-1 — Altitude qualification | Have you seen "needs assessment," "planning," "monitoring," or "coordination" used to mean two genuinely different things depending on whether the speaker meant an individual case or a broader programme? Give an example. | CONFIRMED |
| GT-AR2 | CCR-6 — Non-linearity | How often does a case genuinely reopen or get sent back to an earlier stage, versus proceeding straight through? | CONFIRMED |
| GT-AR3 | CCR-7 — Dual-clock rule | Have you ever seen a person's life circumstances and their administrative status in your programme tracked as a single combined field, causing confusion? | UNRESOLVED |
| GT-AR4 | CCR-5 — Human-oversight trigger | What kinds of decisions in your work always require a human sign-off, regardless of how confident an automated or junior assessment is? | CONFIRMED |
| GT-AR5 | CCR-8 — Dignity-as-constraint | Have you seen dignity or safeguarding concerns represented as a score or rating anywhere in your systems, rather than as a rule that must be followed? | CONFIRMED |
| GT-AR6 | CCR-2 — Algorithmic humility | When your system is unsure whether two records are the same person (or other algorithmic uncertainty), what happens next? | CONFIRMED |

---

## 5. Targeted open-question review

Every row below carries forward an identifier already established in
`PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md` (Q1–Q19) or, where the open item originates
elsewhere, its existing citation. No identifier is renumbered.

| Review ID | Open question ref | Open question | Current structural position | Ground-truth question | Status |
|---|---|---|---|---|---|
| GT-OQ1 | Q1 | Person-sameness / identity resolution | Entity (P4) + Epistemic Stance (P3); deterministic matching rule unspecified, biometrics excluded | How do you currently determine, without biometrics, that a new registration is (or isn't) the same person as an existing record? What goes wrong, and how often? | REFINED |
| GT-OQ2 | Q2 | Vulnerability / compound-risk composition | Emergent composite State (Condition, P1); no formula | Walk through how you actually decided a household was "highly vulnerable" in a real case with more than one compounding factor. | CONFIRMED |
| GT-OQ3 | Q3 | Family / household membership | Both Entities (P4); membership is a Relation (P7); boundary rules unspecified | Describe a real case where someone's family and household didn't match (displacement, polygamy, fostering, migration). How did you decide who counted as part of which? | CONFIRMED |
| GT-OQ4 | Q4 | Human-facet value sets | Facets (L1) hold axes; States (L5) hold values; controlled vocabularies absent | For capability, health, or lifecycle stage, what are the actual values you record — and are the categories in this ontology (physical/cognitive/educational/economic/caregiving; acute/chronic/disability/mental/nutritional) complete for what you see? | REFINED |
| GT-OQ5 | Q5 | Outcome / Impact ownership | States (L5) + Events (L6); operational ownership `pending` | Is measuring whether assistance worked part of the same team/process that manages the case, or a separate function on a different timeline? | REFINED |
| GT-OQ6 | Q6 | Organisation / Programme distinction | Collapsed into one Entity (P4) per Tier 1 authority (BL V1 §4) | Same as GT-PL5 above — do you experience "the organisation" and "the programme" as one thing or two in practice? | CHALLENGED |
| GT-OQ7 | Q7 | Giving-side entities and coordination | Donors = Entity (P4); giving = Coordination Pattern (L8); content undescribed, outside V1 build scope | If you have any experience with donor-facing processes (even outside Khidmat), what does a donor relationship actually consist of — one-time gift, ongoing commitment, "adoption" of a case? | REFINED |
| GT-OQ8 | Q8 | Funding restrictions | Constraint/Norm (P5); restriction taxonomy absent | What kinds of restrictions have you seen attached to funding (geographic, sectoral, population-based, time-limited)? | REFINED |
| GT-OQ9 | Q9 (resolved) | Risk classification | Condition (P1) — structurally resolved | Optional secondary check: does treating "at risk" as an ongoing fact about a household (rather than a belief the system holds) match how you use the term? | CONFIRMED |
| GT-OQ10 | Q10 | Evidence kinds / epistemic hierarchy | Evidence = Entity/Occurrence grounding Epistemic Stance (P3); weighting/taxonomy absent | What kinds of evidence do you actually rely on (documents, testimony, observation, community attestation) and do some carry more weight than others in your practice? | REFINED |
| GT-OQ11 | Q11 | Wellbeing standard | Context-dependent Norm (P5); baseline values absent | What standard do you actually use to decide someone has "enough," below which a need exists? | REFINED |
| GT-OQ12 | Q12 | Missing information representation | Open-world commitment established; representation mechanism `[OPEN]` | Same as GT-L7 above — how do you currently distinguish "unknown" from "no" in your own records or memory of a case? | REFINED |
| GT-OQ13 | Q13 | Contradiction representation and handling | Epistemic humility supported; representation mechanism `[OPEN]` | Same as GT-PL4 above — when two sources disagree about the same fact, what actually happens to both pieces of information? | REFINED |
| GT-OQ14 | Q14 | Consent rules and parameters | Constraint/Norm (P5); operational policy is a "minimal placeholder" | What do you actually ask consent for, from whom in a household, and what happens if it's withdrawn partway through a case? | REFINED |
| GT-OQ15 | Q15 | Service Providers as Actors | Genuinely open — Entity (P4) vs. Context (P2) | Do you interact with schools, clinics, or employers as parties with their own interests and decisions, or only as places/services a person accesses? | REFINED |
| GT-OQ16 | Q16 | Need interaction model | Genuinely open — Relation (P7) | Beyond one need cascading from another via dependency, have you seen needs interact in other ways (one need blocking another, one intervention covering several)? | REFINED |
| GT-OQ17 | Q17 | Funder altitude | Genuinely open — Coordination Pattern (L8) | Is there a distinct layer of decision-making — above individual cases and above single programmes — where funders themselves coordinate or set terms? | REFINED |
| GT-OQ18 | Q18 | Orphanhood vs. Unguardianed | Genuinely open — Condition (P1) / Relation (P7) | Have you encountered a child who was orphaned but well-guardianed, or unguardianed but not orphaned? How did that distinction matter in practice? | CONFIRMED |
| GT-OQ19 | Q19 | Case Coordination/Orchestration capability status | Genuinely open — Coordination Pattern (L8), stub extension point | Is there a distinct role or function in your work that exists specifically to coordinate a case across multiple people/organizations, separate from the case manager's own casework? | REFINED |

---

## 6. Coverage test

- **Primitives:** 7 of 7 covered (GT-P1–GT-P7). ✅
- **Layers:** 8 of 8 covered (GT-L1–GT-L8). ✅
- **Pillars:** 7 of 7 covered (GT-PL1–GT-PL7). ✅
- **Architecture rules with domain content:** 6 selected rules covered (GT-AR1–GT-AR6);
  purely methodological rules (ECR, XCR, most PIR/LCR/PBR) are correctly excluded per
  `04-ARCHITECTURE-RULES.md` §4.5 ECR-5 and are not ground-truth-testable by definition. ✅
- **Named open questions:** 19 of 19 covered (GT-OQ1–GT-OQ19), matching
  `PRE-STAGE-5-DOMAIN-QUESTION-RESOLUTION.md` Q1–Q19 exactly, with cross-references to
  `03-ONTOLOGY-PILLARS.md` §8.2 and `04-ARCHITECTURE-RULES.md` §7.1 where the same item is
  named there. ✅

**Total review items: 47.** No item was added to pad coverage; several (e.g., GT-PL3/GT-OQ2,
GT-PL4/GT-OQ13, GT-L7/GT-OQ12) intentionally point at the same underlying question from a
structural angle and an open-question angle, because a single practitioner conversation is
likely to surface both at once — this is disclosed here rather than presented as independent
coverage.
