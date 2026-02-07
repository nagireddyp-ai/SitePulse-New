from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def sync_servicenow() -> dict:
    return {"status": "queued"}
