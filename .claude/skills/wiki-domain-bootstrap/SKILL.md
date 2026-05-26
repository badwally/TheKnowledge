---
name: wiki-domain-bootstrap
description: Bootstrap a new research domain — write policy, seed concept pages, confirm filter thresholds
triggers: [wiki-domain-bootstrap, wiki domain-bootstrap]
---

## What This Does

Creates a new research domain from a natural-language description: authors a
`policy.yaml`, seeds starter concept pages, and verifies the domain is ready
for source ingestion.

Reference conventions: WIKI.md § 10 (filter policy), § 10.1 (policy.yaml schema).

## Usage

```
/wiki-domain-bootstrap "GLP-1 agonists and metabolic disease" glp1-metabolic
/wiki-domain-bootstrap "AI safety and alignment research" ai-safety
```

## Execution Steps

1. **Check for duplicates**: Search `index.md` and `wiki/proposals/` for existing
   domains with overlapping scope. If one exists, ask whether to extend it or
   create a sibling.

2. **Bootstrap policy**:
   ```
   .venv/bin/wiki bootstrap-domain "<description>" <slug>
   ```
   This runs an LLM pass to author `policy.yaml` with inclusion/exclusion criteria.

3. **Review policy**: Read the generated `.knowledge/policies/<slug>/policy.yaml`.
   Verify:
   - `domain.topic` and `domain.description` are accurate
   - `inclusion_criteria` are specific and falsifiable
   - `exclusion_criteria` prevent scope creep
   Present to user and confirm or request edits.

4. **Seed concept pages** (optional): If the user wants starter concepts, author
   2-3 `wiki/concepts/<concept>.md` pages via `wiki concept-add`. These become
   the MoC anchors.

5. **Create MoC**: Author a `wiki/mocs/<slug>.md` map-of-content page linking
   the starter concepts.

6. **Verify readiness**: Run `wiki lint --scope filter-calibration`. A new domain
   with zero examples is expected — note that filter scores will be unreliable
   until 12+ examples are banked via `wiki filter-correct`.

## Key constraints

- All writes go through the gateway — never write policy.yaml or wiki pages directly (WIKI.md § 9).
- `bootstrap-domain` is LLM-heavy; it calls the API. Inform the user before running.
- Domain slugs are kebab-case, max 60 chars (WIKI.md § 2.1).
