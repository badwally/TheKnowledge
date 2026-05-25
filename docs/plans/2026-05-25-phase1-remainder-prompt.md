# Phase 1 Remainder — Driver Prompt

**Date:** 2026-05-25
**Purpose:** Self-contained briefing to drive the remaining Phase 1 items after M51 closeout. Designed to be pasted into a fresh Claude session (recommended model: `claude-sonnet-4-6`).
**Authoritative scope baseline:** `docs/reviews/2026-05-23-knowledge-system-review.md` § 14 Phase 1 table + § 1 keystones.

---

You are picking up engineering work on the knowledge wiki at `~/code/knowledge`. M51 (INT-11 — `wiki context` read-side op) is the most recent milestone and should be committed before you start. Verify with `git log --oneline -5` and `pytest -x` (expect ~977+ tests passing) before beginning any new work.

## Section 1 — Canonical references (read first, in this order)

1. `CLAUDE.md` — agent control surface, hard rules, operation guide.
2. `WIKI.md` § 3, 4, 5, 11 — schema + citations + validator.
3. `docs/reviews/2026-05-23-knowledge-system-review.md` — THE authoritative scope baseline for this phase. Specifically:
   - § 1 (executive summary + K1–K5)
   - § 5 (ARCH-* findings + acceptance criteria)
   - § 8 (QUAL-* findings)
   - § 10 (TOK-* findings)
   - § 12 (DOC-* findings)
   - § 14 (the phased roadmap — Phase 1 table is your scope)
   - § 15 (open decisions; flagged in Section 4 below)
4. `docs/milestones/M47.md` through `M51.md` — what already shipped, including patterns you must reuse (K2 parity, file_lock, OperationResult, etc.).
5. `docs/plans/2026-05-24-k1-k5-keystones-decisions.md` — for understanding why the codebase looks the way it does. Reference, not required.

Do NOT re-derive any decision recorded in these documents. The doc has done the architectural work; your job is execution.

## Section 2 — Scope baseline (Phase 1 remainder + one M50 follow-up)

**Already shipped (do NOT re-implement; verify if uncertain):**

```
K1 (cite-add + edit --section)        — M48
K2 (MCP-CLI parity sweep)             — M47
K3 (Tailscale + bearer + iOS shim)    — M48
K4 (scheduler substrate)              — M48
K5 (token telemetry)                  — M47
TOK-1 (AnthropicAPIClient)            — M49 phase A (see follow-up below)
ARCH-1 (log lock)                     — M47 side-effect
QUAL-2 / ARCH-11 (draft batch closer) — M49 (pulled from Phase 2)
QUAL-12 (eval framework)              — M50 (pulled from Phase 2)
INT-11 (wiki context)                 — M51 (pulled from Phase 3)
```

**Outstanding Phase 1 items, ordered by execution sequence:**

Round A — correctness fixes (independent, no shared files):

```
ARCH-2  Validator-enforce frontmatter mutation allowlist           [M]
ARCH-4  Research orchestrator per-source lock + filter writeback   [S]
ARCH-6  register_session idempotency (force + lint scope)          [S]
QUAL-4  Validate non-source wikilink targets                       [S]
QUAL-5  Per-domain fine-tune readiness in wiki status              [S]
```

Round B — token efficiency:

```
TOK-1 follow-up  Diagnose cache_read=0 from M50 hand-test          [S]
TOK-3  Memoize filter system-prompt build (once per run)           [S]
TOK-6  Transcription cache (raw/<type>/_transcripts/<sha>.json)    [S]
TOK-7  Codify "don't load log.md/index.md into prompts" guard      [S]
```

Round C — ergonomics + onboarding:

```
TOOL-10  Shell completion + --help examples                        [S]
DOC-1    "New here?" reading order in README                       [S]
DOC-6    GLOSSARY.md                                               [S]
```

**Sequencing rationale:** Round A items touch the validator, locking, and status surfaces — they are invariant-adjacent and benefit most from clean context. Round B is mechanical token plumbing with one diagnostic step (TOK-1 follow-up) that may inform TOK-3 design. Round C is documentation and CLI polish; sequencing it last avoids docs drifting against in-flight code changes.

**Items NOT in this phase (intentional deferrals):**

- All Phase 2 items not already pulled forward (AGT-1 onwards).
- All § 15 open decisions (Section 4 below) — these need andrew, not you.
- Track B Phase 0 — do not touch `kg-core/` extraction.

## Section 3 — Per-item briefs

For each item: planning-doc reference → file targets → acceptance → pattern hooks. Do not invent additional acceptance criteria; the doc is authoritative. Read the full § 5 / § 8 / § 10 / § 12 entry for each item before starting it.

### ARCH-2 — Frontmatter mutation allowlist

- **Reference:** § 5, ARCH-2
- **Files:** `src/gateway/validator.py` + `tests/gateway/test_validator_*.py`
- **Acceptance:** new `validate_source_frontmatter_diff(old, new)` rejects mutations to keys outside the WIKI § 11.5 allowlist (`filter`, `nlm_corpus_ids`, `wiki_pages`, `domains`). Tests prove a `title:` mutation is rejected and an allowlisted mutation passes. Callers in the pipeline are wired to invoke it on every source-frontmatter write.
- **Pattern:** Mirror `validator.py:validate_wiki_page` shape. Acquire `file_lock("wiki-author")` in any caller that mutates.

### ARCH-4 — Research orchestrator per-source lock + filter writeback

- **Reference:** § 5, ARCH-4 (also `M46-followup-items.md` #5)
- **Files:** `src/gateway/research/orchestrator.py` (the `_materialize` path) + `tests/gateway/test_research_orchestrator*.py`
- **Acceptance:** Materializer acquires `file_lock(f"ingest-{source_id}")` around the write. Computed filter score is written back into the source frontmatter (today it leaves an empty `filter:` block). Parallel research-vs-ingest doesn't corrupt files (test with two writers).
- **Pattern:** Existing `file_lock` pattern in `gateway/locking.py`. `LOCK_NAMES` already enumerates `ingest-*` prefix per M47.

### ARCH-6 — register_session idempotency

- **Reference:** § 5, ARCH-6
- **Files:** `src/gateway/nlm_registry.py` + relevant tests
- **Acceptance:** `register_session` accepts `force=True` and handles re-execute on `status=promoted` without crashing. Lint scope `idempotency` enumerates state-file vs on-disk drift. Every op file documents its `Idempotency:` contract field (this is partly done — verify and complete).
- **Current state:** Commit `fb75e46` (2026-05-23 08:03) made partial progress. You inherit it. Diff against the acceptance criteria and finish what's missing rather than starting fresh.

### QUAL-4 — Validate non-source wikilink targets

- **Reference:** § 8, QUAL-4
- **Files:** `src/gateway/validator.py:validate_wikilinks` + lint module
- **Acceptance:** Every `[[<dir>/<slug>]]` resolves. Currently only `sources/` is checked; extend to `entities/`, `concepts/`, `mocs/`, `synthesis/`. Add `[[target|alias]]` as an explicit forward-reference (warning-only). Add lint pass `broken-wikilinks`. The `[[nlm:<uuid>]]` form is documented as intentional and must remain exempt.
- **Pattern:** INT-11/M51 `wiki context` op already implements wikilink walking — `src/gateway/ops/context_op.py:_extract_wikilink_targets`. Read it; reuse the regex if it fits.

### QUAL-5 — Per-domain fine-tune readiness in wiki status

- **Reference:** § 8, QUAL-5
- **Files:** `src/gateway/ops/status.py` + `tests/gateway/test_status_*.py`
- **Acceptance:** `wiki status` shows a "Fine-tune readiness" line per domain showing decision count toward the 500 threshold and percentage (e.g. `glp1-reward-modulation: 268/500 (54%)`). New line in `index.md` § Health summary. Log entry when a domain crosses 80% (one-shot, not re-fired).
- **Pattern:** Status block layout follows the M47 LLM-usage block and M50 evaluation-scores block. Match that aesthetic.

### TOK-1 follow-up — Diagnose `cache_read=0`

- **Reference:** `M50.md` "Hand-test results" + WIKI § 10.4
- **Files:** `src/gateway/llm/api_client.py` + the `cite_suggest` / eval call sites
- **Acceptance:** Identify why `cache_read` tokens are zero despite `cache_control: ephemeral` being sent. Document findings in `docs/M51-tok1-cache-diagnosis.md`. If the issue is a wiring bug, fix it; if it's an Anthropic SDK or billing quirk, document it and re-evaluate the API-key cost case.
- **Pattern:** Read `api_client.py` carefully. Check whether system prompt actually arrives marked, check 5-min TTL window, check whether `cache_creation` tokens appear on the first call of a session (they should). Use `claude -p --output-format json` on a real source corpus, not synthetic input.

### TOK-3 — Memoize filter system-prompt build

- **Reference:** § 10, TOK-3
- **Files:** `src/gateway/research/orchestrator.py:_run_filter` + `src/gateway/filter/semantic.py:filter_score`
- **Acceptance:** `build_system_prompt` called ONCE per filter run (not per candidate). New `filter_score(..., system_prompt=system)` arg; orchestrator passes the prebuilt prompt in. Behavior unchanged in tests; a new test asserts `build` called once for an N-candidate run.
- **Pattern:** Look at `filter/semantic.py` line ~217 and ~324 for the current per-candidate calls.

### TOK-6 — Transcription cache

- **Reference:** § 10, TOK-6
- **Files:** `src/gateway/converters/voice.py` + `audiobook.py` + (new) `src/gateway/transcription.py` shared helper if it doesn't exist
- **Acceptance:** `raw/<type>/_transcripts/<sha256-of-source-bytes>.json` cache. Cache hit returns transcript in <50ms. Pre-cache by hashing the input file BEFORE running Whisper. Document the cache layout in WIKI § 6.
- **Pattern:** Hash the input file with `hashlib.sha256`, key by hex digest. Cache JSON shape: `{"transcript": str, "whisper_version": str, "created_at": iso}`. Bust cache only on Whisper version change.

### TOK-7 — "Don't load log.md/index.md" guard

- **Reference:** § 10, TOK-7
- **Files:** `src/gateway/index.py` + `src/gateway/log.py` + `CLAUDE.md`
- **Acceptance:** One-line guard at the top of `index.py` and `log.py` reading modules (or as a marker constant) that any LLM-prompt assembly code can check. New note in CLAUDE.md § "Hard rules" explaining: `index.md` and `log.md` are human/agent orientation artifacts, NEVER gateway runtime input. Test: grep `gateway/` for `"index.md"` or `"log.md"` reads inside LLM-prompt assembly paths; assert clean.

### TOOL-10 — Shell completion + `--help` examples

- **Reference:** § 7, TOOL-10
- **Files:** `src/gateway/cli.py` + new `docs/shell-completion.md`
- **Acceptance:** `argcomplete` integration documented: `eval "$(register-python-argcomplete wiki)"` in `docs/shell-completion.md`. Each subcommand's `--help` shows at least one usage example. `argcomplete >= 3.0` added to `pyproject.toml`.
- **Pattern:** `argcomplete.autocomplete(parser)` one line before `parser.parse_args()`. `epilog="Example: wiki cite-add ..."` on each ArgumentParser subparser.

### DOC-1 — "New here?" reading order in README

- **Reference:** § 12, DOC-1
- **Files:** `README.md`
- **Acceptance:** Numbered reading list at the top of README, three audiences: (a) engineers wanting to contribute, (b) users doing knowledge work, (c) agents being briefed. Each step names the output ("after this you can..."). New engineer can answer "what is the gateway?" cold in under 30 min using only the listed docs.
- **Pattern:** Don't introduce new docs to satisfy this. Reference existing docs (`CLAUDE.md`, `WIKI.md`, `TUTORIAL.md`, `docs/milestones/*`).

### DOC-6 — GLOSSARY.md

- **Reference:** § 12, DOC-6 + the glossary already at § 2 of the review doc
- **Files:** `GLOSSARY.md` (new, repo root) + `README.md` (cross-link)
- **Acceptance:** ~25–40 terms, alphabetical. Start from the review doc's § 2 list and add anything the M47–M51 docs introduced (`CallResult`, `ScheduleJob`, `AnthropicAPIClient`, evaluate `Judge`/`Golden`, etc.). Each term: one-line definition + link to canonical doc section.
- **Pattern:** No emojis. Prose definitions, not bullet lists per term.

## Section 4 — Decisions that gate work (DO NOT make these yourself)

Read § 15 of the review doc. The following are user decisions, not engineering ones; if you encounter friction on an item below, stop and escalate:

- Hard rule #1 enforcement posture (CI grep vs runtime guard vs git review). Gates ARCH-14, which is NOT in this phase but may surface.
- Source-page stubs fill-vs-demote (ONT-10). Out of phase scope.
- Wedge vertical for Track B. Not your concern.

You may proceed on the items in Section 3 without these decisions.

## Section 5 — Engineering discipline (carry these into every change)

These are non-negotiable. They derive from user preferences and the CLAUDE.md hard rules.

**Workflow**

- Smallest reasonable change per item. Resist scope creep.
- Plan-before-write for any item that touches the validator, gateway choke-point, or citation grammar. A one-sentence plan in chat is enough; no need for a `docs/plans/` file unless the item is M+ effort.
- Confirm before any irreversible operation (frontmatter migration, bulk page rewrite, schema change touching every page).
- Never recap completed work in your responses unless asked.
- Match surrounding code; local consistency trumps external standards.

**Naming**

- Tells the domain story. `Tool` not `AbstractToolInterface`. `execute()` not `executeToolWithValidation()`.
- No temporal markers: nothing is "new," "legacy," "improved," "enhanced," "v2" (except where versioning is the actual semantic, e.g. a `SchemaVersion` field).
- Comments explain intent where non-obvious. No line-by-line narration. Read as evergreen.

**Tests**

- Test-first when behavior is clear (most items in Section 3 qualify).
- Tests cover real logic, not mocked behavior. The K2 parity test is the canonical example — read `tests/gateway/test_mcp_parity.py`.
- Never delete a failing test to make the suite green. If a test is wrong, explain why before rewriting.
- Test output must be clean — no warning spam, no print debugging left in.

**Debugging**

- Root cause, not symptom. Reproduce, compare against a working example (M47–M51 are full of them), form one hypothesis, test minimally, verify. Do not stack fixes.

**Formatting**

- No emojis. No em-dash as a recurrent rhetorical device (use sparingly where other punctuation would not suit). No AI-common structures ("it's not X, it's Y") in code comments or commit messages.

## Section 6 — Gateway discipline reminders (CLAUDE.md hard rules)

- No direct writes to `wiki/` or `raw/`. Use the gateway. Validator + git diff review will catch direct writes.
- No direct calls to `nlm` or NotebookLM MCP. All NLM ops go through `wiki nlm-*`.
- Every claim in every wiki page must be followed by `[[sources/<id>]]`. Drafts (`draft: true`) downgrade this to a warning.
- Lookup before create. Search `index.md` and existing pages before creating a new entity or concept. Validator warns on slug similarity.
- Plan before write for incremental ingests. The gateway logs your plan to `log.md`.

## Section 7 — Per-round milestone protocol

Treat each Round (A, B, C) as a milestone. For each round:

1. Branch: `phase1-round-<a|b|c>` off main.
2. Implement items in any order within the round (they're independent).
3. Each item: failing test → minimal implementation → test passes → incremental commit. Use the M47–M51 commit convention (`feat(<area>): <description>` or `fix(<area>): <description>`).
4. After all items in the round pass: run the full suite (`pytest -x --tb=short`). Expect a net positive test delta.
5. Hand-test at least one acceptance criterion per item against real data (a real source from `raw/`, a real domain from `policies/`). Record results in `docs/milestones/M<N>.md`.
6. Write the milestone doc following the M47–M51 template: What shipped → Modules touched → Test delta → Acceptance checklist → Hand-test results → Follow-ups.
7. Update `WIKI.md` § Gateway operations table if new ops were added.
8. Update `BUILD.md` § 10 with the milestone delivery row.
9. Tag the commit (e.g. `m52-phase1-round-a`).
10. Merge to main only after the K2 parity test stays green.

Three rounds → three milestones (M52 / M53 / M54 if M51 was the prior).

## Section 8 — Verification protocol (final pass before declaring done)

After Round C:

1. Run `pytest -x` — full green, no skipped tests except the documented deferred-hand-test ones.
2. Run `wiki lint` and review all scopes. Expect new lint scopes from QUAL-4 (`broken-wikilinks`) and ARCH-6 (`idempotency`) to be active.
3. Run `wiki status` and verify: fine-tune readiness line present, evaluation block present, LLM usage block present.
4. Run the K2 parity test in isolation: `pytest tests/gateway/test_mcp_parity.py`.
5. `git grep -n "write_text" src/gateway/` and verify every result is either inside the gateway's atomic-write helper or an allowlisted non-`wiki/raw/` path. ARCH-14 is not in scope but the grep is cheap.
6. Open the planning doc § 14 Phase 1 table and confirm 18 of 19 items are now done. The one remaining will be the TOK-1 cache-control resolution if it requires a billing decision rather than a code fix.
7. Diff `docs/session-state.md` predictions against `git diff` and `pytest` output. Any disagreement between what session-state recorded as "open contracts" or "next atomic step" and the actual committed state is a quality incident — investigate before tagging the milestone.

When done, write a closeout summary to `docs/phase1-closeout.md` following the same template as the milestone docs but covering the full Phase 1 arc. Cross-reference each completed item against the planning doc ID.

## Section 9 — Out of scope (do not touch unless explicitly asked)

- Track B (`kg-core/` extraction, Postgres substrate, multi-tenant).
- Phase 2 items not already pulled forward.
- Phase 3 items.
- The § 15 open decisions.
- Any rewrite of M47–M51 deliverables — they shipped, do not regress.

If you find yourself reaching for any of the above, stop and ask.

## Section 10 — Reporting cadence

- After each round: one paragraph summary in chat. Test delta, items done, anything that surprised you.
- Mid-round: only if blocked. Don't narrate progress.
- Final closeout: the doc described in Section 8 step 6, plus a one-paragraph chat summary linking to it.

You have the planning doc, the milestones, and the M47–M51 patterns to draw on. Begin with Round A, ARCH-2 first (it's the largest of the round and shapes the validator surface the others touch).
