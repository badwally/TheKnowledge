#!/usr/bin/env python
"""Score the ACTUAL `wiki retrieve` path against a golden set (Hole 1 instrument).

`wiki eval-retrieval` scores the FTS layer; the draft-visibility fix lives in the
retrieve ASSEMBLY (gateway.ops.retrieve), which that harness never exercises. This
script is the reproducible instrument for the retrieve path: it runs each golden
query through `wiki retrieve --json` and reports recall@k plus the two negative
controls from the brief (docs/260622_rag-retrieval-draft-visibility-brief.md,
Appendix B/C).

Usage:
    .venv/bin/python scripts/probe_retrieve.py [--goldens PATH] [--k N]

Gates reported:
    G-POS    recall@k over all queries; the 3 lexically-easy controls must HIT.
    G-NEG-1  count of `_(needs population from legacy import)_` (and the wider
             placeholder family) leaking into assembled blocks — MUST be 0.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

_PLACEHOLDER_NEEDLE = "needs population from legacy import"
# The wider placeholder family (lone italic-parenthetical stub bodies). Any of
# these leaking into a grounding block is stub pollution.
_PLACEHOLDER_FAMILY = [
    "needs population from legacy import",
    "summary not yet generated",
    "claims not yet extracted",
    "no cross-references yet",
    "no citations returned",
]

# The 3 lexically-easy controls (must flip to HIT post-fix) — by query prefix.
_CONTROL_PREFIXES = (
    "Apple Neural Engine on-device inference",
    "federated learning across silos",
    "mesolimbic dopamine system",
)


def _retrieve(query: str, domain: str | None, k: int) -> dict:
    cmd = [".venv/bin/wiki", "retrieve", query, "--k", str(k), "--json"]
    if domain:
        cmd += ["--domain", domain]
    out = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"sources": [], "_stderr": out.stderr[-300:]}


def _block(query: str, domain: str | None, k: int) -> str:
    cmd = [".venv/bin/wiki", "retrieve", query, "--k", str(k)]
    if domain:
        cmd += ["--domain", domain]
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--goldens", default=".knowledge/eval/retrieval/semantic_mismatch.yaml")
    ap.add_argument("--k", type=int, default=10)
    args = ap.parse_args()

    G = yaml.safe_load(Path(args.goldens).read_text())
    queries = G["queries"]

    hits = 0
    control_results: list[tuple[str, bool]] = []
    pollution = 0
    pollution_examples: list[str] = []

    print(f"# probe_retrieve — {args.goldens} (k={args.k})\n")
    for e in queries:
        q, dom, exp = e["q"], e.get("domain"), e["expect"]
        man = _retrieve(q, dom, args.k)
        slugs = [s.get("slug") for s in man.get("sources", [])]
        hit = any(x in slugs for x in exp)
        hits += hit
        is_control = q.startswith(_CONTROL_PREFIXES)
        if is_control:
            control_results.append((q, hit))
        tag = "HIT " if hit else "MISS"
        ctl = " [CONTROL]" if is_control else ""
        print(f"[{tag}]{ctl} {q[:62]}")
        if not hit:
            print(f"         expect {exp}  got {slugs}")

        block = _block(q, dom, args.k)
        for needle in _PLACEHOLDER_FAMILY:
            c = block.count(needle)
            if c:
                pollution += c
                pollution_examples.append(f"{needle!r}×{c} in block for {q[:40]!r}")

    n = len(queries)
    print(f"\n## G-POS recall@{args.k}: {hits}/{n} = {hits / n:.3f}")
    print("## Controls (must all HIT):")
    for q, hit in control_results:
        print(f"   [{'HIT ' if hit else 'MISS'}] {q[:60]}")
    print(f"## G-NEG-1 placeholder-pollution count: {pollution}  (REQUIRED: 0)")
    for ex in pollution_examples:
        print(f"     LEAK: {ex}")

    controls_ok = all(hit for _, hit in control_results)
    neg1_ok = pollution == 0
    print(f"\nRESULT: controls_ok={controls_ok}  G-NEG-1_ok={neg1_ok}")
    return 0 if (controls_ok and neg1_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
