#!/usr/bin/env python3
"""Migration 0004: backfill created_at / last_updated on entity, concept, synthesis pages.

For each page in wiki/entities/, wiki/concepts/, wiki/synthesis/:
  - If created_at missing: use `git log --diff-filter=A` to get first-commit date.
    Falls back to today if git returns nothing.
  - If last_updated missing: use `git log` most-recent-commit date.
    Falls back to today if git returns nothing.

Idempotent: pages with both fields already set are skipped.

Usage:
  python migrations/0004-backfill-timestamps.py [--dry-run] [--commit]

Default is dry-run. Pass --commit to write changes.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def _knowledge_root() -> Path:
    import os
    env = os.environ.get("KNOWLEDGE_ROOT")
    if env:
        return Path(env)
    # Default: walk up from this script's location to the repo root
    return Path(__file__).parent.parent


def _today_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _git_first_commit_date(path: Path, repo_root: Path) -> str | None:
    """Return ISO-8601 UTC date of the commit that added `path`, or None."""
    rel = str(path.relative_to(repo_root))
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--diff-filter=A", "--format=%cI", "--", rel],
            capture_output=True, text=True, cwd=repo_root, timeout=10,
        )
        lines = [l.strip() for l in result.stdout.splitlines() if l.strip()]
        if lines:
            dt = datetime.fromisoformat(lines[-1].replace("Z", "+00:00"))
            return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        pass
    return None


def _git_last_commit_date(path: Path, repo_root: Path) -> str | None:
    """Return ISO-8601 UTC date of the most recent commit touching `path`, or None."""
    rel = str(path.relative_to(repo_root))
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%cI", "--", rel],
            capture_output=True, text=True, cwd=repo_root, timeout=10,
        )
        lines = [l.strip() for l in result.stdout.splitlines() if l.strip()]
        if lines:
            dt = datetime.fromisoformat(lines[0].replace("Z", "+00:00"))
            return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        pass
    return None


def _backfill_page(path: Path, repo_root: Path, *, dry_run: bool) -> str | None:
    """Return a description of the change made, or None if no-op."""
    import yaml

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    # Parse frontmatter manually (avoid importing gateway in a standalone script)
    end_idx = text.find("\n---", 3)
    if end_idx == -1:
        return None
    fm_text = text[3:end_idx]
    body = text[end_idx + 4:]

    try:
        front = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return None

    if not isinstance(front, dict):
        return None

    already_has_both = front.get("created_at") and front.get("last_updated")
    if already_has_both:
        return None

    today = _today_iso()
    changed: list[str] = []

    if not front.get("created_at"):
        first = _git_first_commit_date(path, repo_root) or today
        front["created_at"] = first
        changed.append(f"created_at={first}")

    if not front.get("last_updated"):
        last = _git_last_commit_date(path, repo_root) or today
        front["last_updated"] = last
        changed.append(f"last_updated={last}")

    if not changed:
        return None

    if not dry_run:
        new_fm = yaml.dump(front, sort_keys=False, default_flow_style=False, allow_unicode=True)
        new_text = f"---\n{new_fm}---{body}"
        path.write_text(new_text, encoding="utf-8")

    rel = str(path.relative_to(repo_root / "wiki" if (repo_root / "wiki").exists() else repo_root))
    return f"{rel}: {', '.join(changed)}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Print what would change without writing (default).")
    parser.add_argument("--commit", action="store_true",
                        help="Actually write changes.")
    args = parser.parse_args()

    dry_run = not args.commit

    root = _knowledge_root()
    wiki_root = root / "wiki"

    dirs = [
        wiki_root / "entities",
        wiki_root / "concepts",
        wiki_root / "synthesis",
    ]

    changes: list[str] = []
    for d in dirs:
        if not d.is_dir():
            continue
        for page in sorted(d.glob("*.md")):
            msg = _backfill_page(page, root, dry_run=dry_run)
            if msg:
                changes.append(msg)

    if not changes:
        print("No pages need backfilling.")
        return

    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] {len(changes)} page(s) would be updated:" if dry_run else
          f"[{mode}] {len(changes)} page(s) updated:")
    for c in changes:
        print(f"  {c}")

    if dry_run:
        print("\nRun with --commit to apply changes.")


if __name__ == "__main__":
    main()
