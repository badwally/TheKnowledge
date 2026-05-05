"""Pydantic models for the web API."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class WatcherState(BaseModel):
    running: bool
    pid: int | None = None
    last_heartbeat: str | None = None


class InboxState(BaseModel):
    pending: int
    failed: int


class StatusResponse(BaseModel):
    watcher: WatcherState
    inbox: InboxState
    drafts: int
    sources: int
    domains: int


class LogEntry(BaseModel):
    timestamp: str
    op: str
    fields: dict[str, str] = {}
    summary: str = ""


class LintResponse(BaseModel):
    summary: str
    report_path: str | None = None
    issues: list[dict[str, Any]] = []


class DomainSummary(BaseModel):
    slug: str
    topic: str = ""
    sources_count: int = 0
    has_notebook: bool = False


class ProposalSummary(BaseModel):
    slug: str
    title: str
    proposed_domain: str
    status: str
    member_sources_count: int


class OperationResultResponse(BaseModel):
    success: bool
    summary: str = ""
    paths_touched: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []
    no_op: bool = False
    authorship_report: dict[str, Any] | None = None


class FinalizeRequest(BaseModel):
    page_path: str
    abandon: bool = False


class FilterCorrectRequest(BaseModel):
    source_id: str
    decision: str  # "include" | "exclude"
    rationale: str


class IngestRequest(BaseModel):
    input: str
    domain: str | None = None
    with_plan: bool = False
    draft: bool = False
    plan_timeout: float | None = None


class QueryRequest(BaseModel):
    question: str
    domain: str
    draft: bool = False


class BootstrapDomainRequest(BaseModel):
    description: str
    slug: str
    force: bool = False


class DiscoverDomainsRequest(BaseModel):
    scope: str | None = None
    since: str | None = None
    untagged: bool = False


class TaskResponse(BaseModel):
    task_id: str
    op_name: str
    status: str
    started_at: str | None = None
    finished_at: str | None = None
    result: dict[str, Any] | None = None
    error: str | None = None


class ResearchSessionSummary(BaseModel):
    session_id: str
    prompt: str
    domain: str
    state: str  # plan_only | edited | running | done | abandoned
    generated_at: str
    edited: bool = False
    query_count: int = 0
    sources_count: int | None = None


class ResearchPlanQueries(BaseModel):
    arxiv: list[str] = []
    youtube: list[str] = []
    web: list[str] = []
    pubmed: list[str] = []


class ResearchPlan(BaseModel):
    queries: ResearchPlanQueries
    target_counts: dict[str, int] = {}


class ResearchSessionDetail(BaseModel):
    session_id: str
    prompt: str
    domain: str
    state: str
    generated_at: str
    edited: bool = False
    plan: ResearchPlan
    sources_count: int | None = None


class CreateSessionRequest(BaseModel):
    prompt: str
    domain: str
    max_results: int = 50


class UpdatePlanRequest(BaseModel):
    queries: ResearchPlanQueries


class ExecuteSessionRequest(BaseModel):
    dry_run: bool = False
    draft: bool = False


class ProgressStep(BaseModel):
    name: str
    status: str  # queued | running | done | failed
    summary: str = ""
    timestamp: str | None = None


class ProgressResponse(BaseModel):
    steps: list[ProgressStep]


class DraftSummary(BaseModel):
    path: str
    type: str
    slug: str
    draft_started_at: str
    draft_unresolved_claims: int = 0
    age_days: float = 0.0


class ContradictionRecord(BaseModel):
    source_id: str = ""
    existing_page: str = ""
    existing_claim: str = ""
    new_claim: str = ""
    severity: str = "moderate"
    recorded_at: str = ""


class OrphanSource(BaseModel):
    source_id: str
    source_type: str
    title: str = ""
    ingested_at: str = ""
    domains: list[str] = []
