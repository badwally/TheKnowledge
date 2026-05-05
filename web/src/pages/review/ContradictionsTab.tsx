import { Fragment, useEffect, useState } from "react";
import { api } from "../../api";
import type { ContradictionRecord } from "../../types";

const SEVERITY_STYLE: Record<string, { bg: string; color: string }> = {
  minor: { bg: "#f0f0f0", color: "#666" },
  moderate: { bg: "#fffbeb", color: "#d97706" },
  major: { bg: "#fef2f2", color: "#dc2626" },
};

export default function ContradictionsTab() {
  const [records, setRecords] = useState<ContradictionRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [expandedIdx, setExpandedIdx] = useState<number | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setRecords(await api.listContradictions());
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
            : `${records.length} contradiction${records.length === 1 ? "" : "s"}`}
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

      {!loading && records.length === 0 && (
        <div style={{ color: "#888", fontSize: 12 }}>
          No contradictions recorded yet. Authorship runs with `--with-plan` populate this log when conflicts are detected.
        </div>
      )}

      {records.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Recorded</th>
              <th>Source</th>
              <th>Affected page</th>
              <th>Severity</th>
              <th>Existing claim</th>
              <th>New claim</th>
            </tr>
          </thead>
          <tbody>
            {records.map((r, idx) => {
              const sev = SEVERITY_STYLE[r.severity] ?? SEVERITY_STYLE.moderate;
              const expanded = expandedIdx === idx;
              return (
                <Fragment key={`fragment-${idx}`}>
                  <tr
                    onClick={() => setExpandedIdx(expanded ? null : idx)}
                    style={{ cursor: "pointer" }}
                  >
                    <td style={{ fontSize: 11 }}>{r.recorded_at}</td>
                    <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                      {r.source_id}
                    </td>
                    <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                      {r.existing_page}
                    </td>
                    <td>
                      <span
                        style={{
                          fontSize: 10,
                          padding: "2px 8px",
                          borderRadius: 3,
                          background: sev.bg,
                          color: sev.color,
                          fontWeight: 600,
                        }}
                      >
                        {r.severity}
                      </span>
                    </td>
                    <td style={{ fontSize: 11, maxWidth: 250, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      {r.existing_claim}
                    </td>
                    <td style={{ fontSize: 11, maxWidth: 250, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      {r.new_claim}
                    </td>
                  </tr>
                  {expanded && (
                    <tr>
                      <td colSpan={6} style={{ background: "#fafafa", padding: 12 }}>
                        <div style={{ marginBottom: 8 }}>
                          <div style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>Existing claim</div>
                          <div style={{ fontSize: 12, marginTop: 2 }}>{r.existing_claim}</div>
                        </div>
                        <div>
                          <div style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>New claim (from {r.source_id})</div>
                          <div style={{ fontSize: 12, marginTop: 2 }}>{r.new_claim}</div>
                        </div>
                        <div style={{ marginTop: 8, fontSize: 11, color: "#666" }}>
                          Resolve by editing <code>{r.existing_page}</code> in your editor; the M42 console is read-only.
                        </div>
                      </td>
                    </tr>
                  )}
                </Fragment>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}
