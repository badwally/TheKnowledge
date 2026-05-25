#!/usr/bin/env python3
"""ONT-4: migrate free-text entity_kind values to the controlled vocabulary.

Maps 25 legacy free-text values to ENTITY_KIND_ENUM. Idempotent — pages
already using enum values are skipped. Dry-run by default.

Usage:
    python migrations/0002-migrate-entity-kinds.py --dry-run
    python migrations/0002-migrate-entity-kinds.py --commit
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Add project src to path so gateway imports work without editable install.
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from gateway import frontmatter as fm
from gateway import paths
from gateway.validator import ENTITY_KIND_ENUM

# Canonical mapping from legacy free-text → enum value.
# Unmapped values (already in enum) are handled by identity pass-through.
_LEGACY_MAP: dict[str, str] = {
    "publication": "paper",
    "journal-issue": "paper",
    "periodical": "paper",
    "regulation": "statute",
    "regulatory_framework": "statute",
    "policy_document": "statute",
    "route": "other",
    "form": "other",
    "project": "other",
    "program": "other",
    "infrastructure-asset": "other",
    "intellectual_property": "other",
    "artifact": "other",
    "certification": "standard",
    "building": "place",
}


def _remap(kind: str) -> str:
    """Return the canonical enum value for a legacy entity_kind string."""
    if kind in ENTITY_KIND_ENUM:
        return kind
    return _LEGACY_MAP.get(kind, "other")


def run(*, dry_run: bool) -> int:
    entities_dir = paths.wiki_dir() / "entities"
    if not entities_dir.exists():
        print("No wiki/entities/ directory found — nothing to migrate.")
        return 0

    changed = 0
    skipped = 0
    unknown: list[str] = []

    for path in sorted(entities_dir.glob("*.md")):
        try:
            front, body = fm.parse(path.read_text())
        except fm.FrontmatterError as e:
            print(f"  SKIP (parse error): {path.name}: {e}")
            skipped += 1
            continue

        kind = front.get("entity_kind")
        if kind is None:
            skipped += 1
            continue

        canonical = _remap(str(kind))
        if canonical == kind:
            skipped += 1
            continue

        if kind not in ENTITY_KIND_ENUM and kind not in _LEGACY_MAP:
            unknown.append(f"{path.name}: {kind!r}")
            canonical = "other"

        front["entity_kind"] = canonical
        new_text = fm.serialize(front, body)

        if dry_run:
            print(f"  DRY-RUN: {path.name}: {kind!r} → {canonical!r}")
        else:
            path.write_text(new_text)
            print(f"  MIGRATED: {path.name}: {kind!r} → {canonical!r}")
        changed += 1

    if unknown:
        print(f"\nWARNING: {len(unknown)} unmapped value(s) defaulted to 'other':")
        for u in unknown:
            print(f"  {u}")

    verb = "would change" if dry_run else "changed"
    print(f"\n{verb} {changed} page(s), skipped {skipped} (already canonical or no entity_kind).")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--dry-run", action="store_true", default=True,
                       help="Preview changes without writing (default)")
    group.add_argument("--commit", dest="dry_run", action="store_false",
                       help="Apply changes to wiki/entities/*.md")
    args = parser.parse_args()
    sys.exit(run(dry_run=args.dry_run))


if __name__ == "__main__":
    main()
