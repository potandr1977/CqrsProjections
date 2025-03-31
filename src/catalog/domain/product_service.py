from src.catalog.domain.product_repository_repository import IProductRepository
from src.catalog.infrastructure.product_repository import ProductRepository


class ProductService:
    def __init__(self, product_repository:IProductRepository):
        self.product_repository = product_repository

    def get_rep_name(self):
        return self.product_repository.get_name()