import json
from dataclasses import asdict

from src.common_infrastructure.kafka_producer_context import KafkaProducerContext
from src.events import PersonCreated
from src.persons.domain.interfaces.person_bus_service import IPersonBusService


class PersonBusService(IPersonBusService):
    def __init__(self, kafka_producer_context:KafkaProducerContext):
        self.kafka_producer = kafka_producer_context

    async def public_person_created(self, person_created: PersonCreated):
        json_str = json.dumps(asdict(person_created), ensure_ascii=False)
        async with self.kafka_producer as producer:
            await producer.send(json_str)