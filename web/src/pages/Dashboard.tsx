import { useEffect, useState } from "react";
import { api } from "../api";
import type { LogEntry, StatusResponse } from "../types";
import StatCard from "../components/StatCard";
import ActivityFeed from "../components/ActivityFeed";

export default function Dashboard() {
  const [status, setStatus] = useState<StatusResponse | null>(null);
  const [log, setLog] = useState<LogEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function refresh() {
    setLoading(true);
    setError(null);
    try {
      const [s, l] = await Promise.all([api.status(), api.log(20)]);
      setStatus(s);
      setLog(l);
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
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>Knowledge base</h1>
        <button className="btn-secondary" onClick={refresh} disabled={loading}>
          {loading ? "Refreshing..." : "Refresh"}
        </button>
      </div>
      <p className="subtitle">Daily glance at watcher state, drafts, and recent activity.</p>

      {error && (
        <div className="result-panel error">
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      {status && (
        <div className="stat-grid">
          <StatCard
            label="Watcher"
            value={status.watcher.running ? "running" : "stopped"}
            detail={status.watcher.last_heartbeat ?? "no heartbeat"}
            status={status.watcher.running ? "healthy" : "danger"}
          />
          <StatCard
            label="Inbox"
            value={status.inbox.pending}
            detail={`${status.inbox.failed} failed`}
            status={status.inbox.failed > 0 ? "warning" : undefined}
          />
          <StatCard
            label="Drafts"
            value={status.drafts}
            status={status.drafts > 0 ? "warning" : undefined}
          />
          <StatCard
            label="Sources"
            value={status.sources}
            detail={`${status.domains} domains`}
          />
        </div>
      )}

      <h2>Recent activity</h2>
      <ActivityFeed entries={log} />
    </div>
  );
}
