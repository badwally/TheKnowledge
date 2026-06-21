"""Pin the C3 calibration example bank for semantic-models (reproducible).

Pins 10 user-picked includes (varied de-anchored scores by fit strength) and 4
excludes (2 off-topic high-confidence, 2 over-valued theory edge-case). Run with
KNOWLEDGE_ROOT pointed at the intended tree so the bank lands there:

  KNOWLEDGE_ROOT=$PWD PYTHONPATH=src .venv/bin/python docs/research/youtube-filter-sl/pin_examples.py

Idempotent: re-running overwrites each example file in place.
"""
from __future__ import annotations

import json
from pathlib import Path

from gateway.filter import examples as ex

POOL = Path("docs/research/youtube-filter-sl/train-pool/pool-scored.json")
DOMAIN = "semantic-models"
POLV = "semantic-models-v1"

# (video_id, score, rationale) — include examples; score is calibration signal
# (de-anchored estimate of relative fit), NOT a user ranking. Gold labels stay binary.
INCLUDES = [
    ("T4afZsyHmUc", 0.95, "Deep learning with knowledge graphs from a leading researcher (Leskovec) at a recognized venue; representation-learning altitude, strong include."),
    ("5OGMYQaIPKw", 0.90, "Hands-on knowledge-graph construction lecture from a named research lab; applied construction depth is fully in-scope."),
    ("83lI3u7KX0g", 0.90, "Applied ontology-development workflows and best practices from an authoritative community (OBO Foundry); include."),
    ("KAs1UA0HJJM", 0.90, "Knowledge-graph representation learning / embeddings is in-scope per the representation-learning criterion; score on topical fit, not formal-logic content."),
    ("SHHHJXwHeWM", 0.88, "KG + LLM integration focused on how knowledge-graph data feeds models — representation-side KG-LLM work, include."),
    ("DwFD_ffS21E", 0.85, "Applied agent-reasoning over knowledge graphs from a recognized graph-database venue; KG+agent work addressing the representation/architecture side clears the bar without formal-theory content."),
    ("m11X-T-v6kg", 0.85, "Applied semantic-application / linked-data implementation guidance from an authoritative standards body (DCMI); include."),
    ("5knKyWUUWAg", 0.82, "Applied semantic data architecture / knowledge-graph construction at scale from a practitioner consultancy; applied architecture depth, include."),
    ("PCnSWteKpL8", 0.80, "Semantic-layer / metrics-layer architecture talk at scale; in-scope per the semantic-layer carve-out even though vendor-delivered, because it addresses the architecture layer."),
    ("s_rDUWyiZOM", 0.80, "Semantic-layer + ontology + AI architecture summit talk; addresses the modeling/architecture layer and the KG-LLM connection — include."),
]
EXCLUDES_HI = [
    ("4nvQgJc6GLw", "Off-topic — a sociology/UPSC interview short with no relation to semantic data models; exclude."),
    ("G-LVg8fWXtw", "Off-topic — embedded battery-free sensor prototyping (UbiComp); not about knowledge representation or semantic data; exclude."),
]
EXCLUDES_EDGE = [
    ("i11lo6A92uE", "On-topic description-logic theory, but the pool heavily over-surfaces single-author foundational-theory talks; down-weight a redundant theory talk relative to applied / representation-learning / semantic-layer coverage."),
    ("ww99npDh4cg", "Broad survey keynote on KGs in a world of LLMs; prioritize talks with concrete applied, construction, or representation-learning content over high-level survey keynotes."),
]


def main() -> int:
    pool = {c["url"].split("v=")[-1]: c for c in json.loads(POOL.read_text())}

    def snap(vid):
        c = pool.get(vid, {})
        return ({"type": "youtube", "title": c.get("title", ""),
                 "url": c.get("url", f"https://www.youtube.com/watch?v={vid}"),
                 "channel": c.get("channel", "")},
                c.get("description") or c.get("title", ""))

    n = 0
    for vid, sc, r in INCLUDES:
        fs, exc = snap(vid)
        ex.pin(source_id=f"yt-{vid}", domain=DOMAIN, decision="include", score=sc,
               policy_version=POLV, rationale=r, pinned_by="user-correction",
               frontmatter_snapshot=fs, content_excerpt=exc); n += 1
    for vid, r in EXCLUDES_HI:
        fs, exc = snap(vid)
        ex.pin(source_id=f"yt-{vid}", domain=DOMAIN, decision="exclude", score=0.0,
               policy_version=POLV, rationale=r, pinned_by="high-confidence",
               frontmatter_snapshot=fs, content_excerpt=exc); n += 1
    for vid, r in EXCLUDES_EDGE:
        fs, exc = snap(vid)
        ex.pin(source_id=f"yt-{vid}", domain=DOMAIN, decision="exclude", score=0.45,
               policy_version=POLV, rationale=r, pinned_by="edge-case",
               frontmatter_snapshot=fs, content_excerpt=exc); n += 1

    allx = ex.load_all(DOMAIN)
    print(f"pinned {n} -> {ex.examples_dir(DOMAIN)}")
    print(f"load_all: {len(allx)} ({sum(1 for e in allx if e.decision=='include')} inc / "
          f"{sum(1 for e in allx if e.decision=='exclude')} exc)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
