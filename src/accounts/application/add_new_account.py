from src.accounts.domain.account_service import AccountService

class AddNewAccountUseCase:
    def __init__(self, account_service: AccountService ):
        self.account_service = account_service

    async def execute(self, person_id: str, account_name: str):
        return await self.account_service.create(person_id, account_name)