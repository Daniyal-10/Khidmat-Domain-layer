import json

with open('scratch/gtr_data.json', 'r') as f:
    data = json.load(f)

divergences = {}
for gtr_id, row in data.items():
    statuses = {row['matrix_status'], row['master_status'], row['r1_status']}
    if len(statuses) > 1:
        divergences[gtr_id] = row

with open('scratch/divergences.json', 'w') as f:
    json.dump(divergences, f, indent=2)
print(f"Found {len(divergences)} divergences.")
