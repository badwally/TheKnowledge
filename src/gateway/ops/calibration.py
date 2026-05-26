"""QUAL-10: Held-out calibration set for filter policy evaluation.

A calibration set lives at `.knowledge/policies/<domain>/calibration_set.yaml`.
It contains 30–50 manually-labelled examples (source_id + ground-truth decision)
that are NOT in the example bank used for distillation. They serve as a held-out
test: after distillation produces a candidate policy, the candidate criteria are
scored against the calibration set to measure precision/recall/F1.

Calibration entry schema:
  source_id: str
  decision: "include" | "exclude"
  rationale: str
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from gateway import paths
from gateway.filter.semantic import FilterClient


@dataclass
class CalibrationEntry:
    source_id: str
    decision: str  # "include" | "exclude"
    rationale: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "decision": self.decision,
            "rationale": self.rationale,
        }


@dataclass
class CalibrationMetrics:
    n_examples: int
    correct: int
    incorrect: int
    true_positives: int
    false_positives: int
    false_negatives: int
    precision: float
    recall: float
    f1: float
    accuracy: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "n_examples": self.n_examples,
            "correct": self.correct,
            "incorrect": self.incorrect,
            "precision": round(self.precision, 3),
            "recall": round(self.recall, 3),
            "f1": round(self.f1, 3),
            "accuracy": round(self.accuracy, 3),
        }


def calibration_path(domain: str) -> Path:
    return paths.policies_dir() / domain / "calibration_set.yaml"


def load_calibration_set(domain: str) -> list[CalibrationEntry]:
    """Load calibration entries for a domain. Returns [] if file absent."""
    p = calibration_path(domain)
    if not p.is_file():
        return []
    try:
        raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception:
        return []
    if not isinstance(raw, list):
        return []
    entries = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        src = item.get("source_id")
        dec = item.get("decision")
        if src and dec in ("include", "exclude"):
            entries.append(
                CalibrationEntry(
                    source_id=str(src),
                    decision=str(dec),
                    rationale=str(item.get("rationale", "")),
                )
            )
    return entries


def add_calibration_entry(domain: str, entry: CalibrationEntry) -> None:
    """Append a new calibration entry; no-op if source_id already present."""
    p = calibration_path(domain)
    existing = load_calibration_set(domain)
    if any(e.source_id == entry.source_id for e in existing):
        return
    existing.append(entry)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        yaml.safe_dump(
            [e.to_dict() for e in existing],
            sort_keys=False,
            allow_unicode=True,
        ),
        encoding="utf-8",
    )


def _build_scoring_prompt(
    entry: CalibrationEntry,
    inclusion_criteria: list[str],
    exclusion_criteria: list[str],
    source_content: str,
) -> str:
    lines = [
        "You are a strict binary classifier for an editorial filter.",
        "",
        "Inclusion criteria (source MUST satisfy at least one):",
    ]
    for c in inclusion_criteria:
        lines.append(f"  - {c}")
    lines += ["", "Exclusion criteria (any match means exclude):"]
    for c in exclusion_criteria:
        lines.append(f"  - {c}")
    lines += [
        "",
        f"Source excerpt:\n{source_content[:1500]}",
        "",
        'Respond with exactly one word: "include" or "exclude".',
    ]
    return "\n".join(lines)


def _load_source_excerpt(source_id: str) -> str:
    """Load the first 1500 chars of the source body from raw/."""
    for type_dir in sorted(paths.raw_dir().iterdir()):
        if not type_dir.is_dir():
            continue
        candidate = type_dir / f"{source_id}.md"
        if candidate.is_file():
            return candidate.read_text(encoding="utf-8")[:1500]
    return f"source_id: {source_id}"


def score_calibration(
    domain: str,
    inclusion_criteria: list[str],
    exclusion_criteria: list[str],
    *,
    client: FilterClient,
) -> CalibrationMetrics | None:
    """Score candidate policy criteria against the domain's calibration set.

    Returns None if the calibration set is absent or empty.
    """
    entries = load_calibration_set(domain)
    if not entries:
        return None

    tp = fp = fn = correct = incorrect = 0

    for entry in entries:
        excerpt = _load_source_excerpt(entry.source_id)
        prompt = _build_scoring_prompt(
            entry, inclusion_criteria, exclusion_criteria, excerpt
        )
        raw = client.call(prompt).strip().lower()
        predicted = "include" if "include" in raw else "exclude"

        if predicted == entry.decision:
            correct += 1
            if predicted == "include":
                tp += 1
        else:
            incorrect += 1
            if predicted == "include":
                fp += 1
            else:
                fn += 1

    n = len(entries)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )
    accuracy = correct / n if n > 0 else 0.0

    return CalibrationMetrics(
        n_examples=n,
        correct=correct,
        incorrect=incorrect,
        true_positives=tp,
        false_positives=fp,
        false_negatives=fn,
        precision=precision,
        recall=recall,
        f1=f1,
        accuracy=accuracy,
    )
