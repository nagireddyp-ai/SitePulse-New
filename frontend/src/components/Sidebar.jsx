const navItems = [
  { id: "dashboard", label: "Dashboard" },
  { id: "kb", label: "Knowledge Base" },
  { id: "chat", label: "Chatbot" },
  { id: "itsm", label: "ITSM" },
];

export default function Sidebar({ active, onNavigate }) {
  return (
    <aside className="sidebar">
      <div className="brand">
        <span className="brand-dot" />
        <div>
          <h1>SitePulse</h1>
          <p>Agentic IT Ops</p>
        </div>
      </div>
      <nav className="nav">
        {navItems.map((item) => (
          <button
            key={item.id}
            className={active === item.id ? "nav-item active" : "nav-item"}
            onClick={() => onNavigate(item.id)}
          >
            {item.label}
          </button>
        ))}
      </nav>
      <div className="sidebar-footer">
        <p>Local-first platform</p>
        <span>Ollama + ChromaDB</span>
      </div>
    </aside>
  );
}
