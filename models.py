from sqlalchemy import Column, String, Integer

from database import Base


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    short_url = Column(String, unique=True, nullable=False)
    long_url = Column(String, nullable=False)
