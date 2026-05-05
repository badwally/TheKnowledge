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

export interface ResearchPlanQueries {
  arxiv: string[];
  youtube: string[];
  web: string[];
  pubmed: string[];
}

export interface ResearchPlan {
  queries: ResearchPlanQueries;
  target_counts: Record<string, number>;
}

export interface ResearchSessionSummary {
  session_id: string;
  prompt: string;
  domain: string;
  state: "plan_only" | "edited" | "running" | "done" | "abandoned";
  generated_at: string;
  edited: boolean;
  query_count: number;
  sources_count: number | null;
}

export interface ResearchSessionDetail {
  session_id: string;
  prompt: string;
  domain: string;
  state: "plan_only" | "edited" | "running" | "done" | "abandoned";
  generated_at: string;
  edited: boolean;
  plan: ResearchPlan;
  sources_count: number | null;
}

export interface ProgressStep {
  name: string;
  status: "queued" | "running" | "done" | "failed";
  summary: string;
  timestamp: string | null;
}

export interface ProgressResponse {
  steps: ProgressStep[];
}

export interface DraftSummary {
  path: string;
  type: string;
  slug: string;
  draft_started_at: string;
  draft_unresolved_claims: number;
  age_days: number;
}

export interface ContradictionRecord {
  source_id: string;
  existing_page: string;
  existing_claim: string;
  new_claim: string;
  severity: string;
  recorded_at: string;
}

export interface OrphanSource {
  source_id: string;
  source_type: string;
  title: string;
  ingested_at: string;
  domains: string[];
}

export interface FilterBandSource {
  source_id: string;
  source_type: string;
  title: string;
  score: number;
  threshold_review: number;
  threshold_include: number;
  domain: string;
}

export interface ArtifactSummary {
  slug: string;
  type: string;
  title: string;
  domain: string;
  created_at: string;
  nlm_artifact_url: string | null;
}
