import boto3

from config.app_config import settings


def get_s3_resource() -> boto3.resource:
    s3 = boto3.resource(
        "s3",
        endpoint_url=settings.localstack.ENDPOINT_URL,
        aws_access_key_id="asdf",
        aws_secret_access_key="asdf",
    )
    yield s3
