"""ONT-4: backfill entity_kind to controlled vocabulary.

Walks wiki/entities/*.md and rewrites any entity_kind value that is not in
ENTITY_KIND_ENUM to its canonical equivalent using a curated mapping.
Values not in the mapping and not already canonical are remapped to "other".

Idempotent: pages with a valid entity_kind are skipped.
"""

from __future__ import annotations

from pathlib import Path

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic
from gateway.validator import ENTITY_KIND_ENUM


# Mapping from legacy free-text values → canonical enum values.
# Based on the 24 free-text values observed in the wiki pre-ONT-4.
_KIND_MAP: dict[str, str] = {
    # paper variants
    "publication": "paper",
    "journal-issue": "paper",
    "journal_issue": "paper",
    "periodical": "paper",
    "article": "paper",
    "preprint": "paper",
    "report": "paper",
    "book": "paper",
    "chapter": "paper",
    "thesis": "paper",
    # statute/regulation variants
    "policy_document": "statute",
    "policy-document": "statute",
    "policy": "statute",
    "regulation": "statute",
    "law": "statute",
    "legislation": "statute",
    "guideline": "standard",
    "guidance": "standard",
    "protocol": "standard",
    # organization variants
    "company": "organization",
    "institution": "organization",
    "agency": "organization",
    "body": "organization",
    # product variants
    "device": "product",
    "tool": "product",
    # dataset variants
    "database": "dataset",
    "repository": "dataset",
    # drug variants
    "medication": "drug",
    "compound": "drug",
    "molecule": "drug",
    "treatment": "drug",
    # software variants
    "app": "software",
    "application": "software",
    "framework": "software",
    "library": "software",
    "platform": "software",
}


def _canonical_kind(raw: str) -> str:
    """Return canonical enum value for a raw entity_kind string."""
    if raw in ENTITY_KIND_ENUM:
        return raw
    mapped = _KIND_MAP.get(raw.lower().replace(" ", "-").replace("_", "-"))
    if mapped:
        return mapped
    return "other"


def backfill_entity_kinds(*, dry_run: bool = False) -> OperationResult:
    """Remap non-enum entity_kind values on all wiki entity pages.

    Skips pages that already have a canonical entity_kind.
    Returns counts of updated, skipped, and errored pages.
    """
    entities_dir = paths.wiki_dir() / "entities"
    if not entities_dir.exists():
        return OperationResult(
            success=True,
            summary="backfill-entity-kinds: no entities/ directory found, nothing to do",
        )

    updated = 0
    skipped = 0
    errors: list[str] = []

    for path in sorted(entities_dir.rglob("*.md")):
        try:
            text = path.read_text()
            front, body = fm.parse(text)
        except Exception as e:
            errors.append(f"{path.name}: read/parse error — {e!r}")
            continue

        kind = front.get("entity_kind")
        if kind is None:
            skipped += 1
            continue
        if str(kind) in ENTITY_KIND_ENUM:
            skipped += 1
            continue

        canonical = _canonical_kind(str(kind))
        new_front = {**front, "entity_kind": canonical}
        new_text = fm.serialize(new_front, body)

        if not dry_run:
            try:
                write_atomic(path, new_text)
            except Exception as e:
                errors.append(f"{path.name}: write error — {e!r}")
                continue

        updated += 1

    if not dry_run:
        log.append(
            op="backfill-entity-kinds",
            fields={"updated": updated, "skipped": skipped, "errors": len(errors)},
            summary=f"backfill-entity-kinds: {updated} updated, {skipped} skipped, {len(errors)} errors",
        )

    mode = " (dry-run)" if dry_run else ""
    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"backfill-entity-kinds{mode}: {updated} updated, "
            f"{skipped} skipped, {len(errors)} errors"
        ),
    )
