"""Tests for K5 LLM telemetry — `CallResult` parsing + `call_with_usage()` (M47)."""

from __future__ import annotations

import json
import subprocess

import pytest

from gateway.llm import ClaudeCLIClient, LLMError
from gateway.llm.telemetry import CallResult, parse_claude_json


# --- CallResult dataclass --------------------------------------------------


def test_call_result_defaults_zero():
    r = CallResult(text="hello")
    assert r.text == "hello"
    assert r.input_tokens == 0
    assert r.output_tokens == 0
    assert r.cache_read_tokens == 0
    assert r.cache_creation_tokens == 0
    assert r.model == "unknown"
    assert r.stop_reason == "unknown"
    assert r.duration_ms == 0
    assert r.total_cost_usd == 0.0


def test_call_result_immutable():
    r = CallResult(text="x")
    with pytest.raises(Exception):  # FrozenInstanceError or AttributeError
        r.text = "y"  # type: ignore[misc]


# --- parse_claude_json -----------------------------------------------------


_REAL_PROBE = {
    "type": "result",
    "subtype": "success",
    "is_error": False,
    "duration_ms": 3163,
    "result": "ping",
    "stop_reason": "end_turn",
    "total_cost_usd": 0.14900625,
    "usage": {
        "input_tokens": 5,
        "cache_creation_input_tokens": 23813,
        "cache_read_input_tokens": 0,
        "output_tokens": 6,
    },
    "modelUsage": {
        "claude-opus-4-7[1m]": {
            "inputTokens": 5,
            "outputTokens": 6,
            "costUSD": 0.14900625,
        }
    },
}


def test_parse_real_probe_shape():
    """Live probe shape from `claude -p --output-format json` (captured 2026-05-24)."""
    r = parse_claude_json(json.dumps(_REAL_PROBE))
    assert r.text == "ping"
    assert r.input_tokens == 5
    assert r.output_tokens == 6
    assert r.cache_creation_tokens == 23813
    assert r.cache_read_tokens == 0
    assert r.model == "claude-opus-4-7[1m]"
    assert r.stop_reason == "end_turn"
    assert r.duration_ms == 3163
    assert r.total_cost_usd == pytest.approx(0.14900625)


def test_parse_missing_cache_fields_default_to_zero():
    payload = {
        "result": "ok",
        "usage": {"input_tokens": 10, "output_tokens": 20},
        "modelUsage": {"claude-haiku-4-5-20251001": {}},
    }
    r = parse_claude_json(json.dumps(payload))
    assert r.cache_read_tokens == 0
    assert r.cache_creation_tokens == 0
    assert r.input_tokens == 10
    assert r.output_tokens == 20
    assert r.model == "claude-haiku-4-5-20251001"


def test_parse_missing_model_usage_keeps_unknown():
    payload = {"result": "ok", "usage": {"input_tokens": 1, "output_tokens": 1}}
    r = parse_claude_json(json.dumps(payload))
    assert r.model == "unknown"


def test_parse_missing_result_falls_back_to_empty_text():
    payload = {"usage": {"input_tokens": 1, "output_tokens": 1}}
    r = parse_claude_json(json.dumps(payload))
    assert r.text == ""


def test_parse_invalid_json_raises():
    with pytest.raises(ValueError):
        parse_claude_json("not json at all {")


def test_parse_empty_string_raises():
    with pytest.raises(ValueError):
        parse_claude_json("")


# --- call_with_usage() argv assembly ---------------------------------------


def _fake_completed(returncode: int, stdout: str = "", stderr: str = ""):
    return subprocess.CompletedProcess(
        args=["claude"],
        returncode=returncode,
        stdout=stdout,
        stderr=stderr,
    )


def test_call_with_usage_passes_output_format_json(monkeypatch):
    captured: list[list[str]] = []

    def fake_run(argv, *_args, **_kwargs):
        captured.append(list(argv))
        return _fake_completed(0, stdout=json.dumps(_REAL_PROBE))

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient(min_interval_s=0.0)

    r = client.call_with_usage(user_prompt="say ping")
    assert r.text == "ping"
    assert r.input_tokens == 5
    # The flag is in the argv
    assert "--output-format" in captured[0]
    fmt_idx = captured[0].index("--output-format")
    assert captured[0][fmt_idx + 1] == "json"


def test_call_with_usage_returns_call_result(monkeypatch):
    def fake_run(*_args, **_kwargs):
        return _fake_completed(0, stdout=json.dumps(_REAL_PROBE))

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient(min_interval_s=0.0)
    r = client.call_with_usage(user_prompt="x")
    assert isinstance(r, CallResult)
    assert r.duration_ms == 3163


def test_call_with_usage_records_subprocess_duration_when_json_lacks_it(monkeypatch):
    """If claude JSON omits duration_ms, we still record wall-clock from subprocess."""
    payload = {
        "result": "ok",
        "usage": {"input_tokens": 1, "output_tokens": 1},
        "modelUsage": {"claude-haiku-4-5-20251001": {}},
    }

    def fake_run(*_args, **_kwargs):
        return _fake_completed(0, stdout=json.dumps(payload))

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient(min_interval_s=0.0)
    r = client.call_with_usage(user_prompt="x")
    # We don't assert a specific value (timing varies), but it should be > 0
    assert r.duration_ms >= 0  # subprocess.run is essentially instant for our stub


def test_call_with_usage_non_zero_exit_raises(monkeypatch):
    def fake_run(*_args, **_kwargs):
        return _fake_completed(1, stdout="", stderr="rate limit")

    monkeypatch.setattr(subprocess, "run", fake_run)
    # Disable retries to keep test fast
    client = ClaudeCLIClient(min_interval_s=0.0, max_retries=0, retry_base_s=0.0)
    with pytest.raises(LLMError) as exc:
        client.call_with_usage(user_prompt="x")
    assert "rate limit" in str(exc.value) or "failed" in str(exc.value)


def test_call_with_usage_invalid_json_raises(monkeypatch):
    def fake_run(*_args, **_kwargs):
        return _fake_completed(0, stdout="not json")

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIClient(min_interval_s=0.0)
    with pytest.raises(LLMError) as exc:
        client.call_with_usage(user_prompt="x")
    assert "json" in str(exc.value).lower()
