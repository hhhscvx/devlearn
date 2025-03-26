from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from src.infrastructure.config import settings


engine = create_async_engine(
    url=settings.db_url,
    future=True,
    echo=settings.DB_ECHO,
    pool_pre_ping=True,
)

AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)


async def get_db_session():
    async with AsyncSessionFactory() as session:
        yield session
