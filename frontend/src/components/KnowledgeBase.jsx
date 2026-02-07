import { kbArticles } from "../data/mockData.js";

export default function KnowledgeBase() {
  return (
    <div className="page">
      <header className="page-header">
        <div>
          <h2>Knowledge Base</h2>
          <p>AI-generated runbooks and resolutions sourced from incidents.</p>
        </div>
        <div className="header-actions">
          <input className="search" placeholder="Search KB articles" />
          <button className="primary">Create Article</button>
        </div>
      </header>

      <section className="kb-grid">
        {kbArticles.map((article) => (
          <article key={article.id} className="kb-card">
            <div className="kb-header">
              <span className="pill">{article.id}</span>
              <span className="updated">Updated {article.updated}</span>
            </div>
            <h3>{article.title}</h3>
            <p>{article.summary}</p>
            <div className="kb-tags">
              {article.tags.map((tag) => (
                <span key={tag} className="tag">
                  {tag}
                </span>
              ))}
            </div>
            <div className="kb-sources">
              <span>Sources:</span>
              {article.sources.map((source) => (
                <span key={source} className="source">
                  {source}
                </span>
              ))}
            </div>
          </article>
        ))}
      </section>
    </div>
  );
}
