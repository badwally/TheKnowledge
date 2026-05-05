import type { ReactNode } from "react";

interface Props {
  label: string;
  value: ReactNode;
  detail?: string;
  status?: "healthy" | "warning" | "danger";
}

export default function StatCard({ label, value, detail, status }: Props) {
  const cls = status ? `stat-card ${status}` : "stat-card";
  return (
    <div className={cls}>
      <div className="stat-label">{label}</div>
      <div className="stat-value">{value}</div>
      {detail && <div className="stat-detail">{detail}</div>}
    </div>
  );
}
