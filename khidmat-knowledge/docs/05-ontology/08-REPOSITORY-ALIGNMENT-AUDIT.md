# REPOSITORY ALIGNMENT AUDIT

## 1. Purpose
The purpose of this audit is to perform a repository-wide documentation alignment and classification based on the newly gathered real Khidmat practitioner ground truth from GTR Session 01. The goal is to establish a clean, authoritative, evidence-aligned repository before proceeding to Evidence Integration, Ontology Mapping, and Ontology Refinement.

## 2. Methodology
The entire repository was reviewed, specifically the frozen baseline documents (`docs/02-understanding`, `docs/03-discovery`), the core reference model (`docs/04-reference-model`), the ontology structures (`docs/05-ontology`), and the raw practitioner evidence (`DOMAIN Gathering`). 

Each document was evaluated against the final decision rules:
- Modifications are only justified if the current document is inconsistent with established evidence/governance, not merely for cleanliness.
- Documents are archived if leaving them in the active knowledge path would cause a future ontologist/agent to use superseded assumptions.
- "FROZEN" statuses are strictly respected based on their governance meaning; frozen baseline documents should not receive arbitrary patches.

## 3. Current Repository State
The repository currently contains authoritative raw practitioner evidence from GTR Session 01, alongside previously frozen discovery and reference models. A recent change added a "Post-GTR Session 01 Evidence Update" patch across multiple files (`MERGED_BUSINESS_UNDERSTANDING.md`, `DOMAIN_DISCOVERY.md`, `SCOPE_COVERAGE.md`, `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md`, `02-ONTOLOGY-LAYERS.md`, `04-ARCHITECTURE-RULES.md`, and `ONTOLOGY-MAP-TRACEABILITY.md`). This haphazard patching violated the frozen historical trace status of several documents and bypassed the formal Stage 6/7 evidence integration and governance processes. 

## 4. Document Inventory
- `DOMAIN Gathering/all_answers.md`
- `DOMAIN Gathering/ORGANIZED-GTR-SESSION-01.md`
- `DOMAIN Gathering/GTR-SESSION-01-PROJECT-ALIGNMENT-CHANGE-REGISTER.md`
- `docs/02-understanding/MERGED_BUSINESS_UNDERSTANDING.md`
- `docs/03-discovery/DOMAIN_DISCOVERY.md`
- `docs/03-discovery/SCOPE_COVERAGE.md`
- `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md`
- `docs/05-ontology/01-DOMAIN-PRIMITIVES.md`
- `docs/05-ontology/02-ONTOLOGY-LAYERS.md`
- `docs/05-ontology/03-ONTOLOGY-PILLARS.md`
- `docs/05-ontology/04-ARCHITECTURE-RULES.md`
- `docs/05-ontology/05-GROUND-TRUTH-*`
- `docs/05-ontology/06-STAGE-6-EVIDENCE-INTEGRATION-REPORT.md`
- `docs/05-ontology/07-STAGE-7-GOVERNANCE-DECISIONS.md`
- `docs/07-closure-archive/ONTOLOGY-MAP-TRACEABILITY.md`

## 5. KEEP Documents
- `DOMAIN Gathering/ORGANIZED-GTR-SESSION-01.md`: Current, authoritative, and useful structured evidence.
- `docs/05-ontology/01-DOMAIN-PRIMITIVES.md`: Structurally sound, formally closed, no haphazard patches detected.
- `docs/05-ontology/03-ONTOLOGY-PILLARS.md`: Structurally sound, formally closed.
- `docs/05-ontology/05-GROUND-TRUTH-*`: Active frameworks and matrices for testing ground truth.

## 6. MODIFY Documents
- `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md`: Needs the "Post-GTR Session 01 Evidence Update" section removed or formally integrated, as it bypasses the "FROZEN 2026-07-29" governance status. 
- `docs/05-ontology/02-ONTOLOGY-LAYERS.md`: Has an improper §12.3 patch that requires evaluation through formal evidence integration rather than a direct file patch.
- `docs/05-ontology/04-ARCHITECTURE-RULES.md`: Has an improper §7.3 patch that requires formal governance rather than a direct file patch.
- `docs/07-closure-archive/ONTOLOGY-MAP-TRACEABILITY.md`: Has an improper patch (§3) that conflicts with its archival trace purpose.

## 7. ARCHIVE Candidates
- `DOMAIN Gathering/GTR-SESSION-01-PROJECT-ALIGNMENT-CHANGE-REGISTER.md`: Once the improper patches are rolled back/properly routed to Stage 6, this register of haphazard changes should be archived.

## 8. KEEP-AS-EVIDENCE Documents
- `DOMAIN Gathering/all_answers.md`: Raw practitioner Q&A. Must be preserved exactly as-is.

## 9. REVIEW-REQUIRED Documents
- `docs/02-understanding/MERGED_BUSINESS_UNDERSTANDING.md`: Frozen traceability record improperly patched. Review required to strip the patch and preserve it as historical evidence.
- `docs/03-discovery/DOMAIN_DISCOVERY.md`: Frozen traceability record improperly patched. Review required to strip the patch.
- `docs/03-discovery/SCOPE_COVERAGE.md`: Frozen traceability record improperly patched. Review required to strip the patch.

## 10. Contradictions with Session 01
- **Programmes**: GTR Session 01 indicates the grassroots Khidmat context operates without nested Programmes. The Reference Model / Ontology Layers (Stage 7 G1) split Organisation and Programme as distinct entities. The haphazard patches state "Programme does not exist in this context" which risks conflating a localized contextual fact with the universal ontology structure.
- **Verification**: GTR Session 01 relies on initial surveys treated as unverified claims, followed by experienced volunteer ground-checks. This maps to the Epistemic Stance layer (Claim vs Finding) but the exact evidence weights were not updated through formal governance.
- **Needs**: GTR Session 01 indicates general needs (food) are tracked at the family head level, while specific needs (medical) are tracked individually. The ontology layer does not yet fully reflect this specific relational structure.

## 11. Terminology Consistency Findings

| Term | Documents Using It | Meaning in Each | Consistent? | Required Action |
| ---- | ------------------ | --------------- | ----------- | --------------- |
| Organisation / Programme | RM, L2, L3, L4, Stage 7 G1, GTR-01 Patch | RM/L2/G1 splits them; GTR-01 patch claims grassroots lacks programmes | UNRESOLVED | Strip patches; address via Stage 6 integration (localize missing programmes to context). |
| Beneficiary / Person | GTR-01, Primitives, RM | GTR uses "Beneficiary/Zimmedar"; RM uses Person/Household | CONTEXT-SPECIFIC | Map Khidmat operational terms to foundational primitives via mapping layer. |
| Verification | RM, GTR-01 | RM sees it as Event changing Claim to Finding; GTR sees it as Volunteer Ground Check | CONFIRMED | Reconcile the operational process to the Epistemic Stance mechanisms. |

## 12. Cross-document Dependency Findings
- The `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` is the bedrock for the `05-ontology` suite (Primitives -> Layers -> Pillars -> Rules). Modifying the RM (as the recent patch did) structurally invalidates the locked state of the ontology unless passed through Stage 6 (Evidence Integration) and Stage 7 (Governance).
- `MERGED_BUSINESS_UNDERSTANDING.md` and `DOMAIN_DISCOVERY.md` trace into the RM. Their frozen statuses protect the rationale for the RM's original baseline.

## 13. Recommended Archive Structure
```text
docs/
└── 07-closure-archive/
    ├── historical-business-understanding/
    ├── historical-discovery/
    └── superseded-review-packages/
```
*Note: We should avoid creating too many folders, but we need clear places for frozen Tier B/C evidence and discovery that is no longer the active canonical model.*

## 14. Proposed Active Canonical Knowledge Path
```text
Raw Practitioner Evidence (all_answers.md)
        ↓
Organized GTR Evidence (ORGANIZED-GTR-SESSION-01.md)
        ↓
Current Reference Model (KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md - unpatched)
        ↓
Current Ontology Baseline (01-DOMAIN-PRIMITIVES, 02-ONTOLOGY-LAYERS, 03-ONTOLOGY-PILLARS, 04-ARCHITECTURE-RULES - unpatched)
        ↓
Stage 6 Evidence Integration Report (To be authored based on GTR-01)
        ↓
Stage 7 Governance Decisions (To be updated with GTR-01 rulings)
        ↓
Ontology Refinement (Future)
```

## 15. Documents requiring modification
- `docs/04-reference-model/KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` (Strip §17)
- `docs/05-ontology/02-ONTOLOGY-LAYERS.md` (Strip §12.3)
- `docs/05-ontology/04-ARCHITECTURE-RULES.md` (Strip §7.3)
- `docs/02-understanding/MERGED_BUSINESS_UNDERSTANDING.md` (Strip §12)
- `docs/03-discovery/DOMAIN_DISCOVERY.md` (Strip §7)
- `docs/03-discovery/SCOPE_COVERAGE.md` (Strip §6)
- `docs/07-closure-archive/ONTOLOGY-MAP-TRACEABILITY.md` (Strip §3)

## 16. Documents that must not be modified
- `DOMAIN Gathering/all_answers.md`
- `DOMAIN Gathering/ORGANIZED-GTR-SESSION-01.md`
- `docs/05-ontology/01-DOMAIN-PRIMITIVES.md`
- `docs/05-ontology/03-ONTOLOGY-PILLARS.md`

## 17. Risks of leaving repository unaligned
Leaving the haphazard "Post-GTR Session 01 Evidence Update" patches in frozen documents:
1. Destroys the historical traceability of the project (we lose the boundary between the original blueprint and new empirical data).
2. Conflates contextual/localized observations (e.g., "no nested programmes") with universal ontology changes without explicit governance.
3. Will cause future agents/ontologists to read contradictory instructions and base new architectures on un-governed operational anomalies.

## 18. Final recommendation
1. **Rollback**: Strip the haphazard "Post-GTR Session 01 Evidence Update" patches from all frozen baseline documents, the reference model, and the ontology files.
2. **Integration**: Route the findings from `ORGANIZED-GTR-SESSION-01.md` through a formal `06-STAGE-6-EVIDENCE-INTEGRATION-REPORT.md` pass.
3. **Governance**: Use the Stage 6 report to explicitly govern how the ontology will adapt to the grassroots evidence (Stage 7), preserving the universal layers while mapping the localized context.
4. **Archival**: Archive the `GTR-SESSION-01-PROJECT-ALIGNMENT-CHANGE-REGISTER.md` as it documents a bypassed process.

## 19. Explicit statement
**Ontology refinement has NOT yet been performed.** This audit explicitly identifies alignment issues and classifies documents. The ontology itself has not been changed, and the proposed modifications are strictly to restore document integrity, not to alter the ontology. 
