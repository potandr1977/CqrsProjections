import uvicorn

from src.accounts.container import AccountContainer
from src.persons.container import PersonContainer

from src.accounts.router import account_router
from src.persons.router import person_router

import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI


import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(application: FastAPI):
    account_container = AccountContainer()
    person_container = PersonContainer()

    application.account_container = account_container
    application.person_container = person_container

    await init_databases(application.account_container)

    # создаём и запускаем несколько воркеров
    workers = [
        account_container.kafka_worker()
    ]

    tasks = [asyncio.create_task(worker.run()) for worker in workers]
    print("Все воркеры запущены")

    try:
        yield
    finally:
        # мягкая остановка воркеров
        for worker in workers:
            if hasattr(worker, "stop") and callable(worker.stop):
                await worker.stop()
        # отмена задач (на случай если stop не реализован)
        for task in tasks:
            task.cancel()
        print("Все воркеры остановлены")

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
    application = FastAPI(lifespan=lifespan)

    application.include_router(account_router)
    application.include_router(person_router)
    # app.include_router(reports_router)

    return application

app = create_app()

if __name__ == "__main__":
    _port = 3003
    print(f"http://127.0.0.1:{_port}/docs")
    uvicorn.run(app, port = _port)