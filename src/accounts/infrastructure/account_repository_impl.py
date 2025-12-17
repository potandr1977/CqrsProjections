import uuid

from motor.metaprogramming import Async
from pymongo import AsyncMongoClient

from src.accounts.domain.interfaces.account_repository import IAccountRepository
from src.accounts.domain.models.account import Account
from src.accounts.domain.models.payment import Payment


class AccountRepository(IAccountRepository):
    def __init__(self, client:AsyncMongoClient, db_name: str):
        self.db = client[db_name]
        self.collection= self.db["accounts"]

    async def create(self, account: Account)->None:
        doc = {
            "id": account.id,
            "name": account.name,
            "person": { "name": account.person.name},
            "payments": [{"id": pay.id, "purpose":pay.purpose, "sum": str(pay.sum)} for pay in account.payments]
        }
        await self.collection.insert_one(doc)

    async def update(self, account: Account)->None:
        await self.collection.update_one(
            {"$id":account.id},
            {
                "$set:": {
                    "name": account.name,
                    "payments": [pay.__dict__ for pay in account.payments]
                }
            })
