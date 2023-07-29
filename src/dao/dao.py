from sqlalchemy import select, insert, delete, CursorResult
from sqlalchemy.ext.asyncio import AsyncSession

from api.routers.models import Url as UrlModel


class UrlDAO:
    model = UrlModel

    def __init__(self, session: AsyncSession):
        self.session = session

    async def database_long_url_check(self, long_url: str) -> UrlModel | None:
        existing_short_url = select(self.model).where(self.model.long_url == long_url)
        url = await self.session.execute(existing_short_url)
        url = url.scalar()
        return url

    async def database_short_url_check(self, short_url: str) -> UrlModel | None:
        existing_short_url = select(self.model).where(self.model.short_url == short_url)
        url = await self.session.execute(existing_short_url)
        url = url.scalar()
        return url

    async def add_url(self, long_url: str, short_url: str) -> None:
        add_url = insert(self.model).values(short_url=short_url, long_url=long_url)
        await self.session.execute(add_url)
        await self.session.commit()

    async def delete_url(self, short_url: str) -> CursorResult:
        delete_url = delete(self.model).where(self.model.short_url == short_url)
        delete_url = await self.session.execute(delete_url)
        await self.session.commit()
        return delete_url
