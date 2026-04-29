"""Bottom-up domain discovery: cluster source pages into draft proposals.

Per BUILD.md M36. Closes the gap between "ingest a pile of unsorted PDFs"
and "grow the citation graph against named domains." The op selects
candidate source pages (by glob, date, or untagged flag), asks the plan
client to group them into 3-8 thematic clusters, and files one
`wiki/proposals/<slug>.md` per cluster as a draft `domain-proposal` page.

The downstream flow is:
  discover-domains  →  human review  →  promote-domain (writes policy + back-tags)
                                    →  reject-proposal (deletes draft)
"""

from __future__ import annotations

import fnmatch
from datetime import datetime, timezone

from gateway import frontmatter as fm
from gateway import paths
from gateway.core import OperationResult
from gateway.ops.apply_plan import apply_plan
from gateway.plan import PlanClient, PlanError, parse_plan_response


_MAX_BODY_CHARS = 800


def discover_domains(
    *,
    scope: str | None = None,
    since: str | None = None,
    untagged: bool = False,
    client: PlanClient | None = None,
) -> OperationResult:
    """Cluster source pages into draft domain proposals.

    Filters (combined as AND):
    - `scope`: glob pattern relative to repo root, e.g. `wiki/sources/pdf-*`
    - `since`: ISO-8601 prefix; sources with `ingested_at < since` are skipped
    - `untagged`: only include sources with empty/missing `domains` frontmatter

    Atomic: the plan client returns one proposal page per cluster; either
    all proposals validate and write together, or none do.
    """
    if client is None:
        from gateway.plan import ClaudeCLIPlanClient

        client = ClaudeCLIPlanClient()

    sources = _collect_sources(scope=scope, since=since, untagged=untagged)
    if not sources:
        return OperationResult(
            success=True,
            no_op=True,
            summary="discover-domains: no candidate sources matched filters",
        )

    prompt = _build_prompt(sources)

    try:
        raw_response = client.call(prompt)
    except Exception as e:
        return OperationResult(success=False, errors=[f"plan client failed: {e}"])

    try:
        plan = parse_plan_response(raw_response)
    except PlanError as e:
        return OperationResult(success=False, errors=[f"could not parse plan: {e}"])

    if not plan.updates:
        return OperationResult(
            success=True,
            no_op=True,
            summary=f"discover-domains: plan returned no proposals over {len(sources)} sources",
        )

    return apply_plan(plan)


# --- candidate selection ---------------------------------------------------


def _collect_sources(
    *,
    scope: str | None,
    since: str | None,
    untagged: bool,
) -> list[dict]:
    sources_dir = paths.wiki_dir() / "sources"
    if not sources_dir.exists():
        return []
    out: list[dict] = []
    for path in sorted(sources_dir.glob("*.md")):
        if scope:
            rel = path.relative_to(paths.knowledge_root()).as_posix()
            if not fnmatch.fnmatch(rel, scope):
                continue
        try:
            front, body = fm.parse(path.read_text())
        except fm.FrontmatterError:
            continue
        domains = list(front.get("domains") or [])
        if untagged and domains:
            continue
        if since and str(front.get("ingested_at", "")) < since:
            continue
        out.append(
            {
                "source_id": front.get("source_id", path.stem),
                "title": str(front.get("title", "")),
                "domains": domains,
                "excerpt": _first_n_chars(body, _MAX_BODY_CHARS),
            }
        )
    return out


def _first_n_chars(text: str, n: int) -> str:
    text = text.strip()
    if len(text) <= n:
        return text
    return text[:n].rstrip() + "..."


# --- prompt construction ---------------------------------------------------


_PROMPT_TEMPLATE = """\
You are clustering an unsorted corpus of source pages from a personal knowledge base
to surface candidate domains. Each source is shown below with its source_id, title,
and a short body excerpt. Group them into 3-8 thematic clusters and emit one
`domain-proposal` page per cluster.

## Sources to cluster ({source_count} total)

{sources_section}

## Your task

Return ONLY a JSON object describing a Plan with one update per cluster:

```
{{
  "source_id": "discover-{timestamp}",
  "rationale": "<one sentence: how you grouped them>",
  "updates": [
    {{
      "target_path": "wiki/proposals/proposal-<slug>.md",
      "update_kind": "create",
      "content": "<full markdown: frontmatter + body>"
    }}
  ]
}}
```

Each proposal page must have:

- **Frontmatter** (YAML, all required):
  - `type: domain-proposal`
  - `slug: proposal-<lowercase-hyphenated>` (must match the file basename)
  - `title: <human-readable>`
  - `proposed_domain: <lowercase-hyphenated slug for the future domain>`
  - `status: draft`
  - `member_sources: [<source_id>, ...]` (list of source_id strings, NOT wikilinks)
  - `rationale: <one paragraph>`

- **Sections** (both required):
  - `## Rationale` — one or two paragraphs explaining the cluster
  - `## Member sources` — bulleted list, one per member, each line:
    `- [[sources/<source_id>]]: <one-line description>`

Rules:
- Slugs are lowercase letters/digits/hyphens only.
- Cluster by *theme*, not by source type.
- A cluster should have at least 3 members. Sources that don't fit any theme
  go into a single `miscellany` or `uncategorized` cluster.
- Every input source must appear in exactly one cluster's `member_sources`.
- Do not invent sources or wiki pages outside `wiki/proposals/`.
"""


def _build_prompt(sources: list[dict]) -> str:
    blocks = []
    for s in sources:
        block = (
            f"- source_id: `{s['source_id']}`\n"
            f"  title: {s['title']}\n"
            f"  domains: {s['domains']}\n"
            f"  excerpt: {s['excerpt']!r}"
        )
        blocks.append(block)
    return _PROMPT_TEMPLATE.format(
        source_count=len(sources),
        sources_section="\n".join(blocks),
        timestamp=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ"),
    )
