from asgiref.sync import sync_to_async
from boto3 import resource


@sync_to_async
def upload_object(
    s3_resource: resource, content: str, object_key: str, bucket_name: str
) -> dict:
    response = s3_resource.Object(bucket_name, object_key).put(Body=content)
    return response


@sync_to_async
def get_object(s3_resource: resource, object_key: str, bucket_name: str) -> dict:
    response = s3_resource.get_object(Bucket=bucket_name, Key=object_key)
    return response
