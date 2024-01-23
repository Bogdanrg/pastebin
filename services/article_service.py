from boto3 import resource
from services import sharer_pb2, sharer_pb2_grpc
from config.app_config import settings
import grpc


class ArticleService:

    @staticmethod
    async def upload_article(s3_resource: resource,
                             content: str,
                             expiration: int = 86400,
                             secret: str | None = None) -> None:
        object_key = await ArticleService.get_unique_key(secret)
        s3_object = s3_resource.Object(settings.app.BUCKET_NAME, object_key).put(Body=content)

    @staticmethod
    async def get_unique_key(secret: str | None = None) -> str:
        async with grpc.aio.insecure_channel(settings.hash_service.SERVICE_URL) as channel:
            stub = sharer_pb2_grpc.HasherStub(channel)
            if secret is not None:
                response = await stub.GetUniqueKey(sharer_pb2.GetKeyRequest(secret=secret))
            else:
                response = await stub.GetUniqueKey(sharer_pb2.GetKeyRequest())
        return response.message.key
