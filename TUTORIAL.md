# Tutorial — using ~/code/knowledge/

How to actually use this knowledge base. Covers the day-1 mental model,
the three ways to add a source, the synthesis loop, cross-project use,
and operational habits. Skim top-to-bottom once; come back for the
cheat sheet at the end.

## 1. The mental model

A personal knowledge base where every authored claim ties to a real
source you ingested. Three load-bearing pieces work together:

- The **wiki** (this repo) is canonical storage — local markdown +
  YAML frontmatter under a single root.
- **NotebookLM** is the heavy-synthesis service for whole-corpus
  questions. The gateway invokes it via `wiki nlm-*`; every artifact
  files back to `wiki/artifacts/` with bidirectional links so nothing
  ends up siloed inside NotebookLM.
- **Obsidian** is the knowledge-graph visualization engine. Open this
  directory as an Obsidian vault and the `[[wikilinks]]` the gateway
  enforces become a navigable graph of sources, concepts, and
  syntheses.

The repo is two layers stacked under a single root:

```
~/code/knowledge/
├── raw/              ← immutable sources (one .md + frontmatter per source)
│                       PDFs / audio kept as binary sidecars
├── wiki/             ← LLM-authored knowledge layer
│   ├── sources/        per-source summary pages, one to one with raw/
│   ├── concepts/       drugs, mechanisms, phenomena, techniques
│   ├── entities/       people, organizations, datasets, papers as entities
│   ├── synthesis/      cross-source analyses (the answer pages)
│   └── mocs/           maps of content per domain (entry points)
├── nlm/              ← NotebookLM bookkeeping (notebook IDs per domain)
└── .knowledge/       ← runtime state — policies, examples, locks, lint reports
```

**One-line rule:** raw sources are append-only; everything in `wiki/` is
authored (or re-authored) through the gateway, which enforces citation
grounding via `[[sources/<id>]]` wikilinks.

**Why it's like this:** filesystem-as-database. Markdown + YAML
frontmatter is canonical, every retrieval primitive (`grep`, file walk,
ripgrep, your editor) just works, no SDK required. The gateway is a thin
discipline layer; the data is the README.

## 2. Day 1 — read what's already there

Open these in order with your editor or `bat`/`less`:

1. **`index.md`** — live content index. The fastest "what's in here" view.
2. **`wiki/mocs/`** — domain entry points (one MOC per topic area).
3. **`wiki/synthesis/`** — answer pages. Pick any one as a worked example
   of the format: claim sentences anchored by `[[sources/<id>]]`
   wikilinks, with frontmatter declaring the domain and any draft state.
4. **`wiki/sources/<canonical-id>.md`** — summary card per source.
   Click any `[[sources/...]]` wikilink in a synthesis to land here.
5. **`raw/<type>/<canonical-id>.md`** — the immutable origin. Wiki
   summaries link here via `[[raw/<type>/<id>]]`.

For the live counts and per-domain breakdown, run `wiki status` and
read `index.md`.

**Navigation shortcuts:**

```sh
rg --type md "VTA" wiki/                  # ripgrep across the wiki layer
ls wiki/synthesis/                        # list every synthesis page
fd -e md . wiki/concepts/glp1*            # find concept pages by pattern
```

## 3. Add a source

Three input shapes. All go through `wiki ingest`; the converter
dispatcher routes by URL pattern or file extension.

### 3a. A web page or paper URL

```sh
wiki ingest https://www.nature.com/articles/s41586-024-07444-7 --domain glp1-reward-modulation
```

Behind the scenes: web converter pulls the article (trafilatura),
filter scores it against the policy, the wiki summary page is created.
For arxiv / pubmed / youtube URLs, a domain-specific converter handles
metadata extraction.

### 3b. A local PDF or voice memo

```sh
# Drop into the watcher inbox; the launchd agent ingests automatically
cp ~/Downloads/paper.pdf ~/code/knowledge/raw/inbox/
cp ~/Documents/Voice\ Memos/idea.m4a ~/code/knowledge/raw/inbox/

# Or invoke directly
wiki ingest ~/Downloads/paper.pdf --domain glp1-reward-modulation
wiki ingest ~/Documents/Voice\ Memos/idea.m4a
```

Voice memos transcribe via mlx-whisper (`large-v3-turbo`, ~5× real-time
on M3 Max) and diarize via pyannote — output is a speaker-labeled
markdown body with timestamp anchors. Audiobooks (`.m4b`) split by
embedded chapters.

The watcher writes the new file to `raw/<type>/<id>.<ext>` and a
canonical markdown to `raw/<type>/<id>.md`. Failed ingests land in
`raw/inbox/_failed/` with an error sidecar.

### 3c. A note you wrote in another tool

If it's already markdown with reasonable frontmatter, just put it in
`raw/inbox/`. Otherwise, voice-memo it.

## 4. Ask a question — the synthesis loop

This is the load-bearing flow. Every answer ends up as a wiki page
grounded in canonical sources.

```sh
wiki query "what is known about GLP-1 modulation of mesolimbic dopamine?" \
  --domain glp1-reward-modulation \
  --draft
```

What happens:
1. Gateway searches `wiki/` (not `raw/`) for keyword-matching pages,
   takes up to 30.
2. Builds a prompt with the question + matched page contents.
3. Calls `claude -p` (single LLM call, ~80 s wall clock).
4. Parses the agent's `Plan` response.
5. `apply_plan()` validates every claim has a `[[sources/<id>]]`
   citation and writes the synthesis page atomically. Without
   `--draft`, claims missing citations cause the write to fail.

Output lands at `wiki/synthesis/<auto-slug>.md` with `draft: true` and
`draft_unresolved_claims: N` recording how many lines need citations
before finalize.

### Finalize a draft

After a follow-up authoring pass adds citations (or removes
unresolvable meta-claims):

```sh
wiki finalize wiki/synthesis/<slug>.md
```

This re-runs the strict validator. If all claims are now cited, the
`draft: true` flag is cleared. Use `--abandon` to delete a stuck draft.

### When to use what

| Need | Command |
|---|---|
| Quick answer based on existing wiki content | `wiki query "..." --domain X` |
| Full corpus answer using NotebookLM | `wiki nlm-briefing <domain>` (see § 6 — large-scale path) |
| One-shot ingest + query in a single turn | `wiki ingest <url> --with-plan --domain X` |
| Slides for a meeting | `wiki nlm-slides <domain> "topic"` |

## 5. Use this KB from another project

The wiki paths are stable. Reference them from any other `~/code/*`
project's CLAUDE.md, README, or notes:

```markdown
The reward-circuit synthesis lives at
`~/code/knowledge/wiki/synthesis/<slug>.md`.
```

For agent access from another Claude Code session, the MCP server is
already registered globally (see `~/.claude/mcp_servers.json`). Tools
appear as `wiki_query`, `wiki_ingest`, `wiki_nlm_*`, etc. in any CC
project. **Restart Claude Code** once after install for them to load.

## 6. NotebookLM workflow (for whole-domain synthesis)

Use NotebookLM when the question spans dozens of sources and a single
in-context call would lose detail. The gateway treats NotebookLM as a
synthesis service:

```sh
wiki nlm-add glp1-reward-modulation pubmed-22128031   # add source to corpus
wiki nlm-briefing glp1-reward-modulation              # full briefing doc
wiki nlm-audio glp1-reward-modulation "reward circuit primer"
wiki nlm-slides glp1-reward-modulation "alcohol use disorder evidence"
```

Every artifact is filed back to `wiki/artifacts/` with bidirectional
links to the sources used. **Discipline gate:** the bare `nlm` CLI is
forbidden in committed wiki content; the pre-commit hook (M9) blocks
commits that contain raw `nlm ` invocations. Always go through
`wiki nlm-*`.

## 7. Operational habits

```sh
wiki status            # watcher heartbeat, inbox queue, recent activity
wiki lint              # all checks; full report at .knowledge/lint/
wiki lint --scope orphans                    # cheap; just the orphan list
wiki finetune --check                         # example-bank state per domain
wiki finetune --domain X --distill --force    # produce a v2 policy candidate
```

**Daily:** `wiki status` to confirm the watcher is alive. The launchd
agent restarts it on crash, but a stale heartbeat (no beat for several
minutes) means investigate.

**Weekly:** `wiki lint`. Look for new orphans, stale drafts older than
7 days, citation-density warnings on synthesis pages. The output is
markdown — stash it in your weekly review notes if you keep them.

**Monthly:** `wiki finetune --check`. Once a domain crosses ~500
high-quality decisions, run `--distill --force` to get a candidate
v2 policy under `.knowledge/policies/<domain>/policy_versions/`.
Review and copy to `policy.yaml` if good — the candidate never
overwrites the live policy.

## 8. The watcher

The launchd agent runs `wiki watch` continuously and ingests anything
dropped in `raw/inbox/`.

```sh
launchctl list | grep knowledge.watcher        # confirm loaded
tail -f ~/code/knowledge/.knowledge/watcher.out.log
scripts/install_watcher.sh --uninstall         # stop + remove
scripts/install_watcher.sh                      # reinstall
```

If the watcher dies and doesn't restart, kill its pid via
`pkill -f "wiki watch"` and rerun the install script.

## 9. Troubleshooting

| Symptom | Diagnosis |
|---|---|
| `wiki ingest` fails with `no converter handles ...` | URL/extension isn't recognized; check `gateway/converters/` |
| `wiki query` returns "no wiki pages matched" | Question doesn't keyword-match any page; use `--domain` to scope or `wiki ingest` first |
| Pre-commit hook blocks commit on `wiki/*.md` | You wrote raw `nlm ` somewhere; replace with `wiki nlm-*` |
| `wiki nlm-*` errors on auth | Run `nlm login` (the upstream NotebookLM CLI's auth, not HF) |
| Voice converter `TranscriptionError: HF_TOKEN` | Diarization needs HF auth; falls back to transcript-only or run `hf auth login` |
| MCP `wiki_*` tools not visible in another CC session | Restart Claude Code after `scripts/install_mcp.sh` |
| Lint reports 215+ source orphans | Expected — legacy migrations don't wikilink sources from MOCs; discharge via `wiki query` synthesis loops |

## 10. Cheat sheet

```sh
# Read
ls wiki/synthesis/                                 # answer pages
rg "<term>" wiki/                                  # grep wiki layer
cat wiki/concepts/<slug>.md

# Write (always through the gateway)
wiki ingest <path-or-url> [--domain X] [--with-plan] [--draft]
wiki query "<question>" --domain X [--draft]
wiki filter <path>                                 # read-only score
wiki filter-correct <source-id>                    # pin a corrected example
wiki finalize <page-path> [--abandon]

# NotebookLM (gateway-mediated)
wiki nlm-add <domain> <source-id>
wiki nlm-briefing <domain>
wiki nlm-audio <domain> "<topic>"
wiki nlm-slides <domain> "<topic>"
wiki nlm-revise <slug> --slide <n> "<instructions>"

# Operate
wiki status
wiki watch                                         # foreground; usually launchd runs this
wiki lint [--scope <check>]
wiki backfill-examples --domain X --legacy-config <yaml> --json <staged.json>
wiki finetune [--check | --domain X --distill [--force]]

# Migrate
wiki batch-ingest <vault> --legacy-import --domain <slug> [--dry-run]
```

## 11. Where to read more

- `CLAUDE.md` — agent control surface (auto-loaded by every CC session here)
- `WIKI.md` — full schema reference for frontmatter, page types, lint rules
- `BUILD.md` § 9 — per-milestone delivery record (every commit linked)
- `MIGRATION.md` — how the legacy research-notebook vaults were converted
- `SESSION_TRANSCRIPT.md` — chronological narrative of the v1 build session
