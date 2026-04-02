import uuid

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, HTTPException, Depends

from src.persons.application.add_new_person import AddNewPersonUseCase
from src.persons.application.create_person_saga.CreatePersonSaga import CreatePersonSaga
from src.persons.domain.person_service import PersonService
from src.persons.person_container import PersonContainer

person_router = APIRouter(prefix="/person", tags=["person"])

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
@inject
async def get_by_id(
        person_id:str,
        person_service: PersonService = Depends(Provide[PersonContainer.person_service])
):
    person = await person_service.get_by_id(person_id)
    if person is None:
        raise HTTPException(status_code=404,detail="Person not found")
    return person

@person_router.post(
    "",
    responses={400: {"description": "Bad request"}},
    description="Создать персону")
async def add_new_person(
        person_name:str,
        person_inn:str,
        use_case: AddNewPersonUseCase = Depends(Provide[PersonContainer.add_new_person_use_case])
):
    person = await use_case.execute(person_name, person_inn)
    return person

@person_router.post(
    "saga",
    #responses={400: {"description": "Bad request"}},
    description="Создать персону")
@inject
async def create_person_saga(
        person_name:str = "Jim Saga",
        person_inn:str = "789",
        person_service: PersonService = Depends(Provide[PersonContainer.person_service])
):
    try:
        ctx_step1 = {
            "person_service": person_service,
            "person_name": person_name,
            "person_inn": person_inn
        }
        saga_id = f"CreatePersonSaga-{str(uuid.uuid4())}"
        saga = CreatePersonSaga(id = saga_id)
        step1_result = await saga.execute_next_step(ctx_step1)
        person = step1_result.result

        account_id = f"Account-{str(uuid.uuid4())}"
        ctx_step2 = {
            "id" : account_id,
            "name" : "account1"
        }
        ste2_result = await saga.execute_next_step(ctx_step2)

        return person
    except Exception as e:
        return e



