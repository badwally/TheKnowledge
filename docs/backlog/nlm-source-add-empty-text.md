# Backlog: NLM Source Promotion Sends Empty `--text` for Non-Text Sources

**Category:** Gateway / Research Pipeline
**Priority:** High
**Effort:** ~1-2 hours
**Trigger to action:** Any research run whose adapters surface video/YouTube (non-text) NLM sources — recurs every such run

---

## Problem

When `wiki research` promotes NotebookLM-discovered sources into the persistent
corpus, the promoter calls `nlm source add <notebook-id> --text "" --title <T>`
for sources that have no extractable text body (video / YouTube / talk
recordings). The empty `--text` makes `nlm` reject the call, so the source fails
to promote.

In the convergent-ai-brain H1a session this dropped 9 of 50 materialized sources
(`added=41 failed=9`) — and they were high-value primary sources (Kriegeskorte
RSA talk, Olshausen sparse-coding talk, Huth workshop), i.e. exactly the
empirical-spine material the domain wanted.

## Evidence

From `log.md`, session `2026-05-30-what-is-the-empirical-evidence-that`:

```
warning: promote source A New Framework for Modeling Brain Information Processing - Nikolaus Kriegeskorte: `nlm source add 9450c6a9-3175-489a-9e25-cbd38e00bf31 --text  --wait --title ...` exited 1: Error: Please specify a source: --url, --text, --file, --drive, or --youtube
warning: promote source Bruno Olshausen: Robust and efficient ... sparse coding networks: `nlm source add 9450c6a9-... --text  --wait --title ...` exited 1: Error: Please specify a source ...
... (9 total; all video/talk sources)

research | step=promoted | added=41 | failed=9
```

## Proposed Solution

In the source-promotion path, branch on the discovered source's media type:

- video / YouTube → `nlm source add <id> --youtube <url>` (or `--url <url>`)
- web/article with a URL → `--url <url>`
- only fall back to `--text` when a real text body exists

If no usable handle exists, skip with an explicit `skipped (no text body)` log
line rather than emitting a guaranteed-to-fail `nlm` call counted as `failed`.

## Acceptance criteria

- [ ] Video/YouTube NLM sources promote via `--youtube`/`--url`, not empty `--text`
- [ ] A research session that surfaces media sources reports `failed=0` for the empty-text cause
- [ ] Sources with genuinely no handle are logged as `skipped`, not `failed`
