from fastapi import FastAPI

from app.routes import chat, incidents, kb, metrics, servicenow_sync

app = FastAPI(title="SitePulse API", version="0.1.0")

app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(incidents.router, prefix="/incidents", tags=["incidents"])
app.include_router(kb.router, prefix="/kb", tags=["kb"])
app.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
app.include_router(servicenow_sync.router, prefix="/servicenow-sync", tags=["servicenow"])


@app.get("/")
def health_check() -> dict:
    return {"status": "ok", "service": "sitepulse"}
