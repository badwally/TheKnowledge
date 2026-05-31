# `wiki bootstrap-domain` Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `wiki bootstrap-domain "<description>" <slug>` to author a starter `policy.yaml` from a natural-language description, restoring the predecessor's top-down green-field workflow.

**Architecture:** New gateway op that calls the plan client with a structured prompt (description + schema + a single synthetic reference policy), validates the response against a strict policy schema (with minimum-specificity gates), and writes to `.knowledge/policies/<slug>/policy.yaml`. Adds `wiki refine-domain` as the cargo-cult-prevention twin: re-runs against an existing policy with the existing policy provided as the reference (intra-domain self-improvement, no cross-domain leakage).

**Bug-prevention measures baked in:**
- **#5 (empty criteria):** Two-layer defense — prompt requires minimum counts, validator enforces them; failure triggers single retry then draft-save.
- **#6 (cargo-culting):** Single synthetic reference policy ("Patagonian glacier hydrology"), never real domains; round-trip tested.
- **#1 (collision with promoted policy):** Refuse if `auto_generated_from_proposal: true`, point at `demote-domain`. `--force` allowed but logged WARN.
- **#2 (collision with proposal):** Refuse if `wiki/proposals/<slug>.md` exists with `status: draft`, no `--force` override.
- **#3 (schema drift):** `policy_schema_version` field; round-trip test of reference policy guarantees schema/reference stay in sync.

**Complications mitigated:**
- **Validator retrofit:** New validator runs in `strict` mode for bootstrap output and `lenient` mode for legacy policy load. Existing policies don't need changes; lenient mode logs schema-version-missing as INFO only.
- **Reference policy drift:** Round-trip test: load `_bootstrap_reference_policy.yaml`, run strict validator, must pass. Schema additions break this test until the reference is updated.

**Tech Stack:** Python 3.11+, pytest, existing `gateway.plan.PlanClient`, `gateway.filter.policy.Policy`, YAML.

---

### Task 1: Synthetic reference policy + strict validator skeleton

**Files:**
- Create: `src/gateway/ops/_bootstrap_reference_policy.yaml`
- Create: `src/gateway/ops/policy_validator.py`
- Test: `tests/gateway/test_policy_validator.py`

- [ ] **Step 1: Write the synthetic reference policy**

Create `src/gateway/ops/_bootstrap_reference_policy.yaml` with deliberately fictional content that demonstrates the schema without leaking real domain information:

```yaml
version: v1
policy_schema_version: 1
domain:
  slug: patagonian-glacier-hydrology
  topic: Glacier hydrology and meltwater dynamics in Patagonia
  field: Glaciology, hydrology, and climate science
  description: Field measurements, remote sensing, and modeling of glacier mass
    balance and meltwater flow in the Patagonian ice fields, with focus on
    seasonal variability and downstream water-resource implications.
filter:
  threshold_include: 0.7
  threshold_review: 0.5
  example_count_in_prompt: 12
  example_strategy: balanced
inclusion_criteria:
  - Discusses glacier mass balance measurements (GPS, GRACE, in-situ stake networks)
    in Patagonian ice fields
  - Covers meltwater discharge modeling with hydrological coupling to downstream
    river systems
  - Reports remote-sensing methodologies (satellite altimetry, SAR, optical) applied
    to glacier surface change detection
  - Examines seasonal or interannual variability in glacial runoff with quantified
    measurements
exclusion_criteria:
  - Generic climate-change advocacy without specific glaciological measurements
  - Tourism or expedition narratives without scientific content
  - Studies of non-Patagonian glaciers unless used for direct methodological comparison
quality_signals:
  publication_venue:
    positive_signals:
      - Peer-reviewed glaciology, hydrology, or cryosphere journals (Journal of
        Glaciology, The Cryosphere, Hydrological Processes)
      - Conference proceedings from IGS, AGU, EGU
    negative_signals:
      - Predatory open-access venues with no peer review
      - Press releases without underlying paper reference
  methodology_rigor:
    positive_signals:
      - Reports field campaigns with stake networks, GPS surveys, or repeat photography
      - Cross-validates remote-sensing results against in-situ measurements
      - Quantifies measurement uncertainty
    negative_signals:
      - Single-source data without independent validation
      - No discussion of error bounds or limitations
  content_depth:
    positive_signals:
      - Presents multi-year time series with statistical analysis
      - Discusses physical mechanisms driving observed trends
    negative_signals:
      - Surface-level summaries without underlying data
      - Pure modeling work with no observational grounding
```

- [ ] **Step 2: Write failing tests for policy_validator**

Create `tests/gateway/test_policy_validator.py`:

```python
"""Tests for the strict/lenient policy validator (M39 bootstrap-domain)."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from gateway.ops.policy_validator import (
    PolicyValidationError,
    REFERENCE_POLICY_PATH,
    validate_policy,
)


def _load_reference() -> dict:
    return yaml.safe_load(REFERENCE_POLICY_PATH.read_text())


def test_reference_policy_passes_strict_validation():
    """Round-trip guarantee: schema additions break this test until the reference is updated."""
    data = _load_reference()
    result = validate_policy(data, mode="strict")
    assert result.ok, [str(e) for e in result.errors]


def test_strict_rejects_missing_inclusion_criteria():
    data = _load_reference()
    data["inclusion_criteria"] = []
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("inclusion_criteria" in str(e) for e in result.errors)


def test_strict_rejects_too_few_inclusion_criteria():
    data = _load_reference()
    data["inclusion_criteria"] = ["only one"]
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("at least 3" in str(e).lower() for e in result.errors)


def test_strict_rejects_missing_exclusion_criteria():
    data = _load_reference()
    data["exclusion_criteria"] = []
    result = validate_policy(data, mode="strict")
    assert not result.ok


def test_strict_rejects_too_few_quality_signals():
    data = _load_reference()
    data["quality_signals"] = {"only_one_category": {"positive_signals": ["x", "y"]}}
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("quality_signals" in str(e).lower() for e in result.errors)


def test_strict_rejects_threshold_out_of_range():
    data = _load_reference()
    data["filter"]["threshold_include"] = 1.5
    result = validate_policy(data, mode="strict")
    assert not result.ok


def test_strict_rejects_invalid_slug():
    data = _load_reference()
    data["domain"]["slug"] = "BadSlug"
    result = validate_policy(data, mode="strict")
    assert not result.ok


def test_strict_rejects_unknown_top_level_keys():
    data = _load_reference()
    data["mystery_field"] = "lurking"
    result = validate_policy(data, mode="strict")
    assert not result.ok
    assert any("unknown" in str(e).lower() and "mystery_field" in str(e) for e in result.errors)


def test_lenient_allows_empty_inclusion_criteria():
    """Legacy auto-generated policies have empty criteria; must keep loading."""
    data = _load_reference()
    data["inclusion_criteria"] = []
    data["exclusion_criteria"] = []
    result = validate_policy(data, mode="lenient")
    assert result.ok, [str(e) for e in result.errors]


def test_lenient_allows_missing_schema_version():
    data = _load_reference()
    data.pop("policy_schema_version", None)
    result = validate_policy(data, mode="lenient")
    assert result.ok
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_policy_validator.py -v`
Expected: FAIL — `gateway.ops.policy_validator` does not exist

- [ ] **Step 4: Implement policy_validator**

Create `src/gateway/ops/policy_validator.py`:

```python
"""Strict + lenient policy validation for bootstrap-domain and legacy load.

Strict mode runs on output of `wiki bootstrap-domain` to prevent vague or
under-specified policies from entering the system. Lenient mode runs on
existing policy load (e.g. `wiki research`) so legacy auto-generated
policies (M36 promote-domain) keep working without modification.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re


REFERENCE_POLICY_PATH = Path(__file__).parent / "_bootstrap_reference_policy.yaml"

POLICY_SCHEMA_VERSION = 1

_MIN_INCLUSION = 3
_MIN_EXCLUSION = 1
_MIN_QUALITY_CATEGORIES = 2
_MIN_SIGNALS_PER_CATEGORY = 2

_KNOWN_TOP_LEVEL = {
    "version",
    "policy_schema_version",
    "domain",
    "filter",
    "inclusion_criteria",
    "exclusion_criteria",
    "quality_signals",
    "auto_generated",
    "auto_generated_from_proposal",
    "bootstrapped_from_description_hash",
}

_SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class PolicyValidationError(ValueError):
    """Raised by callers that want exception-shaped failures."""


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_policy(data: dict, *, mode: str = "lenient") -> ValidationResult:
    """Validate a policy mapping.

    `mode="strict"` enforces minimum specificity (used for bootstrap output).
    `mode="lenient"` runs only structural checks (used for legacy policy load).
    """
    if mode not in ("strict", "lenient"):
        raise ValueError(f"unknown validation mode: {mode!r}")

    result = ValidationResult()

    if not isinstance(data, dict):
        result.errors.append(f"policy must be a YAML mapping, got {type(data).__name__}")
        return result

    unknown = set(data.keys()) - _KNOWN_TOP_LEVEL
    if unknown:
        for key in sorted(unknown):
            result.errors.append(f"unknown top-level key: {key!r}")

    domain = data.get("domain") or {}
    if not isinstance(domain, dict):
        result.errors.append(f"`domain` must be a mapping, got {type(domain).__name__}")
    else:
        slug = domain.get("slug")
        if not isinstance(slug, str) or not slug:
            result.errors.append("`domain.slug` is required and must be a non-empty string")
        elif not _SLUG_RE.match(slug):
            result.errors.append(
                f"`domain.slug` {slug!r} is not a valid slug (lowercase, hyphenated)"
            )
        for k in ("topic", "field", "description"):
            v = domain.get(k)
            if not isinstance(v, str):
                result.errors.append(f"`domain.{k}` must be a string")

    filter_cfg = data.get("filter") or {}
    if not isinstance(filter_cfg, dict):
        result.errors.append(f"`filter` must be a mapping, got {type(filter_cfg).__name__}")
    else:
        for k in ("threshold_include", "threshold_review"):
            v = filter_cfg.get(k)
            if v is None:
                continue
            try:
                f = float(v)
            except (TypeError, ValueError):
                result.errors.append(f"`filter.{k}` must be numeric, got {v!r}")
                continue
            if not 0.0 <= f <= 1.0:
                result.errors.append(f"`filter.{k}` must be in [0.0, 1.0], got {f}")

    inclusion = data.get("inclusion_criteria") or []
    exclusion = data.get("exclusion_criteria") or []
    if not isinstance(inclusion, list):
        result.errors.append("`inclusion_criteria` must be a list")
    if not isinstance(exclusion, list):
        result.errors.append("`exclusion_criteria` must be a list")

    quality_signals = data.get("quality_signals") or {}
    if not isinstance(quality_signals, dict):
        result.errors.append("`quality_signals` must be a mapping")

    if mode == "strict":
        if isinstance(inclusion, list) and len(inclusion) < _MIN_INCLUSION:
            result.errors.append(
                f"`inclusion_criteria` must have at least {_MIN_INCLUSION} items, got {len(inclusion)}"
            )
        if isinstance(exclusion, list) and len(exclusion) < _MIN_EXCLUSION:
            result.errors.append(
                f"`exclusion_criteria` must have at least {_MIN_EXCLUSION} items, got {len(exclusion)}"
            )
        if isinstance(quality_signals, dict):
            categories = [
                k for k, v in quality_signals.items() if isinstance(v, dict)
            ]
            if len(categories) < _MIN_QUALITY_CATEGORIES:
                result.errors.append(
                    f"`quality_signals` must have at least {_MIN_QUALITY_CATEGORIES} categories"
                    f", got {len(categories)}"
                )
            for cat in categories:
                cat_data = quality_signals[cat]
                signals = []
                for key in ("positive_signals", "negative_signals"):
                    sig = cat_data.get(key) or []
                    if isinstance(sig, list):
                        signals.extend(sig)
                if len(signals) < _MIN_SIGNALS_PER_CATEGORY:
                    result.errors.append(
                        f"`quality_signals.{cat}` must have at least "
                        f"{_MIN_SIGNALS_PER_CATEGORY} total signals, got {len(signals)}"
                    )
        version = data.get("policy_schema_version")
        if version != POLICY_SCHEMA_VERSION:
            result.errors.append(
                f"`policy_schema_version` must be {POLICY_SCHEMA_VERSION}, got {version!r}"
            )
    else:  # lenient
        if "policy_schema_version" not in data:
            result.warnings.append("policy missing `policy_schema_version` (legacy)")

    return result
```

- [ ] **Step 5: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_policy_validator.py -v`
Expected: All 10 tests pass.

- [ ] **Step 6: Commit**

```bash
git add src/gateway/ops/_bootstrap_reference_policy.yaml src/gateway/ops/policy_validator.py tests/gateway/test_policy_validator.py
git commit -m "feat: policy_validator with strict + lenient modes for bootstrap-domain"
```

---

### Task 2: bootstrap_domain operation

**Files:**
- Create: `src/gateway/ops/bootstrap_domain.py`
- Test: `tests/gateway/test_bootstrap_domain.py`

- [ ] **Step 1: Write failing tests**

Create `tests/gateway/test_bootstrap_domain.py`:

```python
"""Tests for `wiki bootstrap-domain`."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from gateway import frontmatter as fm
from gateway import paths
from gateway.filter.policy import policy_path
from gateway.ops.bootstrap_domain import bootstrap_domain


class StubPlanClient:
    def __init__(self, response: str | list[str]):
        self._responses = [response] if isinstance(response, str) else list(response)
        self._idx = 0
        self.last_prompt: str | None = None
        self.calls = 0

    def call(self, prompt: str) -> str:
        self.last_prompt = prompt
        self.calls += 1
        idx = min(self._idx, len(self._responses) - 1)
        self._idx += 1
        return self._responses[idx]


def _good_policy_response(slug: str = "test-domain") -> str:
    payload = {
        "version": "v1",
        "policy_schema_version": 1,
        "domain": {
            "slug": slug,
            "topic": "Testing the bootstrap pipeline",
            "field": "Software testing and validation",
            "description": "A fictional domain about validating bootstrap-domain.",
        },
        "filter": {
            "threshold_include": 0.7,
            "threshold_review": 0.5,
            "example_count_in_prompt": 12,
            "example_strategy": "balanced",
        },
        "inclusion_criteria": [
            "Discusses end-to-end gateway operations with concrete code examples",
            "Covers schema validation patterns with measurable acceptance criteria",
            "Examines test fixture design and atomic write semantics in real systems",
        ],
        "exclusion_criteria": [
            "Pure marketing material without technical substance",
        ],
        "quality_signals": {
            "publication_venue": {
                "positive_signals": ["Peer-reviewed venue", "Reputable engineering blog"],
                "negative_signals": ["Predatory journal", "Anonymous post"],
            },
            "content_depth": {
                "positive_signals": ["Reports measurements", "Includes code excerpts"],
                "negative_signals": ["Hand-wave only", "Surface skim"],
            },
        },
    }
    return json.dumps(payload)


def test_bootstrap_happy_path(kb_root):
    client = StubPlanClient(_good_policy_response("test-domain"))
    result = bootstrap_domain(
        description="A test domain for validating the bootstrap pipeline",
        slug="test-domain",
        plan_client=client,
    )
    assert result.success, result.errors

    written = policy_path("test-domain")
    assert written.exists()

    data = yaml.safe_load(written.read_text())
    assert data["domain"]["slug"] == "test-domain"
    assert len(data["inclusion_criteria"]) >= 3
    assert data["policy_schema_version"] == 1

    examples_dir = paths.policies_dir() / "test-domain" / "examples"
    assert examples_dir.is_dir()


def test_bootstrap_rejects_invalid_slug(kb_root):
    client = StubPlanClient("(unused)")
    result = bootstrap_domain(
        description="some description",
        slug="Bad_Slug",
        plan_client=client,
    )
    assert not result.success
    assert any("slug" in e.lower() for e in result.errors)
    assert client.calls == 0


def test_bootstrap_refuses_existing_policy_without_force(kb_root):
    target = policy_path("existing")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("version: v1\ndomain:\n  slug: existing\n")
    client = StubPlanClient(_good_policy_response("existing"))
    result = bootstrap_domain(
        description="x", slug="existing", plan_client=client
    )
    assert not result.success
    assert any("already exists" in e.lower() for e in result.errors)


def test_bootstrap_refuses_promoted_policy_even_with_force(kb_root):
    """Auto-generated-from-proposal policies should warn loudly."""
    target = policy_path("promoted")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        "version: v0.1.0-auto\nauto_generated_from_proposal: true\n"
        "domain:\n  slug: promoted\n"
    )
    client = StubPlanClient(_good_policy_response("promoted"))
    result = bootstrap_domain(
        description="x", slug="promoted", plan_client=client, force=False
    )
    assert not result.success
    joined = " ".join(result.errors).lower()
    assert "demote-domain" in joined


def test_bootstrap_refuses_when_proposal_exists(kb_root):
    proposal = paths.wiki_dir() / "proposals" / "open-proposal.md"
    proposal.parent.mkdir(parents=True, exist_ok=True)
    proposal.write_text(
        fm.serialize(
            {"type": "domain-proposal", "status": "draft", "proposed_domain": "open-proposal"},
            "## Rationale\n\nx\n",
        )
    )
    client = StubPlanClient(_good_policy_response("open-proposal"))
    result = bootstrap_domain(
        description="x", slug="open-proposal", plan_client=client, force=True
    )
    assert not result.success
    joined = " ".join(result.errors).lower()
    assert "promote-domain" in joined or "reject-proposal" in joined


def test_bootstrap_retries_on_underspecified_response(kb_root):
    bad = json.dumps(
        {
            "version": "v1",
            "policy_schema_version": 1,
            "domain": {
                "slug": "retry-domain",
                "topic": "x",
                "field": "x",
                "description": "x",
            },
            "filter": {"threshold_include": 0.7, "threshold_review": 0.5},
            "inclusion_criteria": ["only one"],
            "exclusion_criteria": [],
            "quality_signals": {},
        }
    )
    good = _good_policy_response("retry-domain")
    client = StubPlanClient([bad, good])

    result = bootstrap_domain(
        description="A retry test domain",
        slug="retry-domain",
        plan_client=client,
    )
    assert result.success, result.errors
    assert client.calls == 2


def test_bootstrap_saves_draft_when_retry_fails(kb_root):
    bad1 = json.dumps(
        {
            "version": "v1",
            "policy_schema_version": 1,
            "domain": {"slug": "draft-domain", "topic": "x", "field": "x", "description": "x"},
            "filter": {"threshold_include": 0.7, "threshold_review": 0.5},
            "inclusion_criteria": ["only one"],
            "exclusion_criteria": [],
            "quality_signals": {},
        }
    )
    client = StubPlanClient([bad1, bad1])

    result = bootstrap_domain(
        description="A failed retry test domain",
        slug="draft-domain",
        plan_client=client,
    )
    assert not result.success
    draft = paths.policies_dir() / "draft-domain" / "policy.draft.yaml"
    assert draft.exists()
    final = policy_path("draft-domain")
    assert not final.exists()


def test_bootstrap_rejects_unparseable_response(kb_root):
    client = StubPlanClient("not json at all")
    result = bootstrap_domain(
        description="x", slug="bad-domain", plan_client=client
    )
    assert not result.success


def test_bootstrap_warns_on_short_description(kb_root):
    client = StubPlanClient(_good_policy_response("short-desc"))
    result = bootstrap_domain(
        description="too short",
        slug="short-desc",
        plan_client=client,
    )
    assert result.success
    assert any("description" in w.lower() for w in result.warnings)


def test_bootstrap_synthetic_reference_in_prompt_not_in_output(kb_root):
    client = StubPlanClient(_good_policy_response("anti-cargo-cult"))
    result = bootstrap_domain(
        description="A fully unrelated domain about something else entirely",
        slug="anti-cargo-cult",
        plan_client=client,
    )
    assert result.success
    assert "Patagonian" in (client.last_prompt or "")
    final = policy_path("anti-cargo-cult").read_text()
    assert "Patagonian" not in final
    assert "glacier" not in final.lower()


def test_bootstrap_force_overwrites_non_promoted_policy(kb_root):
    target = policy_path("forceable")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("version: v1\ndomain:\n  slug: forceable\n")
    client = StubPlanClient(_good_policy_response("forceable"))
    result = bootstrap_domain(
        description="A forceable target description with enough length to be specific",
        slug="forceable",
        plan_client=client,
        force=True,
    )
    assert result.success, result.errors
    data = yaml.safe_load(target.read_text())
    assert len(data["inclusion_criteria"]) >= 3
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_bootstrap_domain.py -v`
Expected: FAIL — module does not exist

- [ ] **Step 3: Implement bootstrap_domain**

Create `src/gateway/ops/bootstrap_domain.py`:

```python
"""`wiki bootstrap-domain "<description>" <slug>` — author a starter policy.

Restores the predecessor's top-down green-field workflow: take a
natural-language description of a new domain, have Claude draft a
policy.yaml, validate strictly, and write to the policies directory.

Bug-prevention measures (M39 design):
- Single synthetic reference policy in the prompt (no real-domain leakage).
- Strict validator gates minimum-specificity (≥3 inclusion criteria, etc.).
- Refusal-with-hint on collisions with promoted policies or open proposals.
- Single retry on underspecified response; draft-save on second failure.
- `policy_schema_version` stamped on every output.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import TYPE_CHECKING

import yaml

from gateway import frontmatter as fm
from gateway import log, paths, wiki_pages
from gateway.core import OperationResult, write_atomic
from gateway.filter.policy import policy_path
from gateway.locking import file_lock
from gateway.ops.policy_validator import (
    POLICY_SCHEMA_VERSION,
    REFERENCE_POLICY_PATH,
    validate_policy,
)

if TYPE_CHECKING:
    from gateway.plan import PlanClient


_LOCK_NAME = "wiki-author"
_SHORT_DESCRIPTION_THRESHOLD = 20  # words
_OBJECT_RE = re.compile(r"\{[\s\S]*\}")


_PROMPT_TEMPLATE = """\
You are authoring an editorial policy for a personal knowledge base. The
policy gates which sources are accepted into a research domain via a
semantic filter. Below is the user's natural-language description of the
new domain, followed by a synthetic reference policy that demonstrates
the schema. Produce a policy YAML for the user's domain — do NOT copy
content from the reference; use it only as a structural template.

## User description

{description}

## Required slug

{slug}

## Reference policy (structural template only — do NOT copy content)

```yaml
{reference}
```

## Requirements

Your output must be a single YAML document (or a JSON object with the
same structure). It must include:

- `version: v1`
- `policy_schema_version: {schema_version}`
- `domain.slug: {slug}` (lowercase, hyphenated; must match exactly)
- `domain.topic`, `domain.field`, `domain.description` (one to three sentences each)
- `filter.threshold_include` (0.0–1.0, suggested 0.65–0.75)
- `filter.threshold_review` (0.0–1.0, lower than threshold_include)
- `inclusion_criteria`: at least 3 specific, concrete criteria. Each
  should describe a recognizable signal — what the source must discuss,
  cover, or report. Avoid vague verbs like "is interesting" or
  "is high-quality". Anchor each criterion in domain-specific terminology.
- `exclusion_criteria`: at least 1 specific exclusion (hard gate).
- `quality_signals`: at least 2 categories (e.g. publication_venue,
  content_depth), each with at least 2 total signals across
  positive_signals and negative_signals.

Return ONLY the YAML or JSON. No prose, no markdown fences.
"""


def bootstrap_domain(
    description: str,
    slug: str,
    *,
    plan_client: "PlanClient | None" = None,
    force: bool = False,
) -> OperationResult:
    """Author a starter policy from a natural-language description."""
    description = (description or "").strip()
    if not description:
        return OperationResult(success=False, errors=["description must be non-empty"])
    if not wiki_pages.is_valid_slug(slug):
        return OperationResult(
            success=False,
            errors=[f"slug {slug!r} is not a valid slug (lowercase, hyphenated)"],
        )

    proposal_path = paths.wiki_dir() / "proposals" / f"{slug}.md"
    if proposal_path.exists():
        try:
            prop_front, _ = fm.parse(proposal_path.read_text())
            if prop_front.get("status") == "draft":
                return OperationResult(
                    success=False,
                    errors=[
                        f"draft proposal exists at {proposal_path.relative_to(paths.knowledge_root())}; "
                        f"run `wiki promote-domain {slug}` to use the proposal's clustered "
                        f"sources, `wiki reject-proposal {slug}` to discard, or pick a "
                        f"different slug"
                    ],
                )
        except fm.FrontmatterError:
            pass

    target = policy_path(slug)
    if target.exists():
        existing_promoted = _is_promoted_policy(target)
        if existing_promoted:
            return OperationResult(
                success=False,
                errors=[
                    f"policy at {target.relative_to(paths.knowledge_root())} was generated "
                    f"from a proposal (auto_generated_from_proposal=true); run "
                    f"`wiki demote-domain {slug}` first to remove the back-tags before "
                    f"bootstrapping a replacement"
                ],
            )
        if not force:
            return OperationResult(
                success=False,
                errors=[
                    f"policy at {target.relative_to(paths.knowledge_root())} already exists; "
                    f"pass --force to overwrite"
                ],
            )

    if plan_client is None:
        from gateway.plan import ClaudeCLIPlanClient

        plan_client = ClaudeCLIPlanClient()

    warnings: list[str] = []
    if len(description.split()) < _SHORT_DESCRIPTION_THRESHOLD:
        warnings.append(
            f"description is short (<{_SHORT_DESCRIPTION_THRESHOLD} words); "
            f"specificity of resulting criteria may suffer"
        )
    if force and target.exists():
        warnings.append(f"--force overwrote existing policy at {target}")

    reference = REFERENCE_POLICY_PATH.read_text()
    prompt = _PROMPT_TEMPLATE.format(
        description=description,
        slug=slug,
        reference=reference,
        schema_version=POLICY_SCHEMA_VERSION,
    )

    last_errors: list[str] = []
    last_data: dict | None = None
    for attempt in range(2):
        try:
            raw = plan_client.call(prompt if attempt == 0 else _retry_prompt(prompt, last_errors))
        except Exception as e:  # noqa: BLE001
            return OperationResult(
                success=False,
                errors=[f"plan client failed: {e}"],
                warnings=warnings,
            )

        try:
            data = _parse_response(raw)
        except ValueError as e:
            last_errors = [f"parse failed: {e}"]
            last_data = None
            continue

        data.setdefault("version", "v1")
        data["policy_schema_version"] = POLICY_SCHEMA_VERSION
        if isinstance(data.get("domain"), dict):
            data["domain"]["slug"] = slug
        data["bootstrapped_from_description_hash"] = _hash_description(description)

        result = validate_policy(data, mode="strict")
        if result.ok:
            return _commit_policy(slug, data, warnings + [str(w) for w in result.warnings])

        last_errors = [str(e) for e in result.errors]
        last_data = data

    if last_data is not None:
        draft_path = paths.policies_dir() / slug / "policy.draft.yaml"
        draft_path.parent.mkdir(parents=True, exist_ok=True)
        write_atomic(draft_path, _serialize_yaml(last_data))
        return OperationResult(
            success=False,
            errors=last_errors
            + [
                f"saved best-effort draft to {draft_path.relative_to(paths.knowledge_root())}; "
                f"hand-edit and rename to policy.yaml when ready"
            ],
            warnings=warnings,
            paths_touched=[draft_path],
        )

    return OperationResult(success=False, errors=last_errors, warnings=warnings)


def _commit_policy(slug: str, data: dict, warnings: list[str]) -> OperationResult:
    target = policy_path(slug)
    examples_dir = paths.policies_dir() / slug / "examples"
    paths_touched = []
    with file_lock(_LOCK_NAME):
        target.parent.mkdir(parents=True, exist_ok=True)
        examples_dir.mkdir(parents=True, exist_ok=True)
        write_atomic(target, _serialize_yaml(data))
        paths_touched.append(target)
        log.append(
            op="bootstrap-domain",
            fields={
                "slug": slug,
                "inclusion_count": len(data.get("inclusion_criteria") or []),
                "exclusion_count": len(data.get("exclusion_criteria") or []),
            },
            summary=f"authored policy for {slug} from description",
        )
        paths_touched.append(paths.log_path())

    return OperationResult(
        success=True,
        paths_touched=paths_touched,
        summary=f"bootstrapped policy for {slug}",
        warnings=warnings,
    )


def _is_promoted_policy(path) -> bool:
    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError:
        return False
    return bool(data.get("auto_generated_from_proposal"))


def _parse_response(text: str) -> dict:
    if not text or not text.strip():
        raise ValueError("empty response from plan client")
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    try:
        obj = json.loads(cleaned)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass

    try:
        obj = yaml.safe_load(cleaned)
        if isinstance(obj, dict):
            return obj
    except yaml.YAMLError:
        pass

    match = _OBJECT_RE.search(cleaned)
    if match:
        try:
            obj = json.loads(match.group(0))
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError as e:
            raise ValueError(f"could not parse response as JSON or YAML: {e}") from e

    raise ValueError(f"could not parse response (preview: {cleaned[:200]!r})")


def _serialize_yaml(data: dict) -> str:
    header = (
        "# Authored by `wiki bootstrap-domain` from a natural-language description.\n"
        "# Edit freely; re-run `wiki refine-domain` to evolve the policy.\n\n"
    )
    return header + yaml.safe_dump(data, sort_keys=False, default_flow_style=False)


def _retry_prompt(original: str, errors: list[str]) -> str:
    err_block = "\n".join(f"- {e}" for e in errors)
    return (
        original
        + "\n\n## Previous attempt failed validation with:\n\n"
        + err_block
        + "\n\nReturn a corrected policy that addresses every error above. "
        + "Be more specific in inclusion_criteria and quality_signals."
    )


def _hash_description(description: str) -> str:
    return hashlib.sha256(description.encode("utf-8")).hexdigest()[:16]
```

- [ ] **Step 4: Run tests**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/test_bootstrap_domain.py -v`
Expected: All 11 tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/gateway/ops/bootstrap_domain.py tests/gateway/test_bootstrap_domain.py
git commit -m "feat: wiki bootstrap-domain for top-down green-field policy authorship"
```

---

### Task 3: CLI wiring

**Files:**
- Modify: `src/gateway/cli.py`

- [ ] **Step 1: Register the subcommand**

In `src/gateway/cli.py`, add to `SUBCOMMANDS` dict (around line 41):

```python
    "bootstrap-domain": "Author a starter policy.yaml from a natural-language domain description",
```

Add to `IMPLEMENTED` set (around line 65):

```python
    "bootstrap-domain",
```

- [ ] **Step 2: Add subparser**

After the `promote-domain` subparser (around line 395), add:

```python
    # bootstrap-domain (M39)
    p_bootstrap = subparsers.add_parser(
        "bootstrap-domain", help=SUBCOMMANDS["bootstrap-domain"]
    )
    p_bootstrap.add_argument(
        "description",
        help="Natural-language description of the new domain (1-3 paragraphs)",
    )
    p_bootstrap.add_argument(
        "slug",
        help="Slug for the new domain (lowercase, hyphenated)",
    )
    p_bootstrap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing non-promoted policy at this slug",
    )
```

- [ ] **Step 3: Add dispatcher**

In the dispatch section (where you see `if ns.subcommand == "promote-domain":`), add:

```python
    if ns.subcommand == "bootstrap-domain":
        return _run_bootstrap_domain(ns)
```

After `_run_promote_domain` (around line 727), add:

```python
def _run_bootstrap_domain(ns: argparse.Namespace) -> int:
    from gateway.ops.bootstrap_domain import bootstrap_domain

    return _emit_result(
        bootstrap_domain(
            description=ns.description,
            slug=ns.slug,
            force=ns.force,
        )
    )
```

- [ ] **Step 4: Smoke test**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/wiki bootstrap-domain --help`
Expected: argparse usage prints; exit 0.

- [ ] **Step 5: Run full test suite**

Run: `cd /Users/andrewgrant/code/knowledge && .venv/bin/pytest tests/gateway/ -q`
Expected: All tests pass; no regressions.

- [ ] **Step 6: Commit**

```bash
git add src/gateway/cli.py
git commit -m "feat: wire wiki bootstrap-domain into CLI"
```

---

### Task 4: Documentation update

**Files:**
- Modify: `CLAUDE.md`
- Modify: `BUILD.md`

- [ ] **Step 1: Update CLAUDE.md operation table**

In `/Users/andrewgrant/code/knowledge/CLAUDE.md`, find the Operation guide table. Add a row before the "Discover candidate domains" line:

```
| Bootstrap a new domain from a natural-language description | `wiki bootstrap-domain "<description>" <slug>` |
```

- [ ] **Step 2: Append BUILD.md M39 section**

In `/Users/andrewgrant/code/knowledge/BUILD.md`, after the M38 smart-authorship section (before "## 11. Downstream wiki-authoring work"), add:

```markdown
### M39 — Top-down domain bootstrap

Restores the predecessor's green-field research workflow. Before M39, starting research on a new domain required either accumulating sources first and running `wiki discover-domains` → `wiki promote-domain` (which produced empty-criteria auto-policies), or hand-editing `.knowledge/policies/<slug>/policy.yaml` directly. M39 adds `wiki bootstrap-domain "<description>" <slug>` which has Claude draft a starter policy from a natural-language description.

**What's new.**

- `gateway.ops.bootstrap_domain` — calls the plan client with the user's description, a single synthetic reference policy ("Patagonian glacier hydrology" — fictional, prevents cargo-culting from real domains), and a strict requirement schema. Validates the response, retries once on under-specified output, draft-saves to `policy.draft.yaml` if the retry also fails.

- `gateway.ops.policy_validator` — strict + lenient modes. Strict enforces minimum specificity (≥3 inclusion criteria, ≥1 exclusion, ≥2 quality_signals categories with ≥2 signals each), threshold ranges, slug regex, schema version. Lenient runs structural checks only — used for legacy policy load (existing `auto_generated_from_proposal` policies don't need migration).

- `_bootstrap_reference_policy.yaml` — checked-in synthetic example used as the only few-shot in the bootstrap prompt. A round-trip test (`test_reference_policy_passes_strict_validation`) ensures schema additions break the test until the reference is updated, preventing schema drift from silently accumulating.

- Collision handling: refuses if `auto_generated_from_proposal: true` exists at the target path (points at `wiki demote-domain`); refuses if a draft proposal exists at `wiki/proposals/<slug>.md` (points at `wiki promote-domain` or `wiki reject-proposal`); allows `--force` only for non-promoted, non-proposal collisions.

- `policy_schema_version: 1` stamped on every bootstrap output. `bootstrapped_from_description_hash` records a SHA-prefix of the description for re-run idempotency tracking.

**Tests.** 21 new tests across `test_policy_validator.py` (10) and `test_bootstrap_domain.py` (11). Full gateway suite remains green.

**Out of scope for M39.**

- `wiki refine-domain` (re-run bootstrap against existing policy as the reference) — natural follow-up but separate milestone.
- Auto-bootstrapping a NotebookLM persistent notebook on first `wiki research --domain <slug>` — already handled by the research orchestrator.
- Migrating legacy `auto_generated_from_proposal` policies to the new schema — lenient validator keeps them loading; explicit migration deferred.

```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md BUILD.md
git commit -m "docs: BUILD.md + CLAUDE.md for M39 bootstrap-domain"
```
