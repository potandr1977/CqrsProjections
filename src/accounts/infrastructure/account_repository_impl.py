import uuid

from motor.metaprogramming import Async
from pymongo import AsyncMongoClient

from src.accounts.domain.interfaces.account_repository import IAccountRepository
from src.accounts.domain.models.account import Account
from src.accounts.domain.models.payment import Payment
from src.accounts.domain.models.person import Person


class AccountRepository(IAccountRepository):
    def __init__(self, client:AsyncMongoClient, db_name: str):
        self.db = client[db_name]
        self.collection= self.db["accounts"]

    async def get_by_id(self, account_id: str) ->Account:
        doc = await self.collection.find_one({"id": account_id})
        if not doc:
            return None

        person_doc = doc.get("person")
        person = Person(
            id=str(person_doc["id"]),
            name=person_doc["name"])
        # Преобразуем список платежей
        payments = []
        for p in doc.get("payments", []):
            payments.append(Payment(
                id=str(p["_id"]),
                sum=p["sum"]))
        # Собираем Account
        return Account(
            id=str(doc["id"]),
            name=doc["name"],
            person=person,
            payments=payments )

    async def create(self, account: Account)->None:
        doc = {
            "id": account.id,
            "name": account.name,
            "person": {"id": account.person.id, "name": account.person.name},
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
