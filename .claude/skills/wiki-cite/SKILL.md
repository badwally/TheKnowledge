---
name: wiki-cite
description: Add or fix citations on a wiki page using cite-suggest, or capture a URL from any repo and add it as a citation (AGT-7). Triggers — "add citation", "cite this", "wiki cite", or when you have a quote + URL from another project.
triggers: [wiki-cite, wiki cite, cite-capture]
---

## What This Does

Two modes:

**Mode A — Fix citations on an existing page**: Surfaces uncited claims,
runs `wiki cite-suggest`, confirms with you, writes `[[sources/<id>]]` tokens.

**Mode B — Capture-to-cite from any repo (AGT-7)**: Takes a quote + URL from
anywhere in `~/code/*`, ingests the source if not already present, auto-picks
the target wiki page, and adds the citation — one operation via MCP.

Reference conventions: WIKI.md § 6 (citation format), § 9 rule 3 (citation grounding).

## Usage

```
# Mode A — fix citations on an existing page
/wiki-cite wiki/synthesis/glp1-hunger.md
/wiki-cite wiki/concepts/food-noise.md --claim "Food noise is..."

# Mode B — capture from another project
/wiki-cite "Food noise is a persistent mental chatter about food" https://example.com/paper
/wiki-cite "GLP-1 reduces food noise" https://pubmed.ncbi.nlm.nih.gov/12345 wiki/concepts/food-noise.md
```

## Execution — Mode A (fix existing page)

1. **Read the page**: Identify claims without `[[sources/...]]` citation tokens.

2. **Run cite-suggest**:
   ```
   .venv/bin/wiki cite-suggest wiki/<type>/<slug>.md
   ```

3. **Review candidates**: Show top 1-2 candidates per uncited claim. Confirm.

4. **Write citations** (one at a time):
   ```
   .venv/bin/wiki cite-add wiki/<type>/<slug>.md --claim "<claim text>" --source <id>
   ```

5. **Validate**:
   ```
   .venv/bin/wiki finalize wiki/<type>/<slug>.md
   ```

## Execution — Mode B (capture-to-cite)

Single MCP call via `wiki_cite_capture`:

```python
wiki_cite_capture(
    quote="<the claim text>",
    url="<source URL>",
    target_page="wiki/concepts/<slug>.md",  # omit for auto-pick
)
```

Or CLI:
```
.venv/bin/wiki cite-capture "<quote>" <url> [--target wiki/<type>/<slug>.md]
```

What happens:
1. URL looked up in `raw/` — reused if already ingested (idempotent).
2. If not present: `wiki ingest <url> --draft` pulls it in.
3. `wiki/sources/<id>.md` backfilled if filter excluded it.
4. Target page auto-picked by token-overlap if not specified.
5. `wiki cite-add` adds `[[sources/<id>]]` to the matching claim line.

## Key constraints

- Never use Edit to insert `[[sources/...]]` tokens directly — use `wiki cite` or `wiki cite-add`.
- Mode B auto-pick requires ≥1 shared token between quote and page slug/title — if auto-pick fails, specify `--target` explicitly.
- Citation grounding applies to non-draft pages only; drafts defer the rule.
- Source IDs must exist in `raw/<type>/<id>.md` before citing them (Mode B ensures this).
