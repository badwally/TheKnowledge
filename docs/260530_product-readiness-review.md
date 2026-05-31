# Product-Readiness Code Review — knowledge gateway

**Date:** 2026-05-30
**Scope:** Service/product-readiness of `~/code/knowledge` following last week's scope expansion (standalone product + integrated knowledge-graph service across surfaces: web API on Tailscale, iOS shortcut, MCP).
**Method:** 6-dimension multi-agent review (auth/network, API contract, untrusted input, concurrency/state, hard-rule integrity, operational robustness). Every finding adversarially verified against the real code, refute-by-default.
**Result:** 9 findings raised, **9 confirmed, 0 false positives**. 2 candidates were *downgraded* during verification (the networked surfaces turned out to be walled off where the reviewer feared they weren't). Severity: **1 critical · 2 high · 3 medium · 3 low.**

---

## 1. Verdict

**Not ready to expose as a multi-consumer service yet — but the gap is narrow and concentrated, not architectural.** The single blocker is **authentication: 19 of 20 mutating HTTP endpoints have no auth at all**, on a server that the documented Tailscale/iOS deployment binds to `0.0.0.0`. The auth primitive already exists (`verify_bearer`, constant-time, working) and is correctly applied to exactly one route (`/api/ingest`). It simply was never applied to the other ten routers. This is a one-afternoon fix that converts the system from "open write/spend surface on the tailnet" to "default-deny service."

The good news the verification surfaced: the MCP surface and the web route set were *deliberately* designed against the scariest escalation (arbitrary-shell-via-scheduler is `CLI_ONLY` with an explicit comment; the web layer is a fixed six-endpoint typed allowlist, not a generic op dispatcher). The architecture's instincts are sound. What's missing is the perimeter that the network-layer trust (Tailscale) was implicitly standing in for.

**The recurring theme: the CLI enforces invariants that the new service surfaces don't, and network-layer trust (Tailscale) is being used as a substitute for application-layer auth.** That substitution is the thing to retire before any external consumer touches this.

---

## 2. Critical & High findings

### 🔴 CRITICAL — Auth is missing on nearly every mutating endpoint
`src/gateway/web/app.py:37-47`

`create_app()` registers eleven routers via plain `include_router(...)` with no app-level dependency and no middleware. Only `cloud.py`'s `POST /api/ingest` carries `Depends(verify_bearer)` — `verify_bearer` is referenced exactly once in the entire route tree. The other **19 mutating endpoints are fully open**: `/api/ops/{ingest,query,bootstrap-domain,discover-domains,finalize,filter-correct}`, the entire `/api/research/*` lifecycle, all `/api/nlm/*` generation ops, `/api/domains/{slug}/{promote,demote,reject}`, and `/api/inbox/retry`. On the documented `--bind 0.0.0.0` path, any host reachable on the port can write to the wiki, trigger paid LLM/NotebookLM jobs, and read all sources — bypassing Hard Rule #1 at the network edge.

**Fix:** Apply auth globally, default-deny. `include_router(..., dependencies=[Depends(verify_bearer)])` on every mutating router (or an app-level dependency with a read-only/`/health` allowlist). Add a test asserting every `POST/PUT/DELETE` returns 401 without a token. *This single fix also closes the auth half of findings #2, #3, and #5.*

### 🟠 HIGH — Unauthenticated expensive endpoints = uncapped cost + thread-exhaustion DoS
`src/gateway/web/routes/nlm.py:69-152` (and `research.py` execute/create)

The NLM generation endpoints and research-execute kick off billed Claude+NotebookLM work via `store.run_in_thread`, return 202, and require no auth. `TaskStore.run_in_thread` (`web/tasks.py:82-98`) spawns a raw daemon `threading.Thread` per call with **no concurrency cap**, and there is **no HTTP rate limiting anywhere** (the only throttles are outbound adapter backoff). A single reachable client can drain the $50 research cap / Max-OAuth budget / NLM quota, or spawn unbounded threads.

**Fix:** Auth (above) + per-token rate limit on expensive POSTs (token-bucket keyed on the `verify_bearer` token name) + a `Semaphore`/bounded pool cap on concurrent `TaskStore` workers.

### 🟠 HIGH — Unauthenticated ingest reads arbitrary local files
`src/gateway/web/routes/ops.py:66-90`

`_resolve_input` treats any non-`http(s)` input as a local path: `Path(raw).expanduser().resolve()`, handed straight to `ingest()` which `read_text()`s it into a wiki page. An unauthenticated caller can pass `/etc/passwd`, `~/.ssh/id_rsa`, etc., and exfiltrate it via the `wiki/sources` read endpoints. `cloud.py` has byte-identical logic, so even an authenticated token holder can do this via the JSON `url` field (its multipart branch is already safe; the JSON-url branch is the gap).

**Fix:** On network-facing ingest, reject local-path inputs entirely — accept only `http(s)` URLs or sandboxed multipart uploads. If local paths are ever needed, confine to an allow-listed dir and reject resolved paths that escape it. Apply to both `ops.py` and `cloud.py`.

---

## 3. Medium / Low findings

**Operational robustness (medium):**
- **No in-process cost/call ceiling on any LLM call site** — `llm/client.py:120-182`. `budget` flags are wall-clock only; `costs.py` *estimates* for reporting but never gates. Enforcement lives entirely in the external Anthropic console. *Verifier nuance:* the main path is Max-OAuth (flat-rate), so the dominant runaway risk is **quota/rate-limit exhaustion (availability)**, not metered dollars — a call-count budget is arguably more load-bearing than a USD ceiling. Fix: accumulate `CallResult.total_cost_usd` (already captured) per session, abort on a configurable ceiling, let the API 402/429 before spend.
- **LLM subprocess stderr surfaced verbatim to API consumers** — `web/tasks.py:79-80`. `mark_failed` stores `f"{type(e).__name__}: {e}"`; `LLMError` embeds the raw `claude -p` stderr tail (auth-state hints, file paths, model/account IDs), returned verbatim by `GET /api/tasks/{id}`. Not credential disclosure (token/key never echoed; 300-char cap), but internal-diagnostic leak to remote consumers. Fix: sanitize at the boundary, keep full message operator-only in `log.md`, return an opaque correlation id.
- **Scheduled jobs fail silently** — `scheduler.py:217-238`. Failures write `last_exit_code` + stderr tail to `schedule.yaml` and one `log.md` line, but `wiki status` and `/api/status` don't surface scheduler health, and the cooldown guard suppresses re-runs. An unattended pipeline can die and go unnoticed until the wiki silently goes stale. Fix: track consecutive-failure counts, surface a "scheduler" health block in `wiki status` + `/api/status`, escalate after N consecutive failures.

**Lower priority (low):**
- **No CORS policy** — `web/app.py:29-62`. Safe-by-default today (browsers default-deny); flagged because the safe state is implicit/undocumented and the predictable next step (`allow_origins=['*']`) combined with the missing auth would be dangerous. *Downgraded medium→low during verification* — no present-day defect. Fix: decide explicitly and document; never `'*'` with credentials.
- **Scheduler runs `shell=True` on `schedule.yaml` commands** — `scheduler.py:157-169`. Real arbitrary-execution-on-tick *for anyone who can write that file* — but verification confirmed the new surfaces are walled off: `schedule` is `CLI_ONLY` (`mcp_server.py:64`, with an explicit "would let an agent grant itself persistent execution" comment) and the web layer is a typed six-endpoint allowlist with no schedule route. *Downgraded medium→low* — only reachable writer is the local CLI operator who already has a shell. Residual: git-tracked `schedule.yaml`, and zero command validation invites a future regression. Fix: allowlist `wiki <subcommand>` argv without `shell=True`; document `schedule.yaml` as privileged operator-owned config.
- **No cross-call circuit breaker on LLM retries** — `llm/api_client.py:135-177`. Each call is bounded (3 retries, ~35s, 120s timeout); the gap is aggregate — under a sustained upstream 429/529, every concurrent caller independently burns its full retry budget with no shared backpressure. Latency/cost amplifier under a rare condition. Fix: process-level circuit breaker tripping on consecutive 5xx/429. Lower priority than the spend ceiling.

---

## 4. Cross-cutting themes

1. **Network trust is standing in for app auth.** Tailscale bounds *who can reach* the port; it does nothing about *what they can do* once reached. Every high/critical finding traces to this substitution. The fix is to make the application default-deny and treat the tailnet as defense-in-depth, not the control.
2. **The CLI enforces invariants the service surfaces don't.** Hard Rule #1 (gateway-as-sole-write-path), the auth gate, input sanitization — all assumed/enforced at the CLI and operator boundary, several not carried into the HTTP layer. The service is a thinner trust boundary than the CLI it wraps.
3. **No metering anywhere it counts.** No spend ceiling, no call-count cap, no request rate limit, no concurrent-worker cap. Fine for one local operator; an open invitation for a multi-consumer service. Each is small in isolation; together they're the difference between a capped tool and an uncapped liability.
4. **Failure detail leaks outward, failure *signal* doesn't surface.** Raw stderr flows to API consumers (too much outward), while scheduled-job death stays invisible to operators (too little surfaced). Both are the same root cause: error handling tuned for a single human at a terminal, not an unattended service with remote consumers.

---

## 5. Prioritized next actions

1. **Apply `verify_bearer` to all mutating routers, default-deny** (`app.py`). Single highest-leverage fix — closes the critical and the auth half of three more findings. Add the "every write route 401s without a token" test.
2. **Reject local-path inputs on network-facing ingest** (`ops.py` + `cloud.py` JSON-url branch) — accept only `http(s)` / sandboxed uploads.
3. **Cap concurrency + add per-token rate limiting** on expensive POSTs; bound the `TaskStore` worker pool.
4. **Add an in-process budget ceiling** — per-session call-count *and* cost, abortable, surfaced to the API so it can 402/429 before spend. Prioritize the call-count cap (Max-OAuth quota is the real exposure).
5. **Sanitize error responses** at the service boundary; opaque correlation id out, full stderr to `log.md` only.
6. **Surface scheduler health** in `wiki status` + `/api/status`; escalate on N consecutive failures.
7. **Hygiene:** document the CORS decision; allowlist scheduler commands without `shell=True`; add an LLM circuit breaker. (Defense-in-depth, post-launch.)

---

*Generated by a 6-dimension adversarially-verified multi-agent review. 9/9 findings confirmed against real code; 2 downgraded during verification when the networked surfaces proved already protected. (The original synthesizer write was interrupted by a `/login`; this report was assembled from the completed, verified finding set.)*
