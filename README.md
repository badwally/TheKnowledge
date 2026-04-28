# ~/code/knowledge/

Canonical personal knowledge base. Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`) with a hybrid synthesis substrate — the wiki is canonical; NotebookLM is a synthesis service behind a gateway.

## Documentation

| Doc | Purpose |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Agent control surface — auto-loaded by Claude Code sessions in this directory |
| [WIKI.md](WIKI.md) | Conventions reference — the contract every component codes against |
| [MIGRATION.md](MIGRATION.md) | Legacy Obsidian vault migration plan |
| [BUILD.md](BUILD.md) | Gateway build plan with milestones M0–M10 |

## Layout

- `src/gateway/` — gateway implementation (Python package)
- `tests/gateway/` — pytest suite
- `migrations/` — schema and content migration scripts
- `scripts/` — operational scripts (watcher install, etc.)
- `raw/` — immutable sources (markdown + frontmatter, optional binary sidecars)
- `wiki/` — LLM-authored knowledge layer (entities, concepts, sources, synthesis, MOCs, artifacts)
- `nlm/` — NotebookLM bookkeeping
- `index.md` / `log.md` — content index and chronological event log
- `.knowledge/` — runtime state (policies, locks, lint reports, migration audit)

## CLI

After `pip install -e .`:

```sh
wiki --help
```

Available subcommands documented in [WIKI.md § 9](WIKI.md). Most are stubs at M0; capabilities land progressively per BUILD.md.

## Status

M0 (repo bootstrap) complete. M1 (gateway spine) is the next milestone.
