from dependency_injector import containers, providers
from motor.motor_asyncio import AsyncIOMotorClient

from src.accounts.domain.account_service import AccountService
from src.accounts.infrastructure.account_repository_impl import AccountRepository
from src.common_infrastructure.kafka_producer_context import KafkaProducerContext
from src.persons.application.add_new_person import AddNewPersonUseCase
from src.persons.domain.interfaces.person_bus_service import IPersonBusService
from src.persons.domain.interfaces.person_repository import IPersonRepository
from src.persons.domain.person_service import PersonService
from src.persons.infrastructure.person_bus_service_impl import PersonBusService
from src.persons.infrastructure.person_repository_impl import PersonRepository

pg_database='postgresql+asyncpg://app:app@localhost:5432/airbooking_db'

class PersonContainer(containers.DeclarativeContainer):
    kafka_producer_context =  providers.Factory(KafkaProducerContext, bootstrap_servers="localhost:9092", topic = "persons")
    person_bus_service:IPersonBusService = providers.Factory(PersonBusService, kafka_producer_context = kafka_producer_context)
    # Mongo-клиент как Singleton
    mongo_client = providers.Singleton(AsyncIOMotorClient,"mongodb://localhost:27047")
    # client и db_name - параметры конструктора PersonRepository
    person_repository:IPersonRepository = providers.Singleton(PersonRepository, client = mongo_client, db_name = "person_db")
    person_service:PersonService = providers.Factory(PersonService, person_repository = person_repository, bus_service = person_bus_service)
    add_new_person_use_case = providers.Factory(AddNewPersonUseCase, person_service = person_service)
    wiring_config = containers.WiringConfiguration(modules=["src.persons.router"])