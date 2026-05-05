import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { api } from "../api";
import TaskRunner from "../components/TaskRunner";
import type { DomainSummary } from "../types";

export default function Query() {
  const [question, setQuestion] = useState("");
  const [domain, setDomain] = useState("");
  const [draft, setDraft] = useState(true);
  const [domains, setDomains] = useState<DomainSummary[]>([]);
  const [domainsError, setDomainsError] = useState<string | null>(null);

  const [searchParams] = useSearchParams();

  useEffect(() => {
    const domainParam = searchParams.get("domain");
    if (domainParam) setDomain(domainParam);
    // We deliberately don't read source_id — it's informational context;
    // the user can paste it into the question textarea if useful.
  }, [searchParams]);

  useEffect(() => {
    api
      .domains()
      .then(setDomains)
      .catch((e) => setDomainsError(e.message ?? String(e)));
  }, []);

  const slugs = new Set(domains.map((d) => d.slug));
  const domainKnown = domain === "" || slugs.has(domain);

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
          list="query-domains"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          placeholder="start typing or pick from list"
          autoComplete="off"
        />
        <datalist id="query-domains">
          {domains.map((d) => (
            <option key={d.slug} value={d.slug}>
              {d.topic} ({d.sources_count})
            </option>
          ))}
        </datalist>
        {domainsError && (
          <div className="form-hint form-hint-error">
            could not load domains: {domainsError}
          </div>
        )}
        {!domainsError && !domainKnown && (
          <div className="form-hint form-hint-warn">
            "{domain}" is not an existing domain — query will fail unless this slug exists
          </div>
        )}

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
