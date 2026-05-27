"""Tests for shared gateway core helpers."""

from __future__ import annotations

import pytest

from datetime import datetime, timezone

from gateway.core import claude_cli_env, parse_iso


def test_claude_cli_env_strips_anthropic_api_key(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-do-not-leak")
    monkeypatch.setenv("OTHER_VAR", "should-stay")

    env = claude_cli_env()

    assert "ANTHROPIC_API_KEY" not in env
    assert env.get("OTHER_VAR") == "should-stay"


def test_claude_cli_env_safe_when_key_unset(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    env = claude_cli_env()
    assert "ANTHROPIC_API_KEY" not in env


def test_claude_cli_env_returns_copy(monkeypatch: pytest.MonkeyPatch):
    """Mutating the returned dict must not pollute the parent process env."""
    import os

    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-fake")
    env = claude_cli_env()
    env["INTRODUCED_BY_TEST"] = "1"
    assert os.environ.get("INTRODUCED_BY_TEST") is None


def test_claude_cli_env_opt_in_preserves_api_key(monkeypatch: pytest.MonkeyPatch):
    """`WIKI_ALLOW_API_KEY=1` opts INTO using API credits (e.g., to bypass
    Max-plan rate limits during a bulk run). Without the flag, the key is
    stripped (default Max-plan posture)."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-fake")
    monkeypatch.setenv("WIKI_ALLOW_API_KEY", "1")
    env = claude_cli_env()
    assert env.get("ANTHROPIC_API_KEY") == "sk-fake"


# ---------------------------------------------------------------------------
# parse_iso (M102)
# ---------------------------------------------------------------------------


def test_parse_iso_utc_z_suffix():
    dt = parse_iso("2026-05-27T12:00:00Z")
    assert dt == datetime(2026, 5, 27, 12, 0, 0, tzinfo=timezone.utc)


def test_parse_iso_explicit_offset():
    dt = parse_iso("2026-05-27T12:00:00+00:00")
    assert dt is not None
    assert dt.tzinfo is not None


def test_parse_iso_date_only():
    dt = parse_iso("2026-05-27")
    assert dt is not None
    assert dt.year == 2026 and dt.month == 5 and dt.day == 27
    assert dt.tzinfo == timezone.utc


def test_parse_iso_none_returns_none():
    assert parse_iso(None) is None


def test_parse_iso_non_string_returns_none():
    assert parse_iso(12345) is None
    assert parse_iso([]) is None


def test_parse_iso_empty_string_returns_none():
    assert parse_iso("") is None


def test_parse_iso_invalid_returns_none():
    assert parse_iso("not-a-date") is None
    assert parse_iso("2026-99-99") is None
