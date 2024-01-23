import boto3


def get_s3_resource() -> boto3.resource:
    s3 = boto3.resource("s3")
    yield s3