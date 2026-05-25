# TOK-1 Cache Diagnosis: cache_read=0 in M50 Eval Hand-Test

**Date:** 2026-05-25
**Symptom:** M50 live hand-test (`wiki evaluate glp1-reward-modulation`) showed `cache_read_tokens=0` across all 15 questions, costing ~$1.16 with no cache benefit.
**Fix status:** Resolved in M50.1 (`7ad5996`). This document records the root cause analysis and confirms the fix is mechanically correct.

## Root Cause

The M50 judge passed `wiki_context` as part of a plain `user_prompt` string, with no `cache_control` block in the user turn. The judge system prompt (_JUDGE_SYSTEM_PROMPT) had `cache_control: {type: "ephemeral"}`, but it is approximately 60 tokens — well below Anthropic's 1024-token cache-eligibility floor for Claude Sonnet.

Anthropic's prompt caching requires the total prompt up to and including each `cache_control` breakpoint to exceed 1024 tokens. With only the 60-token system prompt marked, no breakpoint cleared the floor. The Anthropic API responded with `cache_creation_input_tokens=0` and `cache_read_input_tokens=0` on every call.

## Code Path (pre-M50.1)

```
Judge.score(golden, wiki_context)
  → _build_user_prompt(golden, wiki_context)   # returns one big string, no cache_control
  → AnthropicAPIClient.call_with_usage(user_prompt=full_string, system_prompt=<60 tokens w/ cache_control>)
    → messages.create(system=[{text: 60-token prompt, cache_control: ephemeral}],
                       messages=[{role: user, content: <full string, no cache_control>}])
    ← usage.cache_creation_input_tokens = 0  ← floor not cleared
    ← usage.cache_read_input_tokens = 0
```

## Fix (M50.1, commit 7ad5996)

`AnthropicAPIClient.call_with_usage` gained a `user_prompt_prefix` kwarg. When set, the user turn is sent as two content blocks:
1. The prefix block — marked `cache_control: {type: "ephemeral"}`.
2. The dynamic tail block — no cache_control.

The judge now splits at the stable/dynamic boundary:

```python
prefix = f"WIKI CONTEXT:\n\n{wiki_context}\n\n"   # stable across all questions in the run
suffix = _build_question_prompt(golden)              # per-question dynamic tail

self._client.call_with_usage(
    user_prompt=suffix,
    user_prompt_prefix=prefix,          # ← cached
    system_prompt=_JUDGE_SYSTEM_PROMPT,
    ...
)
```

The `wiki_context` for `glp1-reward-modulation` is 10k+ characters (several thousand tokens). The cumulative token count at the user-prefix breakpoint (system 60 tokens + user prefix N tokens) easily exceeds the 1024-token floor. `run_evaluate()` loads `wiki_context` once per run via `load_wiki_context(domain)` and passes the identical string to all 15 questions — ensuring the prefix is byte-for-byte identical across calls within the run, which is required for cache hits.

## SDK Verification (0.104.1)

- `anthropic.types.Usage` exposes `cache_read_input_tokens: Optional[int]` and `cache_creation_input_tokens: Optional[int]` — matching the field names used in `AnthropicAPIClient._to_result()`. No field name mismatch.
- `cache_control: {"type": "ephemeral"}` in content block dicts is accepted by SDK 0.104.1 natively (no beta header needed — prompt caching is GA).
- `messages.create()` signature confirms `system` and `messages` accept block dicts with `cache_control`.

## Expected Post-Fix Behavior

For a 15-question eval run on a domain with a large wiki_context:

| Call | cache_creation | cache_read | Notes |
|------|---------------|------------|-------|
| Q1   | > 0           | 0          | Cache entry written |
| Q2–Q15 | 0          | > 0        | Cache hit (5-min TTL, all questions in ~2–3 min) |

The system prompt's `cache_control` marker still fires but always fails the floor (60 tokens). This wastes a breakpoint slot but does not prevent the user-prefix breakpoint from caching. A cleanup option is to pass `cache_system_prompt=False` from the judge since the system prompt can't clear the floor, but this is cosmetic — behavior is correct either way.

## Verification Next Step

Run `wiki evaluate glp1-reward-modulation` on a live system after M50.1 and confirm:
- `cache_creation_input_tokens > 0` on question 1
- `cache_read_input_tokens > 0` on questions 2+
- Total cost significantly below the $1.16 M50 baseline (expected ~$0.20–0.30 at 4-5× reduction)

No code changes required. Fix is complete in `7ad5996`.
