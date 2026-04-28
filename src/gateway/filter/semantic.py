# src/filter/semantic.py
"""Semantic filtering: construct prompts and parse Claude's scoring responses."""

import json
import yaml


def build_filter_prompt(merged_policy: dict, videos: list[dict]) -> str:
    """Build the full prompt for Claude to evaluate a batch of videos.

    Args:
        merged_policy: Merged editorial policy (template + domain config).
        videos: List of normalized video metadata dicts from Stage 1a.

    Returns:
        Formatted prompt string ready for Claude evaluation.
    """
    policy_yaml = yaml.dump(merged_policy, default_flow_style=False, sort_keys=False)

    video_json = json.dumps(videos, indent=2)

    return f"""## Editorial Policy

{policy_yaml}

## Videos to Evaluate

{video_json}

## Instructions

Evaluate each video against the editorial policy above. For each video, return a JSON array where each element has:
- "video_id": the video's ID
- "relevance_score": integer 1-5 per the scoring rubric
- "inclusion_rationale": 1-2 sentences explaining your score
- "included": boolean (true if relevance_score >= {merged_policy['scoring_rubric']['inclusion_threshold']})

Return ONLY the JSON array, no other text."""


def parse_filter_response(response_text: str) -> list[dict]:
    """Parse Claude's filter response into a list of scoring dicts.

    Args:
        response_text: Claude's response (should be a JSON array).

    Returns:
        List of dicts with video_id, relevance_score, inclusion_rationale, included.

    Raises:
        ValueError: If response cannot be parsed as valid JSON.
    """
    text = response_text.strip()
    # Strip markdown code fences if present
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:-1]) if lines[-1].strip() == "```" else "\n".join(lines[1:])
        text = text.strip()

    try:
        scores = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse Claude's filter response as JSON: {e}")

    if not isinstance(scores, list):
        raise ValueError(f"Expected JSON array, got {type(scores).__name__}")

    return scores


def apply_scores(videos: list[dict], scores: list[dict]) -> list[dict]:
    """Merge Claude's scores back into the video metadata.

    Args:
        videos: Original normalized video metadata.
        scores: Claude's scoring output (from parse_filter_response).

    Returns:
        Videos with relevance_score, inclusion_rationale, and included fields added.
    """
    score_map = {s["video_id"]: s for s in scores}

    result = []
    for video in videos:
        vid = video["video_id"]
        if vid in score_map:
            scored = dict(video)
            scored["relevance_score"] = score_map[vid]["relevance_score"]
            scored["inclusion_rationale"] = score_map[vid]["inclusion_rationale"]
            scored["included"] = score_map[vid]["included"]
            result.append(scored)

    return result


def _source_guidance(source_type: str) -> str:
    """Return evaluation guidance for a source type."""
    guidance = {
        "youtube": "Evaluate channel authority, speaker expertise, and content depth. Prefer substantive technical content over news or hype.",
        "arxiv": "Evaluate methodology rigor, novelty, and relevance to research criteria. Note whether the paper has been peer-reviewed (check journal_ref in source_metadata). Preprints without peer review should still be included if methodology is sound.",
        "pubmed": "Evaluate peer review status, journal quality, and methodology. Prioritize systematic reviews and meta-analyses. Check publication_type in source_metadata.",
        "semantic_scholar": "Evaluate citation impact and field relevance. High citation count with recent influential citations indicates established work.",
    }
    return guidance.get(source_type, "Evaluate based on general quality signals in the editorial policy.")


def build_item_filter_prompt(merged_policy: dict, items: list[dict]) -> str:
    """Build filter prompt for multi-source items.

    Groups items by source_type and includes source-specific evaluation
    guidance so Claude applies appropriate quality signals.

    Args:
        merged_policy: Merged editorial policy (template + domain config).
        items: List of normalized item dicts (ITEM_REQUIRED_FIELDS format).

    Returns:
        Formatted prompt string ready for Claude evaluation.
    """
    policy_yaml = yaml.dump(merged_policy, default_flow_style=False, sort_keys=False)

    # Build source-type preamble
    source_types = sorted(set(item["source_type"] for item in items))
    preamble_parts = []
    for st in source_types:
        count = sum(1 for item in items if item["source_type"] == st)
        guidance = _source_guidance(st)
        preamble_parts.append(f"- **{st}** ({count} items): {guidance}")
    preamble = "\n".join(preamble_parts)

    items_json = json.dumps(items, indent=2)

    return f"""## Editorial Policy

{policy_yaml}

## Source Types in This Batch

{preamble}

## Items to Evaluate

{items_json}

## Instructions

Evaluate each item against the editorial policy above, applying source-appropriate quality signals. For each item, return a JSON array where each element has:
- "item_id": the item's ID
- "relevance_score": integer 1-5 per the scoring rubric
- "inclusion_rationale": 1-2 sentences explaining your score
- "included": boolean (true if relevance_score >= {merged_policy['scoring_rubric']['inclusion_threshold']})

Return ONLY the JSON array, no other text."""


def apply_item_scores(items: list[dict], scores: list[dict]) -> list[dict]:
    """Merge Claude's scores back into item metadata.

    Args:
        items: Original normalized item metadata.
        scores: Claude's scoring output (from parse_filter_response).

    Returns:
        Scored items only. Items without a matching score in the response are dropped.
    """
    score_map = {s["item_id"]: s for s in scores}

    result = []
    for item in items:
        iid = item["item_id"]
        if iid in score_map:
            scored = dict(item)
            scored["relevance_score"] = score_map[iid]["relevance_score"]
            scored["inclusion_rationale"] = score_map[iid]["inclusion_rationale"]
            scored["included"] = score_map[iid]["included"]
            result.append(scored)

    return result
