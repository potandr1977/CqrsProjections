from dependency_injector import containers, providers
from motor.motor_asyncio import AsyncIOMotorClient

from src.accounts.application.add_new_account import AddNewAccountUseCase
from src.accounts.application.person_created_handler import PersonHandler
from src.accounts.application.worker import KafkaWorker
from src.accounts.domain.account_service import AccountService

from src.accounts.domain.interfaces.account_repository import IAccountRepository
from src.accounts.infrastructure.account_repository_impl import AccountRepository
from src.common_infrastructure.kafka_consumer_context import KafkaConsumerContext

pg_database='postgresql+asyncpg://app:app@localhost:5432/airbooking_db'



class AccountContainer(containers.DeclarativeContainer):
    kafka_consumer_context = providers.Factory(KafkaConsumerContext, servers="localhost:9092", topic="persons", group_id="person_group")
    person_handler = providers.Factory(PersonHandler)
    kafka_worker = providers.Factory(KafkaWorker,kafka_consumer_context=kafka_consumer_context, handler=person_handler)
    # Mongo-клиент как Singleton
    mongo_client = providers.Singleton(
        AsyncIOMotorClient,
        "mongodb://localhost:27047"
    )
    # client и db_name - параметры конструктора AccountRepository
    account_repository:IAccountRepository = providers.Singleton(AccountRepository, client=mongo_client, db_name="account_db")
    account_service:AccountService = providers.Factory(AccountService, account_repository = account_repository)
    add_new_account_use_case = providers.Factory(AddNewAccountUseCase, account_service = account_service)
    wiring_config = containers.WiringConfiguration(modules=["src.accounts.router"])