from fastapi import APIRouter, Query
from app.services.jsearch_fetcher import fetch_jobs

router = APIRouter()

@router.get("/jobs")
def get_jobs(role: str = Query(default="developer"), location: str = Query(default="India")):
    jobs = fetch_jobs(role=role, location=location)
    return {"jobs": jobs}
