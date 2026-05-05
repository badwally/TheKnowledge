import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Ingest() {
  const [input, setInput] = useState("");
  const [domain, setDomain] = useState("");
  const [withPlan, setWithPlan] = useState(false);
  const [draft, setDraft] = useState(false);

  return (
    <div>
      <h1>Ingest source</h1>
      <p className="subtitle">URL or local path → raw/ + wiki/sources/</p>

      <div className="op-form">
        <label>Input</label>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="https://example.com/article  or  /path/to/file.pdf"
        />

        <label>Domain (optional)</label>
        <input
          type="text"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          placeholder="glp1-reward-modulation"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={withPlan}
              onChange={(e) => setWithPlan(e.target.checked)}
            />
            --with-plan
          </label>
          <label>
            <input
              type="checkbox"
              checked={draft}
              onChange={(e) => setDraft(e.target.checked)}
            />
            --draft
          </label>
        </div>

        <TaskRunner
          buttonLabel="Ingest"
          startTask={() =>
            api.startIngest({
              input,
              domain: domain || null,
              with_plan: withPlan,
              draft,
            })
          }
        />
      </div>
    </div>
  );
}
