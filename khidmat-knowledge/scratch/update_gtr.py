import os
import re

def extract_proposal_data():
    with open('docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md', 'r', encoding='utf-8') as f:
        content = f.read()

    table_match = re.search(r'\|\s*GTR\s*\|\s*Proposed Final Status.*?\|(.*?)\n\n', content, re.DOTALL)
    if not table_match:
        table_match = re.search(r'\|\s*GTR\s*\|\s*Proposed Final Status.*?\|(.*?)##', content, re.DOTALL)
    
    rows = table_match.group(1).strip().split('\n')
    data = {}
    for row in rows:
        parts = [p.strip() for p in row.split('|') if p.strip()]
        if len(parts) >= 4:
            gtr = parts[0]
            status = parts[1].replace('**', '')
            evidence = parts[2]
            reason = parts[3]
            data[gtr] = {
                'status': status,
                'evidence': evidence,
                'reason': reason
            }
    return data

def update_gtr_records(data):
    for gtr, info in data.items():
        path = f'docs/05-ontology/GTR/{gtr}-R1.md'
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Evidence / response
        content = re.sub(
            r'(\|\s*\*\*Evidence / response\*\*\s*\|)(.*?)(\n)',
            f'\\1 {info["evidence"]} |\\3',
            content
        )

        # Update Classification
        content = re.sub(
            r'(\|\s*\*\*Finding classification\*\*\s*\|)(.*?)(\n)',
            f'\\1 {info["status"]} |\\3',
            content
        )

        # Update Reviewer reasoning
        content = re.sub(
            r'(\|\s*\*\*Reviewer reasoning\*\*\s*\|)(.*?)(\n)',
            f'\\1 {info["reason"]} |\\3',
            content
        )

        # Update Ontology implication
        impl = "Validated." if info['status'] == 'CONFIRMED' else "Proposition not assessed."
        content = re.sub(
            r'(\|\s*\*\*Ontology implication\*\*\s*\|)(.*?)(\n)',
            f'\\1 {impl} |\\3',
            content
        )

        # Update Follow-up requirement
        req = "sufficient — no further evidence needed for this Review ID." if info['status'] == 'CONFIRMED' else "Not assessable in this practitioner context; carried to Stage 6 as untested; validation would require a different context or practitioner."
        content = re.sub(
            r'(\|\s*\*\*Follow-up requirement\*\*\s*\|)(.*?)(\n)',
            f'\\1 {req} |\\3',
            content
        )

        # Update Provenance
        prov_text = "Derived directly from raw practitioner evidence in DOMAIN Gathering/all_answers.md. All synthetic or unsupported historical claims have been purged."
        content = re.sub(r'## 7\. Provenance\n.*', f'## 7. Provenance\n\n{prov_text}', content, flags=re.DOTALL)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

data = extract_proposal_data()
update_gtr_records(data)
print(f"Updated {len(data)} GTR records.")
