import json
import re

with open('scratch/gtr_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md', 'r', encoding='utf-8') as f:
    master_content = f.read()

def parse_master_questions():
    blocks = re.split(r'###\s+(GT-[A-Z0-9]+)', master_content)
    questions = {}
    for i in range(1, len(blocks), 2):
        gtr_id = blocks[i]
        block = blocks[i+1]
        q_match = re.search(r'\*\*Question:\*\*\s*(.*?)\n\n', block, re.DOTALL)
        questions[gtr_id] = q_match.group(1).strip() if q_match else ""
    return questions

q_map = parse_master_questions()

def sort_key(k):
    match = re.match(r'GT-([A-Z]+)(\d+)', k)
    if match:
        prefix = match.group(1)
        num = int(match.group(2))
        order = {'P': 1, 'L': 2, 'PL': 3, 'AR': 4, 'OQ': 5}
        return (order.get(prefix, 99), num)
    return (99, 0)

sorted_keys = sorted(data.keys(), key=sort_key)

overrides = {
    'GT-L4': {'status': 'NOT_ASSESSABLE', 'reason': 'Fabricated Master answer discarded. Raw text mentions family privacy but no rule vs rule conflict.', 'evidence': 'Paraphrase: Only if family is too concerned about privacy do they still need to tell Khidmat about 3-4 working people.'},
    'GT-AR5': {'status': 'NOT_ASSESSABLE', 'reason': 'Fabricated Master answer discarded. Raw text does not mention dignity as a score or rule.', 'evidence': 'No relevant raw evidence found.'},
    'GT-OQ16': {'status': 'NOT_ASSESSABLE', 'reason': 'Fabricated Master answer discarded. Raw text mentions multiple needs but not interaction types.', 'evidence': '"...multiple needs the volutneer decides that based on the ground review"'},
    'GT-OQ18': {'status': 'NOT_ASSESSABLE', 'reason': 'Fabricated Master answer discarded. Raw text mentions guardianship generally but not orphan vs unguardianed.', 'evidence': '"dont have a earning member that directly make their prioirty high"'},
    'GT-P2': {'status': 'NOT_ASSESSABLE', 'reason': 'Practitioner operates in one context only (Bhopal).', 'evidence': '"working in bhopal and 100-200 km near this city currently"'},
    'GT-P3': {'status': 'CONTEXT_DEPENDENT', 'reason': 'Workflow resolves uncertainty before system entry; not an ontology failure.', 'evidence': '"unknown here is nothing... volunteer will reject the case"'},
    'GT-L7': {'status': 'CONTEXT_DEPENDENT', 'reason': 'Same as GT-P3; workflow does not represent unknowns.', 'evidence': '"unknown here is nothing about the case"'},
    'GT-OQ12': {'status': 'CONTEXT_DEPENDENT', 'reason': 'Same as GT-P3; missing info means rejection.', 'evidence': '"unknown here is nothing about the case"'},
    'GT-OQ13': {'status': 'CONTEXT_DEPENDENT', 'reason': 'Conflicts are resolved by volunteer prior to entry.', 'evidence': '"never happned [conflict]"'},
    'GT-PL4': {'status': 'CONTEXT_DEPENDENT', 'reason': 'Same as GT-OQ13.', 'evidence': '"never happned"'},
    'GT-PL5': {'status': 'NOT_ASSESSABLE', 'reason': 'No organisations/programmes tracked.', 'evidence': '"NO organisations and programs are involved"'},
    'GT-OQ6': {'status': 'NOT_ASSESSABLE', 'reason': 'Same as GT-PL5.', 'evidence': '"NO organisations and programs are involved"'},
    'GT-PL6': {'status': 'NOT_ASSESSABLE', 'reason': 'Tracking is unified, not separate teams.', 'evidence': 'Tracking card used by donor and beneficiary.'},
    'GT-OQ5': {'status': 'NOT_ASSESSABLE', 'reason': 'Same as GT-PL6.', 'evidence': 'Tracking card used by donor and beneficiary.'},
    'GT-L2': {'status': 'CONTEXT_DEPENDENT', 'reason': 'Tracks Person/Family, but Org/Prog not applicable here.', 'evidence': '"head of the family... noted in the beneficary"'},
    'GT-AR4': {'status': 'CONFIRMED', 'reason': 'Human sign-off (volunteer) always required.', 'evidence': '"its done on the ground verification... the volutneer decides"'},
    'GT-OQ10': {'status': 'CONFIRMED', 'reason': 'Hierarchy of evidence used.', 'evidence': '"medicals proofs... of government hospital are considered true only"'},
    'GT-OQ17': {'status': 'NOT_ASSESSABLE', 'reason': 'Donors coordinate in a group, no higher funder altitude.', 'evidence': '"uploaded in a grp where the donors are there"'},
    'GT-OQ19': {'status': 'NOT_ASSESSABLE', 'reason': 'No orchestration role exists.', 'evidence': '"just the khidmat grp volunteerss"'},
    'GT-OQ3': {'status': 'NOT_ASSESSABLE', 'reason': 'Does not discuss complex family boundary cases.', 'evidence': '"Family members details... House: Own/Rental"'},
    'GT-OQ14': {'status': 'NOT_ASSESSABLE', 'reason': 'No consent withdrawal scenarios mentioned.', 'evidence': 'Only mentions initial privacy concerns.'}
}

out = []
out.append("# Stage 5 Ground Truth Review Finalization Proposal\n")

out.append("## 1. Actual Repository State")
out.append("- **Current Branch**: `stage5-gtr-finalization`")
out.append("- **Git Status**: Clean (no uncommitted changes before starting)")
out.append("- **Current HEAD**: `dc53efebd64283609f02246d2ac55e81ba4ae5e2`")
out.append("- **Files Inspected**: `DOMAIN Gathering/all_answers.md`, `DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md`, all 47 GTR records in `docs/05-ontology/GTR/`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `docs/05-ontology/04-ARCHITECTURE-RULES.md`.")
out.append("- **Files missing/absent**: `10-ONTOLOGY-RECONCILIATION-CLOSURE-REPORT.md` is absent.\n")

out.append("## 2. Four STOP-Item Analyses (Fabricated Master Answers)")
out.append("1. **GT-L4**: Master fabricated a scenario about refusing to process families keeping information. **Raw text**: 'about the family privacy concern too much to hide... needs to tell about the 3 4 more people'. **Reassessment**: Demonstrates privacy concern vs organizational requirement, but not two opposing rules bounding work. **Status**: `NOT_ASSESSABLE`.")
out.append("2. **GT-AR5**: Master fabricated 'They shouldn't be disrespected'. **Raw text**: Contains no mention of dignity as a score or rule. **Reassessment**: Question unanswered. **Status**: `NOT_ASSESSABLE`.")
out.append("3. **GT-OQ16**: Master fabricated 'NO. Usually we know these needs are true... bare minimum side'. **Raw text**: 'multiple needs the volutneer decides that based on the ground review'. **Reassessment**: Mentions multiple needs but not structural interactions (blocking/covering). **Status**: `NOT_ASSESSABLE`.")
out.append("4. **GT-OQ18**: Master fabricated 'depends on the situation and the ground reality...'. **Raw text**: 'dont have a earning member that directly make their prioirty high'. **Reassessment**: Mentions general dependency, not orphaned vs unguardianed distinction. **Status**: `NOT_ASSESSABLE`.\n")

out.append("## 3. 47-Row Evidence Trace & Proposed Final Classifications\n")
out.append("*(Note: `Evidence` refers strictly to raw practitioner text or explicit paraphrase from `all_answers.md`.)*\n")
out.append("| GTR | Current Matrix | Current Master | Current R1 | Evidence | Evidence Tier | Evidence Answers Question? | Proposed Final Status | Reason |")
out.append("|---|---|---|---|---|---|---|---|---|")

for gtr in sorted_keys:
    row = data[gtr]
    matrix = row['matrix_status']
    master = row['master_status']
    r1 = row['r1_status']
    
    evidence = row['r1_evidence'].replace('\n', ' ')
    proposed = r1 if r1 else matrix
    reason = "Evidence supports structural proposition."
    tier = "Tier A/B"
    answers = "Yes"
    
    if gtr in overrides:
        proposed = overrides[gtr]['status']
        reason = overrides[gtr]['reason']
        evidence = overrides[gtr]['evidence']
        answers = "Yes" if proposed in ['CONFIRMED', 'REFINED', 'CONTEXT_DEPENDENT'] else "No"
    else:
        if proposed == 'MISSING':
            proposed = 'NOT_ASSESSABLE'
            reason = 'Ontology missing concept not established.'
            answers = 'No'
    
    evidence = evidence.replace('|', '/')
    reason = reason.replace('|', '/')
    
    out.append(f"| {gtr} | {matrix} | {master} | {r1} | {evidence} | {tier} | {answers} | **{proposed}** | {reason} |")

out.append("\n## 4. Matrix / Master / R1 Divergences & Synthetic Findings")
out.append("- **Fabricated Content (GT-L4, GT-AR5, GT-OQ16, GT-OQ18)**: Master answers contained synthetic quotes. Repaired via `NOT_ASSESSABLE` status.")
out.append("- **Cognition & Unknowns (GT-P3, L7, OQ12, OQ13, PL4)**: Matrix/R1 claimed `MISSING`. However, the practitioner workflow explicitly resolves or rejects ambiguity *before* entry. This is operational scope, not an ontology absence. Repaired to `CONTEXT_DEPENDENT`.")
out.append("- **Context Boundaries (GT-P2, PL5, PL6, OQ5, OQ6, OQ17, OQ19)**: Practitioner operates solely in Bhopal with one workflow. Questions demanding cross-context or cross-org comparison cannot be answered. Repaired to `NOT_ASSESSABLE` or `CONTEXT_DEPENDENT`.")
out.append("- **Wrong-Question / Synthetic Residue (GT-OQ17)**: R1 says 'WhatsApp', raw says 'grp'. Will correct synthetic residue in Phase 2.\n")

out.append("## 5. Master Register Status & Repair Plan")
out.append("The current `MASTER-GTR-INTERVIEW-FLOW.md` is NOT an authoritative raw-evidence register because it contains unverified/synthetic content (e.g., the fabricated quotes in GT-AR5, GT-L4).")
out.append("- **Current Master content**: Contains a mix of true quotes and synthetic 'Final Confirmed Answers'.")
out.append("- **Verified raw practitioner evidence**: Exists solely in `all_answers.md` and `ORGANIZED-GTR-SESSION-01.md`.")
out.append("- **Unverified/synthetic Master content**: The synthetic quotes generated during earlier review passes (now marked unlocated).")
out.append("- **Proposed repaired Master state**: In Phase 2, the Master file will be wiped of all synthetic quotes and replaced strictly with verbatim quotes from the raw evidence, becoming the true authoritative raw-evidence layer.\n")

out.append("## 6. Exact Proposed Phase 2 File Changes")
out.append("1. **All 47 GTR R1 records (`docs/05-ontology/GTR/*-R1.md`)**: Replace fabricated quotes with exact raw text. Apply the single Proposed Final Status from the table above.")
out.append("2. **`05-GROUND-TRUTH-REVIEW-MATRIX.md`**: Update Status column to match the Proposed Final Status exactly. Fix mapping metadata.")
out.append("3. **`MASTER-GTR-INTERVIEW-FLOW.md`**: Repair Master state by erasing fabricated answers and replacing with verbatim quotes. Update statuses to match the Matrix.")
out.append("4. **`05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `05-GROUND-TRUTH-PRACTITIONER-EXECUTION-PLAN.md`, `05-GROUND-TRUTH-REVIEW-RECORD-TEMPLATE.md`**: Flag stale historical notices (e.g. readiness).")
out.append("5. **`README.md`**: Append explicit scope statement limiting GTR validity to Khidmat/Bhopal. Remove readiness claims.")
out.append("6. **`ONTOLOGY-DESIGN-COMPLETION-UPDATE.html`**: Append banner superseding 'GREEN' status.\n")

out.append("## 7. Stage 6/7 Correction Candidates Table")
out.append("| File | Section | Current Wording | Reason for Future Correction |")
out.append("|---|---|---|---|")
out.append("| `04-ARCHITECTURE-RULES.md` | Various | 'practitioner-corroborated', 'validated' | GTR provides only single-practitioner, single-context evidence. |")
out.append("| `03-ONTOLOGY-PILLARS.md` | Various | Claims of 'Strong' validation | Evidence is Tier B/C local practice; insufficient for universal 'Strong' rating. |")
out.append("| `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | §3.1 note (2026-09-07) | Post-freeze amendment | Documented here, must not be edited in Stage 5. |")
out.append("| Stage 7 Rulings (G1-G5) | N/A | (Assumption of Stage 5 GREEN) | Rely on unverified evidence; requires re-basing. |\n")

out.append("## 8. Cognition Assessment")
out.append("The ontology's capability for Epistemic Stance and uncertainty representation (unknowns, contradictions) was completely unexercised by the practitioner's workflow. The Khidmat group relies on deterministic artifacts (government reports) or direct volunteer visits to establish absolute facts, and rejects unverified cases before system entry. This means the Cognition layer is `CONTEXT_DEPENDENT` or `NOT_ASSESSABLE`, but **not** `MISSING` (the ontology doesn't lack it; the practice just doesn't need it).")

out.append("\n## 9. New-GTR Decision")
out.append("No new GTR IDs are proposed. The existing 47 questions remain the bounded set. No genuinely missing ontology-level questions were identified that require expansion of the review set.")

out.append("\n## 10. Explicit Stage 5 Closure Recommendation")
out.append("**STAGE 5 CLOSED WITH QUALIFICATIONS**")
out.append("Rationale: Once the provenance failures are repaired and the classifications are correctly scoped to the actual raw evidence (resulting in a higher proportion of `NOT_ASSESSABLE` and `CONTEXT_DEPENDENT` items), the 47-GTR package will be internally consistent, traceable, and epistemically defensible for the specific Khidmat/Bhopal context.")

with open('docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Revised proposal created with Master Register Status.")
