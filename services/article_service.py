import grpc
from boto3 import resource
from starlette import status

import exceptions
from config.app_config import settings
from core.s3.mapper import upload_object
from services import sharer_pb2, sharer_pb2_grpc


class ArticleService:
    @staticmethod
    async def upload_article(
        s3_resource: resource,
        content: str,
        expiration: int = 86400,
        secret: str | None = None,
    ) -> str:
        object_key: str = await ArticleService.get_unique_key(secret)
        response: dict = await upload_object(
            s3_resource, content, object_key, settings.localstack.BUCKET_NAME
        )
        response_metadata: dict = response.get("ResponseMetadata")
        if response_metadata.get("HTTPStatusCode") != 200:
            raise exceptions.ContentUploadingException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot upload a text block.",
            )
        return object_key

    @staticmethod
    async def get_unique_key(secret: str | None = None) -> str:
        async with grpc.aio.insecure_channel(
            settings.hash_service.SERVICE_URL
        ) as channel:
            stub = sharer_pb2_grpc.HasherStub(channel)
            if secret is not None:
                response = await stub.GetUniqueKey(
                    sharer_pb2.GetKeyRequest(secret=secret)
                )
            else:
                response = await stub.GetUniqueKey(sharer_pb2.GetKeyRequest())
        return response.message.key
