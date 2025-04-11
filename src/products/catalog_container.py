from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from src.products.domain.product_repository_interface import IProductRepository
from src.products.domain.product_service import ProductService
from src.products.domain.product_service_interface import IProductService
from src.products.infrastructure.product_repository import ProductRepository

pg_database='postgresql+asyncpg://app:app@localhost:5432/airbooking_db'

class CatalogContainer(containers.DeclarativeContainer):
    #engine = create_async_engine(pg_database, echo=True)
    repository:IProductRepository = providers.Factory(ProductRepository)
    service:IProductService = providers.Factory(ProductService, product_repository = repository)
    wiring_config = containers.WiringConfiguration(modules=["products.catalog_endpoints"])