import { useEffect, useRef, useState } from "react";
import { api } from "../../api";
import type { DomainSummary } from "../../types";

interface Props {
  onCreated: () => void;
  onCancel: () => void;
}

export default function NewSessionForm({ onCreated, onCancel }: Props) {
  const [prompt, setPrompt] = useState("");
  const [domain, setDomain] = useState("");
  const [maxResults, setMaxResults] = useState(50);
  const [advanced, setAdvanced] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [taskId, setTaskId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [domains, setDomains] = useState<DomainSummary[]>([]);
  const intervalRef = useRef<number | null>(null);

  useEffect(() => {
    api.domains().then(setDomains).catch(() => {});
    return () => {
      if (intervalRef.current) window.clearInterval(intervalRef.current);
    };
  }, []);

  const slugs = new Set(domains.map((d) => d.slug));
  const domainKnown = domain === "" || slugs.has(domain);

  async function onSubmit() {
    if (!prompt.trim() || !domain.trim()) {
      setError("prompt and domain are both required");
      return;
    }
    setSubmitting(true);
    setError(null);
    try {
      const ack = await api.createSession({
        prompt,
        domain,
        max_results: maxResults,
      });
      setTaskId(ack.task_id);
      intervalRef.current = window.setInterval(async () => {
        try {
          const t = await api.getTask(ack.task_id);
          if (t.status === "done") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setSubmitting(false);
            onCreated();
          } else if (t.status === "failed") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setError(t.error ?? "task failed");
            setSubmitting(false);
          }
        } catch (e: any) {
          setError(e.message);
          if (intervalRef.current) {
            window.clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          setSubmitting(false);
        }
      }, 2000);
    } catch (e: any) {
      setError(e.message);
      setSubmitting(false);
    }
  }

  return (
    <div style={{ padding: 12, background: "#fafafa", borderBottom: "1px solid #eee" }}>
      <label style={{ fontSize: 10, textTransform: "uppercase", color: "#666" }}>
        Prompt
      </label>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="On-device RAG with proprietary data..."
        style={{
          width: "100%",
          fontSize: 12,
          padding: 6,
          border: "1px solid #ccc",
          borderRadius: 3,
          minHeight: 60,
          marginTop: 2,
          fontFamily: "inherit",
          resize: "vertical",
        }}
        disabled={submitting}
      />

      <label
        style={{
          fontSize: 10,
          textTransform: "uppercase",
          color: "#666",
          marginTop: 8,
        }}
      >
        Domain
      </label>
      <input
        type="text"
        list="new-session-domains"
        value={domain}
        onChange={(e) => setDomain(e.target.value)}
        placeholder="start typing or pick from list"
        autoComplete="off"
        style={{
          width: "100%",
          fontSize: 12,
          padding: "5px 8px",
          border: "1px solid #ccc",
          borderRadius: 3,
          marginTop: 2,
        }}
        disabled={submitting}
      />
      <datalist id="new-session-domains">
        {domains.map((d) => (
          <option key={d.slug} value={d.slug}>
            {d.topic} ({d.sources_count})
          </option>
        ))}
      </datalist>
      {!domainKnown && (
        <div style={{ marginTop: 4, color: "#b45309", fontSize: 11 }}>
          "{domain}" is not an existing domain — submission will fail unless this slug exists
        </div>
      )}

      <button
        onClick={() => setAdvanced((v) => !v)}
        style={{
          fontSize: 11,
          color: "#1a4c8e",
          background: "none",
          border: "none",
          cursor: "pointer",
          padding: "8px 0 0",
        }}
      >
        {advanced ? "▾ Hide advanced" : "▸ Advanced"}
      </button>

      {advanced && (
        <div>
          <label
            style={{
              fontSize: 10,
              textTransform: "uppercase",
              color: "#666",
              marginTop: 4,
            }}
          >
            Max results per adapter
          </label>
          <input
            type="number"
            value={maxResults}
            onChange={(e) => setMaxResults(parseInt(e.target.value) || 50)}
            style={{
              width: 100,
              fontSize: 12,
              padding: "4px 6px",
              border: "1px solid #ccc",
              borderRadius: 3,
              marginTop: 2,
            }}
          />
        </div>
      )}

      {error && (
        <div style={{ marginTop: 8, color: "#dc2626", fontSize: 11 }}>{error}</div>
      )}

      {taskId && submitting && (
        <div style={{ marginTop: 8, fontSize: 11, color: "#d97706" }}>
          ⟳ Generating per-adapter queries... (~12s)
        </div>
      )}

      <div style={{ marginTop: 10, display: "flex", gap: 8 }}>
        <button
          className="btn-primary"
          onClick={onSubmit}
          disabled={submitting}
          style={{ fontSize: 11, padding: "5px 14px" }}
        >
          {submitting ? "Creating..." : "Create plan"}
        </button>
        <button
          className="btn-secondary"
          onClick={onCancel}
          disabled={submitting}
          style={{ fontSize: 11, padding: "5px 14px" }}
        >
          Cancel
        </button>
      </div>
    </div>
  );
}
