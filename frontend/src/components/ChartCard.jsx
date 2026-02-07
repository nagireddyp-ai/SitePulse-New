export default function ChartCard({ title, children, subtitle }) {
  return (
    <div className="chart-card">
      <div className="chart-header">
        <div>
          <h4>{title}</h4>
          {subtitle ? <p>{subtitle}</p> : null}
        </div>
      </div>
      <div className="chart-body">{children}</div>
    </div>
  );
}
