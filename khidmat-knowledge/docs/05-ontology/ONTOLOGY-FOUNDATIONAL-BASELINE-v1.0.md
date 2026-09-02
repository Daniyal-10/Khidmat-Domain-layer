# ONTOLOGY-FOUNDATIONAL-BASELINE-v1.0

## 1. Status

> Khidmat Humanitarian Domain Ontology — Foundational Design Formally Closed

Reference:
`TASK-6B-FINAL-ONTOLOGY-CLOSURE-VERIFICATION.md`

---

## 2. Closed Primitive Set

Exactly:
1. Condition
2. Context
3. Epistemic Stance
4. Entity
5. Norm
6. Occurrence
7. Relation

---

## 3. Closed Layer Set

Exactly:
1. Facets
2. Entities
3. Relationships
4. Constraints
5. States
6. Events
7. Cognition
8. Coordination Patterns

---

## 4. Closed Pillar Set

Exactly:
1. Human & Social Subject
2. Context & Environment
3. Vulnerability & Need
4. Epistemics & Knowledge
5. Actors & Ecosystem
6. Action & Coordination
7. Resources & Support

---

## 5. Foundational Semantic Boundaries

* Reality ≠ Claim ≠ Epistemic Stance
* Person ≠ Identifier / Reference
* Identifier / Reference ≠ Sameness Claim
* Sameness Claim ≠ Epistemic Stance
* Occurrence ≠ State
* Evidence ≠ Claim
* Evidence ≠ Epistemic Stance
* Organisation ≠ Programme
* Outcome / Impact ≠ measurement representation
* Administrative record ≠ humanitarian reality
* Unknown ≠ false
* absence of information ≠ negative fact

---

## 6. Explicit Implementation Boundary

The ontology does NOT prescribe:
* database schema
* tables
* API contracts
* JSON structures
* event-sourcing implementation
* workflow engines
* storage structures
* AI-agent architecture

The ontology provides semantic constraints and vocabulary; downstream architecture must implement rather than redefine it.

---

## 7. Known Non-Blocking Items

### GOVERNED PROVISIONAL
* Need Interactions
* Service Provider agency
* Outcome/Impact ownership
* Funder Altitude
* Case Orchestration

### UNRESOLVED — NON-MANDATORY — NON-FORECLOSING
* CCR-7 Dual-clock rule

### PARAMETER-ABSENT
* Vulnerability / Risk composition thresholds

### DEFERRED TAXONOMIC DETAIL
* Evidence taxonomy depth
* Specific giving-side patterns
* Human-facet value sets

These do NOT invalidate foundational ontology closure.

---

## 8. Closure Authority

The formal closure decision is supported by:
```text
TASK-6-FINAL-ONTOLOGIST-ONLY-CLOSURE-AUDIT.md
TASK-6A-AUTHORITATIVE-ONTOLOGY-REMEDIATION.md
TASK-6B-FINAL-ONTOLOGY-CLOSURE-VERIFICATION.md
```

---

## 9. Downstream Rule

> Downstream architecture, domain modeling, implementation, and AI systems must implement the closed ontology rather than silently redefine its foundational semantics.

If downstream work reveals a genuine semantic contradiction, it must be raised explicitly as an ontology change request rather than silently modifying the ontology.
