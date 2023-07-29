from fastapi import FastAPI

from config import settings
from database import Base, engine
from router import router as url_router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE
    )

    @app.on_event("startup")
    async def startup():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    app.include_router(url_router)

    return app



