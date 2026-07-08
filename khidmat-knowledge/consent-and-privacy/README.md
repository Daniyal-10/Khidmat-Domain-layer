# Consent & Privacy Domain

## Purpose

A minimal placeholder declaration for `Consent`, required so that Case Management
can reference a consent concept without inventing one of its own.

## Scope

**Level 2 placeholder.** A single minimal entity exists so downstream domains have
something concrete to reference; no broader privacy/consent taxonomy or reasoning
has been authored.

## Owns

- `Consent` (`ontology.yaml`) — a minimal placeholder declaration.

## Does Not Own

- Any broader data-protection, retention, or privacy-policy modelling — none of
  that exists yet in this repository.
- Consent *capture* mechanics during registration (owned by `registration/`, to
  the extent it exists there at all).

## Directory Structure

```
consent-and-privacy/
└── ontology.yaml    # Consent — minimal placeholder entity
```

## Related Documents

- `ARCHITECTURE.md` — Level 2 maturity definition
- `case-management/README.md` — the domain that references `Consent` from here
- `ontology_authority_matrix.md` — Consent & Privacy Domain entry
- `architecture-decisions/ADR-004` — Placeholder Domain Strategy
