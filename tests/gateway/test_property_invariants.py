"""Real Hypothesis property tests for gateway production invariants (T6).

Each test drives a REAL production function — no reimplementations, no answer-key
derivation from the unit under test.

Properties:
  1. _union_same_slug idempotence — unioning an existing page with a body whose
     bullets are already present returns the page unchanged.
  2. _title_to_slug canonicalization — same title → same slug; the canonical form
     is a fixed point (applying the fn twice gives the same result).
  3. IntentQueue fencing-token monotonicity — for a single intent claimed multiple
     times (reclaim path), claim() always issues a strictly higher token than before.
"""

from __future__ import annotations

import tempfile
import time
from pathlib import Path

import pytest
from hypothesis import given, settings, strategies as st

from gateway import frontmatter as fm
from gateway.intent_queue import Intent, IntentQueue, compute_intent_id
from gateway.ops.committer import _title_to_slug, _union_same_slug

pytestmark = pytest.mark.unit

# ---------------------------------------------------------------------------
# Helper generators and builders
# ---------------------------------------------------------------------------

# A bullet text: no newlines, no leading/trailing whitespace, doesn't start with
# '#' or '-' (those are structural lines in _union_same_slug's parser).
_bullet_text = st.text(
    alphabet=st.characters(
        blacklist_categories=("Cc",),   # exclude control chars (incl. \n)
        blacklist_characters="#-",
    ),
    min_size=2,
    max_size=40,
).map(str.strip).filter(lambda s: bool(s) and "\n" not in s)

# A title: printable, non-empty, not all punctuation/whitespace (so slug is non-empty)
_title = st.text(
    alphabet=st.characters(
        blacklist_categories=("Cc",),
        blacklist_characters="\n\r",
    ),
    min_size=1,
    max_size=60,
).filter(lambda t: bool(_title_to_slug(t.strip())))  # must produce a non-empty slug


def _render_claims_page(bullets: list[str]) -> str:
    """Render a full page with frontmatter + ## Claims + bullets.

    Mirrors the shape real committer tests use (test_committer.py:406-415):
    a minimal YAML frontmatter block followed by a ## Claims body.
    """
    front = {
        "type": "entity",
        "title": "Test Entity",
        "slug": "test-entity",
    }
    body_lines = ["## Claims"]
    body_lines.extend(f"- {b}" for b in bullets)
    body = "\n".join(body_lines) + "\n"
    return fm.serialize(front, body)


def _claims(page: str) -> set[str]:
    """Extract the set of bullet texts from a page rendered by _render_claims_page.

    Extracts raw bullet payloads (the text after '- ') without stripping, so the
    result is comparable to the input bullets list passed to _render_claims_page.
    """
    try:
        _, body = fm.parse(page)
    except fm.FrontmatterError:
        return set()
    return {
        line[2:]           # raw text after leading "- " (no strip — preserves exact value)
        for line in body.splitlines()
        if line.startswith("- ")
    }


# ---------------------------------------------------------------------------
# Property 1: _union_same_slug idempotence
# ---------------------------------------------------------------------------


@given(bullets=st.lists(_bullet_text, min_size=1, max_size=8, unique=True))
@settings(max_examples=200)
def test_union_same_slug_idempotent_when_bullets_already_present(
    bullets: list[str],
) -> None:
    """Unioning an existing page with a body whose bullets are already present is a
    no-op: _union_same_slug returns the page with the same bullet set.

    Drives the REAL _union_same_slug (ops/committer.py:86).  The idempotence
    guarantee is at :130-132: when net_new_bullets is empty, the function returns
    the existing page (via fm.serialize) without modification.
    """
    existing = _render_claims_page(bullets)
    # arg2 is a bullet-only ## Claims body — NOT a full page (brief: CRITICAL arg shape)
    new_body = "## Claims\n" + "\n".join(f"- {b}" for b in bullets)

    result = _union_same_slug(existing, new_body)

    # Must not reject (return None) — existing + same bullets is always unionable
    assert result is not None, (
        f"_union_same_slug returned None (rejected) for bullets already present; "
        f"bullets={bullets!r}"
    )
    # The bullet set must be identical — no duplication, no loss
    assert _claims(result) == set(bullets), (
        f"bullet set changed after idempotent union; "
        f"expected={set(bullets)!r}, got={_claims(result)!r}"
    )


# ---------------------------------------------------------------------------
# Property 2: _title_to_slug canonicalization is a fixed point
# ---------------------------------------------------------------------------


@given(title=_title)
@settings(max_examples=200)
def test_title_to_slug_is_a_fixed_point(title: str) -> None:
    """Applying _title_to_slug twice yields the same result as applying it once
    (the canonical slug form is idempotent under re-application).

    Also asserts: same title always produces the same slug (determinism).

    Drives the REAL _title_to_slug (ops/committer.py:71):
      re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    A slug contains only [a-z0-9-], so re.sub collapses nothing further on second
    application — the fn is therefore a fixed point on its own output.
    """
    slug = _title_to_slug(title)
    # Non-empty slug is guaranteed by the filter on _title; just assert for clarity
    assert isinstance(slug, str)

    # Fixed-point invariant: slug of slug == slug
    slug_of_slug = _title_to_slug(slug)
    assert slug_of_slug == slug, (
        f"_title_to_slug is not a fixed point: "
        f"title={title!r} → slug={slug!r} → slug_of_slug={slug_of_slug!r}"
    )

    # Determinism: same title → same slug on a second call
    assert _title_to_slug(title) == slug, (
        f"_title_to_slug is non-deterministic for title={title!r}"
    )


# ---------------------------------------------------------------------------
# Property 3: IntentQueue fencing-token monotonicity (per-intent-id)
# ---------------------------------------------------------------------------


@given(
    n_claims=st.integers(min_value=2, max_value=6),
)
@settings(max_examples=100)
def test_intent_queue_fencing_tokens_strictly_increase_on_reclaim(
    n_claims: int,
) -> None:
    """For a single intent claimed multiple times via the reclaim path, each successive
    fencing token is strictly greater than the previous one.

    The fencing counter is per-intent-id (intent_queue.py:141: counter file is named
    per intent_id).  The monotonicity guarantee is at :266 (_next_fencing_token).

    Drives the REAL IntentQueue with a real filesystem queue root:
    - submit() → claim() → lease expires → reclaim_expired() → claim() → ... (n_claims)
    Uses a fresh tmp dir per example via tempfile.TemporaryDirectory.
    """
    identity = {"agent": "property-test"}
    payload = {"page_type": "entity", "title": "MonotonicTest"}
    intent_id = compute_intent_id(payload, identity)
    intent = Intent(intent_id=intent_id, payload=payload, identity=identity)

    with tempfile.TemporaryDirectory() as tmp_dir:
        queue = IntentQueue(root=Path(tmp_dir) / "intents")

        tokens: list[int] = []
        for i in range(n_claims):
            # (Re-)submit: first iteration is a fresh submit; subsequent ones rely on
            # reclaim_expired() moving the claimed intent back to submitted/.
            if i == 0:
                queue.submit(intent)
            else:
                # Expire the lease on the currently-claimed intent and reclaim it.
                # Pass a far-future `now` so the lease appears expired immediately.
                reclaimed = queue.reclaim_expired(now=time.time() + 10_000)
                assert intent_id in reclaimed, (
                    f"reclaim_expired did not return intent {intent_id!r} at step {i}"
                )

            claim = queue.claim()
            assert claim is not None, f"claim() returned None at step {i}"
            assert claim.intent.intent_id == intent_id
            tokens.append(claim.fencing_token)

        # Monotonicity: each successive token is strictly greater than the previous
        for i in range(1, len(tokens)):
            assert tokens[i] > tokens[i - 1], (
                f"Fencing token monotonicity violated at claim #{i}: "
                f"token={tokens[i]} ≤ previous={tokens[i - 1]} "
                f"(full sequence: {tokens})"
            )
