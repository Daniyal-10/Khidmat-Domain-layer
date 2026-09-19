# Stage 5 Ground Truth Review Finalization Proposal

## 1. Actual Repository State
- **Current Branch**: `stage5-gtr-finalization`
- **Git Status**: Clean (no uncommitted changes)
- **Current HEAD**: `dc53efebd64283609f02246d2ac55e81ba4ae5e2`
- **Files Inspected**: `all_answers.md`, `MASTER-GTR-INTERVIEW-FLOW.md`, `05-GROUND-TRUTH-REVIEW-MATRIX.md`, 47 GTR records.
- **Files that do not exist**: `10-ONTOLOGY-RECONCILIATION-CLOSURE-REPORT.md`.

## 2. 47-Row Evidence Trace

### GT-P1
- **Question**: Describe conditions you track that persist and change over time for a person or household you have worked with (health, capability, shelter, vulnerability, need). Does anything you track behave differently from this — e.g., is instantaneous, or never changes?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "The volunteers estimate the donation amt (based on what they asked and how much they really should get to fullfill the need)... jo requirements survey mai aati h jo woh khete hai agau unse woh ground reaility match nhi hoti h toh usko reject kardiya jata h aur agar sab geniune hota h tabhi aage form fill kiya jaaata h"
- **R1 Evidence**: We track food, medical, shelter, education needs. They persist and change over time (e.g. medical can be one-time or ongoing). Zakaat eligibility and income are also tracked.

### GT-P2
- **Question**: When you say something is true of a person or situation, what determines whether that statement would still be true somewhere else, or at another time of year, or under a different programme?
- **Current Classification** (Matrix/Master/R1): CONTEXT_DEPENDENT / NOT_ASSESSABLE / CONTEXT_DEPENDENT
- **Master Answer**: "NO we dont cover the seasonal things are not covered. And not the pandemic situations also"
- **R1 Evidence**: Khidmat operates in Bhopal and 100-200 km near this city. We don't have multiple locations or programs. The concept of cross-context variability is not exercised here.

### GT-P3
- **Question**: When information about a person or household is incomplete, contradictory, or unverified, how do you and your organization currently represent that state, distinct from simply not recording anything?
- **Current Classification** (Matrix/Master/R1): MISSING / UNRESOLVED / MISSING
- **Master Answer**: "unknown here is nothing about the case which is not much requried in this case... The volunteer will reject the case as not genuine case"
- **R1 Evidence**: 'the volunteer will reject the case as not genuine'. 'First we dont register who dont have the documents'. They don't represent uncertainty; they resolve it before registering, or reject.

### GT-P4
- **Question**: Which things in your work have to be tracked and recognized as "the same one" across multiple encounters, and which do not?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Firstly we dont register who dont have the documents available and secondly they can be determine by the beneficary ID contact no, family members the deaitls we take in the survey form"
- **R1 Evidence**: 'The Beneficiary ID (Unique ID) should be there , as there can be similar name or identity mismatch'. Re-identification is explicitly handled.

### GT-P5
- **Question**: What rules bind your work regardless of the specific case (consent, safeguarding, eligibility, funder restrictions), and do any of them apply only within a specific scope rather than everywhere?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "We don't help the beggers... Yes donors have limit to donate is some cases so that the needy once don't become too much dependent on other... NO we dont cover the seasonal things are not covered"
- **R1 Evidence**: Rules apply regardless of case: 'We don't help the beggers', 'medicals proofs... of government hospital are considered true only', 'donors have limit to donate'.

### GT-P6
- **Question**: Which moments in a case's history are single, dateable events, and which are better described as an ongoing state rather than a moment?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "also medical needs are of one time and long also soo they can be if one time then help via the donors and then closed if recusisng like medicens they can conitnue"
- **R1 Evidence**: 'medical needs are of one time and long also soo they can be if one time then help via the donors and then closed if recusisng like medicens they can conitnue'. Clear boundary between event and ongoing state.

### GT-P7
- **Question**: Describe how a vulnerability or risk in one family member affects others who depend on them, in a real case you have seen.
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Family members details Name gender age relation particular... ofcs these are only considered without metnioning explicitly in the sys but when we are telling the too much needy and also dont have a earning member that directly make their prioirty high"
- **R1 Evidence**: 'when we are telling the too much needy and also dont have a earning member that directly make their prioirty high'. Dependency and lack of an earning member directly affects vulnerability.

### GT-L1
- **Question**: Of the dimensions listed for a person, household, or community (lifecycle stage, capability type, health dimension, shelter condition, service access, need category, risk horizon/trend/severity), which do you actually use, which are missing, and what values do they actually take in practice?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Beneficiary detilas... Name... Age... gender... Hosue : Own Rental... monthly income... zakaat eligible: yes/no... Requirements 1. 2. 3. 4." + "Mostly the needs are here in the Food, Shelter, Medical, Education"
- **R1 Evidence**: Dimensions tracked: Age, gender, housing (own/rental), zakaat eligible, monthly income, specific requirements (food, shelter, medical, education).

### GT-L2
- **Question**: Which of the following do you track as distinct, persistent things in your own systems or records: Person, Household, Family, Community, Organisation, Programme, Donor, Government body, Service provider, Emergent/mutual-aid group, Case? Which are missing?
- **Current Classification** (Matrix/Master/R1): CONTEXT_DEPENDENT / CONFIRMED / CONTEXT_DEPENDENT
- **Master Answer**: "Mostly families are covered as we are taking about the help of the family based... head of the family (zimmedar) is noted in the beneficary for the family... Family members details Name gender age relation particular... Also 2 3 vendors are there... Donors can make the donation via the cards"
- **R1 Evidence**: They track Person, Family ('zimmedar', members), Donor. Do NOT track Organisation/Programme ('just the khidmat grp doing the root work').

### GT-L3
- **Question**: Which connections between people, households, and organizations does your work actually need to record (kinship, dependency, guardianship, responsibility, referral, handoff), and are there important connections not on this list?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Family members details Name gender age relation particular"
- **R1 Evidence**: Record kinship explicitly ('relation: mother, wife, son, daughter').

### GT-L4
- **Question**: Describe a real situation where two rules bound your work in opposite directions (e.g., donor reporting requirements vs. a family's preference for privacy). How was it actually handled?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "When the family is trying to keep the information which is required to fill the survey form or the documents, we don't process them forward. They are rejected in the volunteer verification."
- **R1 Evidence**: 'about the family privacy concern too much to hide... only if they are too much concern still they tell in khidmat... they needs to tell about the 3 4 more people'. Privacy preference bounds against verification requirement.

### GT-L5
- **Question**: For a need, a health condition, a shelter condition, or a vulnerability you have assessed, what specific values did it take, and how did you record a change in it over time?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Mostly the needs are here in the Food Shelter Medical Education... The volunteers estimate the donation amt (based on what they asked and how much they really should get to fullfill the need)"
- **R1 Evidence**: Needs tracked as Food, Shelter, Medical, Education. Earning members taking longer -> food assistance continues (change over time).

### GT-L6
- **Question**: Walk through the specific dateable events in one real case from first contact to the most recent update. Did any of them get revisited or reopened?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "first the survey is done... then those beneficary are visited by the volunteers... the form goes is uploaded in a grp... the donors adopt the beneifcary... The donor and the beneficiary has this card to track the delivery... On which the delivery signatures are taken... about the reverifcation mostly the families and the needy once that we help are too humble families soo there earning members maybe take more longer"
- **R1 Evidence**: Specific timeline: Survey -> volunteer visit/verification -> upload to donor group -> donor adoption -> fulfillment -> tracking card signatures.

### GT-L7
- **Question**: In your own words, what is the difference between "we checked and this is not true" and "we have not checked this yet"? Does your current practice distinguish these, and how?
- **Current Classification** (Matrix/Master/R1): MISSING / UNRESOLVED / MISSING
- **Master Answer**: "unknown here is nothing about the case which is not much requried in this case... The volunteer will reject the case as not genuine case"
- **R1 Evidence**: 'unknown here is nothing about the case which is not much requried'. They do not record missing information, they require documents to proceed.

### GT-L8
- **Question**: Describe a case that was reopened, referred, or handed off between people or organizations. What made it a reopening/referral/handoff rather than a new case?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "uploaded in a grp where the donors are there and then here the first come first server is who says that he will help them they are taken as resposible for that particaulr beneficary... The donor and the beneficiary has this card to track the delivery"
- **R1 Evidence**: 'if recusisng like medicens they can conitnue'. Recurring cases are supported.

### GT-PL1
- **Question**: Does grouping a person's identity, lifecycle stage, capability, and health together (separate from their household and their needs) match how you actually think about a person you're assisting?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Khidmat from layout (what data is taken ) Beneficiary detilas date: beneficary photo... zakaat eligible: yes/no... monthly income:..."
- **R1 Evidence**: Form groups Person details (Age, gender, photo) separately from Household context (House: Own/Rental, Address).

### GT-PL2
- **Question**: Can you give an example where the *same* household condition (e.g., a damaged roof) meant something different depending on season, location, or programme?
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / NOT_ASSESSABLE / NOT_ASSESSABLE
- **Master Answer**: "NO we dont cover the seasonal things are not covered. And not the pandemic situations also"
- **R1 Evidence**: 'NO we dont cover the seasonal things are not covered. And not the pandemic situations also'. Seasonal or location changes not tested.

### GT-PL3
- **Question**: When you assess vulnerability, do you follow any explicit rule for how multiple factors combine, or is it a judgment call? Describe how.
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "its done on the ground verification and the multiple needs the volutneer decides that based on the ground review and that is mentioned in the case summary"
- **R1 Evidence**: 'its done on the ground verification and the multiple needs the volutneer decides that based on the ground review'. It is a judgment call by the volunteer, no mathematical formula.

### GT-PL4
- **Question**: How does your organization currently record disagreement between two sources of information about the same person or household?
- **Current Classification** (Matrix/Master/R1): MISSING / NOT_ASSESSABLE / MISSING
- **Master Answer**: "we only send a experienced volunteer to the beneficary based on the lead survey so why we will have conflit on the, never happned"
- **R1 Evidence**: 'never happned'. They send an experienced volunteer to verify, so no conflict reaches the system.

### GT-PL5
- **Question**: In your operating environment, is there a meaningful difference between "an organisation" and "a programme," or are they effectively the same thing in practice?
- **Current Classification** (Matrix/Master/R1): CONTEXT_DEPENDENT / NOT_ASSESSABLE / CONTEXT_DEPENDENT
- **Master Answer**: "NO organisations and programs are involved in this just the khidmat grp doing the root work"
- **R1 Evidence**: 'NO organisations and programs are involved in this just the khidmat grp doing the root work'. They do not experience the distinction.

### GT-PL6
- **Question**: Describe a case where "did the case close" and "did it actually work" were tracked by different people, on a different timeline, or not tracked together at all.
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / UNRESOLVED / NOT_ASSESSABLE
- **Master Answer**: **Final Status:**
UNRESOLVED
- **R1 Evidence**: Tracking card used by donor and beneficiary. Delivery tracked on the card. 'Did it work' is not explicitly separated from fulfillment.

### GT-PL7
- **Question**: When you describe a form of assistance, do you naturally describe *what need it addresses*, *how it's delivered*, and *why/when* as three separate things, or as one description?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / UNRESOLVED / CONFIRMED
- **Master Answer**: **Final Status:**
UNRESOLVED
- **R1 Evidence**: Need and assistance are bundled but distinct: 'medical, monthly grocery aur rent mein help ki zaroorat hai... jo ap direct contact karke bhi help kar sakte hai ya khidmat ke zariye'.

### GT-AR1
- **Question**: Have you seen "needs assessment," "planning," "monitoring," or "coordination" used to mean two genuinely different things depending on whether the speaker meant an individual case or a broader programme? Give an example.
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / NOT_ASSESSABLE / NOT_ASSESSABLE
- **Master Answer**: "NO organisations and programs are involved in this just the khidmat grp doing the root work"
- **R1 Evidence**: No programmes exist in this operation.

### GT-AR2
- **Question**: How often does a case genuinely reopen or get sent back to an earlier stage, versus proceeding straight through?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "about the reverifcation mostly the families and the needy once that we help are too humble families soo there earning members maybe take more longer and even if they have still some time we help them with the bare minimum need to food"
- **R1 Evidence**: 'if recusisng like medicens they can conitnue'. Also reverification if earning member takes longer.

### GT-AR3
- **Question**: Have you ever seen a person's life circumstances and their administrative status in your programme tracked as a single combined field, causing confusion?
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / NOT_ASSESSABLE / NOT_ASSESSABLE
- **Master Answer**: "NOt heppend"
- **R1 Evidence**: Not addressed in the evidence.

### GT-AR4
- **Question**: What kinds of decisions in your work always require a human sign-off, regardless of how confident an automated or junior assessment is?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / NOT_ASSESSABLE / CONFIRMED
- **Master Answer**: **Final Status:**
NOT_ASSESSABLE
- **R1 Evidence**: 'its done on the ground verification... the volutneer decides that based on the ground review'. Humans make the decisions.

### GT-AR5
- **Question**: Have you seen dignity or safeguarding concerns represented as a score or rating anywhere in your systems, rather than as a rule that must be followed?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Yes. They shouldn't be disrespected. We don't share the information unnecessarily anywhere. They are shared only in the group of the donors so they can help them, that's it."
- **R1 Evidence**: 'about the family privacy concern too much to hide... still they tell in khidmat'. It's handled as a constraint and discussion, not a score.

### GT-AR6
- **Question**: When your system is unsure whether two records are the same person (or other algorithmic uncertainty), what happens next?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Firstly we dont register who dont have the documents available and secondly they can be determine by the beneficary ID contact no, family members the deaitls we take in the survey form"
- **R1 Evidence**: 'The Beneficiary ID (Unique ID) should be there , as there can be similar name or identity mismatch'. Identification issues are handled explicitly.

### GT-OQ1
- **Question**: How do you currently determine, without biometrics, that a new registration is (or isn't) the same person as an existing record? What goes wrong, and how often?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "The Beneficiary ID (Unique ID) should be there , as there can be similar name or identity mismatch... all docs and the things are taken which is menitoned in the form and then we are working on the beneficary ids so this solves the id issues"
- **R1 Evidence**: Beneficiary ID, contact no, family members details, aadhar/voter id. 'we dont register who dont have the documents available'.

### GT-OQ2
- **Question**: Walk through how you actually decided a household was "highly vulnerable" in a real case with more than one compounding factor.
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "its done on the ground verification and the multiple needs the volutneer decides that based on the ground review and that is mentioned in the case summary"
- **R1 Evidence**: Volunteer decides based on ground review and writes in case summary. No formula.

### GT-OQ3
- **Question**: Describe a real case where someone's family and household didn't match (displacement, polygamy, fostering, migration). How did you decide who counted as part of which?
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / CONFIRMED / NOT_ASSESSABLE
- **Master Answer**: "Mostly families are covered as we are taking about the help of the family based and verified persons. Household condition can be considered (for the family only) but it is rare and its the volunteer take... when the need is genral like the food so the head of the family (zimmedar) is noted in the beneficary for the family"
- **R1 Evidence**: They take 'Family members details' and 'House: Own/Rental', but do not detail complex boundary cases.

### GT-OQ4
- **Question**: For capability, health, or lifecycle stage, what are the actual values you record — and are the categories in this ontology (physical/cognitive/educational/economic/caregiving; acute/chronic/disability/mental/nutritional) complete for what you see?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / UNRESOLVED / CONFIRMED
- **Master Answer**: **Final Status:**
UNRESOLVED
- **R1 Evidence**: 'accident mein spinal cord mein multiple injuries', 'widow', 'study'. Form captures precise life and health values.

### GT-OQ5
- **Question**: Is measuring whether assistance worked part of the same team/process that manages the case, or a separate function on a different timeline?
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / UNRESOLVED / NOT_ASSESSABLE
- **Master Answer**: **Final Status:**
UNRESOLVED
- **R1 Evidence**: Outcome tracking not distinct from fulfillment.

### GT-OQ6
- **Question**: Same as GT-PL5 above — do you experience "the organisation" and "the programme" as one thing or two in practice?
- **Current Classification** (Matrix/Master/R1): CONTEXT_DEPENDENT / NOT_ASSESSABLE / CONTEXT_DEPENDENT
- **Master Answer**: "NO organisations and programs are involved in this just the khidmat grp doing the root work"
- **R1 Evidence**: 'NO organisations and programs are involved in this just the khidmat grp doing the root work'.

### GT-OQ7
- **Question**: If you have any experience with donor-facing processes (even outside Khidmat), what does a donor relationship actually consist of — one-time gift, ongoing commitment, "adoption" of a case?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "there the donors adopt the beneifcary... also from the donor side asper the needed decided doantions the donors can combine or split to help the beneficaries... Donors can make the donation via the cards"
- **R1 Evidence**: Donors adopt beneficiary from the group. They can combine or split donations. Can send proxy. Have limits to prevent dependency. Tracking card used.

### GT-OQ8
- **Question**: What kinds of restrictions have you seen attached to funding (geographic, sectoral, population-based, time-limited)?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "zakaat eligible: yes/no... We don't help the beggers... Yes donors have limit to donate is some cases so that the needy once don't become too much dependent on other"
- **R1 Evidence**: 'Yes donors have limit to donate is some cases so that the needy once don't become too much dependent on other'. Restrictions exist.

### GT-OQ9
- **Question**: Optional secondary check: does treating "at risk" as an ongoing fact about a household (rather than a belief the system holds) match how you use the term?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "ofcs these are only considered without metnioning explicitly in the sys but when we are telling the too much needy and also dont have a earning member that directly make their prioirty high"
- **R1 Evidence**: Priority is implicitly high when too much needy/no earning member. Handled via case summary, treated as a fact of the case.

### GT-OQ10
- **Question**: What kinds of evidence do you actually rely on (documents, testimony, observation, community attestation) and do some carry more weight than others in your practice?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / NOT_ASSESSABLE / CONFIRMED
- **Master Answer**: "The medicals proofs (reports, prescreptions) of government hospital are considered true only so no double verification from hospitals are needed... evidence when the volunteer visted them and verifired them , their claims about the needs and confims it"
- **R1 Evidence**: Government hospital reports/prescriptions considered true. Aadhar, Voter ID, Ayushman. Volunteer ground verification.

### GT-OQ11
- **Question**: What standard do you actually use to decide someone has "enough," below which a need exists?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Below the poverty line. Extremely needy mostly... zakaat eligible: yes/no... Yes donors have limit to donate is some cases so that the needy once don't become too much dependent on other"
- **R1 Evidence**: Standard involves checking: 'Below the poverty line', 'Extremely needy mostly', 'Widow cases', 'No income'. Ground reality must match claimed requirement.

### GT-OQ12
- **Question**: Same as GT-L7 above — how do you currently distinguish "unknown" from "no" in your own records or memory of a case?
- **Current Classification** (Matrix/Master/R1): MISSING / UNRESOLVED / MISSING
- **Master Answer**: "unknown here is nothing about the case which is not much requried in this case... The volunteer will reject the case as not genuine case"
- **R1 Evidence**: 'unknown here is nothing about the case which is not much requried'. Unknowns are not represented.

### GT-OQ13
- **Question**: Same as GT-PL4 above — when two sources disagree about the same fact, what actually happens to both pieces of information?
- **Current Classification** (Matrix/Master/R1): MISSING / NOT_ASSESSABLE / MISSING
- **Master Answer**: "we only send a experienced volunteer to the beneficary based on the lead survey so why we will have conflit on the, never happned"
- **R1 Evidence**: 'never happned' regarding conflict. Disagreement is resolved prior to entry.

### GT-OQ14
- **Question**: What do you actually ask consent for, from whom in a household, and what happens if it's withdrawn partway through a case?
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / UNRESOLVED / NOT_ASSESSABLE
- **Master Answer**: **Final Status:**
UNRESOLVED
- **R1 Evidence**: No formal withdrawal mentioned, only initial privacy concerns.

### GT-OQ15
- **Question**: Do you interact with schools, clinics, or employers as parties with their own interests and decisions, or only as places/services a person accesses?
- **Current Classification** (Matrix/Master/R1): CONFIRMED / CONFIRMED / CONFIRMED
- **Master Answer**: "Also 2 3 vendors are there connected with them so the beneficiary can visit them and take the ration (from the card)"
- **R1 Evidence**: Connect with vendors for ration. Beneficiary visits them. Government hospitals are trusted evidence sources. Vendors act as distinct service providers.

### GT-OQ16
- **Question**: Beyond one need cascading from another via dependency, have you seen needs interact in other ways (one need blocking another, one intervention covering several)?
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / NOT_ASSESSABLE / NOT_ASSESSABLE
- **Master Answer**: "NO. Usually we know these needs are true as the volunteer confirms them. That helps them bare minimum side."
- **R1 Evidence**: Need interaction beyond cascading not explicitly described.

### GT-OQ17
- **Question**: Is there a distinct layer of decision-making — above individual cases and above single programmes — where funders themselves coordinate or set terms?
- **Current Classification** (Matrix/Master/R1): CONTEXT_DEPENDENT / NOT_ASSESSABLE / CONTEXT_DEPENDENT
- **Master Answer**: **Final Status:**
NOT_ASSESSABLE
- **R1 Evidence**: Donors coordinate informally in a WhatsApp group, first come first serve adoption.

### GT-OQ18
- **Question**: Have you encountered a child who was orphaned but well-guardianed, or unguardianed but not orphaned? How did that distinction matter in practice?
- **Current Classification** (Matrix/Master/R1): NOT_ASSESSABLE / CONFIRMED / NOT_ASSESSABLE
- **Master Answer**: "Yes, depends on the situation and the ground reality that the volunteer confirms, that how much they need really."
- **R1 Evidence**: Not directly addressed.

### GT-OQ19
- **Question**: Is there a distinct role or function in your work that exists specifically to coordinate a case across multiple people/organizations, separate from the case manager's own casework?
- **Current Classification** (Matrix/Master/R1): CONTEXT_DEPENDENT / NOT_ASSESSABLE / CONTEXT_DEPENDENT
- **Master Answer**: **Final Status:**
NOT_ASSESSABLE
- **R1 Evidence**: 'just the khidmat grp volunteerss (the staff)'. No separate coordination role.

