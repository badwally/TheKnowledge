import { useState } from "react";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";

export default function Query() {
  const [question, setQuestion] = useState("");
  const [domain, setDomain] = useState("");
  const [draft, setDraft] = useState(true);

  return (
    <div>
      <h1>Query the wiki</h1>
      <p className="subtitle">Ask the persistent NotebookLM corpus; file the answer as a synthesis.</p>

      <div className="op-form">
        <label>Question</label>
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="What is known about GLP-1 modulation of mesolimbic dopamine?"
        />

        <label>Domain</label>
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
              checked={draft}
              onChange={(e) => setDraft(e.target.checked)}
            />
            --draft
          </label>
        </div>

        <TaskRunner
          buttonLabel="Query"
          startTask={() => api.startQuery({ question, domain, draft })}
        />
      </div>
    </div>
  );
}
