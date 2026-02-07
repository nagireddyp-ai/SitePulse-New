import { chatTranscript } from "../data/mockData.js";

export default function Chatbot() {
  return (
    <div className="page">
      <header className="page-header">
        <div>
          <h2>Realtime RAG Assistant</h2>
          <p>Query incidents, logs, and KB articles with source citations.</p>
        </div>
        <button className="primary">Start Live Session</button>
      </header>

      <section className="chat-layout">
        <div className="chat-panel">
          {chatTranscript.map((message, index) => (
            <div key={`${message.sender}-${index}`} className={`chat-bubble ${message.sender}`}>
              <p>{message.text}</p>
              {message.sources ? (
                <div className="chat-sources">
                  {message.sources.map((source) => (
                    <span key={source}>{source}</span>
                  ))}
                </div>
              ) : null}
            </div>
          ))}
        </div>
        <div className="chat-sidebar">
          <h4>Context Feed</h4>
          <div className="context-card">
            <strong>INC-1001</strong>
            <p>Nginx upstream timeouts detected in web-01 logs.</p>
          </div>
          <div className="context-card">
            <strong>KB-3002</strong>
            <p>Disk usage remediation steps for /var cleanup.</p>
          </div>
          <div className="context-card">
            <strong>Log Alert</strong>
            <p>sshd reverse mapping delay on app-02.</p>
          </div>
        </div>
      </section>

      <footer className="chat-input">
        <input placeholder="Ask SitePulse about incidents, logs, or runbooks" />
        <button className="primary">Send</button>
      </footer>
    </div>
  );
}
