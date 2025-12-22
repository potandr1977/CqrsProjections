import asyncio
from aiokafka import AIOKafkaConsumer

class KafkaConsumerContext:
    def __init__(self, servers: str, topic: str, group_id: str):
        self.servers = servers
        self.topic = topic
        self.group_id = group_id
        self.consumer: AIOKafkaConsumer | None = None

    async def __aenter__(self):
        self.consumer = AIOKafkaConsumer(
            self.topic,
            bootstrap_servers=self.servers,
            group_id=self.group_id,
            auto_offset_reset="earliest" # читаем с начала, можно "latest"
        )
        await self.consumer.start()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self.consumer:
            await self.consumer.stop()

    async def listen(self):
        """Асинхронный итератор для получения сообщений"""
        async for msg in self.consumer:
            yield msg.value.decode("utf-8")

'''
async def main():
    async with KafkaConsumerContext("localhost:9092", "accounts", "account_group") as kafka: 
        async for message in kafka.listen(): 
            print(f"Получено: {message}") 
            # можно добавить обработку, например запись в БД
'''