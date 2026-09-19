import os
import re

def audit():
    matrix_path = 'docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md'
    master_path = 'DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md'
    prop_path = 'docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md'
    
    # Read Proposal
    with open(prop_path, 'r', encoding='utf-8') as f:
        prop_content = f.read()
    prop_map = {}
    table_match = re.search(r'\|\s*GTR\s*\|\s*Proposed Final Status.*?\|(.*?)\n\n', prop_content, re.DOTALL)
    for row in table_match.group(1).strip().split('\n'):
        parts = [p.strip() for p in row.split('|') if p.strip()]
        if len(parts) >= 2 and parts[0].startswith('GT-'):
            prop_map[parts[0]] = parts[1].replace('**', '')

    # Read Matrix
    with open(matrix_path, 'r', encoding='utf-8') as f:
        matrix_content = f.read()
    matrix_map = {}
    for line in matrix_content.split('\n'):
        if line.startswith('| GT-'):
            parts = [p.strip() for p in line.split('|') if p.strip()]
            matrix_map[parts[0]] = parts[-1]

    # Read Master
    with open(master_path, 'r', encoding='utf-8') as f:
        master_content = f.read()
    master_map = {}
    blocks = re.split(r'###\s+(GT-[A-Z0-9]+)', master_content)
    for i in range(1, len(blocks), 2):
        gtr = blocks[i]
        status_match = re.search(r'\*\*Final Status:\*\*\s*([A-Z_]+)', blocks[i+1])
        if status_match:
            master_map[gtr] = status_match.group(1)

    # Read R1s
    r1_map = {}
    for gtr in prop_map.keys():
        path = f'docs/05-ontology/GTR/{gtr}-R1.md'
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        m = re.search(r'\|\s*\*\*Finding classification\*\*\s*\|\s*([A-Z_]+)\s*\|', c)
        if m:
            r1_map[gtr] = m.group(1)
            
    # Audit
    confirmed = 0
    not_assessable = 0
    errors = []
    
    for gtr, p_status in prop_map.items():
        if p_status == 'CONFIRMED': confirmed += 1
        elif p_status == 'NOT_ASSESSABLE': not_assessable += 1
        
        mx_status = matrix_map.get(gtr)
        ms_status = master_map.get(gtr)
        r1_status = r1_map.get(gtr)
        
        if not (p_status == mx_status == ms_status == r1_status):
            errors.append(f"{gtr} mismatch: Prop={p_status}, Matrix={mx_status}, Master={ms_status}, R1={r1_status}")
            
    print(f"Total: {len(prop_map)}")
    print(f"CONFIRMED: {confirmed}")
    print(f"NOT_ASSESSABLE: {not_assessable}")
    if errors:
        for e in errors: print(e)
    else:
        print("Consistency: Matrix = Master = GTR R1 = Proposal")
        
audit()
