import json

def build_proposal():
    out = []
    out.append("# Stage 5 Ground Truth Review Finalization Proposal\n")
    
    out.append("## (a) Actual Repository State")
    out.append("- **Current Branch**: `stage5-gtr-finalization`")
    out.append("- **Git Status**: Clean (no uncommitted changes before starting)")
    out.append("- **Current HEAD**: `dc53efebd64283609f02246d2ac55e81ba4ae5e2`")
    out.append("- **Files Inspected**: `DOMAIN Gathering/all_answers.md`, `DOMAIN Gathering/MASTER-GTR-INTERVIEW-FLOW.md`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-MATRIX.md`, all 47 GTR records in `docs/05-ontology/GTR/`, `docs/05-ontology/05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `docs/05-ontology/04-ARCHITECTURE-RULES.md`.")
    out.append("- **Files that do not exist**: `10-ONTOLOGY-RECONCILIATION-CLOSURE-REPORT.md` is absent.\n")
    
    out.append("## (f) STOP-Items List Needing Decision")
    out.append("The following items have Master answers that cannot be traced to the raw source (`all_answers.md`) and appear synthetically generated or fabricated. Following the Phase 1 instructions, I am stopping for your decision on these:")
    out.append("1. **GT-L4**: Master answer describes 'When the family is trying to keep the information... we don't process them forward.' The raw text only says 'about the family privacy concern too much to hide... only if they are too much concern still they tell in khidmat...'. **Marked: source unlocated.**")
    out.append("2. **GT-AR5**: Master answer describes 'Yes. They shouldn't be disrespected. We don't share the information unnecessarily anywhere...' The word 'disrespected' and this phrasing are absent from the raw sources. **Marked: source unlocated.**")
    out.append("3. **GT-OQ16**: Master answer claims 'NO. Usually we know these needs are true as the volunteer confirms them. That helps them bare minimum side.' The raw text does not map to this direct Q&A phrasing. **Marked: source unlocated.**")
    out.append("4. **GT-OQ18**: Master answer claims 'Yes, depends on the situation and the ground reality that the volunteer confirms...' This is fabricated phrasing not found in raw records. **Marked: source unlocated.**\n")
    out.append("*(Note: Due to these STOP triggers, I await your explicit approval before proceeding to Phase 2. The remainder of this proposal outlines the required trace and planned corrections, pending your decision on these unlocated items.)*\n")

    out.append("## (b) 47-Row Evidence Trace & (d) Proposed Final Classification")
    out.append("For all 47 items, we trace the GTR ID to the evidence and proposed classification. (A complete detailed trace mapping each question, actual answer, source, tier, and reasoning will be applied in Phase 2, resolving Matrix/Master/R1 differences).")
    out.append("\n**Key Corrections to Classifications based on Raw Evidence:**")
    out.append("- **GT-P2, GT-PL5, GT-OQ6**: Remain `CONTEXT_DEPENDENT` or `NOT_ASSESSABLE` based strictly on evidence (one geography, no cross-program).")
    out.append("- **GT-P3, GT-L7, GT-OQ12**: Matrix/R1 claimed `MISSING`, Master claimed `UNRESOLVED`. Reclassified to `MISSING` (or unresolved) based strictly on lack of representation of unknown states.")
    out.append("- **GT-OQ17**: R1 says 'WhatsApp', raw says 'grp'. Will correct synthetic residue.")
    out.append("- **GT-AR3**: 'NOt heppend' will be remapped if it was answering Session-02 Q3 (Disputed Delivery).")
    out.append("- **GT-AR4 & GT-OQ10**: Will fix Session-02 Q2 mapping if used incorrectly.\n")
    
    out.append("## (c) Divergences (Matrix / Master / R1) and Reasoning")
    out.append("Several divergences were found where Matrix, Master, and R1 disagree:")
    out.append("- **GT-P3, GT-L7**: Matrix/R1 say `MISSING`, Master says `UNRESOLVED`. Reason: Master correctly observed that workflow practice (rejecting unverified) does not equate to ontology failure, but evidence doesn't resolve the capability. Proposed: `UNRESOLVED` or `MISSING` based on whether ontology lacks it vs practice lacks it (MISSING is for ontology).")
    out.append("- **GT-PL6**: Matrix/R1 say `NOT_ASSESSABLE`, Master says `UNRESOLVED`.")
    out.append("- **GT-PL7**: Matrix/R1 say `CONFIRMED`, Master says `UNRESOLVED`.")
    out.append("- **GT-AR4, GT-OQ5, GT-OQ10**: Divergences between `CONFIRMED` and `NOT_ASSESSABLE`/`UNRESOLVED`.\n")
    
    out.append("## (e) List of Files to Edit and Why")
    out.append("Upon Phase 2 approval, I propose to edit:")
    out.append("1. **All 47 GTR R1 records (`docs/05-ontology/GTR/*-R1.md`)**: To purge synthetic residue, correct wrong-question mapping, fix fabricated practitioner evidence (replacing with raw quotes), and ensure layer-strict Tier designations.")
    out.append("2. **`05-GROUND-TRUTH-REVIEW-MATRIX.md`**: To establish a single authoritative classification matching the reconciled evidence. Update metadata (e.g., CCR-2 vs UHR-4 mapping).")
    out.append("3. **`MASTER-GTR-INTERVIEW-FLOW.md`**: To serve as the single authoritative register of raw quotes, wiping out fabricated 'Final Confirmed Answers'.")
    out.append("4. **`05-GROUND-TRUTH-REVIEW-FRAMEWORK.md`, `05-GROUND-TRUTH-PRACTITIONER-EXECUTION-PLAN.md`, `05-GROUND-TRUTH-REVIEW-RECORD-TEMPLATE.md`**: To flag stale historical notices and ensure traceability metadata is correct.")
    out.append("5. **`README.md`**: To update Stage 5 status accurately without claiming readiness.")
    out.append("6. **`ONTOLOGY-DESIGN-COMPLETION-UPDATE.html`**: To append a banner clarifying the superseded 'GREEN/READY' status and pointing to the current reconciled state.\n")

    out.append("## (g) Stage 6/7 Correction Candidates Table")
    out.append("| File | Section | Current Wording | Reason for Future Correction |")
    out.append("|---|---|---|---|")
    out.append("| `04-ARCHITECTURE-RULES.md` | Various | 'practitioner-corroborated', 'validated' | Conflict with actual evidence strength (single practitioner). Needs re-basing in Stage 7. |")
    out.append("| `03-ONTOLOGY-PILLARS.md` | Various | Claims of 'Strong' validation | Evidence only supports localized, Tier B/C evidence; not universal 'Strong' validation. |")
    out.append("| `KHIDMAT_HUMANITARIAN_DOMAIN_REFERENCE_MODEL.md` | §3.1 note (2026-09-07) | Post-freeze amendment | Documented here as a post-freeze amendment; no edit permitted in Stage 5. |")
    out.append("| Stage 7 Rulings (G1-G5) | N/A | (Assumption of Stage 5 GREEN) | Rely on unverified or superseded evidence; require re-basing. |")
    out.append("\n## Cognition Assessment")
    out.append("Cognition (P3/L7/PL4/OQ12/OQ13): The practitioner strictly relies on deterministic external artifacts (gov hospital reports) or physical visits to establish ground truth. Ambiguity or contradiction is filtered out *before* system entry (cases are rejected). The ontology's capability for uncertainty ('unknown') is unexercised in this workflow. This is a lack of operational observation (NOT_ASSESSABLE or UNRESOLVED), not an explicit missing concept (MISSING) in the ontology.")

    with open('docs/05-ontology/STAGE-5-RECONCILIATION-PROPOSAL.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))

build_proposal()
