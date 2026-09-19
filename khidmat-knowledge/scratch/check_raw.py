import json
import re

with open('scratch/gtr_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('DOMAIN Gathering/all_answers.md', 'r', encoding='utf-8') as f:
    raw = f.read()

def normalize(t):
    return re.sub(r'\s+', ' ', t).strip().lower()

raw_norm = normalize(raw)
unlocated = []
for gtr, info in data.items():
    ans = info.get('master_answer', '')
    if not ans or ans.startswith('**Final Status:**'):
        continue
    # Strip quotes
    ans = ans.strip('"').strip("'")
    if not ans:
        continue
    parts = [p.strip() for p in ans.split('...')]
    found_all = True
    for p in parts:
        if not p: continue
        if normalize(p) not in raw_norm:
            # Maybe look for chunks if it's long? Let's just do a basic check
            # For short phrases like "Yes, depends on the situation..." we will see if it's there
            # Also check if it's in ORGANIZED-GTR-SESSION-01.md
            pass
            found_all = False
    
    if not found_all:
        unlocated.append(gtr)

print(f"Potentially unlocated items: {unlocated}")
