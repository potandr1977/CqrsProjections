from sqlalchemy.ext.asyncio import AsyncEngine

from src.catalog.domain.product_repository_repository import IProductRepository


class ProductRepository(IProductRepository):
    def __init__(self): #, engine: AsyncEngine):
        self.name = "ProductRepName"

    def get_name(self):
        return self.name