# MCP API Reference

The gateway exposes all operations as MCP tools via `wiki mcp-serve`. Tools are named `wiki_*` and delegate to the same `gateway/ops/*.py` functions as the CLI. All tools return a dict with at least `success: bool` and `summary: str`.

Configure in any Claude Code project's MCP settings (`.mcp.json` or equivalent) so agents in `~/code/*` repos get `wiki_*` tools without shelling out.

**CLI-only operations** (not available as MCP tools): `watch`, `mcp-serve`, `serve`, `migrate`, `demote-domain`, `schedule`, `auth`, `batch-ingest`, `backfill-examples`, `backfill-entity-kinds`, `backfill-timestamps`, `backfill-synthesizes`, `rotate-log`.

---

## Read / orient

### `wiki_status()`
Show recent activity, watcher state, pending queues, and finetune readiness.

### `wiki_lint(scope=None)`
Run health checks. `scope` restricts to one check slug (e.g. `"orphans"`, `"stale-drafts"`). Returns `findings` list and `report_path`.

### `wiki_context(query, depth=1, format="markdown", caller=None, budget=None)`
Fetch a known wiki page + N-hop wikilink-resolved neighbors. `query` is a slug, path, or title substring. `budget` (chars, markdown only): over budget, neighbors are authority-ranked (inbound links + domain overlap) and truncated rather than dropped. Read-only. Use for precise neighborhood expansion around a known page; use `wiki_retrieve` for question-driven retrieval.

### `wiki_agent_log(since="24h")`
Show per-agent event counts and top payloads for the last N hours.

---

## Retrieve (RAG)

The wiki is a relevance-rankable RAG substrate: SQLite FTS5/BM25 over section-level chunks, plus graph-authority ranking (a term's canonical page outranks pages that merely mention it). Derived index at `.index/wiki.db` — self-healing on read, never canonical. **`wiki_retrieve` is the default first call for grounding an answer in the wiki.**

### `wiki_retrieve(query, domain=None, k=12, budget_chars=40000, caller=None)`
The default RAG call. One LLM-free call → a bounded, ranked context block of the most relevant sections, each wrapped in `<page path=… section=…>` with `[[sources/<id>]]` citations preserved. Returns the block plus a source manifest. Prefer over `wiki_search` (snippets, not usable context) and `wiki_query` (heavy NotebookLM synthesis).

### `wiki_answer(question, domain=None, k=12, budget_chars=40000, file_draft=False, caller=None)`
Retrieve → one Claude call grounded only in the retrieved sections; cites only `[[sources/<id>]]` present in context (ungrounded citations stripped). NotebookLM-independent. `file_draft=True` files the answer as a draft synthesis page.

### `wiki_search(query, scope="all", domain=None, page_type=None, limit=20)`
Ranked full-text search (FTS5/BM25) over `wiki/` + `raw/`. Returns hits with `score`, `snippet`, `path`, `title`, `domain`.

### `wiki_related(query, limit=10, caller=None)`
Pages co-citing the same sources as a target page (graph neighbors), ranked by shared-citation count then inbound-link authority. `query` resolves like `wiki_context`. LLM-free.

---

## Ingest

### `wiki_ingest(input, domain=None, with_plan=False, draft=False)`
Ingest a single source. `input` is a URL or path to a canonical markdown file. `with_plan=True` invokes the authorship agent. `draft=True` relaxes citation rules on agent-generated pages.

### `wiki_filter(input, domain=None)`
Score a candidate source without writing. Returns `score`, `rationale`, `policy_version`.

### `wiki_filter_correct(source_id, decision, rationale, domain=None)`
Override a past filter decision and pin as a corrected example. `decision` is `"include"` or `"exclude"`.

### `wiki_poll(name)`
Run a registered poller by name (e.g. `"apple-notes"`, `"rss"`, `"gmail"`). Returns items ingested.

### `wiki_poll_list()`
List registered pollers with their names and source types.

---

## Authorship

### `wiki_query(question, domain=None)`
Search the wiki for `question` and file a synthesis page with the answer. Invokes the authorship agent.

### `wiki_concept_add(slug, body)`
Author a `wiki/concepts/<slug>.md` page from a markdown body.

### `wiki_cite(page_path, source_id, line_number)`
Add a `[[sources/<id>]]` citation token to a specific line of a wiki page.

### `wiki_cite_add(page_path, claim_text, source_id, fuzzy=False)`
Add a citation by claim text (resolves to a line via exact → normalized → optional fuzzy match).

### `wiki_edit(page_path, section_name, new_body)`
Replace the body of one named section in a wiki page. Validator-checked; writes via `write_atomic`.

### `wiki_finalize(page_path, abandon=False)`
Finalize a draft page: re-validate strict, clear draft fields. `abandon=True` deletes the draft.

### `wiki_finalize_batch(domain=None, limit=None, execute=False, suggest=False)`
Batch-finalize stale drafts. Dry-run by default; `execute=True` to apply. `suggest=True` enables LLM cite-suggest for Cat B pages.

---

## Domains

### `wiki_bootstrap_domain(description, slug)`
Author a starter `policy.yaml` from a natural-language domain description.

### `wiki_discover_domains(scope=None, since=None, untagged=False, timeout=None)`
Cluster untagged source pages into draft domain proposals. Single-shot LLM pass.

### `wiki_promote_domain(proposal_slug)`
Bless a draft domain proposal: write `policy.yaml`, back-tag member sources, flip proposal status.

### `wiki_reject_proposal(proposal_slug)`
Delete a draft domain proposal.

### `wiki_skill_emit(domain)`
Generate `.claude/skills/wiki-<domain>/SKILL.md` from policy.yaml + MOC wikilinks + recent synthesis titles.

### `wiki_publish_notion(domain, include_sources=False, include_artifacts=False)`
Mirror wiki domain pages to a Notion database (requires `NOTION_TOKEN`).

---

## Research

### `wiki_research(prompt, domain=None, dry_run=False, execute=None, abandon=None, archive=None)`
Corpus-constructive research: fan out search across adapters, filter candidates, build a NotebookLM session, file syntheses. `dry_run=True` plans without executing. `execute=<session_id>` runs a saved plan. `abandon=<session_id>` / `archive=True` manage plan lifecycle.

---

## NotebookLM

> All NLM tools are opt-in and resource-intensive. Never auto-trigger.

### `wiki_nlm_add(domain, source_id)`
Add a source to the domain's NotebookLM corpus.

### `wiki_nlm_sync(domain, limit=None, dry_run=False)`
Bulk-sync every raw source tagged with `domain` into its NotebookLM corpus.

### `wiki_nlm_slides(domain, topic)`
Generate a slide deck from the domain corpus; file as a wiki artifact.

### `wiki_nlm_audio(domain, topic)`
Generate an audio overview; file as a wiki artifact.

### `wiki_nlm_briefing(domain)`
Generate a briefing doc; file as a wiki artifact.

### `wiki_nlm_revise(artifact_slug, slides)`
Revise individual slides in an existing slide deck.

---

## Evaluation

### `wiki_evaluate(domain=None, goldens_path=None, dry_run=False)`
Run per-domain evaluation against golden Q/A pairs at `.knowledge/eval/<domain>/goldens.yaml`. LLM-as-judge; persists results; tracks delta.

### `wiki_finetune(domain=None, check=False, distill=False, threshold=None, force=False)`
Inspect or distill the per-domain example bank. `check=True` reports counts. `distill=True` runs LLM distillation and writes a candidate policy version; adds `calibration_metrics` block if a calibration set exists.

---

## Agents

### `wiki_triage(action="list")`
Manage the inbox-triage review queue. `action` is `"list"`, `"approve"`, or `"reject"`.

### `wiki_draft_close(action="run")`
Run the draft-closer agent: auto-finalize easy wins, escalate hard cases.

### `wiki_agents(agent_name, action="run")`
Run a named agent (`"inbox-triage"`, `"draft-closer"`, `"agent-digest"`) on demand.

### `wiki_digest(hours=24.0, stale_days=7)`
Daily content brief: new sources, new synthesis, stale drafts, triage queue.

### `wiki_agenda(date=None, lookahead_days=1)`
Calendar-aware meeting prep briefing.

### `wiki_contradiction(action="list", slug=None, resolution=None)`
List or resolve structured contradiction pages.

### `wiki_contradiction_sweep(domain=None, dry_run=False)`
Weekly per-domain LLM contradiction scan; writes draft synthesis pages.

---

## Return shape

All tools return a serialized `OperationResult`:

```json
{
  "success": true,
  "summary": "ingested web-2026-01-15-abc (score 0.92)",
  "paths_touched": ["raw/web/web-2026-01-15-abc.md", "wiki/sources/web-2026-01-15-abc.md"],
  "errors": [],
  "data": {}
}
```

On failure, `success` is `false` and `errors` contains one or more error strings. The tool never raises — inspect `success` before using the result.
