from pymongo import AsyncMongoClient

from src.accounts.domain.models.person import Person
from src.persons.domain.interfaces.person_repository import IPersonRepository


class PersonRepository(IPersonRepository):
    def __init__(self, client:AsyncMongoClient, db_name: str):
        self.db = client[db_name]
        self.collection= self.db["persons"]

    async def get_by_id(self, person_id: str) -> Person | None:
        doc = await self.collection.find_one({"id": person_id})
        if not doc:
            return None

        person_doc = doc.get("person")
        person = Person(
            id=str(person_doc["id"]),
            name=person_doc["name"])
        return person

    async def create(self, person: Person)->None:
        doc = {
            "id": person.id,
            "name": person.name
        }
        await self.collection.insert_one(doc)

    async def update(self, person: Person)->None:
        await self.collection.update_one(
            {"$id":person.id},
            {
                "$set:": {
                    "name": person.name
                }
            })
