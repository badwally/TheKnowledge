"""Tests for AnthropicAPIClient (TOK-1, M49).

Mocks the `anthropic.Anthropic` client so tests are hermetic. Real-network
verification is via the hand-test in docs/milestones/M49.md.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import anthropic
import pytest

from gateway.llm.api_client import AnthropicAPIClient
from gateway.llm import LLMError


def _mock_message(text: str = "ok", input_tokens: int = 10, output_tokens: int = 2,
                  cache_read: int = 0, cache_creation: int = 0,
                  model: str = "claude-sonnet-4-6") -> MagicMock:
    """Build a mock anthropic.types.Message matching the SDK shape."""
    msg = MagicMock()
    msg.content = [MagicMock(type="text", text=text)]
    msg.usage = MagicMock(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        cache_read_input_tokens=cache_read,
        cache_creation_input_tokens=cache_creation,
    )
    msg.model = model
    msg.stop_reason = "end_turn"
    return msg


def test_call_with_usage_returns_text_and_telemetry(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message(
            text="hello", input_tokens=42, output_tokens=7
        )

        client = AnthropicAPIClient()
        result = client.call_with_usage(
            user_prompt="say hello",
            system_prompt="be brief",
            model="claude-sonnet-4-6",
        )

    assert result.text == "hello"
    assert result.input_tokens == 42
    assert result.output_tokens == 7
    assert result.model == "claude-sonnet-4-6"


def test_raises_when_key_missing(monkeypatch):
    from gateway.llm.api_client import APIKeyMissingError

    monkeypatch.delenv("ANTHROPIC_API_KEY_RESEARCH", raising=False)
    with pytest.raises(APIKeyMissingError):
        AnthropicAPIClient()


def test_cache_control_applied_to_system_prompt(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message()

        client = AnthropicAPIClient()
        client.call_with_usage(
            user_prompt="q",
            system_prompt="long stable prefix",
            model="claude-sonnet-4-6",
        )

        kwargs = mock_client.messages.create.call_args.kwargs
        assert kwargs["system"] == [
            {
                "type": "text",
                "text": "long stable prefix",
                "cache_control": {"type": "ephemeral"},
            }
        ]


def test_cache_control_can_be_disabled(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message()

        client = AnthropicAPIClient()
        client.call_with_usage(
            user_prompt="q",
            system_prompt="prefix",
            model="claude-sonnet-4-6",
            cache_system_prompt=False,
        )

        kwargs = mock_client.messages.create.call_args.kwargs
        assert kwargs["system"] == "prefix"


def test_cache_read_tokens_surface_in_call_result(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        mock_client.messages.create.return_value = _mock_message(
            input_tokens=5,
            output_tokens=3,
            cache_read=2000,
            cache_creation=0,
        )

        client = AnthropicAPIClient()
        result = client.call_with_usage(
            user_prompt="q",
            system_prompt="long prefix",
            model="claude-sonnet-4-6",
        )

    assert result.cache_read_tokens == 2000
    assert result.input_tokens == 5


def _mock_response(status_code: int) -> MagicMock:
    """Build a MagicMock that quacks as the httpx.Response APIStatusError needs."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.headers = {"request-id": "test-req"}
    resp.request = MagicMock()
    return resp


def test_retries_on_rate_limit_then_succeeds(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")
    sleeps: list[float] = []

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        rate_err = anthropic.RateLimitError(
            message="rate", response=_mock_response(429), body=None
        )
        mock_client.messages.create.side_effect = [rate_err, _mock_message(text="ok-after-retry")]

        client = AnthropicAPIClient(retry_base_s=0.01, sleep=sleeps.append)
        result = client.call_with_usage(user_prompt="q", model="claude-sonnet-4-6")

    assert result.text == "ok-after-retry"
    assert mock_client.messages.create.call_count == 2
    assert len(sleeps) == 1  # one backoff between attempts


def test_non_retryable_error_propagates_immediately(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY_RESEARCH", "sk-ant-test")

    with patch("gateway.llm.api_client.anthropic.Anthropic") as mock_class:
        mock_client = mock_class.return_value
        bad_req = anthropic.BadRequestError(
            message="bad", response=_mock_response(400), body=None
        )
        mock_client.messages.create.side_effect = bad_req

        client = AnthropicAPIClient(retry_base_s=0.01)
        with pytest.raises(anthropic.BadRequestError):
            client.call_with_usage(user_prompt="q", model="claude-sonnet-4-6")

    # Single attempt — no retries on 400
    assert mock_client.messages.create.call_count == 1
