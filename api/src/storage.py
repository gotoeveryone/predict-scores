import os

import boto3
from botocore.exceptions import ClientError, EndpointConnectionError, NoCredentialsError


class StorageManager:
    def __init__(self):
        bucket_name = os.environ.get("AWS_S3_BUCKET")
        if not bucket_name:
            raise RuntimeError("AWS_S3_BUCKET is not set.")

        s3 = boto3.resource("s3")
        self.bucket = s3.Bucket(bucket_name)

    def get(self, key) -> bytes:
        try:
            obj = self.bucket.Object(key)
            return obj.get()["Body"].read()
        except (ClientError, EndpointConnectionError, NoCredentialsError) as exc:
            raise RuntimeError(f"Failed to get s3://{self.bucket.name}/{key}") from exc
