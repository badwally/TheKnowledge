"""TOK-1 (M49): Anthropic SDK client for prompt-caching-eligible call sites.

Parallel to ``ClaudeCLIClient`` (which uses ``claude -p`` subprocess against
the user's Max-plan OAuth). This client uses the Anthropic Python SDK
against a separate API key (``ANTHROPIC_API_KEY_RESEARCH``) with a
console-side spend cap. The reason for parallel rather than overloading
``ClaudeCLIClient`` is that the two billing/auth paths are mutually
exclusive — Max OAuth refuses the API key, and the API key path enables
caching that ``claude -p`` does not currently surface as a controllable
lever.

Selection per call site:
- Filter / plan / VLM / research: ``ClaudeCLIClient`` (Max OAuth, no cache)
- ``wiki cite --suggest``: ``AnthropicAPIClient`` (API key, cached)
"""

from __future__ import annotations

import os
import threading
import time
from typing import Callable

import anthropic

from gateway.llm.telemetry import CallResult


class APIKeyMissingError(RuntimeError):
    """Raised when ``ANTHROPIC_API_KEY_RESEARCH`` is not set."""


class AnthropicAPIClient:
    """Anthropic SDK client with prompt caching on the system prompt.

    Reads ``ANTHROPIC_API_KEY_RESEARCH`` once at construction time. Uses
    the same min-interval throttle pattern as ``ClaudeCLIClient``, but
    with its own independent class-level lock + last-call timestamp.

    The throttle budgets are intentionally independent: ``ClaudeCLIClient``
    hits the Max-plan OAuth quota while ``AnthropicAPIClient`` hits the
    separate API-key console quota. Sharing a single throttle would
    falsely couple two distinct rate-limit headrooms. Parallel callers
    across both clients each saturate their own quota.
    """

    _throttle_lock = threading.Lock()
    _last_call_monotonic: float = float("-inf")

    def __init__(
        self,
        *,
        timeout_s: float = 120.0,
        max_retries: int = 3,
        retry_base_s: float = 5.0,
        min_interval_s: float = 0.0,
        sleep: Callable[[float], None] = time.sleep,
        monotonic: Callable[[], float] = time.monotonic,
    ):
        api_key = os.environ.get("ANTHROPIC_API_KEY_RESEARCH", "")
        if not api_key:
            raise APIKeyMissingError(
                "ANTHROPIC_API_KEY_RESEARCH not set; configure a separate API "
                "key for research subprocesses (see memory: "
                "separate_api_key_for_caching)"
            )
        self._client = anthropic.Anthropic(api_key=api_key, timeout=timeout_s)
        self._timeout = timeout_s
        self._max_retries = max_retries
        self._retry_base_s = retry_base_s
        self._min_interval_s = max(0.0, min_interval_s)
        self._sleep = sleep
        self._monotonic = monotonic

    def _throttle(self) -> None:
        if self._min_interval_s <= 0:
            return
        with AnthropicAPIClient._throttle_lock:
            now = self._monotonic()
            elapsed = now - AnthropicAPIClient._last_call_monotonic
            wait = self._min_interval_s - elapsed
            if wait > 0:
                self._sleep(wait)
            AnthropicAPIClient._last_call_monotonic = self._monotonic()

    def call_with_usage(
        self,
        *,
        user_prompt: str,
        system_prompt: str | None = None,
        user_prompt_prefix: str | None = None,
        model: str,
        max_tokens: int = 4096,
        cache_system_prompt: bool = True,
    ) -> CallResult:
        """Call the API and return a ``CallResult``.

        When ``cache_system_prompt`` is True (default) and a system prompt
        is provided, applies ``cache_control={"type": "ephemeral"}`` to
        the system prompt block.

        When ``user_prompt_prefix`` is provided, the user message is sent
        as two content blocks — the prefix marked ``cache_control:
        ephemeral``, and ``user_prompt`` as the dynamic suffix. Use this
        when the cacheable region lives in the user turn (e.g., a large
        wiki context block reused across many small per-question prompts)
        and the system prompt is too short to clear Anthropic's 1024-token
        cache-eligibility floor on its own.
        """
        system_blocks: list[dict] | str | None = None
        if system_prompt is not None:
            if cache_system_prompt:
                system_blocks = [
                    {
                        "type": "text",
                        "text": system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    }
                ]
            else:
                system_blocks = system_prompt

        if user_prompt_prefix is not None:
            user_content: list[dict] | str = [
                {
                    "type": "text",
                    "text": user_prompt_prefix,
                    "cache_control": {"type": "ephemeral"},
                },
                {"type": "text", "text": user_prompt},
            ]
        else:
            user_content = user_prompt

        last_err: Exception | None = None
        for attempt in range(self._max_retries + 1):
            self._throttle()
            try:
                kwargs = {
                    "model": model,
                    "max_tokens": max_tokens,
                    "messages": [{"role": "user", "content": user_content}],
                }
                if system_blocks is not None:
                    kwargs["system"] = system_blocks
                msg = self._client.messages.create(**kwargs)
                return self._to_result(msg)
            except anthropic.APIStatusError as e:
                # Retry only the transient status codes. Non-retryable 4xx
                # (BadRequest 400, Authentication 401, PermissionDenied
                # 403, NotFound 404, UnprocessableEntity 422, ...) must
                # propagate immediately — they aren't going to resolve
                # within the 35s of compounding backoff this loop spends.
                # 503/529 (ServiceUnavailable, Overloaded) are defined in
                # anthropic._exceptions but not re-exported at the
                # top-level module, so they're handled via status_code
                # rather than named-class matching.
                if e.status_code not in (429, 500, 503, 504, 529):
                    raise
                last_err = e
                if attempt < self._max_retries:
                    self._sleep(self._retry_base_s * (2 ** attempt))
                    continue
                break
            except (anthropic.APITimeoutError, anthropic.APIConnectionError) as e:
                # Network-level errors inherit from APIError, not
                # APIStatusError — would otherwise propagate unwrapped.
                last_err = e
                if attempt < self._max_retries:
                    self._sleep(self._retry_base_s * (2 ** attempt))
                    continue
                break

        from gateway.llm import LLMError  # deferred to avoid circular import
        raise LLMError(
            f"AnthropicAPIClient failed after {self._max_retries + 1} attempts: {last_err}"
        )

    @staticmethod
    def _to_result(msg) -> CallResult:
        # msg.content is a list of content blocks; collect text-typed ones.
        text_parts: list[str] = []
        for block in msg.content:
            if getattr(block, "type", None) == "text":
                text_parts.append(getattr(block, "text", ""))
        text = "".join(text_parts)

        usage = msg.usage
        return CallResult(
            text=text,
            input_tokens=int(getattr(usage, "input_tokens", 0) or 0),
            output_tokens=int(getattr(usage, "output_tokens", 0) or 0),
            cache_read_tokens=int(getattr(usage, "cache_read_input_tokens", 0) or 0),
            cache_creation_tokens=int(getattr(usage, "cache_creation_input_tokens", 0) or 0),
            model=str(getattr(msg, "model", "unknown") or "unknown"),
            stop_reason=str(getattr(msg, "stop_reason", "unknown") or "unknown"),
            duration_ms=0,
            total_cost_usd=0.0,
        )
