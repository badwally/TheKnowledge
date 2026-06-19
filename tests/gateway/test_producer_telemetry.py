from __future__ import annotations

from gateway import provenance
from gateway.provenance import ProducerTelemetry


def _fired(alarms, name):
    return {a["identity"] for a in alarms if a["alarm"] == name}


def test_rejection_spike_fires():
    t = ProducerTelemetry()
    for _ in range(8):
        t.incr("bad-agent", "reject")
    for _ in range(2):
        t.incr("bad-agent", "accept")
    alarms = provenance.alarms(t.snapshot())
    assert "bad-agent" in _fired(alarms, "rejection-spike")


def test_dedup_merge_spike_fires():
    t = ProducerTelemetry()
    for _ in range(9):
        t.incr("stale-agent", "merge")
    t.incr("stale-agent", "accept")
    alarms = provenance.alarms(t.snapshot())
    assert "stale-agent" in _fired(alarms, "dedup-merge-spike")


def test_deposit_silence_fires():
    prev = ProducerTelemetry()
    for _ in range(10):
        prev.incr("was-active", "accept")
    prev_snap = prev.snapshot()
    # current: identical totals -> no new activity since prev -> silence
    cur = ProducerTelemetry()
    for _ in range(10):
        cur.incr("was-active", "accept")
    alarms = provenance.alarms(cur.snapshot(), prev_snapshot=prev_snap)
    assert "was-active" in _fired(alarms, "deposit-silence")


def test_healthy_traffic_fires_nothing_negative_control():
    t = ProducerTelemetry()
    for _ in range(20):
        t.incr("good-agent", "accept")
    for _ in range(2):
        t.incr("good-agent", "reject")
    for _ in range(1):
        t.incr("good-agent", "merge")
    # prev with strictly less activity -> not silent
    prev = ProducerTelemetry()
    for _ in range(5):
        prev.incr("good-agent", "accept")
    alarms = provenance.alarms(t.snapshot(), prev_snapshot=prev.snapshot())
    assert alarms == []


def test_low_volume_does_not_trip_spikes_negative_control():
    """A producer below min_volume cannot trip a spike alarm (noise suppression)."""
    t = ProducerTelemetry()
    t.incr("new-agent", "reject")
    t.incr("new-agent", "merge")
    assert provenance.alarms(t.snapshot()) == []
