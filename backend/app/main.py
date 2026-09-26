from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.api.auth import router as auth_router
from app.api.cards import router as cards_router
from app.api.catalog import router as catalog_router
from app.api.draw import router as draw_router
from app.core.config import settings
from app.db.session import Base, SessionLocal, engine
from app.models import User  # noqa: F401  ensure metadata
from app.seed import seed_if_empty

api = APIRouter(prefix="/api/v1")
api.include_router(auth_router)
api.include_router(catalog_router)
api.include_router(draw_router)
api.include_router(cards_router)

@asynccontextmanager
async def lifespan(_app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        seed_if_empty(db)
    finally:
        db.close()
    yield


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)
_origins = settings.cors_origin_list
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=_origins != ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api)


@app.get("/health")
def health():
    return {"ok": True, "name": settings.app_name}
