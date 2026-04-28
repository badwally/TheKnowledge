"""YouTube Data API v3 client for the research pipeline."""

from googleapiclient.discovery import build


def build_client(api_key: str):
    """Build a YouTube Data API v3 client."""
    return build("youtube", "v3", developerKey=api_key)


def search_videos(client, query: str, max_results: int = 50, **kwargs) -> list[dict]:
    """Search YouTube for videos matching a query.

    Args:
        client: YouTube API client from build_client().
        query: Search query string.
        max_results: Maximum results to return (API max per page is 50).
        **kwargs: Additional search parameters (publishedAfter, videoDuration,
                  relevanceLanguage, etc.)

    Returns:
        List of search result items from YouTube API.
    """
    request = client.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=min(max_results, 50),
        **kwargs,
    )
    response = request.execute()
    return response.get("items", [])


def get_video_details(client, video_ids: list[str]) -> dict[str, dict]:
    """Fetch content details and statistics for a batch of video IDs.

    Args:
        client: YouTube API client.
        video_ids: List of video IDs (max 50 per API call).

    Returns:
        Dict mapping video_id to its details response.
    """
    request = client.videos().list(
        part="contentDetails,statistics",
        id=",".join(video_ids[:50]),
    )
    response = request.execute()
    return {item["id"]: item for item in response.get("items", [])}


def check_captions(client, video_id: str) -> bool:
    """Check whether captions are available for a video.

    Note: This costs 50 quota units per call. Use judiciously.

    Args:
        client: YouTube API client.
        video_id: Single video ID.

    Returns:
        True if at least one caption track exists.
    """
    try:
        request = client.captions().list(part="snippet", videoId=video_id)
        response = request.execute()
        return len(response.get("items", [])) > 0
    except Exception:
        return False


def search_and_normalize(
    client, query: str, max_results: int = 50, skip_captions: bool = False, **kwargs
) -> list[dict]:
    """Full search pipeline: search → get details → check captions → normalize.

    Args:
        client: YouTube API client.
        query: Search query.
        max_results: Max results.
        skip_captions: If True, skip caption checks (saves 50 units/video).
        **kwargs: Additional search parameters.

    Returns:
        List of normalized video metadata dicts.
    """
    search_results = search_videos(client, query, max_results, **kwargs)
    if not search_results:
        return []

    video_ids = [item["id"]["videoId"] for item in search_results]
    details_map = get_video_details(client, video_ids)

    normalized = []
    for item in search_results:
        vid = item["id"]["videoId"]
        if vid not in details_map:
            continue
        captions = False if skip_captions else check_captions(client, vid)
        normalized.append(normalize_video(item, details_map[vid], captions))

    return normalized


def normalize_video(search_item: dict, details: dict, captions_available: bool) -> dict:
    """Flatten YouTube API response into our standard video metadata format.

    Args:
        search_item: Item from YouTube search.list response.
        details: Item from YouTube videos.list response (contentDetails + statistics).
        captions_available: Whether captions exist for this video.

    Returns:
        Normalized video metadata dict matching the pipeline schema.
    """
    snippet = search_item["snippet"]
    video_id = search_item["id"]["videoId"]
    description = snippet["description"][:500]
    view_count = int(details.get("statistics", {}).get("viewCount", 0))

    return {
        "video_id": video_id,
        "url": f"https://youtube.com/watch?v={video_id}",
        "title": snippet["title"],
        "channel_name": snippet["channelTitle"],
        "channel_id": snippet["channelId"],
        "publish_date": snippet["publishedAt"],
        "duration": details["contentDetails"]["duration"],
        "view_count": view_count,
        "description": description,
        "has_captions": captions_available,
    }
