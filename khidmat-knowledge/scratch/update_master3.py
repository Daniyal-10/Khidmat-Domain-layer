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
            evidence = parts[2]
            reason = parts[3]
            data[gtr] = {'status': status, 'evidence': evidence, 'reason': reason}
    return data

def update_master(data):
    path = 'DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = re.split(r'(###\s+GT-[A-Z0-9]+)', content)
    out_blocks = [blocks[0]]
    for i in range(1, len(blocks), 2):
        header = blocks[i]
        block = blocks[i+1]
        gtr = header.split()[1]
        
        if gtr in data:
            if '**Final Status:**' not in block:
                # Add Verified Raw Evidence if not there
                if '**Verified Raw Evidence' not in block:
                    block = block.rstrip() + f"\n\n**Verified Raw Evidence (Tier A/B):**\n{data[gtr]['evidence']}\n"
                # Add Final Status
                block = block.rstrip() + f"\n\n**Final Status:**\n{data[gtr]['status']}\n"
                # Add Justification
                block = block.rstrip() + f"\n\n**Justification:**\n{data[gtr]['reason']}\n\n"
                
        out_blocks.append(header)
        out_blocks.append(block)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(''.join(out_blocks))

data = extract_proposal_data()
update_master(data)
print("Fixed missing Final Statuses in Master")
