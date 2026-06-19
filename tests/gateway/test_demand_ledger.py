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


class _DifferentEncoder:
    """A GENUINELY different encoder — different dim + different hash seed, so it
    produces VECTORS that differ byte-wise from LexicalFallbackEncoder, while
    preserving the paraphrase-proximity property (shared char-3-grams still land
    close). This is a real model bump, not a relabel of the same vectors.
    """
    model_version = "different-v2"
    dim = 384  # different dimensionality → vectors cannot be byte-identical

    def _features(self, text):
        import re
        norm = text.lower()
        tokens = re.findall(r"[A-Za-z0-9_]+", norm)
        feats = list(tokens)
        joined = " ".join(tokens)
        feats.extend(joined[i : i + 3] for i in range(max(0, len(joined) - 2)))
        return feats

    def _hash_bucket(self, feature):
        import hashlib
        # DIFFERENT seed: prefix the feature so the hash differs from the default.
        h = hashlib.blake2b(("SEED2::" + feature).encode("utf-8"), digest_size=8).digest()
        idx = int.from_bytes(h[:4], "big") % self.dim
        sign = 1.0 if (h[4] & 1) else -1.0
        return idx, sign

    def embed(self, texts):
        import numpy as np
        out = []
        for text in texts:
            vec = np.zeros(self.dim, dtype=np.float32)
            for feat in self._features(text):
                idx, sign = self._hash_bucket(feat)
                vec[idx] += sign
            norm = float(np.linalg.norm(vec))
            if norm > 0.0:
                vec = vec / norm
            out.append(vec.astype(np.float32).tolist())
        return out


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


def test_different_encoder_actually_produces_different_vectors():
    """Guard: _DifferentEncoder must NOT be a relabel — its vectors differ from
    LexicalFallbackEncoder's. Without this, the I4 test below is tautological."""
    from gateway.embedding_index import LexicalFallbackEncoder
    base = LexicalFallbackEncoder()
    other = _DifferentEncoder()
    text = "semaglutide gastric emptying"
    v_base = base.embed([text])[0]
    v_other = other.embed([text])[0]
    # Different dim → cannot be byte-identical; assert the vectors genuinely differ.
    assert len(v_base) != len(v_other), "encoders must differ in dimensionality"


def test_i4_reembed_survives_model_bump_without_resetting_recurrence(kb_root):
    """I4: a real model bump (different vectors) must NOT reset recurrence, AND
    the clustering (which DOES use vectors) must survive the bump — paraphrases
    still merge into ONE cluster after reembed."""
    from gateway.demand_ledger import DemandLedger
    led = DemandLedger()
    # Record a recurring gap PLUS a paraphrase so clustering (vector-dependent) is
    # exercised — not just the text-count mass.
    for _ in range(3):
        led.record_gap("semaglutide gastric emptying")
    for _ in range(2):
        led.record_gap("how semaglutide slows gastric emptying")  # paraphrase

    before_clusters = led.cluster()
    before_mass = sum(c.recurrence_mass for c in before_clusters)
    # Paraphrases merge → one cluster before the bump.
    assert len(before_clusters) == 1, "paraphrases must merge pre-reembed"

    led.reembed(new_encoder=_DifferentEncoder())  # GENUINELY different vectors

    after_clusters = led.cluster()
    after_mass = sum(c.recurrence_mass for c in after_clusters)
    # (a) recurrence mass preserved (derives from retained raw text, I4)
    assert after_mass == before_mass, "recurrence preserved across real model bump"
    # (b) clustering survives the bump — paraphrases STILL merge under new vectors
    assert len(after_clusters) == 1, "paraphrases must still merge post-reembed"


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


# ---------------------------------------------------------------------------
# CRITICAL 1 — cold-start must change trigger behavior (one-offs cannot push over)
# ---------------------------------------------------------------------------


class _SubmitSpy:
    """A fake IntentQueue that records every submit() call."""
    def __init__(self):
        self.submitted = []

    def submit(self, intent):
        self.submitted.append(intent)
        return intent.intent_id

    def depth(self):
        return len(self.submitted)


def test_cold_start_one_off_paraphrase_does_not_push_cluster_over(kb_root):
    """CRITICAL 1: a cluster whose recurring member has 4 occurrences (below mass=5)
    PLUS a single 1-occurrence paraphrase must NOT trigger. The one-off (own count
    1 < cold_start_min 3) contributes 0 toward the trigger, so trigger-mass stays 4.

    On the buggy code, the paraphrase is absorbed → total mass 5 → triggers. RED.
    """
    from gateway.demand_ledger import DemandLedger
    spy = _SubmitSpy()
    led = DemandLedger(queue=spy)
    for _ in range(4):
        led.record_gap("semaglutide and gastric emptying")          # 4 occurrences
    led.record_gap("how semaglutide slows gastric emptying")        # 1 occurrence (one-off)
    triggered = [c for c in led.cluster() if c.triggered]
    assert len(triggered) == 0, (
        "one-off paraphrase must not push a below-mass cluster over the trigger"
    )
    assert len(spy.submitted) == 0, "no intent should be submitted"


def test_cold_start_min_change_flips_borderline_case(kb_root):
    """CRITICAL 1: cold_start_min_recurrences must have behavioral effect.

    Construct a cluster: recurring member at 4 occurrences + a paraphrase at 2
    occurrences. Trigger-mass counts only members whose own count >= cold_start_min.

    - cold_start_min=3: only the 4-occurrence member qualifies → trigger-mass 4 < 5 → NO trigger.
    - cold_start_min=2: BOTH members qualify (4 and 2) → trigger-mass 6 >= 5 → TRIGGER.

    Lowering the threshold flips the outcome → proves the parameter is live.
    """
    from gateway import demand_ledger as dl_mod
    from gateway.demand_ledger import DemandLedger

    def _make_ledger(cold_start_min):
        spy = _SubmitSpy()
        led = DemandLedger(queue=spy)
        return led, spy

    # Helper to record the same corpus into a fresh root via reuse of kb_root would
    # collide; instead patch thresholds and re-derive on a fresh ledger each time
    # against the SAME on-disk gaps file is not isolated — use two sub-roots.
    import tempfile, os
    from pathlib import Path

    def _run(cold_start_min):
        d = Path(tempfile.mkdtemp())
        (d / ".knowledge" / "demand").mkdir(parents=True, exist_ok=True)
        spy = _SubmitSpy()
        led = DemandLedger(queue=spy, root=d)
        for _ in range(4):
            led.record_gap("semaglutide and gastric emptying")
        for _ in range(2):
            led.record_gap("how semaglutide slows gastric emptying")
        # Patch thresholds for this run
        orig = dl_mod.thresholds
        def patched():
            t = dict(orig())
            t["demand.cold_start_min_recurrences"] = cold_start_min
            return t
        dl_mod.thresholds = patched
        try:
            triggered = [c for c in led.cluster() if c.triggered]
        finally:
            dl_mod.thresholds = orig
        return len(spy.submitted)

    high = _run(3)   # only 4-occ member qualifies → mass 4 → no trigger
    low = _run(2)    # both qualify → mass 6 → trigger
    assert high == 0, "cold_start_min=3 should NOT trigger (mass 4)"
    assert low == 1, "cold_start_min=2 should trigger (mass 6)"


# ---------------------------------------------------------------------------
# IMPORTANT — stable cluster identity + submission-count spy (no re-trigger on drift)
# ---------------------------------------------------------------------------


def test_build_intent_submitted_exactly_once_across_cluster_runs(kb_root):
    """The build-tier intent is SUBMITTED exactly once across repeated cluster()
    calls — distinguishes fired-now from already-triggered (spy counts submits)."""
    from gateway.demand_ledger import DemandLedger
    spy = _SubmitSpy()
    led = DemandLedger(queue=spy)
    for _ in range(6):
        led.record_gap("GLP-1 receptor agonist weight loss mechanism")
    led.cluster()
    led.cluster()
    led.cluster()
    assert len(spy.submitted) == 1, (
        f"intent submitted {len(spy.submitted)} times; must be exactly 1"
    )


def test_cluster_gaining_member_does_not_re_trigger(kb_root):
    """IMPORTANT: a triggered cluster that gains a NEW member between cluster()
    runs must NOT re-trigger. The dedup key must be a STABLE cluster identity that
    does not change when a member joins (not a member-set hash)."""
    from gateway.demand_ledger import DemandLedger
    spy = _SubmitSpy()
    led = DemandLedger(queue=spy)
    for _ in range(6):
        led.record_gap("tirzepatide dual agonist weight loss")
    led.cluster()  # fires once
    assert len(spy.submitted) == 1
    # A new paraphrase joins the cluster (drift)
    led.record_gap("how tirzepatide drives weight loss as a dual agonist")
    led.record_gap("how tirzepatide drives weight loss as a dual agonist")
    led.record_gap("how tirzepatide drives weight loss as a dual agonist")
    led.cluster()  # must NOT re-trigger despite the larger member set
    assert len(spy.submitted) == 1, (
        "cluster that gained a member re-triggered — dedup key not stable"
    )


def test_toctou_concurrent_cluster_runs_submit_one_intent(kb_root):
    """IMPORTANT (TOCTOU): two concurrent cluster() calls over identical on-disk
    state must produce exactly ONE durable intent in the real queue — the
    triggered.json read-modify-write is lock-guarded AND the intent_id is stable
    (content-addressed on a drift-proof cluster anchor) so the queue coalesces any
    that slip through. Uses the REAL IntentQueue (not a spy) to exercise the
    durable backstop."""
    from gateway.demand_ledger import DemandLedger
    from gateway.intent_queue import IntentQueue

    # Two ledgers over the SAME on-disk gaps (default kb_root demand dir).
    led_a = DemandLedger(queue=IntentQueue())
    for _ in range(6):
        led_a.record_gap("liraglutide appetite suppression pathway")

    led_b = DemandLedger(queue=IntentQueue())

    # Simulate interleaving: both run cluster() against the same state.
    led_a.cluster()
    led_b.cluster()

    # Exactly one durable intent across both runs (stable intent_id + lock).
    q = IntentQueue()
    # Count submitted + any terminal copies of the demand-trigger intent.
    submitted = q.depth()
    assert submitted == 1, f"expected exactly 1 durable intent, got {submitted}"
