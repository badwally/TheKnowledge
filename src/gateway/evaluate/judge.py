"""LLM-as-judge for the M50 evaluation framework (Phase C).

Uses TOK-1 ``AnthropicAPIClient`` so the judge system prompt (the rubric
+ schema description) gets prompt-cached across questions in the same
evaluation run. Sonnet 4.6 emits a structured JSON envelope; we parse
it into an ``EvalResult``.

One ``Judge`` instance per evaluation run — `cache_control` on the system
prompt accrues benefit only when the same prefix repeats across calls
within the 5-minute TTL.
"""

from __future__ import annotations

import json
import logging
import re

from gateway.evaluate.schema import EvalResult, Golden
from gateway.llm.api_client import AnthropicAPIClient
from gateway.llm.config import model_for

_log = logging.getLogger(__name__)


_JUDGE_SYSTEM_PROMPT = (
    "You are an evaluator scoring a knowledge wiki against a golden Q/A "
    "specification. The user will give you:\n"
    "1. A WIKI CONTEXT block (synthesis pages, concept pages, entity pages, "
    "and source bodies for one domain — each wrapped in <page> or <source> "
    "tags).\n"
    "2. A QUESTION the wiki should be able to answer.\n"
    "3. The GOLDEN expectations:\n"
    "   - `must_cite`: source IDs (bare, no `sources/` prefix) that should "
    "appear in the wiki's answer (via `[[sources/<id>]]` inline tokens or "
    "footnote-style `[N]` references whose footnote definitions map to "
    "that source).\n"
    "   - `must_assert`: natural-language facts the wiki must contain "
    "(paraphrase OK).\n"
    "   - `must_not_assert`: incorrect or outdated statements that, if "
    "found in the wiki, are violations.\n"
    "4. The `rubric_weight` dict: per-component scoring weights.\n\n"
    "Score by:\n"
    "- For each `must_cite` source-id, check whether the wiki context "
    "actually cites it. Populate `cite_hits` and `cite_misses`.\n"
    "- For each `must_assert` statement, semantically judge whether the "
    "wiki content asserts it (paraphrase OK). Populate `assertion_hits` "
    "and `assertion_misses`.\n"
    "- For each `must_not_assert` statement, check whether the wiki "
    "asserts it. Any match goes in `anti_assertion_violations`.\n"
    "- Compute a single `score` (0.0-1.0) using rubric_weight:\n"
    "  cite_ratio = len(cite_hits) / max(1, len(cite_hits)+len(cite_misses))\n"
    "  assert_ratio = len(assertion_hits) / max(1, len(assertion_hits)+len(assertion_misses))\n"
    "  anti_penalty = 1.0 if no violations else 0.0\n"
    "  score = w_cite * cite_ratio + w_assert * assert_ratio + w_anti * anti_penalty\n\n"
    "Emit STRICTLY this JSON shape — no prose, no markdown fences:\n\n"
    '{"score": <float>, '
    '"cite_hits": [<source-ids>], "cite_misses": [<source-ids>], '
    '"assertion_hits": [<statements>], "assertion_misses": [<statements>], '
    '"anti_assertion_violations": [<statements>], '
    '"reasoning": "<one-paragraph explanation>"}'
)


class Judge:
    """LLM-as-judge runner. One instance per evaluation run so the cached
    system prompt prefix gets the 5-minute TTL benefit across all questions."""

    def __init__(self, *, client: AnthropicAPIClient | None = None,
                 max_tokens: int = 4096):
        self._client = client if client is not None else AnthropicAPIClient()
        self._max_tokens = max_tokens

    def score(self, *, golden: Golden, wiki_context: str) -> EvalResult:
        # Split prompt so the large, stable wiki_context block gets
        # cache_control. The judge system prompt is ~60 tokens — below
        # Anthropic's 1024-token cache-eligibility floor — so caching it
        # alone produces 0% hit rate. The wiki_context block crosses the
        # floor and is identical across every question in the run.
        prefix = f"WIKI CONTEXT:\n\n{wiki_context}\n\n"
        suffix = _build_question_prompt(golden)
        call_result = self._client.call_with_usage(
            user_prompt=suffix,
            user_prompt_prefix=prefix,
            system_prompt=_JUDGE_SYSTEM_PROMPT,
            model=model_for("evaluate_judge"),
            max_tokens=self._max_tokens,
        )
        return _parse_judge_response(call_result, golden=golden)


def _build_question_prompt(golden: Golden) -> str:
    return (
        "QUESTION:\n\n"
        f"{golden.question}\n\n"
        "GOLDEN EXPECTATIONS:\n\n"
        f"must_cite: {json.dumps(golden.must_cite)}\n"
        f"must_assert: {json.dumps(golden.must_assert)}\n"
        f"must_not_assert: {json.dumps(golden.must_not_assert)}\n"
        f"rubric_weight: {json.dumps(golden.rubric_weight)}\n\n"
        "Emit the JSON envelope now."
    )


def _parse_judge_response(call_result, *, golden: Golden) -> EvalResult:
    raw = call_result.text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```\s*$", "", raw)

    # Skip any prose preamble before the first `{`. Sonnet sometimes emits
    # "Here is the evaluation:\n\n{...}" despite the strict-output instruction.
    brace = raw.find("{")
    if brace > 0:
        raw = raw[brace:]

    # Use raw_decode so trailing content after the JSON object doesn't fail
    # the parse — the M50 hand-test surfaced cases where Sonnet emits the
    # JSON envelope followed by additional commentary (which strict json.loads
    # rejects with `Extra data` at the first character past the object).
    decoder = json.JSONDecoder()
    try:
        payload, _end = decoder.raw_decode(raw)
    except json.JSONDecodeError as e:
        _log.warning(
            "Judge: malformed JSON for golden %s: %s; first 200 chars: %r",
            golden.id, e, raw[:200],
        )
        # Rescue path: extract score via regex so a single unescaped-quote
        # character in an assertion string doesn't zero out the golden.
        score_match = re.search(r'"score"\s*:\s*([0-9.]+)', raw)
        rescued_score = float(score_match.group(1)) if score_match else 0.0
        return EvalResult(
            golden_id=golden.id,
            question=golden.question,
            score=rescued_score,
            judge_reasoning=f"judge JSON parse failed (score rescued via regex): {e}",
            input_tokens=call_result.input_tokens,
            output_tokens=call_result.output_tokens,
            cache_read_tokens=call_result.cache_read_tokens,
        )

    return EvalResult(
        golden_id=golden.id,
        question=golden.question,
        score=float(payload.get("score", 0.0) or 0.0),
        cite_hits=list(payload.get("cite_hits") or []),
        cite_misses=list(payload.get("cite_misses") or []),
        assertion_hits=list(payload.get("assertion_hits") or []),
        assertion_misses=list(payload.get("assertion_misses") or []),
        anti_assertion_violations=list(payload.get("anti_assertion_violations") or []),
        judge_reasoning=str(payload.get("reasoning") or ""),
        input_tokens=call_result.input_tokens,
        output_tokens=call_result.output_tokens,
        cache_read_tokens=call_result.cache_read_tokens,
    )
