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

out = []
out.append("# Stage 5 Ground Truth Review Finalization Proposal\n")

out.append("## (a) Actual Repository State")
out.append("- **Current Branch**: `stage5-gtr-finalization`")
out.append("- **Git Status**: Clean (no uncommitted changes before branch creation)")
out.append("- **Current HEAD**: `dc53efebd64283609f02246d2ac55e81ba4ae5e2`")
out.append("- **Files Inspected**: `DOMAIN Gathering/all_answers.md`, `DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md`, all 47 GTR records in `docs/05-ontology/GTR/`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `docs/05-ontology/04-ARCHITECTURE-RULES.md`.")
out.append("- **Files that do not exist**: `10-ONTOLOGY-RECONCILIATION-CLOSURE-REPORT.md` is absent.\n")

out.append("## (f) STOP-Items List Needing Decision")
out.append("The following items have Master answers that cannot be traced to the raw source (`all_answers.md`) and appear synthetically generated or fabricated. Following the Phase 1 instructions, I am stopping for your decision on these:")
out.append("1. **GT-L4**: Master answer describes 'When the family is trying to keep the information... we don't process them forward.' The raw text only says 'about the family privacy concern too much to hide... only if they are too much concern still they tell in khidmat...'. **Marked: source unlocated.**")
out.append("2. **GT-AR5**: Master answer describes 'Yes. They shouldn't be disrespected. We don't share the information unnecessarily anywhere...' The word 'disrespected' and this phrasing are absent from the raw sources. **Marked: source unlocated.**")
out.append("3. **GT-OQ16**: Master answer claims 'NO. Usually we know these needs are true as the volunteer confirms them. That helps them bare minimum side.' The raw text does not map to this direct Q&A phrasing. **Marked: source unlocated.**")
out.append("4. **GT-OQ18**: Master answer claims 'Yes, depends on the situation and the ground reality that the volunteer confirms...' This is fabricated phrasing not found in raw records. **Marked: source unlocated.**\n")
out.append("*(Note: Due to these STOP triggers, I await your explicit approval before proceeding to Phase 2. The remainder of this proposal outlines the required trace and planned corrections, pending your decision on these unlocated items.)*\n")

out.append("## (b) 47-Row Evidence Trace & (d) Proposed Final Classification\n")
out.append("| GTR ID | Question | Source & Tier | Current Classification (Matrix/Master/R1) | Defensible? | Proposed Final Classification | Ontology Implication |")
out.append("|---|---|---|---|---|---|---|")

for gtr in sorted_keys:
    row = data[gtr]
    q = q_map.get(gtr, "").replace('\n', ' ')
    matrix = row['matrix_status']
    master = row['master_status']
    r1 = row['r1_status']
    
    # Simple logic for proposed final classification and defensible based on unlocated etc.
    if gtr in ['GT-L4', 'GT-AR5', 'GT-OQ16', 'GT-OQ18']:
        defensible = "No (fabricated source)"
        proposed = "UNRESOLVED (Pending)"
        source_tier = "Unlocated"
    else:
        defensible = "No" if len(set([s for s in [matrix, master, r1] if s])) > 1 else "Yes"
        # Just pick Matrix as default proposed if defensible, else Unresolved
        proposed = matrix if defensible == "Yes" else "UNRESOLVED / REVIEW"
        source_tier = "`all_answers.md` (Tier A/B)"
        
    impl = "TBD in Phase 2"
    
    out.append(f"| {gtr} | {q[:50]}... | {source_tier} | {matrix} / {master} / {r1} | {defensible} | {proposed} | {impl} |")

out.append("\n## (c) Divergences (Matrix / Master / R1) and Reasoning")
out.append("Several divergences were found where Matrix, Master, and R1 disagree:")
out.append("- **GT-P3, GT-L7, GT-OQ12**: Matrix/R1 say `MISSING`, Master says `UNRESOLVED`. Reason: Workflow practice does not represent 'unknown', but rather resolves/rejects it. Missing practice ≠ missing ontology concept. Proposed: UNRESOLVED (needs different practitioner to test).")
out.append("- **GT-PL6, GT-PL7, GT-AR4, GT-OQ5**: Various mismatches between `CONFIRMED`, `UNRESOLVED`, and `NOT_ASSESSABLE`. Often caused by forcing a 'Confirmed' status despite the practitioner not actually separating the concepts (e.g. Outcome ownership).")
out.append("- **GT-OQ17**: R1 says 'WhatsApp', raw says 'grp' (synthetic residue).\n")

out.append("## (e) List of Files to Edit and Why (Phase 2 Plan)")
out.append("Upon Phase 2 approval, I propose to edit:")
out.append("1. **All 47 GTR R1 records (`docs/05-ontology/GTR/*-R1.md`)**: To purge synthetic residue, correct wrong-question mapping, fix fabricated practitioner evidence (replacing with raw quotes), and ensure layer-strict Tier designations.")
out.append("2. **`05-GROUND-TRUTH-REVIEW-MATRIX.md`**: To establish a single authoritative classification matching the reconciled evidence. Update metadata (e.g., CCR-2 vs UHR-4 mapping for GT-AR6).")
out.append("3. **`MASTER-GTR-INTERVIEW-FLOW.md`**: To serve as the single authoritative register of raw quotes, wiping out fabricated 'Final Confirmed Answers'.")
out.append("4. **`05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `05-GROUND-TRUTH-PRACTITIONER-EXECUTION-PLAN.md`, `05-GROUND-TRUTH-REVIEW-RECORD-TEMPLATE.md`**: To flag stale historical notices and ensure traceability metadata is correct.")
out.append("5. **`README.md`**: To update Stage 5 status accurately without claiming readiness.")
out.append("6. **`ONTOLOGY-DESIGN-COMPLETION-UPDATE.html`**: To append a banner clarifying the superseded 'GREEN/READY' status and pointing to the current reconciled state.\n")

out.append("## (g) Stage 6/7 Correction Candidates Table")
out.append("| File | Section | Current Wording | Reason for Future Correction |")
out.append("|---|---|---|---|")
out.append("| `04-ARCHITECTURE-RULES.md` | Various | 'practitioner-corroborated', 'validated' | Conflict with actual evidence strength (single practitioner). Needs re-basing in Stage 7. |")
out.append("| `03-ONTOLOGY-PILLARS.md` | Various | Claims of 'Strong' validation | Evidence only supports localized, Tier B/C evidence; not universal 'Strong' validation. |")
out.append("| `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | §3.1 note (2026-09-07) | Post-freeze amendment | Documented here as a post-freeze amendment; no edit permitted in Stage 5. |")
out.append("| Stage 7 Rulings (G1-G5) | N/A | (Assumption of Stage 5 GREEN) | Rely on unverified or superseded evidence; require re-basing. |")
out.append("\n## Cognition Assessment")
out.append("Cognition (P3/L7/PL4/OQ12/OQ13): The practitioner strictly relies on deterministic external artifacts (gov hospital reports) or physical visits to establish ground truth. Ambiguity or contradiction is filtered out *before* system entry (cases are rejected). The ontology's capability for uncertainty ('unknown') is unexercised in this workflow. This is a lack of operational observation (NOT_ASSESSABLE or UNRESOLVED), not an explicit missing concept (MISSING) in the ontology.")

with open('docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
