# Daily Review — 2026-06-15

A three-repo day. The bulk was `~/code/knowledge` (an orita-cmo domain build earlier, a Firecrawl infrastructure fix + domain finalization later); plus lighter work in `Condo` (test coverage + a docs accuracy fix) and a greenfield `local-inference` stack stood up from scratch.

---

## Where I worked

- **`~/code/knowledge` — gateway infrastructure.** The web converter's Firecrawl fallback path and the launchd daemons that drive background ingest.
- **`~/code/knowledge` — `orita-cmo` domain.** Competitive-intelligence corpus, a canonical map-of-content, and the company entity page.
- **`~/code/Condo` — test + docs.** Integration coverage for the d1.2 A1 pattern-gap-rejection branch; a registry building-count correction.
- **`~/code/local-inference` — new project.** A local MLX two-model inference stack on Apple Silicon, scaffolded with docs.
- **`~/code/claude-config` — skill engineering.** Built and shipped the `daily-review` skill itself.
- **Housekeeping.** Session-state checkpoints, two session-review docs, a `data-collectives` brief rename.

Four tracks: an infra fix, a research-domain build, a greenfield setup, and tooling on the workflow itself — not the single-repo day a glance at `knowledge` would suggest.

## Why

- **Firecrawl was dead in background ingest.** The launchd watcher/scheduler start from a minimal environment and never saw `FIRECRAWL_API_KEY` / `WIKI_WEB_SCRAPER`, so every auto-ingested biorXiv/PNAS URL silently 403'd to a trafilatura stub. This blocks the Phase-1 firecrawl-scrape plan, which assumed background ingest could reach Firecrawl.
- **`orita-cmo` had no canonical entry point.** The domain had ~25 competitor entities and several syntheses but nothing that let you understand it in one read — and the company page was still a draft.
- **Condo's A1 fallback branch lacked coverage, and a doc quoted an unmeasured figure.** The pattern-gap-rejection path needed an integration test, and the README's registry building count was an estimate rather than a measured number.
- **No local inference path existed.** `local-inference` was stood up to serve two Qwen models locally on Apple Silicon with a documented setup.

## What we accomplished

**Firecrawl infra (shipped, `origin/main`):**
- `secrets_env.py` loader — reads gitignored `.knowledge/secrets.env` at `cli.main()`, `setdefault` semantics so a shell var always wins. PR #16 → `a71d59bb`.
- Empty-value guard follow-up (`4cf76a13`): `KEY=` no longer writes an empty string that would suppress the trafilatura fallback. +2 tests.
- Suite-wide `os.environ` isolation fixture in `conftest.py` (root-cause fix for the global side effect). **1942 tests green.**
- WIKI.md §14.1a documents the mechanism; watcher reloaded onto the new code.

**orita-cmo domain (shipped, `origin/main`):**
- Phase 0 competitive-set discovery (`3ef47911`) + Phase 1 direct-competitor pages (`72e38682`) + single-CMO/AI-agents operating-model synthesis (`22ae4562`).
- Canonical **MOC** hub `wiki/mocs/orita-cmo.md` (`8f94e49a`) — upstream-only position + the own-execution-vs-Klaviyo-partnership fork, fully link-resolved.
- `orita.md` finalized (`feb19e46`) — passed the citation gate, off the stale-draft list.

**Condo (committed, local):**
- Integration coverage for the d1.2 A1 pattern-gap-rejection branch (`0167911`).
- README registry building count corrected to a **measured 2,756** (was ~2,671 estimate) (`a20be31`).

**local-inference (committed, new repo):**
- MLX inference setup — Qwen3.6-35B + Qwen3.5-122B on Apple Silicon, with a `thinking_proxy.py` (`6abc795`); README, project `CLAUDE.md`, and session-state opt-in scaffolding.

**claude-config (committed + pushed, `origin/master`):**
- Shipped the **`daily-review` skill** through the full skillify cycle — qualify → RED → write → GREEN → deploy (`3a0226c`). GREEN out-performed a hand-written review by catching repos a single-repo glance missed.

**Housekeeping:** session-state checkpoint (`64dc4e53`), session reviews (`1a3e02c1`, `260615_session-review-firecrawl-moc.md`), `data-collectives` brief rename (`e3a701cc`), the cross-project daily-review doc itself (`f468f17f`).

## Lessons

- **Cut branches from `origin/main`, not local `main`.** Branching off a local main that was 6 commits ahead swept the orita arc into the Firecrawl PR's squash — ~12–15 wasted tool calls and a reconciliation round. One `git rev-list --count origin/main..HEAD` before `checkout -b` prevents it. (This repo's local routinely runs ahead of origin.)
- **Before any fix that adds a global side effect, ask "who else triggers this path?"** Loading a real file in `main()` leaked env into every `main()`-calling test; the constraint was knowable up front but discovered after the suite failed.
- **Seed schema constraints before authoring, not after.** Checking the MOC's `required_sections` + `citation_grounded` first made it validate on the first try — the inverse of the test-pollution miss, same day.
- **Empty env values are a footgun.** An empty `FIRECRAWL_API_KEY` *wins* over no-key under set-if-absent and silently breaks fallback chains.
- **Run the daily review last — it misses its own tail.** This doc was written mid-evening, then went stale twice as the day's own closing moves (the skill commit, the doc commit) landed after it. Building the review tooling is itself reviewable work.

## Priorities

1. **Keep the Firecrawl loader global (decided).** Parity (works in watcher and by hand) beats blast-radius worry; `fallback` mode only spends after trafilatura already 403'd. Revisit only when a non-Firecrawl secret joins `secrets.env`.
2. **orita-cmo is corpus-complete but strategy-thin.** The descriptive landscape is done; prescriptive positioning ("how Orita *should* position") needs Orita's own strategy material — not a retrieval task.
3. **Two competitor lists remain unreachable** — CB Insights (paid account) and F6S (hCaptcha), the richest curated sources.

## Next actions

- **Reconcile the local working-tree backlog** (~199 gateway-owned files, the `log.md` appends, the deleted narrative doc) — trigger: next time you intend to push domain content, stage by content-match, never `git add -u`.
- **Broaden the Firecrawl Phase-1 rollout** per `docs/plans/2026-06-15-firecrawl-scrape-phase1.md` — trigger: now unblocked, when you want known-hard sources (biorXiv/PNAS) ingested in batch.
- **Add Orita strategy material to the corpus** — trigger: when you want the prescriptive-positioning synthesis; until then it stays deferred.
- **Scope a per-key secret** — trigger: the moment a second, more-sensitive secret lands in `secrets.env`.
- **Verify `local-inference` end-to-end** — trigger: the first real local-model call; it's scaffolded but the two-model serving path is unproven.
- **Commit any remaining Condo untracked artifacts** — trigger: next Condo session.

---
*Code-quality, token, and prompt-engineering analysis is out of scope here — see `docs/260615_session-review-firecrawl-moc.md` (session-review).*
