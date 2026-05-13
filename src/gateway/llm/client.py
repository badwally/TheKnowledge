"""Shared `claude -p` subprocess wrapper for filter / plan / VLM stages.

M44 consolidates argv assembly, retry/backoff, and error mapping that were
previously triplicated across `filter/semantic.py`, `plan.py`, and `vlm.py`.

Every research-run LLM call goes through here with these efficiency flags:

- ``--tools ""`` (configurable)    strip built-in tool declarations from the
                                   system prompt (the bulk of agent-harness
                                   tokens)
- ``--no-session-persistence``     avoid writing a session record per call
- ``--system-prompt <prefix>``     replace Claude Code's default system prompt
                                   with the task-specific prefix
- ``--model <id>``                 explicit model selection (Haiku for filter,
                                   Opus for plan/VLM)

Auth: reuses ``claude_cli_env()`` so the user's Max-plan OAuth session is
honored and ``ANTHROPIC_API_KEY`` is dropped from the subprocess env.

**No `--bare`.** Per `claude --help`, `--bare` forces auth to
``ANTHROPIC_API_KEY``/``apiKeyHelper`` only and ignores OAuth — incompatible
with Max billing. The remaining flags above still strip the bulk of the
agent harness (tools declarations + default system prompt).
"""

from __future__ import annotations

import os
import subprocess
import threading
import time
from typing import Callable

from gateway.core import claude_cli_env


class LLMError(RuntimeError):
    """Raised when a `claude -p` invocation fails or times out."""


def _env_min_interval() -> float:
    """Read `WIKI_LLM_MIN_INTERVAL_S` from the environment.

    Returns 0.0 (no throttling) if unset or unparseable. Negative values are
    clamped to 0.
    """
    raw = os.environ.get("WIKI_LLM_MIN_INTERVAL_S", "")
    if not raw:
        return 0.0
    try:
        return max(0.0, float(raw))
    except ValueError:
        return 0.0


class ClaudeCLIClient:
    """Shared subprocess wrapper around `claude -p`.

    Per-stage clients (filter / plan / VLM) own their prompt assembly and
    error-type wrapping; this class owns argv construction, retry, and the
    subprocess call itself.

    Global throttling: a class-level lock + last-call-timestamp enforces a
    minimum interval between every `call()` across all instances and
    threads. This caps the rate at which the parallel filter (M44.1) and
    other parallel pipelines hit Anthropic, avoiding coordinated
    rate-limit waves on Max-plan accounts.

    Default interval is 0 (no throttling). Set `WIKI_LLM_MIN_INTERVAL_S=1.5`
    or similar when running large research sessions that exhaust Max-plan
    headroom.
    """

    # Class-level throttle state — shared across every ClaudeCLIClient
    # instance and every thread that calls `call()`. Initialized to -inf so
    # the first call ever passes through without artificial delay.
    _throttle_lock = threading.Lock()
    _last_call_monotonic: float = float("-inf")

    def __init__(
        self,
        *,
        executable: str = "claude",
        timeout_s: float = 120.0,
        max_retries: int = 3,
        retry_base_s: float = 5.0,
        min_interval_s: float | None = None,
        sleep: Callable[[float], None] = time.sleep,
        monotonic: Callable[[], float] = time.monotonic,
    ):
        self._exe = executable
        self._timeout = timeout_s
        self._max_retries = max_retries
        self._retry_base_s = retry_base_s
        self._min_interval_s = (
            _env_min_interval() if min_interval_s is None else max(0.0, min_interval_s)
        )
        self._sleep = sleep
        self._monotonic = monotonic

    def _throttle(self) -> None:
        """Block until the global min-interval since the last call has elapsed.

        Holding the class lock during the sleep is intentional: it
        serializes all in-flight callers at the rate of 1 per
        `min_interval_s`. With `min_interval_s == 0` the lock has near-zero
        hold time and parallel callers pass through unimpeded.
        """
        if self._min_interval_s <= 0:
            return
        with ClaudeCLIClient._throttle_lock:
            now = self._monotonic()
            elapsed = now - ClaudeCLIClient._last_call_monotonic
            wait = self._min_interval_s - elapsed
            if wait > 0:
                self._sleep(wait)
            ClaudeCLIClient._last_call_monotonic = self._monotonic()

    def call(
        self,
        *,
        user_prompt: str,
        system_prompt: str | None = None,
        model: str | None = None,
        tools: str | None = "",
        extra_args: list[str] | None = None,
    ) -> str:
        """Invoke `claude -p` and return stdout.

        - ``system_prompt`` is passed via ``--system-prompt`` (replaces the
          Claude Code default, eliminating most of the agent-harness tokens).
        - ``tools=""`` (the default) disables all built-in tools; set
          ``tools="Read"`` or similar when a stage genuinely needs a tool
          (VLM image attachment); set ``tools=None`` to omit the flag and
          inherit Claude Code's default.
        - ``extra_args`` is appended verbatim (e.g.,
          ``["--dangerously-skip-permissions"]`` for VLM).
        - Retries on non-zero exit (rate limits, transient overloads)
          with exponential backoff so a 100+ call research run does not
          silently drop decisions on a brief 429/529.
        """
        argv = self._build_argv(
            user_prompt=user_prompt,
            system_prompt=system_prompt,
            model=model,
            tools=tools,
            extra_args=extra_args,
        )

        last_err = ""
        for attempt in range(self._max_retries + 1):
            self._throttle()
            try:
                result = subprocess.run(
                    argv,
                    capture_output=True,
                    text=True,
                    timeout=self._timeout,
                    check=False,
                    stdin=subprocess.DEVNULL,
                    env=claude_cli_env(),
                )
            except FileNotFoundError as e:
                raise LLMError(
                    f"`{self._exe}` not found on PATH; install Claude Code or inject a client"
                ) from e
            except subprocess.TimeoutExpired as e:
                raise LLMError(
                    f"`{self._exe} -p` timed out after {self._timeout}s"
                ) from e

            if result.returncode == 0:
                return result.stdout

            last_err = result.stderr.strip()[:300]
            if attempt < self._max_retries:
                self._sleep(self._retry_base_s * (2 ** attempt))

        raise LLMError(
            f"`{self._exe} -p` failed after {self._max_retries + 1} attempts; last stderr: {last_err}"
        )

    def _build_argv(
        self,
        *,
        user_prompt: str,
        system_prompt: str | None,
        model: str | None,
        tools: str | None,
        extra_args: list[str] | None,
    ) -> list[str]:
        argv: list[str] = [
            self._exe,
            "-p",
            "--no-session-persistence",
        ]
        if tools is not None:
            argv += ["--tools", tools]
        if model:
            argv += ["--model", model]
        if system_prompt is not None:
            argv += ["--system-prompt", system_prompt]
        if extra_args:
            argv += list(extra_args)
        argv.append(user_prompt)
        return argv
