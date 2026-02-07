from pydantic import BaseModel


class KnowledgeArticle(BaseModel):
    article_id: str
    title: str
    body: str
    tags: list[str]
    sources: list[str]
