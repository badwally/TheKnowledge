# Session state — 2026-05-30

Last updated: 2026-05-30 (web-API security hardening shipped — PRs #12 + #14 merged to main; branch cleanup; review docs filed)

---

## Open contracts

None blocking.

**Web-API hardening — DONE this session (PRs #12 `1f49209c`, #14 `b2c1584e` on main).**
Closed all 6 actionable findings from the 2026-05-30 product-readiness review
(`docs/260530_product-readiness-review.md`). Operational consequences now in effect:

- **Auth is default-deny on every `/api/*` route except `/api/health`.** `wiki serve` now
  requires a valid bearer token for ALL endpoints — including reads. The local browser SPA
  must send the token (it no longer works token-less). The iOS Shortcut already sends
  `ios-shortcut-andrew-iphone`, so it is unaffected.
- **New env knobs** (all have safe defaults; set in the `wiki serve` environment to tune):
  - `WIKI_MAX_CONCURRENT_TASKS` (default 4) — concurrent paid jobs before HTTP 503.
  - `WIKI_RATE_LIMIT_PER_MIN` (default 60; 0 disables) — per-token mutating-request rate before 429.
  - `WIKI_LLM_MAX_CALLS_PER_RUN` (default 300; 0 disables) — per-run LLM call ceiling (BudgetExceededError).
  - `WIKI_ALLOW_PRIVATE_FETCH` (unset/off) — set to `1` only to let `wiki ingest` fetch internal/private-IP URLs.
- **Ingest over the API accepts only http(s) URLs or multipart uploads** — local filesystem paths
  are rejected (use the `wiki ingest` CLI for local files).

Deferred (low-severity; each with a revival trigger):
- **Scheduler silent-failure surfacing** — failed cron jobs are recorded in `schedule.yaml` + `log.md`
  but not shown in `wiki status` / `/api/status`. Revive when a scheduled job silently dies unnoticed.
- **CORS policy** — none configured (safe-by-default; browsers block cross-origin). Revive when adding a
  cross-origin browser/extension consumer.
- **LLM circuit breaker** — no shared backpressure across concurrent callers on sustained upstream 429/5xx.
  Revive if a provider outage causes compounding-retry latency/cost during a real run.
- **SSRF DNS-rebinding residual** — host validated at check, re-resolved at connect (redirect-bypass IS
  closed). Revive with a pinned-resolver fetch (resolve once, connect to IP literal + Host header) if the
  service is exposed beyond the trusted tailnet.

Carry-forward (gateway build — unchanged):
- **schema-drift**: ~208 remaining (legacy editorial tail — human judgment).
- **finalize-batch escalated**: ~460 researcher entity pages with no auto-appliable citations; needs source ingestion.
- **orphans / discharge-orphans**: resume condo-capital-infra, glp1-reward-modulation, ai-native-business.
- **edge-ai notebook quota**: ~15 YouTube sources (`yt-rugGoieVQ2Y`, `yt-tVvKlx-oVqc`, `yt-0Wwn5IEqFcg`, …)
  return persistent `RESOURCE_EXHAUSTED` (code 8) — likely per-source NLM restriction. Filter from
  `_orphan_sources_for_domain` or ingest via a different path. Do NOT run edge-ai discharge until diagnosed.
- `wiki migrate` stub remains.

Carry-forward (orita-cmo — unchanged):
- **R3** (`2026-05-28-orita-gcp-r3`): query plan ready. Retry: `.venv/bin/wiki research --execute 2026-05-28-orita-gcp-r3`
- **R2** (ICP validation): blocked on user exporting HubSpot closed-won/closed-lost CSVs (12-month window).
- **nlm login bug**: Chrome must be quit (Cmd-Q) before `nlm login`. Verify with `nlm login --check`.

Carry-forward (iOS Shortcut — K3/M48 — unchanged):
- **Tailscale**: Mac (`andrew-grants-m2-max.tail477197.ts.net`, `100.109.141.64`) and iPhone connected.
- **wiki serve**: restart with `wiki serve --bind 0.0.0.0` after reboots (now auth-gated — see above).
- **Bearer token**: `ios-shortcut-andrew-iphone` in `.knowledge/auth.yaml`.
- **Next step**: Safari → Share → Wiki Capture → confirm task_id notification → export to `scripts/wiki-capture.shortcut` → commit.

---

## Files mid-edit

None. Working tree on clean `main`; only untracked items are gateway-managed `nlm/`/`wiki/`/`raw/` content
(synthesis drafts, source maps, clippings) deliberately left alone (wiki/raw writes go through the gateway).

---

## Decisions made this session

- **Multi-agent product-readiness review** (6 dimensions, adversarial verification, refute-by-default):
  9 findings, 0 false positives; 2 candidates downgraded during verification. Report: `docs/260530_product-readiness-review.md`.
- **Auth scope = default-deny ALL `/api`** (not mutating-only). User's call — correct posture for a
  service consuming private research; cost is the SPA needing a token.
- **Auth via app-level middleware**, not per-router dependencies — default-deny holds by construction;
  a forgotten router can't open a write surface.
- **Ingest SSRF guard validates every redirect hop** — switched `_fetch` off `trafilatura.fetch_url`
  (opaque auto-redirect) to a redirect-disabled `requests` loop. Caught mid-PR by the background security
  reviewer (redirect-bypass); folded the fix into the same commit before merge.
- **#4 ceiling counts calls, not USD** — Max-OAuth path's real exposure is quota, not metered dollars.
  Per-run budget via ContextVar; orchestrator filter pool propagates via per-task `copy_context()`.
- **Stacked-PR footgun**: PR #13 merged into its base branch (#12) instead of main (merged before retarget).
  Re-landed its content as PR #14 onto main. Lesson: retarget a stacked PR to main BEFORE merging it.
- **Branch cleanup**: 35 local branches → `main` only. Deleted 31 merged + 3 verified-stale
  (`fix/research-bounded-synthesis-slugs` proven strictly behind main via tip-to-tip diff; reflog SHA `180f70df`).

---

## Commits this session (all on main)

- PR #12 `1f49209c` — Harden web API: default-deny auth, local-path-ingest rejection, concurrency cap +
  per-token rate limit, SSRF guard (incl. redirect hops). 1935 tests.
- PR #14 `b2c1584e` — Sanitize task error responses (log full detail operator-only); per-run LLM call budget. 1945 tests.
- `83874968` docs — product-readiness review (260530) + session review (260529).

---

## Next atomic step

Security/productization stream is complete and on main. Resume the knowledge-build stream:

1. **Resume discharge-orphans** (after notebook quota resets):
   - `wiki routine discharge-orphans --domain condo-capital-infra --limit 20`
   - `wiki routine discharge-orphans --domain glp1-reward-modulation --limit 20`
   - `wiki routine discharge-orphans --domain ai-native-business --limit 20`
   - **Do NOT run edge-ai** until the persistent RESOURCE_EXHAUSTED sources are diagnosed/filtered.
2. **R3 retry**: `.venv/bin/wiki research --execute 2026-05-28-orita-gcp-r3`
3. **iOS Shortcut completion**: Safari → Share → Wiki Capture (token already valid under new auth gate).
