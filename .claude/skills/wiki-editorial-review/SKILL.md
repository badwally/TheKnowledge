---
name: wiki-editorial-review
description: Review wiki pages for quality — citation coverage, claim accuracy, staleness, cross-links
triggers: [wiki-editorial-review, wiki editorial-review]
---

## What This Does

Performs a structured editorial pass on one or more wiki pages: citation
grounding, claim currency, cross-link completeness, and schema compliance.
Produces a ranked list of issues with suggested remediation.

Reference conventions: WIKI.md § 12.2 (lint checks), § 7 (synthesis pages), § 6 (citations).

## Usage

```
/wiki-editorial-review wiki/concepts/food-noise.md
/wiki-editorial-review --domain glp1          # Review all glp1-tagged pages
```

## Execution Steps

1. **Run lint** on the target scope:
   ```
   .venv/bin/wiki lint [--scope <check>]
   ```
   Focus on: `citation-density`, `stale-claims`, `orphans`, `broken-wikilinks`, `schema-drift`.

2. **Read target pages**: For each flagged page, read the full content. Assess:
   - **Citation grounding**: every factual claim followed by `[[sources/<id>]]`?
   - **Claim currency**: references to recent events/studies that may be outdated?
   - **Cross-links**: does the page link to related concepts and entities?
   - **Schema compliance**: required frontmatter fields present? (WIKI.md § 3)

3. **Prioritize findings**: Rank by severity:
   - **Critical** — citation missing on a specific factual claim
   - **High** — stale claim with a clear update source
   - **Medium** — missing cross-link to a closely related page
   - **Low** — prose quality, heading structure

4. **Propose fixes**: For each critical/high finding, propose the specific remediation:
   - Missing citation → suggest running `/wiki-cite` on the page
   - Stale claim → identify the source that would update it
   - Missing cross-link → name the target page

5. **Apply with user approval**: Do not apply fixes autonomously. Present the
   ranked list and ask which to address. Then use the appropriate skill or command.

## Key constraints

- Read-only by default. Never edit pages without explicit user confirmation per finding.
- `wiki lint` writes a report to `.knowledge/lint/` — not a wiki page.
- Claim accuracy assessment is advisory; the user is the authority on domain knowledge.
