---
name: wiki-cite
description: Add or fix citations on a wiki page using cite-suggest — surface candidate sources, confirm, write citation tokens
triggers: [wiki-cite, wiki cite]
---

## What This Does

Surfaces citation candidates for a wiki page's uncited claims, confirms with
the user, and writes `[[sources/<id>]]` tokens via the gateway.

Reference conventions: WIKI.md § 6 (citation format), § 9 rule 3 (citation grounding).

## Usage

```
/wiki-cite wiki/synthesis/glp1-hunger.md
/wiki-cite wiki/concepts/food-noise.md --claim "Food noise is..."
```

## Execution Steps

1. **Read the page**: Identify claims without `[[sources/...]]` citation tokens.
   A claim is uncited if it ends a sentence without a wikilink to a source page.

2. **Run cite-suggest**: 
   ```
   .venv/bin/wiki cite-suggest wiki/<type>/<slug>.md
   ```
   This surfaces candidate source IDs ranked by semantic similarity.

3. **Review candidates**: For each uncited claim, show the top 1-2 candidates.
   Ask the user to confirm or provide the correct source ID.

4. **Write citations** (one at a time):
   ```
   .venv/bin/wiki cite-add wiki/<type>/<slug>.md --claim "<claim text>" --source <id>
   ```
   Or for line-level precision:
   ```
   .venv/bin/wiki cite wiki/<type>/<slug>.md --line <N> --source <id>
   ```

5. **Validate**: After all citations are added, run:
   ```
   .venv/bin/wiki finalize wiki/<type>/<slug>.md
   ```
   If validation fails, report the specific uncited claim.

## Key constraints

- Never use Edit to insert `[[sources/...]]` tokens directly — use `wiki cite` or `wiki cite-add`.
- Citation grounding applies to non-draft pages only. Use `--draft` at ingest to defer.
- Source IDs must exist in `raw/<type>/<id>.md` before citing them.
