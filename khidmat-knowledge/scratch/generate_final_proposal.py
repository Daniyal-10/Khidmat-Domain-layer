import json

def generate_proposal():
    out = []
    out.append("# Stage 5 Ground Truth Review Finalization Proposal\n")

    out.append("## 1. Actual Repository State")
    out.append("- **Current Branch**: `stage5-gtr-finalization`")
    out.append("- **Git Status**: Clean (no uncommitted changes before starting)")
    out.append("- **Current HEAD**: `dc53efebd64283609f02246d2ac55e81ba4ae5e2`")
    out.append("- **Files Inspected**: `DOMAIN Gathering/all_answers.md`, `DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md`, all 47 GTR records in `docs/05-ontology/GTR/`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `docs/05-ontology/04-ARCHITECTURE-RULES.md`.")
    out.append("- **Files missing/absent**: `10-ONTOLOGY-RECONCILIATION-CLOSURE-REPORT.md` is absent.\n")

    # Hardcode all 47 items strictly based on raw evidence and new instructions
    # Format: id, matrix, master, r1, evidence, tier, answers?, proposed, reason
    items = [
        ("GT-P1", "CONFIRMED", "CONFIRMED", "CONFIRMED", "We track food, medical, shelter, education needs. They persist and change over time.", "Tier A/B", "Yes", "CONFIRMED", "Practitioner explicitly tracks conditions that change over time."),
        ("GT-P2", "CONTEXT_DEPENDENT", "NOT_ASSESSABLE", "CONTEXT_DEPENDENT", "'working in bhopal and 100-200 km near this city currently'", "Tier A/B", "No", "NOT_ASSESSABLE", "Operates in one location/context; cannot assess cross-context variation."),
        ("GT-P3", "MISSING", "UNRESOLVED", "MISSING", "'unknown here is nothing... volunteer will reject the case'", "Tier A/B", "No", "NOT_ASSESSABLE", "Workflow resolves unknowns before entry; system representation of uncertainty was not assessed."),
        ("GT-P4", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'The Beneficiary ID (Unique ID) should be there...'", "Tier A/B", "Yes", "CONFIRMED", "Explicitly tracks re-identification across encounters."),
        ("GT-P5", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'We don't help the beggers', 'donors have limit to donate'", "Tier A/B", "Yes", "CONFIRMED", "Demonstrates universal rules applied to casework."),
        ("GT-P6", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'medical needs are of one time and long also... if one time then help via the donors and then closed'", "Tier A/B", "Yes", "CONFIRMED", "Distinguishes one-time dateable events from ongoing states."),
        ("GT-P7", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'dont have a earning member that directly make their prioirty high'", "Tier A/B", "Yes", "CONFIRMED", "Establishes dependency relations cascading into need priority."),
        
        ("GT-L1", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Age, gender, housing, income, requirements collected.", "Tier A/B", "Yes", "CONFIRMED", "Tracks specific facet dimensions on individuals."),
        ("GT-L2", "CONTEXT_DEPENDENT", "CONFIRMED", "CONTEXT_DEPENDENT", "'head of the family... noted in the beneficary'", "Tier A/B", "Yes", "CONTEXT_DEPENDENT", "Tracks Person/Family, but absence of Org/Prog supports that Entity types are context-dependent in practice."),
        ("GT-L3", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'relation: mother, wife, son, daughter'", "Tier A/B", "Yes", "CONFIRMED", "Explicitly tracks kinship relationships."),
        ("GT-L4", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'about the family privacy concern too much to hide...'", "Tier A/B", "No", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Raw text shows rule vs preference, not rule vs rule."),
        ("GT-L5", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Needs tracked: Food, Shelter, Medical. 'earning members maybe take more longer...'", "Tier A/B", "Yes", "CONFIRMED", "Tracks specific states and state changes over time."),
        ("GT-L6", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Survey -> visit -> upload -> adoption -> fulfillment (tracking card).", "Tier A/B", "Yes", "CONFIRMED", "Confirms event sequence and linearity in a case."),
        ("GT-L7", "MISSING", "UNRESOLVED", "MISSING", "'unknown here is nothing about the case'", "Tier A/B", "No", "NOT_ASSESSABLE", "Workflow resolves unknowns before entry; system epistemic stance was not assessed."),
        ("GT-L8", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'uploaded in a grp where the donors are there... first come first server'", "Tier A/B", "Yes", "CONFIRMED", "Confirms handoff and recurring loops in coordination."),

        ("GT-PL1", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Form groups Person details separate from Household context.", "Tier A/B", "Yes", "CONFIRMED", "Conceptually separates person from environment."),
        ("GT-PL2", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "'NO we dont cover the seasonal things...'", "Tier A/B", "No", "NOT_ASSESSABLE", "Seasonal/location changes not encountered; cannot assess."),
        ("GT-PL3", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'multiple needs the volutneer decides that based on the ground review'", "Tier A/B", "Yes", "CONFIRMED", "Vulnerability composition is a judgment call, not a formula."),
        ("GT-PL4", "MISSING", "NOT_ASSESSABLE", "MISSING", "'never happned [conflict]'", "Tier A/B", "No", "NOT_ASSESSABLE", "Conflicts resolved before entry; contradiction representation not assessed."),
        ("GT-PL5", "CONTEXT_DEPENDENT", "NOT_ASSESSABLE", "CONTEXT_DEPENDENT", "'NO organisations and programs are involved'", "Tier A/B", "Yes", "CONTEXT_DEPENDENT", "Distinction between Org/Prog is absent in this context."),
        ("GT-PL6", "NOT_ASSESSABLE", "UNRESOLVED", "NOT_ASSESSABLE", "Tracking card used jointly by donor and beneficiary.", "Tier A/B", "No", "NOT_ASSESSABLE", "Outcome tracking not separated from fulfillment; proposition not assessed."),
        ("GT-PL7", "CONFIRMED", "UNRESOLVED", "CONFIRMED", "Need (medical) and modality (grocery, rent) bundled in description.", "Tier A/B", "Yes", "CONFIRMED", "Practitioner bundles need, delivery, and why together."),

        ("GT-AR1", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "No programmes exist in this operation.", "Tier A/B", "No", "NOT_ASSESSABLE", "Cannot assess altitude split without a programme layer."),
        ("GT-AR2", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'if recusisng like medicens they can conitnue'", "Tier A/B", "Yes", "CONFIRMED", "Confirms non-linearity (recurrent/reopening states)."),
        ("GT-AR3", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "Not addressed in evidence.", "Tier A/B", "No", "NOT_ASSESSABLE", "Dual-clock rule not assessed."),
        ("GT-AR4", "CONFIRMED", "NOT_ASSESSABLE", "CONFIRMED", "'its done on the ground verification... the volutneer decides'", "Tier A/B", "No", "NOT_ASSESSABLE", "Shows human judgment, but does not establish a universal 'always requires human sign-off' rule against automation."),
        ("GT-AR5", "CONFIRMED", "CONFIRMED", "CONFIRMED", "No raw evidence addressing dignity as score vs rule.", "Tier A/B", "No", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Not assessed."),
        ("GT-AR6", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'Beneficiary ID... as there can be similar name or identity mismatch'", "Tier A/B", "Yes", "CONFIRMED", "Identity uncertainty is manually managed via IDs and family details."),

        ("GT-OQ1", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Uses Beneficiary ID, contact no, family details.", "Tier A/B", "Yes", "CONFIRMED", "Determines identity manually without biometrics."),
        ("GT-OQ2", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Volunteer decides vulnerability based on ground review.", "Tier A/B", "Yes", "CONFIRMED", "Matches PL3; composite risk is human judgment."),
        ("GT-OQ3", "NOT_ASSESSABLE", "CONFIRMED", "NOT_ASSESSABLE", "'Family members details... House: Own/Rental'", "Tier A/B", "No", "NOT_ASSESSABLE", "Does not discuss complex family/household boundary cases."),
        ("GT-OQ4", "CONFIRMED", "UNRESOLVED", "CONFIRMED", "Mentions specific examples: widow, study, accident.", "Tier A/B", "No", "NOT_ASSESSABLE", "Provides observed examples but does not establish or validate the ontology's proposed semantic value-set structure."),
        ("GT-OQ5", "NOT_ASSESSABLE", "UNRESOLVED", "NOT_ASSESSABLE", "Tracking card used by donor and beneficiary.", "Tier A/B", "No", "NOT_ASSESSABLE", "Same as PL6; outcome ownership distinct from case journey is not assessed."),
        ("GT-OQ6", "CONTEXT_DEPENDENT", "NOT_ASSESSABLE", "CONTEXT_DEPENDENT", "'NO organisations and programs are involved'", "Tier A/B", "Yes", "CONTEXT_DEPENDENT", "Same as PL5; demonstrates structural absence in context."),
        ("GT-OQ7", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Donors adopt from group, track via card, have limits.", "Tier A/B", "Yes", "CONFIRMED", "Validates donor coordination mechanisms."),
        ("GT-OQ8", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'donors have limit to donate...'", "Tier A/B", "Yes", "CONFIRMED", "Validates existence of funding restrictions."),
        ("GT-OQ9", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'dont have a earning member that directly make their prioirty high'", "Tier A/B", "No", "NOT_ASSESSABLE", "Describes urgency/priority, but does not establish the distinct semantic concept of 'Risk' classification."),
        ("GT-OQ10", "CONFIRMED", "NOT_ASSESSABLE", "CONFIRMED", "'medicals proofs... of government hospital are considered true only'", "Tier A/B", "Yes", "CONFIRMED", "Validates epistemic hierarchy and evidence weighting."),
        ("GT-OQ11", "CONFIRMED", "CONFIRMED", "CONFIRMED", "'Below the poverty line... Extremely needy mostly'", "Tier A/B", "Yes", "CONFIRMED", "Establishes baseline wellbeing standard used."),
        ("GT-OQ12", "MISSING", "UNRESOLVED", "MISSING", "'unknown here is nothing about the case'", "Tier A/B", "No", "NOT_ASSESSABLE", "Workflow avoids missing info; system representation is not assessed."),
        ("GT-OQ13", "MISSING", "NOT_ASSESSABLE", "MISSING", "'never happned [conflict]'", "Tier A/B", "No", "NOT_ASSESSABLE", "Conflicts avoided; system representation not assessed."),
        ("GT-OQ14", "NOT_ASSESSABLE", "UNRESOLVED", "NOT_ASSESSABLE", "Mentions initial privacy concern, no withdrawal.", "Tier A/B", "No", "NOT_ASSESSABLE", "Consent parameters/withdrawal not assessed."),
        ("GT-OQ15", "CONFIRMED", "CONFIRMED", "CONFIRMED", "Vendors provide ration, hospitals provide proofs.", "Tier A/B", "Yes", "CONFIRMED", "Service providers exist as distinct entities/actors."),
        ("GT-OQ16", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "NOT_ASSESSABLE", "'multiple needs the volutneer decides...'", "Tier A/B", "No", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Need interactions not assessed."),
        ("GT-OQ17", "CONTEXT_DEPENDENT", "NOT_ASSESSABLE", "CONTEXT_DEPENDENT", "'uploaded in a grp where the donors are there'", "Tier A/B", "Yes", "CONTEXT_DEPENDENT", "Context demonstrates coordination without a distinct funder altitude."),
        ("GT-OQ18", "NOT_ASSESSABLE", "CONFIRMED", "NOT_ASSESSABLE", "'dont have a earning member...'", "Tier A/B", "No", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Orphan vs unguardianed not assessed."),
        ("GT-OQ19", "CONTEXT_DEPENDENT", "NOT_ASSESSABLE", "CONTEXT_DEPENDENT", "'just the khidmat grp volunteerss'", "Tier A/B", "Yes", "CONTEXT_DEPENDENT", "Context operates without a distinct orchestration role.")
    ]

    out.append("## 2. Four STOP-Item Analyses (Fabricated Master Answers)")
    out.append("1. **GT-L4**: Master fabricated a scenario about refusing to process families keeping information. **Raw text**: 'about the family privacy concern... needs to tell about 3 4 more people'. **Reassessment**: Shows rule vs preference, not a structural conflict of two rules. **Status**: `NOT_ASSESSABLE`.")
    out.append("2. **GT-AR5**: Master fabricated 'They shouldn't be disrespected'. **Raw text**: No mention of dignity/safeguarding as score or rule. **Status**: `NOT_ASSESSABLE`.")
    out.append("3. **GT-OQ16**: Master fabricated 'NO. Usually we know these needs are true... bare minimum side'. **Raw text**: 'multiple needs the volutneer decides'. **Reassessment**: Does not establish interactions (blocking/covering) between needs. **Status**: `NOT_ASSESSABLE`.")
    out.append("4. **GT-OQ18**: Master fabricated 'depends on the situation and the ground reality...'. **Raw text**: 'dont have a earning member'. **Reassessment**: Does not discuss orphaned vs unguardianed distinction. **Status**: `NOT_ASSESSABLE`.\n")

    out.append("## 3. 47-Row Evidence Trace & Proposed Final Classifications\n")
    out.append("*(Note: `Evidence` refers strictly to raw practitioner text or explicit paraphrase from `all_answers.md`.)*\n")
    out.append("| GTR | Current Matrix | Current Master | Current R1 | Evidence | Evidence Tier | Evidence Answers Question? | Proposed Final Status | Reason |")
    out.append("|---|---|---|---|---|---|---|---|---|")

    for item in items:
        gtr, matrix, master, r1, evidence, tier, answers, proposed, reason = item
        out.append(f"| {gtr} | {matrix} | {master} | {r1} | {evidence} | {tier} | {answers} | **{proposed}** | {reason} |")

    # Calculate status distribution
    dist = {}
    for item in items:
        dist[item[7]] = dist.get(item[7], 0) + 1

    out.append("\n## 4. Final Status Distribution")
    for k, v in sorted(dist.items()):
        out.append(f"- **{k}**: {v}")

    out.append("\n## 5. Explanations for Final Epistemic Audits")
    out.append("During the final audit, several classifications were rigorously corrected to distinguish between observed workflows and actual validation of semantic propositions:")
    out.append("- **Cognition/Unknowns (GT-P3, L7, PL4, OQ12, OQ13)**: The practitioner workflow explicitly rejects unverified cases before entry. Because the situation is avoided, the ontology's capability for uncertainty representation was not actually tested. Reclassified from `CONTEXT_DEPENDENT`/`MISSING` to `NOT_ASSESSABLE`.")
    out.append("- **Human Sign-off (GT-AR4)**: The evidence shows the volunteer decides, but without automated systems present, this does not universally prove an 'always' rule against automation. Reclassified to `NOT_ASSESSABLE`.")
    out.append("- **Risk vs Priority (GT-OQ9)**: The practitioner mentioned high priority, but the raw evidence does not establish the distinct semantic concept of 'Risk'. Reclassified to `NOT_ASSESSABLE`.")
    out.append("- **Value-Sets (GT-OQ4)**: The practitioner provided examples of casework (widow, accident) but did not validate the structural completeness of the ontology's facet axes. Reclassified to `NOT_ASSESSABLE`.")
    out.append("- **Context Dependencies (GT-L2, PL5, OQ6, OQ17, OQ19)**: The evidence positively establishes that in this specific operational context, certain layers (org/prog, orchestration, funder altitude) are absent. This supports `CONTEXT_DEPENDENT` (i.e. the existence of these entities is context-dependent in practice), but strictly scopes this validation to the Khidmat context rather than claiming universal structural absence.\n")

    out.append("## 6. Distinguishing Epistemic Findings")
    out.append("- **Observed practice**: Workflows (e.g., rejecting unverified cases).")
    out.append("- **Contextual finding** (`CONTEXT_DEPENDENT`): When a concept's presence genuinely varies based on the practitioner's local operation (e.g., absent organisation layer).")
    out.append("- **Ontology validation** (`CONFIRMED`): When the raw evidence actively and strictly supports the structural proposition.")
    out.append("- **Not assessable** (`NOT_ASSESSABLE`): When the session simply did not encounter or discuss the proposition, or when observed practice does not equate to structural validation.")
    out.append("- **Unresolved** (`UNRESOLVED`): When meaningful but insufficient or conflicting evidence exists.\n")

    out.append("## 7. Master Register Status & Proposed Phase 2 File Changes")
    out.append("The current `MASTER-GTR-INTERVIEW-FLOW.md` is NOT an authoritative raw-evidence register. In Phase 2, it will be wiped of all synthetic quotes and replaced strictly with verbatim quotes from the raw evidence.")
    out.append("Upon Phase 2 approval, I propose to edit:")
    out.append("1. **GTR R1 records (`docs/05-ontology/GTR/*-R1.md`)**: Apply raw quotes and final statuses.")
    out.append("2. **`05-GROUND-TRUTH-REVIEW-MATRIX.md`**: Update Matrix statuses.")
    out.append("3. **`MASTER-GTR-INTERVIEW-FLOW.md`**: Repair Master state by erasing fabricated answers and inserting verbatim quotes.")
    out.append("4. **Framework/Plan/Template**: Flag historical notices.")
    out.append("5. **`README.md`**: Append explicit scope statement. Remove readiness claims.")
    out.append("6. **`ONTOLOGY-DESIGN-COMPLETION-UPDATE.html`**: Append superseding banner.\n")

    out.append("## 8. Stage 6/7 Correction Candidates")
    out.append("| File | Section | Current Wording | Reason for Future Correction |")
    out.append("|---|---|---|---|")
    out.append("| `04-ARCHITECTURE-RULES.md` | Various | 'practitioner-corroborated', 'validated' | GTR provides only single-practitioner, single-context evidence. |")
    out.append("| `03-ONTOLOGY-PILLARS.md` | Various | Claims of 'Strong' validation | Evidence is Tier B/C local practice; insufficient for universal 'Strong' rating. |")
    out.append("| `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | §3.1 note (2026-09-07) | Post-freeze amendment | Documented here, must not be edited in Stage 5. |")
    out.append("| Stage 7 Rulings (G1-G5) | N/A | (Assumption of Stage 5 GREEN) | Rely on unverified evidence; requires re-basing. |\n")

    out.append("## 9. New-GTR Decision")
    out.append("No new GTR IDs are proposed. The existing 47 questions remain the bounded set.")

    out.append("\n## 10. Explicit Stage 5 Outcome")
    out.append("**PROPOSED OUTCOME AFTER SUCCESSFUL PHASE 2: STAGE 5 CLOSED WITH QUALIFICATIONS**")
    out.append("Rationale: Once provenance failures are fully repaired and classifications correctly scoped, the 47-GTR package will be internally consistent, traceable, and epistemically defensible, though significantly narrower in validation scope than previously claimed.")

    with open('docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    
    print("Final rigorous proposal written.")

generate_proposal()
