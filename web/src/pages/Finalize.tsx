import { useState } from "react";
import { api } from "../api";
import ResultPanel from "../components/ResultPanel";
import type { OperationResult } from "../types";

export default function Finalize() {
  const [pagePath, setPagePath] = useState("");
  const [abandon, setAbandon] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<OperationResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setResult(null);
    try {
      const r = await api.finalize(pagePath, abandon);
      setResult(r);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div>
      <h1>Finalize draft</h1>
      <p className="subtitle">Re-run the validator on a draft page to clear the draft flag.</p>

      <div className="op-form">
        <label>Page path</label>
        <input
          type="text"
          value={pagePath}
          onChange={(e) => setPagePath(e.target.value)}
          placeholder="wiki/synthesis/2026-05-04-my-question.md"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={abandon}
              onChange={(e) => setAbandon(e.target.checked)}
            />
            --abandon (delete the page instead of finalizing)
          </label>
        </div>

        <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
          {submitting ? "Running..." : abandon ? "Abandon" : "Finalize"}
        </button>

        {error && (
          <div className="result-panel error" style={{ marginTop: 16 }}>
            <div className="result-status">Failed</div>
            <pre>{error}</pre>
          </div>
        )}
        {result && <ResultPanel result={result} />}
      </div>
    </div>
  );
}
