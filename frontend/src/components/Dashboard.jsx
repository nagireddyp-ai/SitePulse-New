import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  LineChart,
  Line,
} from "recharts";
import MetricCard from "./MetricCard.jsx";
import ChartCard from "./ChartCard.jsx";
import InsightsPanel from "./InsightsPanel.jsx";
import {
  dashboardMetrics,
  incidentStatus,
  slaTrend,
  resolutionTimes,
} from "../data/mockData.js";

const PIE_COLORS = ["#7C5CFF", "#2DD4BF", "#FDBA74"];

export default function Dashboard() {
  return (
    <div className="page">
      <header className="page-header">
        <div>
          <div className="section-eyebrow">Realtime Mission Control</div>
          <h2>Operational Overview</h2>
          <p>Track live SLA performance, ticket volume, and resolution speed.</p>
          <div className="status-row">
            <span className="pill pill-success">SLA 98.2%</span>
            <span className="pill pill-warning">2 breaches today</span>
            <span className="pill pill-info">Agents active: 5</span>
          </div>
        </div>
        <div className="header-actions">
          <button className="ghost">Download PDF</button>
          <button className="primary">Export Snapshot</button>
        </div>
      </header>

      <section className="metrics-grid">
        <MetricCard label="MTTR" value={`${dashboardMetrics.mttr} min`} subtext="Avg last 7 days" />
        <MetricCard label="SLA Breaches" value={dashboardMetrics.slaBreaches} subtext="Rolling 24h" />
        <MetricCard label="Ticket Volume" value={dashboardMetrics.ticketVolume} subtext="Open + in progress" />
        <MetricCard label="Agent Actions" value={dashboardMetrics.agentActions} subtext="Automated workflows" />
      </section>

      <section className="sla-banner">
        <div>
          <h3>SLA Health</h3>
          <p>Keep critical incidents within 2-hour resolution targets.</p>
        </div>
        <div className="sla-meter">
          <div className="sla-progress" style={{ width: "82%" }} />
        </div>
        <div className="sla-meta">
          <span>82% within target</span>
          <span>Target: 95%</span>
        </div>
      </section>

      <section className="charts-grid">
        <ChartCard title="Incident Status Distribution" subtitle="Open vs. in-progress vs. resolved">
          <ResponsiveContainer width="100%" height={220}>
            <PieChart>
              <Pie data={incidentStatus} dataKey="value" innerRadius={60} outerRadius={90} paddingAngle={4}>
                {incidentStatus.map((entry, index) => (
                  <Cell key={entry.name} fill={PIE_COLORS[index % PIE_COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </ChartCard>

        <ChartCard title="Resolution Times" subtitle="Avg minutes by category">
          <ResponsiveContainer width="100%" height={220}>
            <BarChart data={resolutionTimes} margin={{ top: 10, right: 20, left: 0, bottom: 0 }}>
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="minutes" fill="#7C5CFF" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </ChartCard>

        <ChartCard title="SLA Trend" subtitle="Breaches vs. resolved tickets">
          <ResponsiveContainer width="100%" height={220}>
            <LineChart data={slaTrend} margin={{ top: 10, right: 20, left: 0, bottom: 0 }}>
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="resolved" stroke="#2DD4BF" strokeWidth={3} />
              <Line type="monotone" dataKey="breaches" stroke="#F97316" strokeWidth={3} />
            </LineChart>
          </ResponsiveContainer>
        </ChartCard>

        <InsightsPanel
          title="Realtime Highlights"
          items={[
            "P1 incident INC-1001 flagged for upstream timeout.",
            "SLA compliance holding at 98.2%.",
            "Knowledge base auto-refresh completed 4 minutes ago.",
          ]}
        />
      </section>
    </div>
  );
}
