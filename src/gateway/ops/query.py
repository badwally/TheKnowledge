"""`wiki query "<question>" --domain <slug>` — query the persistent notebook.

This is a thin wrapper around `NlmClient.notebook_query`: send the
question to the domain's persistent NotebookLM corpus, resolve the
returned citations through the gateway's source-map, and file the answer
as a synthesis page.

The bag-of-words / keyword-score fallback that lived here pre-rebuild is
gone — corpus-grounded synthesis is the only path. Without a persistent
notebook the operation errors out and tells the user to run
`wiki research` to build one.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from gateway import frontmatter as fm
from gateway import log, nlm_registry, paths
from gateway.core import OperationResult
from gateway.ops.apply_plan import apply_plan
from gateway.plan import Plan, WikiUpdate
from gateway.research import source_map as _source_map

if TYPE_CHECKING:
    from gateway.nlm_client import NlmClient


__all__ = ["query"]


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slugify(text: str, *, max_words: int = 6) -> str:
    cleaned = _SLUG_RE.sub("-", text.lower()).strip("-")
    words = [w for w in cleaned.split("-") if w]
    return "-".join(words[:max_words]) or "query"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _coerce_citations(raw: dict) -> dict[int, str]:
    out: dict[int, str] = {}
    for k, v in (raw or {}).items():
        try:
            num = int(k)
        except (TypeError, ValueError):
            continue
        if isinstance(v, str) and v:
            out[num] = v
    return out


_CITE_MARKER_RE = re.compile(r"\[(\d+)\]")


def _inline_citations(answer: str, resolved: dict[int, str]) -> str:
    """Replace `[N]` markers with the resolved `[[sources/...]]` wikilink.

    Markers without a matching citation are left untouched so the
    operator can still see the original NotebookLM-side numbering.
    """
    if not resolved:
        return answer

    def _sub(match: re.Match) -> str:
        try:
            num = int(match.group(1))
        except ValueError:
            return match.group(0)
        link = resolved.get(num)
        return f"{match.group(0)} {link}" if link else match.group(0)

    return _CITE_MARKER_RE.sub(_sub, answer)


def query(
    question: str,
    *,
    domain: str,
    nlm_client: "NlmClient | None" = None,
    draft: bool = False,
) -> OperationResult:
    """Ask the persistent domain notebook a question; file the answer.

    `domain` is required: the persistent NotebookLM corpus is the
    grounding context, and there's exactly one per domain. If no
    notebook exists for the domain, the operation tells the caller to
    run `wiki research` first.
    """
    if not question or not question.strip():
        return OperationResult(success=False, errors=["question must be non-empty"])
    if not domain:
        return OperationResult(
            success=False,
            errors=["--domain is required for `wiki query`"],
        )

    notebook_id = nlm_registry.get_persistent(domain)
    if not notebook_id:
        return OperationResult(
            success=False,
            errors=[
                f"no notebook for domain {domain!r}; "
                "run `wiki research` first to build one"
            ],
        )

    if nlm_client is None:
        from gateway.nlm_client import NlmCLIClient

        nlm_client = NlmCLIClient()

    # 1) ask the corpus.
    try:
        response = nlm_client.notebook_query(notebook_id, question)
    except Exception as e:  # noqa: BLE001 — surface as op error
        return OperationResult(
            success=False,
            errors=[f"notebook_query failed: {e}"],
        )

    answer = (response.get("answer") or "").strip()
    raw_citations = _coerce_citations(response.get("citations", {}))

    # 2) source-map. Prefer cached map; rebuild only if absent so we
    # don't shell out for every query.
    smap = _source_map.load_cached_source_map(notebook_id)
    if smap is None:
        try:
            smap = _source_map.build_source_map(notebook_id, client=nlm_client)
        except _source_map.SourceMapError as e:
            return OperationResult(
                success=False,
                errors=[f"source map build failed: {e}"],
            )

    # 3) resolve citations.
    resolved = _source_map.resolve_citations(raw_citations, smap)
    unresolved = sorted(
        n for n, link in resolved.items() if link.startswith("[[nlm:")
    )
    if unresolved:
        log.append(
            "query",
            fields={
                "domain": domain,
                "unresolved_citations": ",".join(str(n) for n in unresolved),
            },
            summary=(
                f"lint-warning: query response cited {len(unresolved)} "
                f"NotebookLM source(s) with no `raw/` counterpart"
            ),
        )

    # 4) build the synthesis plan.
    today = _today()
    slug = f"{today}-{_slugify(question)}"
    rel = f"wiki/synthesis/{slug}.md"

    _now = _now_iso()
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": question.strip().rstrip("?"),
        "domains": [domain],
        "question": question,
        "created_at": _now,
        "last_updated": _now,
        "sources_count": len(set(resolved.values())) if resolved else 0,
        "nlm_notebook_id": notebook_id,
    }

    # Rewrite `[N]` markers in the answer to inline `[[sources/...]]` so the
    # validator's citation-grounding rule passes (citations must appear on
    # the same line as the claim).
    rendered_answer = _inline_citations(answer, resolved) if answer else (
        "_(notebook returned an empty answer)_"
    )
    # Honest provenance: lines without an inline `[N]` marker stay uncited.
    # The validator surfaces them as warnings under `--draft`; finalization
    # requires `wiki cite` (or rewrite) to ground each uncited claim.

    body_lines = [
        f"# {front['title']}",
        "",
        "## Synthesis",
        "",
        rendered_answer,
        "",
    ]

    body_lines.append("## Sources cited")
    body_lines.append("")
    if resolved:
        seen: set[str] = set()
        for link in resolved.values():
            if link in seen:
                continue
            seen.add(link)
            body_lines.append(f"- {link}")
    else:
        body_lines.append("_(no citations returned)_")
    body_lines.append("")

    update = WikiUpdate(
        target_path=rel,
        update_kind="create",
        content=fm.serialize(front, "\n".join(body_lines)),
        rationale="filed answer to query against persistent corpus",
    )
    plan = Plan(
        source_id=f"query-{slug}",
        rationale=f"query against {domain} corpus",
        updates=[update],
    )

    # If every citation is unresolved, the page can't satisfy the
    # citation-grounding rule with `[[sources/...]]` — file it as a
    # draft so the operator can chase down the missing raw/ pages and
    # `wiki finalize` later. A draft-only path is fine because the
    # `lint-warning` event was already logged above.
    effective_draft = draft or (
        bool(unresolved) and len(unresolved) == len(resolved)
    )
    return apply_plan(plan, draft=effective_draft)
