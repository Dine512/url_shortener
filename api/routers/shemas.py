from pydantic import BaseModel


class ShortUrl(BaseModel):
    short_url: str


class LongUrl(BaseModel):
    long_url: str


class DeleteUrlResponse(BaseModel):
    message: str
