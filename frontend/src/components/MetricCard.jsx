export default function MetricCard({ label, value, subtext }) {
  return (
    <div className="metric-card">
      <p className="metric-label">{label}</p>
      <h3>{value}</h3>
      {subtext ? <span className="metric-subtext">{subtext}</span> : null}
    </div>
  );
}
