"""Shared LLM client surface for filter / plan / VLM stages (M44)."""

from gateway.llm.client import ClaudeCLIClient, LLMError
from gateway.llm.config import (
    DEFAULT_FILTER_MODEL,
    DEFAULT_PLAN_MODEL,
    DEFAULT_VLM_MODEL,
    Stage,
    model_for,
)

__all__ = [
    "ClaudeCLIClient",
    "LLMError",
    "DEFAULT_FILTER_MODEL",
    "DEFAULT_PLAN_MODEL",
    "DEFAULT_VLM_MODEL",
    "Stage",
    "model_for",
]
