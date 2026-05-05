"""Tests for the strict/lenient policy validator (M39 bootstrap-domain)."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway.ops.policy_validator import (
    PolicyValidationError,
    REFERENCE_POLICY_PATH,
    validate_policy,
)


def _load_reference() -> dict:
    return yaml.safe_load(REFERENCE_POLICY_PATH.read_text())


def test_reference_policy_passes_strict_validation():
    """Round-trip guarantee: schema additions break this test until the reference is updated."""
    data = _load_reference()
    result = validate_policy(data, mode="strict")
    assert result.ok, [str(e) for e in result.errors]


def test_strict_rejects_missing_inclusion_criteria():
    data = _load_reference()
    data["inclusion_criteria"] = []
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("inclusion_criteria" in str(e) for e in result.errors)


def test_strict_rejects_too_few_inclusion_criteria():
    data = _load_reference()
    data["inclusion_criteria"] = ["only one"]
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("at least 3" in str(e).lower() for e in result.errors)


def test_strict_rejects_missing_exclusion_criteria():
    data = _load_reference()
    data["exclusion_criteria"] = []
    result = validate_policy(data, mode="strict")
    assert not result.ok


def test_strict_rejects_too_few_quality_signals():
    data = _load_reference()
    data["quality_signals"] = {"only_one_category": {"positive_signals": ["x", "y"]}}
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("quality_signals" in str(e).lower() for e in result.errors)


def test_strict_rejects_threshold_out_of_range():
    data = _load_reference()
    data["filter"]["threshold_include"] = 1.5
    result = validate_policy(data, mode="strict")
    assert not result.ok


def test_strict_rejects_invalid_slug():
    data = _load_reference()
    data["domain"]["slug"] = "BadSlug"
    result = validate_policy(data, mode="strict")
    assert not result.ok


def test_strict_rejects_unknown_top_level_keys():
    data = _load_reference()
    data["mystery_field"] = "lurking"
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("unknown" in str(e).lower() and "mystery_field" in str(e) for e in result.errors)


def test_lenient_allows_empty_inclusion_criteria():
    """Legacy auto-generated policies have empty criteria; must keep loading."""
    data = _load_reference()
    data["inclusion_criteria"] = []
    data["exclusion_criteria"] = []
    result = validate_policy(data, mode="lenient")
    assert result.ok, [str(e) for e in result.errors]


def test_lenient_allows_missing_schema_version():
    data = _load_reference()
    data.pop("policy_schema_version", None)
    result = validate_policy(data, mode="lenient")
    assert result.ok
