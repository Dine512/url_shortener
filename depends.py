from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import async_session_maker
from services import UrlService


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


async def get_url_service(
        session: AsyncSession = Depends(get_session)
) -> UrlService:
    return UrlService(session=session)
