"""Tests for the shared `gateway.llm.client.ClaudeCLIClient` (M44)."""

from __future__ import annotations

import subprocess

import pytest

from gateway.llm import ClaudeCLIClient, LLMError


def _fake_completed(returncode: int, stdout: str = "", stderr: str = ""):
    return subprocess.CompletedProcess(
        args=["claude"],
        returncode=returncode,
        stdout=stdout,
        stderr=stderr,
    )


# --- argv assembly ----------------------------------------------------------


def test_argv_includes_no_session_persistence_and_tools_empty(monkeypatch):
    captured: list[list[str]] = []

    def fake_run(argv, *_args, **_kwargs):
        captured.append(list(argv))
        return _fake_completed(0, stdout="ok")

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient()
    client.call(user_prompt="hello", system_prompt="sys", model="claude-haiku-4-5-20251001")

    assert len(captured) == 1
    argv = captured[0]
    assert argv[0] == "claude"
    assert argv[1] == "-p"
    assert "--no-session-persistence" in argv
    assert "--tools" in argv
    # --tools "" defaults: assert the empty string follows --tools
    assert argv[argv.index("--tools") + 1] == ""
    # --bare is forbidden: it bypasses Max OAuth and forces API-key auth
    assert "--bare" not in argv


def test_argv_includes_model_and_system_prompt_in_correct_positions(monkeypatch):
    captured: list[list[str]] = []
    monkeypatch.setattr(subprocess, "run", lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, "ok")))

    ClaudeCLIClient().call(
        user_prompt="USER",
        system_prompt="SYS",
        model="claude-opus-4-7",
    )
    argv = captured[0]
    assert argv[argv.index("--model") + 1] == "claude-opus-4-7"
    assert argv[argv.index("--system-prompt") + 1] == "SYS"
    # user prompt is the final positional
    assert argv[-1] == "USER"


def test_argv_omits_tools_flag_when_tools_none(monkeypatch):
    captured: list[list[str]] = []
    monkeypatch.setattr(subprocess, "run", lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, "ok")))

    ClaudeCLIClient().call(user_prompt="u", tools=None)
    argv = captured[0]
    assert "--tools" not in argv


def test_argv_supports_named_tools_for_vlm(monkeypatch):
    captured: list[list[str]] = []
    monkeypatch.setattr(subprocess, "run", lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, "ok")))

    ClaudeCLIClient().call(user_prompt="u", tools="Read")
    argv = captured[0]
    assert argv[argv.index("--tools") + 1] == "Read"


def test_argv_appends_extra_args_before_user_prompt(monkeypatch):
    captured: list[list[str]] = []
    monkeypatch.setattr(subprocess, "run", lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, "ok")))

    ClaudeCLIClient().call(
        user_prompt="USER",
        extra_args=["--dangerously-skip-permissions"],
    )
    argv = captured[0]
    assert "--dangerously-skip-permissions" in argv
    assert argv[-1] == "USER"
    assert argv.index("--dangerously-skip-permissions") < argv.index("USER")


def test_argv_omits_system_prompt_when_none(monkeypatch):
    captured: list[list[str]] = []
    monkeypatch.setattr(subprocess, "run", lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, "ok")))

    ClaudeCLIClient().call(user_prompt="u")
    argv = captured[0]
    assert "--system-prompt" not in argv


# --- retry behavior ---------------------------------------------------------


def test_retries_then_succeeds(monkeypatch):
    sleeps: list[float] = []
    calls = {"n": 0}

    def fake_run(*_args, **_kwargs):
        calls["n"] += 1
        if calls["n"] < 3:
            return _fake_completed(1, stderr="rate_limit_error: 429")
        return _fake_completed(0, stdout="success")

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient(retry_base_s=0.01, sleep=sleeps.append)
    out = client.call(user_prompt="p")
    assert out == "success"
    assert calls["n"] == 3
    assert sleeps == [pytest.approx(0.01), pytest.approx(0.02)]


def test_raises_after_max_retries(monkeypatch):
    sleeps: list[float] = []

    def fake_run(*_args, **_kwargs):
        return _fake_completed(1, stderr="overloaded_error: 529")

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient(max_retries=2, retry_base_s=0.01, sleep=sleeps.append)
    with pytest.raises(LLMError, match="3 attempts"):
        client.call(user_prompt="p")
    assert len(sleeps) == 2


# --- error mapping ----------------------------------------------------------


def test_missing_executable_raises_llm_error(monkeypatch):
    def fake_run(*_args, **_kwargs):
        raise FileNotFoundError("claude not found")

    monkeypatch.setattr(subprocess, "run", fake_run)
    with pytest.raises(LLMError, match="not found on PATH"):
        ClaudeCLIClient().call(user_prompt="p")


def test_timeout_raises_llm_error(monkeypatch):
    def fake_run(*_args, **_kwargs):
        raise subprocess.TimeoutExpired(cmd=["claude"], timeout=1.0)

    monkeypatch.setattr(subprocess, "run", fake_run)
    with pytest.raises(LLMError, match="timed out"):
        ClaudeCLIClient(timeout_s=1.0).call(user_prompt="p")


# --- env hygiene ------------------------------------------------------------


def test_strips_anthropic_api_key_from_subprocess_env(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-fake-should-not-leak")
    captured_envs: list[dict] = []

    def fake_run(*_args, env=None, **_kwargs):
        captured_envs.append(env or {})
        return _fake_completed(0, stdout="ok")

    monkeypatch.setattr(subprocess, "run", fake_run)
    ClaudeCLIClient(retry_base_s=0.01, sleep=lambda _s: None).call(user_prompt="p")

    assert "ANTHROPIC_API_KEY" not in captured_envs[0]
    assert captured_envs[0].get("PATH") is not None


# --- global min-interval throttle ------------------------------------------


@pytest.fixture(autouse=False)
def _reset_throttle():
    """Reset the class-level last-call timestamp before and after each
    throttle test so they are order-independent."""
    ClaudeCLIClient._last_call_monotonic = float("-inf")
    yield
    ClaudeCLIClient._last_call_monotonic = float("-inf")


def test_min_interval_default_is_zero_no_throttle(monkeypatch, _reset_throttle):
    """Without WIKI_LLM_MIN_INTERVAL_S and without an explicit override,
    `call()` does not sleep before subprocess.run."""
    monkeypatch.delenv("WIKI_LLM_MIN_INTERVAL_S", raising=False)
    sleeps: list[float] = []

    def fake_run(*_args, **_kwargs):
        return _fake_completed(0, stdout="ok")

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient(sleep=sleeps.append)
    client.call(user_prompt="p")
    client.call(user_prompt="p")

    assert sleeps == [], f"expected no throttle sleeps, got {sleeps}"


def test_min_interval_serializes_consecutive_calls(monkeypatch, _reset_throttle):
    """With min_interval_s=1.5 and consecutive calls at simulated t=0, t=0.5,
    the second call sleeps for 1.0s before issuing subprocess.run."""
    sleeps: list[float] = []
    clock = {"t": 0.0}

    def fake_monotonic() -> float:
        return clock["t"]

    def fake_sleep(s: float) -> None:
        sleeps.append(s)
        clock["t"] += s  # advance simulated clock by the sleep amount

    monkeypatch.setattr(subprocess, "run", lambda *_a, **_k: _fake_completed(0, "ok"))
    client = ClaudeCLIClient(
        min_interval_s=1.5, sleep=fake_sleep, monotonic=fake_monotonic
    )

    client.call(user_prompt="first")  # t=0 → no prior call → no sleep, stamps t=0
    clock["t"] = 0.5                  # 0.5s passes between calls
    client.call(user_prompt="second")  # 0.5 elapsed, needs 1.0 more

    assert sleeps == [pytest.approx(1.0)]


def test_min_interval_skips_sleep_when_enough_time_elapsed(
    monkeypatch, _reset_throttle
):
    """If the gap since the last call already exceeds min_interval_s, no
    sleep is performed."""
    sleeps: list[float] = []
    clock = {"t": 0.0}

    def fake_sleep(s: float) -> None:
        sleeps.append(s)

    monkeypatch.setattr(subprocess, "run", lambda *_a, **_k: _fake_completed(0, "ok"))
    client = ClaudeCLIClient(
        min_interval_s=1.0,
        sleep=fake_sleep,
        monotonic=lambda: clock["t"],
    )

    client.call(user_prompt="first")
    clock["t"] = 5.0  # plenty of time has passed
    client.call(user_prompt="second")

    assert sleeps == []


def test_min_interval_throttle_is_shared_across_instances(
    monkeypatch, _reset_throttle
):
    """Two separate ClaudeCLIClient instances share the class-level
    throttle — so parallel filter workers each instantiating their own
    client still cooperate on the global rate limit."""
    sleeps: list[float] = []
    clock = {"t": 0.0}

    def fake_sleep(s: float) -> None:
        sleeps.append(s)
        clock["t"] += s

    monkeypatch.setattr(subprocess, "run", lambda *_a, **_k: _fake_completed(0, "ok"))

    inst_a = ClaudeCLIClient(
        min_interval_s=2.0, sleep=fake_sleep, monotonic=lambda: clock["t"]
    )
    inst_b = ClaudeCLIClient(
        min_interval_s=2.0, sleep=fake_sleep, monotonic=lambda: clock["t"]
    )

    inst_a.call(user_prompt="from-a")  # stamps t=0
    inst_b.call(user_prompt="from-b")  # would need to wait 2.0s

    assert sleeps == [pytest.approx(2.0)]


def test_min_interval_reads_env_var(monkeypatch, _reset_throttle):
    """When `min_interval_s` is not supplied to the constructor, the
    `WIKI_LLM_MIN_INTERVAL_S` env var is consulted."""
    monkeypatch.setenv("WIKI_LLM_MIN_INTERVAL_S", "0.75")
    client = ClaudeCLIClient()
    assert client._min_interval_s == pytest.approx(0.75)


def test_min_interval_env_var_invalid_falls_back_to_zero(
    monkeypatch, _reset_throttle
):
    """Unparseable WIKI_LLM_MIN_INTERVAL_S falls back to 0 rather than
    crashing the orchestrator."""
    monkeypatch.setenv("WIKI_LLM_MIN_INTERVAL_S", "not-a-number")
    client = ClaudeCLIClient()
    assert client._min_interval_s == 0.0


def test_min_interval_constructor_override_wins_over_env(
    monkeypatch, _reset_throttle
):
    monkeypatch.setenv("WIKI_LLM_MIN_INTERVAL_S", "5.0")
    client = ClaudeCLIClient(min_interval_s=0.1)
    assert client._min_interval_s == pytest.approx(0.1)
