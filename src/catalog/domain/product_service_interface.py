from abc import abstractmethod, ABC

from src.catalog.infrastructure.product_repository import ProductRepository


class IProductService(ABC):
    @abstractmethod
    def get_rep_name(self):
        pass