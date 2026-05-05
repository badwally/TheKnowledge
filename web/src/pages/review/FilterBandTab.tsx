import { useEffect, useState } from "react";
import { api } from "../../api";
import type { FilterBandSource } from "../../types";

export default function FilterBandTab() {
  const [items, setItems] = useState<FilterBandSource[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState<string | null>(null);
  const [modal, setModal] = useState<
    { source_id: string; decision: "include" | "exclude" } | null
  >(null);
  const [rationale, setRationale] = useState("");

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setItems(await api.listFilterBand());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  function openModal(source_id: string, decision: "include" | "exclude") {
    setModal({ source_id, decision });
    setRationale("");
  }

  async function submitCorrection() {
    if (!modal) return;
    if (!rationale.trim()) {
      setError("rationale is required");
      return;
    }
    setBusy(`${modal.decision}:${modal.source_id}`);
    setError(null);
    try {
      await api.filterCorrect(modal.source_id, modal.decision, rationale);
      setModal(null);
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
          {loading ? "Loading…" : `${items.length} source${items.length === 1 ? "" : "s"} in review band`}
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

      {!loading && items.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>
          No sources in the review band (between threshold_review and threshold_include for any domain).
        </div>
      )}

      {items.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Source ID</th>
              <th>Type</th>
              <th>Title</th>
              <th>Score</th>
              <th>Domain</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {items.map((s) => (
              <tr key={s.source_id}>
                <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                  {s.source_id}
                </td>
                <td>{s.source_type}</td>
                <td style={{ fontSize: 11, maxWidth: 280, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                  {s.title}
                </td>
                <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                  {s.score.toFixed(2)}
                </td>
                <td style={{ fontSize: 11 }}>{s.domain}</td>
                <td>
                  <button
                    className="btn-secondary"
                    onClick={() => openModal(s.source_id, "include")}
                    disabled={busy === `include:${s.source_id}`}
                    style={{ fontSize: 11, marginRight: 6, color: "#0a8a3e", borderColor: "#0a8a3e" }}
                  >
                    Include
                  </button>
                  <button
                    className="btn-secondary"
                    onClick={() => openModal(s.source_id, "exclude")}
                    disabled={busy === `exclude:${s.source_id}`}
                    style={{ fontSize: 11, color: "#dc2626", borderColor: "#dc2626" }}
                  >
                    Exclude
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {modal && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "rgba(0,0,0,0.4)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 100,
          }}
          onClick={() => setModal(null)}
        >
          <div
            style={{
              background: "white",
              borderRadius: 6,
              padding: 20,
              width: 480,
              maxWidth: "90%",
              boxShadow: "0 4px 12px rgba(0,0,0,0.2)",
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <h3 style={{ marginTop: 0 }}>
              {modal.decision === "include" ? "Include" : "Exclude"}{" "}
              <code style={{ fontSize: 12 }}>{modal.source_id}</code>
            </h3>
            <label style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>
              Rationale
            </label>
            <textarea
              value={rationale}
              onChange={(e) => setRationale(e.target.value)}
              placeholder="Why this decision is correct..."
              style={{
                width: "100%",
                fontSize: 12,
                padding: 6,
                border: "1px solid #ccc",
                borderRadius: 3,
                minHeight: 80,
                marginTop: 4,
                fontFamily: "inherit",
                resize: "vertical",
              }}
            />
            <div style={{ marginTop: 12, display: "flex", gap: 8, justifyContent: "flex-end" }}>
              <button
                className="btn-secondary"
                onClick={() => setModal(null)}
                disabled={!!busy}
              >
                Cancel
              </button>
              <button
                className="btn-primary"
                onClick={submitCorrection}
                disabled={!!busy || !rationale.trim()}
              >
                {busy ? "Submitting..." : "Submit"}
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
