"""Semantic filter package per WIKI.md § 10.

- policy.py:   load .knowledge/policies/<domain>/policy.yaml
- examples.py: pin / load / select calibration examples
- semantic.py: build prompt, call Claude (subprocess by default), parse response
"""

from gateway.filter.examples import Example, examples_dir, load_all, pin, select
from gateway.filter.policy import Policy, PolicyError, load_policy, policy_exists, policy_path
from gateway.filter.semantic import (
    ClaudeCLIFilterClient,
    FilterClient,
    FilterError,
    FilterResult,
    build_prompt,
    parse_response,
    score,
)

__all__ = [
    "ClaudeCLIFilterClient",
    "Example",
    "FilterClient",
    "FilterError",
    "FilterResult",
    "Policy",
    "PolicyError",
    "build_prompt",
    "examples_dir",
    "load_all",
    "load_policy",
    "parse_response",
    "pin",
    "policy_exists",
    "policy_path",
    "score",
    "select",
]
