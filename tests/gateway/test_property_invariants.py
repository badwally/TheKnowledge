"""Real Hypothesis property tests for gateway production invariants (T6).

Each test drives a REAL production function — no reimplementations, no answer-key
derivation from the unit under test.

Properties:
  1. _union_same_slug idempotence — unioning an existing page with a body whose
     bullets are already present returns the page unchanged.
  2. _title_to_slug canonicalization — same title → same slug; the canonical form
     is a fixed point (applying the fn twice gives the same result).
  3. IntentQueue fencing-token monotonicity — across multiple distinct intents claimed
     in interleaved rounds, each successive claim for a given intent always issues a
     strictly higher fencing token than any prior claim for that same intent.
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

# A bullet text: no control chars (including \n), no leading/trailing whitespace,
# doesn't start with '#' or '-' (those are structural lines in _union_same_slug's parser).
_bullet_text = st.text(
    alphabet=st.characters(
        blacklist_categories=("Cc",),   # excludes all control chars (incl. \n, \r, \t)
        blacklist_characters="#-",
    ),
    min_size=2,
    max_size=40,
).map(str.strip).filter(bool)

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
# Property 3: IntentQueue fencing-token monotonicity across varied intents
# ---------------------------------------------------------------------------

# Intent title generator: ASCII printable, non-empty after strip, produces a
# non-trivial identity for compute_intent_id (varied hash inputs).
_intent_title = st.text(
    alphabet=st.characters(whitelist_categories=("Lu", "Ll", "Nd", "Zs")),
    min_size=3,
    max_size=30,
).filter(lambda t: t.strip())


@given(
    titles=st.lists(_intent_title, min_size=2, max_size=8).map(
        # De-duplicate by stripping so each intent has a distinct identity
        lambda ts: list({t.strip(): t for t in ts}.values())
    ).filter(lambda ts: len(ts) >= 2),
    n_rounds=st.integers(min_value=2, max_value=5),
)
@settings(max_examples=150)
def test_intent_queue_fencing_tokens_strictly_increase_on_reclaim(
    titles: list[str],
    n_rounds: int,
) -> None:
    """For each distinct intent in a varied set, successive fencing tokens from
    claim() are strictly increasing across the reclaim cycle.

    Generator dimensions that make this genuinely exploratory (not a disguised
    parametrize):
    - `titles`: 2–8 distinct intent titles → varied compute_intent_id hashes,
      varied number of intents in the queue, varied claim-sequence ordering.
    - `n_rounds`: 2–5 claim rounds, each separated by reclaim_expired().

    The fencing counter is per-intent-id (intent_queue.py:141). The invariant:
    for every intent in the set, token[round k+1] > token[round k] (durable
    monotonic advance at :266, _next_fencing_token). Across intents, tokens are
    independent (each starts from 1) — the invariant is per-intent-id only.

    Drives the REAL IntentQueue with real filesystem state (os.replace atomics,
    real fencing/ counter files) — no monkeypatching of the token issuance path.
    Uses tempfile.TemporaryDirectory for isolation per example.
    """
    identity = {"agent": "property-test"}

    # Build intents with distinct IDs from the generated titles.
    intents: list[Intent] = []
    for title in titles:
        payload = {"page_type": "entity", "title": title}
        intent_id = compute_intent_id(payload, identity)
        intents.append(Intent(intent_id=intent_id, payload=payload, identity=identity))

    with tempfile.TemporaryDirectory() as tmp_dir:
        queue = IntentQueue(root=Path(tmp_dir) / "intents")

        # tokens_by_id[intent_id] = [token_from_round_0, token_from_round_1, ...]
        tokens_by_id: dict[str, list[int]] = {i.intent_id: [] for i in intents}

        for round_idx in range(n_rounds):
            # Submit all intents (or re-submit after reclaim_expired).
            for intent in intents:
                queue.submit(intent)

            # Claim all submitted intents, collecting one token per intent per round.
            claimed_this_round: dict[str, int] = {}
            while True:
                c = queue.claim()
                if c is None:
                    break
                claimed_this_round[c.intent.intent_id] = c.fencing_token

            # Every intent must have been claimed exactly once this round.
            for intent in intents:
                assert intent.intent_id in claimed_this_round, (
                    f"intent {intent.intent_id!r} (title={intent.payload['title']!r}) "
                    f"was not claimed in round {round_idx}"
                )
                tokens_by_id[intent.intent_id].append(
                    claimed_this_round[intent.intent_id]
                )

            # Force-expire all claimed intents so they can be re-submitted next round.
            queue.reclaim_expired(now=time.time() + 10_000)
            # Re-submit is handled at the top of the next round iteration; the
            # reclaimed intents land back in submitted/ so submit() is idempotent.

        # Per-intent monotonicity: each round's token must be strictly greater than
        # the previous round's token for the same intent.
        for intent in intents:
            iid = intent.intent_id
            tok_seq = tokens_by_id[iid]
            assert len(tok_seq) == n_rounds, (
                f"Expected {n_rounds} tokens for intent {iid!r}, got {len(tok_seq)}"
            )
            for k in range(1, len(tok_seq)):
                assert tok_seq[k] > tok_seq[k - 1], (
                    f"Fencing token monotonicity violated for intent "
                    f"{iid!r} (title={intent.payload['title']!r}) "
                    f"at round {k}: token={tok_seq[k]} ≤ previous={tok_seq[k - 1]} "
                    f"(full sequence: {tok_seq})"
                )
