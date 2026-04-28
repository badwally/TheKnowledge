"""Editorial policy loader per WIKI.md § 10.1.

A policy lives at `.knowledge/policies/<domain-slug>/policy.yaml`. Versioned
copies live alongside under `policy_versions/`. The loader returns a `Policy`
dataclass with sane defaults so callers don't repeat threshold logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from gateway import paths


DEFAULT_THRESHOLD_INCLUDE = 0.70
DEFAULT_THRESHOLD_REVIEW = 0.50
DEFAULT_EXAMPLE_COUNT = 12
DEFAULT_EXAMPLE_STRATEGY = "balanced"


class PolicyError(ValueError):
    """Raised when a policy is missing, malformed, or self-inconsistent."""


@dataclass
class Policy:
    """Loaded policy with derived/default fields filled in."""

    domain_slug: str
    version: str = "v1"

    domain_topic: str = ""
    domain_field: str = ""
    domain_description: str = ""

    threshold_include: float = DEFAULT_THRESHOLD_INCLUDE
    threshold_review: float = DEFAULT_THRESHOLD_REVIEW
    example_count_in_prompt: int = DEFAULT_EXAMPLE_COUNT
    example_strategy: str = DEFAULT_EXAMPLE_STRATEGY

    inclusion_criteria: list[str] = field(default_factory=list)
    exclusion_criteria: list[str] = field(default_factory=list)
    quality_signals: dict[str, Any] = field(default_factory=dict)

    raw: dict[str, Any] = field(default_factory=dict)


def policy_path(domain_slug: str) -> Path:
    return paths.policies_dir() / domain_slug / "policy.yaml"


def policy_exists(domain_slug: str) -> bool:
    return policy_path(domain_slug).exists()


def load_policy(domain_slug: str) -> Policy:
    """Load and validate the policy for a domain.

    Raises PolicyError if missing or malformed.
    """
    path = policy_path(domain_slug)
    if not path.exists():
        raise PolicyError(f"no policy file for domain {domain_slug!r} (looked at {path})")

    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as e:
        raise PolicyError(f"invalid YAML in policy {path}: {e}") from e

    if not isinstance(data, dict):
        raise PolicyError(f"policy must be a YAML mapping, got {type(data).__name__}")

    domain = data.get("domain", {}) or {}
    declared_slug = domain.get("slug")
    if declared_slug and declared_slug != domain_slug:
        raise PolicyError(
            f"domain.slug in {path} is {declared_slug!r} but loaded as {domain_slug!r}"
        )

    filter_cfg = data.get("filter", {}) or {}

    return Policy(
        domain_slug=domain_slug,
        version=str(data.get("version", "v1")),
        domain_topic=str(domain.get("topic", "")),
        domain_field=str(domain.get("field", "")),
        domain_description=str(domain.get("description", "")),
        threshold_include=float(filter_cfg.get("threshold_include", DEFAULT_THRESHOLD_INCLUDE)),
        threshold_review=float(filter_cfg.get("threshold_review", DEFAULT_THRESHOLD_REVIEW)),
        example_count_in_prompt=int(filter_cfg.get("example_count_in_prompt", DEFAULT_EXAMPLE_COUNT)),
        example_strategy=str(filter_cfg.get("example_strategy", DEFAULT_EXAMPLE_STRATEGY)),
        inclusion_criteria=list(data.get("inclusion_criteria", []) or []),
        exclusion_criteria=list(data.get("exclusion_criteria", []) or []),
        quality_signals=dict(data.get("quality_signals", {}) or {}),
        raw=data,
    )
