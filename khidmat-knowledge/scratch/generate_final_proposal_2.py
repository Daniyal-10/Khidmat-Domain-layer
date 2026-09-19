import json

# Ensure items matches all 47 rows.
items = [
    # GT-P
    ("GT-P1", "CONFIRMED", "Practitioner explicitly tracks conditions that change over time.", "'widow cases', 'medical needs are of one time and long also'"),
    ("GT-P2", "NOT_ASSESSABLE", "Operates in one location/context; cannot assess cross-context variation.", "'working in bhopal and 100-200 km near this city'"),
    ("GT-P3", "NOT_ASSESSABLE", "Workflow resolves unknowns before entry; system representation of uncertainty was not assessed.", "'unknown here is nothing... volunteer will reject the case'"),
    ("GT-P4", "CONFIRMED", "Explicitly tracks re-identification across encounters.", "'The Beneficiary ID (Unique ID) should be there... identity mismatch'"),
    ("GT-P5", "CONFIRMED", "Demonstrates universal rules applied to casework.", "'We don't help the beggers', 'donors have limit'"),
    ("GT-P6", "CONFIRMED", "Distinguishes one-time dateable events from ongoing states.", "'medical needs are of one time and long also...'"),
    ("GT-P7", "CONFIRMED", "Establishes dependency relations cascading into priority.", "'dont have a earning member that directly make their prioirty high'"),
    
    # GT-L
    ("GT-L1", "CONFIRMED", "Tracks specific facet dimensions on individuals.", "Age, gender, housing, income, requirements collected."),
    ("GT-L2", "NOT_ASSESSABLE", "Local absence of Org/Prog layer does not establish context-dependence.", "'NO organisations and programs are involved'"),
    ("GT-L3", "CONFIRMED", "Explicitly tracks kinship relationships.", "'relation: mother, wife, son, daughter'"),
    ("GT-L4", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Raw text shows rule vs preference, not rule vs rule.", "'about the family privacy concern too much to hide...'"),
    ("GT-L5", "CONFIRMED", "Tracks specific states and state changes over time.", "Needs tracked: Food, Shelter. 'earning members maybe take more longer...'"),
    ("GT-L6", "CONFIRMED", "Confirms event sequence and linearity in a case.", "Survey -> visit -> upload -> adoption -> fulfillment (tracking card)."),
    ("GT-L7", "NOT_ASSESSABLE", "Workflow resolves unknowns before entry; system epistemic stance was not assessed.", "'unknown here is nothing about the case'"),
    ("GT-L8", "CONFIRMED", "Confirms handoff and recurring loops in coordination.", "'uploaded in a grp where the donors are there... first come first server'"),

    # GT-PL
    ("GT-PL1", "CONFIRMED", "Conceptually separates person from environment in form layout.", "Form groups Person details separate from Household context."),
    ("GT-PL2", "NOT_ASSESSABLE", "Seasonal/location changes not encountered; cannot assess.", "'NO we dont cover the seasonal things...'"),
    ("GT-PL3", "CONFIRMED", "Vulnerability composition is a judgment call, not a formula.", "'multiple needs the volutneer decides that based on the ground review'"),
    ("GT-PL4", "NOT_ASSESSABLE", "Conflicts resolved before entry; contradiction representation not assessed.", "'never happned [conflict]'"),
    ("GT-PL5", "NOT_ASSESSABLE", "Local absence of Org/Prog layer does not establish context-dependence.", "'NO organisations and programs are involved'"),
    ("GT-PL6", "NOT_ASSESSABLE", "Outcome tracking not separated from fulfillment; proposition not assessed.", "Tracking card used jointly by donor and beneficiary."),
    ("GT-PL7", "CONFIRMED", "Practitioner bundles need, delivery, and why together.", "Need (medical) and modality (grocery, rent) bundled in description."),

    # GT-AR
    ("GT-AR1", "NOT_ASSESSABLE", "Cannot assess altitude split without a programme layer.", "No programmes exist in this operation."),
    ("GT-AR2", "CONFIRMED", "Confirms non-linearity (recurrent/reopening states).", "'if recusisng like medicens they can conitnue'"),
    ("GT-AR3", "NOT_ASSESSABLE", "Dual-clock rule not assessed.", "Not addressed in evidence."),
    ("GT-AR4", "NOT_ASSESSABLE", "Shows human judgment, but does not establish a universal 'always requires human sign-off' rule against automation.", "'its done on the ground verification... the volutneer decides'"),
    ("GT-AR5", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Not assessed.", "No raw evidence addressing dignity as score vs rule."),
    ("GT-AR6", "NOT_ASSESSABLE", "Identity tracking is manual; does not validate rule handling algorithmic uncertainty.", "'Beneficiary ID... as there can be similar name or identity mismatch'"),

    # GT-OQ
    ("GT-OQ1", "CONFIRMED", "Determines identity manually without biometrics.", "Uses Beneficiary ID, contact no, family details."),
    ("GT-OQ2", "CONFIRMED", "Matches PL3; composite risk is human judgment.", "Volunteer decides vulnerability based on ground review."),
    ("GT-OQ3", "NOT_ASSESSABLE", "Does not discuss complex family/household boundary cases.", "'Family members details... House: Own/Rental'"),
    ("GT-OQ4", "NOT_ASSESSABLE", "Provides observed examples but does not establish or validate the ontology's proposed semantic value-set structure.", "Mentions specific examples: widow, study, accident."),
    ("GT-OQ5", "NOT_ASSESSABLE", "Outcome ownership distinct from case journey is not assessed.", "Tracking card used by donor and beneficiary."),
    ("GT-OQ6", "NOT_ASSESSABLE", "Local absence of Org/Prog layer does not establish context-dependence.", "'NO organisations and programs are involved'"),
    ("GT-OQ7", "CONFIRMED", "Validates donor coordination mechanisms.", "Donors adopt from group, track via card, have limits."),
    ("GT-OQ8", "CONFIRMED", "Validates existence of funding restrictions.", "'donors have limit to donate...'"),
    ("GT-OQ9", "NOT_ASSESSABLE", "Describes urgency/priority, but does not establish the distinct semantic concept of 'Risk'.", "'dont have a earning member that directly make their prioirty high'"),
    ("GT-OQ10", "CONFIRMED", "Validates epistemic hierarchy and evidence weighting.", "'medicals proofs... of government hospital are considered true only'"),
    ("GT-OQ11", "CONFIRMED", "Establishes baseline wellbeing standard used.", "'Below the poverty line... Extremely needy mostly'"),
    ("GT-OQ12", "NOT_ASSESSABLE", "Workflow avoids missing info; system representation is not assessed.", "'unknown here is nothing about the case'"),
    ("GT-OQ13", "NOT_ASSESSABLE", "Conflicts are avoided; system representation not assessed.", "'never happned [conflict]'"),
    ("GT-OQ14", "NOT_ASSESSABLE", "Consent parameters/withdrawal not assessed.", "Mentions initial privacy concern, no withdrawal."),
    ("GT-OQ15", "NOT_ASSESSABLE", "Establishes them as services/places, but not explicitly as Actors with their own interests.", "Vendors provide ration, hospitals provide proofs."),
    ("GT-OQ16", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Need interactions not assessed.", "'multiple needs the volutneer decides...'"),
    ("GT-OQ17", "NOT_ASSESSABLE", "Local absence of funder altitude does not establish context-dependence.", "'uploaded in a grp where the donors are there'"),
    ("GT-OQ18", "NOT_ASSESSABLE", "STOP item: Fabricated master wording discarded. Orphan vs unguardianed not assessed.", "'dont have a earning member...'"),
    ("GT-OQ19", "NOT_ASSESSABLE", "Local absence of orchestration role does not establish context-dependence.", "'just the khidmat grp volunteerss'")
]

out = []
out.append("# Stage 5 Ground Truth Review Finalization Proposal\n")

out.append("## 1. Actual Repository State")
out.append("- **Current Branch**: `stage5-gtr-finalization`")
out.append("- **Git Status**: Clean (no uncommitted changes before starting)")
out.append("- **Current HEAD**: `dc53efebd64283609f02246d2ac55e81ba4ae5e2`")
out.append("- **Files Inspected**: `DOMAIN Gathering/all_answers.md`, `DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md`, all 47 GTR records in `docs/05-ontology/GTR/`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `docs/05-ontology/04-ARCHITECTURE-RULES.md`.")
out.append("- **Files missing/absent**: `10-ONTOLOGY-RECONCILIATION-CLOSURE-REPORT.md` is absent.\n")

out.append("## 2. Four STOP-Item Analyses (Fabricated Master Answers)")
out.append("1. **GT-L4**: Master fabricated a scenario about refusing to process families keeping information. **Raw text**: 'about the family privacy concern... needs to tell about 3 4 more people'. **Reassessment**: Shows rule vs preference, not a structural conflict of two rules. **Status**: `NOT_ASSESSABLE`.")
out.append("2. **GT-AR5**: Master fabricated 'They shouldn't be disrespected'. **Raw text**: No mention of dignity/safeguarding as score or rule. **Status**: `NOT_ASSESSABLE`.")
out.append("3. **GT-OQ16**: Master fabricated 'NO. Usually we know these needs are true... bare minimum side'. **Raw text**: 'multiple needs the volutneer decides'. **Reassessment**: Does not establish interactions (blocking/covering) between needs. **Status**: `NOT_ASSESSABLE`.")
out.append("4. **GT-OQ18**: Master fabricated 'depends on the situation and the ground reality...'. **Raw text**: 'dont have a earning member'. **Reassessment**: Does not discuss orphaned vs unguardianed distinction. **Status**: `NOT_ASSESSABLE`.\n")

out.append("## 3. 47-Row Evidence Trace & Proposed Final Classifications\n")
out.append("*(Note: `Evidence` refers strictly to verbatim raw practitioner text or explicit paraphrase from `all_answers.md`.)*\n")
out.append("| GTR | Proposed Final Status | Evidence | Reason |")
out.append("|---|---|---|---|")

for gtr, proposed, reason, evidence in items:
    evidence = evidence.replace('|', '/')
    reason = reason.replace('|', '/')
    out.append(f"| {gtr} | **{proposed}** | {evidence} | {reason} |")

# Calculate status distribution
dist = {}
for _, proposed, _, _ in items:
    dist[proposed] = dist.get(proposed, 0) + 1

out.append("\n## 4. Final Status Distribution")
for k, v in sorted(dist.items()):
    out.append(f"- **{k}**: {v}")

total = sum(dist.values())
out.append(f"\n**Total Items**: {total}")

out.append("\n## 5. Explanations for Final Epistemic Audits")
out.append("During the final audit, several classifications were rigorously corrected to distinguish between observed workflows, local absence, and actual validation of semantic propositions:")
out.append("- **Local Absence vs Context-Dependence (GT-L2, PL5, OQ6, OQ17, OQ19)**: Previously marked `CONTEXT_DEPENDENT` based on the absence of Org/Prog/Funder/Orchestration layers. Corrected to `NOT_ASSESSABLE`. The practitioner explicitly stating these concepts are absent locally does not positively establish that the ontology proposition varies with operational context.")
out.append("- **Cognition/Unknowns (GT-P3, L7, PL4, OQ12, OQ13)**: The practitioner workflow explicitly rejects unverified cases before entry. Because the situation is avoided, the ontology's capability for uncertainty representation was not actually tested. Reclassified to `NOT_ASSESSABLE`.")
out.append("- **Human Sign-off (GT-AR4)**: The evidence shows the volunteer decides, but without automated systems present, this does not universally prove an 'always' rule against automation. Reclassified to `NOT_ASSESSABLE`.")
out.append("- **Risk vs Priority (GT-OQ9)**: The practitioner mentioned high priority, but the raw evidence does not establish the distinct semantic concept of 'Risk'. Reclassified to `NOT_ASSESSABLE`.")
out.append("- **Value-Sets (GT-OQ4)**: The practitioner provided examples of casework (widow, accident) but did not validate the structural completeness of the ontology's facet axes. Reclassified to `NOT_ASSESSABLE`.")
out.append("- **Algorithmic Humility (GT-AR6)**: Manual identity tracking with Beneficiary IDs does not test an architecture rule about algorithmic uncertainty handling. Reclassified to `NOT_ASSESSABLE`.")
out.append("- **Service Provider Actors (GT-OQ15)**: Engaging vendors as places/services does not actively validate them as independent 'Actors' with distinct interests. Reclassified to `NOT_ASSESSABLE`.\n")

out.append("## 6. Distinguishing Epistemic Findings")
out.append("- **Observed practice**: Workflows (e.g., rejecting unverified cases). Does not automatically confirm a proposition.")
out.append("- **Contextual finding** (`CONTEXT_DEPENDENT`): Requires positive evidence that a proposition varies with operational context, not just local absence.")
out.append("- **Ontology validation** (`CONFIRMED`): When the raw evidence actively and strictly supports the structural proposition.")
out.append("- **Not assessable** (`NOT_ASSESSABLE`): When the session simply did not encounter, test, or establish the proposition.")
out.append("- **Unresolved** (`UNRESOLVED`): When meaningful but conflicting or insufficient evidence exists.\n")

out.append("## 7. Master Register Status & Proposed Phase 2 File Changes")
out.append("The current `MASTER-GTR-INTERVIEW-FLOW.md` is NOT an authoritative raw-evidence register. In Phase 2, it will NOT be destructively erased. Instead, it will be carefully repaired:")
out.append("- Identify unsupported/synthetic material.")
out.append("- Remove or clearly mark unsupported claims.")
out.append("- Preserve genuine practitioner evidence.")
out.append("- Preserve question IDs/order/context and provenance.")
out.append("- Make clear which material came from raw practitioner evidence.")
out.append("- Do not silently replace historical content without traceability.")
out.append("\nOther Phase 2 tasks:")
out.append("- **GTR R1 records**: Apply raw quotes and final statuses.")
out.append("- **Matrix**: Update Matrix statuses.")
out.append("- **Framework/Plan**: Flag historical notices.")
out.append("- **`README.md` & `ONTOLOGY-DESIGN-COMPLETION-UPDATE.html`**: Append superseding scope statements.\n")

out.append("## 8. Stage 6/7 Correction Candidates")
out.append("| File | Section | Current Wording | Reason for Future Correction |")
out.append("|---|---|---|---|")
out.append("| `04-ARCHITECTURE-RULES.md` | Various | 'practitioner-corroborated', 'validated' | GTR provides only single-practitioner, single-context evidence. |")
out.append("| `03-ONTOLOGY-PILLARS.md` | Various | Claims of 'Strong' validation | Evidence is Tier B/C local practice; insufficient for universal 'Strong' rating. |")
out.append("| `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | §3.1 note (2026-09-07) | Post-freeze amendment | Documented here, must not be edited in Stage 5. |")
out.append("| Stage 7 Rulings (G1-G5) | N/A | (Assumption of Stage 5 GREEN) | Rely on unverified evidence; requires re-basing. |\n")

out.append("## 9. New-GTR Decision")
out.append("No new GTR IDs are proposed or required. The existing 47 questions remain the bounded set.")

out.append("\n## 10. Explicit Stage 5 Outcome")
out.append("**PROPOSED OUTCOME AFTER SUCCESSFUL PHASE 2: STAGE 5 CLOSED WITH QUALIFICATIONS**")
out.append("Rationale: Once provenance failures are fully repaired and classifications correctly scoped, the 47-GTR package will be internally consistent, traceable, and epistemically defensible, though significantly narrower in validation scope than previously claimed.")
out.append("\n**PHASE 2 NOT YET AUTHORIZED.**")

with open('docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Final rigorous proposal written.")
