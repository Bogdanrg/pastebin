from fastapi import FastAPI
from config.app_config import settings
from core.application import factory
from api.v1.sharer.sharer_routes import sharer_router


app: FastAPI = factory.create(
    title=settings.app.TITLE,
    rest_routers=[sharer_router],
    startup_tasks=[],
    shutdown_tasks=[],
)
