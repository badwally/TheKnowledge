"""Tests for gateway.llm.config — model selection per stage."""

from gateway.llm.config import (
    DEFAULT_CITE_SUGGEST_MODEL,
    model_for,
)


def test_cite_suggest_stage_returns_sonnet():
    assert model_for("cite_suggest") == "claude-sonnet-4-6"
    assert DEFAULT_CITE_SUGGEST_MODEL == "claude-sonnet-4-6"
