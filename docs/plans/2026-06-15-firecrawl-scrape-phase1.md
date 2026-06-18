# Plan: Firecrawl Scrape for Web Conversion — Phase 1

**Date:** 2026-06-15
**Status:** Phase 1 landed (flag-gated, default off); live-validated 2026-06-15; uncommitted
**Category:** Ingest / Source Access
**Related:** `docs/backlog/h1a-corpus-access-paywalled-sources.md`, `CLAUDE.md § Research pipeline preconditions`

---

## 1. Context — how Firecrawl is used today

Firecrawl has exactly one touchpoint in the codebase: the research **search**
adapter (`src/gateway/research/adapters/web.py`) POSTs to `/v1/search` with
`{query, limit}` and maps result rows to `CandidateItem`s. That is the entire
integration.

The **scrape** step — turning an accepted URL into the canonical markdown that
lands in `raw/` — does **not** use Firecrawl. The web converter
(`src/gateway/converters/web.py`) fetches with a plain `requests.get` (single
User-Agent, no JavaScript) and extracts with `trafilatura`. This is the brittle
path: it returns 403/429 or an empty shell on JS-rendered, paywalled, or
anti-bot-protected pages.

The cost of this shows up downstream, not at fetch time. `CLAUDE.md` gates
research runs on convert-failure rate and corpus word-count; the H1a backlog
item documents a concrete instance where 20 of 21 sources materialized empty or
paywalled (arxiv 429s, PNAS/biorXiv 403s), NLM cited the one rich source for all
four branches, and eight synthesis pages were abandoned. The backlog's
recommended fix — manually hunt `*.full` HTML URLs to dodge 403s — is exactly
what a rendering, proxy-aware scraper automates.

`README.md:81` describes the `web` type as "Firecrawl + boilerplate strip." This
is inaccurate today (it is trafilatura). Phase 1 makes the description true when
the flag is on.

## 2. Problem statement

The acquisition layer for `type=web` sources is the lowest-fidelity stage in the
pipeline and the dominant cause of sparse corpora. We pay for Firecrawl on the
cheap step (search) and hand-roll the hard step (scrape).

## 3. Goals / Non-goals

**Goals**

- Route web conversion through Firecrawl `/scrape` (JS render, proxy/anti-bot,
  PDF parsing) when explicitly enabled.
- Degrade safely: any Firecrawl miss falls back to the existing
  requests+trafilatura path. The flag can only improve yield, never regress it.
- Preserve the existing security posture (SSRF guard) and frontmatter schema.
- Default off. No behavior change until an operator opts in.

**Non-goals (deferred to later phases — see § 9)**

- Migrating the search adapter to `/v2` or using `scrapeOptions`, `categories`,
  domain filters, or `tbs`.
- `/map`, `/crawl`, batch scrape, structured JSON extraction.
- Making Firecrawl the default scraper. That is a Phase 2 decision contingent on
  live yield and credit-cost data.

## 4. Design

A single seam, `_acquire(source) -> (markdown_body, metadata_dict, source_app)`,
dispatches on three modes. Every branch normalizes metadata to the trafilatura
key shape (`title`, `date`, `author`, `description`) so `convert()` is
path-agnostic, and records `meta.source_app` (`firecrawl` vs `trafilatura`) so
corpus audits can attribute yield and measure each mode's effect.

```
WIKI_WEB_SCRAPER unset (default)  →  trafilatura only
WIKI_WEB_SCRAPER=fallback         →  trafilatura first; escalate to Firecrawl
                                      ONLY on failure (403/429/empty); if
                                      Firecrawl also misses, raise the original
WIKI_WEB_SCRAPER=firecrawl        →  Firecrawl first; trafilatura on a miss
```

**Ordering matters for cost.** Firecrawl scrape is a paid roundtrip per page, so
`fallback` is the cost-smart mode and the intended eventual default: trafilatura
handles the ~majority of pages it can already read for free, and only the hard
pages (the 403/429/JS-shell cases) incur a Firecrawl call. `firecrawl` mode
(scrape-first) is for a batch of known-hard sources where paying per page is
acceptable in exchange for maximum fidelity. The escalation trigger is a
`ConversionError` from the trafilatura branch, which fires on both an HTTP error
(403/429) and an empty extract (a 200-status JS shell) — so it catches the two
dominant sparse-corpus failure modes. (Limitation: a page that returns *partial*
boilerplate trafilatura extracts as non-empty will not escalate; a min-length
threshold is a later refinement, not Phase 1.)

`_fetch_firecrawl` returns `None` (the "fall back" / "miss" signal) on: unset
`FIRECRAWL_API_KEY`, a non-public target (SSRF parity via `_assert_public_url`),
any HTTP/JSON error, or an empty body. Errors are swallowed by design — a
scrape-service outage must degrade ingest, not abort it.

**Scrape request.** `POST /v2/scrape` with `formats: ["markdown"]`,
`onlyMainContent: true`, `parsers: ["pdf"]`, and `proxy` from
`WIKI_FIRECRAWL_PROXY` (default `auto`). Firecrawl's markdown is used directly;
trafilatura is not run over it (running a readability pass over already-clean
markdown is redundant and lossy).

### Flag surface

| Variable | Default | Effect |
|---|---|---|
| `WIKI_WEB_SCRAPER` | unset | `fallback` = trafilatura-first/escalate-on-failure; `firecrawl` = scrape-first; anything else = trafilatura only |
| `WIKI_FIRECRAWL_PROXY` | `auto` | Firecrawl proxy tier (`basic` / `auto` / `stealth`) — cost lever |
| `FIRECRAWL_API_KEY` | unset | Required for either Firecrawl mode to activate (already used by the search adapter) |

## 5. Credit-cost policy

Firecrawl scrape bills per page: ~1 credit basic, +4 for enhanced/stealth proxy,
+4 for JSON mode (not used here). Two levers keep this bounded. First, **mode**:
`fallback` pays only for pages trafilatura cannot read (the cost-smart default),
versus `firecrawl` which pays for every page. Second, **proxy tier**: `proxy:
auto` lets Firecrawl escalate only when needed rather than paying stealth on
every page. PDF parsing is 1 credit/page; `parsers: ["pdf"]` is retained because
PDF sources are common in this corpus and are precisely the ones trafilatura
cannot read. Keep `proxy` operator-tunable so a batch of known-hard domains can
be run at stealth without hardcoding the cost.

## 6. Security

`_assert_public_url` is applied before handing a URL to Firecrawl, preserving the
SSRF posture even though Firecrawl fetches server-side. `WIKI_ALLOW_PRIVATE_FETCH`
continues to override for trusted internal ingest. The redirect-validation logic
on the direct-fetch path is unchanged.

## 7. Acceptance criteria

- [x] Mode unset (default): byte-identical behavior to pre-change; existing
      converter tests pass unmodified.
- [x] `firecrawl` mode + hit: body and metadata come from Firecrawl;
      `source_app == "firecrawl"`; trafilatura fetch is bypassed.
- [x] `firecrawl` mode + miss: falls back to trafilatura; `source_app == "trafilatura"`.
- [x] `fallback` mode + trafilatura success: Firecrawl not called; `source_app == "trafilatura"`.
- [x] `fallback` mode + trafilatura failure: escalates; `source_app == "firecrawl"`.
- [x] `fallback` mode + both fail: raises the original `ConversionError`.
- [x] No key, or internal target: `_fetch_firecrawl` returns `None` (no raise).
- [x] **Live validation (2026-06-15):** biorXiv full-text
      `10.1101/2020.06.26.174482v2.full` (an H1a-backlog 403) — trafilatura
      `ConversionError: HTTP 403`; Firecrawl returned **22,966 words**, title
      parsed, `source_app=firecrawl`. Full body, not an abstract stub.

## 8. Test plan

Unit tests added to `tests/gateway/test_converters.py`: metadata mapping (primary
and og/article fallbacks); `firecrawl`-mode hit and miss; `fallback`-mode
trafilatura-success (no escalation), escalation-on-failure, and both-fail-raises;
flag-off bypass; and no-key short-circuit. The default path is also covered by
the pre-existing suite.

Note: the formal suite requires the project venv (`.venv/bin/python -m pytest
tests/gateway/test_converters.py`); the edited paths were additionally exercised
in isolation during development. Run the formal suite locally before tagging.

**Before live runs:** confirm `FIRECRAWL_API_KEY` status — `BUILD.md:704` notes
the disclosed key was flagged for rotation.

## 9. Follow-on phases (deferred backlog)

Ranked by payoff; each is independent of Phase 1.

1. **[DONE 2026-06-15] Search adapter → `/v2` + `filter_hints`.** Moved off
   `/v1/search`. The previously-dormant `filter_hints` param now maps to
   `categories` (`research`/`github`/`pdf`), `includeDomains`/`excludeDomains`
   (mutually exclusive; include wins), `tbs`, `sources`, and `location`. The v2
   grouped response (`data.{web,news,images}`) is flattened over `web`+`news`
   (`images` dropped — no page URL). Hint-free calls keep the minimal
   `{query, limit}` payload. `src/gateway/research/adapters/web.py`;
   `tests/test_research_adapter_web.py` (11 passed under pytest).
2. **[DONE 2026-06-15] `scrapeOptions` on search.** `filter_hints["scrape_options"]`
   passes through to Firecrawl `scrapeOptions`, returning full content per result
   in the search call. The flat-list response that scrapeOptions produces is
   handled by the same `_extract_results`.

   Note: the orchestrator (`research/orchestrator.py:243`) still calls
   `adapter.search(q, max_results=...)` without `filter_hints` — same as the
   arxiv/semantic_scholar adapters, which already read hints the orchestrator
   does not yet pass. Wiring the orchestrator to derive and pass hints
   (from prompt + domain policy) is the remaining half and is deferred to a
   dedicated change, since it touches every adapter's call path.

3. **Structured extraction (`json` format).** Pull authors, publish date, and
   abstract deterministically into frontmatter. **Deferred, not built:** JSON
   mode adds +4 credits/page and there is no evidence yet that the OpenGraph
   metadata mapping in Phase 1 is insufficient. Build only if a frontmatter-
   fidelity gap is observed in real ingests (validate-then-formalize).
4. **`/map` + `/crawl`.** Whole-site/blog/docs ingestion as a source set;
   complements `wiki batch-ingest`. `/map` is cheap URL discovery. **Deferred:**
   new endpoint surface that needs integration design (where discovered URLs
   enter the ingest/dedup/watcher path) — not safe to build blind.
5. **Batch scrape.** One async job over N vetted URLs vs. sequential fetch+retry.
   **Deferred:** depends on the same ingest-integration design as item 4.
6. **Promote `fallback` to the default mode.** Make trafilatura-first/escalate
   the implicit behavior (no flag needed), contingent on observed credit-cost
   over a real ingest window. Revisit `README.md:81` wording at that point.
