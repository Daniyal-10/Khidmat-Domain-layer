# Outcome Semantics

> **Added under remediation B5**, closing the outcome portion of Foundation Gap FG-6.
> FG-6 recorded that this domain holds Baseline, Endline, Indicator and Logframe — all **programme altitude** — while no repository source states what an outcome *is* for a person, or what "worked" means.
>
> **Sources:** `98-archive/execution_cleanup/BUSINESS_ARCHITECTURE_BLUEPRINT.md` §13; `GLOSSARY.md` Outcome Terms and Beneficiary Lifecycle Terms; `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch7; `PROJECT_OVERVIEW.md` Ch9.2; `CONSTITUTION.md` Article XIII.
> **Tier A, B and D were not executed.**

---

## 1. What an Outcome Is

Blueprint §13 states the governing distinction directly: *"The goal is not case closure. The goal is improved human wellbeing."* This is the same distinction `GLOSSARY.md` draws between **Engagement Stage** (administrative relationship to the ecosystem) and **Human Development Stage** (the person's own position in the humanitarian developmental trajectory — crisis, stabilization, recovery, self-reliance, resilience, community contribution), which it states must *never* be conflated. `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch3 restates it with a worked case: a person may be actively enrolled while in acute crisis, or graduated to self-reliance and exited.

Three independent internal sources agree. **Established Fact (Tier C).**

`GLOSSARY.md` defines **Outcome Indicator** as *"a measurable signal used to assess whether an intervention produced meaningful change in a beneficiary, family, household, or community."*

## 2. Outcome Categories

Blueprint §13 names four:

| Category | Content as evidenced |
|---|---|
| **Health outcomes** | recovery, stability |
| **Educational outcomes** | continued schooling |
| **Economic outcomes** | sustainable income |
| **Family outcomes** | reduced dependency |

**Carried unvalidated** — single internal source. Recorded as AR-018.

These are the case-altitude counterpart to the ecosystem-level success measures in `PROJECT_OVERVIEW.md` Ch9.2 and `CONSTITUTION.md` Article XIII, which are explicitly *ecosystem outcomes, not application-level KPIs*. The two altitudes are distinct and neither substitutes for the other.

## 3. The Developmental Trajectory

`GLOSSARY.md` enumerates the Human Development Stage progression: **crisis → stabilization → recovery → self-reliance → resilience → community contribution.** This is the case-altitude outcome trajectory — what "improvement" means for a person, expressed as movement along it.

`case-management/07-business-lifecycles.md` carries an abbreviated form (Acute Crisis, Stabilized, Resilient). The two are consistent; the glossary form is the fuller one.

**Insufficient repository evidence:** no source states what evidence moves a person from one stage to the next. The stages are evidenced; the transition criteria are not.

## 4. What "Worked" Means — Explicitly Unresolved

This sub-question of FG-6 **cannot be closed from repository evidence, and is not closed here.**

The repository states this plainly and repeatedly, and the honest action under the remediation instructions is to record it rather than fill it:

- `HUMANITARIAN_BUSINESS_REFERENCE_MODEL.md` Ch7 carries a standing Open Discovery Assumption: *"The specific, informal criteria the client and domain team currently use in practice to judge whether an intervention 'worked' (prior to formal outcome indicators) remains an unresolved discovery topic."*
- `ASSUMPTION_REGISTER.md` **AR-011** records the same, with the overturn condition "Tier A practitioner evidence detailing the actual informal success criteria used by the domain team." That condition has not been met.
- `case-management/10-open-questions.md` asks it independently: *"What are the exact informal criteria practitioners use to determine if an intervention 'worked' prior to formal reassessment?"*
- Blueprint §13 concedes the same limitation from the opposite direction: *"V1 can record that assistance occurred but cannot yet measure whether it worked."*

Four independent repository sources agree that this is unknown. Supplying an answer would be inventing business knowledge, which the remediation instructions prohibit and which `ONTOLOGY_DESIGN.md` §6 would reject as unevidenced. **AR-011 remains open** and is the reason this portion of B5 is classified as partially deferred rather than resolved.

## 5. The Attribution Problem

`08-decision-points.md` §3 (Impact Conclusion Decision) already records the constraint: *"Difficult to prove causality (did we cause the improvement, or did the economy recover?)"* and *"High statistical margins of error in conflict zones."* `KNOWLEDGE_TRANSFORMATION_PATTERNS.md` §4.2 records the organisational consequence: this uncertainty *"often leads Programme Management to resist mandatory adaptations."*

This is recorded as an established constraint on outcome measurement, not a gap. It is real and will not be resolved by better modelling.

## 6. Business Relationships Added

- An **Outcome Indicator** measures change in a **Person**, **Family**, **Household** or **Community**. *(`GLOSSARY.md`.)*
- A **Human Development Stage** transition evidences an **Outcome**.
- An **Outcome** is distinct from, and may diverge from, an **Engagement Stage** transition. *(`GLOSSARY.md`; HBRM Ch3.)*
- A **Baseline** is compared against an **Endline**. *(Already in `04-relationships.md`; referenced.)*

## 7. Open Questions Added

1. What evidence moves a person from one Human Development Stage to the next?
2. What are the informal criteria by which practitioners judge that an intervention worked? *(AR-011 — open, blocked on Tier A.)*
3. Are the four outcome categories complete?
4. At what interval, and by whom, is a person's development stage re-assessed?

## 8. Evidence Disposition Summary

| Statement | Disposition |
|---|---|
| Outcome is improved human wellbeing, not case closure | **Established Fact (Tier C, 3 independent internal sources)** |
| Engagement Stage and Human Development Stage must never be conflated | **Established Fact (Tier C, glossary + HBRM Ch3 + case-management/07)**; externally corroborated in shape by TD-03 BD-TD03-002 |
| The six-stage developmental trajectory | **Carried unvalidated (glossary only)** — AR-018 |
| The four outcome categories | **Carried unvalidated (single internal source)** — AR-018 |
| Causal attribution of outcomes is genuinely hard | **Established constraint (Tier C, 2 internal sources)** |
| What "worked" means | **Insufficient repository evidence — AR-011 remains OPEN** |
