"""Per-run LLM call budget (260530 review finding #4)."""

from __future__ import annotations

import pytest

from gateway.llm import budget


def test_no_active_budget_is_noop():
    # Outside any call_budget context, charging does nothing (CLI/operator path).
    for _ in range(1000):
        budget.charge_one()
    assert budget.current_budget() is None


def test_charge_within_budget_passes():
    with budget.call_budget(3) as b:
        budget.charge_one()
        budget.charge_one()
        budget.charge_one()
        assert b.used == 3


def test_charge_over_budget_raises():
    with budget.call_budget(2):
        budget.charge_one()
        budget.charge_one()
        with pytest.raises(budget.BudgetExceededError):
            budget.charge_one()


def test_budget_resets_after_context():
    with budget.call_budget(1):
        budget.charge_one()
    # Outside the context the budget is gone; a fresh context starts clean.
    assert budget.current_budget() is None
    with budget.call_budget(1):
        budget.charge_one()  # would raise if state leaked across contexts


def test_zero_or_negative_env_disables(monkeypatch):
    monkeypatch.setenv("WIKI_LLM_MAX_CALLS_PER_RUN", "0")
    assert budget.default_max_calls() is None
    with budget.call_budget():  # uses default → disabled
        for _ in range(1000):
            budget.charge_one()  # never raises


def test_default_env_value(monkeypatch):
    monkeypatch.setenv("WIKI_LLM_MAX_CALLS_PER_RUN", "42")
    assert budget.default_max_calls() == 42


def test_cli_client_call_charges_and_aborts(monkeypatch):
    """ClaudeCLIClient.call charges the budget and raises once exceeded."""
    import types

    import gateway.llm.client as c

    fake = types.SimpleNamespace(returncode=0, stdout="ok", stderr="")
    monkeypatch.setattr(c.subprocess, "run", lambda *a, **k: fake)
    monkeypatch.setattr(c, "claude_cli_env", lambda: {})
    client = c.ClaudeCLIClient()

    with budget.call_budget(2):
        assert client.call(user_prompt="a") == "ok"
        assert client.call(user_prompt="b") == "ok"
        with pytest.raises(budget.BudgetExceededError):
            client.call(user_prompt="c")


def test_propagates_to_pool_workers_via_copy_context():
    """The shared budget must be enforceable across threads when the caller
    propagates context (as the orchestrator's filter pool does)."""
    import contextvars
    from concurrent.futures import ThreadPoolExecutor

    with budget.call_budget(5):
        ctx = contextvars.copy_context()
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = [pool.submit(ctx.run, budget.charge_one) for _ in range(5)]
            for f in futures:
                f.result()
        # 6th charge (back on the main thread, same budget) trips the limit.
        with pytest.raises(budget.BudgetExceededError):
            budget.charge_one()
