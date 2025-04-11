from sqlalchemy.ext.asyncio import AsyncEngine

from src.products.domain.product import Product
from src.products.domain.product_repository_interface import IProductRepository


class ProductRepository(IProductRepository):
    def __init__(self): #, engine: AsyncEngine):
        self.name = "ProductRepName"

    def get_name(self):
        return self.name

    def get_one(self, sku:str)->Product:
        ...

    def get_page(self, page_num: int, page_size: int) -> tuple[Product]:
        ...

    def create_or_update(self, product:Product)->Product:
        ...