import { NavLink, Route, Routes, useLocation } from "react-router-dom";
import DraftsTab from "./DraftsTab";
import ContradictionsTab from "./ContradictionsTab";
import OrphansTab from "./OrphansTab";
import FilterBandTab from "./FilterBandTab";

const TABS = [
  { path: "drafts", label: "Drafts" },
  { path: "contradictions", label: "Contradictions" },
  { path: "orphans", label: "Orphans" },
  { path: "filter-band", label: "Filter-band" },
];

export default function Review() {
  const location = useLocation();
  const activePath = location.pathname.replace(/^\/review\/?/, "") || "drafts";

  return (
    <div>
      <h1>Review</h1>
      <p className="subtitle">Pending curation decisions across the wiki.</p>

      <div
        style={{
          display: "flex",
          gap: 0,
          borderBottom: "1px solid #ddd",
          marginBottom: 12,
        }}
      >
        {TABS.map((t) => {
          const isActive = activePath === t.path;
          return (
            <NavLink
              key={t.path}
              to={`/review/${t.path}`}
              style={{
                padding: "8px 16px",
                fontSize: 12,
                fontWeight: isActive ? 600 : 400,
                color: isActive ? "#1a4c8e" : "#666",
                borderBottom: isActive ? "2px solid #1a4c8e" : "2px solid transparent",
                marginBottom: -1,
                textDecoration: "none",
              }}
            >
              {t.label}
            </NavLink>
          );
        })}
      </div>

      <Routes>
        <Route index element={<DraftsTab />} />
        <Route path="drafts" element={<DraftsTab />} />
        <Route path="contradictions" element={<ContradictionsTab />} />
        <Route path="orphans" element={<OrphansTab />} />
        <Route path="filter-band" element={<FilterBandTab />} />
      </Routes>
    </div>
  );
}
