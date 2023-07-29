from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import settings

engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()
