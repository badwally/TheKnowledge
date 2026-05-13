"""Tests for the M3 semantic filter integration."""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

from gateway import frontmatter as fm
from gateway import paths
from gateway.filter import (
    ClaudeCLIFilterClient,
    Example,
    FilterClient,
    FilterError,
    Policy,
    PolicyError,
    build_prompt,
    examples_dir,
    load_all,
    load_policy,
    parse_response,
    pin,
    policy_exists,
    score,
    select,
)
from gateway.ops.filter_correct import filter_correct
from gateway.ops.filter_op import filter_source
from gateway.ops.ingest import ingest, ingest_canonical


# --- helpers ----------------------------------------------------------------


class StubClient(FilterClient):
    """Returns a fixed canned response, recording the prompts it received."""

    def __init__(self, response: str):
        self.response = response
        self.prompts: list[str] = []

    def call(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return self.response


def write_policy(domain_slug: str, *, threshold_include: float = 0.7, threshold_review: float = 0.5) -> Path:
    target_dir = paths.policies_dir() / domain_slug
    target_dir.mkdir(parents=True, exist_ok=True)
    path = target_dir / "policy.yaml"
    path.write_text(yaml.safe_dump({
        "domain": {
            "slug": domain_slug,
            "topic": "Test domain for filter integration",
            "field": "test",
        },
        "version": "v1",
        "filter": {
            "threshold_include": threshold_include,
            "threshold_review": threshold_review,
            "example_count_in_prompt": 6,
            "example_strategy": "balanced",
        },
        "inclusion_criteria": ["mentions the test topic"],
        "exclusion_criteria": ["off-topic chatter"],
        "quality_signals": {"speaker_expertise": {"positive_signals": ["cites studies"]}},
    }, sort_keys=False))
    return path


# --- policy.py --------------------------------------------------------------


def test_policy_exists_false_then_true(kb_root):
    assert not policy_exists("test-domain")
    write_policy("test-domain")
    assert policy_exists("test-domain")


def test_load_policy_returns_defaults_when_filter_unset(kb_root):
    target_dir = paths.policies_dir() / "minimal"
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "policy.yaml").write_text(yaml.safe_dump({
        "domain": {"slug": "minimal"},
    }))
    policy = load_policy("minimal")
    assert policy.domain_slug == "minimal"
    assert policy.threshold_include == 0.70
    assert policy.threshold_review == 0.50


def test_load_policy_validates_slug_match(kb_root):
    target_dir = paths.policies_dir() / "alpha"
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "policy.yaml").write_text(yaml.safe_dump({
        "domain": {"slug": "beta"},
    }))
    with pytest.raises(PolicyError):
        load_policy("alpha")


def test_load_policy_missing_raises(kb_root):
    with pytest.raises(PolicyError):
        load_policy("nonexistent")


# --- examples.py ------------------------------------------------------------


def test_pin_and_load_example(kb_root):
    pin(
        source_id="yt-abc",
        domain="test",
        decision="include",
        score=0.92,
        policy_version="test-v1",
        rationale="Cites relevant primary literature",
        pinned_by="user-correction",
        frontmatter_snapshot={"title": "Sample"},
        content_excerpt="lorem ipsum" * 80,
    )
    examples = load_all("test")
    assert len(examples) == 1
    e = examples[0]
    assert e.source_id == "yt-abc"
    assert e.decision == "include"
    assert e.score == 0.92
    assert len(e.content_excerpt) == 500  # truncated


def test_select_balanced_returns_mix(kb_root):
    for i in range(3):
        pin(source_id=f"correct-{i}", domain="d", decision="include", score=1.0,
            policy_version="d-v1", rationale="user fix", pinned_by="user-correction")
        pin(source_id=f"include-{i}", domain="d", decision="include", score=0.95,
            policy_version="d-v1", rationale="solid", pinned_by="high-confidence")
        pin(source_id=f"exclude-{i}", domain="d", decision="exclude", score=0.05,
            policy_version="d-v1", rationale="off-topic", pinned_by="high-confidence")

    policy = Policy(domain_slug="d", example_count_in_prompt=6, example_strategy="balanced")
    chosen = select(load_all("d"), policy)
    decisions = [e.decision for e in chosen]
    pinned_bys = [e.pinned_by for e in chosen]
    assert "include" in decisions and "exclude" in decisions
    assert "user-correction" in pinned_bys


# --- semantic.py ------------------------------------------------------------


def test_parse_response_plain_json():
    s, r = parse_response('{"score": 0.85, "rationale": "Solid match"}')
    assert s == 0.85
    assert r == "Solid match"


def test_parse_response_strips_code_fences():
    text = '```json\n{"score": 0.42, "rationale": "Marginal"}\n```'
    s, r = parse_response(text)
    assert s == 0.42


def test_parse_response_missing_keys():
    with pytest.raises(Exception):
        parse_response('{"foo": "bar"}')


def test_parse_response_score_out_of_range():
    with pytest.raises(Exception):
        parse_response('{"score": 1.5, "rationale": "x"}')


def test_build_prompt_includes_policy_examples_and_source():
    policy = Policy(domain_slug="t", raw={"domain": {"slug": "t"}, "filter": {"threshold_include": 0.7}})
    examples = [Example(
        source_id="yt-x", domain="t", decision="include", score=0.9,
        policy_version="t-v1", rationale="good", pinned_at="2026-04-01T00:00:00Z",
        pinned_by="high-confidence",
    )]
    prompt = build_prompt(policy, examples, {"type": "youtube", "title": "T"}, "body content")
    assert "domain:" in prompt and "slug: t" in prompt
    assert "good" in prompt
    assert "body content" in prompt


def test_score_uses_injected_client(kb_root):
    write_policy("test-domain")
    policy = load_policy("test-domain")
    client = StubClient('{"score": 0.81, "rationale": "Looks great"}')
    result = score({"type": "youtube", "title": "T"}, "body", policy, client=client)
    assert result.score == 0.81
    assert result.rationale == "Looks great"
    assert result.policy_version == "test-domain-v1"
    assert len(client.prompts) == 1


# --- ingest with filter -----------------------------------------------------


def _build_high_score_text(make_source, *, domain="test-domain"):
    return make_source(
        id_="yt-high1ABC_xx",
        body="Detailed receptor pharmacology content.\n",
        domains=[domain],
    )


def _build_low_score_text(make_source, *, domain="test-domain"):
    return make_source(
        id_="yt-low2XYZ_yy",
        body="Off-topic celebrity gossip content.\n",
        domains=[domain],
    )


def test_ingest_filter_above_threshold_writes_wiki(kb_root, make_source, tmp_path):
    write_policy("test-domain")
    text = _build_high_score_text(make_source)
    src = tmp_path / "high.md"
    src.write_text(text)

    client = StubClient('{"score": 0.92, "rationale": "Strong relevance"}')
    result = ingest(src, filter_client=client)

    assert result.success, result.errors
    assert paths.raw_source_path("youtube", "yt-high1ABC_xx").exists()
    assert paths.wiki_source_path("yt-high1ABC_xx").exists()

    # Filter block written into raw frontmatter
    raw_text = paths.raw_source_path("youtube", "yt-high1ABC_xx").read_text()
    front, _ = fm.parse(raw_text)
    assert front["filter"]["score"] == 0.92
    assert front["filter"]["policy_version"] == "test-domain-v1"


def test_ingest_filter_below_review_skips_wiki(kb_root, make_source, tmp_path):
    write_policy("test-domain", threshold_include=0.7, threshold_review=0.5)
    text = _build_low_score_text(make_source)
    src = tmp_path / "low.md"
    src.write_text(text)

    client = StubClient('{"score": 0.15, "rationale": "Off-topic"}')
    result = ingest(src, filter_client=client)

    assert result.success
    assert paths.raw_source_path("youtube", "yt-low2XYZ_yy").exists()
    assert not paths.wiki_source_path("yt-low2XYZ_yy").exists()


def test_ingest_filter_review_band_skips_wiki(kb_root, make_source, tmp_path):
    write_policy("test-domain", threshold_include=0.7, threshold_review=0.5)
    text = _build_low_score_text(make_source)
    src = tmp_path / "review.md"
    src.write_text(text)

    client = StubClient('{"score": 0.6, "rationale": "Maybe"}')
    result = ingest(src, filter_client=client)

    assert result.success
    assert "review" in result.summary
    assert not paths.wiki_source_path("yt-low2XYZ_yy").exists()


def test_ingest_no_domain_skips_filter(kb_root, make_source, tmp_path):
    text = make_source(domains=[])
    src = tmp_path / "no-domain.md"
    src.write_text(text)

    result = ingest(src)  # no client; should not call filter

    assert result.success
    assert paths.wiki_source_path("yt-testABC_123").exists()
    assert any("no domain" in w for w in result.warnings)


def test_ingest_explicit_domain_overrides_frontmatter(kb_root, make_source, tmp_path):
    write_policy("override-domain")
    text = make_source(id_="yt-override42_AB", domains=["other-domain"])
    src = tmp_path / "override.md"
    src.write_text(text)

    client = StubClient('{"score": 0.9, "rationale": "ok"}')
    result = ingest(src, domain="override-domain", filter_client=client)

    assert result.success
    raw = paths.raw_source_path("youtube", "yt-override42_AB").read_text()
    front, _ = fm.parse(raw)
    assert front["filter"]["policy_version"] == "override-domain-v1"


def test_ingest_no_policy_warns_skips_wiki(kb_root, make_source, tmp_path):
    # Source has a domain but no policy file exists
    text = make_source(id_="yt-noPolicyABCD", domains=["unconfigured"])
    src = tmp_path / "no-policy.md"
    src.write_text(text)

    result = ingest(src)
    assert result.success
    assert any("no policy file" in w for w in result.warnings)
    assert not paths.wiki_source_path("yt-noPolicyABCD").exists()


# --- wiki filter (standalone) -----------------------------------------------


def test_filter_op_returns_score_without_writing(kb_root, make_source, tmp_path):
    write_policy("test-domain")
    text = make_source(domains=["test-domain"])
    src = tmp_path / "scored.md"
    src.write_text(text)

    client = StubClient('{"score": 0.77, "rationale": "Solid"}')
    result = filter_source(src, client=client)

    assert result.success
    assert "0.77" in result.summary
    # No raw file or wiki page written
    assert not paths.raw_source_path("youtube", "yt-testABC_123").exists()
    assert not paths.wiki_source_path("yt-testABC_123").exists()


def test_filter_op_no_domain_errors(kb_root, make_source, tmp_path):
    text = make_source(domains=[])
    src = tmp_path / "x.md"
    src.write_text(text)
    result = filter_source(src)
    assert not result.success
    assert any("no domain" in e for e in result.errors)


# --- wiki filter-correct ----------------------------------------------------


def test_filter_correct_pins_example_and_updates_frontmatter(kb_root, make_source, tmp_path):
    write_policy("test-domain", threshold_include=0.7, threshold_review=0.5)

    # First, ingest with a low score so the source lands in raw/ but not wiki/
    text = make_source(id_="yt-correctMeAB", body="body\n", domains=["test-domain"])
    src = tmp_path / "src.md"
    src.write_text(text)
    client = StubClient('{"score": 0.2, "rationale": "Looks marginal"}')
    first = ingest(src, filter_client=client)
    assert first.success

    # Override to include
    correction = filter_correct(
        "yt-correctMeAB",
        decision="include",
        rationale="The original review missed the methodology section",
        domain="test-domain",
    )
    assert correction.success, correction.errors

    raw = paths.raw_source_path("youtube", "yt-correctMeAB").read_text()
    front, _ = fm.parse(raw)
    assert front["filter"]["user_correction"]["score"] == 1.0

    examples = load_all("test-domain")
    assert any(e.source_id == "yt-correctMeAB" and e.pinned_by == "user-correction" for e in examples)


def test_filter_correct_unknown_source_errors(kb_root):
    result = filter_correct(
        "yt-doesNotExist",
        decision="include",
        rationale="x",
        domain="test-domain",
    )
    assert not result.success
    assert any("no raw source" in e for e in result.errors)


# --- ClaudeCLIFilterClient retry behavior -----------------------------------


def _fake_completed(returncode: int, stdout: str = "", stderr: str = ""):
    return subprocess.CompletedProcess(
        args=["claude", "-p", "<prompt>"],
        returncode=returncode,
        stdout=stdout,
        stderr=stderr,
    )


def test_claude_cli_retries_then_succeeds(monkeypatch):
    sleeps: list[float] = []
    calls = {"n": 0}

    def fake_run(*_args, **_kwargs):
        calls["n"] += 1
        if calls["n"] < 3:
            return _fake_completed(1, stderr="rate_limit_error: 429")
        return _fake_completed(0, stdout='{"score": 0.9, "rationale": "ok"}')

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIFilterClient(retry_base_s=0.01, sleep=sleeps.append)
    out = client.call("prompt")
    assert '"score": 0.9' in out
    assert calls["n"] == 3
    assert len(sleeps) == 2
    assert sleeps[0] == pytest.approx(0.01)
    assert sleeps[1] == pytest.approx(0.02)


def test_claude_cli_raises_after_max_retries(monkeypatch):
    sleeps: list[float] = []

    def fake_run(*_args, **_kwargs):
        return _fake_completed(1, stderr="overloaded_error: 529")

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIFilterClient(max_retries=2, retry_base_s=0.01, sleep=sleeps.append)
    with pytest.raises(FilterError, match="3 attempts"):
        client.call("prompt")
    assert len(sleeps) == 2  # 2 retries between 3 total attempts


# --- M44: split-prompt path + Haiku routing --------------------------------


class SplitStubClient(FilterClient):
    """Stub that implements both `call` and `call_split` for M44 assertions."""

    def __init__(self, response: str):
        self.response = response
        self.split_calls: list[tuple[str, str]] = []
        self.plain_calls: list[str] = []

    def call(self, prompt: str) -> str:
        self.plain_calls.append(prompt)
        return self.response

    def call_split(self, *, system: str, user: str) -> str:
        self.split_calls.append((system, user))
        return self.response


def test_score_prefers_call_split_when_available(kb_root):
    write_policy("test-domain")
    policy = load_policy("test-domain")
    client = SplitStubClient('{"score": 0.81, "rationale": "ok"}')
    score({"type": "youtube", "title": "T"}, "body", policy, client=client)
    assert len(client.split_calls) == 1
    assert client.plain_calls == []
    system, user = client.split_calls[0]
    assert "Editorial policy" in system
    assert "slug: test-domain" in system
    assert "Source under evaluation" in user
    assert "body" in user
    # Policy should NOT appear in user payload — wasted tokens
    assert "Editorial policy" not in user


def test_score_falls_back_to_call_for_legacy_stubs(kb_root):
    write_policy("test-domain")
    policy = load_policy("test-domain")
    client = StubClient('{"score": 0.81, "rationale": "ok"}')
    score({"type": "youtube", "title": "T"}, "body", policy, client=client)
    assert len(client.prompts) == 1
    # Backwards-compat path: system + user concatenated into one string
    assert "Editorial policy" in client.prompts[0]
    assert "Source under evaluation" in client.prompts[0]


def test_claude_cli_filter_client_argv_has_bare_tools_empty_haiku(monkeypatch):
    captured: list[list[str]] = []

    def fake_run(argv, *_a, **_kwargs):
        captured.append(list(argv))
        return _fake_completed(0, stdout='{"score": 0.9, "rationale": "ok"}')

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIFilterClient(retry_base_s=0.01, sleep=lambda _s: None)
    client.call_split(system="SYS", user="USR")

    argv = captured[0]
    assert "--bare" not in argv  # --bare bypasses Max OAuth
    assert "--no-session-persistence" in argv
    assert "--tools" in argv
    assert argv[argv.index("--tools") + 1] == ""
    assert "--model" in argv
    assert argv[argv.index("--model") + 1] == "claude-haiku-4-5-20251001"
    assert argv[argv.index("--system-prompt") + 1] == "SYS"
    assert argv[-1] == "USR"


def test_claude_cli_filter_client_call_prompt_omits_system_prompt_flag(monkeypatch):
    """Legacy `call(prompt)` entry point: no --system-prompt, single positional."""
    captured: list[list[str]] = []
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda argv, *_a, **_k: (captured.append(list(argv)) or _fake_completed(0, stdout='{"score":0.5,"rationale":"x"}')),
    )
    ClaudeCLIFilterClient(retry_base_s=0.01, sleep=lambda _s: None).call("monolithic")
    argv = captured[0]
    assert "--system-prompt" not in argv
    assert argv[-1] == "monolithic"


def test_claude_cli_strips_anthropic_api_key_from_subprocess_env(monkeypatch):
    """Regression: the gateway's `claude -p` subprocess invocations must drop
    `ANTHROPIC_API_KEY` so the Claude CLI uses the user's Max-plan OAuth login
    instead of billing against API credits. Filter, plan, and VLM all funnel
    through the same `claude_cli_env()` helper."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-fake-should-not-leak")
    captured_envs: list[dict] = []

    def fake_run(*_args, env=None, **_kwargs):
        captured_envs.append(env or {})
        return _fake_completed(0, stdout='{"score": 0.9, "rationale": "ok"}')

    monkeypatch.setattr(subprocess, "run", fake_run)
    client = ClaudeCLIFilterClient(retry_base_s=0.01, sleep=lambda _s: None)
    client.call("prompt")

    assert len(captured_envs) == 1
    assert "ANTHROPIC_API_KEY" not in captured_envs[0], (
        "ANTHROPIC_API_KEY leaked into claude -p subprocess env — "
        "Max plan would be bypassed in favor of API billing"
    )
    # Other env vars should still be present
    assert captured_envs[0].get("PATH") is not None
