from src.carts.domain.cart_repository_interface import ICartRepository
from src.carts.domain.cart_service_interface import ICartService


class CartService(ICartService):
    def __init__(self, cart_repository:ICartRepository):
        self.cart_repository = cart_repository

    def get_rep_name(self):
        return self.cart_repository.get_name()