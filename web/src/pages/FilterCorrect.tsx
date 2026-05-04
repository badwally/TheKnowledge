import { useState } from "react";
import { api } from "../api";
import ResultPanel from "../components/ResultPanel";
import type { OperationResult } from "../types";

export default function FilterCorrect() {
  const [sourceId, setSourceId] = useState("");
  const [decision, setDecision] = useState<"include" | "exclude">("include");
  const [rationale, setRationale] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<OperationResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setResult(null);
    try {
      const r = await api.filterCorrect(sourceId, decision, rationale);
      setResult(r);
    } catch (e: any) {
      setError(e.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div>
      <h1>Correct a filter decision</h1>
      <p className="subtitle">Pin a corrected decision for future filter calibration.</p>

      <div className="op-form">
        <label>Source ID</label>
        <input
          type="text"
          value={sourceId}
          onChange={(e) => setSourceId(e.target.value)}
          placeholder="yt-LfRiBJgD7sk"
        />

        <label>Decision</label>
        <select
          value={decision}
          onChange={(e) => setDecision(e.target.value as "include" | "exclude")}
        >
          <option value="include">include</option>
          <option value="exclude">exclude</option>
        </select>

        <label>Rationale</label>
        <textarea
          value={rationale}
          onChange={(e) => setRationale(e.target.value)}
          placeholder="Why this decision is correct..."
        />

        <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
          {submitting ? "Running..." : "Submit"}
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
