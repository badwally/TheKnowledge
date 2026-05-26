"""QUAL-7: PubMed retraction monitor.

Checks each ingested PubMed source against the NCBI eFetch API. Sources
confirmed retracted get `retracted: true` + `retracted_at` stamped into
their `raw/pubmed/<id>.md` frontmatter.

Hard rule §6 allows frontmatter mutation by pipeline stages; body content
is never modified.

Cursor: .knowledge/pollers/pubmed-retractions/cursor.yaml
  checked:
    pubmed-22128031: "2026-05-26T00:00:00Z"
    ...

Re-checks run after RECHECK_DAYS to pick up newly-issued retraction notices.
"""

from __future__ import annotations

import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Callable

import yaml

from gateway import frontmatter as fm, paths
from gateway.core import write_atomic
from gateway.pollers.base import Poller, PollerResult


_EFETCH_URL = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    "?db=pubmed&id={pmid}&rettype=xml&retmode=xml"
)
_REQUEST_TIMEOUT = 15
RECHECK_DAYS = 30


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _days_since(iso_str: str) -> float | None:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - dt).total_seconds() / 86400
    except Exception:
        return None


def _pmid_from_id(source_id: str) -> str | None:
    if source_id.startswith("pubmed-"):
        return source_id[len("pubmed-"):]
    return None


def fetch_pubmed_xml(pmid: str) -> str:
    """Fetch PubMed XML for a PMID. Raises urllib.error.URLError on failure."""
    url = _EFETCH_URL.format(pmid=pmid)
    req = urllib.request.Request(url, headers={"Accept": "application/xml"})
    with urllib.request.urlopen(req, timeout=_REQUEST_TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def is_retracted(xml_text: str) -> tuple[bool, str | None]:
    """Parse PubMed XML. Returns (retracted, retraction_pmid_or_None).

    Checks PublicationTypeList for 'Retraction of Publication' and
    CommentsCorrectionsList for RefType 'RetractionIn'.
    """
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return False, None

    # Check PublicationType entries
    for pt in root.iter("PublicationType"):
        if pt.text and "retraction" in pt.text.lower():
            return True, None

    # Check CommentsCorrections for RetractionIn (notice was issued)
    for cc in root.iter("CommentsCorrections"):
        ref_type = cc.get("RefType", "")
        if "retraction" in ref_type.lower():
            pmid_el = cc.find("PMID")
            ref_pmid = pmid_el.text if pmid_el is not None else None
            return True, ref_pmid

    return False, None


class PubmedRetractionPoller(Poller):
    name = "pubmed-retractions"
    source_type = "pubmed"

    def __init__(
        self,
        *,
        fetch_fn: Callable[[str], str] = fetch_pubmed_xml,
    ) -> None:
        self._fetch = fetch_fn

    def run(self) -> PollerResult:
        raw_pubmed = paths.raw_dir() / "pubmed"
        if not raw_pubmed.exists():
            return PollerResult(success=True, summary="pubmed-retractions: no raw/pubmed/ sources")

        cursor = self._load_cursor()
        checked = 0
        skipped = 0
        retracted_count = 0
        errors: list[str] = []

        for src in sorted(raw_pubmed.glob("*.md")):
            try:
                front, body = fm.parse(src.read_text())
            except Exception as e:
                errors.append(f"{src.name}: parse error: {e}")
                continue

            source_id = front.get("id", src.stem)
            pmid = _pmid_from_id(source_id)
            if not pmid:
                skipped += 1
                continue

            # Skip recently checked (unless already known retracted)
            if not front.get("retracted"):
                last_checked = cursor.get(source_id)
                if last_checked:
                    age = _days_since(last_checked)
                    if age is not None and age < RECHECK_DAYS:
                        skipped += 1
                        continue

            try:
                xml_text = self._fetch(pmid)
            except Exception as e:
                errors.append(f"{source_id}: fetch error: {e}")
                continue

            retracted, _ = is_retracted(xml_text)
            cursor[source_id] = _now_iso()
            checked += 1

            if retracted and not front.get("retracted"):
                front["retracted"] = True
                front["retracted_at"] = _now_iso()
                new_text = fm.serialize(front, body)
                write_atomic(src, new_text)
                retracted_count += 1

        self._save_cursor(cursor)

        return PollerResult(
            success=True,
            fetched=checked,
            skipped=skipped,
            errors=errors,
            summary=(
                f"pubmed-retractions: {checked} checked, {skipped} skipped, "
                f"{retracted_count} newly retracted, {len(errors)} errors"
            ),
        )

    def _load_cursor(self) -> dict:
        p = self.cursor_path()
        if not p.is_file():
            return {}
        try:
            raw = yaml.safe_load(p.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                return raw.get("checked", {}) or {}
        except Exception:
            pass
        return {}

    def _save_cursor(self, checked: dict) -> None:
        p = self.cursor_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            yaml.safe_dump({"checked": checked}, sort_keys=True, allow_unicode=True),
            encoding="utf-8",
        )
