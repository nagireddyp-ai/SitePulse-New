from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "SitePulse API"
    servicenow_base_url: str = "http://localhost:8010"
    chroma_path: str = str(Path(__file__).resolve().parents[3] / "data" / "chroma")
    data_path: str = str(Path(__file__).resolve().parents[3] / "data")
    ollama_host: str = "http://localhost:11434"
    llm_model: str = "llama3.1:8b"
    embedding_model: str = "nomic-embed-text"

    class Config:
        env_prefix = "SITEPULSE_"


settings = Settings()
