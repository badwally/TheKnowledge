"""Load and merge editorial policy template with domain configuration."""

import yaml


def load_policy(path: str) -> dict:
    """Load a YAML policy or domain config file."""
    with open(path) as f:
        return yaml.safe_load(f)


def merge_policy(template: dict, domain: dict) -> dict:
    """Merge domain config values into the editorial policy template.

    Domain config values override template values at matching keys.
    Uses recursive dict merge so template-only keys are preserved.
    """
    return _deep_merge(template, domain)


def _deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge override into base. Lists and scalars are replaced."""
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_merged_policy(template_path: str, domain_path: str) -> dict:
    """Convenience: load template and domain, return merged policy."""
    template = load_policy(template_path)
    domain = load_policy(domain_path)
    return merge_policy(template, domain)
