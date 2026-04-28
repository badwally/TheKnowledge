"""`wiki batch-ingest` — vault-scoped operations.

M8 supports the legacy-import mode. Future modes (e.g., re-ingest a directory
of canonical sources, fan out a research-notebook pipeline run) layer onto
the same dispatcher.
"""

from __future__ import annotations

from pathlib import Path

from gateway.core import OperationResult


def batch_ingest(
    vault_path: str | Path,
    *,
    legacy_import: bool = False,
    domain: str | None = None,
    dry_run: bool = False,
) -> OperationResult:
    """Run batch operations against a vault directory."""
    if not legacy_import:
        return OperationResult(
            success=False,
            errors=[
                "batch-ingest requires --legacy-import in M8 (other modes not yet wired); "
                "for canonical sources use `wiki ingest <file>` per source"
            ],
        )

    if not domain:
        return OperationResult(
            success=False,
            errors=["--legacy-import requires --domain <slug> for the migrated content"],
        )

    from gateway.ops.migrate import migrate_vault

    return migrate_vault(Path(vault_path), domain, dry_run=dry_run)
