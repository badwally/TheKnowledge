"""Re-score the C1 train pool IN PLACE with the current policy + example bank.

No YouTube search (deterministic, no quota) — reuses the saved candidates from
pool-scored.json and re-runs only the filter model. Used for the C3 before/after
precision@10 (train) measurement. Reconstructs the filter `front` from the saved
pool rows (type/title/url/authors/channel/domains); view_count/publish_date are
not persisted in the pool row, a minor fidelity gap vs the original C1 scoring.

Usage:
  PYTHONPATH=src .venv/bin/python docs/research/youtube-filter-sl/rescore_train.py [--limit N] [--out PATH]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from gateway.filter import load_all, load_policy, select, score as filter_score
from gateway.filter.semantic import build_system_prompt

POOL = Path("docs/research/youtube-filter-sl/train-pool/pool-scored.json")
DOMAIN = "semantic-models"


def _front(row: dict) -> dict:
    return {
        "type": "youtube",
        "title": row.get("title", ""),
        "url": row["url"],
        "authors": [row["channel"]] if row.get("channel") else [],
        "domains": [DOMAIN],
        "meta": {"channel_name": row.get("channel", "")},
    }


def _tier(s: float, policy) -> str:
    if s >= policy.threshold_include:
        return "accept"
    if s >= policy.threshold_review:
        return "review"
    return "reject"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="score only the first N (smoke test)")
    ap.add_argument("--only", default="", help="comma-sep video_ids to score (smoke test)")
    ap.add_argument("--out", default="docs/research/youtube-filter-sl/train-pool/pool-scored-after.json")
    args = ap.parse_args()

    rows = json.loads(POOL.read_text())
    policy = load_policy(DOMAIN)
    examples = select(load_all(DOMAIN), policy)
    system = build_system_prompt(policy, examples)
    print(f"policy v{policy.version}, {len(examples)} examples in prompt, {len(rows)} candidates", file=sys.stderr)

    if args.only:
        want = set(args.only.split(","))
        rows = [r for r in rows if r["url"].split("v=")[-1] in want]
    elif args.limit:
        rows = rows[: args.limit]

    out = []
    for i, row in enumerate(rows, 1):
        front = _front(row)
        body = row.get("description") or row.get("title", "")
        res = filter_score(front, body, policy, examples, _prebuilt_system=system)
        new = {**row, "score": round(res.score, 4), "tier": _tier(res.score, policy)}
        out.append(new)
        vid = row["url"].split("v=")[-1]
        print(f"{i:3}/{len(rows)}  {row.get('score'):.2f}->{res.score:.2f}  [{vid}] {row['title'][:55]}", file=sys.stderr)

    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {args.out} ({len(out)} rows)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
