# M46+ — Outstanding follow-up items

**Created:** 2026-05-13 at end of M44 / M44.1 / M44.2 / M44.3 / M45 / M45.1 series.
**Suspended on:** Claude Max 7d usage at 87%; resume window opens approximately 2026-05-16 when the 7d limit resets.
**Purpose:** Picked-up reference for the next working session. Items are ordered by my read of severity / friction at session end; reorder as you triage. Item #1 from the original close-out (`wiki cite` + `wiki finalize` for the 5 M44.3 backfilled drafts) was completed before suspension and is omitted here.

---

## #2 — Orchestrator renders unresolved NLM citations as `[[sources/<num>]]` instead of `[[nlm:<id>]]`

**Severity:** Real bug (medium). Surfaces in `wiki lint --scope citation-chains` as `dangling-synthesizes-ref` for every research-run synthesis page where any NotebookLM citation didn't resolve via the source-map.

**Symptom:** Bogus entries like `sources/3`, `sources/4`, …, `sources/48` in `synthesizes:` (and as `[[sources/3]]` body wikilinks) — these are NotebookLM citation NUMBERS that got rendered as wikilink targets instead of being passed through the `[[nlm:<id>]]` fallback path. Observed on every 2026-05-12 / 05-13 research-run output.

**Contract:** `gateway/research/source_map.py:resolve_citations` is supposed to emit `[[sources/<slug>]]` only when a resolved slug exists, else `[[nlm:<id>]]` (per its docstring). Something upstream is constructing a `source_map` entry that resolves the integer key to a string `sources/<num>` instead of leaving it unresolved.

**First places to look:**
- `gateway/research/orchestrator.py` `_coerce_citations()` — the integer-key coercion
- `gateway/research/source_map.py` `resolve_citations()` — the wikilink construction
- The actual `source_map` payload arriving from `notebook_query` in `analysis.py`

**Fix shape:** unlikely to need a new module; one helper + one test. Half-session.

---

## #3 — `nlm_registry.register_session` non-idempotent on `status=promoted`

**Severity:** Real bug (medium). Causes long research runs to crash at the very end with `ValueError: session already registered for domain X (status=promoted); abandon it first to re-register`. Burned us during M44 validation; would re-bite anyone who re-executes a previously-promoted plan.

**Contract:** The gateway-ops idempotent-convergent memory says re-running an op on partial state should converge to canonical state, not crash. Today the registry only relaxes for `status=ABANDONED` (per `src/gateway/nlm_registry.py` lines 385–397) — `PROMOTED` and `EPHEMERAL` reject.

**Fix shape:** allow `register_session` to replace `PROMOTED` entries when the caller passes an explicit `force=True` (or, gentler, when the new notebook_id differs from the recorded one — the user is rerunning, intent is replace). One function + 3 tests.

---

## #4 — Academic-publisher convert failures (doi.org, sciencedirect, wiley, springer, ASCE, tandfonline)

**Severity:** Persistent friction (medium). Every academic research run loses 50–80% of accepted candidates at the convert stage — the converter can't get past JS-rendered or paywalled publisher pages. The 2026-05-13 ML-models run materialized 4 of 24 accepted; the 05-11 methodology run materialized 5 of 18. Reserve-study-firms (firmware-explainer / YouTube content) wasn't affected.

**Approach:** the obvious lever is a Firecrawl backend for the web converter (the firecrawl skill set is already installed). Different from PDF-extraction: this is JS-rendered web pages. Likely:
- New `src/gateway/converters/firecrawl.py` that calls the firecrawl HTTP API
- Dispatch precedence: try cheap `httpx`-based fetch first; fall back to Firecrawl on `no extractable content` or 403/429
- Cost gate (Firecrawl bills per page) — opt-in via `WIKI_FIRECRAWL_FALLBACK=1` or per-domain policy flag

**Fix shape:** medium — new converter + dispatch tweak + per-domain opt-in + cost telemetry. Full session.

---

## #5 — Filter score not written to `raw/` frontmatter on the research path

**Severity:** Low / cosmetic-but-real. The `wiki ingest` path writes a `filter:` block into `raw/<type>/<id>.md` frontmatter (score, policy_version, rationale, decided_at, user_correction). The research orchestrator's `_materialize` writes raw/ files without this block, so research-materialized sources have empty `filter:` blocks when inspected.

**Fix shape:** Thread the per-candidate score from `_run_filter` into `_materialize` and have `_materialize` write the filter block before `write_atomic`. ~30 lines + 1 test. Quarter-session.

---

## #6 — `wiki cite` / `wiki edit` gateway op for hand-editing existing pages

**Severity:** Open architectural question. Memory: `gateway_edit_path_open_question.md`. M45 makes this a real use case — attributing framing prose in `draft: true` synthesis pages requires a structured way to add citations without going through `wiki ingest` or `wiki research`.

**Status:** `wiki cite` already exists (`gateway/ops/cite.py`) and works for line-keyed source-citation tokens. Item #1 used it successfully. **Bug surfaced during item #1:** `wiki cite` uses FILE line numbers; `citation-grounding` validator errors report BODY-relative line numbers. The two conventions don't match, causing a sharp edge when copy-pasting from validator output into `wiki cite` arguments.

**Open question:** should `wiki cite` accept body-relative lines too (maybe via a `--body-line` flag)? Or should the validator's error messages report file-line numbers? Probably the latter — file lines are the universal reference.

Also: should the `wiki edit` op exist beyond `wiki cite`? Use cases: rewriting a stale Summary, adding a missing Related section, fixing a typo without going through ingest. Possibly yes, possibly punt to direct file edit + `git diff` review.

**Fix shape:** the line-number-convention fix is ~10 lines + 1 test. The `wiki edit` question is a real design decision worth its own consultation.

---

## #7 — Legacy synthesis page `2026-05-08-how-should-a-condo-hoa-integrate-cross-cutting.md` predates M45

**Severity:** Low cosmetic. Flagged by `wiki lint --scope citation-chains` as `aggregate-framing-without-synthesizes` — it emits "Based on…" openers without an enumerated constituent set. Could be retrofitted via the M45 backfill script (`scripts/m45_backfill_synthesizes.py`).

**Fix shape:** one shell command (`python scripts/m45_backfill_synthesizes.py 2026-05-08-how-should-a-condo-hoa-integrate`), then `wiki finalize` per page if validation passes. ~10 minutes.

---

## #8 — Stray Python/zsh processes from prior sessions

**Severity:** Cosmetic. `ps aux` shows old (`Sat06PM` etc.) Python and zsh processes from earlier `wiki research` launches that didn't clean up. They're idle and consuming no resources, but they clutter the process table.

**Fix shape:** `kill <pid>` per stale process. Or do nothing — they'll go away on next reboot.

---

## Session-end housekeeping (completed at suspension)

- `wiki cite` + `wiki finalize` ran on all 5 M44.3 backfilled synthesis pages from the 2026-05-11 methodology session. They are now non-draft and committable.
- 5 `wiki/sources/web-*.md` pages created via `ingest._make_source_page()` to back the citations.
- README.md and TUTORIAL.md updated to document M44 (parallel Haiku filter) and M45 (--draft default, `synthesizes:` chain, `wiki cite`/`wiki finalize` workflow).
- M45 design doc + BUILD.md § 10 M44/M44.1/M44.2/M44.3/M45/M45.1 entries written.
- Memory proposals for the next session: see chat transcript.

---

## What NOT to do when resuming

- **Don't extend `_AGGREGATE_FRAMING_OPENERS_RE` further.** The session ended with explicit user agreement that allowlist-chasing is the wrong move. New rejection patterns from `wiki research` runs are the `--draft` workflow's responsibility, not the allowlist's.
- **Don't extend `_STRUCTURAL_FRAME_LABELS` reflexively.** Only add labels that are genuinely structural metadata (no claim in the value). M45.1 added Gap/Limitation/Tension Identified for this reason. New additions need the same justification.
- **Don't re-execute promoted research sessions** until #3 (`register_session` idempotency) is fixed. Re-execute on a `status=promoted` session crashes at run-end after 30+ minutes of work.

---

## Items added 2026-05-23 during `ai-native-business` domain build

### #N — `nlm-sync` / `nlm-add` fails on Substack and custom-domain pages

**Severity:** Real bug (medium). Blocks Substack-from-inbox-style corpus building. Surfaced 2026-05-23 during the `ai-native-business` domain build.

**Symptom:** `nlm source add <notebook-id> --url <url> --wait` exits 1 with:
```
Error: Could not add url source.
Hint: Check the URL is accessible. For YouTube, ensure the video is public.
```
The URLs *are* accessible (confirmed via `curl -sI` returning 200) and trafilatura ingests them fine into `raw/`. The failure is downstream — NotebookLM's URL crawler can't fetch them, likely due to Substack / Cloudflare / Bot-protection rejecting NotebookLM's user-agent.

**Affected hosts observed:** `latent.space`, `notboring.co`, `bigtechnology.com`, `productmarketfit.tech`, `enginesofchange.ai` (partial — `/components-not-solutions` worked but `/when-the-human-layer` failed), `reboundcapital.substack.com`, `nlp.elvissaravia.com`, `news.aiinvestinghq.com`, `michaeljburry.substack.com`, `natesnewsletter.substack.com`. Roughly 11 of 18 sources in the 2026-05-23 batch hit this. Other Substacks worked (`thezvi`, `pmresearcher`, `dwarkesh`, `departmentofproduct`, `backofmind`).

**Workaround shape:** when `--url` mode fails, retry with `--text <body>` mode using the raw markdown body already in `raw/<type>/<id>.md`. The text body is what NLM ultimately indexes anyway — bypassing the crawler is equivalent.

**Related symptom:** the empty-`--text` failure that appeared during Pillar 1's research-run promotion (`nlm source add ... --text  --wait` with empty body) on Pieter Levels and HBS YouTube transcripts looks like the same bug class — both fall back to a broken adapter when the primary path is unavailable.

**Fix shape:** add an exception-catching fallback in `gateway/ops/nlm.py` around the `--url` add. One helper + one integration test. Half-session.

### #N+1 — Filter rejects clearly-relevant industry-context sources for "industry/macro/moats"-style domains

**Severity:** Policy-calibration friction (low/medium). The `wiki bootstrap-domain` LLM produced an inclusion list weighted toward operator-specific case studies with numbers, which excluded broader-but-still-load-bearing AI industry / model-market / economics analysis. ~93% rejection rate on Pillar 1's research run, ~78% rejection rate on the first Substack ingest pass.

**Mitigation already applied:** two new inclusion criteria added to `.knowledge/policies/ai-native-business/policy.yaml`; thresholds lowered (include 0.7→0.55, review 0.5→0.35). Re-tested fine on subsequent ingests.

**Suggested change to `bootstrap-domain` prompt:** when the domain description references "industry/macro/economics/moats/defensibility/capital", ask the LLM to add an explicit "context-adjacent" inclusion criterion. These domains need broader latitude than pure operator-specifics.

**Fix shape:** prompt change in `gateway/ops/bootstrap_domain.py`. Trivial.

### #N+2 — `wiki research` adapters fail hard on HTTP 429 instead of backoff (arxiv, YouTube Data API search)

**Severity:** Real bug (medium). Hit during the 2026-05-23 parallel-execute run. Semantic Scholar has 429-aware backoff (commit `1dd03ff`); arxiv and youtube-search adapters do not.

**Symptom:** `[research:<session>] search failed for arxiv: arxiv API returned HTTP 429`. Same shape for youtube. Adapter returns 0 candidates; downstream filter has nothing to score; synthesis depth drops.

**Trigger:** running 4 `wiki research --execute` sessions in parallel maxed YouTube's per-day quota (10K units; ~100 searches/day) and arxiv's per-IP rate. Sequential single-session runs are fine.

**Fix shape:** mirror the Semantic Scholar 429-aware retry/backoff into `research/adapters/arxiv.py` and `research/adapters/youtube.py`. Use exponential backoff with jitter; cap retries. Half-session.

### #N+3 — Stale auto-generated MoC from `wiki research` run not idempotent across reruns

**Severity:** Friction (low). Pillar 1's run auto-generated `wiki/mocs/ai-native-business.md` from its own corpus. Subsequent runs (other pillars/archetypes) don't update this MoC; only the original session's worldview is captured.

**Suggested behavior:** `wiki research --execute` should update the MoC instead of rewriting it, or skip MoC generation when one already exists (let `wiki query` author the MoC explicitly).

**Fix shape:** small `gateway/ops/research/apply_plan.py` change.
