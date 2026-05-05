import type { OperationResult } from "../types";

interface Props {
  result: OperationResult;
}

export default function ResultPanel({ result }: Props) {
  const cls = result.success
    ? result.no_op
      ? "result-panel running"
      : "result-panel success"
    : "result-panel error";
  const status = result.success
    ? result.no_op
      ? "✓ No-op"
      : "✓ Completed"
    : "✗ Failed";
  return (
    <div className={cls}>
      <div className="result-status">{status}</div>
      <pre>{result.summary}</pre>
      {result.paths_touched.length > 0 && (
        <pre>
          {result.paths_touched.map((p) => `  touched: ${p}`).join("\n")}
        </pre>
      )}
      {result.authorship_report && (
        <pre>
          {`  authorship: ${result.authorship_report.pages_created.length} created, ${result.authorship_report.pages_updated.length} updated`}
          {result.authorship_report.contradictions.length > 0
            ? `, ${result.authorship_report.contradictions.length} contradiction(s) found`
            : ""}
        </pre>
      )}
      {result.warnings.length > 0 && (
        <pre>{result.warnings.map((w) => `  warning: ${w}`).join("\n")}</pre>
      )}
      {result.errors.length > 0 && (
        <pre>{result.errors.map((e) => `  error: ${e}`).join("\n")}</pre>
      )}
    </div>
  );
}
