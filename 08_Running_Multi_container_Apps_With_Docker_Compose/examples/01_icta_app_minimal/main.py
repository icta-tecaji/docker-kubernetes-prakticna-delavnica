"""ICTA app, version 1, minimal app."""

from __future__ import annotations

import redis
from fastapi import FastAPI
from pydantic import BaseModel
from redis import exceptions

app = FastAPI()
cache = redis.Redis(host="redis", port=6379)


class TotalHits(BaseModel):
    """Model for total hits on the server."""

    hits: int | None = None


async def get_hit_count() -> int | None:
    """Get total hits on the server."""
    try:
        res = await cache.incr("hits")
        return int(res)
    except exceptions.ConnectionError as exc:
        print(f"Error connecting to Redis: {exc}")  # noqa: T201
        return None


@app.get("/hits", summary="Get total hits on the server", response_model=TotalHits)
async def get_total_hits() -> TotalHits:
    """Get total hits on the server."""
    count = await get_hit_count()
    return TotalHits(hits=count)
