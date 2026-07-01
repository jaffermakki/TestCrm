from sqlalchemy.ext.asyncio import AsyncEngine

from app.database.base import Base


async def create_database(engine: AsyncEngine):

    async with engine.begin() as connection:

        await connection.run_sync(
            Base.metadata.create_all
        )
