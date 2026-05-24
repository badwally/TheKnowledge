"""K5 cost estimation — per-model pricing for `wiki status --cost`.

The Claude API emits `total_cost_usd` directly in the `--output-format json`
envelope (parsed by ``gateway.llm.telemetry.parse_claude_json``), so the
authoritative cost for any single call is already captured in
``CallResult.total_cost_usd``.

This module exists for two cases the live envelope doesn't cover:

1. Aggregating log lines from before K5 telemetry shipped (where only
   ``input_tokens``/``output_tokens`` were known).
2. Estimating cost from a token count + model id when re-computing for
   reporting (sanity check against API-reported totals).

Pricing table source: Anthropic published rates as of 2026-05-24. Update
when Anthropic re-prices any tier. **This is an estimate**, not an
authoritative billing source — `total_cost_usd` from the API envelope
always wins when available.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelPricing:
    """USD per million tokens for one model tier."""

    input_per_mtok: float
    output_per_mtok: float
    cache_read_per_mtok: float
    cache_creation_per_mtok: float


# Pricing as of 2026-05-24. Keys mirror what the claude JSON envelope's
# `modelUsage` keys look like. Update when Anthropic re-prices.
PRICING: dict[str, ModelPricing] = {
    # Opus 4.7 (with optional 1M-context flag): $15 / $75 standard,
    # cache read at 10% of input, cache creation at 25% premium over
    # input for the 5-minute TTL tier.
    "claude-opus-4-7": ModelPricing(15.00, 75.00, 1.50, 18.75),
    "claude-opus-4-7[1m]": ModelPricing(15.00, 75.00, 1.50, 18.75),
    # Sonnet 4.6: $3 / $15 standard.
    "claude-sonnet-4-6": ModelPricing(3.00, 15.00, 0.30, 3.75),
    # Haiku 4.5: $0.80 / $4.00 standard.
    "claude-haiku-4-5-20251001": ModelPricing(0.80, 4.00, 0.08, 1.00),
    "claude-haiku-4-5": ModelPricing(0.80, 4.00, 0.08, 1.00),
}


def estimate_cost(
    model: str,
    *,
    input_tokens: int = 0,
    output_tokens: int = 0,
    cache_read_tokens: int = 0,
    cache_creation_tokens: int = 0,
) -> float:
    """Estimate USD cost for a call given model + token counts.

    Returns 0.0 if the model id isn't in the pricing table (e.g., a
    future model or an unknown alias). Callers may want to log a warning
    when this happens, but the function itself stays silent so it works
    cleanly inside aggregation loops.
    """
    prices = PRICING.get(model)
    if prices is None:
        return 0.0
    return (
        input_tokens * prices.input_per_mtok / 1_000_000
        + output_tokens * prices.output_per_mtok / 1_000_000
        + cache_read_tokens * prices.cache_read_per_mtok / 1_000_000
        + cache_creation_tokens * prices.cache_creation_per_mtok / 1_000_000
    )


def known_models() -> list[str]:
    """Return the list of model ids with pricing entries (for diagnostics)."""
    return sorted(PRICING.keys())
