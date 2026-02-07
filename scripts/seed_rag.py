import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_ROOT = PROJECT_ROOT / "backend"
for path in (PROJECT_ROOT, BACKEND_ROOT):
    if str(path) not in sys.path:
        sys.path.append(str(path))

from app.config.settings import settings
from rag.pipeline import RagPipeline


def load_json(path: Path):
    return json.loads(path.read_text())


def main() -> None:
    pipeline = RagPipeline(
        chroma_path=settings.chroma_path,
        model=settings.llm_model,
        embedding_model=settings.embedding_model,
        ollama_host=settings.ollama_host,
    )
    data_path = Path(settings.data_path)
    kb_articles = load_json(data_path / "kb_articles.json")
    incidents = load_json(data_path / "incidents.json")

    for article in kb_articles:
        pipeline.ingest(article["body"], {"type": "kb", "title": article["title"], "article_id": article["article_id"]})

    for incident in incidents:
        pipeline.ingest(
            incident["description"],
            {
                "type": "incident",
                "title": incident["title"],
                "incident_id": incident["incident_id"],
                "priority": incident["priority"],
            },
        )

    print("Seeded RAG store with incidents and KB articles.")


if __name__ == "__main__":
    main()
