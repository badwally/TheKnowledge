"""Dedup adjudicator determinism / replay (I1).

The serial commit phase must be replayable: the same logged inputs produce the
same verdict, independent of candidate ordering. The verdict basis must be
JSON-serializable so it can be recorded into provenance.
"""

from __future__ import annotations

from gateway.dedup import adjudicate, DepositIdentity, Candidate


def test_same_inputs_same_verdict_replay():
    ident = DepositIdentity("drug", "Ozempic", ("Semaglutide",), ("med",))
    cands = [
        Candidate("semaglutide", "drug", "Semaglutide", ("Ozempic",), ("med",), 1.0),
        Candidate("tirzepatide", "drug", "Tirzepatide", (), ("med",), 0.4),
    ]
    v1 = adjudicate(ident, cands, blocking_band=0.15, identity_threshold=0.30)
    # Re-run with candidates in a DIFFERENT order — deterministic sort must yield
    # the identical verdict (the serial commit phase must be replayable, I1).
    v2 = adjudicate(ident, list(reversed(cands)), blocking_band=0.15, identity_threshold=0.30)
    assert (v1.decision, v1.target_slug, v1.rule) == (v2.decision, v2.target_slug, v2.rule)
    assert v1.decision == "merge"


def test_verdict_basis_is_json_serializable_for_provenance():
    import json
    ident = DepositIdentity("concept", "A")
    v = adjudicate(ident, [Candidate("b", "concept", "B", (), ("x",), 0.5)],
                   blocking_band=0.15, identity_threshold=0.30)
    json.dumps(v.basis)  # must not raise — basis is logged into provenance
