import { useState } from "react";
import { api } from "../../api";
import type { ResearchPlanQueries, ResearchSessionDetail } from "../../types";

interface Props {
  session: ResearchSessionDetail;
  onSaved: (updated: ResearchSessionDetail) => void;
}

const ADAPTERS: Array<keyof ResearchPlanQueries> = [
  "arxiv",
  "youtube",
  "web",
  "pubmed",
];

export default function PlanEditor({ session, onSaved }: Props) {
  const [queries, setQueries] = useState<ResearchPlanQueries>(session.plan.queries);
  const [original] = useState<ResearchPlanQueries>(session.plan.queries);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  function isEdited(adapter: keyof ResearchPlanQueries, idx: number): boolean {
    const orig = original[adapter];
    return orig[idx] !== queries[adapter][idx];
  }

  function isAdded(adapter: keyof ResearchPlanQueries, idx: number): boolean {
    return idx >= original[adapter].length;
  }

  function updateQuery(
    adapter: keyof ResearchPlanQueries,
    idx: number,
    value: string,
  ) {
    setQueries((prev) => ({
      ...prev,
      [adapter]: prev[adapter].map((q, i) => (i === idx ? value : q)),
    }));
  }

  function addQuery(adapter: keyof ResearchPlanQueries) {
    setQueries((prev) => ({
      ...prev,
      [adapter]: [...prev[adapter], ""],
    }));
  }

  function removeQuery(adapter: keyof ResearchPlanQueries, idx: number) {
    setQueries((prev) => ({
      ...prev,
      [adapter]: prev[adapter].filter((_, i) => i !== idx),
    }));
  }

  async function save() {
    setSaving(true);
    setError(null);
    try {
      // Strip empty rows
      const cleaned: ResearchPlanQueries = {
        arxiv: queries.arxiv.filter((q) => q.trim()),
        youtube: queries.youtube.filter((q) => q.trim()),
        web: queries.web.filter((q) => q.trim()),
        pubmed: queries.pubmed.filter((q) => q.trim()),
      };
      const updated = await api.updatePlan(session.session_id, cleaned);
      onSaved(updated);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setSaving(false);
    }
  }

  return (
    <div>
      {ADAPTERS.map((adapter) => (
        <div key={adapter} style={{ marginBottom: 16 }}>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: 4,
            }}
          >
            <div style={{ fontSize: 11, fontWeight: 600, textTransform: "uppercase" }}>
              {adapter} ({queries[adapter].length})
            </div>
            <button
              onClick={() => addQuery(adapter)}
              style={{
                fontSize: 11,
                color: "#1a4c8e",
                background: "none",
                border: "none",
                cursor: "pointer",
              }}
            >
              + add
            </button>
          </div>
          {queries[adapter].length === 0 && (
            <div style={{ fontSize: 11, color: "#999", fontStyle: "italic" }}>
              (no queries)
            </div>
          )}
          {queries[adapter].map((q, idx) => {
            const edited = isEdited(adapter, idx) || isAdded(adapter, idx);
            return (
              <div
                key={idx}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 6,
                  marginBottom: 3,
                  background: edited ? "#fffbeb" : "#f7f7f9",
                  border: edited ? "1px dashed #d97706" : "1px solid transparent",
                  borderRadius: 3,
                  padding: 2,
                }}
              >
                <input
                  type="text"
                  value={q}
                  onChange={(e) => updateQuery(adapter, idx, e.target.value)}
                  style={{
                    flex: 1,
                    border: "none",
                    background: "transparent",
                    padding: "4px 8px",
                    fontSize: 12,
                    fontFamily: "inherit",
                  }}
                />
                <button
                  onClick={() => removeQuery(adapter, idx)}
                  style={{
                    background: "none",
                    border: "none",
                    color: "#888",
                    cursor: "pointer",
                    fontSize: 14,
                    padding: "0 6px",
                  }}
                  title="Remove"
                >
                  ×
                </button>
              </div>
            );
          })}
        </div>
      ))}

      {error && (
        <div style={{ color: "#dc2626", fontSize: 12, marginTop: 8 }}>{error}</div>
      )}

      <div style={{ marginTop: 12, display: "flex", gap: 8 }}>
        <button className="btn-primary" onClick={save} disabled={saving}>
          {saving ? "Saving..." : "Save plan"}
        </button>
      </div>
    </div>
  );
}
