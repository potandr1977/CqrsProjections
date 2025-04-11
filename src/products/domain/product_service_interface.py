from abc import abstractmethod, ABC
from datetime import datetime

from src.products.domain.product import Product


class IProductService(ABC):
    @abstractmethod
    def get_rep_name(self):
        ...

    def create_product(self, name: str, description: str, edit_date: datetime) -> Product:
        ...