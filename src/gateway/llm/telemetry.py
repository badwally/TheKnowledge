"""K5 telemetry: structured usage capture for every `claude -p` invocation (M47).

Pre-M47, `ClaudeCLIClient.call()` returned plain text and the gateway had no
visibility into per-call token usage or cost. M47 adds `call_with_usage()`
alongside (back-compat preserved) which invokes `claude -p --output-format json`
and parses the structured envelope into a `CallResult`.

The JSON shape was captured live on 2026-05-24 against `claude` 2.1.150:

    {
      "type": "result",
      "result": "<assistant text>",
      "stop_reason": "end_turn",
      "duration_ms": 3163,
      "total_cost_usd": 0.14900625,
      "usage": {
        "input_tokens": 5,
        "output_tokens": 6,
        "cache_read_input_tokens": 0,
        "cache_creation_input_tokens": 23813
      },
      "modelUsage": { "<model-id>": { ... } }
    }

Missing fields default to zero / unknown so old/partial envelopes don't crash.
"""

from __future__ import annotations

from dataclasses import dataclass
import json


@dataclass(frozen=True)
class CallResult:
    """Result of a single `claude -p --output-format json` invocation."""

    text: str
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_creation_tokens: int = 0
    model: str = "unknown"
    stop_reason: str = "unknown"
    duration_ms: int = 0
    total_cost_usd: float = 0.0


def parse_claude_json(raw: str) -> CallResult:
    """Parse a `claude -p --output-format json` payload into a `CallResult`.

    Raises ``ValueError`` if the input isn't valid JSON. Missing or
    differently-shaped fields fall back to safe defaults so a future
    claude-CLI envelope change degrades gracefully rather than crashing
    every LLM call site.
    """
    if not raw.strip():
        raise ValueError("empty JSON payload from claude -p")
    payload = json.loads(raw)  # raises ValueError on malformed JSON

    text = payload.get("result", "")
    if not isinstance(text, str):
        text = ""

    usage = payload.get("usage") or {}
    input_tokens = int(usage.get("input_tokens", 0) or 0)
    output_tokens = int(usage.get("output_tokens", 0) or 0)
    cache_read_tokens = int(usage.get("cache_read_input_tokens", 0) or 0)
    cache_creation_tokens = int(usage.get("cache_creation_input_tokens", 0) or 0)

    # modelUsage keys the model id (e.g., "claude-opus-4-7[1m]"). Pick the
    # first key — there's typically only one per call. Robust against
    # missing/empty modelUsage.
    model_usage = payload.get("modelUsage") or {}
    if isinstance(model_usage, dict) and model_usage:
        model = next(iter(model_usage.keys()))
    else:
        model = "unknown"

    stop_reason = payload.get("stop_reason") or "unknown"
    if not isinstance(stop_reason, str):
        stop_reason = "unknown"

    duration_ms = int(payload.get("duration_ms", 0) or 0)
    total_cost_usd = float(payload.get("total_cost_usd", 0.0) or 0.0)

    return CallResult(
        text=text,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_read_tokens=cache_read_tokens,
        cache_creation_tokens=cache_creation_tokens,
        model=model,
        stop_reason=stop_reason,
        duration_ms=duration_ms,
        total_cost_usd=total_cost_usd,
    )
