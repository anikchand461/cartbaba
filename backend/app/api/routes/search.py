from fastapi import APIRouter
from app.services.recommender import run_cartbaba

router = APIRouter(prefix="/search")

@router.post("/")
def search(query: str):
    return run_cartbaba(query)
