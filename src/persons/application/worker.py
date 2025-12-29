import asyncio

class KafkaWorker:
    def __init__(self, kafka_consumer_context, handler):
        self.kafka_consumer_context = kafka_consumer_context
        self.handler = handler

    async def run(self):
        async with self.kafka_consumer_context as consumer:
            async for message in consumer.listen():
                await self.handler.handle(message)
