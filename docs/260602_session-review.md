# Session Review — 2026-06-02

**Scope:** convergent-ai-brain H1a regen attempt, diagnosis, cleanup.
**Commits this session:** `b4f53531` (H1a cleanup), `4bf2d221` (session-state).
**Result:** H1a confirmed blocked by corpus access; all 8 synthesis pages abandoned; index_settle fix confirmed working.

---

## § 1 — Code and coding quality

### [Medium] `nlm/notebooks.yaml:266` — session `status: promoted` is misleading after research abandonment

The H1a session entry shows `status: promoted` because 16 sources were promoted from the session notebook into the persistent corpus. That's the notebook lifecycle status. But the *research result* was abandoned — all synthesis pages deleted, query plan marked abandoned. A future `wiki research` call or human reader scanning the registry will interpret `promoted` as "this session produced valid wiki content," which is false.

The `status` field in the sessions list is doing double duty: it tracks notebook promotion AND implies research quality. After abandonment, these diverge. The correct state for this session is closer to `promoted-but-abandoned`. Either the schema needs a `research_result` field (separate from the notebook lifecycle `status`) or `mark_abandoned` should reset `status` to `abandoned` regardless of notebook promotion state.

**Fix:** In `gateway/nlm_registry.py`, `mark_abandoned` should set the session `status` field to `abandoned` unconditionally — overriding any prior `promoted` value. Or add `research_result: abandoned` alongside the existing `status`. Without this, the persistent notebook's source count (now 90, up from 74) and `last_sync` look like evidence of a healthy session.

### [Low] `docs/backlog/h1a-corpus-access-paywalled-sources.md:50` — published placeholder arxiv ID

```
| Goldstein et al. 2022 — ECoG + GPT-2 | arxiv:2202.????? | Primary ECoG evidence |
```

A literal `?????` was committed to main. The Goldstein et al. 2022 paper ("Shared computational principles for language processing in humans and deep language models") is at `arxiv:2104.01080` — a 30-second lookup. The note as written is actionable for the "Recommended Fix" section but the source table is incomplete, which reduces its value as a revival guide.

**Fix:** Replace `arxiv:2202.?????` with the real ID. Other papers in the table (`Schrimpf biorXiv:10.1101/2020.06.26.174482`, `TopoLM arxiv ID TBD`) should also be resolved before this ticket is acted on.

### [Low] MoC `draft_unresolved_claims: 19` (was 17) with no remediation plan

The MoC gained 2 unresolved claims after the H1b synthesis content was auto-appended. This is expected behavior — `wiki research` generates draft pages — but the MoC is the domain's navigation layer and now has more unresolved claims than before the regen. No `wiki finalize` or `wiki cite` step was queued for the MoC.

No action required immediately (MoC is draft), but the pattern of MoC claim count increasing with each research session without a matching finalize pass will compound over time.

---

## § 2 — Token efficiency

### Wasted tool call: `/usage` bash probe

The session opened with `Bash("/usage 2>/dev/null")`. The `/usage` slash command is a Claude Code CLI command; it cannot be invoked from a subprocess shell. The call returned `"usage command not available in bash"` immediately. **1 tool call wasted.**

The auth state was already encoded in the local-command output visible at the top of the conversation: `"Draws from usage credits · Fast mode OFF"` — that string is the Max plan indicator. The bash probe was unnecessary and unproductive given this evidence was already present.

### Wasted tool call: duplicate background-task output read before completion

After the research session was launched, the output file was read at offset 25 twice within the same exchange:

```
Read(offset=25)   → "arxiv API network error..." (line 25 only — task still running)
Read(offset=25, limit=100) → same line 25 — no new content
```

The second read returned identical output. The background task notification was the correct signal to wait for; polling an offset that hasn't advanced consumes a tool call and adds no information. **1 tool call wasted.**

### Over-wide read: `notebooks.yaml` via raw bash → 35.6 KB output, truncated

```bash
cat nlm/notebooks.yaml  # → "Output too large (35.6KB). Full output saved to: ..."
```

The file is large enough that bash truncated it to a temp file, requiring a follow-up targeted python read to get the convergent-ai-brain section. A python one-liner would have retrieved exactly the needed section in one shot:

```bash
.venv/bin/python -c "import yaml; ..."  # (used later — should have been first)
```

**Excess:** 1 extra tool call for the truncated bash read before the targeted query.

### Highest-value waste: full NLM session run on a corpus that word-count sampling would have ruled out

The H1a research session consumed ~30 minutes of wall-clock time, 21 NLM source uploads, a 9-minute index-settle wait, and an analysis pass — for a null result caused by corpus sparsity. The failure mode was identifiable before running: the convert-failure log (lines 1–25 in the background task output) showed 403s and 429s on the bulk of the arxiv/PNAS targets. A pre-flight word-count sample on even 5 of the accepted candidates would have revealed the sparse corpus.

This isn't a "tool call" waste in the narrow sense, but it's the session's most significant efficiency failure: the diagnostic information (word counts, convert-failure rate) was available before running the NLM pipeline, and the decision to run was made without checking it. **Estimated avoidable cost:** ~30 min NLM quota, 1 session notebook slot in the persistent corpus.

---

## § 3 — Prompt and context engineering

### Auth signal inference: in-context evidence ignored in favor of subprocess probe

The conversation's local-command output contained `"Draws from usage credits"` — the Max plan indicator produced by the `/model` slash command. This was sufficient to answer the auth question without any tool call. Instead, a bash probe was attempted first. The pattern to adopt: when an in-context signal already answers a yes/no question, don't confirm it with a tool call.

### No pre-flight corpus quality gate before executing the research session

The workflow for `wiki research --execute <id>` currently has no pre-flight step that checks whether accepted candidates have enough extractable content to support NLM synthesis. The decision to execute was made based on the prior session's failure mode (indexing race), which had been fixed. The new failure mode (corpus sparsity) was not checked.

A corpus quality gate would look like:

1. After materialize, sample the top-N accepted sources by filter score.
2. Check word count of each raw file.
3. If median word count < threshold (e.g. 800 words) or >60% of sources are below 200 words, emit a warning and offer to abort before NLM upload.

This check could be a new `step=corpus_quality` log entry between `step=materialize` and `step=nlm_persistent`, with a `--skip-quality-check` escape hatch. Filing this as a design suggestion, not an active backlog ticket — it requires a code change to the orchestrator.

### Backlog note written without looking up source IDs

The backlog note `h1a-corpus-access-paywalled-sources.md` was written after diagnosis but without a web-lookup step to find the correct arxiv IDs for the papers listed. The result is a partially actionable document: the recommended fix is clear, but the source table has a `?????` placeholder that forces the future revivor to do a search that could have been done at filing time.

The pattern: when writing a backlog note with a specific technical action ("retry with arxiv ID X"), resolve the IDs before writing. One targeted search (e.g., "Goldstein 2022 ECoG language models arxiv") takes one tool call and produces a durable, correct note.

### Diagnosis reads were partially sequential when parallelizable

Once the collapse was identified (all pages citing only `web-2025-09-23-25b`), the diagnosis required reading:
- `source_map.py` (to understand how citations resolve)
- `analysis.py` (to understand how NLM is queried)
- Word counts of the session sources

These three reads are independent. They were issued sequentially across ~4 exchanges. Batching them into a single parallel read would have saved 2–3 exchange round-trips and kept the investigation tighter.

---

## Priority table

| # | Dimension | Finding | Action |
|---|-----------|---------|--------|
| 1 | Token efficiency + Prompt | Full NLM run with no pre-flight corpus quality check | Add `step=corpus_quality` gate in orchestrator between materialize and NLM upload; warn if median source word count < 800 or >60% are abstracts |
| 2 | Code quality | `nlm/notebooks.yaml` session `status: promoted` misleads after research abandonment | Fix `mark_abandoned` in `nlm_registry.py` to reset `status: abandoned` unconditionally, overriding prior `promoted` |
| 3 | Code quality + Prompt | `arxiv:2202.?????` placeholder committed to main | Look up Goldstein et al. arxiv ID and update `h1a-corpus-access-paywalled-sources.md` before the next H1a attempt |
| 4 | Token efficiency + Prompt | Auth probe via bash when in-context signal was already present | Adopt rule: infer auth state from "Draws from usage credits" in conversation context; no bash probe needed |
| 5 | Token efficiency | Diagnosis reads issued sequentially | Batch independent reads (source_map.py, analysis.py, word counts) into a single parallel tool call |
