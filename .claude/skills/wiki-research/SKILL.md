---
name: wiki-research
description: Run structured multi-source research on a question and file the result as a wiki synthesis page
triggers: [wiki-research, wiki research]
---

## What This Does

Takes a research question, fans out across search adapters, filters candidates,
and files a synthesis page via the gateway. Uses `wiki research` + `wiki query`.

Reference conventions: WIKI.md § 5 (query workflow), § 7 (synthesis pages).

## Usage

```
/wiki-research "How does GLP-1 affect dopamine reward circuits?"
/wiki-research "What are the risks of AI agents in clinical settings?" --domain edge-ai-agentic
```

## Execution Steps

1. **Check existing coverage**: Run `wiki search "<key terms>"` and scan
   `index.md` for related synthesis pages. If an answer already exists, link
   to it and stop unless the user wants a fresh synthesis.

2. **Scoped research**: Run:
   ```
   .venv/bin/wiki research "<question>" [--domain <slug>] --review
   ```
   This fans out search, filters candidates, and builds a query plan.

3. **Review plan**: The `--review` flag surfaces the proposed source set.
   Confirm or adjust before executing.

4. **Execute**:
   ```
   .venv/bin/wiki research "<question>" --execute <plan-id>
   ```
   Or use the shorthand: `.venv/bin/wiki query "<question>" [--domain <slug>]`

5. **Inspect output**: The gateway writes a draft synthesis page to
   `wiki/synthesis/<slug>.md`. Read it and verify:
   - `synthesizes:` frontmatter lists source IDs
   - `## Sources cited` section has `[[sources/...]]` links
   - Key claims are citation-grounded

6. **Finalize**: If citations are complete, run `wiki finalize` on the page.
   Otherwise leave as draft and note the gap.

## Key constraints

- `wiki query` writes a wiki page — it is a write op. Plan before running (WIKI.md § 9).
- Do not call NotebookLM tools directly. Route through `wiki nlm-*` commands (WIKI.md § 9).
- Synthesis pages require `synthesizes:` frontmatter per ONT-11; validator warns if absent.
