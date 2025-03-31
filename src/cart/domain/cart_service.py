from src.cart.domain.cart_service_interface import ICartService
from src.cart.infrastructure.cart_repository import CartRepository


class CartService(ICartService):
    def __init__(self, product_repository:CartRepository):
        self.product_repository = product_repository

    def get_rep_name(self):
        return self.product_repository.get_name()