# Business Flow Validation Report: Programs

## 1. Program Design & Initialization
- **Transition**: A humanitarian organization or government defines a new initiative. The Program entity is created, its thematic area assigned, and its Intervention Catalogue defined.
- **Dependency**: Shared ontology (Sectors, Actor types).

## 2. Eligibility Definition
- **Transition**: Program Managers attach Eligibility Criteria to the Program. These criteria use the concepts from the Shared Human Model and Risk domain to define inclusion/exclusion rules.
- **Dependency**: Risk Domain (Vulnerability, Resilience), Shared Human Model.

## 3. Case Plan Matching (Enrollment)
- **Transition**: A Case Manager reviews an assessed family. The system evaluates the family against active Programs. If eligible, the family is proposed for Enrollment, and interventions from the Program's catalogue are added to the Case Plan.
- **Dependency**: Case Management, Needs Assessment.

## 4. Capacity & Quota Management
- **Transition**: As beneficiaries are enrolled, the Program's conceptual capacity (e.g., "funded for 500 households") is drawn down. If capacity is reached, new eligible cases are Waitlisted.

## 5. Program Cycle Advancement
- **Transition**: A Program reaches the end of its annual cycle. All active enrollments undergo review for continuation, graduation, or termination based on updated needs assessments.
- **Dependency**: Beneficiary Lifecycle, Verification Operations (for re-verification).

## 6. Program Closure
- **Transition**: The Program concludes. Enrolled beneficiaries are systematically exited or transitioned to a successor program. Cohort-level impact metrics are finalized.
- **Dependency**: Impact, Case Management (for administrative closure of related case plans).
