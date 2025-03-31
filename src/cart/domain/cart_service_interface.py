from abc import abstractmethod, ABC

from src.cart.infrastructure.cart_repository import CartRepository


class ICartService(ABC):
    @abstractmethod
    def get_rep_name(self):
        pass