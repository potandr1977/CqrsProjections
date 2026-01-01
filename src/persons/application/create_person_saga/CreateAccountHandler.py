import uuid
from typing import Dict, Any

from src.persons.domain.models.account import Account
from src.persons.domain.models.person import Person

async def create_account(ctx: Dict, prev_result: Any):
    person:Person = prev_result
    if person is None:
        raise RuntimeError("Не удалось получить person_service")

    account_id = ctx.get("id")
    account_name = ctx.get("name")

    account = Account(id=account_id, name=account_name)
    person.accounts.append(account)

    return person

async def compensate_create_account(ctx: Dict, prev_result: Dict):
    person:Person = ctx.get("person")
    if person is not None:
        person.name = "removed"
