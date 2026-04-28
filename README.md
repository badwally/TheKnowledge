# ~/code/knowledge/

Canonical personal knowledge base. Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`) with a hybrid synthesis substrate — the wiki is canonical; NotebookLM is a synthesis service behind a gateway.

**Start here:** [TUTORIAL.md](TUTORIAL.md) — the day-1 workflow guide.

## Documentation

| Doc | Purpose |
|---|---|
| [TUTORIAL.md](TUTORIAL.md) | How to actually use the KB — read, ingest, query, finalize, MCP from other projects |
| [CLAUDE.md](CLAUDE.md) | Agent control surface — auto-loaded by Claude Code sessions in this directory |
| [WIKI.md](WIKI.md) | Conventions reference — the contract every component codes against |
| [MIGRATION.md](MIGRATION.md) | Legacy Obsidian vault migration plan (executed M11–M14) |
| [BUILD.md](BUILD.md) | Gateway build plan and per-milestone delivery record (M0–M25) |
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
- `.knowledge/` — runtime state (policies, examples, locks, lint reports, migration audit, poller cursors, watcher state)

## Install

```sh
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

For voice / audiobook converters and speaker diarization (M3 Max recommended; ~3 GB of model weights):

```sh
pip install -e ".[whisper]"
hf auth login                 # paste a Hugging Face token (Read scope)
# Accept terms once at https://huggingface.co/pyannote/speaker-diarization-3.1
```

`wiki` is now on PATH. Optional operational integrations:

```sh
scripts/install_watcher.sh           # launchd agent: raw/inbox/ → auto-ingest
scripts/install_mcp.sh               # ~/.claude/mcp_servers.json: wiki_* tools in any project
scripts/install_pre_commit_hook.sh   # blocks commits on schema-drift or raw `nlm` calls
```

## CLI

```sh
wiki --help
```

| Command | What it does |
|---|---|
| `wiki ingest <input> [--domain X] [--with-plan] [--draft]` | Ingest URL or local file. PDFs / audio / m4b route to type-specific converters. `--with-plan` runs the wiki authorship agent in the same call. `--draft` allows partial citations. |
| `wiki filter <input>` | Read-only filter score against the domain policy (no writes) |
| `wiki filter-correct <id>` | Override a past filter decision; pin as a `user-correction` example |
| `wiki query "<question>" [--domain X] [--draft]` | Search the wiki and file a synthesis page grounded in `[[sources/...]]` citations |
| `wiki finalize <page> [--abandon]` | Promote a draft page to strict (or delete it) |
| `wiki nlm-add <domain> <source-id>` | Add a raw source to the domain's NotebookLM corpus |
| `wiki nlm-briefing <domain>` | Generate a briefing doc → file as `wiki/artifacts/...` |
| `wiki nlm-audio <domain> "<topic>"` | Audio overview → `wiki/artifacts/` |
| `wiki nlm-slides <domain> "<topic>"` | Slide deck → `wiki/artifacts/` |
| `wiki nlm-revise <slug> --slide N "<instructions>"` | Revise an existing artifact |
| `wiki batch-ingest <vault> --legacy-import --domain <slug>` | Migrate a research-notebook Obsidian vault |
| `wiki backfill-examples --domain X --legacy-config <yaml> --json <staged.json>` | Populate the policy + example bank from legacy artifacts |
| `wiki finetune [--check \| --domain X --distill [--force]]` | Inspect example-bank readiness or distill a v2 policy candidate |
| `wiki lint [--scope <check>]` | Run health checks; report at `.knowledge/lint/<timestamp>.md` |
| `wiki status` | Watcher heartbeat, inbox queue, recent activity |
| `wiki watch` | Inbox watcher daemon (foreground; launchd usually runs this) |
| `wiki mcp-serve` | Start the MCP server (stdio) — exposes every gateway op as `wiki_*` tools |

`wiki index` / `wiki search` / `wiki migrate` remain stubs (operational sugar).

## Content state

| Domain | Sources | Wiki concepts | MOCs | Synthesis pages |
|---|---:|---:|---:|---:|
| ai-temporal-video | 86 | 46 | 5 | 3 + 4 query-driven |
| glp1-reward-modulation | 127 | 28 | 5 | 3 + 5 query-driven |
| edge-ai-agentic | 150 | 75 | 8 | 4 + 4 query-driven |
| **Total** | **363** | **149** | **18** | **18 (10 legacy + 8 query-driven\*)** |

\*M23–M25 ran 13 query-driven syntheses across the three domains, citing **148 of 363 sources (41%)**. Source-orphan lint findings dropped 363 → 215.

See [BUILD.md § 9](BUILD.md) for per-milestone delivery records.

## Status

**Feature-complete + content-active.** 28 commits on `main`, 294 tests pass in ~2.7s.

| Layer | State |
|---|---|
| Gateway v1 (M0–M10) | Shipped |
| Real legacy migrations (M11–M14) | Shipped — three vaults, 363 sources |
| Wikilink canonicalization + migration idempotency (M12) | Shipped |
| Lint check stubs (M15–M18: missing-pages, filter-calibration, contradictions, stale-claims) | Shipped |
| Filter fine-tuning loop (M19 backfill + M20 distill) | Shipped — GLP-1 v2 candidate generated |
| Voice / audiobook converters with mlx-whisper + diarization (M21–M22) | Shipped — Apple Silicon Metal-native |
| Synthesis-driven citation-graph build-out (M23–M25) | Shipped — 41% source coverage across all three domains |
| Optional integrations (watcher, MCP, pre-commit hook) | Active |

### Deferred items (not load-bearing)

- `wiki index --rebuild`, `wiki search`, `wiki migrate <name>` — operational sugar
- Apple Notes AppleScript poller (framework ships; platform-specific adapter pending)
- Open-weight classifier fine-tune (the second WIKI § 10.4 option) — useful only when a domain crosses ~1000 high-quality decisions
- Slug-rename op for query-driven synthesis pages with auto-derived slugs
- Second-pass synthesis queries to push per-domain citation coverage past 70%
