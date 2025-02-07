from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from src.async_db import get_async_db_session
from src.models import CollisionModel

app = FastAPI()


@app.get("/collisions/{collision_id}", response_model=CollisionModel)
async def get_collision(
    collision_id: int, session: AsyncSession = Depends(get_async_db_session)
):
    result = await session.get(CollisionModel, collision_id)
    if not result:
        return {"error": "Collision not found"}
    return result
