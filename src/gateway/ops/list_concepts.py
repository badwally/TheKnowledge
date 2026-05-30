"""`wiki list-concepts` — enumerate concept/entity/synthesis pages, optionally by domain.

Output is one tab-separated line per page: slug<TAB>canonical name.
Designed to pipe into fzf for interactive selection:

    wiki context "$(wiki list-concepts --domain glp1 | fzf | cut -f1)"
    wiki query "" --domain "$(wiki list-domains | fzf | cut -f1)"
"""

from __future__ import annotations

import json

from gateway import frontmatter as fm, paths
from gateway.core import OperationResult

_KIND_DIRS = {
    "concepts": "concepts",
    "entities": "entities",
    "synthesis": "synthesis",
    "mocs": "mocs",
    "all": None,  # sentinel — expanded below
}
_NAME_FIELDS = ("canonical_name", "title")


def list_concepts(
    *,
    domain: str | None = None,
    kind: str = "concepts",
    fmt: str = "text",
) -> OperationResult:
    """List wiki pages of the given kind, optionally filtered to one domain.

    ``kind``: one of concepts | entities | synthesis | mocs | all.
    ``domain``: domain slug filter; omit to list across all domains.
    ``fmt``: text (tab-separated slug + name) | json.
    """
    kb_root = paths.knowledge_root()
    kinds = list(_KIND_DIRS.keys() - {"all"}) if kind == "all" else [kind]

    rows: list[dict] = []
    for k in kinds:
        kind_dir = kb_root / "wiki" / k
        if not kind_dir.exists():
            continue
        for p in sorted(kind_dir.glob("*.md")):
            try:
                front, _ = fm.parse(p.read_text())
            except Exception:
                continue
            if domain and domain not in (front.get("domains") or []):
                continue
            slug = str(front.get("slug", p.stem))
            name = next(
                (str(front[f]) for f in _NAME_FIELDS if front.get(f)), slug
            )
            rows.append({"kind": k, "slug": slug, "name": name})

    if not rows:
        label = f"domain={domain!r}" if domain else "all domains"
        return OperationResult(success=True, summary=f"no {kind} pages found ({label})")

    if fmt == "json":
        return OperationResult(success=True, summary=json.dumps(rows, indent=2))

    lines = [f"{r['slug']}\t{r['name']}" for r in rows]
    return OperationResult(success=True, summary="\n".join(lines))
