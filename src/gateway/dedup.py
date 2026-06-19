"""Deterministic, LLM-free dedup adjudicator (design §6, I1 KEYSTONE).

The Stage-2 procedure decides {merge, link, distinct} from logged inputs with
NO model call and NO embedding geometry as authority. Merge authority is
alias/canonical exact-or-normalized match plus same entity_kind. Embedding-NN
distance is recall-only — it widens the candidate net (Stage 1) and can suggest
a *link*, but never alone triggers a merge (Phase-3 ENTRY GATE: the active
lexical-fallback encoder gets hard identity cases backwards).

Pure functions only: same inputs → same Verdict (replay test). The caller
(CommitGate) gathers candidates from the entity namespace + alias index and
passes them in; this module never touches the index, so it is replayable.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Sequence


@dataclass(frozen=True)
class DepositIdentity:
    entity_kind: str
    canonical_name: str
    aliases: tuple[str, ...] = ()
    domains: tuple[str, ...] = ()


@dataclass(frozen=True)
class Candidate:
    slug: str
    entity_kind: str
    canonical_name: str
    aliases: tuple[str, ...] = ()
    domains: tuple[str, ...] = ()
    nn_distance: float = 1.0


@dataclass(frozen=True)
class Verdict:
    decision: str            # "merge" | "link" | "distinct"
    target_slug: str | None
    rule: str
    basis: dict = field(default_factory=dict)


_PUNCT = re.compile(r"[^\w\s]")
_WS = re.compile(r"\s+")


def normalize_name(s: str) -> str:
    """Casefold, drop punctuation, collapse whitespace — for exact-or-normalized match."""
    return _WS.sub(" ", _PUNCT.sub(" ", s.casefold())).strip()


def _name_set(kind_name: str, aliases: Sequence[str]) -> frozenset[str]:
    return frozenset(normalize_name(n) for n in (kind_name, *aliases) if n)


def adjudicate(
    identity: DepositIdentity,
    candidates: Sequence[Candidate],
    *,
    blocking_band: float,
    identity_threshold: float,
) -> Verdict:
    """Deterministic precedence. Candidates are pre-sorted by the caller; ties are
    broken by ascending nn_distance then slug for total determinism."""
    id_names = _name_set(identity.canonical_name, identity.aliases)
    id_domains = frozenset(identity.domains)

    # Total, deterministic order so the same candidate set always yields the same
    # verdict (replay/I1): nearest first, then slug.
    ordered = sorted(candidates, key=lambda c: (round(c.nn_distance, 6), c.slug))

    best_link: Candidate | None = None
    cross_kind_name_collision: Candidate | None = None
    for c in ordered:
        cand_names = _name_set(c.canonical_name, c.aliases)
        basis = {
            "candidate": c.slug, "candidate_kind": c.entity_kind,
            "nn_distance": round(c.nn_distance, 6),
            "id_names": sorted(id_names), "cand_names": sorted(cand_names),
            "blocking_band": blocking_band, "identity_threshold": identity_threshold,
        }
        # RULE 1 (authority): cross-kind never merges, regardless of distance.
        if c.entity_kind != identity.entity_kind:
            # A cross-kind candidate that shares an exact name is the canonical
            # cross-kind collision — never a merge (record so the verdict names it).
            if (id_names & cand_names) and cross_kind_name_collision is None:
                cross_kind_name_collision = c
                cross_kind_name_collision_basis = basis
            # Not a merge; may still be a related link if topically near.
            if best_link is None and c.nn_distance <= blocking_band:
                best_link = c
            continue
        # RULE 2 (authority): same-kind + alias/canonical exact-or-normalized match → merge.
        if id_names & cand_names:
            return Verdict("merge", c.slug, "alias-canonical-exact-match", basis)
        # RULE 3 (recall-only): same-kind, NO name match. Embedding NN alone does
        # NOT merge. A LINK (related) is proposed only when the pair is within the
        # tight topical blocking_band AND domains overlap. The looser
        # identity_threshold is the merge-candidacy geometry window, but merge
        # requires alias authority — so a same-kind near-but-not-tight pair (two
        # distinct sibling referents like Type-1/Type-2 diabetes or two Fed
        # branches) stays DISTINCT, neither merged nor spuriously linked.
        if c.nn_distance <= blocking_band and (id_domains & frozenset(c.domains)):
            if best_link is None:
                best_link = c

    # A suppressed cross-kind exact-name collision is the named non-merge outcome.
    if cross_kind_name_collision is not None:
        return Verdict(
            "distinct", None, "cross-kind-never-merge",
            cross_kind_name_collision_basis,
        )

    if best_link is not None:
        return Verdict(
            "link", best_link.slug, "nn-recall-link",
            {"candidate": best_link.slug, "nn_distance": round(best_link.nn_distance, 6)},
        )
    return Verdict("distinct", None, "no-authoritative-match", {})
