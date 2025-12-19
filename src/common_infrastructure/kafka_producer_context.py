import json
from dataclasses import is_dataclass, asdict

from aiokafka import AIOKafkaProducer

class KafkaProducerContext:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer: AIOKafkaProducer | None = None

    async def __aenter__(self):
        # создаём и запускаем продюсер
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: v.encode("utf-8"),
        )
        await self.producer.start()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        # корректно закрываем соединение
        if self.producer:
            await self.producer.stop()

    async def send(self, message):
        # если dataclass — преобразуем в dict
        if is_dataclass(message):
            message = asdict(message)
        # если dict — сериализуем в JSON
        if isinstance(message, dict):
            message = json.dumps(message, ensure_ascii=False)
        await self.producer.send_and_wait(self.topic, message)

    '''
    Использование
    
    async def main(): 
        async with KafkaProducerContext("localhost:9092", "accounts") as kafka: 
            await kafka.send("hello world")
             
    asyncio.run(main())
    '''