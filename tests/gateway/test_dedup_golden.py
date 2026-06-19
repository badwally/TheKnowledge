"""Adjudicator scored against the independent dedup golden (§16 I3).

The golden is human-curated and judges the adjudicator's decision directly, not
embedding geometry. A geometry-only merger MUST mis-score it (falsifiability).
"""

from __future__ import annotations

import yaml

from gateway import paths
from gateway.dedup import adjudicate, DepositIdentity, Candidate


def _load():
    p = paths.knowledge_root() / ".knowledge/eval/dedup/golden.yaml"
    return yaml.safe_load(p.read_text())["cases"]


def test_adjudicator_scores_dedup_golden_at_precision_1():
    wrong = []
    for case in _load():
        a, b = case["a"], case["b"]
        ident = DepositIdentity(a["entity_kind"], a["canonical_name"],
                                tuple(a.get("aliases", [])), tuple(a.get("domains", [])))
        cand = Candidate(b["slug"], b["entity_kind"], b["canonical_name"],
                         tuple(b.get("aliases", [])), tuple(b.get("domains", [])), b["nn_distance"])
        v = adjudicate(ident, [cand], blocking_band=0.15, identity_threshold=0.30)
        if v.decision != case["expect"]:
            wrong.append((case["name"], case["expect"], v.decision, v.rule))
    assert not wrong, f"dedup golden mis-scored: {wrong}"


def test_golden_is_falsifiable_a_broken_adjudicator_fails():
    # A geometry-only "adjudicator" (merge iff nn<=0.30) MUST mis-score the golden —
    # proving the golden actually tests the alias-authority discipline, not a tautology.
    def geometry_only(ident, cand):
        return "merge" if cand.nn_distance <= 0.30 else "distinct"
    mismatches = 0
    for case in _load():
        b = case["b"]
        got = geometry_only(case["a"], Candidate(b["slug"], b["entity_kind"], b["canonical_name"],
                            tuple(b.get("aliases", [])), tuple(b.get("domains", [])), b["nn_distance"]))
        if got != case["expect"]:
            mismatches += 1
    assert mismatches >= 2, "golden must punish a geometry-only merger (Type1/Type2, Fed branches)"
