# Phase 2 Rounds C + D — M57 + M58 Session Start

Date: 2026-05-25
Branch sequence: phase2-round-c (M57) → merge → phase2-round-d (M58) → merge
Model: claude-sonnet-4-6
Working directory: ~/code/knowledge

---

## Verify before starting

```
git log --oneline -3          # expect f92e747 at tip (or newer)
.venv/bin/pytest -x -q        # expect 1117 passing
git checkout -b phase2-round-c
```

---

## What Rounds A + B delivered (do not re-implement)

- TOK-4: _gather_existing_pages two-stage select (200-char snippets, 10 KB cap)
- ONT-2: _CITO_VERBS frozenset + validate_citation_verbs(); [[sources/<id>|disputes]] syntax is formal
- ONT-4: ENTITY_KIND_ENUM (12-value frozenset); entity page hard-reject on unknown kind
- ONT-8: _MAX_SLUG_LEN = 80; force_long_slug param; lint/long_slugs.py registered as long-slugs
- ARCH-10: src/gateway/data/citations_allowlist.yaml (v1); citations.py loads at import time
- AGT-9: src/gateway/events.py — emit/subscribe/list_events; .knowledge/events/<date>/<seq:04d>.json; events_dir()/agents_dir() in paths; "agent" prefix in LOCK_NAME_PREFIXES
- ONT-3: "contradiction" PAGE_SCHEMAS entry; CONTRADICTION_SEVERITY_ENUM + CONTRADICTION_STATUS_ENUM in validator; validate_contradiction_frontmatter(); lint/contradiction_pages.py registered as "contradiction-pages"; migration 0003
- AGT-14: ops/agent_log.py — aggregate(since_hours)/build_digest_page(); DIGEST_SCHEDULE_ENTRY; CLI wiki agent-log; MCP wiki_agent_log
- QUAL-3: ops/contradiction.py — list_contradictions()/resolve_contradiction(); wiki contradiction list/resolve CLI + MCP; wiki status includes contradiction summary; contested: true on sources with ≥2 open contradictions

---

## Round C items (M57) — Integration pollers

Two independent items. Execute in any order. INT-8 is smaller; ship it first.

### Dependency graph

INT-8 (no deps) — standalone
INT-9 (no deps) — standalone

---

## Item 1: INT-8 — Code-repo metadata poller (S)

**Purpose:** 20+ sibling projects at ~/code/*/. Each has CLAUDE.md and README.md
containing structured project state. Makes `wiki query "what's the architecture
of chief-of-staff"` work without manual ingestion.

**New files:**
- src/gateway/pollers/repo_metadata.py — new RepoMetadataPoller
- src/gateway/pollers/__init__.py — register in _REGISTRY (mirror apple_notes pattern)

**Pattern reference:**
```
# Poller base contract
grep -n "class Poller\|def run\|cursor_path\|read_cursor\|write_cursor" src/gateway/pollers/base.py

# Apple Notes poller — mirror this shape exactly
wc -l src/gateway/pollers/apple_notes.py   # ~233 lines, full reference
head -30 src/gateway/pollers/apple_notes.py

# Registry
cat src/gateway/pollers/__init__.py
```

**Behavior:**
- Polls ~/code/*/README.md, ~/code/*/CLAUDE.md, ~/code/*/docs/*.md
- Excludes: node_modules/, .venv/, __pycache__/, .git/, vendor/, dist/, build/
- Cursor: per-file content hash at .knowledge/pollers/repo-metadata/cursor.yaml
  Only re-ingests files whose content hash changed since last run.
- Auto-domain-tag: project slug from directory name (e.g. ~/code/chief-of-staff/ →
  domain tag "chief-of-staff") if a .knowledge/policies/<slug>.yaml exists, else untagged.
- Output: raw/note/note-repo-<project>-<filename>-<hash8>.md
- Frontmatter meta.source_app: "repo-metadata"
- name = "repo-metadata" (class attribute, used by registry key)

**Acceptance (all must be tested):**
- New file detected and written to raw/note/ with correct frontmatter
- Unchanged file skipped on second run (cursor hash matches)
- Changed file re-ingested on second run (content hash differs)
- Excluded paths (node_modules, .venv) never ingested
- Missing ~/code/ dir → clean PollerResult with 0 ingested, no crash
- meta.source_app == "repo-metadata" on every output page
- Registered in _REGISTRY under "repo-metadata"
- `wiki poll repo-metadata` runs without error (integration smoke: may use tmp_path fixture for isolated ~/code/ equivalent)

---

## Item 2: INT-9 — Readwise poller (M)

**Purpose:** Readwise v3 Export API provides highlights from Kindle, Pocket,
Instapaper, Twitter saves, and web articles in one endpoint. Replaces the
deferred INT-1 (Gmail), INT-2 (RSS), INT-3 (Podcast + RSS chain).

**New files:**
- src/gateway/pollers/readwise.py — new ReadwisePoller
- src/gateway/pollers/__init__.py — register in _REGISTRY

**API shape:**
- GET https://readwise.io/api/v3/list/
- Header: Authorization: Token <READWISE_TOKEN>
- Cursor param: updatedAfter=<iso8601> (ISO 8601 string)
- Response shape (relevant fields per document object):
  ```json
  {
    "id": "<str>",
    "title": "<str>",
    "author": "<str>",
    "category": "books | articles | tweets | podcasts",
    "source_url": "<url or null>",
    "updated": "<iso8601>",
    "highlights": [
      {"text": "<str>", "note": "<str or null>", "highlighted_at": "<iso8601>"}
    ]
  }
  ```
- Pagination: response has `next` URL field; follow until null.
- Auth: READWISE_TOKEN env var — fail fast with clear error if absent.

**Cursor:** .knowledge/pollers/readwise/cursor.yaml
```yaml
last_updated_after: "2020-01-01T00:00:00Z"   # initial value for first run
```
After successful run: set to max(document["updated"]) across the batch.

**Output format:** One raw/note/ file per Readwise document (not per highlight).
File key: note-readwise-<readwise_id>.md (stable, idempotent across re-runs).
Re-run on same document: update the ## Highlights section in place
(content-hash check on the highlights block — same as apple_notes update logic).

**Frontmatter:**
```yaml
type: note
id: note-readwise-<readwise_id>
source_type: note
title: <document title>
authors: [<author>]
url: <source_url or "">
published_at: <highlighted_at of first highlight, or "">
ingested_at: <now>
content_hash: sha256:<hash of body>
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  source_app: readwise
  readwise_id: "<str>"
  readwise_category: books | articles | tweets | podcasts
  source_url: "<url or null>"
  highlighted_at: "<iso8601 of most recent highlight>"
```

**Body structure:**
```markdown
<document title>

Author: <author>

Category: <readwise_category>

## Highlights

- <highlight text> _(note: <note if present>)_
- <highlight text>
...
```

**Acceptance (all must be tested — use a mock HTTP client, do not hit real API):**
- New document written to raw/note/ with correct frontmatter and ## Highlights section
- Re-run with same document: highlights block updated, not duplicated (idempotent)
- Cursor advances to max(updated) after successful batch
- Missing READWISE_TOKEN → PollerResult with success=False, clear error message
- Pagination: follows `next` URL until null
- meta.source_app == "readwise" on every output page
- Empty response (no documents): clean PollerResult, cursor unchanged
- Registered in _REGISTRY under "readwise"

**Pattern:** Mirror src/gateway/pollers/apple_notes.py. Use `requests` (already a dep —
confirm with: grep requests pyproject.toml).

---

## Milestone protocol for M57

1. Branch: phase2-round-c (already created above)
2. TDD: failing test → minimal implementation → passing
3. Commits: feat|fix|perf|docs(<area>): <description> + Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
4. After both items: pytest -x --tb=short — expect net +15 or more tests above 1117
5. K2 gate: pytest tests/gateway/test_mcp_parity.py — must pass before merge
   NOTE: pollers do NOT need MCP tools (poll is CLI-only by design — check CLI_ONLY set).
   Confirm: grep "poll" src/gateway/mcp_server.py
6. Milestone doc: docs/milestones/M57.md — follow M56.md template
7. BUILD.md § 10: add M57 row
8. Tag: m57-phase2-round-c
9. Merge to main
10. Update docs/session-state.md
11. THEN: git checkout -b phase2-round-d and start Round D

---

## Round D items (M58) — Agents + ontology + resilience

Four items. Two dependency chains:
- AGT-9 [done] → AGT-1 → (contributes to 3-agent exit criterion)
- AGT-9 [done] → AGT-2 → (contributes to 3-agent exit criterion)
- ONT-6 (no deps)
- TOK-12 (no deps)

Recommended execution order: ONT-6 → TOK-12 → AGT-1 → AGT-2
(ONT-6 is smallest; TOK-12 is self-contained; agents last because they
integrate multiple subsystems and benefit from ONT-6 fields being in place)

---

## Item 3: ONT-6 — Enforce documented frontmatter fields (S)

**Purpose:** created_at and last_updated are documented as required in WIKI.md
but never validated. 0/769 entities have last_updated; 17/769 have created_at.
Closes the gap between documentation and enforcement.

**Files:**
- src/gateway/validator.py — add required fields + validate_timestamps()
- src/gateway/ops/ingest.py — stamp created_at/last_updated at write time
  (grep -n "front\[" src/gateway/ops/ingest.py | head -20 to find write point)
- src/gateway/ops/finalize.py — stamp last_updated on finalize
- migrations/0004-backfill-timestamps.py — backfill from git log

**Validator additions:**
- Add "created_at" and "last_updated" to required_fields for entity, concept, synthesis PAGE_SCHEMAS
- Add "sources_count" to required_fields for synthesis PAGE_SCHEMAS only
- New validate_timestamps(front) — checks ISO-8601 parseable for created_at and last_updated
  Wire into validate_wiki_page for pages with these fields

**Write-path stamping (ingest op):**
- On first write (new page): set front["created_at"] = now_iso(), front["last_updated"] = now_iso()
- On update (re-ingest): set front["last_updated"] = now_iso(); preserve created_at

**Migration 0004:**
- For each wiki/entities/*.md, wiki/concepts/*.md, wiki/synthesis/*.md:
  - If created_at missing: use git log --follow --diff-filter=A -- <path> to get first-commit date
  - If git log returns nothing: fall back to today
  - Set last_updated = today (or git log date of most recent commit)
  - Dry-run default; --commit to apply
- Idempotent: skip pages that already have both fields

**Known-but-optional fields for sources:** add "contested" to validator known-but-optional
source frontmatter fields (QUAL-3 resolution workflow sets this — add it so validator
doesn't warn on source pages that have been contested).

**Pattern reference:**
```
grep -n "validate_wiki_page_frontmatter\|required_fields\|entity\|concept\|synthesis" src/gateway/validator.py | head -30
grep -n "PAGE_SCHEMAS\|required_fields" src/gateway/wiki_pages.py
```

**Acceptance (all tested):**
- New entity/concept/synthesis page without created_at → SEVERITY_ERROR
- New synthesis page without sources_count → SEVERITY_ERROR
- created_at with invalid date format → SEVERITY_ERROR
- Write path stamps created_at + last_updated on new pages (test via ingest op fixture)
- Re-ingest updates last_updated, preserves created_at
- Migration script is idempotent (run twice → same result)
- Migration no-op when page already has both fields
- `contested` no longer causes an unknown-field warning on source pages

---

## Item 4: TOK-12 — Salvage-on-partial-failure for research runs (M)

**Purpose:** Per-branch NLM synthesis answers live only in memory during
`wiki research --execute`. A crash at the apply_plan step burns all NLM work.
Re-running re-queries NLM unnecessarily.

**Files:**
- src/gateway/research/analysis.py — write per-finding JSON after each branch
- src/gateway/research/orchestrator.py — restore findings from disk on --execute

**Persistence location:** nlm/findings/<session-id>/<branch-slug>.json
- branch-slug: slugify(branch_name) — lowercase, hyphens, alphanumeric only
- Each file is one branch's findings dict, JSON-serialized

**Pattern reference:**
```
# analyze() function — this is where to write findings
grep -n "def analyze\|findings\[name\]\|_investigate_branch" src/gateway/research/analysis.py | head -20

# orchestrator — find where apply_plan is called and where --execute is handled
grep -n "apply_plan\|execute_session\|findings\|analyze" src/gateway/research/orchestrator.py | head -30

# nlm_dir() for path construction
grep -n "def nlm_dir\|findings" src/gateway/paths.py
```

**analyze() changes:**
- After each `findings[name] = _investigate_branch(...)` call, write to
  nlm/findings/<session_id>/<branch-slug>.json immediately
- Errors: if branch raised, still write {"branch": name, "error": str(e)} to disk
  (lets --execute distinguish "not run yet" from "failed")

**orchestrator --execute changes:**
- Before calling analyze(), check nlm/findings/<session_id>/ for existing files
- If ALL branches have findings files AND all are < 24h old → skip NLM phase entirely,
  load findings from disk, proceed to apply_plan
- If SOME branches present and < 24h old → skip those branches, re-query only missing
- If ANY findings are ≥ 24h old → re-query all (NLM session likely expired)
- 24h staleness threshold: constant FINDINGS_STALE_HOURS = 24

**Acceptance (all tested — mock NLM client):**
- After analyze(), nlm/findings/<session>/<branch>.json exists for each branch
- --execute with all fresh findings → analyze() NOT called (NLM skipped)
- --execute with partial findings → only missing branches re-queried
- --execute with stale findings (>24h) → all branches re-queried
- Failed branch (error) written to disk and does not block --execute recovery
- branch-slug collision-safe (different branch names → different slugs)

---

## Item 5: AGT-1 — Inbox-triage agent (M)

**Deps:** AGT-9 (done — events.py is in place)

**Purpose:** Triggered by ingest.complete and poll.complete events. Dispatches
newly ingested sources to domains; routes review-band sources to a triage queue.

**New files:**
- src/gateway/agents/inbox_triage.py — agent logic
- src/gateway/agents/__init__.py — package init (may need to create)
- .knowledge/agents/inbox-triage.yaml — subscription config (written by tests/fixture)
- src/gateway/cli.py — `wiki triage list` subcommand

**Subscription config (.knowledge/agents/inbox-triage.yaml):**
```yaml
agent: inbox-triage
subscribes_to: [ingest.complete, poll.complete]
debounce_s: 0
max_concurrent_runs: 1
```

**Triage queue location:** .knowledge/triage/<source_id>.yaml

**Agent logic (run_triage(source_id) → TriageResult):**
1. Read source frontmatter from raw/<type>/<source_id>.md
2. If domains already set (non-empty list): run filter.score(source_id, domain)
   and persist score to source frontmatter (same as `wiki filter` op)
3. If domain absent/empty: attempt domain inference
   - Load available policies from .knowledge/policies/*.yaml
   - Score title + tags against each policy description (lightweight: keyword overlap,
     NOT an LLM call — keep this cheap)
   - If confidence ≥ 0.6 for exactly one domain: tag source with that domain, run filter
   - If confidence < 0.6 or ambiguous (≥2 domains above 0.4): tag source with "needs-domain"
4. If filter score is in review band (0.3 ≤ score ≤ 0.7): write to triage queue
5. NEVER calls wiki filter-correct autonomously

**`wiki triage list` output:** source_id, title, score, inferred_domain (from triage queue files)

**wiki status integration:** add triage queue depth to status output.

**Pattern reference:**
```
# Filter score function
grep -n "def score\|FilterResult\|score.*float" src/gateway/filter/semantic.py | head -10

# How filter op uses score
grep -n "def run_filter\|score\|domain" src/gateway/ops/filter.py | head -20

# Policy loading
grep -n "def load_policy\|policies_dir\|policy" src/gateway/ops/filter.py | head -10

# Events subscribe pattern (already implemented)
grep -n "def subscribe\|subscribes_to\|since_cursor" src/gateway/events.py | head -10
```

**Acceptance (all tested):**
- Event triggers agent run (subscribe returns matching event → run_triage called)
- Domain-present path: filter score written to source frontmatter
- Domain-absent, confident inference: domain tag applied + filter score written
- Domain-absent, ambiguous: "needs-domain" tag applied, no filter call
- Review-band source (0.3 ≤ score ≤ 0.7): written to .knowledge/triage/<id>.yaml
- No autonomous filter-correct call under any path
- wiki triage list shows review-band sources
- wiki status shows triage depth
- NEVER filters when domain is "needs-domain" without explicit human domain assignment

---

## Item 6: AGT-2 — Draft-closer agent (S)

**Deps:** AGT-9 (done)

**Purpose:** Reads stale drafts; auto-finalizes only easy wins (1:1 claim-to-source,
enumerated synthesizes:). Escalates hard cases with pre-computed invocations.

**New files:**
- src/gateway/agents/draft_closer.py — agent logic
- Scheduler entry in .knowledge/schedule.yaml (written by tests or a setup fixture)

**Easy win definition (both conditions must hold):**
1. Every framing claim sentence in the body has exactly one candidate source in
   `synthesizes:` frontmatter field (1:1 claim-to-source attribution possible)
2. No claim sentence references more than one `[[sources/<id>]]` pattern

**Agent logic (run_draft_closer() → DraftCloserResult):**
1. Run lint stale_drafts check → list of stale draft page paths
2. For each draft:
   a. Check easy-win criteria (read body + synthesizes: frontmatter)
   b. If easy win: call finalize(page_path) through gateway
   c. If hard case: write escalation entry to log.md with pre-computed
      `wiki cite <page_path> --claim "<claim text>"` invocations
3. Write per-domain summary to log.md: pages_finalized, pages_escalated, pages_skipped

**Scheduler entry (daily, NOT event-triggered):**
```yaml
name: draft-closer
cron: "0 8 * * *"   # 8am UTC daily
command: "wiki agent-log --since 24h"   # placeholder; actual CLI TBD
enabled: true
cooldown_seconds: 600
```
Note: The actual CLI invocation for the draft-closer will be `wiki draft-close run`
(or similar) — design the CLI interface before implementing.

**Pattern reference:**
```
# Stale drafts lint check
grep -n "def run\|draft.*true\|stale" src/gateway/lint/stale_drafts.py | head -20

# Finalize op
grep -n "def finalize\|draft.*true\|synthesizes" src/gateway/ops/finalize.py | head -20

# Log append pattern
grep -n "def append\|log.append" src/gateway/log.py | head -10
```

**Acceptance (all tested):**
- Easy-win page (1:1 attribution): finalize() called, page no longer draft
- Hard-case page (multi-source claim): escalation entry written to log.md with
  pre-computed wiki cite invocation; page stays draft
- No autonomous filter-correct call
- Per-domain summary written to log.md after run
- NEVER finalizes when synthesizes: lists >1 candidate for a claim
- Scheduler entry exists (check .knowledge/schedule.yaml or a registered constant)

---

## Milestone protocol for M58

Same as M57. After all 4 items:
1. pytest -x --tb=short — expect net +25 or more tests above M57 baseline
2. K2 gate: pytest tests/gateway/test_mcp_parity.py
   - AGT-1 needs wiki_triage MCP tool (triage list)
   - AGT-2: wiki_draft_close if CLI op is added; or mark CLI_ONLY
   - ONT-6: no new CLI ops → no parity change
   - TOK-12: no new CLI ops → no parity change
3. Milestone doc: docs/milestones/M58.md
4. BUILD.md § 10: add M58 row
5. Tag: m58-phase2-round-d
6. Merge to main
7. Update docs/session-state.md

---

## Key code locations (grep these before writing new code)

```bash
# Poller base + registry
grep -n "class Poller\|PollerResult\|cursor_path\|read_cursor\|write_cursor" src/gateway/pollers/base.py
cat src/gateway/pollers/__init__.py

# requests dep (needed for Readwise)
grep "requests" pyproject.toml

# validate_wiki_page — where to wire ONT-6 timestamp check
grep -n "def validate_wiki_page\b" src/gateway/validator.py

# PAGE_SCHEMAS required_fields — to add created_at/last_updated/sources_count
grep -n "entity\|concept\|synthesis" src/gateway/wiki_pages.py | head -20

# Ingest write path — where to stamp timestamps
grep -n "front\[.created_at\|front\[.last_updated\|wiki_author\|file_lock" src/gateway/ops/ingest.py | head -20

# Filter score + policy loading
grep -n "def score\|def load_policy\|policies_dir\|FilterResult" src/gateway/filter/semantic.py src/gateway/ops/filter.py 2>/dev/null | head -20

# Research analysis — where to write per-branch findings
grep -n "def analyze\|findings\[name\]" src/gateway/research/analysis.py | head -10

# nlm_dir path for findings persistence
grep -n "nlm_dir\|findings" src/gateway/paths.py

# Events bus (AGT-9 — already in place)
grep -n "def emit\|def subscribe\|def list_events" src/gateway/events.py

# Status op pattern (for triage count addition)
grep -n "def _contradiction\|def _finetune\|lines.append" src/gateway/ops/status.py | head -20

# CLI subcommand pattern (for wiki triage list)
grep -n "add_parser.*triage\|SUBCOMMANDS\|IMPLEMENTED" src/gateway/cli.py | head -10
```

---

## Hard rules (no exceptions)

1. No direct writes to wiki/ or raw/. All writes through the gateway.
2. No direct calls to nlm or NotebookLM MCP.
3. Every claim in every wiki page must cite [[sources/<id>]]. Contradiction pages exempt.
4. Never load log.md or index.md wholesale into an LLM prompt.
5. Message Send Gate: AGT-2 digest writes to log.md only — never auto-sends to any channel.
6. AGT-1 NEVER calls filter-correct autonomously.

---

## Open decisions — escalate, do not decide

- AGT-2 daily CLI invocation name: decide before implementing (suggest `wiki draft-close run`)
- AGT-1 domain inference: keyword-overlap is the specified approach (NOT an LLM call).
  If that proves too weak during implementation, escalate — do not silently upgrade to LLM.
- TOK-12 stale threshold: FINDINGS_STALE_HOURS = 24 is specified; do not adjust without asking.
