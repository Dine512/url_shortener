import string
import random

from config import settings
from dao import UrlDAO
from models import Url


class UrlService:
    def __init__(self, session):
        self.url_dao = UrlDAO(session=session)

    async def create_short_url(self, long_url: str) -> str:
        existing_short_url = await self.url_dao.database_long_url_check(long_url)
        if existing_short_url:
            return settings.SERVICE_URL + existing_short_url.short_url

        while True:
            characters = string.ascii_letters + string.digits
            short_url = ''.join(random.choice(characters) for _ in range(settings.SHORT_URL_LENGTH))
            short_url_in_db = await self.url_dao.database_short_url_check(short_url)
            if not short_url_in_db:
                break

        await self.url_dao.add_url(long_url=long_url, short_url=short_url)
        short_url = settings.SERVICE_URL + short_url
        return short_url

    async def delete_url(self, short_url: str) -> int:
        short_url = short_url.split('/')[-1]
        result = await self.url_dao.delete_url(short_url)
        return result.rowcount

    async def get_long_url(self, short_url: str) -> Url | None:
        short_url = short_url.split('/')[-1]
        url_data = await self.url_dao.database_short_url_check(short_url)
        return url_data









