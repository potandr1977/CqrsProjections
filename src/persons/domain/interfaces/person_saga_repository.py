from abc import abstractmethod, ABC

from src.accounts.domain.models.account import Account
from src.persons.domain.models.person import Person


class IPersonSagaRepository(ABC):
    @abstractmethod
    async def get_by_id(self, person_id: str)->Person | None:...
    # @abstractmethod
    # async def get_all(self)->list[Account]:...
    @abstractmethod
    async def create(self, person: Person)->Person:...
    @abstractmethod
    async def update(self, person: Person)->None:...
    # @abstractmethod
    # async def delete(self, account_id: str)->None:...