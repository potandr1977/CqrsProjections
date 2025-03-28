from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base

from domain.DepTest import DepTest


#Host=pgserver;Port=5432;Database=airbooking_db;User Id=app;Password=app;Pooling=true;
pg_database='postgresql+asyncpg://app:app@localhost:5432/airbooking_db'

engine = create_async_engine(pg_database, echo=True)
Base = declarative_base()
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

deptest = DepTest(engine)

def get_deptest():
    return deptest

# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

