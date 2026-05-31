"""`wiki list-domains` — enumerate blessed domains with slug, title, wiki page count."""

from __future__ import annotations

import json

import yaml

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult


def list_domains(*, fmt: str = "text") -> OperationResult:
    """Return all blessed domains (those with a policy.yaml).

    Each row: slug, short title (first sentence of policy topic), wiki page count.
    Wiki page count spans concepts + entities + synthesis + mocs — a proxy for
    knowledge depth, not raw-source volume.
    """
    pol_dir = paths.policies_dir()
    kb_root = paths.knowledge_root()

    rows: list[dict] = []
    if not pol_dir.exists():
        return OperationResult(success=True, summary="no blessed domains found")
    for domain_dir in sorted(pol_dir.iterdir()):
        if not domain_dir.is_dir():
            continue
        policy_path = domain_dir / "policy.yaml"
        if not policy_path.exists():
            continue

        try:
            data = yaml.safe_load(policy_path.read_text()) or {}
        except yaml.YAMLError:
            continue

        slug = data.get("domain", {}).get("slug", domain_dir.name)
        topic = data.get("domain", {}).get("topic", "") or ""
        title = topic.split(".")[0].strip() or slug

        page_count = _count_wiki_pages(kb_root, slug)
        rows.append({"slug": slug, "title": title, "wiki_pages": page_count})

    if not rows:
        return OperationResult(success=True, summary="no blessed domains found")

    if fmt == "json":
        return OperationResult(success=True, summary=json.dumps(rows, indent=2))

    slug_w = max(len(r["slug"]) for r in rows) + 2
    lines = [
        f"{r['slug']:<{slug_w}} {r['wiki_pages']:>4} pages   {r['title']}"
        for r in rows
    ]
    return OperationResult(success=True, summary="\n".join(lines))


def _count_wiki_pages(kb_root, slug: str) -> int:
    count = 0
    for kind in ("concepts", "entities", "synthesis", "mocs"):
        kind_dir = kb_root / "wiki" / kind
        if not kind_dir.exists():
            continue
        for p in kind_dir.glob("*.md"):
            try:
                front, _ = fm.parse(p.read_text())
                if slug in (front.get("domains") or []):
                    count += 1
            except Exception:
                continue
    return count
