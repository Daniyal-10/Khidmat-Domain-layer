# Repository Gap Report: Programs

### Type A — Already Covered
- **Actor Definitions**: Implementing Partners and Funder typologies belong to the Shared Ontology (`actor` / `organisation`).
- **Needs & Vulnerability Profiles**: The inputs for eligibility criteria are fully covered by the Shared Human Model and Risk domain.

### Type B — Belongs to Programs
- **Intervention Taxonomy Ownership**: The current `support-interventions` taxonomy was initiated during Registration modeling. This is a misplaced boundary. Programs definitively own the intervention catalogue. A migration must transfer ownership of this concept to Programs.
- **Program Entity Model**: The repository currently lacks a structural `Program` entity to group interventions and cohorts.
- **Eligibility Rule Primitives**: While the inputs exist (e.g., `household_income`, `disability_status`), the rule-engine vocabulary to bind them to a program (e.g., `requires_income_below`, `requires_age_over`) needs to be defined.
- **Enrollment State**: The macro-status (`Waitlisted`, `Enrolled`, `Graduated`, `Terminated`) is currently missing and distinct from Case Status.

### Type C — Belongs to Existing Domain
- **Case Plan Execution**: Linking an enrolled beneficiary to specific deliveries belongs to Case Management.
- **Impact Measurement**: Determining if the program worked belongs to Impact.

### Type D — Future Roadmap
- **Detailed Financial Ledgers**: Granular tracking of program expenditure, donor restrictions, and audit trails.
- **Grant Management**: Tracking the lifecycle of the funding proposal that created the program.

### Type E — Requires Architectural Decision
- **Cross-Program Constraints (Mutual Exclusivity)**: When two programs exist (e.g., Federal Food Subsidy and NGO Food Rations), who owns the rule that says a beneficiary cannot be enrolled in both simultaneously? Is it a Program-level constraint, or a Case Management conflict resolution rule?
