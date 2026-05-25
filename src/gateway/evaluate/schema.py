"""M50 schema.

Goldens are per-domain Q/A pairs at `.knowledge/eval/<domain>/goldens.yaml`.
Each entry describes one question and what a correct wiki answer must say + cite.

EvalResult is the per-question scoring output. EvalRunSummary aggregates
results into one run record persisted to disk.
"""

from __future__ import annotations

import logging
from dataclasses import asdict, dataclass, field
from pathlib import Path

import yaml

_log = logging.getLogger(__name__)


class SchemaError(ValueError):
    """Raised when a goldens.yaml file doesn't validate."""


@dataclass
class Golden:
    """One golden Q/A entry."""

    id: str
    question: str
    must_cite: list[str] = field(default_factory=list)
    must_assert: list[str] = field(default_factory=list)
    must_not_assert: list[str] = field(default_factory=list)
    rubric_weight: dict[str, float] = field(
        default_factory=lambda: {"cite": 0.4, "assert": 0.5, "anti": 0.1}
    )

    def __post_init__(self):
        for k in ("cite", "assert", "anti"):
            self.rubric_weight.setdefault(k, 0.0)


@dataclass
class EvalResult:
    """One question's scoring outcome."""

    golden_id: str
    question: str
    score: float
    cite_hits: list[str] = field(default_factory=list)
    cite_misses: list[str] = field(default_factory=list)
    assertion_hits: list[str] = field(default_factory=list)
    assertion_misses: list[str] = field(default_factory=list)
    anti_assertion_violations: list[str] = field(default_factory=list)
    judge_reasoning: str = ""
    cache_read_tokens: int = 0
    input_tokens: int = 0
    output_tokens: int = 0


@dataclass
class EvalRunSummary:
    """One run record. Persisted to disk as YAML."""

    domain: str
    timestamp: str
    n_questions: int
    mean_score: float
    results: list[EvalResult] = field(default_factory=list)
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cache_read_tokens: int = 0


_REQUIRED_FIELDS = ("id", "question", "must_cite", "must_assert", "must_not_assert")


def validate_rubric_weights(golden: Golden) -> list[str]:
    """Return warning messages if rubric_weight doesn't sum to ~1.0.

    Doesn't raise — partial keys are a footgun the user might still want.
    Caller logs the warnings via _log.warning.
    """
    s = sum(golden.rubric_weight.values())
    if 0.95 <= s <= 1.05:
        return []
    return [
        f"golden {golden.id!r} rubric_weight sums to {s:.3f} (expected ~1.0); "
        f"scoring math may be unintentional. weights: {dict(golden.rubric_weight)}"
    ]


def load_goldens(path: Path) -> list[Golden]:
    raw = yaml.safe_load(path.read_text()) or {}
    entries = raw.get("goldens") or []
    if not isinstance(entries, list):
        raise SchemaError("`goldens` must be a list")

    seen_ids: set[str] = set()
    out: list[Golden] = []
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise SchemaError(f"goldens[{i}] is not a mapping")
        for required in _REQUIRED_FIELDS:
            if required not in entry:
                raise SchemaError(f"goldens[{i}] missing required field: {required}")
        gid = entry["id"]
        if gid in seen_ids:
            raise SchemaError(f"goldens[{i}] duplicate id: {gid!r}")
        seen_ids.add(gid)
        rw = entry.get("rubric_weight") or {}
        if not isinstance(rw, dict):
            raise SchemaError(f"goldens[{i}] rubric_weight must be a mapping")
        for k, v in rw.items():
            if not isinstance(v, (int, float)):
                raise SchemaError(
                    f"goldens[{i}] rubric_weight[{k!r}] must be numeric, got {type(v).__name__}"
                )
        # Only pass rubric_weight when YAML supplied one — otherwise let the
        # dataclass default_factory ({cite:0.4, assert:0.5, anti:0.1}) fire.
        # Passing an empty dict here would bypass the default and __post_init__
        # would fill 0.0s instead.
        kwargs = dict(
            id=str(gid),
            question=str(entry["question"]),
            must_cite=list(entry.get("must_cite") or []),
            must_assert=list(entry.get("must_assert") or []),
            must_not_assert=list(entry.get("must_not_assert") or []),
        )
        if rw:
            kwargs["rubric_weight"] = dict(rw)
        out.append(Golden(**kwargs))
    for g in out:
        for w in validate_rubric_weights(g):
            _log.warning("schema: %s", w)
    return out


def save_goldens(path: Path, goldens: list[Golden]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"goldens": [asdict(g) for g in goldens]}
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))


def scaffold_template(path: Path, *, domain: str) -> Path:
    """Write a placeholder goldens.yaml. Refuses to overwrite an existing file."""
    if path.exists():
        raise FileExistsError(f"{path} already exists; refusing to overwrite")
    placeholder = Golden(
        id="q01",
        question=f"EXAMPLE: replace with a real question about {domain}. Edit me.",
        must_cite=["EXAMPLE-source-id"],
        must_assert=["EXAMPLE: a key fact a correct answer must contain"],
        must_not_assert=["EXAMPLE: a wrong assertion that would fail this golden"],
    )
    save_goldens(path, [placeholder])
    return path
