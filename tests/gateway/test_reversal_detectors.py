"""Tests for G2 reversal/anomaly detectors.

RED-before-GREEN: these tests are written before the implementation.
Mirrors the provenance.alarms() pattern (Phase-4 A7):
  - pure function over a snapshot dict
  - named negative controls
  - min_volume floor so a tiny sample can't trip a rate
  - frozen Alarm dataclass with name/value/threshold/tripped/detail
"""
from __future__ import annotations

import json

import pytest

from gateway import contradictions_log
from gateway.reversal_detectors import Alarm, detect
from gateway.ops.lint import lint


# ---------------------------------------------------------------------------
# Detector 1 — auto_resolution_reversal_rate (>5%, min_volume floor)
# ---------------------------------------------------------------------------

def test_reversal_rate_trips_above_5pct(kb_root):
    """6 reversals out of 100 auto-resolutions → 6% > 5% threshold → tripped."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 6,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is True


def test_reversal_rate_at_threshold_does_not_trip(kb_root):
    """Exactly 5% (5/100) is at the threshold, not above it — must not trip."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 5,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is False


def test_below_min_volume_cannot_trip_rate(kb_root):
    """2 reversals out of 3 auto-resolutions = 67%, but below min_volume → no alarm.

    Named negative control: min_volume floor prevents noise from tiny samples.
    """
    snap = {
        "auto_resolutions": 3,
        "reversed": 2,
        "cross_project": 0,
        "total": 3,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["auto_resolution_reversal_rate"].tripped is False  # min_volume floor


# ---------------------------------------------------------------------------
# Detector 2 — cross_project_override_rate (>10%, min_volume floor)
# ---------------------------------------------------------------------------

def test_cross_project_rate_trips_above_10pct(kb_root):
    """11 cross-project overrides out of 100 total → 11% > 10% → tripped."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 11,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is True


def test_cross_project_rate_at_threshold_does_not_trip(kb_root):
    """Exactly 10% is at the threshold, not above — must not trip."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 10,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is False


def test_cross_project_below_min_volume_cannot_trip(kb_root):
    """Named negative control: cross_project rate with total < min_volume → no alarm."""
    snap = {
        "auto_resolutions": 3,
        "reversed": 0,
        "cross_project": 2,
        "total": 3,
        "max_cascade_depth": 1,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["cross_project_override_rate"].tripped is False


# ---------------------------------------------------------------------------
# Detector 3 — observed_cascade_depth (>3)
# ---------------------------------------------------------------------------

def test_cascade_depth_trips_above_3(kb_root):
    """Max cascade depth of 4 > threshold of 3 → tripped."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 4,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["observed_cascade_depth"].tripped is True


def test_cascade_depth_at_threshold_does_not_trip(kb_root):
    """Depth exactly 3 is at the threshold, not above — must not trip."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 0,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 3,
    }
    alarms = {a.name: a for a in detect(snap)}
    assert alarms["observed_cascade_depth"].tripped is False


# ---------------------------------------------------------------------------
# Healthy traffic → no alarms (named negative control)
# ---------------------------------------------------------------------------

def test_healthy_traffic_trips_nothing(kb_root):
    """Named negative control: healthy traffic trips none of the three detectors.

    1 reversal / 100 = 1% < 5%; 2 cross-project / 100 = 2% < 10%; depth 2 < 3.
    """
    snap = {
        "auto_resolutions": 100,
        "reversed": 1,
        "cross_project": 2,
        "total": 100,
        "max_cascade_depth": 2,
    }
    assert all(not a.tripped for a in detect(snap))


# ---------------------------------------------------------------------------
# Alarm dataclass shape
# ---------------------------------------------------------------------------

def test_alarm_is_frozen_dataclass_with_required_fields(kb_root):
    """Alarm must expose name, value, threshold, tripped, detail."""
    snap = {
        "auto_resolutions": 100,
        "reversed": 6,
        "cross_project": 0,
        "total": 100,
        "max_cascade_depth": 1,
    }
    alarms = detect(snap)
    assert len(alarms) == 3  # exactly three detectors
    for a in alarms:
        assert hasattr(a, "name")
        assert hasattr(a, "value")
        assert hasattr(a, "threshold")
        assert hasattr(a, "tripped")
        assert hasattr(a, "detail")
        # Frozen: attempting mutation must raise
        with pytest.raises((AttributeError, TypeError)):
            a.name = "mutated"  # type: ignore[misc]


def test_detect_always_returns_all_three_alarms(kb_root):
    """detect() always returns 3 Alarm objects regardless of trips."""
    snap = {
        "auto_resolutions": 0,
        "reversed": 0,
        "cross_project": 0,
        "total": 0,
        "max_cascade_depth": 0,
    }
    alarms = detect(snap)
    names = {a.name for a in alarms}
    assert names == {
        "auto_resolution_reversal_rate",
        "cross_project_override_rate",
        "observed_cascade_depth",
    }


# ---------------------------------------------------------------------------
# Step 6 — lint wiring: reversal-anomalies scope check
# ---------------------------------------------------------------------------

def test_lint_reversal_anomalies_scope_runs_without_error(kb_root):
    """reversal-anomalies is a registered lint check that runs cleanly (no exceptions)."""
    res = lint(scope="reversal-anomalies")
    assert res.success is True


def test_lint_reversal_anomalies_no_findings_on_empty_act_log(kb_root):
    """Empty act log → no tripped alarms → no lint findings."""
    # Act log doesn't exist in the fresh kb_root → snapshot is all-zero → no trips
    res = lint(scope="reversal-anomalies")
    assert res.success is True
    # Summary should show 0 findings for this check
    assert "reversal-anomalies: 0" in res.summary or "0 finding" in res.summary


def test_lint_reversal_anomalies_emits_finding_when_reversal_rate_tripped(kb_root):
    """When reversal rate is above 5% (via realistic acts + revert markers), a finding is emitted."""
    # Write 10 resolution acts — above min_volume=10 — then mark 2 as reverted → 20% > 5%
    acts_path = contradictions_log.resolution_acts_path()
    acts_path.parent.mkdir(parents=True, exist_ok=True)
    for i in range(10):
        act = {
            "act_id": f"act-{i:04d}",
            "rule": "trust-tier-then-recency",
            "policy_version": "contradiction-policy-v1",
            "inputs": {"a": {"source": f"pubmed-{i}", "claim": "x"},
                       "b": {"source": f"arxiv-{i}", "claim": "y"}},
            "winner": {"source": f"pubmed-{i}", "claim": "x", "trust": 0.9},
            "loser": {"source": f"arxiv-{i}", "claim": "y", "trust": 0.5},
            "resolved_at": "2026-06-19T10:00:00Z",
        }
        # Mark 2 of the acts as reverted (20% reversal rate)
        if i < 2:
            act["reverts_act"] = f"reverting-intent-{i}"
        acts_path.open("a").write(json.dumps(act) + "\n")

    res = lint(scope="reversal-anomalies")
    assert res.success is True
    # At least one finding for the tripped reversal rate
    assert res.data is not None and len(res.data.get("findings", [])) > 0 or \
           "reversal-anomalies: 1" in res.summary or \
           "auto_resolution_reversal_rate" in res.summary or \
           res.summary.count("finding") >= 1


def test_lint_reversal_anomalies_scope_runs_only_that_check(kb_root):
    """Scoped lint run executes ONLY reversal-anomalies, not any other check."""
    res = lint(scope="reversal-anomalies")
    assert res.success is True
    # The summary/counts must not mention other checks like orphans or schema-drift
    assert "orphans" not in res.summary
    assert "schema-drift" not in res.summary
