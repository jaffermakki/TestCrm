from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.init_db import create_database
from app.database.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):

    await create_database(engine)

    yield

    await engine.dispose()
