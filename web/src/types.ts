export interface WatcherState {
  running: boolean;
  pid: number | null;
  last_heartbeat: string | null;
}

export interface InboxState {
  pending: number;
  failed: number;
}

export interface StatusResponse {
  watcher: WatcherState;
  inbox: InboxState;
  drafts: number;
  sources: number;
  domains: number;
}

export interface LogEntry {
  timestamp: string;
  op: string;
  fields: Record<string, string>;
  summary: string;
}

export interface DomainSummary {
  slug: string;
  topic: string;
  sources_count: number;
  has_notebook: boolean;
}

export interface ProposalSummary {
  slug: string;
  title: string;
  proposed_domain: string;
  status: string;
  member_sources_count: number;
}

export interface AuthorshipReport {
  pages_created: string[];
  pages_updated: string[];
  contradictions: Array<{
    existing_page: string;
    existing_claim: string;
    new_claim: string;
    source_id: string;
    severity: string;
  }>;
}

export interface OperationResult {
  success: boolean;
  summary: string;
  paths_touched: string[];
  warnings: string[];
  errors: string[];
  no_op: boolean;
  authorship_report: AuthorshipReport | null;
}

export interface TaskResponse {
  task_id: string;
  op_name: string;
  status: "queued" | "running" | "done" | "failed";
  started_at: string | null;
  finished_at: string | null;
  result: OperationResult | null;
  error: string | null;
}
