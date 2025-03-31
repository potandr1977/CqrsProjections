from abc import abstractmethod, ABC

from sqlalchemy.ext.asyncio import AsyncEngine


class ICartRepository(ABC):
    @abstractmethod
    def get_name(self):
        pass