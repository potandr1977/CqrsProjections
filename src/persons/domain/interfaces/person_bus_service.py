from abc import abstractmethod, ABC

from src.events import PersonCreated



class IPersonBusService(ABC):
    @abstractmethod
    async def public_person_created(self, person_created: PersonCreated):...
