import os

import boto3


class StorageManager:
    def __init__(self):
        s3 = boto3.resource("s3")
        self.bucket = s3.Bucket(os.environ.get("AWS_S3_BUCKET"))

    def get(self, key) -> bytes:
        obj = self.bucket.Object(key)

        return obj.get()["Body"].read()
