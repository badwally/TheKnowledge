"""index.md updates.

M1 implements only `update_for(...)` — adds a new source line to a
"Recent ingests" section. The full domain-grouped catalog per WIKI.md § 7
is rebuilt by `wiki index --rebuild`, which lands in a later milestone.
"""

from datetime import datetime, timezone

from gateway import paths

_HEADER = """# Knowledge Index

Last updated: {timestamp}

Content catalog. Rebuilt by `wiki index --rebuild`. The agent reads this
first to orient before drilling into specific pages.

## Recent ingests

"""


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def update_for(source_id: str, source_type: str, title: str, domains: list[str] | None = None) -> bool:
    """Add a single-source line to index.md if not already present.

    Returns True if a new line was added; False if already indexed.
    """
    path = paths.index_path()
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_HEADER.format(timestamp=_now_iso()))

    existing = path.read_text()
    target_token = f"sources/{source_id}"
    if target_token in existing:
        return False

    domain_str = f" · {','.join(domains)}" if domains else ""
    line = f"- [[sources/{source_id}]] · {source_type} · {title}{domain_str}\n"

    if "## Recent ingests" not in existing:
        existing = existing.rstrip("\n") + "\n\n## Recent ingests\n\n"

    new_content = existing if existing.endswith("\n") else existing + "\n"
    new_content += line
    path.write_text(new_content)
    return True
