from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from src.catalog.domain.product_service import ProductService
from src.catalog.infrastructure.product_repository import ProductRepository

pg_database='postgresql+asyncpg://app:app@localhost:5432/airbooking_db'

class CatalogContainer(containers.DeclarativeContainer):
    #engine = create_async_engine(pg_database, echo=True)
    repository = providers.Factory(ProductRepository)
    service = providers.Factory(ProductService, repository = repository)
    wiring_config = containers.WiringConfiguration(modules=["catalog.catalog_endpoints"])