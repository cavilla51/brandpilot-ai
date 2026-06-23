from fastapi import FastAPI

from app.api.auth import router as auth_router

from app.database import engine
from app.database import Base

from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BrandPilot AI",
    version="0.1.0"
)

app.include_router(auth_router)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "brandpilot-api"
    }