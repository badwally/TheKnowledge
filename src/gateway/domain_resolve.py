"""Multi-label domain resolution at commit (design §6, decision 6).

A deposit resolves to one-or-more LIVE domains; multi-domain is first-class.
Quarantine ONLY when the resolved set is empty — never untagged-by-default."""

from __future__ import annotations

from typing import Sequence

from gateway import paths


def live_domains() -> list[str]:
    """Domains with an on-disk ``policy.yaml`` under ``.knowledge/policies/``."""
    pol_dir = paths.policies_dir()
    if not pol_dir.exists():
        return []
    return [
        d.name for d in sorted(pol_dir.iterdir())
        if d.is_dir() and (d / "policy.yaml").exists()
    ]


def resolve_domains(identity: dict, live_domains: Sequence[str]) -> list[str]:
    live = {str(d) for d in live_domains}
    raw = identity.get("domains") or (
        [identity["domain"]] if identity.get("domain") else []
    )
    resolved = [str(d) for d in raw if str(d) in live]
    # de-dup, stable order
    seen: dict[str, None] = {}
    for d in resolved:
        seen.setdefault(d, None)
    return list(seen)
