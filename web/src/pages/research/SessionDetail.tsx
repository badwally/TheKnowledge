import { useEffect, useState } from "react";
import { api } from "../../api";
import type { ResearchSessionDetail } from "../../types";
import PlanEditor from "./PlanEditor";
import ProgressView from "./ProgressView";

interface Props {
  sessionId: string;
}

export default function SessionDetail({ sessionId }: Props) {
  const [session, setSession] = useState<ResearchSessionDetail | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [executing, setExecuting] = useState(false);

  async function refresh() {
    setError(null);
    try {
      setSession(await api.getSession(sessionId));
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      setError(msg);
    }
  }

  useEffect(() => {
    refresh();
  }, [sessionId]);

  async function execute() {
    if (!session) return;
    setExecuting(true);
    try {
      await api.executeSession(session.session_id);
      // Optimistically refresh; the polling in ProgressView takes over.
      refresh();
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      setError(msg);
      setExecuting(false);
    }
  }

  if (error) {
    return (
      <div style={{ padding: 16 }}>
        <div className="result-panel error">
          <div className="result-status">Failed to load session</div>
          <pre>{error}</pre>
        </div>
      </div>
    );
  }

  if (!session) {
    return <div style={{ padding: 16, color: "#888" }}>Loading…</div>;
  }

  const showPlanEditor =
    session.state === "plan_only" || session.state === "edited";
  const showProgress = session.state === "running" || executing;
  const showDone = session.state === "done";
  const showAbandoned = session.state === "abandoned";

  return (
    <div style={{ padding: 16 }}>
      <div style={{ marginBottom: 12 }}>
        <div style={{ fontSize: 14, fontWeight: 600, marginBottom: 2 }}>
          {session.session_id}
        </div>
        <div style={{ fontSize: 11, color: "#666", marginBottom: 4 }}>
          {session.prompt}
        </div>
        <div style={{ fontSize: 10, color: "#888" }}>
          {session.domain} · {session.state}
          {session.edited && " · edited"}
        </div>
      </div>

      {showPlanEditor && (
        <>
          <PlanEditor session={session} onSaved={(s) => setSession(s)} />
          <div style={{ marginTop: 12 }}>
            <button
              className="btn-primary"
              onClick={execute}
              disabled={executing}
            >
              Execute →
            </button>
          </div>
        </>
      )}

      {showProgress && (
        <ProgressView sessionId={session.session_id} onTerminal={refresh} />
      )}

      {showDone && (
        <div className="result-panel success" style={{ marginTop: 12 }}>
          <div className="result-status">Promoted</div>
          <pre>
            {`${session.sources_count ?? "?"} source(s) added to ${session.domain} corpus`}
          </pre>
          <pre style={{ marginTop: 8, fontSize: 11 }}>
            Synthesis pages live under wiki/synthesis/{session.session_id}-*.md
          </pre>
        </div>
      )}

      {showAbandoned && (
        <div className="result-panel error" style={{ marginTop: 12 }}>
          <div className="result-status">Abandoned</div>
          <pre>
            Session was abandoned during execute. Check the activity feed on
            Dashboard or the per-step progress in log.md for the failure cause.
          </pre>
        </div>
      )}
    </div>
  );
}
