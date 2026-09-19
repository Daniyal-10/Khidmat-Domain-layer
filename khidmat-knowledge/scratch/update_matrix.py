import os
import re

def extract_proposal_data():
    with open('docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md', 'r', encoding='utf-8') as f:
        content = f.read()

    table_match = re.search(r'\|\s*GTR\s*\|\s*Proposed Final Status.*?\|(.*?)\n\n', content, re.DOTALL)
    rows = table_match.group(1).strip().split('\n')
    data = {}
    for row in rows:
        parts = [p.strip() for p in row.split('|') if p.strip()]
        if len(parts) >= 4 and parts[0].startswith('GT-'):
            gtr = parts[0]
            status = parts[1].replace('**', '')
            data[gtr] = status
    return data

def update_matrix(data):
    path = 'docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will look for | GT-XXX | ... | Status | and replace Status.
    lines = content.split('\n')
    out_lines = []
    for line in lines:
        if line.startswith('| GT-'):
            parts = line.split('|')
            gtr = parts[1].strip()
            if gtr in data:
                # the status is usually the last column (parts[-2])
                parts[-2] = f" {data[gtr]} "
                line = '|'.join(parts)
        out_lines.append(line)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines))

data = extract_proposal_data()
update_matrix(data)
print("Updated Matrix")
