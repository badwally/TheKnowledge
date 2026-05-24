"""Shared LLM client surface for filter / plan / VLM stages (M44 + M47 telemetry)."""

from gateway.llm.api_client import AnthropicAPIClient, APIKeyMissingError
from gateway.llm.client import ClaudeCLIClient, LLMError
from gateway.llm.config import (
    DEFAULT_FILTER_MODEL,
    DEFAULT_PLAN_MODEL,
    DEFAULT_VLM_MODEL,
    Stage,
    model_for,
)
from gateway.llm.telemetry import CallResult, parse_claude_json

__all__ = [
    "AnthropicAPIClient",
    "APIKeyMissingError",
    "ClaudeCLIClient",
    "LLMError",
    "CallResult",
    "parse_claude_json",
    "DEFAULT_FILTER_MODEL",
    "DEFAULT_PLAN_MODEL",
    "DEFAULT_VLM_MODEL",
    "Stage",
    "model_for",
]
