import { useState } from "react";
import Sidebar from "./components/Sidebar.jsx";
import Dashboard from "./components/Dashboard.jsx";
import KnowledgeBase from "./components/KnowledgeBase.jsx";
import Chatbot from "./components/Chatbot.jsx";
import ItsmPanel from "./components/ItsmPanel.jsx";

const views = {
  dashboard: Dashboard,
  kb: KnowledgeBase,
  chat: Chatbot,
  itsm: ItsmPanel,
};

export default function App() {
  const [activeView, setActiveView] = useState("dashboard");
  const ActiveComponent = views[activeView];

  return (
    <div className="app">
      <Sidebar active={activeView} onNavigate={setActiveView} />
      <main className="content">
        <div className="topbar">
          <div>
            <h1>SitePulse Command Center</h1>
            <p>Local-first AI operations for incident triage, knowledge, and SLA tracking.</p>
          </div>
          <div className="topbar-actions">
            <input className="search" placeholder="Search incidents, KB, logs" />
            <button className="ghost">New Incident</button>
            <button className="primary">Launch Agent Run</button>
          </div>
        </div>
        <ActiveComponent />
      </main>
    </div>
  );
}
