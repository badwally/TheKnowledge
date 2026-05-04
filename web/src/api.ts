import type {
  DomainSummary,
  LogEntry,
  OperationResult,
  ProgressResponse,
  ProposalSummary,
  ResearchPlanQueries,
  ResearchSessionDetail,
  ResearchSessionSummary,
  StatusResponse,
  TaskResponse,
} from "./types";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const resp = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });
  if (!resp.ok) {
    let detail: unknown = null;
    try {
      detail = await resp.json();
    } catch (_) {}
    const detailObj = detail as Record<string, unknown> | null;
    const msg = detailObj?.detail
      ? typeof detailObj.detail === "string"
        ? detailObj.detail
        : JSON.stringify(detailObj.detail)
      : `HTTP ${resp.status}`;
    throw new Error(msg);
  }
  return resp.json();
}

export const api = {
  status: () => request<StatusResponse>("/api/status"),
  log: (lines = 50) => request<LogEntry[]>(`/api/log?lines=${lines}`),
  lint: (scope?: string) =>
    request<{ summary: string; report_path: string | null }>(
      `/api/lint${scope ? `?scope=${scope}` : ""}`,
    ),
  domains: () => request<DomainSummary[]>("/api/domains"),
  proposals: () => request<ProposalSummary[]>("/api/proposals"),
  promote: (slug: string) =>
    request<OperationResult>(`/api/domains/${slug}/promote`, { method: "POST" }),
  demote: (slug: string) =>
    request<OperationResult>(`/api/domains/${slug}/demote`, { method: "POST" }),
  reject: (slug: string) =>
    request<OperationResult>(`/api/domains/${slug}/reject`, { method: "POST" }),
  finalize: (page_path: string, abandon: boolean) =>
    request<OperationResult>("/api/ops/finalize", {
      method: "POST",
      body: JSON.stringify({ page_path, abandon }),
    }),
  filterCorrect: (source_id: string, decision: string, rationale: string) =>
    request<OperationResult>("/api/ops/filter-correct", {
      method: "POST",
      body: JSON.stringify({ source_id, decision, rationale }),
    }),
  startIngest: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/ingest", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  startQuery: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/query", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  startBootstrap: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/bootstrap-domain", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  startDiscover: (body: object) =>
    request<{ task_id: string; status: string }>("/api/ops/discover-domains", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  getTask: (id: string) => request<TaskResponse>(`/api/tasks/${id}`),

  // Research (M41)
  listSessions: () => request<ResearchSessionSummary[]>("/api/research/sessions"),
  getSession: (id: string) =>
    request<ResearchSessionDetail>(`/api/research/sessions/${id}`),
  createSession: (body: object) =>
    request<{ task_id: string; status: string }>("/api/research/sessions", {
      method: "POST",
      body: JSON.stringify(body),
    }),
  updatePlan: (id: string, queries: ResearchPlanQueries) =>
    request<ResearchSessionDetail>(`/api/research/sessions/${id}/plan`, {
      method: "PUT",
      body: JSON.stringify({ queries }),
    }),
  executeSession: (id: string, body: object = {}) =>
    request<{ task_id: string; status: string }>(
      `/api/research/sessions/${id}/execute`,
      { method: "POST", body: JSON.stringify(body) },
    ),
  getProgress: (id: string) =>
    request<ProgressResponse>(`/api/research/sessions/${id}/progress`),
};
