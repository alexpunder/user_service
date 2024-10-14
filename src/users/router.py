import json
import logging

from fastapi import APIRouter

from src.config import settings
from src.users.schemas import BaseUser
from src.users.service import producer

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/', response_model=BaseUser)
async def test_kafka_send_topik(
    user_data: BaseUser,
):
    some_data = json.dumps(user_data.model_dump()).encode(encoding='utf-8')

    try:
        logging.info(f'Sending data to Kafka: {some_data=}')
        await producer.send_and_wait(
            topic=settings.kafka_settings.TOPIC_NAME, value=some_data
        )
        logging.info('Message send to Kafka')
    except Exception as error:
        logging.exception(f'Error sending message to Kafka: {error}')

    return user_data
