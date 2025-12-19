import uuid

from src.persons.domain.models.person import Person
from src.events.PersonCreated import PersonCreated
from src.persons.domain.interfaces.person_bus_service import IPersonBusService
from src.persons.domain.interfaces.person_repository import IPersonRepository


class PersonService:
    def __init__(self, person_repository:IPersonRepository, bus_service:IPersonBusService):
        self.person_repository = person_repository
        self.bus_service = bus_service

    async def create(self, person_name: str, person_inn:str):
        person_id = f"Person-{str(uuid.uuid4())}"
        person = Person(id=person_id, name=person_name, inn=person_inn)
        person_created = PersonCreated(person_id, person_name, person_inn)
        await self.bus_service.public_person_created(person_created)
        await self.person_repository.create(person)
        return person

    async def get_by_id(self, person_id: str)->Person:
        return await self.person_repository.get_by_id(person_id)