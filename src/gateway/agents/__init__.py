"""Gateway agents package.

Agents are triggered by events (ingest.complete, poll.complete, schedules) and
coordinate gateway ops autonomously. Each agent exposes a single run function
returning a typed result; agents never call filter-correct or perform hard
destructive ops without explicit human confirmation.
"""
