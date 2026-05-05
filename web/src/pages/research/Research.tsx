import { useParams } from "react-router-dom";
import SessionsList from "./SessionsList";
import SessionDetail from "./SessionDetail";

export default function Research() {
  const { sessionId } = useParams();
  return (
    <div style={{ display: "flex", height: "100%", gap: 0 }}>
      <div style={{ width: "42%", borderRight: "1px solid #eee", overflow: "auto" }}>
        <SessionsList selectedId={sessionId ?? null} />
      </div>
      <div style={{ flex: 1, overflow: "auto", padding: "0 4px" }}>
        {sessionId ? (
          <SessionDetail sessionId={sessionId} />
        ) : (
          <div style={{ padding: 20, color: "#888" }}>
            <p className="subtitle">
              Select a session on the left, or click "+ New" to start one.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
