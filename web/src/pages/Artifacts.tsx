import { useEffect, useRef, useState } from "react";
import { api } from "../api";
import type {
  ArtifactSummary,
  DomainSummary,
  OperationResult,
  TaskResponse,
} from "../types";

interface ConfirmModalProps {
  title: string;
  body: string;
  onConfirm: () => void;
  onCancel: () => void;
}

function ConfirmModal({ title, body, onConfirm, onCancel }: ConfirmModalProps) {
  return (
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
      onClick={onCancel}
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
        <h3 style={{ marginTop: 0 }}>{title}</h3>
        <p style={{ fontSize: 13, color: "#444" }}>{body}</p>
        <div style={{ marginTop: 12, display: "flex", gap: 8, justifyContent: "flex-end" }}>
          <button className="btn-secondary" onClick={onCancel}>
            Cancel
          </button>
          <button className="btn-primary" onClick={onConfirm}>
            Confirm & generate
          </button>
        </div>
      </div>
    </div>
  );
}

interface ReviseModalProps {
  artifactSlug: string;
  onConfirm: (instructions: string[]) => void;
  onCancel: () => void;
}

function ReviseModal({ artifactSlug, onConfirm, onCancel }: ReviseModalProps) {
  const [rows, setRows] = useState<Array<{ slide: string; text: string }>>([
    { slide: "", text: "" },
  ]);

  function addRow() {
    setRows((r) => [...r, { slide: "", text: "" }]);
  }

  function update(i: number, field: "slide" | "text", value: string) {
    setRows((r) => r.map((row, idx) => (idx === i ? { ...row, [field]: value } : row)));
  }

  function submit() {
    const instructions = rows
      .filter((r) => r.slide.trim() && r.text.trim())
      .map((r) => `slide ${r.slide.trim()}: ${r.text.trim()}`);
    if (instructions.length === 0) return;
    onConfirm(instructions);
  }

  return (
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
      onClick={onCancel}
    >
      <div
        style={{
          background: "white",
          borderRadius: 6,
          padding: 20,
          width: 560,
          maxWidth: "90%",
          boxShadow: "0 4px 12px rgba(0,0,0,0.2)",
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <h3 style={{ marginTop: 0 }}>
          Revise <code style={{ fontSize: 12 }}>{artifactSlug}</code>
        </h3>
        {rows.map((r, i) => (
          <div key={i} style={{ marginBottom: 8, display: "flex", gap: 6, alignItems: "flex-start" }}>
            <span style={{ fontSize: 11, paddingTop: 6 }}>Slide</span>
            <input
              type="text"
              value={r.slide}
              onChange={(e) => update(i, "slide", e.target.value)}
              placeholder="N"
              style={{ width: 60, fontSize: 12, padding: 6, border: "1px solid #ccc", borderRadius: 3 }}
            />
            <textarea
              value={r.text}
              onChange={(e) => update(i, "text", e.target.value)}
              placeholder="instructions for this slide…"
              style={{
                flex: 1,
                fontSize: 12,
                padding: 6,
                border: "1px solid #ccc",
                borderRadius: 3,
                minHeight: 40,
                fontFamily: "inherit",
                resize: "vertical",
              }}
            />
          </div>
        ))}
        <button
          onClick={addRow}
          style={{ fontSize: 11, color: "#1a4c8e", background: "none", border: "none", cursor: "pointer", padding: "4px 0" }}
        >
          + Add another revision
        </button>
        <div style={{ marginTop: 12, display: "flex", gap: 8, justifyContent: "flex-end" }}>
          <button className="btn-secondary" onClick={onCancel}>
            Cancel
          </button>
          <button className="btn-primary" onClick={submit}>
            Confirm & revise
          </button>
        </div>
      </div>
    </div>
  );
}

interface AsyncOpState {
  taskId: string | null;
  status: "queued" | "running" | "done" | "failed" | null;
  result: OperationResult | null;
  error: string | null;
}

const INITIAL_OP: AsyncOpState = { taskId: null, status: null, result: null, error: null };

function useAsyncOp(): [AsyncOpState, (start: () => Promise<{ task_id: string; status: string }>) => Promise<void>] {
  const [state, setState] = useState<AsyncOpState>(INITIAL_OP);
  const intervalRef = useRef<number | null>(null);

  useEffect(() => {
    return () => {
      if (intervalRef.current) window.clearInterval(intervalRef.current);
    };
  }, []);

  async function trigger(start: () => Promise<{ task_id: string; status: string }>) {
    setState({ taskId: null, status: "queued", result: null, error: null });
    try {
      const ack = await start();
      setState((s) => ({ ...s, taskId: ack.task_id }));
      intervalRef.current = window.setInterval(async () => {
        try {
          const t: TaskResponse = await api.getTask(ack.task_id);
          if (t.status === "done") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setState({ taskId: ack.task_id, status: "done", result: t.result, error: null });
          } else if (t.status === "failed") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setState({ taskId: ack.task_id, status: "failed", result: null, error: t.error });
          } else {
            setState((s) => ({ ...s, status: t.status }));
          }
        } catch (e) {
          setState((s) => ({
            ...s,
            status: "failed",
            error: e instanceof Error ? e.message : String(e),
          }));
          if (intervalRef.current) {
            window.clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
        }
      }, 3000);
    } catch (e) {
      setState({
        taskId: null,
        status: "failed",
        result: null,
        error: e instanceof Error ? e.message : String(e),
      });
    }
  }

  return [state, trigger];
}

function OpStatus({ label, state }: { label: string; state: AsyncOpState }) {
  if (!state.status) return null;
  if (state.status === "queued" || state.status === "running") {
    return (
      <div className="result-panel running" style={{ marginTop: 8 }}>
        <div className="result-status">⟳ {label}: {state.status}</div>
      </div>
    );
  }
  if (state.status === "failed") {
    return (
      <div className="result-panel error" style={{ marginTop: 8 }}>
        <div className="result-status">✗ {label} failed</div>
        <pre>{state.error ?? ""}</pre>
      </div>
    );
  }
  if (state.status === "done" && state.result) {
    return (
      <div className="result-panel success" style={{ marginTop: 8 }}>
        <div className="result-status">✓ {label} done</div>
        <pre>{state.result.summary}</pre>
        {state.result.paths_touched.length > 0 && (
          <pre>{state.result.paths_touched.map((p) => `  touched: ${p}`).join("\n")}</pre>
        )}
      </div>
    );
  }
  return null;
}

export default function Artifacts() {
  const [domains, setDomains] = useState<DomainSummary[]>([]);
  const [selectedSlug, setSelectedSlug] = useState<string>("");
  const [artifacts, setArtifacts] = useState<ArtifactSummary[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loadingDomains, setLoadingDomains] = useState(true);

  // Add-source form
  const [sourceId, setSourceId] = useState("");
  const [addBusy, setAddBusy] = useState(false);
  const [addResult, setAddResult] = useState<OperationResult | null>(null);

  // Topic inputs
  const [audioTopic, setAudioTopic] = useState("");
  const [slidesTopic, setSlidesTopic] = useState("");

  // Async ops
  const [syncState, runSync] = useAsyncOp();
  const [briefingState, runBriefing] = useAsyncOp();
  const [audioState, runAudio] = useAsyncOp();
  const [slidesState, runSlides] = useAsyncOp();
  const [reviseState, runRevise] = useAsyncOp();

  // Confirm modals
  const [confirm, setConfirm] = useState<
    | { kind: "sync" | "briefing" | "audio" | "slides"; title: string; body: string; onConfirm: () => void }
    | null
  >(null);

  // Revise modal
  const [reviseTarget, setReviseTarget] = useState<string | null>(null);

  async function loadDomains() {
    setLoadingDomains(true);
    setError(null);
    try {
      const all = await api.domains();
      const withNotebook = all.filter((d) => d.has_notebook);
      setDomains(withNotebook);
      if (!selectedSlug && withNotebook.length > 0) {
        setSelectedSlug(withNotebook[0].slug);
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoadingDomains(false);
    }
  }

  async function loadArtifacts(slug: string) {
    if (!slug) {
      setArtifacts([]);
      return;
    }
    try {
      setArtifacts(await api.listArtifacts(slug));
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    }
  }

  useEffect(() => {
    loadDomains();
  }, []);

  useEffect(() => {
    loadArtifacts(selectedSlug);
  }, [selectedSlug]);

  async function addSource() {
    if (!sourceId.trim() || !selectedSlug) return;
    setAddBusy(true);
    setAddResult(null);
    setError(null);
    try {
      const r = await api.nlmAdd(selectedSlug, sourceId.trim());
      setAddResult(r);
      setSourceId("");
      loadArtifacts(selectedSlug);
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setAddBusy(false);
    }
  }

  function confirmSync() {
    setConfirm({
      kind: "sync",
      title: `Sync all sources for ${selectedSlug}?`,
      body: `Adds every raw source tagged with ${selectedSlug} to its NotebookLM corpus. Idempotent. May take minutes for large domains.`,
      onConfirm: () => {
        setConfirm(null);
        runSync(() => api.nlmSync(selectedSlug));
      },
    });
  }

  function confirmBriefing() {
    setConfirm({
      kind: "briefing",
      title: `Generate briefing for ${selectedSlug}?`,
      body: "Calls NotebookLM and may take 1-5 minutes. Confirm to proceed.",
      onConfirm: () => {
        setConfirm(null);
        runBriefing(() => api.nlmBriefing(selectedSlug));
      },
    });
  }

  function confirmAudio() {
    if (!audioTopic.trim()) return;
    setConfirm({
      kind: "audio",
      title: `Generate audio for ${selectedSlug}?`,
      body: `Topic: "${audioTopic.trim()}". Calls NotebookLM and may take 1-5 minutes.`,
      onConfirm: () => {
        setConfirm(null);
        runAudio(() => api.nlmAudio(selectedSlug, audioTopic.trim()));
      },
    });
  }

  function confirmSlides() {
    if (!slidesTopic.trim()) return;
    setConfirm({
      kind: "slides",
      title: `Generate slides for ${selectedSlug}?`,
      body: `Topic: "${slidesTopic.trim()}". Calls NotebookLM and may take 1-5 minutes.`,
      onConfirm: () => {
        setConfirm(null);
        runSlides(() => api.nlmSlides(selectedSlug, slidesTopic.trim()));
      },
    });
  }

  function submitRevise(instructions: string[]) {
    if (!reviseTarget) return;
    const target = reviseTarget;
    setReviseTarget(null);
    runRevise(() => api.nlmRevise(target, instructions));
  }

  return (
    <div>
      <h1>Artifacts</h1>
      <p className="subtitle">
        Manage a domain's NotebookLM corpus and generate briefings, audio overviews, and slide decks.
      </p>

      {error && (
        <div className="result-panel error" style={{ marginBottom: 12 }}>
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      <div style={{ marginBottom: 16 }}>
        <label style={{ fontSize: 11, textTransform: "uppercase", color: "#666" }}>
          Domain
        </label>
        <select
          value={selectedSlug}
          onChange={(e) => setSelectedSlug(e.target.value)}
          disabled={loadingDomains}
          style={{
            display: "block",
            marginTop: 4,
            fontSize: 13,
            padding: "5px 8px",
            border: "1px solid #ccc",
            borderRadius: 3,
            minWidth: 320,
          }}
        >
          {domains.length === 0 && <option value="">(no domains with NotebookLM corpus)</option>}
          {domains.map((d) => (
            <option key={d.slug} value={d.slug}>
              {d.slug} — {d.topic}
            </option>
          ))}
        </select>
      </div>

      {selectedSlug && (
        <>
          <h2>Add source to corpus</h2>
          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Source ID</label>
            <input
              type="text"
              value={sourceId}
              onChange={(e) => setSourceId(e.target.value)}
              placeholder="yt-LfRiBJgD7sk"
            />
            <div style={{ marginTop: 8, display: "flex", gap: 8, alignItems: "center" }}>
              <button className="btn-primary" onClick={addSource} disabled={addBusy}>
                {addBusy ? "Adding…" : "Add"}
              </button>
              <button className="btn-secondary" onClick={confirmSync}>
                Sync all sources for this domain
              </button>
            </div>
            {addResult && (
              <div
                className={addResult.success ? "result-panel success" : "result-panel error"}
                style={{ marginTop: 8 }}
              >
                <div className="result-status">{addResult.success ? "✓ Added" : "✗ Failed"}</div>
                <pre>{addResult.summary}</pre>
              </div>
            )}
            <OpStatus label="Sync" state={syncState} />
          </div>

          <h2>Generate artifact</h2>
          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Briefing (no topic — uses corpus-wide context)</label>
            <button
              className="btn-primary"
              onClick={confirmBriefing}
              disabled={briefingState.status === "queued" || briefingState.status === "running"}
              style={{ marginTop: 4 }}
            >
              Generate briefing
            </button>
            <OpStatus label="Briefing" state={briefingState} />
          </div>

          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Audio overview — Topic</label>
            <input
              type="text"
              value={audioTopic}
              onChange={(e) => setAudioTopic(e.target.value)}
              placeholder="e.g., reward circuit primer"
            />
            <button
              className="btn-primary"
              onClick={confirmAudio}
              disabled={!audioTopic.trim() || audioState.status === "queued" || audioState.status === "running"}
              style={{ marginTop: 8 }}
            >
              Generate audio
            </button>
            <OpStatus label="Audio" state={audioState} />
          </div>

          <div className="op-form" style={{ marginBottom: 16 }}>
            <label>Slide deck — Topic</label>
            <input
              type="text"
              value={slidesTopic}
              onChange={(e) => setSlidesTopic(e.target.value)}
              placeholder="e.g., alcohol use disorder evidence"
            />
            <button
              className="btn-primary"
              onClick={confirmSlides}
              disabled={!slidesTopic.trim() || slidesState.status === "queued" || slidesState.status === "running"}
              style={{ marginTop: 8 }}
            >
              Generate slides
            </button>
            <OpStatus label="Slides" state={slidesState} />
          </div>

          <h2>Existing artifacts</h2>
          {artifacts.length === 0 && (
            <div style={{ color: "#888", fontSize: 12 }}>No artifacts for this domain yet.</div>
          )}
          {artifacts.length > 0 && (
            <table>
              <thead>
                <tr>
                  <th>Slug</th>
                  <th>Type</th>
                  <th>Title</th>
                  <th>Created</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {artifacts.map((a) => (
                  <tr key={a.slug}>
                    <td style={{ fontFamily: "ui-monospace, monospace", fontSize: 11 }}>
                      {a.slug}
                    </td>
                    <td>{a.type}</td>
                    <td style={{ fontSize: 11, maxWidth: 280, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      {a.title}
                    </td>
                    <td style={{ fontSize: 11 }}>{a.created_at}</td>
                    <td>
                      {a.type === "slides" && (
                        <button
                          className="btn-secondary"
                          onClick={() => setReviseTarget(a.slug)}
                          style={{ fontSize: 11, marginRight: 6 }}
                        >
                          Revise
                        </button>
                      )}
                      {a.nlm_artifact_url && (
                        <a
                          href={a.nlm_artifact_url}
                          target="_blank"
                          rel="noreferrer"
                          className="btn-secondary"
                          style={{ fontSize: 11, textDecoration: "none", padding: "3px 8px" }}
                        >
                          Open in NotebookLM
                        </a>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
          <OpStatus label="Revise" state={reviseState} />
        </>
      )}

      {confirm && (
        <ConfirmModal
          title={confirm.title}
          body={confirm.body}
          onConfirm={confirm.onConfirm}
          onCancel={() => setConfirm(null)}
        />
      )}

      {reviseTarget && (
        <ReviseModal
          artifactSlug={reviseTarget}
          onConfirm={submitRevise}
          onCancel={() => setReviseTarget(null)}
        />
      )}
    </div>
  );
}
