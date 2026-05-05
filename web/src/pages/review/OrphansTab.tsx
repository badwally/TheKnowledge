import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../../api";
import type { OrphanSource } from "../../types";

export default function OrphansTab() {
  const [orphans, setOrphans] = useState<OrphanSource[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setOrphans(await api.listOrphans());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 8,
        }}
      >
        <div style={{ fontSize: 12, color: "#666" }}>
          {loading
            ? "Loading…"
            : `${orphans.length} orphan source${orphans.length === 1 ? "" : "s"}`}
        </div>
        <button
          className="btn-secondary"
          onClick={refresh}
          disabled={loading}
          style={{ fontSize: 11 }}
        >
          Refresh
        </button>
      </div>

      {error && (
        <div className="result-panel error" style={{ marginBottom: 12 }}>
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      {!loading && orphans.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>
          No orphan sources. Every ingested source is cited by at least one wiki page.
        </div>
      )}

      {orphans.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Source ID</th>
              <th>Type</th>
              <th>Title</th>
              <th>Domain</th>
              <th>Ingested</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {orphans.map((o) => {
              const primaryDomain = o.domains[0] || "";
              const queryHref = `/ops/query?domain=${encodeURIComponent(primaryDomain)}&source_id=${encodeURIComponent(o.source_id)}`;
              return (
                <tr key={o.source_id}>
                  <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                    {o.source_id}
                  </td>
                  <td>{o.source_type}</td>
                  <td style={{ fontSize: 11, maxWidth: 320, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                    {o.title}
                  </td>
                  <td style={{ fontSize: 11 }}>{primaryDomain || "—"}</td>
                  <td style={{ fontSize: 11 }}>{o.ingested_at}</td>
                  <td>
                    <Link
                      to={queryHref}
                      className="btn-secondary"
                      style={{ fontSize: 11, textDecoration: "none", padding: "3px 8px" }}
                    >
                      Discharge via query
                    </Link>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}
