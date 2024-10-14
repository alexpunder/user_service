import asyncio
import logging

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from src.config import settings

loop = asyncio.get_event_loop()

producer = AIOKafkaProducer(
    loop=loop,
    bootstrap_servers=settings.kafka_settings.BOOTSTRAP_SERVERS,
)

consumer = AIOKafkaConsumer(
    settings.kafka_settings.TOPIC_NAME,
    loop=loop,
    bootstrap_servers=settings.kafka_settings.BOOTSTRAP_SERVERS,
)


async def test_kafka_get_messages():
    logging.info('Начало цикла по выводу сообщений из очереди.')

    async for message in consumer:
        logging.info(f'Вывод сообщения полученного от Продюсера: {message=}')
