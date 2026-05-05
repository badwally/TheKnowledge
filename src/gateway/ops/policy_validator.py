"""Strict + lenient policy validation for bootstrap-domain and legacy load.

Strict mode runs on output of `wiki bootstrap-domain` to prevent vague or
under-specified policies from entering the system. Lenient mode runs on
existing policy load (e.g. `wiki research`) so legacy auto-generated
policies (M36 promote-domain) keep working without modification.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re


REFERENCE_POLICY_PATH = Path(__file__).parent / "_bootstrap_reference_policy.yaml"

POLICY_SCHEMA_VERSION = 1

_MIN_INCLUSION = 3
_MIN_EXCLUSION = 1
_MIN_QUALITY_CATEGORIES = 2
_MIN_SIGNALS_PER_CATEGORY = 2

_KNOWN_TOP_LEVEL = {
    "version",
    "policy_schema_version",
    "domain",
    "filter",
    "inclusion_criteria",
    "exclusion_criteria",
    "quality_signals",
    "auto_generated",
    "auto_generated_from_proposal",
    "bootstrapped_from_description_hash",
}

_SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class PolicyValidationError(ValueError):
    """Raised by callers that want exception-shaped failures."""


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_policy(data: dict, *, mode: str = "lenient") -> ValidationResult:
    """Validate a policy mapping.

    `mode="strict"` enforces minimum specificity (used for bootstrap output).
    `mode="lenient"` runs only structural checks (used for legacy policy load).
    """
    if mode not in ("strict", "lenient"):
        raise ValueError(f"unknown validation mode: {mode!r}")

    result = ValidationResult()

    if not isinstance(data, dict):
        result.errors.append(f"policy must be a YAML mapping, got {type(data).__name__}")
        return result

    unknown = set(data.keys()) - _KNOWN_TOP_LEVEL
    if unknown:
        for key in sorted(unknown):
            result.errors.append(f"unknown top-level key: {key!r}")

    domain = data.get("domain") or {}
    if not isinstance(domain, dict):
        result.errors.append(f"`domain` must be a mapping, got {type(domain).__name__}")
    else:
        slug = domain.get("slug")
        if not isinstance(slug, str) or not slug:
            result.errors.append("`domain.slug` is required and must be a non-empty string")
        elif not _SLUG_RE.match(slug):
            result.errors.append(
                f"`domain.slug` {slug!r} is not a valid slug (lowercase, hyphenated)"
            )
        for k in ("topic", "field", "description"):
            v = domain.get(k)
            if not isinstance(v, str):
                result.errors.append(f"`domain.{k}` must be a string")

    filter_cfg = data.get("filter") or {}
    if not isinstance(filter_cfg, dict):
        result.errors.append(f"`filter` must be a mapping, got {type(filter_cfg).__name__}")
    else:
        for k in ("threshold_include", "threshold_review"):
            v = filter_cfg.get(k)
            if v is None:
                continue
            try:
                f = float(v)
            except (TypeError, ValueError):
                result.errors.append(f"`filter.{k}` must be numeric, got {v!r}")
                continue
            if not 0.0 <= f <= 1.0:
                result.errors.append(f"`filter.{k}` must be in [0.0, 1.0], got {f}")

    inclusion = data.get("inclusion_criteria") or []
    exclusion = data.get("exclusion_criteria") or []
    if not isinstance(inclusion, list):
        result.errors.append("`inclusion_criteria` must be a list")
    if not isinstance(exclusion, list):
        result.errors.append("`exclusion_criteria` must be a list")

    quality_signals = data.get("quality_signals") or {}
    if not isinstance(quality_signals, dict):
        result.errors.append("`quality_signals` must be a mapping")

    if mode == "strict":
        if isinstance(inclusion, list) and len(inclusion) < _MIN_INCLUSION:
            result.errors.append(
                f"`inclusion_criteria` must have at least {_MIN_INCLUSION} items, got {len(inclusion)}"
            )
        if isinstance(exclusion, list) and len(exclusion) < _MIN_EXCLUSION:
            result.errors.append(
                f"`exclusion_criteria` must have at least {_MIN_EXCLUSION} items, got {len(exclusion)}"
            )
        if isinstance(quality_signals, dict):
            categories = [
                k for k, v in quality_signals.items() if isinstance(v, dict)
            ]
            if len(categories) < _MIN_QUALITY_CATEGORIES:
                result.errors.append(
                    f"`quality_signals` must have at least {_MIN_QUALITY_CATEGORIES} categories"
                    f", got {len(categories)}"
                )
            for cat in categories:
                cat_data = quality_signals[cat]
                signals = []
                for key in ("positive_signals", "negative_signals"):
                    sig = cat_data.get(key) or []
                    if isinstance(sig, list):
                        signals.extend(sig)
                if len(signals) < _MIN_SIGNALS_PER_CATEGORY:
                    result.errors.append(
                        f"`quality_signals.{cat}` must have at least "
                        f"{_MIN_SIGNALS_PER_CATEGORY} total signals, got {len(signals)}"
                    )
        version = data.get("policy_schema_version")
        if version != POLICY_SCHEMA_VERSION:
            result.errors.append(
                f"`policy_schema_version` must be {POLICY_SCHEMA_VERSION}, got {version!r}"
            )
    else:  # lenient
        if "policy_schema_version" not in data:
            result.warnings.append("policy missing `policy_schema_version` (legacy)")

    return result
