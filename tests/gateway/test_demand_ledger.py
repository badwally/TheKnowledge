"""Tests for DemandLedger (Task 4: DemandLedger + canonicalization trigger + I4).

TDD — tests written RED first. Step 1 covers demand thresholds via embedding_index.
"""
from __future__ import annotations

import pytest


# ---------------------------------------------------------------------------
# Step 1 — Demand thresholds
# ---------------------------------------------------------------------------


def test_thresholds_has_demand_proximity_radius():
    """embedding_index.thresholds() includes demand.proximity_radius ~0.40."""
    from gateway.embedding_index import thresholds
    t = thresholds()
    assert "demand.proximity_radius" in t, f"keys: {list(t.keys())}"
    # ~0.40 — question band that collapses paraphrases to one cluster
    assert 0.30 <= t["demand.proximity_radius"] <= 0.55


def test_thresholds_has_demand_recurrence_mass():
    """embedding_index.thresholds() includes demand.recurrence_mass == 5."""
    from gateway.embedding_index import thresholds
    t = thresholds()
    assert "demand.recurrence_mass" in t
    assert t["demand.recurrence_mass"] == 5


def test_thresholds_has_demand_cold_start_min_recurrences():
    """embedding_index.thresholds() includes demand.cold_start_min_recurrences == 3."""
    from gateway.embedding_index import thresholds
    t = thresholds()
    assert "demand.cold_start_min_recurrences" in t
    assert t["demand.cold_start_min_recurrences"] == 3


# ---------------------------------------------------------------------------
# Step 5 — DemandLedger clustering + trigger + I4
# ---------------------------------------------------------------------------


class _BumpedEncoder:
    """Stub encoder with a different model_version — simulates a model bump."""
    model_version = "bumped-v2"
    dim = 256

    def embed(self, texts):
        # Use the real lexical fallback under the hood but report different version
        from gateway.embedding_index import LexicalFallbackEncoder
        enc = LexicalFallbackEncoder()
        return enc.embed(texts)


def test_recurring_gap_triggers_exactly_one_canonicalization(kb_root):
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    for _ in range(6):  # >= recurrence_mass(5), past cold-start(3)
        led.record_gap("how does semaglutide affect gastric emptying")
    clusters = [c for c in led.cluster() if c.triggered]
    assert len(clusters) == 1


def test_first_occurrence_logged_not_triggered_cold_start(kb_root):
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    led.record_gap("a brand new gap never seen before")
    assert all(not c.triggered for c in led.cluster())


def test_purity_paraphrases_one_cluster_distinct_two(kb_root):
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    led.record_gap("semaglutide and gastric emptying")
    led.record_gap("how semaglutide slows gastric emptying")   # paraphrase
    led.record_gap("federal reserve interest rate policy")     # distinct
    clusters = led.cluster()
    assert len(clusters) == 2   # paraphrases merge, distinct stays separate


def test_i4_reembed_survives_model_bump_without_resetting_recurrence(kb_root):
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    for _ in range(4):
        led.record_gap("semaglutide gastric emptying")
    before = sum(c.recurrence_mass for c in led.cluster())
    led.reembed(new_encoder=_BumpedEncoder())   # re-cluster from retained raw text
    after = sum(c.recurrence_mass for c in led.cluster())
    assert after == before   # recurrence preserved across re-embed


def test_cold_start_gate_exactly_at_boundary(kb_root):
    """Exactly cold_start_min_recurrences (3) recordings → still not triggered
    (needs recurrence_mass=5 to trigger, but test verifies cold-start threshold
    separates from trigger)."""
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    for _ in range(3):
        led.record_gap("tirzepatide mechanism of action")
    # Not yet at recurrence_mass(5) — no trigger
    assert all(not c.triggered for c in led.cluster())


def test_below_recurrence_mass_negative_control(kb_root):
    """A cluster with 4 recurrences (< mass=5) triggers NONE."""
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    for _ in range(4):
        led.record_gap("insulin resistance and obesity mechanism")
    triggered = [c for c in led.cluster() if c.triggered]
    assert len(triggered) == 0, "below mass must not trigger"


def test_re_running_cluster_does_not_double_trigger(kb_root):
    """Calling cluster() twice does NOT produce two triggers — dedup by cluster."""
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    for _ in range(6):
        led.record_gap("GLP-1 receptor agonist weight loss")
    first = [c for c in led.cluster() if c.triggered]
    second = [c for c in led.cluster() if c.triggered]
    # Both calls see exactly one triggered cluster, not two
    assert len(first) == 1
    assert len(second) == 1


def test_record_gap_returns_gap_record(kb_root):
    """record_gap returns a GapRecord with text and caller fields."""
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    rec = led.record_gap("test question about nutrition", caller="test-caller")
    assert rec.text == "test question about nutrition"
    assert rec.caller == "test-caller"


def test_distinct_gaps_stay_separate_clusters(kb_root):
    """Two completely unrelated topics produce two clusters (purity negative)."""
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    for _ in range(6):
        led.record_gap("machine learning gradient descent optimization")
    for _ in range(6):
        led.record_gap("medieval european agricultural history")
    clusters = led.cluster()
    assert len(clusters) == 2
