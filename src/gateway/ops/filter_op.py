"""`wiki filter <path-or-url>` — score a candidate without writing anything.

Read-only. Useful for probing how the current policy would score a source
before committing to ingest. Lands here in M3.
"""

from __future__ import annotations

from pathlib import Path

from gateway import converters, frontmatter as fm
from gateway.core import OperationResult
from gateway.filter import (
    FilterError,
    PolicyError,
    load_all,
    load_policy,
    policy_exists,
    score,
    select,
)
from gateway.filter.semantic import FilterClient


def filter_source(
    source: str | Path,
    *,
    domain: str | None = None,
    client: FilterClient | None = None,
) -> OperationResult:
    """Score `source` (URL or path) and return the result without writing."""
    text = _read_source(source)
    if isinstance(text, OperationResult):
        return text

    try:
        front, body = fm.parse(text)
    except fm.FrontmatterError as e:
        return OperationResult(success=False, errors=[f"frontmatter: {e}"])

    effective_domain = _pick_domain(domain, front)
    if not effective_domain:
        return OperationResult(
            success=False,
            errors=[
                "no domain specified and no domains in source frontmatter; "
                "pass --domain <slug> or set domains in the source"
            ],
        )

    if not policy_exists(effective_domain):
        return OperationResult(
            success=False,
            errors=[f"no policy file for domain {effective_domain!r}"],
        )

    try:
        policy = load_policy(effective_domain)
    except PolicyError as e:
        return OperationResult(success=False, errors=[f"policy: {e}"])

    examples = select(load_all(effective_domain), policy)

    try:
        result = score(front, body, policy, examples, client=client)
    except FilterError as e:
        return OperationResult(success=False, errors=[f"filter: {e}"])

    return OperationResult(
        success=True,
        summary=(
            f"score={result.score:.2f} · {effective_domain} · "
            f"{result.rationale}"
        ),
    )


def _read_source(source: str | Path) -> str | OperationResult:
    if isinstance(source, str) and source.startswith(("http://", "https://")):
        try:
            converter = converters.dispatch(source)
        except converters.NoConverterError as e:
            return OperationResult(success=False, errors=[str(e)])
        try:
            return converter.convert(source)
        except converters.ConversionError as e:
            return OperationResult(success=False, errors=[f"conversion failed: {e}"])

    path = Path(source).expanduser() if isinstance(source, str) else source
    if not path.exists():
        return OperationResult(success=False, errors=[f"input not found: {path}"])
    return path.read_text()


def _pick_domain(domain: str | None, front: dict) -> str | None:
    if domain:
        return domain
    domains = front.get("domains") or []
    if domains:
        return str(domains[0])
    return None
