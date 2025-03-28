from src.catalog.infrastructure.product_repository import ProductRepository


class ProductService:
    def __init__(self, product_repository:ProductRepository):
        self.product_repository = product_repository

    def get_rep_name(self):
        return self.product_repository.get_name()