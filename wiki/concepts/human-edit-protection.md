---
schema_version: 1
type: concept
slug: human-edit-protection
canonical_name: Human-Edit Protection
domains:
- knowledge-systems
created_at: '2026-05-28T20:24:02Z'
last_updated: '2026-05-28T20:24:02Z'
---

# Human-Edit Protection

## Summary

Human-edit protection is a layered mechanism — a soft commit-prefix flag plus a durable in-file marker — that prevents an LLM-driven knowledge base from clobbering hand-written content during automated operations [[sources/web-2026-04-11-879]].

## Key claims

- WikiLoom protects hand-edited pages via two layers: a soft, short-term `human-edit:` commit prefix that causes `lint --fix` and other auto-tools to skip the page, and a durable `<!-- wikiloom:auto -->` marker that creates a hard boundary inside the page [[sources/web-2026-04-11-879]].
- Content above the `<!-- wikiloom:auto -->` marker survives every operation, including `wikiloom ingest <file> --force` — the only command that wipes the auto region [[sources/web-2026-04-11-879]].
- For normal updates (re-ingesting a different source that updates a page), new content is appended to the auto region so user edits anywhere on the page survive without needing the marker [[sources/web-2026-04-11-879]].
- The soft protection from the `human-edit:` commit prefix is cleared by the next auto-action (e.g. a re-ingest), so durable pins must be placed above the marker [[sources/web-2026-04-11-879]].
- `wikiloom save` is the command users run to commit manual edits with the `human-edit:` prefix; it also auto-bumps `frontmatter.modified` and freshens dormant pages back to active [[sources/web-2026-04-11-879]].
- Writer commands block if there are uncommitted edits under `wiki/`, forcing the user to run `wikiloom save` first so manual edits never land inside an automated `ingest:` commit [[sources/web-2026-04-11-879]].
- `wikiloom protect` scans for pages whose human-edit flag has drifted from git history; `--sync` applies git truth back to the manifest and frontmatter [[sources/web-2026-04-11-879]].

## Sources

- [[sources/web-2026-04-11-879]] — WikiLoom GitHub README

## Related

- [[entities/wikiloom]]
- [[concepts/auto-commit-pattern]]
- [[concepts/page-lifecycle]]
