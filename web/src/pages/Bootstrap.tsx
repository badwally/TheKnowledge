import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Bootstrap() {
  const [description, setDescription] = useState("");
  const [slug, setSlug] = useState("");
  const [force, setForce] = useState(false);

  return (
    <div>
      <h1>Bootstrap a new domain</h1>
      <p className="subtitle">Author a starter policy.yaml from a natural-language description.</p>

      <div className="op-form">
        <label>Description (1-3 sentences)</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="On-device LLM inference for autonomous agentic workflows: edge runtimes, quantization, inter-agent protocols..."
        />

        <label>Slug</label>
        <input
          type="text"
          value={slug}
          onChange={(e) => setSlug(e.target.value)}
          placeholder="edge-ai-agentic"
        />

        <div className="checkbox-row">
          <label>
            <input
              type="checkbox"
              checked={force}
              onChange={(e) => setForce(e.target.checked)}
            />
            --force (overwrite existing non-promoted policy)
          </label>
        </div>

        <TaskRunner
          buttonLabel="Bootstrap"
          startTask={() => api.startBootstrap({ description, slug, force })}
        />
      </div>
    </div>
  );
}
