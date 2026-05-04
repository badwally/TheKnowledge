import type { LogEntry } from "../types";

interface Props {
  entries: LogEntry[];
}

function formatEntry(entry: LogEntry): string {
  const ts = entry.timestamp.replace("T", " ").replace("Z", "");
  const fields = Object.entries(entry.fields)
    .map(([k, v]) => `${k}=${v}`)
    .join(" ");
  return `${ts} ${entry.op}${fields ? " " + fields : ""}`;
}

export default function ActivityFeed({ entries }: Props) {
  if (entries.length === 0) {
    return <div className="activity-feed">(no recent activity)</div>;
  }
  return (
    <div className="activity-feed">
      {entries.map((e, i) => (
        <div key={i}>{formatEntry(e)}</div>
      ))}
    </div>
  );
}
