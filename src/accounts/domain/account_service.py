import uuid

from src.accounts.domain.models.account import Account
from src.accounts.domain.models.person import Person
from src.accounts.infrastructure.account_repository_impl import AccountRepository


class AccountService:
    def __init__(self, account_repository:AccountRepository):
        self.account_repository = account_repository

    async def create(self, person_id: str, account_name: str):
        account_id = f"Account-{str(uuid.uuid4())}"
        person = Person(id=person_id, name="John Doe")
        account = Account(account_id, account_name, person)
        await self.account_repository.create(account)
        return account

    async def get_by_id(self, account_id: str)->Account:
        return await self.account_repository.get_by_id(account_id)