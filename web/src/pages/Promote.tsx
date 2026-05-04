import { useEffect, useState } from "react";
import { api } from "../api";
import ResultPanel from "../components/ResultPanel";
import type { OperationResult, ProposalSummary } from "../types";

export default function Promote() {
  const [proposals, setProposals] = useState<ProposalSummary[]>([]);
  const [result, setResult] = useState<OperationResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState<string | null>(null);

  async function refresh() {
    try {
      setProposals(await api.proposals());
    } catch (e: any) {
      setError(e.message);
    }
  }

  useEffect(() => {
    refresh();
  }, []);

  async function run(action: "promote" | "demote" | "reject", slug: string) {
    setBusy(`${action}:${slug}`);
    setError(null);
    setResult(null);
    try {
      const fn =
        action === "promote" ? api.promote : action === "demote" ? api.demote : api.reject;
      const r = await fn(slug);
      setResult(r);
      refresh();
    } catch (e: any) {
      setError(e.message);
    } finally {
      setBusy(null);
    }
  }

  return (
    <div>
      <h1>Promote / Demote / Reject</h1>
      <p className="subtitle">Manage draft and promoted domain proposals.</p>

      {error && (
        <div className="result-panel error">
          <div className="result-status">Error</div>
          <pre>{error}</pre>
        </div>
      )}

      <h2>Proposals</h2>
      <table>
        <thead>
          <tr>
            <th>Slug</th>
            <th>Title</th>
            <th>Status</th>
            <th>Members</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {proposals.map((p) => (
            <tr key={p.slug}>
              <td>{p.slug}</td>
              <td>{p.title}</td>
              <td>{p.status}</td>
              <td>{p.member_sources_count}</td>
              <td>
                {p.status === "draft" && (
                  <>
                    <button
                      className="btn-secondary"
                      onClick={() => run("promote", p.proposed_domain)}
                      disabled={busy === `promote:${p.proposed_domain}`}
                    >
                      Promote
                    </button>
                    {" "}
                    <button
                      className="btn-secondary"
                      onClick={() => run("reject", p.slug)}
                      disabled={busy === `reject:${p.slug}`}
                    >
                      Reject
                    </button>
                  </>
                )}
                {p.status === "blessed" && (
                  <button
                    className="btn-secondary"
                    onClick={() => run("demote", p.proposed_domain)}
                    disabled={busy === `demote:${p.proposed_domain}`}
                  >
                    Demote
                  </button>
                )}
              </td>
            </tr>
          ))}
          {proposals.length === 0 && (
            <tr>
              <td colSpan={5} style={{ color: "#888" }}>
                No proposals. Run `wiki discover-domains` to create some.
              </td>
            </tr>
          )}
        </tbody>
      </table>

      {result && <ResultPanel result={result} />}
    </div>
  );
}
