# ~/code/knowledge/

A personal knowledge base where every answer ties to a real source you ingested — not training data, not a hallucination. Sources land as markdown in a local vault; queries return cited synthesis pages; NotebookLM artifacts file back to the same vault with bidirectional links; Obsidian renders the whole citation graph visually.

Implements the LLM Wiki pattern (Karpathy gist `442a6bf555914893e9891c11519de94f`) with a hybrid synthesis substrate — the wiki is canonical, NotebookLM is the heavy-synthesis service behind the gateway, and Obsidian is the knowledge-graph visualization engine on top of the vault.

## What you do

- Drop a PDF, voice memo, audiobook, or URL into an inbox, or run `wiki ingest`.
- Ask the corpus a question with `wiki query "<question>"` — semantic retrieval across mixed media, an agent writes a synthesis with every claim wikilinked to a source.
- For whole-corpus work, route through NotebookLM via `wiki nlm-briefing` / `nlm-audio` / `nlm-slides` — artifacts file back as wiki pages, not silos.
- Open the vault in Obsidian to navigate the citation graph visually; cite stable wiki paths from any other project, editor, or agent.

## How it works with tools you already use

- **Obsidian** is the knowledge-graph visualization engine. Open the vault and the wikilinks become a navigable graph of sources, concepts, and syntheses.
- **NotebookLM** is the heavy-synthesis service behind the gateway, not a replacement. Every artifact files back to the vault.
- **Voice memos and audiobooks** transcribe locally (mlx-whisper + speaker diarization on Apple Silicon).
- **MCP** exposes every gateway operation as `wiki_*` tools to any other Claude Code project.

## What's different

Citations are mechanically enforced — the validator rejects any claim missing `[[sources/<id>]]`, so authored content can't drift into hallucination. Auditable claims, portable storage, one source of truth across your stack.

**Start here:** [TUTORIAL.md](TUTORIAL.md) — the day-1 workflow guide.

## Documentation

| Doc | Purpose |
|---|---|
| [TUTORIAL.md](TUTORIAL.md) | How to actually use the KB — read, ingest, query, finalize, MCP from other projects |
| [CLAUDE.md](CLAUDE.md) | Agent control surface — auto-loaded by Claude Code sessions in this directory |
| [WIKI.md](WIKI.md) | Conventions reference — the contract every component codes against |
| [MIGRATION.md](MIGRATION.md) | Legacy Obsidian vault migration plan (executed M11–M14) |
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
| `wiki discover-domains [--scope GLOB] [--since DATE] [--untagged]` | Cluster untagged sources into domain proposals |
| `wiki promote-domain <proposal-slug>` | Bless a proposal — writes policy, back-tags member sources |
| `wiki demote-domain <domain-slug>` | Reverse a promotion — removes tags, deletes auto-generated policy |
| `wiki reject-proposal <proposal-slug>` | Delete a draft proposal |
| `wiki research "<prompt>" [--domain X] [--review] [--execute ID]` | Multi-adapter search with per-adapter query expansion; `--review` pauses for plan editing |
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

## Status

**v1 + operational integrations shipped.** See [BUILD.md § 9](BUILD.md) for the per-milestone delivery record (commits, tests, hand-tests). For live content state, run `wiki status` and read `index.md`.

### Deferred items (not load-bearing)

- `wiki index --rebuild`, `wiki search`, `wiki migrate <name>` — operational sugar
- Apple Notes AppleScript poller (framework ships; platform-specific adapter pending)
- Open-weight classifier fine-tune (the second WIKI § 10.4 option) — useful only when a domain crosses ~1000 high-quality decisions
- Slug-rename op for query-driven synthesis pages with auto-derived slugs

## License

MIT — see [LICENSE](LICENSE).
