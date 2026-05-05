import { useEffect, useRef, useState } from "react";
import { api } from "../../api";
import type { ProgressStep } from "../../types";

interface Props {
  sessionId: string;
  onTerminal?: () => void;
}

const STATUS_GLYPH: Record<string, { glyph: string; color: string }> = {
  queued: { glyph: "○", color: "#999" },
  running: { glyph: "⟳", color: "#d97706" },
  done: { glyph: "✓", color: "#0a8a3e" },
  failed: { glyph: "✗", color: "#dc2626" },
};

export default function ProgressView({ sessionId, onTerminal }: Props) {
  const [steps, setSteps] = useState<ProgressStep[]>([]);
  const [error, setError] = useState<string | null>(null);
  const intervalRef = useRef<number | null>(null);
  const onTerminalRef = useRef(onTerminal);

  useEffect(() => {
    onTerminalRef.current = onTerminal;
  }, [onTerminal]);

  useEffect(() => {
    let active = true;

    async function poll() {
      try {
        const resp = await api.getProgress(sessionId);
        if (!active) return;
        setSteps(resp.steps);
        const hasFailed = resp.steps.some((s) => s.status === "failed");
        const isDone = resp.steps.some(
          (s) => s.name === "promoted" && s.status === "done",
        );
        if (hasFailed || isDone) {
          if (intervalRef.current) {
            window.clearInterval(intervalRef.current);
            intervalRef.current = null;
          }
          onTerminalRef.current?.();
        }
      } catch (e) {
        const msg = e instanceof Error ? e.message : String(e);
        setError(msg);
      }
    }

    poll();
    intervalRef.current = window.setInterval(poll, 3000);

    return () => {
      active = false;
      if (intervalRef.current) {
        window.clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
    };
  }, [sessionId]);

  if (error) {
    return (
      <div className="result-panel error">
        <div className="result-status">Progress poll failed</div>
        <pre>{error}</pre>
      </div>
    );
  }

  return (
    <div
      style={{
        background: "#f7f7f9",
        borderRadius: 4,
        padding: 12,
        fontFamily: "ui-monospace, monospace",
        fontSize: 11,
        lineHeight: 1.7,
      }}
    >
      {steps.map((s) => {
        const g = STATUS_GLYPH[s.status] ?? { glyph: "?", color: "#888" };
        return (
          <div key={s.name} style={{ color: g.color }}>
            <span style={{ display: "inline-block", width: 16 }}>{g.glyph}</span>
            <span style={{ display: "inline-block", width: 200 }}>{s.name}</span>
            <span style={{ color: "#666" }}>{s.summary}</span>
          </div>
        );
      })}
    </div>
  );
}
