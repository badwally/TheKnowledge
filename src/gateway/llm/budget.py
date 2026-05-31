"""Per-run LLM call budget (260530 review finding #4).

A single authenticated request can fan out into many LLM calls (a research or
discharge run legitimately makes 100+). Without a ceiling, a runaway loop or a
malicious caller could drive unbounded calls — and on the Max-OAuth path the
real exposure is quota/rate-limit exhaustion, not metered dollars, so the
ceiling counts *calls*, not cost.

The budget is per-run: established at a run boundary (the web TaskStore worker
wraps each task in `call_budget()`), incremented on every LLM client call, and
it aborts THAT run with `BudgetExceededError` when the limit is crossed. The
long-lived server is unaffected — each task gets a fresh budget. Outside any
`call_budget()` context (e.g. the operator CLI) charging is a no-op, so
operator-driven runs are not capped.

The active budget lives in a ContextVar holding a thread-safe `CallBudget`.
Callers that fan out across threads (the orchestrator's filter pool) propagate
it with `contextvars.copy_context()` so pool workers charge the same budget.

Default ceiling is `WIKI_LLM_MAX_CALLS_PER_RUN` (300); 0 or negative disables.
"""

from __future__ import annotations

import contextlib
import contextvars
import os
import threading

_DEFAULT_MAX_CALLS = 300
_UNSET = object()

_budget_var: contextvars.ContextVar = contextvars.ContextVar(
    "llm_call_budget", default=None
)


class BudgetExceededError(RuntimeError):
    """Raised when a run exceeds its per-run LLM call budget."""


class CallBudget:
    """Thread-safe counter of LLM calls made within one run."""

    def __init__(self, max_calls: int | None) -> None:
        self.max_calls = max_calls
        self._used = 0
        self._lock = threading.Lock()

    @property
    def used(self) -> int:
        return self._used

    def charge(self) -> None:
        with self._lock:
            self._used += 1
            if self.max_calls is not None and self._used > self.max_calls:
                raise BudgetExceededError(
                    f"LLM call budget exceeded: {self._used} calls in one run "
                    f"(limit {self.max_calls}). Set WIKI_LLM_MAX_CALLS_PER_RUN "
                    f"to adjust, or 0 to disable."
                )


def default_max_calls() -> int | None:
    """Resolve the default per-run ceiling from the environment. 0/negative or
    unparseable → None (disabled)."""
    raw = os.environ.get("WIKI_LLM_MAX_CALLS_PER_RUN")
    if raw is None:
        return _DEFAULT_MAX_CALLS
    try:
        value = int(raw)
    except ValueError:
        return _DEFAULT_MAX_CALLS
    return value if value > 0 else None


@contextlib.contextmanager
def call_budget(max_calls=_UNSET):
    """Establish a per-run call budget for the duration of the context.

    `max_calls=None` disables the ceiling for this run; omit the argument to use
    the env-configured default. Restores the previous budget on exit (so nested
    runs are well-behaved)."""
    if max_calls is _UNSET:
        max_calls = default_max_calls()
    token = _budget_var.set(CallBudget(max_calls))
    try:
        yield _budget_var.get()
    finally:
        _budget_var.reset(token)


def charge_one() -> None:
    """Charge one LLM call against the active budget, if any. No-op when no
    budget is established (operator/CLI path)."""
    current = _budget_var.get()
    if current is not None:
        current.charge()


def current_budget() -> CallBudget | None:
    return _budget_var.get()
