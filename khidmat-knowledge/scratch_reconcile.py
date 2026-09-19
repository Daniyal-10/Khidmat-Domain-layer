import re

file_path = r'D:\CODINGGGGGGG\AI Research\PROJECTTTTSSSSS\Khidmat Domain layer\khidmat-knowledge\DOMAIN Gathering\MASTER-GTR-INTERVIEW-FLOW.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to split the file by blocks starting with '### GT-'
blocks = re.split(r'(?=### GT-)', content)

new_blocks = [blocks[0]]

for block in blocks[1:]:
    m = re.match(r'### (GT-[A-Z0-9]+)', block)
    if not m:
        new_blocks.append(block)
        continue
    gt_id = m.group(1)
    
    # Defaults
    if '[X] ANSWER PROVIDED' not in block:
        block = block.replace('`[ ] CONFIRMED`', '`[X] CONFIRMED`')
        
    final_ans_str = ''
    
    # Exceptions
    if gt_id == 'GT-AR4':
        block = re.sub(r'\*\*Recorded Answer / Evidence from Previous Practitioner Session:\*\*.*?\*\*Evidence Status Before Confirmation:\*\*',
            '**Recorded Answer / Evidence from Previous Practitioner Session:**\n'
            '"we only send a experienced volunteer to the beneficary based on the lead survey so why we will have conflit on the, never happned" (Original recorded answer)\n\n'
            '**Correction based on actual evidence:**\n'
            'Experienced volunteers visit the beneficiary and conduct the ground-reality verification. The case proceeds only when the volunteer confirms the reported needs against ground reality. This acts as a human verification gate/sign-off.\n\n'
            '**Evidence Status Before Confirmation:**', block, flags=re.DOTALL)
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nCORRECTION REQUIRED / then CONFIRMED\n', block, flags=re.DOTALL)
    
    elif gt_id == 'GT-PL6':
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nPARTIALLY SUPPORTED / NOT FULLY CONFIRMED\n', block, flags=re.DOTALL)
        block = block.replace('`[X] CONFIRMED`', '`[ ] CONFIRMED`')
    
    elif gt_id == 'GT-PL7':
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nPARTIALLY SUPPORTED\n', block, flags=re.DOTALL)
        block = block.replace('`[X] CONFIRMED`', '`[ ] CONFIRMED`')
    
    elif gt_id == 'GT-OQ4':
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nPARTIALLY SUPPORTED\n', block, flags=re.DOTALL)
        block = block.replace('`[X] CONFIRMED`', '`[ ] CONFIRMED`')
    
    elif gt_id == 'GT-OQ5':
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nPARTIALLY SUPPORTED\n', block, flags=re.DOTALL)
        block = block.replace('`[X] CONFIRMED`', '`[ ] CONFIRMED`')
    
    elif gt_id == 'GT-OQ14':
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nNOT CONFIRMED / EVIDENCE DOES NOT FULLY ANSWER QUESTION\n', block, flags=re.DOTALL)
        block = block.replace('`[X] CONFIRMED`', '`[ ] CONFIRMED`')
    
    elif gt_id == 'GT-OQ17':
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nNOT FULLY CONFIRMED / NOT OBSERVED AS A DISTINCT LAYER IN THIS PRACTITIONER CONTEXT\n', block, flags=re.DOTALL)
        block = block.replace('`[X] CONFIRMED`', '`[ ] CONFIRMED`')
    
    elif gt_id == 'GT-OQ19':
        block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nNOT FULLY CONFIRMED / NOT OBSERVED AS A DISTINCT ROLE IN THIS PRACTITIONER CONTEXT\n', block, flags=re.DOTALL)
        block = block.replace('`[X] CONFIRMED`', '`[ ] CONFIRMED`')
        
    else:
        # One of the 39 (including the 4 already done)
        if gt_id not in ['GT-L4', 'GT-AR5', 'GT-OQ16', 'GT-OQ18']:
            # Normal confirmed
            # Extract recorded answer to put into final confirmed answer
            rec_match = re.search(r'\*\*Recorded Answer / Evidence from Previous Practitioner Session:\*\*\n(.*?)\n\*\*Evidence', block, flags=re.DOTALL)
            if rec_match:
                rec_text = rec_match.group(1).strip()
                block = re.sub(r'\*\*Final Confirmed Answer:\*\*\n.*?\*\*Final Status:\*\*', f'**Final Confirmed Answer:**\n{rec_text}\n\n**Final Status:**', block, flags=re.DOTALL)
            
            # Read previous Evidence Status Before Confirmation
            status_match = re.search(r'\*\*Evidence Status Before Confirmation:\*\*\n(.*?)\n', block)
            if status_match:
                st = status_match.group(1).strip()
                if st == 'NOT OBSERVED':
                    block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nNOT OBSERVED — CONFIRMED\n', block, flags=re.DOTALL)
                elif st == 'NOT ASSESSABLE':
                    block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nNOT ASSESSABLE — CONFIRMED\n', block, flags=re.DOTALL)
                else:
                    block = re.sub(r'\*\*Final Status:\*\*.*', '**Final Status:**\nCONFIRMED\n', block, flags=re.DOTALL)
    
    new_blocks.append(block)

new_content = ''.join(new_blocks)

# Update Top Summary
summary = '''## FINAL GTR CONFIRMATION SUMMARY

* Total Review IDs: 47
* Confirmed: 39
* Partially supported: 4
* Not confirmed / not observed: 3
* Corrections required: 1
* Final confirmation pending: 0'''

new_content = re.sub(r'## FINAL GTR CONFIRMATION SUMMARY.*?---', summary + '\n\n---', new_content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done')
