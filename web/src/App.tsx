import { NavLink, Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Finalize from "./pages/Finalize";
import FilterCorrect from "./pages/FilterCorrect";
import Ingest from "./pages/Ingest";
import Query from "./pages/Query";

function Sidebar() {
  return (
    <nav className="sidebar">
      <div className="sidebar-brand">wiki</div>
      <div className="sidebar-group-label">Wiki</div>
      <NavLink to="/" end>Dashboard</NavLink>
      <NavLink to="/ops/ingest">Ingest</NavLink>
      <NavLink to="/ops/query">Query</NavLink>
      <NavLink to="/ops/finalize">Finalize</NavLink>
      <NavLink to="/ops/filter-correct">Filter correct</NavLink>
      <div className="sidebar-group-label">Domains</div>
      <NavLink to="/domains/bootstrap">Bootstrap</NavLink>
      <NavLink to="/domains/discover">Discover</NavLink>
      <NavLink to="/domains/promote">Promote</NavLink>
      <div className="sidebar-group-label">System</div>
      <NavLink to="/system/lint">Lint</NavLink>
    </nav>
  );
}

function Placeholder({ name }: { name: string }) {
  return (
    <div>
      <h1>{name}</h1>
      <p className="subtitle">Page not yet implemented.</p>
    </div>
  );
}

export default function App() {
  return (
    <div className="app">
      <Sidebar />
      <main className="content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/ops/ingest" element={<Ingest />} />
          <Route path="/ops/query" element={<Query />} />
          <Route path="/ops/finalize" element={<Finalize />} />
          <Route path="/ops/filter-correct" element={<FilterCorrect />} />
          <Route path="/domains/bootstrap" element={<Placeholder name="Bootstrap domain" />} />
          <Route path="/domains/discover" element={<Placeholder name="Discover domains" />} />
          <Route path="/domains/promote" element={<Placeholder name="Promote / Demote / Reject" />} />
          <Route path="/system/lint" element={<Placeholder name="Lint" />} />
        </Routes>
      </main>
    </div>
  );
}
