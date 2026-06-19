"""Deterministic dedup adjudicator precedence (Phase-3 KEYSTONE I1, entry-gate 1b).

Merge authority is alias/canonical exact-or-normalized match + same entity_kind.
Embedding-NN distance is recall-only — it widens the candidate net and can suggest
a link, but never alone triggers a merge.
"""

from __future__ import annotations

from gateway.dedup import adjudicate, DepositIdentity, Candidate


def _id(kind, name, aliases=(), domains=("med",)):
    return DepositIdentity(
        entity_kind=kind, canonical_name=name,
        aliases=tuple(aliases), domains=tuple(domains),
    )


def _cand(slug, kind, name, aliases=(), domains=("med",), dist=0.05):
    return Candidate(
        slug=slug, entity_kind=kind, canonical_name=name,
        aliases=tuple(aliases), domains=tuple(domains), nn_distance=dist,
    )


def test_cross_kind_never_merges_even_at_zero_distance():
    # A drug and a concept with identical names and distance 0.0 must NOT merge.
    v = adjudicate(_id("drug", "Insulin"), [_cand("c1", "concept", "Insulin", dist=0.0)],
                   blocking_band=0.15, identity_threshold=0.30)
    assert v.decision != "merge"
    assert v.rule == "cross-kind-never-merge"


def test_alias_authority_merges_disjoint_surface_at_far_distance():
    # Ozempic ↔ Semaglutide: NN distance 1.0 (lexical encoder gets it backwards),
    # but aliases declare same referent → merge by authority, NOT by geometry.
    ident = _id("drug", "Ozempic", aliases=["Semaglutide"])
    cand = _cand("semaglutide", "drug", "Semaglutide", aliases=["Ozempic", "Wegovy"], dist=1.0)
    v = adjudicate(ident, [cand], blocking_band=0.15, identity_threshold=0.30)
    assert v.decision == "merge"
    assert v.rule == "alias-canonical-exact-match"
    assert v.target_slug == "semaglutide"


def test_shared_surface_distinct_referents_never_merge_on_geometry():
    # Type 1 vs Type 2 diabetes: NN distance 0.198 (< 0.30), same kind, domain
    # overlap, but NO alias/canonical match → must be link at most, never merge.
    ident = _id("concept", "Type 1 diabetes")
    cand = _cand("type-2-diabetes", "concept", "Type 2 diabetes", dist=0.198)
    v = adjudicate(ident, [cand], blocking_band=0.15, identity_threshold=0.30)
    assert v.decision != "merge"


def test_normalized_match_merges_across_punctuation_and_case():
    ident = _id("organization", "Federal Reserve System", aliases=["The Fed"])
    cand = _cand("federal-reserve", "organization", "federal reserve system", dist=0.25)
    v = adjudicate(ident, [cand], blocking_band=0.15, identity_threshold=0.30)
    assert v.decision == "merge"
    assert v.rule == "alias-canonical-exact-match"


def test_no_candidates_is_distinct():
    v = adjudicate(_id("drug", "Tirzepatide"), [], blocking_band=0.15, identity_threshold=0.30)
    assert v.decision == "distinct"
    assert v.target_slug is None


def test_nn_recall_link_when_near_and_domain_overlap_but_no_name_match():
    ident = _id("concept", "reward blunting", domains=["med"])
    cand = _cand("food-noise", "concept", "food noise", domains=["med"], dist=0.12)
    v = adjudicate(ident, [cand], blocking_band=0.15, identity_threshold=0.30)
    assert v.decision == "link"
    assert v.rule == "nn-recall-link"
