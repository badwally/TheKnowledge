# gateway.llm

The llm package provides the two LLM call paths used by the gateway. `ClaudeCLIClient` shells out to `claude -p` and routes through the user's Max-plan OAuth session — used by filter, plan, VLM, and research stages where prompt caching is not available. `AnthropicAPIClient` uses the Anthropic Python SDK against a separate `ANTHROPIC_API_KEY_RESEARCH` key with a console-side spend cap — used by call sites where prompt caching yields meaningful savings (currently `wiki cite --suggest`). The two clients share the same throttle pattern (class-level lock + last-call timestamp) but use independent locks so their rate-limit headrooms do not interfere. `telemetry.py` captures structured token usage from `claude -p --output-format json` responses. `config.py` centralizes model-id constants.

See `ARCHITECTURE.md` for the auth path decision and `MEMORY.md` entry `separate_api_key_for_caching.md` for the TOK-1 rationale.

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Package exports |
| `client.py` | `ClaudeCLIClient` — `claude -p` subprocess wrapper with retry, throttle, argv assembly |
| `api_client.py` | `AnthropicAPIClient` — SDK client with prompt caching on the system prompt |
| `telemetry.py` | `CallResult` dataclass; `parse_claude_json()` — parses `--output-format json` envelope |
| `config.py` | Model ID constants (`HAIKU_MODEL`, `SONNET_MODEL`, `OPUS_MODEL`) |

## Worked example: filter scoring a candidate source

```
Input:  user_prompt="Abstract text of a candidate paper..."
        system_prompt="You are a domain filter for GLP-1 research. Score 0-1..."
Call:   ClaudeCLIClient().call(user_prompt=user_prompt, system_prompt=system_prompt,
                               model="claude-haiku-4-5")

1. ClaudeCLIClient._throttle() checks global min-interval
   - If WIKI_LLM_MIN_INTERVAL_S unset: no-op (passes through immediately)
   - If set (e.g. 1.5): acquires class lock, sleeps if < 1.5 s since last call
2. argv assembled:
   ["claude", "-p", user_prompt,
    "--system-prompt", system_prompt,
    "--model", "claude-haiku-4-5",
    "--tools", "",
    "--no-session-persistence",
    "--output-format", "json"]
   Note: --bare is NOT used (breaks Max OAuth billing)
3. subprocess.run(argv, env=claude_cli_env(), timeout=120, capture_output=True)
   - claude_cli_env() strips ANTHROPIC_API_KEY; OAuth session used instead
4. Non-zero exit → retry with exponential backoff up to max_retries=3
   (handles transient rate limits and overloads)
5. stdout parsed by telemetry.parse_claude_json(raw) → CallResult(
       text="0.87",
       input_tokens=312,
       output_tokens=4,
       cache_read_tokens=0,
       total_cost_usd=0.000041
   )
6. Caller (filter/semantic.py) extracts CallResult.text, parses float score

Failure modes:
- claude not on PATH          → LLMError("subprocess failed: FileNotFoundError")
- All retries exhausted       → LLMError("max retries exceeded after 3 attempts")
- JSON parse fails            → parse_claude_json returns CallResult with text=raw (graceful)
- ANTHROPIC_API_KEY_RESEARCH  not set (AnthropicAPIClient only)
                              → APIKeyMissingError raised at construction time
```
