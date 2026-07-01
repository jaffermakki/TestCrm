from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Tech-Pro CRM Enterprise",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "application": "Tech-Pro CRM Enterprise",
        "version": "3.0.0",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
