from fastapi import FastAPI
from config.app_config import settings
from core.application import factory
from api.v1.sharer.sharer_routes import sharer_router
from boto3 import client


async def create_s3_bucket() -> None:
    s3 = client("s3", endpoint_url=settings.localstack.ENDPOINT_URL,
                aws_access_key_id="asdf",
                aws_secret_access_key="asdf")
    s3.create_bucket(Bucket=settings.localstack.BUCKET_NAME)


app: FastAPI = factory.create(
    title=settings.app.TITLE,
    rest_routers=[sharer_router],
    startup_tasks=[create_s3_bucket],
    shutdown_tasks=[],
)
