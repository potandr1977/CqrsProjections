from abc import abstractmethod, ABC


class IProductRepository(ABC):
    @abstractmethod
    def get_name(self):
        pass