"""TOK-10: plan_authorship_small model routing tests."""

from __future__ import annotations

from gateway.llm.config import (
    DEFAULT_PLAN_AUTHORSHIP_MODEL,
    DEFAULT_PLAN_AUTHORSHIP_SMALL_MODEL,
    model_for,
)
from gateway.ops.ingest import _SMALL_BODY_THRESHOLD, _SMALL_SOURCE_TYPES, _authorship_model


# --- model_for stage routing ------------------------------------------------


def test_model_for_plan_authorship_small_returns_sonnet():
    m = model_for("plan_authorship_small")
    assert "sonnet" in m.lower()


def test_model_for_plan_authorship_small_is_different_from_opus():
    assert model_for("plan_authorship_small") != model_for("plan_authorship")


def test_model_for_plan_authorship_returns_opus():
    m = model_for("plan_authorship")
    assert "opus" in m.lower()


def test_plan_authorship_small_constant():
    assert DEFAULT_PLAN_AUTHORSHIP_SMALL_MODEL == "claude-sonnet-4-6"


def test_plan_authorship_constant():
    assert DEFAULT_PLAN_AUTHORSHIP_MODEL == "claude-opus-4-7"


# --- _authorship_model routing ----------------------------------------------


def test_voice_source_routes_to_small():
    front = {"type": "voice", "id": "voice-abc"}
    body = "Short voice note transcript."
    assert _authorship_model(front, body) == model_for("plan_authorship_small")


def test_note_source_routes_to_small():
    front = {"type": "note", "id": "note-notion-abc"}
    body = "A Notion page body."
    assert _authorship_model(front, body) == model_for("plan_authorship_small")


def test_small_body_web_routes_to_small():
    front = {"type": "web", "id": "web-2026-01-01-abc"}
    body = "x" * (_SMALL_BODY_THRESHOLD - 1)
    assert _authorship_model(front, body) == model_for("plan_authorship_small")


def test_large_body_web_routes_to_opus():
    front = {"type": "web", "id": "web-2026-01-01-def"}
    body = "x" * (_SMALL_BODY_THRESHOLD + 1)
    assert _authorship_model(front, body) == model_for("plan_authorship")


def test_arxiv_large_routes_to_opus():
    front = {"type": "arxiv", "id": "arxiv-2026-12345"}
    body = "A long academic paper body. " * 200
    assert _authorship_model(front, body) == model_for("plan_authorship")


def test_small_source_types_frozenset():
    assert "voice" in _SMALL_SOURCE_TYPES
    assert "note" in _SMALL_SOURCE_TYPES
    assert "web" not in _SMALL_SOURCE_TYPES
    assert "arxiv" not in _SMALL_SOURCE_TYPES


def test_threshold_value():
    assert _SMALL_BODY_THRESHOLD == 2048
