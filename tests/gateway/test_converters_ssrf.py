"""SSRF guard on the web converter's URL fetch (260530 review follow-up to #3).

The API now accepts only http(s) URLs for ingest, but any http(s) URL was
still fetched — including internal/loopback/link-local targets such as the
cloud metadata endpoint http://169.254.169.254/ or http://localhost:7474/.
`_assert_public_url` resolves the host and refuses to fetch when it maps to a
non-public address; `WIKI_ALLOW_PRIVATE_FETCH=1` overrides for trusted
operator use of internal URLs.
"""

from __future__ import annotations

import pytest

from gateway.converters import web as web_mod
from gateway.converters.base import ConversionError


@pytest.mark.parametrize(
    "url",
    [
        "http://127.0.0.1/x",
        "http://localhost/x",  # resolves to loopback
        "http://169.254.169.254/latest/meta-data/",  # cloud metadata
        "http://10.0.0.1/x",
        "http://192.168.1.1/x",
        "http://172.16.5.5/x",
        "http://0.0.0.0/x",
        "http://[::1]/x",
    ],
)
def test_assert_public_url_blocks_internal_targets(url):
    with pytest.raises(ConversionError):
        web_mod._assert_public_url(url)


def test_assert_public_url_blocks_hostname_resolving_to_private(monkeypatch):
    monkeypatch.setattr(web_mod, "_resolve_ips", lambda host: ["10.0.0.5"])
    with pytest.raises(ConversionError):
        web_mod._assert_public_url("https://evil.example/x")


def test_assert_public_url_allows_public_host(monkeypatch):
    monkeypatch.setattr(web_mod, "_resolve_ips", lambda host: ["93.184.216.34"])
    # Should not raise.
    web_mod._assert_public_url("https://example.com/x")


def test_env_override_allows_private(monkeypatch):
    monkeypatch.setenv("WIKI_ALLOW_PRIVATE_FETCH", "1")
    # No raise even for loopback when the operator opts in.
    web_mod._assert_public_url("http://127.0.0.1/x")


class _FakeResp:
    """Minimal stand-in for a requests.Response."""

    def __init__(self, status_code, *, location=None, text=""):
        self.status_code = status_code
        self.headers = {"Location": location} if location else {}
        self.text = text

    @property
    def is_redirect(self):
        return self.status_code in (301, 302, 303, 307, 308) and "Location" in self.headers


def test_fetch_blocks_private_url_before_request(monkeypatch):
    called = {"hit": False}

    def _boom(*a, **k):  # requests.get must not be reached for a blocked host
        called["hit"] = True
        return _FakeResp(200, text="should not happen")

    monkeypatch.setattr(web_mod.requests, "get", _boom)
    with pytest.raises(ConversionError):
        web_mod._fetch("http://169.254.169.254/latest/meta-data/")
    assert called["hit"] is False


def test_fetch_blocks_redirect_to_private(monkeypatch):
    """A public host that 302-redirects to an internal address is blocked at
    the redirect hop (the redirect-bypass SSRF class). Literal IPs are used so
    no DNS resolution (or mock) is involved."""
    requested = []

    def _get(url, **k):
        requested.append(url)
        return _FakeResp(302, location="http://169.254.169.254/latest/meta-data/")

    monkeypatch.setattr(web_mod.requests, "get", _get)
    with pytest.raises(ConversionError):
        web_mod._fetch("https://93.184.216.34/start")  # public literal IP
    # We connected to the public host once, but never to the internal target.
    assert requested == ["https://93.184.216.34/start"]


def test_fetch_follows_public_redirect(monkeypatch):
    monkeypatch.setattr(web_mod, "_resolve_ips", lambda host: ["93.184.216.34"])
    seq = [
        _FakeResp(302, location="https://final.example/page"),
        _FakeResp(200, text="<html>ok</html>"),
    ]

    def _get(url, **k):
        return seq.pop(0)

    monkeypatch.setattr(web_mod.requests, "get", _get)
    assert web_mod._fetch("https://start.example/a") == "<html>ok</html>"


def test_convert_blocks_private_url(monkeypatch):
    # The full convert() path refuses an internal URL (guard runs in _fetch).
    monkeypatch.setattr(web_mod.requests, "get", lambda *a, **k: _FakeResp(200, text="<html/>"))
    with pytest.raises(ConversionError):
        web_mod.WebConverter().convert("http://127.0.0.1:7474/api/status")
