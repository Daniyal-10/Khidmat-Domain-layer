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
            if '**Final Confirmed Answer' in block:
                if gtr in ['GT-L4', 'GT-AR5', 'GT-OQ16', 'GT-OQ18']:
                    ans_match = re.search(r'\*\*Final Confirmed Answer[^\n]*\*\*\s*(.*?)\n\n', block, re.DOTALL)
                    if ans_match and not 'UNSUPPORTED / SYNTHETIC' in ans_match.group(0):
                        old_ans = ans_match.group(1).strip()
                        new_ans_block = f"**Final Confirmed Answer (Historical/Synthetic):**\n> [!WARNING] UNSUPPORTED / SYNTHETIC PRIOR CONTENT — NOT PRACTITIONER EVIDENCE\n> {old_ans}\n\n**Verified Raw Evidence (Tier A/B):**\n{data[gtr]['evidence']}\n\n"
                        block = block.replace(ans_match.group(0), new_ans_block)
                else:
                    ans_match = re.search(r'\*\*Final Confirmed Answer[^\n]*\*\*\s*(.*?)\n\n', block, re.DOTALL)
                    if ans_match and not 'Verified Raw Evidence' in block:
                        new_ans_block = f"**Verified Raw Evidence (Tier A/B):**\n{data[gtr]['evidence']}\n\n"
                        block = block.replace(ans_match.group(0), new_ans_block)
            else:
                # Need to add it
                new_ans_block = f"\n**Verified Raw Evidence (Tier A/B):**\n{data[gtr]['evidence']}\n\n"
                # insert before "**Final Status:**" if exists, or just append
                if '**Final Status:**' in block:
                    block = block.replace('**Final Status:**', new_ans_block + '**Final Status:**')
                else:
                    block += new_ans_block
            
            if '**Final Status:**' in block:
                status_match = re.search(r'\*\*Final Status:\*\*\s*([A-Z_]+)', block)
                if status_match:
                    block = block.replace(status_match.group(0), f"**Final Status:**\n{data[gtr]['status']}")
            else:
                block += f"**Final Status:**\n{data[gtr]['status']}\n\n"
                
            if '**Justification:**' in block:
                just_match = re.search(r'\*\*Justification:\*\*\s*(.*?)(?=\n###|\Z)', block, re.DOTALL)
                if just_match:
                    block = block.replace(just_match.group(0), f"**Justification:**\n{data[gtr]['reason']}\n")
            else:
                block += f"**Justification:**\n{data[gtr]['reason']}\n"
                
        out_blocks.append(header)
        out_blocks.append(block)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(''.join(out_blocks))

data = extract_proposal_data()
update_master(data)
print("Updated Master Part 2")
