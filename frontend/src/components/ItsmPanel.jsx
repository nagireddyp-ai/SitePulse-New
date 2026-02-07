import StatusBadge from "./StatusBadge.jsx";
import { incidents, serviceRequests } from "../data/mockData.js";

export default function ItsmPanel() {
  return (
    <div className="page">
      <header className="page-header">
        <div>
          <div className="section-eyebrow">ITSM Control Plane</div>
          <h2>ITSM Operations</h2>
          <p>Incident and service request queues synced with mock ServiceNow.</p>
          <div className="status-row">
            <span className="pill pill-warning">3 nearing SLA breach</span>
            <span className="pill pill-info">Sync every 5 min</span>
          </div>
        </div>
        <div className="header-actions">
          <button className="ghost">View SLA policy</button>
          <button className="primary">Sync Now</button>
        </div>
      </header>

      <section className="metrics-grid">
        <div className="metric-card accent-card">
          <p className="metric-label">Open Incidents</p>
          <h3>18</h3>
          <span className="metric-subtext">P1/P2 prioritized</span>
        </div>
        <div className="metric-card accent-card teal">
          <p className="metric-label">In Progress</p>
          <h3>12</h3>
          <span className="metric-subtext">Actively remediating</span>
        </div>
        <div className="metric-card accent-card amber">
          <p className="metric-label">Resolved Today</p>
          <h3>34</h3>
          <span className="metric-subtext">Auto-closed 8</span>
        </div>
      </section>

      <section className="table-section">
        <div className="section-header">
          <h3>Incidents</h3>
          <span className="pill">{incidents.length} active</span>
        </div>
        <div className="table">
          <div className="table-row header">
            <span>ID</span>
            <span>Title</span>
            <span>Status</span>
            <span>Priority</span>
            <span>SLA</span>
            <span>Owner</span>
          </div>
          {incidents.map((incident) => (
            <div key={incident.id} className="table-row">
              <span>{incident.id}</span>
              <span>{incident.title}</span>
              <StatusBadge status={incident.status} />
              <span>{incident.priority}</span>
              <span className="sla">{incident.sla}</span>
              <span>{incident.owner}</span>
            </div>
          ))}
        </div>
      </section>

      <section className="table-section">
        <div className="section-header">
          <h3>Service Requests</h3>
          <span className="pill">{serviceRequests.length} in queue</span>
        </div>
        <div className="table">
          <div className="table-row header">
            <span>ID</span>
            <span>Title</span>
            <span>Status</span>
            <span>Priority</span>
            <span>SLA</span>
            <span>Owner</span>
          </div>
          {serviceRequests.map((request) => (
            <div key={request.id} className="table-row">
              <span>{request.id}</span>
              <span>{request.title}</span>
              <StatusBadge status={request.status} />
              <span>{request.priority}</span>
              <span className="sla">{request.sla}</span>
              <span>{request.owner}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
