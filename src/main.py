import asyncio

import uvicorn
from fastapi import FastAPI

from src.accounts.router import account_router
from src.accounts.container import AccountContainer

async def ensure_database_exists(container:AccountContainer, db_name: str, collection_name: str):
    client = container.mongo_client()
    existing_dbs = await client.list_database_names()
    if not db_name in existing_dbs:
        print(f"База данных '{db_name}' не найдена, создаём...")
        db = client[db_name]
        await db.create_collection(collection_name)
        await db[collection_name].insert_one({"init": True})
        print(f"База данных '{db_name}' создана")

async def init_databases(container: AccountContainer):
    await ensure_database_exists(container, "person_db", "persons")
    await ensure_database_exists(container, "account_db", "accounts")
    await ensure_database_exists(container, "payment_db", "payments")

def create_app() -> FastAPI:
    account_container = AccountContainer()

    application = FastAPI()
    application.account_container = account_container

    application.include_router(account_router)
    #app.include_router(payment_router)
    #app.include_router(reports_router)

    asyncio.run(init_databases(account_container))

    return application

app = create_app()

if __name__ == "__main__":
    _port = 3003
    print(f"http://127.0.0.1:{_port}/docs")
    uvicorn.run(app, port = _port)