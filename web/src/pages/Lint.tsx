import { useState } from "react";
import { api } from "../api";

const SCOPES = [
  "all",
  "schema-drift",
  "orphans",
  "drafts",
  "citation-density",
] as const;

export default function Lint() {
  const [scope, setScope] = useState<string>("all");
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<{ summary: string; report_path: string | null } | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setResult(null);
    try {
      const r = await api.lint(scope === "all" ? undefined : scope);
      setResult(r);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div>
      <h1>Lint</h1>
      <p className="subtitle">Run health checks across the wiki.</p>

      <div className="op-form">
        <label>Scope</label>
        <select value={scope} onChange={(e) => setScope(e.target.value)}>
          {SCOPES.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>

        <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
          {submitting ? "Running..." : "Run lint"}
        </button>

        {error && (
          <div className="result-panel error" style={{ marginTop: 16 }}>
            <div className="result-status">Failed</div>
            <pre>{error}</pre>
          </div>
        )}
        {result && (
          <div className="result-panel success" style={{ marginTop: 16 }}>
            <div className="result-status">Lint complete</div>
            <pre>{result.summary}</pre>
            {result.report_path && <pre>report: {result.report_path}</pre>}
          </div>
        )}
      </div>
    </div>
  );
}
