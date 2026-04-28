"""`wiki query "<question>"` — search the wiki and (optionally) file an answer.

M6 v1: keyword-based scope discovery + agent-driven synthesis. The agent
receives the question + matched wiki pages and returns either:
- a Plan that creates/updates a synthesis page (preferred), or
- inline JSON with `synthesis_text` for the gateway to file.

Hundreds-of-sources NotebookLM-mediated synthesis is wired through
`wiki nlm-briefing` etc. (M5); the query op delegates there when scope
exceeds in-context limits in a future iteration.
"""

from __future__ import annotations

from pathlib import Path
import re

from gateway import frontmatter as fm
from gateway import paths
from gateway.core import OperationResult
from gateway.ops.apply_plan import apply_plan
from gateway.plan import Plan, PlanClient, parse_plan_response


# How many wiki pages to search and pass into the prompt.
_MAX_PAGES_IN_PROMPT = 30


def _all_wiki_pages() -> list[Path]:
    """Return every page under wiki/ except artifacts (artifacts are wrappers)."""
    out: list[Path] = []
    wiki = paths.wiki_dir()
    if not wiki.exists():
        return out
    for sub in ("entities", "concepts", "synthesis", "mocs", "sources"):
        d = wiki / sub
        if d.exists():
            out.extend(p for p in d.glob("*.md"))
    return out


def _match_score(question: str, text: str) -> int:
    """Cheap keyword-overlap score for first-pass scope narrowing."""
    q_words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]+", question)}
    if not q_words:
        return 0
    text_words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]+", text)}
    return len(q_words & text_words)


def _select_relevant(
    question: str,
    pages: list[Path],
    *,
    domain: str | None = None,
    limit: int = _MAX_PAGES_IN_PROMPT,
) -> list[Path]:
    scored: list[tuple[int, Path]] = []
    for path in pages:
        try:
            front, body = fm.parse(path.read_text())
        except fm.FrontmatterError:
            continue
        if domain:
            page_domains = list(front.get("domains") or [])
            page_domain = front.get("domain") or (page_domains[0] if page_domains else None)
            if page_domain != domain and domain not in page_domains:
                continue
        score = _match_score(question, front.get("title", "")) * 3 + _match_score(question, body)
        if score > 0:
            scored.append((score, path))
    scored.sort(reverse=True, key=lambda t: t[0])
    return [path for _, path in scored[:limit]]


_QUERY_PROMPT_TEMPLATE = """\
You are answering a question against a personal knowledge base. The pages
shown below are the candidates the gateway considered relevant. Synthesize
an answer with citations into the wiki source pages they cite.

## Question

{question}

{domain_section}

## Candidate wiki pages

{pages_section}

## Your task

Return ONLY a JSON object describing a Plan that creates a synthesis page.

```
{{
  "source_id": "synthesis-query-{slug_hint}",
  "rationale": "<one sentence>",
  "updates": [
    {{
      "target_path": "wiki/synthesis/{slug_hint}.md",
      "update_kind": "create",
      "content": "<canonical synthesis page (frontmatter + body) per WIKI.md § 4.4>",
      "rationale": "<why this synthesis exists>"
    }}
  ]
}}
```

Required frontmatter fields for synthesis pages: type, slug, title, domains, question.
Required sections: Synthesis, Sources cited.
Cite into existing source pages as `[[sources/<id>]]`. If you cannot find an
appropriate citation in the candidates above, say so in the synthesis body
and acknowledge the gap.
"""


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def _slugify(question: str, *, max_words: int = 6) -> str:
    cleaned = _SLUG_RE.sub("-", question.lower()).strip("-")
    words = [w for w in cleaned.split("-") if w]
    return "-".join(words[:max_words]) or "query"


def query(
    question: str,
    *,
    domain: str | None = None,
    client: PlanClient | None = None,
) -> OperationResult:
    """Search the wiki and file a synthesis page answering `question`."""
    if client is None:
        from gateway.plan import ClaudeCLIPlanClient

        client = ClaudeCLIPlanClient()

    pages = _select_relevant(question, _all_wiki_pages(), domain=domain)
    if not pages:
        return OperationResult(
            success=False,
            errors=[
                "no wiki pages matched the question; ingest some sources first "
                "(or scope to a different domain with --domain)"
            ],
        )

    pages_section = "\n\n".join(
        f"### {path.relative_to(paths.knowledge_root())}\n\n```\n{path.read_text()[:3000]}\n```"
        for path in pages
    )
    domain_section = f"## Scope: domain `{domain}`\n" if domain else ""
    slug_hint = _slugify(question)

    prompt = _QUERY_PROMPT_TEMPLATE.format(
        question=question,
        domain_section=domain_section,
        pages_section=pages_section,
        slug_hint=slug_hint,
    )

    try:
        raw_response = client.call(prompt)
    except Exception as e:
        return OperationResult(success=False, errors=[f"plan client failed: {e}"])

    try:
        plan = parse_plan_response(raw_response)
    except Exception as e:
        return OperationResult(
            success=False,
            errors=[f"could not parse plan: {e}", f"raw response: {raw_response[:500]!r}"],
        )

    return apply_plan(plan)
