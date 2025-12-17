from fastapi import APIRouter

from src.accounts.container import AccountContainer

account_router = APIRouter(prefix="/account", tags=["account"])
account_container = AccountContainer()

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

@account_router.get("")
async def ping():
    return "pong"


@account_router.post(
    "",
    responses={400: {"description": "Bad request"}},
    description="Создать счёт")
async def add_new_account(person_id: str, account_name):
    use_case = account_container.add_new_account_use_case()
    account = await use_case.execute(person_id, account_name)
    return account

