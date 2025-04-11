from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from src.carts.domain.cart_repository_interface import ICartRepository
from src.carts.domain.cart_service import CartService
from src.carts.domain.cart_service_interface import ICartService
from src.carts.infrastructure.cart_repository import CartRepository
from src.products.domain.product_service import ProductService
from src.products.infrastructure.product_repository import ProductRepository

pg_database='postgresql+asyncpg://app:app@localhost:5432/airbooking_db'

class CartContainer(containers.DeclarativeContainer):
    #engine = create_async_engine(pg_database, echo=True)
    repository:ICartRepository = providers.Factory(CartRepository)
    service:ICartService = providers.Factory(CartService, cart_repository = repository)
    wiring_config = containers.WiringConfiguration(modules=["carts.cart_endpoints"])