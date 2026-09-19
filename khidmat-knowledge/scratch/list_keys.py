import json

with open('scratch/gtr_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Let's map out the evidence for all 47 to make a decision
keys = data.keys()
for k in keys:
    print(k, data[k]['r1_status'])
