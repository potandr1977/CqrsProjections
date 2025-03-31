from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from src.cart.domain.cart_repository_interface import ICartRepository
from src.cart.domain.cart_service import CartService
from src.cart.domain.cart_service_interface import ICartService
from src.cart.infrastructure.cart_repository import CartRepository
from src.catalog.domain.product_service import ProductService
from src.catalog.infrastructure.product_repository import ProductRepository

pg_database='postgresql+asyncpg://app:app@localhost:5432/airbooking_db'

class CatalogContainer(containers.DeclarativeContainer):
    #engine = create_async_engine(pg_database, echo=True)
    repository:ICartRepository = providers.Factory(CartRepository)
    service:ICartService = providers.Factory(CartService, repository = repository)
    wiring_config = containers.WiringConfiguration(modules=["cart.cart_endpoints"])