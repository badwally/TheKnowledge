"""Derive YouTube search queries from domain configuration."""

import yaml


def load_domain_queries(domain_path: str) -> list[str]:
    """Generate search queries from the domain config.

    Extracts the topic and key terms to produce a set of search queries
    that cover the domain from multiple angles.

    Args:
        domain_path: Path to domain config YAML.

    Returns:
        List of search query strings.
    """
    with open(domain_path) as f:
        domain = yaml.safe_load(f)

    topic = domain["domain"]["topic"]
    field = domain["domain"]["field"]

    # Use explicit queries if provided, otherwise auto-generate
    search_queries = domain.get("search_queries", {})
    youtube_queries = search_queries.get("youtube")
    if youtube_queries:
        return youtube_queries

    # Fallback: core topic + field-qualified variant
    queries = [topic]
    queries.append(f"{field} {topic}")

    return queries
