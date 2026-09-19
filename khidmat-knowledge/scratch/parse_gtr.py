import os
import re
import json

def parse_matrix():
    with open('docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md', 'r', encoding='utf-8') as f:
        content = f.read()
    status_map = {}
    for line in content.split('\n'):
        if line.startswith('| GT-'):
            parts = [p.strip() for p in line.split('|')]
            # usually: | GT-P1 | Target | Primitive | Layer | Position | Question | Why | Expected | Status |
            # But the columns vary by table!
            gtr_id = parts[1]
            status = parts[-2]
            status_map[gtr_id] = status
    return status_map

def parse_master():
    with open('DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md', 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = re.split(r'###\s+(GT-[A-Z0-9]+)', content)
    master_map = {}
    for i in range(1, len(blocks), 2):
        gtr_id = blocks[i]
        block = blocks[i+1]
        
        answer_match = re.search(r'\*\*Final Confirmed Answer:\*\*\s*(.*?)\n\n', block, re.DOTALL)
        answer = answer_match.group(1).strip() if answer_match else ""
        
        status_match = re.search(r'\*\*Final Status:\*\*\s*([A-Z_]+)', block)
        status = status_match.group(1).strip() if status_match else ""
        
        master_map[gtr_id] = {'answer': answer, 'status': status}
    return master_map

def parse_r1(gtr_id):
    path = f'docs/05-ontology/GTR/{gtr_id}-R1.md'
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    evidence_match = re.search(r'\|\s*\*\*Evidence / response\*\*\s*\|\s*(.*?)\s*\|', content)
    evidence = evidence_match.group(1).strip() if evidence_match else ""
    
    status_match = re.search(r'\|\s*\*\*Finding classification\*\*\s*\|\s*(.*?)\s*\|', content)
    status = status_match.group(1).strip() if status_match else ""
    
    return {'evidence': evidence, 'status': status}

matrix = parse_matrix()
master = parse_master()
all_data = {}
for gtr_id in matrix.keys():
    r1 = parse_r1(gtr_id)
    all_data[gtr_id] = {
        'matrix_status': matrix.get(gtr_id, ''),
        'master_status': master.get(gtr_id, {}).get('status', ''),
        'master_answer': master.get(gtr_id, {}).get('answer', ''),
        'r1_status': r1.get('status', '') if r1 else '',
        'r1_evidence': r1.get('evidence', '') if r1 else ''
    }

with open('scratch/gtr_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=2)

divergences = {}
for gtr_id, row in all_data.items():
    statuses = set([s for s in [row['matrix_status'], row['master_status'], row['r1_status']] if s])
    if len(statuses) > 1:
        divergences[gtr_id] = row

with open('scratch/divergences.json', 'w', encoding='utf-8') as f:
    json.dump(divergences, f, indent=2)

print(f"Parsed {len(all_data)} items. Found {len(divergences)} divergences.")
