import { useEffect, useState } from "react";
import { api } from "../../api";
import type { DraftSummary } from "../../types";

export default function DraftsTab() {
  const [drafts, setDrafts] = useState<DraftSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState<string | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setDrafts(await api.listDrafts());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  async function finalize(path: string, abandon: boolean) {
    if (abandon && !confirm(`Permanently delete ${path}?`)) return;
    setBusy(`${abandon ? "abandon" : "finalize"}:${path}`);
    setError(null);
    try {
      await api.finalize(path, abandon);
      refresh();
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(null);
    }
  }

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
          {loading ? "Loading…" : `${drafts.length} draft${drafts.length === 1 ? "" : "s"}`}
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

      {!loading && drafts.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>No drafts pending.</div>
      )}

      {drafts.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Path</th>
              <th>Type</th>
              <th>Age (days)</th>
              <th>Unresolved</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {drafts.map((d) => {
              const stale = d.age_days > 7;
              return (
                <tr
                  key={d.path}
                  style={{ background: stale ? "#fffbeb" : undefined }}
                >
                  <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                    {d.path}
                  </td>
                  <td>{d.type}</td>
                  <td style={{ color: stale ? "#d97706" : undefined }}>
                    {d.age_days.toFixed(1)}
                  </td>
                  <td>{d.draft_unresolved_claims}</td>
                  <td>
                    <button
                      className="btn-secondary"
                      onClick={() => finalize(d.path, false)}
                      disabled={busy === `finalize:${d.path}`}
                      style={{ fontSize: 11, marginRight: 6 }}
                    >
                      Finalize
                    </button>
                    <button
                      className="btn-secondary"
                      onClick={() => finalize(d.path, true)}
                      disabled={busy === `abandon:${d.path}`}
                      style={{ fontSize: 11, color: "#dc2626", borderColor: "#dc2626" }}
                    >
                      Abandon
                    </button>
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
