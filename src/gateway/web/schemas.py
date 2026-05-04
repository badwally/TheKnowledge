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
