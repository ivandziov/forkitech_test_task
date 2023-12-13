from time import monotonic

from fastapi import APIRouter

from src.test_task.schemas import TestResponse
from src.test_task.utils import work

router: APIRouter = APIRouter()


@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1: float = monotonic()
    await work()
    ts2: float = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
