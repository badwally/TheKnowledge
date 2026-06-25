# tests/test_bakeoff.py
from pathlib import Path
import yaml
from gateway import paths, search_index, frontmatter as fm
from gateway.scripts.bakeoff import score_config, run_sweep


def _page(slug, body):
    d = paths.wiki_dir() / "concepts"; d.mkdir(parents=True, exist_ok=True)
    (d / f"{slug}.md").write_text(fm.serialize(
        {"type": "concept", "slug": slug, "title": slug, "domains": ["d"],
         "created_at": "2026-01-01T00:00:00Z", "last_updated": "2026-05-01T00:00:00Z"}, body))


def test_score_config_reports_recall_and_zero_leaks(kb_root: Path, tmp_path: Path):
    _page("anhedonia", "## Body\n\nblunted reward sensitivity and lost motivation.\n")
    search_index.refresh(rebuild=True)
    from gateway.retrieval_index import retrieval_index
    retrieval_index().rebuild_from_canonical()
    g = tmp_path / "g.yaml"
    g.write_text(yaml.safe_dump({"queries": [
        {"q": "losing pleasure and drive", "domain": "d", "expect": ["anhedonia"]}]}))
    res = score_config(str(g), k=10)
    assert res["n"] == 1 and res["recall_at_k"] == 1.0
    assert res["placeholder_leaks"] == 0


def test_run_sweep_scores_each_config(kb_root: Path, tmp_path: Path):
    _page("anhedonia", "## Body\n\nblunted reward sensitivity and lost motivation.\n")
    search_index.refresh(rebuild=True)
    g = tmp_path / "g.yaml"
    import yaml as _y
    g.write_text(_y.safe_dump({"queries": [
        {"q": "losing pleasure and drive", "domain": "d", "expect": ["anhedonia"]}]}))
    configs = [{"encoder": "stub", "k_rrf": 60}, {"encoder": "stub", "k_rrf": 10}]
    rows = run_sweep(configs, str(g), [("losing pleasure and drive", "d")])
    assert len(rows) == 2
    for r in rows:
        assert "recall_at_k" in r and "query_ms_p50" in r and r["placeholder_leaks"] == 0
