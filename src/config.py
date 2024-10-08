from typing import Sequence, Type

from fastapi.middleware import Middleware
from fastapi.responses import ORJSONResponse, Response
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.middleware import middleware


class ExtendBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )


class AppSettings(ExtendBaseSettings):
    model_config = SettingsConfigDict(env_prefix='APP_')

    DEBUG: bool = True
    LOG_LEVEL: str = 'INFO'
    TITLE: str = 'User service'
    SUMMARY: str = ''
    DESCRIPTION: str | None = 'Microservice'
    VERSION: str = '0.0.1'
    DOCS_URL: str = '/'
    REDOC_URL: str = '/redoc'
    DEFAULT_RESPONSE_CLASS: Type[Response] = ORJSONResponse
    MIDDLEWARE: Sequence[Middleware] = middleware
    TERMS_OF_SERVICE: str | None = None
    CONTACT: dict = {}
    LICENSE_INFO: dict = {}


class DBSettings(ExtendBaseSettings):
    model_config = SettingsConfigDict(env_prefix='DB_')

    DSN: str = 'sqlite+aiosqlite:///./user.db'


class KafkaSettings(ExtendBaseSettings):
    BOOTSTRAP_SERVERS: str = 'localhost:9092'
    TOPIC_NAME: str = 'user_data'


class Settings(ExtendBaseSettings):
    app_settings: AppSettings = AppSettings()
    db_settings: DBSettings = DBSettings()
    kafka_settings: KafkaSettings = KafkaSettings()


settings = Settings()
