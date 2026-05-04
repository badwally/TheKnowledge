import { useEffect, useRef, useState } from "react";
import { api } from "../api";
import type { OperationResult, TaskResponse } from "../types";
import ResultPanel from "./ResultPanel";

interface Props {
  // Returns the task_id from the start endpoint, or null on synchronous failure.
  startTask: () => Promise<{ task_id: string; status: string } | null>;
  buttonLabel?: string;
}

export default function TaskRunner({ startTask, buttonLabel = "Run" }: Props) {
  const [taskId, setTaskId] = useState<string | null>(null);
  const [task, setTask] = useState<TaskResponse | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const intervalRef = useRef<number | null>(null);

  useEffect(() => {
    return () => {
      if (intervalRef.current) window.clearInterval(intervalRef.current);
    };
  }, []);

  async function onSubmit() {
    setSubmitting(true);
    setError(null);
    setTask(null);
    setTaskId(null);
    try {
      const ack = await startTask();
      if (!ack) {
        setSubmitting(false);
        return;
      }
      setTaskId(ack.task_id);
      intervalRef.current = window.setInterval(async () => {
        try {
          const t = await api.getTask(ack.task_id);
          setTask(t);
          if (t.status === "done" || t.status === "failed") {
            if (intervalRef.current) {
              window.clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
            setSubmitting(false);
          }
        } catch (e: any) {
          setError(e.message);
          if (intervalRef.current) {
            window.clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          setSubmitting(false);
        }
      }, 3000);
    } catch (e: any) {
      setError(e.message);
      setSubmitting(false);
    }
  }

  const result: OperationResult | null = task?.result ?? null;

  return (
    <>
      <button className="btn-primary" onClick={onSubmit} disabled={submitting}>
        {submitting ? "Running..." : buttonLabel}
      </button>
      {error && (
        <div className="result-panel error" style={{ marginTop: 16 }}>
          <div className="result-status">Submission failed</div>
          <pre>{error}</pre>
        </div>
      )}
      {taskId && task && task.status !== "done" && task.status !== "failed" && (
        <div className="result-panel running" style={{ marginTop: 16 }}>
          <div className="result-status">⟳ {task.status}</div>
          <pre>task_id: {taskId}</pre>
        </div>
      )}
      {task && task.status === "failed" && (
        <div className="result-panel error" style={{ marginTop: 16 }}>
          <div className="result-status">✗ Task failed</div>
          <pre>{task.error}</pre>
        </div>
      )}
      {task && task.status === "done" && result && <ResultPanel result={result} />}
    </>
  );
}
