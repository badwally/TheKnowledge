"""Model selection per LLM stage.

M44: filter routes to Haiku 4.5 (binary triage); plan and VLM stay on Opus 4.7.
Per-domain overrides may be added via `.knowledge/policies/<domain>/model.yaml`
in a follow-up — the resolver is in place but currently returns defaults.
"""

from __future__ import annotations

from typing import Literal


Stage = Literal["filter", "plan", "vlm"]


DEFAULT_FILTER_MODEL = "claude-haiku-4-5-20251001"
DEFAULT_PLAN_MODEL = "claude-opus-4-7"
DEFAULT_VLM_MODEL = "claude-opus-4-7"


def model_for(stage: Stage, domain: str | None = None) -> str:
    """Return the model ID to use for a given stage.

    `domain` is reserved for future per-domain overrides (e.g., a domain
    whose policy needs Opus-level reasoning for filter). Returns the
    default for the stage today.
    """
    if stage == "filter":
        return DEFAULT_FILTER_MODEL
    if stage == "plan":
        return DEFAULT_PLAN_MODEL
    if stage == "vlm":
        return DEFAULT_VLM_MODEL
    raise ValueError(f"unknown LLM stage: {stage!r}")
