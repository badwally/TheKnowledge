import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../../api";
import type { ResearchSessionSummary } from "../../types";
import NewSessionForm from "./NewSessionForm";

interface Props {
  selectedId: string | null;
}

const STATE_LABELS: Record<string, { color: string; label: string }> = {
  plan_only: { color: "#666", label: "plan" },
  edited: { color: "#1a4c8e", label: "edited" },
  running: { color: "#d97706", label: "running" },
  done: { color: "#0a8a3e", label: "done" },
  abandoned: { color: "#dc2626", label: "abandoned" },
};

export default function SessionsList({ selectedId }: Props) {
  const [sessions, setSessions] = useState<ResearchSessionSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showNewForm, setShowNewForm] = useState(false);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      setSessions(await api.listSessions());
    } catch (e: any) {
      setError(e.message);
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
          padding: "12px 12px 8px",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          borderBottom: "1px solid #eee",
        }}
      >
        <div style={{ fontSize: 13, fontWeight: 600 }}>Sessions</div>
        <button
          className="btn-secondary"
          onClick={() => setShowNewForm((v) => !v)}
          style={{ fontSize: 11, padding: "3px 8px" }}
        >
          {showNewForm ? "Cancel" : "+ New"}
        </button>
      </div>

      {showNewForm && (
        <NewSessionForm
          onCreated={() => {
            setShowNewForm(false);
            refresh();
          }}
          onCancel={() => setShowNewForm(false)}
        />
      )}

      {error && (
        <div style={{ padding: 12, color: "#dc2626", fontSize: 12 }}>{error}</div>
      )}

      {loading && !sessions.length && (
        <div style={{ padding: 12, color: "#888", fontSize: 12 }}>Loading…</div>
      )}

      {!loading && sessions.length === 0 && !showNewForm && (
        <div style={{ padding: 12, color: "#888", fontSize: 12 }}>
          No sessions yet. Click "+ New" to start one.
        </div>
      )}

      <div>
        {sessions.map((s) => {
          const isSelected = s.session_id === selectedId;
          const state = STATE_LABELS[s.state] ?? { color: "#888", label: s.state };
          return (
            <Link
              key={s.session_id}
              to={`/research/${s.session_id}`}
              style={{
                display: "block",
                padding: "8px 12px",
                borderBottom: "1px solid #f0f0f0",
                background: isSelected ? "#f0f4fa" : "white",
                borderLeft: isSelected
                  ? "3px solid #1a4c8e"
                  : "3px solid transparent",
                textDecoration: "none",
                color: "inherit",
              }}
            >
              <div style={{ fontSize: 11, fontWeight: 600, marginBottom: 2 }}>
                {s.session_id}
              </div>
              <div style={{ fontSize: 10, color: "#666", marginBottom: 2 }}>
                {s.prompt.slice(0, 80)}
                {s.prompt.length > 80 ? "…" : ""}
              </div>
              <div style={{ fontSize: 10, display: "flex", gap: 8 }}>
                <span style={{ color: state.color, fontWeight: 600 }}>
                  ● {state.label}
                </span>
                <span style={{ color: "#888" }}>{s.domain}</span>
                <span style={{ color: "#888" }}>
                  {s.sources_count != null
                    ? `${s.sources_count} sources`
                    : `${s.query_count} queries`}
                </span>
              </div>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
