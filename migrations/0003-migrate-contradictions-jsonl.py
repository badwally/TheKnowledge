#!/usr/bin/env python3
"""ONT-3: migrate .knowledge/contradictions.jsonl to wiki/contradictions/*.md pages.

One-time migration — same exception as ONT-4. Dry-run by default.
No-op when .knowledge/contradictions.jsonl is absent.

Usage:
    python migrations/0003-migrate-contradictions-jsonl.py --dry-run
    python migrations/0003-migrate-contradictions-jsonl.py --commit
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Add project src to path so gateway imports work without editable install.
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from gateway import paths  # noqa: E402


def run(*, dry_run: bool = True) -> int:
    """Migrate contradictions.jsonl → wiki/contradictions/*.md.

    Returns the number of pages written (0 when JSONL absent or empty).
    """
    jsonl_path = paths.knowledge_internal() / "contradictions.jsonl"
    if not jsonl_path.exists():
        return 0

    contradictions_dir = paths.wiki_dir() / "contradictions"
    if not dry_run:
        contradictions_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    with jsonl_path.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue

            slug = str(record.get("slug", "")).strip()
            if not slug:
                continue

            parties = record.get("parties", [])
            severity = record.get("severity", "minor")
            status = record.get("status", "open")
            resolution = record.get("resolution", "")
            summary = str(record.get("summary", "")).strip() or "Contradiction between source documents."

            front_lines = [
                "---",
                f"type: contradiction",
                f"slug: {slug}",
                "parties:",
            ]
            for p in parties:
                front_lines.append(f"  - \"{p}\"")
            front_lines.extend([
                f"severity: {severity}",
                f"status: {status}",
                f"resolution: \"{resolution}\"",
                "---",
                "",
            ])
            body = "\n".join(front_lines) + f"## Summary\n\n{summary}\n"

            out_path = contradictions_dir / f"{slug}.md"
            if dry_run:
                print(f"[dry-run] would write {out_path.relative_to(paths.knowledge_root())}")
            else:
                out_path.write_text(body)
                print(f"wrote {out_path.relative_to(paths.knowledge_root())}")
            count += 1

    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--commit", dest="dry_run", action="store_false")
    args = parser.parse_args()
    migrated = run(dry_run=args.dry_run)
    print(f"{'[dry-run] ' if args.dry_run else ''}migrated {migrated} contradiction(s)")
    sys.exit(0)
