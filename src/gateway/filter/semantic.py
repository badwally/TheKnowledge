"""Filter call: build prompt, invoke Claude, parse response.

The default `FilterClient` shells out to `claude -p` so the user's Max-plan
auth is reused without an `ANTHROPIC_API_KEY`. Tests inject mocks via
`score(..., client=MyMockClient())`.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import re
import subprocess
from typing import Protocol

import yaml

from gateway.filter.examples import Example
from gateway.filter.policy import Policy


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
    """

    def __init__(self, executable: str = "claude", timeout_s: float = 120.0):
        self._exe = executable
        self._timeout = timeout_s

    def call(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                [self._exe, "-p", prompt],
                capture_output=True,
                text=True,
                timeout=self._timeout,
                check=False,
            )
        except FileNotFoundError as e:
            raise FilterError(f"`{self._exe}` not found on PATH; install Claude Code or inject a FilterClient") from e
        except subprocess.TimeoutExpired as e:
            raise FilterError(f"`{self._exe} -p` timed out after {self._timeout}s") from e

        if result.returncode != 0:
            raise FilterError(
                f"`{self._exe} -p` exited {result.returncode}: {result.stderr.strip()[:300]}"
            )
        return result.stdout


# --- prompt construction ----------------------------------------------------


_PROMPT_TEMPLATE = """\
You are a semantic relevance filter for a personal research knowledge base.
Score the source below against the editorial policy and respond with a single JSON object.

## Editorial policy

```yaml
{policy_yaml}
```

## Past decisions for calibration

{examples_section}

## Source under evaluation

{source_section}

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


def build_prompt(
    policy: Policy,
    examples: list[Example],
    front: dict,
    body_head: str,
) -> str:
    policy_yaml = yaml.safe_dump(policy.raw, sort_keys=False, default_flow_style=False, allow_unicode=True).rstrip()
    return _PROMPT_TEMPLATE.format(
        policy_yaml=policy_yaml,
        examples_section=_format_examples(examples),
        source_section=_format_source(front, body_head),
    )


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
    """Run the filter end-to-end and return a structured result."""
    examples = examples if examples is not None else []
    client = client or ClaudeCLIFilterClient()

    body_head = _truncate(body, body_head_chars)
    prompt = build_prompt(policy, examples, front, body_head)
    raw = client.call(prompt)
    s, rationale = parse_response(raw)

    return FilterResult(
        score=s,
        rationale=rationale,
        policy_version=f"{policy.domain_slug}-{policy.version}",
        decided_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
