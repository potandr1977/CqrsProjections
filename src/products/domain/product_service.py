from src.products.domain.product import Product
from src.products.domain.product_repository_interface import IProductRepository


class ProductService:
    def __init__(self, product_repository:IProductRepository):
        self.product_repository = product_repository

    def get_rep_name(self):
        return self.product_repository.get_name()

    def get_one(self, sku: str) -> Product:
        return self.product_repository.get_one(sku)

    def get_page(self, page_num: int, page_size: int) -> tuple[Product]:
        return self.product_repository.get_page(page_num, page_size)

    def create(self, name:str, description:str)->Product:
        product = Product.create(name,description)
        self.product_repository.create_or_update(product)
        return product

    def update(self, product: Product) -> Product:
        return self.product_repository.create_or_update(product)