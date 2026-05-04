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
