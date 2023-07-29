from fastapi import APIRouter, Depends, HTTPException
from pydantic import HttpUrl
from starlette.responses import JSONResponse

from depends import get_url_service
from services import UrlService

router = APIRouter(prefix='/url_shortener')


@router.post('/generate_short_url')
async def url_generator(
        long_url: HttpUrl,
        url_service: UrlService = Depends(get_url_service)
) -> JSONResponse:
    short_url = await url_service.create_short_url(str(long_url))
    return JSONResponse(status_code=200, content={'short_url': short_url})


@router.delete('/delete')
async def delete_url(
        short_url: str,
        url_service: UrlService = Depends(get_url_service)
) -> JSONResponse:
    deleted_count = await url_service.delete_url(short_url)

    if deleted_count == 0:
        raise HTTPException(status_code=404, detail='Url not found')

    return JSONResponse(status_code=200, content={'message': 'Url removed'})


@router.post('/get_long_url')
async def get_long_url(
        short_url: str,
        url_service: UrlService = Depends(get_url_service)
) -> JSONResponse:
    url_data = await url_service.get_long_url(short_url)

    if not url_data:
        raise HTTPException(status_code=404, detail='Url not found')

    return JSONResponse(status_code=200, content={'long_url': url_data.long_url})
