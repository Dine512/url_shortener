from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASS: str
    PG_NAME: str

    SHORT_URL_LENGTH: int = 4

    SERVICE_URL: str = 'const.com/'

    TITLE: str = 'Сервис генерации короткой ссылки'

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}'

    class Config:
        env_file = ".env"


settings = Settings()
