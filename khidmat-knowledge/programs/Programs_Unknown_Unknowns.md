# Programs: Unknown Unknowns

During discovery, several deep architectural ambiguities were identified that require further exploration or explicit bounding:

## 1. Budgeting vs. Conceptual Capacity
At what level of detail does Khidmat track program resources? If a program has $100,000, do we track every $50 intervention down to a live ledger balance? Or do we track "Capacity: 2000 Households" and rely on an external ERP for the financial audit? *Recommendation: Track conceptual capacity (quotas/slots), defer financial ledgers to ERPs.*

## 2. Managerial Overrides
Humanitarian work requires flexibility. If a program strictly requires age > 60, but a highly vulnerable 59-year-old presents, can a Program Manager override the eligibility? How does the ontology represent an enrollment that technically violates the program's defined criteria but was human-authorized?

## 3. Mutual Exclusivity and Double-Dipping
Who resolves multi-program conflicts? If Program A and Program B offer conflicting interventions, does Program A declare "Cannot be co-enrolled in Program B"? Modeling complex inter-program dependencies could create an unmaintainable web of rules.

## 4. The "Programless" Case
Can a Case Plan exist entirely outside of a Program? E.g., an ad-hoc emergency intervention funded by discretionary overhead. Does Khidmat require a "General Fund" pseudo-program to maintain structural integrity, or can Case Management operate independently of Programs in edge cases?

## 5. Evolving Eligibility
If a program changes its eligibility criteria halfway through the year, what happens to the already-enrolled beneficiaries who no longer qualify? Does the ontology need to version the eligibility criteria against the enrollment timestamp?
