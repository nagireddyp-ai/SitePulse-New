const statusStyles = {
  Open: "status open",
  "In Progress": "status progress",
  Resolved: "status resolved",
};

export default function StatusBadge({ status }) {
  return <span className={statusStyles[status] || "status"}>{status}</span>;
}
