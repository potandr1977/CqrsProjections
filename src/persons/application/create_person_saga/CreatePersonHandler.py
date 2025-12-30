from typing import Dict, Any

from src.persons.domain.models.person import Person
from src.persons.domain.person_service import PersonService

async def create_person(ctx: Dict, prev_result: Any):
    person_service:PersonService = ctx.get("person_service")
    if person_service is None:
        raise RuntimeError("Не удалось получить person_service")

    person_name = ctx.get("person_name")
    person_inn = ctx.get("person_inn")
    person = await person_service.create(person_name, person_inn)

    return person


async def compensate_create_person(ctx: Dict, prev_result: Dict):
    person:Person = ctx.get("person")
    if person is not None:
        person.name = "removed"