# Khidmat Knowledge Architecture

## Domain Inventory

| Domain                  | Maturity  | Status              |
|-------------------------|-----------|---------------------|
| shared                  | Level 1   | Active              |
| registration            | Level 1   | Active              |
| verification-operations | Level 2   | Placeholder         |
| case-management         | Level 2   | Placeholder         |
| beneficiary-lifecycle   | Level 2   | Placeholder         |
| volunteer-operations    | Level 2   | Placeholder         |
| support-delivery        | Level 2   | Placeholder         |
| programs                | Level 2   | Placeholder         |
| impact                  | Level 2   | Placeholder         |

## Dependency Rules

- registration/ may import from shared/
- No other domain may import from registration/
- Future domains may import from shared/
- No circular dependencies permitted
- Concepts shared between two or more domains must be promoted to shared/

## Maturity Levels

Level 1: Taxonomy, ontology, reasoning, and questioning are fully defined
         and production-ready. Files are complete.

Level 2: Folder exists. README declares scope.
         Placeholder file lists concepts the domain will eventually own.
         No taxonomy or ontology is invented until the domain enters active development.