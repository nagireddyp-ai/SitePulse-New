# SitePulse Backend

FastAPI service that hosts core APIs, agents, and RAG integration.

## Structure
- `app/` FastAPI app and routes
- `config/` configuration and settings
- `services/` integrations (Ollama, ChromaDB)
- `models/` Pydantic models

## Dev Setup (Windows)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
