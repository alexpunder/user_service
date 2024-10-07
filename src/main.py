from fastapi import FastAPI

from src.config import settings
from src.users import users_router

app = FastAPI(
    debug=settings.app_settings.DEBUG,
    title=settings.app_settings.TITLE,
    summary=settings.app_settings.SUMMARY,
    description=settings.app_settings.DESCRIPTION,
    version=settings.app_settings.VERSION,
    docs_url=settings.app_settings.DOCS_URL,
    redoc_url=settings.app_settings.REDOC_URL,
    default_response_class=settings.app_settings.DEFAULT_RESPONSE_CLASS,
    middleware=settings.app_settings.MIDDLEWARE,
    terms_of_service=settings.app_settings.TERMS_OF_SERVICE,
    contact=settings.app_settings.CONTACT,
    license_info=settings.app_settings.LICENSE_INFO,
)

app.include_router(
    router=users_router,
)
