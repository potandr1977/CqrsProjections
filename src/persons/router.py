from fastapi import APIRouter, HTTPException

from src.accounts.container import AccountContainer
from src.persons.container import PersonContainer

person_router = APIRouter(prefix="/person", tags=["person"])
person_container = PersonContainer()

'''
творим произвол с данными на потребу своей чёрной души.
@router.on_event("startup")
async def startup_event():
    person_service = AccountContainer.

    alice = Person(id="p1", name="Alice", accounts=[Account(id="a1", person_id="p1", name="Alice Account")])
    bob = Person(id="p2", name="Bob", accounts=[Account(id="a2", person_id="p2", name="Bob Account")])

    await person_service.create_person(alice)
    await person_service.create_person(bob)
'''

@person_router.get("ping")
async def ping():
    return "person-pong"

@person_router.get(
    "",
    responses={400: {"description": "Bad request"}},
    description="Получить персону")
async def get_by_id(person_id:str):
    person_service = person_container.person_service()
    person = await person_service.get_by_id(person_id)
    if person is None:
        raise HTTPException(status_code=404,detail="Person not found")
    return person

@person_router.post(
    "",
    responses={400: {"description": "Bad request"}},
    description="Создать персону")
async def add_new_person(person_name:str, person_inn:str):
    use_case = person_container.add_new_person_use_case()
    person = await use_case.execute(person_name, person_inn)
    return person



