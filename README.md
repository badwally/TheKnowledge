# ~/code/knowledge/

Canonical personal knowledge base. Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`) with a hybrid synthesis substrate — the wiki is canonical; NotebookLM is a synthesis service behind a gateway.

## Documentation

| Doc | Purpose |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Agent control surface — auto-loaded by Claude Code sessions in this directory |
| [WIKI.md](WIKI.md) | Conventions reference — the contract every component codes against |
| [MIGRATION.md](MIGRATION.md) | Legacy Obsidian vault migration plan |
| [BUILD.md](BUILD.md) | Gateway build plan and per-milestone delivery record |
| [SESSION_TRANSCRIPT.md](SESSION_TRANSCRIPT.md) | Chronological narrative of the design-and-build session that produced v1 |

## Layout

- `src/gateway/` — gateway implementation (Python package)
- `tests/gateway/` — pytest suite
- `migrations/` — schema and content migration scripts
- `scripts/` — operational scripts (watcher install, MCP install, pre-commit hook)
- `raw/` — immutable sources (markdown + frontmatter, optional binary sidecars)
- `wiki/` — LLM-authored knowledge layer (entities, concepts, sources, synthesis, MOCs, artifacts)
- `nlm/` — NotebookLM bookkeeping
- `index.md` / `log.md` — content index and chronological event log
- `.knowledge/` — runtime state (policies, locks, lint reports, migration audit, poller cursors)

## Install

```sh
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

`wiki` is now on PATH. Optional integrations:

```sh
scripts/install_watcher.sh           # launchd agent: raw/inbox/ → auto-ingest
scripts/install_mcp.sh               # ~/.claude/mcp_servers.json: wiki_* tools in any project
scripts/install_pre_commit_hook.sh   # blocks commits on schema-drift or raw `nlm` calls
```

## CLI

```sh
wiki --help
```

| Command | Status | What it does |
|---|---|---|
| `wiki ingest <input>` | M1/M2/M3/M6/M10 | Ingest URL or canonical markdown path. `--with-plan` runs the wiki authorship agent. `--draft` allows partial citations. PDFs and any non-`.md` local file route to a converter. |
| `wiki filter <input>` | M3 | Read-only filter score (no writes) |
| `wiki filter-correct <id>` | M3 | Override a past filter decision; pin as `user-correction` example |
| `wiki query "<question>"` | M6 | Search wiki, file synthesis page via plan |
| `wiki finalize <page>` | M6 | Promote draft → strict (or `--abandon`) |
| `wiki nlm-add <domain> <id>` | M5 | Add raw source to NotebookLM corpus |
| `wiki nlm-slides <domain> "<topic>"` | M5 | Slide deck → wiki artifact |
| `wiki nlm-audio <domain> "<topic>"` | M5 | Audio overview → wiki artifact |
| `wiki nlm-briefing <domain>` | M5 | Briefing doc → wiki artifact |
| `wiki nlm-revise <slug> --slide …` | M5 | Revise slide deck → new wiki artifact |
| `wiki batch-ingest <vault> --legacy-import --domain <slug>` | M8 | Migrate a research-notebook vault |
| `wiki lint [--scope <check>]` | M9 | Health checks; report under `.knowledge/lint/` |
| `wiki status` | M4 | Watcher state + inbox queue + recent activity |
| `wiki watch` | M4 | Inbox watcher daemon (foreground; used by launchd) |
| `wiki mcp-serve` | M7 | Run the MCP server over stdio |
| `wiki index` / `wiki search` / `wiki migrate` | stubs | Post-v1 work |

## Status

**Feature-complete per BUILD.md.** All 11 originally-planned milestones (M0–M10) shipped. 217/217 tests pass in ~2.4s. 11 commits on `main`.

See [BUILD.md § 5](BUILD.md) for per-milestone delivery records and [SESSION_TRANSCRIPT.md](SESSION_TRANSCRIPT.md) for the design-and-build session log.

### Stubs deferred to follow-up

- Lint checks: `missing-pages`, `stale-claims`, `contradictions`, `filter-calibration` (LLM-driven; framework registered, runners return `[]`)
- Voice / audiobook converters (Whisper is a 2-5GB dep; needs per-env config)
- Real Apple Notes AppleScript poller (framework ships; AppleScript integration is platform-specific)
- CLI: `index --rebuild`, `search`, `migrate <name>` (operational sugar; not load-bearing for the architecture)
- Filter fine-tuning loop (roadmap; trigger threshold ~500–1000 high-quality decisions per domain)
