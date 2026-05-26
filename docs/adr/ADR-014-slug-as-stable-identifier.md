# ADR-014: Slug as stable identifier (human-readable kebab-case)

**Status:** Accepted
**Date:** 2026-05-25

## Context

Every wiki page and source needs a stable identifier used as the citation anchor (`[[sources/<id>]]`) and as the filename. The identifier format affects debuggability, URL shape, collision risk, and how well it survives refactoring.

## Decision

Source IDs use a structured kebab-case format: `<type>-<YYYY>-<MM>-<DD>-<hash8>` (e.g., `web-2026-01-15-a3f7b2c1`). Wiki page slugs use human-readable kebab-case derived from the title (e.g., `glp1-receptor-agonists`). Slugs are capped at 80 characters (enforced by the validator). A `slugmap.yaml` registry catches cross-type slug collisions.

UUID as ID was rejected: UUIDs are opaque in `git log`, `grep`, and terminal output. A pure content hash was rejected: the hash changes if the source is re-processed, breaking existing citations. Auto-incrementing integers were rejected: they are fragile when sources are deleted or imported from multiple origins.

## Consequences

Slug collisions between similar titles (e.g., two papers titled "Obesity Treatment") require manual disambiguation. The validator warns on high-similarity slugs. Human-readable slugs leak title information into filenames, which is acceptable for a personal knowledge base but would require reconsideration for multi-tenant or public deployments.
