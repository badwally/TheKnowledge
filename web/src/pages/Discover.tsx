import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Discover() {
  const [scope, setScope] = useState("");
  const [since, setSince] = useState("");
  const [untagged, setUntagged] = useState(true);

  return (
    <div>
      <h1>Discover candidate domains</h1>
      <p className="subtitle">Cluster sources into draft proposals (bottom-up).</p>

      <div className="op-form">
        <label>Scope (glob, optional)</label>
        <input
          type="text"
          value={scope}
          onChange={(e) => setScope(e.target.value)}
          placeholder="raw/pdf/*.md"
        />

        <label>Since (ISO date, optional)</label>
        <input
          type="text"
          value={since}
          onChange={(e) => setSince(e.target.value)}
          placeholder="2026-04-01"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={untagged}
              onChange={(e) => setUntagged(e.target.checked)}
            />
            --untagged (only sources with no domain)
          </label>
        </div>

        <TaskRunner
          buttonLabel="Discover"
          startTask={() =>
            api.startDiscover({
              scope: scope || null,
              since: since || null,
              untagged,
            })
          }
        />
      </div>
    </div>
  );
}
