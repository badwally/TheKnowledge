"""Librarian Phase 2 (T5) — per-namespace embedding adequacy gate (I2).

Each namespace ships its own golden set under .knowledge/eval/embedding/ and an
independently-falsifiable gate. The active lexical fallback must pass its own
(accurately weak) gate OR be marked active+falsifiable. The falsifiability probe is
adversarial: flipping a golden label must FLIP the gate verdict — a gate that
passes regardless of labels is a rubber stamp and a defect.
"""

from __future__ import annotations

import pytest

from gateway.evaluate.embedding_eval import (
    NamespaceGateReport,
    evaluate_all,
    evaluate_namespace,
)
from gateway.embedding_index import LexicalFallbackEncoder


# The eval reads the real on-disk golden sets under the repo's .knowledge/.
# No KNOWLEDGE_ROOT override — these goldens are repo fixtures.


@pytest.mark.parametrize("namespace", ["section", "entity", "question"])
def test_namespace_gate_passes_or_fallback_active_and_falsifiable(namespace):
    report = evaluate_namespace(namespace)
    assert isinstance(report, NamespaceGateReport)
    assert report.model_version == "lexical-fallback-v1"
    # I2: the gate passes against its golden OR the named fallback is
    # active AND falsifiable.
    assert report.passed or (report.fallback_active and report.fallback_falsifiable), \
        report.summary()
    # And it is falsifiable — not a rubber stamp.
    assert report.fallback_falsifiable, "gate must fail on a flipped golden label"


@pytest.mark.parametrize("namespace", ["section", "question"])
def test_lexical_fallback_clears_easy_namespaces(namespace):
    """The active lexical fallback clears its operating point on the section and
    question namespaces (their goldens are within lexical reach). The entity
    namespace is intentionally NOT here — its hard identity pairs (Phase-3) are
    beyond lexical reach, so it rides the active+falsifiable fallback (I2)."""
    report = evaluate_namespace(namespace)
    assert report.passed, report.summary()


@pytest.mark.parametrize("namespace", ["section", "entity", "question"])
def test_gate_is_falsifiable_flip_label_fails(namespace):
    """Adversarial: with a flipped golden label the metric drops below floor.

    Exercised via the report's `fallback_falsifiable` flag, which re-scores a
    one-label-flipped copy of the golden and asserts it falls below the floor.
    A gate that passes regardless of labels would set this False → test fails.
    """
    report = evaluate_namespace(namespace)
    assert report.fallback_falsifiable, (
        f"{namespace}: flipping one golden label did NOT drop the metric below "
        "the floor — the gate is not falsifiable (rubber stamp)."
    )


def test_evaluate_all_three_namespaces():
    reports = evaluate_all()
    assert set(reports) == {"section", "entity", "question"}
    for ns, r in reports.items():
        assert r.namespace == ns
        # Every namespace either clears its gate OR rides the active+falsifiable
        # fallback (entity, by design — see I2).
        assert r.passed or (r.fallback_active and r.fallback_falsifiable), r.summary()


def test_entity_gate_hard_cases_force_alias_authority_fallback():
    """ENTRY GATE 1a: with hard identity pairs, the lexical-fallback encoder
    cannot hit precision 1.0 by NN geometry, so the alias-authority fallback
    is active and falsifiable (I2). The gate must not 'pass' in dead space."""
    report = evaluate_namespace("entity")
    assert report.metric == "precision"
    # The honest outcome: embedding geometry is inadequate on hard identity, so
    # the named fallback is active. (If a future neural encoder passes outright,
    # report.passed is True and this is also acceptable.)
    assert report.passed or (report.fallback_active and report.fallback_falsifiable), report.summary()
    if not report.passed:
        # Prove fitness is NOT being claimed in dead space: the encoder is below
        # floor on the hardened set (the gate is falsifiable, not vacuous).
        assert report.value < report.floor, report.summary()


def test_forced_encoder_failure_makes_gate_unfalsifiable_or_fail():
    """Negative control: a degenerate encoder that maps every text to the same
    vector cannot distinguish merge from no-merge → the entity gate FAILS (its
    precision drops below floor). Proves the gate measures the encoder, not a
    constant."""

    class _ConstantEncoder(LexicalFallbackEncoder):
        def embed(self, texts):
            # every text -> identical unit vector
            return [[1.0] + [0.0] * (self.dim - 1) for _ in texts]

    report = evaluate_namespace("entity", encoder=_ConstantEncoder())
    # With every distance == 0, every pair predicts "merge" → no-merge pairs are
    # all wrong → precision < 1.0 → gate fails.
    assert not report.passed, report.summary()
