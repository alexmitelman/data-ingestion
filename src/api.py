from fastapi import Depends, FastAPI, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import func

from src.async_db import get_async_db_session
from src.models import CollisionModel

app = FastAPI()


@app.get("/collisions/", response_model=list[CollisionModel])
async def get_collisions(
    borough: str | None = None,
    injuries_min: int | None = None,
    injuries_max: int | None = None,
    sort_by: str = Query(
        "crash_datetime", enum=["crash_datetime", "number_of_persons_injured"]
    ),
    order: str = Query("desc", enum=["asc", "desc"]),
    page: int = 1,
    limit: int = 10,
    session: AsyncSession = Depends(get_async_db_session),
):
    query = select(CollisionModel)

    if borough:
        query = query.where(func.lower(CollisionModel.borough) == borough.lower())
    if injuries_min is not None:
        query = query.where(CollisionModel.number_of_persons_injured >= injuries_min)
    if injuries_max is not None:
        query = query.where(CollisionModel.number_of_persons_injured <= injuries_max)

    if order == "desc":
        query = query.order_by(getattr(CollisionModel, sort_by).desc())
    else:
        query = query.order_by(getattr(CollisionModel, sort_by).asc())

    query = query.offset((page - 1) * limit).limit(limit)
    result = await session.execute(query)
    return result.scalars().all()


@app.get("/collisions/{collision_id}", response_model=CollisionModel)
async def get_collision(
    collision_id: int, session: AsyncSession = Depends(get_async_db_session)
):
    result = await session.get(CollisionModel, collision_id)
    if not result:
        return {"error": "Collision not found"}
    return result
