"""Filter call: build prompt, invoke Claude, parse response.

The default `FilterClient` shells out to `claude -p` so the user's Max-plan
auth is reused without an `ANTHROPIC_API_KEY`. Tests inject mocks via
`score(..., client=MyMockClient())`.

M44: the default client now delegates to `gateway.llm.ClaudeCLIClient` with
``--bare --tools "" --model <Haiku> --system-prompt <policy+examples>`` to
strip the Claude Code agent harness per call and route filter to Haiku 4.5
(binary triage). The `FilterClient` Protocol is unchanged so injected stubs
and lint callers (which build their own prompts) continue to work.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import re
import time
from typing import Callable, Protocol

import yaml

from gateway.filter.examples import Example
from gateway.filter.policy import Policy
from gateway.llm import CallResult, ClaudeCLIClient, LLMError, model_for
from gateway.log import log_llm_call


class FilterError(RuntimeError):
    """Raised when the filter call fails or returns an unparseable response."""


@dataclass
class FilterResult:
    score: float
    rationale: str
    policy_version: str
    decided_at: str

    def to_frontmatter_block(self) -> dict:
        """Shape per WIKI.md § 3.1 `filter:` block (without user_correction)."""
        return {
            "score": round(self.score, 3),
            "policy_version": self.policy_version,
            "rationale": self.rationale,
            "decided_at": self.decided_at,
            "user_correction": None,
        }


class FilterClient(Protocol):
    """Anything that takes a prompt string and returns a response string."""

    def call(self, prompt: str) -> str: ...


class ClaudeCLIFilterClient:
    """Default backend: `claude -p <prompt>` subprocess call.

    Reuses the user's Claude Code Max-plan authentication. Slow per call
    (~5–30s) but correct for the use case (single source per ingest).

    M44: delegates argv construction, retry, and the subprocess call itself
    to `gateway.llm.ClaudeCLIClient`. Exposes both:

    - ``call(prompt)`` — Protocol-compatible: sends the whole prompt as the
      user positional with no system prompt. Used by lint callers that
      build their own prompts.
    - ``call_split(system, user)`` — optimized: sends ``system`` via
      ``--system-prompt`` (stripped of agent harness via ``--bare --tools \"\"``)
      and ``user`` as the positional. Used by ``score()`` to cut per-call
      token cost.

    Routes to Haiku 4.5 by default (binary triage). Override via ``model=``.
    """

    def __init__(
        self,
        executable: str = "claude",
        timeout_s: float = 120.0,
        max_retries: int = 3,
        retry_base_s: float = 5.0,
        sleep: Callable[[float], None] = time.sleep,
        *,
        model: str | None = None,
        cli: ClaudeCLIClient | None = None,
    ):
        self._model = model or model_for("filter")
        self._cli = cli or ClaudeCLIClient(
            executable=executable,
            timeout_s=timeout_s,
            max_retries=max_retries,
            retry_base_s=retry_base_s,
            sleep=sleep,
        )

    def call(self, prompt: str) -> str:
        """Backwards-compatible single-string entry point (no system split)."""
        return self._invoke(system_prompt=None, user_prompt=prompt)

    def call_split(self, *, system: str, user: str) -> str:
        """M44 optimized entry: system prefix via --system-prompt."""
        return self._invoke(system_prompt=system, user_prompt=user)

    def call_with_usage(self, prompt: str) -> CallResult:
        """K5 telemetry variant of ``call(prompt)``."""
        return self._invoke_with_usage(system_prompt=None, user_prompt=prompt)

    def call_split_with_usage(self, *, system: str, user: str) -> CallResult:
        """K5 telemetry variant of ``call_split``.

        Returns a ``CallResult`` so the caller can record per-call usage
        via ``log_llm_call("filter", result)``.
        """
        return self._invoke_with_usage(system_prompt=system, user_prompt=user)

    def _invoke(self, *, system_prompt: str | None, user_prompt: str) -> str:
        try:
            return self._cli.call(
                user_prompt=user_prompt,
                system_prompt=system_prompt,
                model=self._model,
                tools="",
            )
        except LLMError as e:
            raise FilterError(str(e)) from e

    def _invoke_with_usage(
        self, *, system_prompt: str | None, user_prompt: str
    ) -> CallResult:
        try:
            return self._cli.call_with_usage(
                user_prompt=user_prompt,
                system_prompt=system_prompt,
                model=self._model,
                tools="",
            )
        except LLMError as e:
            raise FilterError(str(e)) from e


# --- prompt construction ----------------------------------------------------
#
# M44 splits the prompt into two pieces: a static system prefix (policy +
# examples + instructions, identical across all candidates in a research run)
# and a per-item user payload (frontmatter + body head). Passed to the CLI as
# `--system-prompt <prefix>` plus the positional user prompt. `build_prompt()`
# is preserved as a backwards-compatible concat for callers that still want
# one string.


_SYSTEM_PROMPT_TEMPLATE = """\
You are a semantic relevance filter for a personal research knowledge base.
Score the source provided in the user message against the editorial policy
and respond with a single JSON object.

## Editorial policy

```yaml
{policy_yaml}
```

## Past decisions for calibration

{examples_section}

## Instructions

Score the source's relevance to the editorial policy on a 0.0–1.0 scale where:

- 1.0 — strongly matches inclusion criteria, high-quality, must include
- 0.7 — clearly relevant, should be included
- 0.5 — ambiguous; merits human review
- 0.3 — marginal relevance
- 0.0 — clearly fails (violates exclusion criteria, low quality, off-topic)

Respond with ONLY a JSON object, no surrounding text or code fences:
{{"score": <0.0-1.0>, "rationale": "<1-2 sentences explaining the score>"}}
"""


_USER_PROMPT_TEMPLATE = """\
## Source under evaluation

{source_section}
"""


def build_system_prompt(policy: Policy, examples: list[Example]) -> str:
    """Static prefix: policy + examples + scoring instructions.

    Identical across all candidates in a single research run.
    """
    policy_yaml = yaml.safe_dump(policy.raw, sort_keys=False, default_flow_style=False, allow_unicode=True).rstrip()
    return _SYSTEM_PROMPT_TEMPLATE.format(
        policy_yaml=policy_yaml,
        examples_section=_format_examples(examples),
    )


def build_user_prompt(front: dict, body_head: str) -> str:
    """Per-item payload: source frontmatter + body head."""
    return _USER_PROMPT_TEMPLATE.format(
        source_section=_format_source(front, body_head),
    )


def build_prompt(
    policy: Policy,
    examples: list[Example],
    front: dict,
    body_head: str,
) -> str:
    """Backwards-compatible monolithic prompt (system + user concatenated)."""
    return build_system_prompt(policy, examples) + "\n" + build_user_prompt(front, body_head)


def _format_examples(examples: list[Example]) -> str:
    if not examples:
        return "_(no past examples yet — apply the policy directly)_"
    blocks = []
    for ex in examples:
        blocks.append(
            f"- **{ex.decision}** ({ex.score:.2f}, {ex.pinned_by}): "
            f"{ex.rationale.strip() or '(no rationale)'} "
            f"[id={ex.source_id}]"
        )
    return "\n".join(blocks)


def _format_source(front: dict, body_head: str) -> str:
    interesting_fields = {
        k: front.get(k)
        for k in ("type", "title", "url", "authors", "published_at", "domains", "meta")
        if front.get(k) not in (None, [], {})
    }
    front_yaml = yaml.safe_dump(interesting_fields, sort_keys=False, allow_unicode=True).rstrip()
    return f"### Frontmatter\n\n```yaml\n{front_yaml}\n```\n\n### Body (truncated)\n\n{body_head}"


def _truncate(body: str, max_chars: int) -> str:
    if len(body) <= max_chars:
        return body
    return body[:max_chars].rstrip() + "\n\n... [truncated for filter scoring]"


# --- response parsing -------------------------------------------------------


_JSON_OBJECT_RE = re.compile(r"\{[^{}]*\}", re.DOTALL)


def parse_response(text: str) -> tuple[float, str]:
    """Pull (score, rationale) out of a Claude response string."""
    if not text or not text.strip():
        raise FilterError("empty response from filter client")

    cleaned = text.strip()
    if cleaned.startswith("```"):
        # strip code-fence wrapper if present
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    obj = None
    try:
        obj = json.loads(cleaned)
    except json.JSONDecodeError:
        match = _JSON_OBJECT_RE.search(cleaned)
        if match:
            try:
                obj = json.loads(match.group(0))
            except json.JSONDecodeError as e:
                raise FilterError(f"could not parse JSON in filter response: {e}") from e

    if not isinstance(obj, dict):
        raise FilterError(f"filter response did not contain a JSON object: {cleaned[:200]!r}")
    if "score" not in obj or "rationale" not in obj:
        raise FilterError(f"filter response missing 'score' or 'rationale': {obj!r}")

    try:
        score = float(obj["score"])
    except (TypeError, ValueError) as e:
        raise FilterError(f"score not a number: {obj['score']!r}") from e

    if not 0.0 <= score <= 1.0:
        raise FilterError(f"score out of range [0.0, 1.0]: {score}")

    rationale = str(obj["rationale"]).strip()
    if not rationale:
        rationale = "(no rationale provided)"

    return score, rationale


# --- public score function --------------------------------------------------


def score(
    front: dict,
    body: str,
    policy: Policy,
    examples: list[Example] | None = None,
    client: FilterClient | None = None,
    body_head_chars: int = 16000,
) -> FilterResult:
    """Run the filter end-to-end and return a structured result.

    M44: prefers the client's `call_split(system, user)` if available so
    the policy + examples prefix is sent via ``--system-prompt`` (stripped
    of the Claude Code agent harness via ``--bare --tools \"\"``). Falls
    back to single-prompt `call(prompt)` for stubs and clients that don't
    implement the split path.
    """
    examples = examples if examples is not None else []
    client = client or ClaudeCLIFilterClient()

    body_head = _truncate(body, body_head_chars)
    system = build_system_prompt(policy, examples)
    user = build_user_prompt(front, body_head)

    # K5: prefer call_split_with_usage so per-call telemetry lands in log.md.
    # Tests injecting bare stubs without the telemetry method fall back to
    # call_split (M44 path) and silently skip telemetry — that's intended.
    call_split_with_usage = getattr(client, "call_split_with_usage", None)
    call_split = getattr(client, "call_split", None)
    if callable(call_split_with_usage):
        result = call_split_with_usage(system=system, user=user)
        log_llm_call("filter", result)
        raw = result.text
    elif callable(call_split):
        raw = call_split(system=system, user=user)
    else:
        raw = client.call(system + "\n" + user)

    s, rationale = parse_response(raw)

    return FilterResult(
        score=s,
        rationale=rationale,
        policy_version=f"{policy.domain_slug}-{policy.version}",
        decided_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
