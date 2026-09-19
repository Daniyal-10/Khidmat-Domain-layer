import json
import re

def parse_master_questions():
    with open('DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md', 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = re.split(r'###\s+(GT-[A-Z0-9]+)', content)
    questions = {}
    for i in range(1, len(blocks), 2):
        gtr_id = blocks[i]
        block = blocks[i+1]
        
        q_match = re.search(r'\*\*Question:\*\*\s*(.*?)\n\n', block, re.DOTALL)
        q = q_match.group(1).strip() if q_match else ""
        questions[gtr_id] = q
    return questions

q_map = parse_master_questions()

with open('scratch/gtr_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def sort_key(k):
    match = re.match(r'GT-([A-Z]+)(\d+)', k)
    if match:
        prefix = match.group(1)
        num = int(match.group(2))
        order = {'P': 1, 'L': 2, 'PL': 3, 'AR': 4, 'OQ': 5}
        return (order.get(prefix, 99), num)
    return (99, 0)

sorted_keys = sorted(data.keys(), key=sort_key)

with open('scratch/proposal_draft.md', 'w', encoding='utf-8') as f:
    f.write("# Stage 5 Ground Truth Review Finalization Proposal\n\n")
    f.write("## 1. Actual Repository State\n")
    f.write("- **Current Branch**: `stage5-gtr-finalization`\n")
    f.write("- **Git Status**: Clean (no uncommitted changes)\n")
    f.write("- **Current HEAD**: `dc53efebd64283609f02246d2ac55e81ba4ae5e2`\n")
    f.write("- **Files Inspected**: `all_answers.md`, `MASTER-GTR-INTERVIEW-FLOW.md`, `05-GROUND-TRUTH-REVIEW-MATRIX.md`, 47 GTR records.\n")
    f.write("- **Files that do not exist**: `10-ONTOLOGY-RECONCILIATION-CLOSURE-REPORT.md`.\n\n")
    
    f.write("## 2. 47-Row Evidence Trace\n\n")
    
    for gtr in sorted_keys:
        row = data[gtr]
        f.write(f"### {gtr}\n")
        f.write(f"- **Question**: {q_map.get(gtr, '')}\n")
        f.write(f"- **Current Classification** (Matrix/Master/R1): {row['matrix_status']} / {row['master_status']} / {row['r1_status']}\n")
        f.write(f"- **Master Answer**: {row['master_answer']}\n")
        f.write(f"- **R1 Evidence**: {row['r1_evidence']}\n")
        f.write("\n")
