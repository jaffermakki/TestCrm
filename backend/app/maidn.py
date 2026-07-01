from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.core.lifespan import lifespan

app = FastAPI(
    title="Tech-Pro CRM Enterprise",
    version="3.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router)


@app.get("/")
async def root():
    return {
        "application": "Tech-Pro CRM Enterprise",
        "version": "3.0.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }
