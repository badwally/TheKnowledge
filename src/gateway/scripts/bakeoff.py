"""Bake-off scorer for Hole-2 retrieval configs. Scores a config on the probe
through the REAL hybrid retrieve path (recall + placeholder-leak control)."""
from __future__ import annotations

import json
import os
import time
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


def time_config(sample_queries: list[tuple[str, str | None]]) -> dict:
    times = []
    for q, dom in sample_queries:
        t0 = time.perf_counter()
        retr.retrieve(q, domain=dom, hybrid=True)
        times.append((time.perf_counter() - t0) * 1000.0)
    times.sort()

    def pct(p: float) -> float:
        return times[min(len(times) - 1, int(p * len(times)))] if times else 0.0

    return {"query_ms_p50": pct(0.5), "query_ms_p90": pct(0.9)}


def run_sweep(configs: list[dict], goldens_path: str, sample_queries: list[tuple[str, str | None]], k: int = 10) -> list[dict]:
    """Primary sweep axis is encoder identity + truncation dim (the WIKI_RETRIEVAL_ENCODER
    spec). RRF k_rrf is secondary; if the frontier is close, thread k_rrf through
    retrieve()->_hybrid_hits->_rrf_fuse in a follow-up and add it to the matrix then."""
    from gateway.retrieval_index import retrieval_index

    rows = []
    for cfg in configs:
        os.environ["WIKI_RETRIEVAL_ENCODER"] = cfg["encoder"]
        retrieval_index().rebuild_from_canonical()
        sc = score_config(goldens_path, k=k)
        tm = time_config(sample_queries)
        rows.append({"config": cfg, **sc, **tm})
    return rows


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--goldens", default=".knowledge/eval/retrieval/semantic_mismatch.yaml")
    ap.add_argument("--k", type=int, default=10)
    args = ap.parse_args()
    qs = [(e["q"], e.get("domain")) for e in yaml.safe_load(open(args.goldens))["queries"]]
    # Production sweep configs are edited here before a real run (see Task C3).
    configs = [{"encoder": os.environ.get("WIKI_RETRIEVAL_ENCODER", "stub"), "k_rrf": 60}]
    rows = run_sweep(configs, args.goldens, qs, k=args.k)
    print(json.dumps(rows, indent=2))
