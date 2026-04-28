#!/usr/bin/env python3
"""Phased import of the three legacy research-notebook Obsidian vaults
into the canonical knowledge base. Per MIGRATION.md § 3.

Phases:
  1 — `data/obsidian/`           → domain `ai-temporal-video`
  2 — `data/obsidian_glp1/`      → domain `glp1-reward-modulation`
  3 — `data/obsidian_edge_ai/`   → domain `edge-ai-agentic`
        (only after the legacy edge_ai pipeline run is committed)

Default behavior is `--dry-run` so a misclick can't accidentally rewrite
the canonical wiki. Pass `--commit` to actually apply.

Usage:
    python migrations/0001-import-legacy-vaults.py --phase 1 --dry-run
    python migrations/0001-import-legacy-vaults.py --phase 1 --commit
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

DEFAULT_LEGACY_ROOT = Path("~/code/research-notebook/data").expanduser()

PHASES: dict[int, tuple[str, str]] = {
    1: ("obsidian", "ai-temporal-video"),
    2: ("obsidian_glp1", "glp1-reward-modulation"),
    3: ("obsidian_edge_ai", "edge-ai-agentic"),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", type=int, choices=PHASES.keys(), required=True)
    parser.add_argument(
        "--legacy-root",
        type=Path,
        default=DEFAULT_LEGACY_ROOT,
        help="Override the legacy data root (default: ~/code/research-notebook/data/)",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", default=True, help="Default: report only")
    mode.add_argument("--commit", action="store_true", help="Actually apply the migration")
    ns = parser.parse_args(argv)

    legacy_subdir, domain_slug = PHASES[ns.phase]
    vault_path = ns.legacy_root / legacy_subdir

    if not vault_path.is_dir():
        print(f"error: vault not found at {vault_path}", file=sys.stderr)
        return 1

    from gateway.ops.batch_ingest import batch_ingest

    result = batch_ingest(
        vault_path,
        legacy_import=True,
        domain=domain_slug,
        dry_run=not ns.commit,
    )
    if result.success:
        print(f"phase {ns.phase} ({domain_slug}): {result.summary}")
        for p in result.paths_touched:
            print(f"  touched: {p}")
        return 0

    print("migration failed:", file=sys.stderr)
    for e in result.errors:
        print(f"  - {e}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
