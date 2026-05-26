"""QUAL-1: link-rot monitor — HEAD-check web sources, update link_status frontmatter.

Run via `wiki poll link-rot`. Updates raw/web/<id>.md and wiki/sources/<id>.md
frontmatter with `link_status: ok | redirect | dead` and `last_checked_at`.
Sources checked within RECHECK_DAYS are skipped.

Wayback archive_url written at ingest (QUAL-13) is surfaced by lint/link_rot.py
as a fallback reference for dead sources.
"""

from __future__ import annotations

import urllib.error
import urllib.request
from datetime import datetime, timezone

from gateway import frontmatter as fm, log, paths
from gateway.core import write_atomic
from gateway.pollers.base import Poller, PollerResult


_RECHECK_DAYS = 30
_REQUEST_TIMEOUT = 10
_USER_AGENT = "wiki-link-rot/1.0"


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _days_since(iso_str: str) -> float | None:
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        delta = datetime.now(timezone.utc) - dt
        return delta.total_seconds() / 86400
    except Exception:
        return None


def check_url(url: str) -> tuple[str, str | None]:
    """HEAD-check a URL. Returns (status, effective_url).

    status: 'ok' (2xx), 'redirect' (3xx with different final URL), 'dead' (error/4xx/5xx).
    """
    if not url or not url.startswith("http"):
        return "dead", None
    try:
        req = urllib.request.Request(
            url, method="HEAD", headers={"User-Agent": _USER_AGENT}
        )
        with urllib.request.urlopen(req, timeout=_REQUEST_TIMEOUT) as resp:
            effective = resp.url
            if effective and effective.rstrip("/") != url.rstrip("/"):
                return "redirect", effective
            return "ok", effective
    except urllib.error.HTTPError as e:
        if 300 <= e.code < 400:
            return "redirect", None
        return "dead", None
    except Exception:
        return "dead", None


class LinkRotPoller(Poller):
    name = "link-rot"
    source_type = "web"

    def run(self) -> PollerResult:
        raw_web = paths.raw_dir() / "web"
        if not raw_web.exists():
            return PollerResult(success=True, summary="link-rot: no raw/web/ sources")

        checked = 0
        skipped = 0
        errors: list[str] = []

        for src in sorted(raw_web.glob("*.md")):
            try:
                front, body = fm.parse(src.read_text())
            except Exception as e:
                errors.append(f"{src.stem}: parse error: {e!r}")
                continue

            url = str(front.get("url") or "")
            if not url:
                skipped += 1
                continue

            last_checked = front.get("last_checked_at")
            if last_checked:
                days = _days_since(str(last_checked))
                if days is not None and days < _RECHECK_DAYS:
                    skipped += 1
                    continue

            status, effective_url = check_url(url)
            now = _now_iso()

            new_front = dict(front)
            new_front["link_status"] = status
            new_front["last_checked_at"] = now
            if status == "redirect" and effective_url and effective_url.rstrip("/") != url.rstrip("/"):
                meta = dict(new_front.get("meta") or {})
                meta["redirect_url"] = effective_url
                new_front["meta"] = meta

            try:
                write_atomic(src, fm.serialize(new_front, body))
            except Exception as e:
                errors.append(f"{src.stem}: write error: {e!r}")
                continue

            checked += 1

            # Mirror status to wiki/sources page
            wiki_path = paths.wiki_source_path(src.stem)
            if wiki_path.exists():
                try:
                    wfront, wbody = fm.parse(wiki_path.read_text())
                    new_wfront = dict(wfront)
                    new_wfront["link_status"] = status
                    new_wfront["last_checked_at"] = now
                    write_atomic(wiki_path, fm.serialize(new_wfront, wbody))
                except Exception as e:
                    errors.append(f"{src.stem} wiki page: {e!r}")

        log.append(
            op="link-rot",
            fields={"checked": checked, "skipped": skipped, "errors": len(errors)},
            summary=f"checked={checked} skipped={skipped}",
        )

        return PollerResult(
            success=len(errors) == 0,
            fetched=checked,
            skipped=skipped,
            errors=errors,
            summary=f"link-rot: {checked} checked, {skipped} skipped, {len(errors)} errors",
        )
