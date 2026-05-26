# ADR-008: Prompt caching via separate Anthropic API key

**Status:** Accepted
**Date:** 2026-05-25

## Context

Research subprocesses make many sequential LLM calls (taxonomy extraction, per-branch investigation, synthesis queries). Each call re-transmits the full system prompt and policy context, making long research runs expensive. Anthropic's prompt caching reduces input-token cost for repeated prefixes, but prompt caching is only available on the direct Anthropic API — not on the Claude Max plan that the rest of the system uses (via Claude CLI OAuth).

## Decision

Research subprocesses use a separate Anthropic API key (`ANTHROPIC_API_KEY`) distinct from the Claude Max OAuth credential used for interactive CLI calls. A console-side $50/month spending cap acts as a safety net. The API client (`src/gateway/llm/api_client.py`) implements `AnthropicAPIClient` for this path; the CLI client (`src/gateway/llm/client.py`) implements `ClaudeCLIClient` for the interactive path.

Using `claude -p --bare` with the Max plan was rejected: it bypasses the OAuth agent harness but still runs against the Max plan, which has no prompt caching support and "Credit balance is too low" errors when the spending cap is hit. Routing all calls through the API key was also considered and rejected — it would require managing API credits for all interactive use, losing the simplicity of Max plan billing.

## Consequences

Two authentication paths must be maintained: Max OAuth for interactive ops, API key for research. The $50/month cap provides budget predictability but requires monitoring. Operators must set `ANTHROPIC_API_KEY` in the environment for research ops to function. The `config.py` module in `src/gateway/llm/` tracks which op names use which auth path.
