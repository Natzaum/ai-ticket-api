from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def check_status():
    return {"status": "Alive"}
