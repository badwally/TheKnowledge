"""Bake-off scorer for Hole-2 retrieval configs. Scores a config on the probe
through the REAL hybrid retrieve path (recall + placeholder-leak control)."""
from __future__ import annotations

from pathlib import Path

import yaml

from gateway.ops import retrieve as retr

_LEAK_NEEDLES = ("needs population from legacy import", "summary not yet generated",
                 "claims not yet extracted", "no cross-references yet", "no citations returned")


def score_config(goldens_path: str, k: int = 10) -> dict:
    queries = yaml.safe_load(Path(goldens_path).read_text())["queries"]
    hits = leaks = 0
    for e in queries:
        block, sections = retr.retrieve(e["q"], domain=e.get("domain"), k=k, hybrid=True)
        slugs = [s.slug for s in sections]
        hits += any(x in slugs for x in e["expect"])
        leaks += sum(block.count(n) for n in _LEAK_NEEDLES)
    n = len(queries)
    return {"recall_at_k": hits / n if n else 0.0, "placeholder_leaks": leaks, "n": n}
