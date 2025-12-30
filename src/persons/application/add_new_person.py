from src.persons.domain.person_service import PersonService


class AddNewPersonUseCase:
    def __init__(self, person_service: PersonService ):
        self.person_service = person_service

    async def execute(self, person_name: str, person_inn:str):
        return await self.person_service.create(person_name, person_inn)