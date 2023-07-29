from fastapi import APIRouter, Depends, HTTPException

from api.routers.shemas import LongUrl, ShortUrl, DeleteUrlResponse
from api.depends import get_url_service
from src.services.services import UrlService

router = APIRouter(prefix='/url_shortener')


@router.post('/generate_short_url')
async def url_generator(
        long_url: LongUrl,
        url_service: UrlService = Depends(get_url_service)
) -> ShortUrl:
    short_url = await url_service.create_short_url(long_url.long_url)
    return ShortUrl(short_url=short_url)


@router.delete('/delete')
async def delete_url(
        short_url: ShortUrl,
        url_service: UrlService = Depends(get_url_service)
) -> DeleteUrlResponse:
    deleted_count = await url_service.delete_url(short_url.short_url)

    if deleted_count == 0:
        raise HTTPException(status_code=404, detail='Url not found')

    return DeleteUrlResponse(message='URL Removed')


@router.post('/get_long_url')
async def get_long_url(
        short_url: ShortUrl,
        url_service: UrlService = Depends(get_url_service)
) -> LongUrl:
    url_data = await url_service.get_long_url(short_url.short_url)

    if not url_data:
        raise HTTPException(status_code=404, detail='Url not found')

    return LongUrl(long_url=url_data.long_url)
