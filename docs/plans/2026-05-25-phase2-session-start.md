# Phase 2 — Session Start Brief

**Date:** 2026-05-25
**For:** Next Claude Code session picking up Phase 2
**Model recommendation:** claude-sonnet-4-6 (same as Phase 1)
**Working directory:** `~/code/knowledge`

Paste this document into a fresh session. Do not re-derive decisions recorded here.

---

## State of the repo at handoff

- **Branch:** `main`
- **Last commit:** `80269e1` — Phase 2 planning doc committed and pushed
- **Tests passing:** 1038
- **Tag:** `m54-phase1-round-c` is the Phase 1 close. No Phase 2 work has started.

Verify before starting:
```sh
git log --oneline -5
.venv/bin/pytest -x -q
```
Expected: 1038 passing, no failures.

---

## What Phase 1 delivered (do not re-implement)

Full record at `docs/phase1-closeout.md`. Summary:

- **M47–M54**: 18/18 Phase 1 items, ~793 → 1038 tests
- **Gateway surfaces**: CLI (`wiki`), MCP (`wiki mcp-serve`), Web UI (`wiki serve`)
- **Key infrastructure now present**: `file_lock`, `OperationResult`, `AnthropicAPIClient` (with token telemetry), `wiki evaluate` (eval framework), `wiki finalize-batch` (draft closer op), `wiki context` (INT-11), `assert_safe_for_prompt` (TOK-7), transcription disk cache (TOK-6), filter system-prompt memoized once per batch (TOK-3), argcomplete wired (TOOL-10)
- **Session-state discipline**: `docs/session-state.md` is load-bearing. Re-read it before any plan-or-write action. PreCompact and SessionStart hooks are active.

---

## Authoritative references (read in this order before touching code)

1. `docs/session-state.md` — open contracts and next atomic step (always read first)
2. `docs/plans/2026-05-25-phase2-plan.md` — **the primary planning document**; full acceptance criteria per item; do not re-derive
3. `docs/reviews/2026-05-23-knowledge-system-review.md` — the authoritative scope baseline; §§ 6–12 have per-finding detail; § 14 has the phased roadmap; § 15 has open decisions
4. `CLAUDE.md` — agent control surface, hard rules, gateway discipline
5. `docs/phase1-closeout.md` — what shipped, patterns to reuse
6. `BUILD.md` § 10 — per-milestone delivery history; tells you which patterns were established when

Do not load `log.md` or `index.md` wholesale into any prompt. Both are unbounded. Use `_tail_log_entries()` for log excerpts.

---

## Decisions already made (do not re-open)

| Decision | Resolution |
|---|---|
| Readwise customer? | Yes — INT-9 (Readwise poller) replaces INT-1 (Gmail), INT-2 (RSS), INT-3 (Podcast + RSS) |
| Docs depth target | "Any senior engineer cold" — ~15h. All DOC items are L-effort. |
| Agent runtime model | Per-agent processes (not a daemon). AGT-9 uses filesystem event bus. |
| Prompt caching API key | Separate Anthropic API key with $50/month cap (decided prior to Phase 1; see memory) |
| Hook format in settings.json | Fixed (`matcher+hooks` wrapper). Already committed. |

---

## Phase 2 round structure

| Round | Milestone | Items | Effort | Gate |
|---|---|---|---|---|
| A | M55 | TOK-4, ONT-2, ONT-4, ONT-8, ARCH-10 | 3M + 2S | Independent — start here |
| B | M56 | AGT-9, AGT-14, ONT-3, QUAL-3 | 3M + 1S | ONT-3 deps ONT-2 (Round A) |
| C | M57 | INT-8, INT-9 | 1M + 1S | Independent |
| D | M58 | AGT-1, AGT-2, ONT-6, TOK-12 | 2M + 1S + 1M | AGT-1/2 dep AGT-9 (Round B) |
| E | M59 | DOC-3, DOC-4, DOC-7, DOC-2 | 4L | DOC-4 deps DOC-3 |

Already done from Phase 2 (do not re-implement): QUAL-12 (M50), QUAL-2+ARCH-11 (M49), INT-11 (M51).

---

## Round A detail — start here (M55)

Five independent items. No shared files. Any execution order within the round.

### TOK-4 — `_gather_existing_pages` two-stage select
- **What:** Stage 1 sends frontmatter + 200-char snippet per page (~3 KB total). Stage 2 fetches full bodies only on agent request. Cap user-prompt existing-pages block at ~10 KB.
- **Find the code:** `grep -rn "_gather_existing_pages" src/` to locate. Likely in `src/gateway/ops/ingest.py` or `src/gateway/authorship/`.
- **Test:** assert stage-1 output for a 30-page fixture is ≤15 KB.
- **Why first:** fires on every `wiki ingest --with-plan`; highest token-cost reduction of the round.

### ONT-2 — CiTO 8-verb typed citations
- **What:** `[[sources/<id>|supports]]` syntax. `_CITO_VERBS` frozenset in `citations.py`. Validator `SEVERITY_WARNING` on unknown verb. WIKI.md § 5.6 added.
- **Verbs:** `supports`, `disputes`, `extends`, `qualifies`, `confirms`, `reviews`, `usesMethodIn`, `citesAsAuthority`
- **Key:** existing `[[sources/<id>]]` (no alias) must be unchanged. This is purely additive.
- **Why:** ONT-3 and QUAL-3 in Round B depend on `disputes` verb being formal.

### ONT-4 — `entity_kind` controlled vocab
- **What:** ~12-kind enum (`person`, `organization`, `paper`, `drug`, `dataset`, `product`, `software`, `statute`, `standard`, `place`, `event`, `other`). Validator rejects non-enum on new pages. Migration script consolidates 24 free-text values.
- **Find current values:** `grep -h "entity_kind:" wiki/entities/*.md | sort | uniq -c | sort -rn | head -30`

### ONT-8 — Slug cap 80 chars
- **What:** Validator `SEVERITY_ERROR` on new slugs >80 chars. Legacy slugs grandfathered with `SEVERITY_WARNING`. `--force-long-slug` override documented in WIKI.md.
- **Note:** review doc lists dep as ONT-1, but ONT-1 is Phase 3. Legacy grandfathering makes this safe to ship now.

### ARCH-10 — Citation allowlist to versioned YAML
- **What:** Move `_STRUCTURAL_FRAME_LABELS` and `_AGGREGATE_FRAMING_OPENERS_RE` from `src/gateway/citations.py` to a `citations_allowlist.yaml`. Load from YAML at import. WIKI.md § 5.2 documents as NLM compat shim.
- **Find the code:** `grep -n "_STRUCTURAL_FRAME_LABELS\|_AGGREGATE_FRAMING_OPENERS" src/gateway/citations.py`
- **Critical:** behavior must be identical on ship. The YAML contains the current phrases verbatim — no pruning.

---

## Milestone protocol (same as Phase 1)

1. Branch: `phase2-round-a` (then b, c, d, e) off main.
2. Each item: failing test → minimal implementation → passes → incremental commit.
3. Commit convention: `feat|fix|perf|docs(<area>): <description>` + `Co-Authored-By: Claude <model> <noreply@anthropic.com>`.
4. After all items: `pytest -x --tb=short`. Expect net positive test delta.
5. Write `docs/milestones/M55.md` (then 56, 57, 58, 59) — follow M52–M54 template.
6. Update `BUILD.md` § 10 with milestone row.
7. Update `WIKI.md` § Gateway operations if new ops added.
8. Tag: `m55-phase2-round-a` (etc.).
9. Merge to main after K2 parity green: `pytest tests/gateway/test_mcp_parity.py`.
10. Update `docs/session-state.md` at every milestone boundary.

---

## Hard rules (no exceptions, ever)

1. No direct writes to `wiki/` or `raw/`. All writes through the gateway.
2. No direct calls to `nlm` or NotebookLM MCP. All NLM ops through `wiki nlm-*`.
3. Every claim in every wiki page must cite `[[sources/<id>]]`. Drafts downgrade to warning.
4. Never load `log.md` or `index.md` wholesale into an LLM prompt. Both are unbounded. Use `_tail_log_entries()` for log; use `wiki context` for wiki content.
5. Message Send Gate: never send any message on any channel without explicit user approval. Draft → present → wait for explicit send → execute.

---

## Open decisions — do not make these yourself

Stop and escalate if you encounter friction on:
- Hard rule #1 enforcement posture (CI grep vs runtime guard) — gates ARCH-14, not in Phase 2
- Source-page stubs fill-vs-demote (ONT-10) — Phase 3
- Wedge vertical for Track B — not Phase 2
- Open-source posture for Track B — not Phase 2

---

## Pattern hooks (reuse these from Phase 1)

- **New gateway op:** see `src/gateway/ops/context_op.py` (M51, INT-11) — `OperationResult`, `_emit_result`, K2 parity test
- **New converter:** see `src/gateway/converters/voice.py` — six-step contract, tests at `tests/gateway/test_transcription.py`
- **New poller:** see `src/gateway/pollers/apple_notes.py` — cursor pattern, content hash, `raw/<type>/` output
- **New lint check:** see `src/gateway/lint/broken_wikilinks.py` (M52, QUAL-4) — `SEVERITY_ERROR/WARNING`, `KNOWN_CHECKS` registration
- **File lock:** `from gateway.locking import file_lock` — context manager, `LOCK_NAMES` prefix convention
- **Token telemetry:** `AnthropicAPIClient` in `src/gateway/llm/api_client.py` — pass-through, logs automatically
- **Validator extension:** `src/gateway/validator.py` — `ValidationResult`, `add_finding()`, `SEVERITY_*` constants

---

## First action in new session

1. `git log --oneline -5` — confirm at `80269e1` or later
2. `.venv/bin/pytest -x -q` — confirm 1038 passing
3. Read `docs/session-state.md` — check open contracts
4. Read `docs/plans/2026-05-25-phase2-plan.md` Round A section for full acceptance criteria
5. Branch: `git checkout -b phase2-round-a`
6. Start with TOK-4 (highest token-reduction ROI; sets the pattern for the round)
