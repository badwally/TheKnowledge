"""AGT-6: scheduled briefing generator.

Weekly per-domain nlm-briefing with corpus-hash skip. Idempotent: re-running
when corpus is unchanged produces no artifact and logs a skip.

Hard rule: never auto-escalates to audio or slides.
See memory: feedback_artifact_generation_opt_in.md.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult, write_atomic


def _corpus_hash(domain: str) -> str:
    """Stable hash over raw source IDs tagged to this domain, sorted."""
    raw_root = paths.raw_dir()
    if not raw_root.exists():
        return hashlib.sha256(b"").hexdigest()[:16]
    entries: list[str] = []
    for type_dir in sorted(raw_root.iterdir()):
        if not type_dir.is_dir():
            continue
        for src in sorted(type_dir.glob("*.md")):
            try:
                front, _ = fm.parse(src.read_text())
            except Exception:
                continue
            if domain in list(front.get("domains") or []):
                entries.append(f"{src.stem}:{src.stat().st_mtime_ns}")
    return hashlib.sha256("|".join(entries).encode()).hexdigest()[:16]


def _hash_store() -> Path:
    return paths.knowledge_internal() / "briefing-cron"


def _load_stored_hash(domain: str) -> str | None:
    p = _hash_store() / f"{domain}.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text()).get("corpus_hash")
    except Exception:
        return None


def _store_hash(domain: str, corpus_hash: str) -> None:
    p = _hash_store() / f"{domain}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(
        p,
        json.dumps(
            {
                "corpus_hash": corpus_hash,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            },
            indent=2,
        ),
    )


def _blessed_domains() -> list[str]:
    pd = paths.policies_dir()
    if not pd.exists():
        return []
    return sorted(p.parent.name for p in pd.glob("*/policy.yaml"))


def run_briefing_cron() -> OperationResult:
    """Run nlm-briefing for each blessed domain if its corpus has changed."""
    from gateway.ops.nlm import nlm_briefing  # avoid circular import at module level

    domains = _blessed_domains()
    if not domains:
        return OperationResult(success=True, summary="briefing-cron: no blessed domains")

    ran: list[str] = []
    skipped: list[str] = []
    errors: list[str] = []

    for domain in domains:
        current_hash = _corpus_hash(domain)
        if current_hash == _load_stored_hash(domain):
            skipped.append(domain)
            continue
        result = nlm_briefing(domain)
        if result.success:
            _store_hash(domain, current_hash)
            ran.append(domain)
        else:
            errors.extend(
                result.errors or [f"{domain}: nlm_briefing returned no error detail"]
            )

    log.append(
        op="briefing-cron",
        fields={"ran": len(ran), "skipped": len(skipped), "errors": len(errors)},
        summary=f"ran={ran} skipped={skipped}",
    )

    return OperationResult(
        success=len(errors) == 0,
        errors=errors,
        summary=(
            f"briefing-cron: {len(ran)} ran, {len(skipped)} skipped, {len(errors)} errors"
        ),
    )
