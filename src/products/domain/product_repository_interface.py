from abc import abstractmethod, ABC

from src.products.domain.product import Product


class IProductRepository(ABC):
    @abstractmethod
    def get_name(self):
        ...

    @abstractmethod
    def get_one(self, sku:str)->Product:
        ...

    @abstractmethod
    def get_page(self, page_num:int, page_size:int)->tuple[Product]:
        ...

    @abstractmethod
    def create_or_update(self, product:Product)->Product:
        ...