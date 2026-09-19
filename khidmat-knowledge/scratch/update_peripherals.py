import os
import re

for root, _, files in os.walk('docs/05-ontology'):
    for file in files:
        if file in ['05-GROUND-TRUTH-REVIEW-FRAMEWORK.md', '05-GROUND-TRUTH-PRACTITIONER-EXECUTION-PLAN.md', '05-GROUND-TRUTH-REVIEW-RECORD-TEMPLATE.md']:
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            banner = '> [!WARNING] HISTORICAL DOCUMENT\n> This document reflects the original Stage 5 methodology. Practitioner validation was executed but is strictly scoped to one context (Khidmat, Bhopal). Claims of \'universal validation\' or \'practitioner consensus\' in this document are historical and have been superseded by the final reconciliation audit.\n\n'
            if '> [!WARNING] HISTORICAL DOCUMENT' not in content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(banner + content)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
readme = re.sub(r'Stage 5: .*?(\n)', r'Stage 5: RECONCILIATION COMPLETE — PENDING FINAL CLOSURE AUDIT (Note: Evidence scoped to single Khidmat context; NOT universally validated)\1', readme)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

html_path = 'ONTOLOGY-DESIGN-COMPLETION-UPDATE.html'
if os.path.exists(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html_banner = '<div style="background-color: #fff3cd; color: #856404; padding: 15px; margin-bottom: 20px; border: 1px solid #ffeeba; border-radius: 4px;"><strong>NOTICE:</strong> The Stage 5 "GREEN/READY" status described below has been superseded by a final epistemic reconciliation audit. The ontology is structurally intact, but the practitioner validation scope is officially limited to the Khidmat/Bhopal context. See the Stage 5 Reconciliation Proposal for details.</div>\n'
    if 'NOTICE:' not in html:
        html = html.replace('<body>', f'<body>\n{html_banner}')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
print('Updated peripheral files.')
