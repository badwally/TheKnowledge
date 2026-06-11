"""`wiki answer` — local grounded synthesis (WS6, 2026-06-09 RAG review).

The cheap, NotebookLM-independent complement to `wiki query`:

    retrieve (WS2) → one Claude call grounded ONLY in the retrieved sections
    → answer that cites only [[sources/<id>]] present in the context.

`wiki query` synthesizes over a domain's *raw corpus* through NotebookLM
(heavy, quota-bound). `wiki answer` answers "what does my wiki already know"
from the *authored wiki layer* in seconds. It makes an LLM call, so — like
artifact generation — it is explicit-invocation only, never auto-triggered.

Confabulation guard: the model is instructed to answer only from the
provided context, and any `[[sources/<id>]]` it emits that did not appear in
the retrieved block is stripped post-hoc. The retrieved block is sent as a
cached prompt prefix (M50.1 pattern) so repeated questions over the same
neighborhood reuse the cache.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone

from gateway import frontmatter as fm, log, paths
from gateway.core import OperationResult
from gateway.ops.retrieve import RetrievedSection, retrieve

_SOURCE_LINK_RE = re.compile(r"\[\[sources/([^\]|#]+)\]\]")
_DEFAULT_MODEL = "claude-sonnet-4-6"
_DEFAULT_MAX_TOKENS = 1500

_SYSTEM_PROMPT = (
    "You answer questions strictly from the wiki context provided in the user "
    "message. Rules:\n"
    "1. Use ONLY facts stated in the <page> blocks. Do not add outside knowledge.\n"
    "2. Every claim must be followed by the [[sources/<id>]] citation(s) that "
    "appear in the context block supporting it. Copy citations verbatim.\n"
    "3. If the context does not answer the question, say so plainly. Do not "
    "speculate or fill gaps from training data.\n"
    "4. Be concise and concrete. No preamble."
)


@dataclass
class AnswerResult:
    answer: str
    sections: list[RetrievedSection] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)  # ids cited & valid
    stripped: list[str] = field(default_factory=list)     # confabulated cites removed
    usage: dict = field(default_factory=dict)


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _valid_source_ids(block: str) -> set[str]:
    return set(_SOURCE_LINK_RE.findall(block))


def _strip_confabulated(answer: str, valid: set[str]) -> tuple[str, list[str]]:
    """Remove [[sources/<id>]] links whose id is not in the retrieved context."""
    stripped: list[str] = []

    def _sub(m: re.Match) -> str:
        sid = m.group(1)
        if sid in valid:
            return m.group(0)
        stripped.append(sid)
        return ""

    return _SOURCE_LINK_RE.sub(_sub, answer).strip(), stripped


def answer(
    question: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = 12,
    budget_chars: int = 40_000,
    client=None,
    model: str | None = None,
) -> AnswerResult:
    """Retrieve grounding context and produce a cited answer.

    `client` is any object with `call_with_usage(...)->CallResult` (the
    AnthropicAPIClient interface); injected in tests. Constructed lazily from
    `ANTHROPIC_API_KEY_RESEARCH` when omitted. When `domains` names ≥2 domains
    the grounding block is balanced by a per-domain quota merge (see
    `retrieve`); `domains` takes precedence over the single `domain`.
    """
    block, sections = retrieve(
        question, domain=domain, domains=domains, k=k, budget_chars=budget_chars
    )
    if not sections:
        return AnswerResult(answer="", sections=[])

    if client is None:
        from gateway.llm.api_client import AnthropicAPIClient
        client = AnthropicAPIClient()

    prefix = f"WIKI CONTEXT:\n\n{block}\n\n"
    result = client.call_with_usage(
        user_prompt=f"Question: {question}",
        user_prompt_prefix=prefix,
        system_prompt=_SYSTEM_PROMPT,
        model=model or _DEFAULT_MODEL,
        max_tokens=_DEFAULT_MAX_TOKENS,
    )

    valid = _valid_source_ids(block)
    cleaned, stripped = _strip_confabulated(result.text or "", valid)
    cited = [sid for sid in dict.fromkeys(_SOURCE_LINK_RE.findall(cleaned))]
    usage = {
        "output_tokens": getattr(result, "output_tokens", 0),
        "input_tokens": getattr(result, "input_tokens", 0),
        "cache_read_tokens": getattr(result, "cache_read_tokens", 0),
    }
    return AnswerResult(
        answer=cleaned, sections=sections, source_ids=cited,
        stripped=stripped, usage=usage,
    )


def answer_op(
    question: str,
    *,
    domain: str | None = None,
    domains: list[str] | None = None,
    k: int = 12,
    budget_chars: int = 40_000,
    file_draft: bool = False,
    client=None,
    model: str | None = None,
    caller: str | None = None,
) -> OperationResult:
    """CLI/MCP entry: grounded answer, optionally filed as a draft synthesis.

    `file_draft=True` writes the answer to wiki/synthesis/ via the gateway's
    apply_plan path (always as a draft — citation grounding is then checked at
    `wiki finalize`). `domains` (≥2) balances the grounding context across the
    named domains and files list-valued `domains:` frontmatter.
    """
    domain_label = ",".join(domains) if domains else (domain or "")
    res = answer(question, domain=domain, domains=domains, k=k,
                 budget_chars=budget_chars, client=client, model=model)
    if not res.sections:
        return OperationResult(
            success=False,
            summary=f"no wiki context found for {question!r}"
            + (f" in domain {domain!r}" if domain else ""),
        )
    if not res.answer:
        return OperationResult(
            success=False,
            summary="model returned an empty answer",
        )

    log.append(
        op="answer",
        fields={
            "caller": caller or "",
            "question": question,
            "domain": domain_label,
            "sections": len(res.sections),
            "cited": len(res.source_ids),
            "stripped": len(res.stripped),
            "output_tokens": res.usage.get("output_tokens", 0),
        },
        summary=(
            f"answer: {question!r} domain={domain_label or '-'} "
            f"sections={len(res.sections)} cited={len(res.source_ids)} "
            f"stripped={len(res.stripped)}"
        ),
    )

    data = {
        "question": question,
        "domain": domain_label or None,
        "answer": res.answer,
        "source_ids": res.source_ids,
        "stripped": res.stripped,
        "usage": res.usage,
    }

    if file_draft:
        filed = _file_draft(question, domain, res, domains=domains)
        if filed.success:
            data["filed_path"] = filed.summary
        return OperationResult(
            success=filed.success,
            summary=res.answer,
            paths_touched=[paths.log_path()],
            warnings=filed.errors,
            data=data,
        )

    return OperationResult(
        success=True,
        summary=res.answer,
        paths_touched=[paths.log_path()],
        data=data,
    )


def _file_draft(
    question: str, domain: str | None, res: AnswerResult,
    *, domains: list[str] | None = None,
) -> OperationResult:
    """Write the answer as a draft synthesis page via apply_plan."""
    import hashlib
    from gateway.ops.apply_plan import apply_plan
    from gateway.plan import Plan, WikiUpdate

    def _slug(text: str) -> str:
        words = re.findall(r"[a-z0-9]+", text.lower())[:6]
        return "-".join(words) or "answer"

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = f"{today}-{_slug(question)}"
    if (paths.knowledge_root() / "wiki" / "synthesis" / f"{slug}.md").exists():
        slug = f"{slug}-{hashlib.sha256(question.encode()).hexdigest()[:6]}"
    rel = f"wiki/synthesis/{slug}.md"

    now = _now_iso()
    front = {
        "type": "synthesis",
        "slug": slug,
        "title": question.strip().rstrip("?"),
        "domains": list(domains) if domains else ([domain] if domain else []),
        "question": question,
        "created_at": now,
        "last_updated": now,
        "sources_count": len(res.source_ids),
        "provenance": "wiki-answer",  # local grounded synthesis, not NLM
    }
    body = "\n".join([
        f"# {front['title']}", "", "## Synthesis", "", res.answer, "",
        "## Sources cited", "",
        *([f"- [[sources/{sid}]]" for sid in res.source_ids] or ["_(none)_"]),
        "",
    ])
    plan = Plan(
        source_id=f"answer-{slug}",
        rationale=f"wiki answer (local grounded synthesis) for "
                  f"{','.join(domains) if domains else (domain or 'cross-domain')}",
        updates=[WikiUpdate(
            target_path=rel, update_kind="create",
            content=fm.serialize(front, body),
            rationale="filed local grounded answer",
        )],
    )
    result = apply_plan(plan, draft=True)
    return OperationResult(success=result.success, summary=rel, errors=result.errors)
