from sqlalchemy.ext.asyncio import AsyncEngine

from src.carts.domain.cart_repository_interface import ICartRepository
from src.carts.domain.cart_service_interface import ICartService


class CartRepository(ICartRepository):
    def __init__(self): #, engine: AsyncEngine):
        self.name = "CartRepName"

    def get_name(self):
        return self.name