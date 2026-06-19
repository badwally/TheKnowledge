"""Tests for G2 reversal/anomaly detectors.

RED-before-GREEN: these tests are written before the implementation.
Mirrors the provenance.alarms() pattern (Phase-4 A7):
  - pure function over a snapshot dict
  - named negative controls
  - min_volume floor so a tiny sample can't trip a rate
  - frozen Alarm dataclass with name/value/threshold/tripped/detail
"""
from __future__ import annotations

import pytest

from gateway.reversal_detectors import Alarm, detect


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
