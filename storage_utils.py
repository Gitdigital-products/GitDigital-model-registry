import boto3
from botocore.exceptions import ClientError
import os

class StorageManager:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION", "us-east-1")
        )
        self.bucket_name = os.getenv("STORAGE_BUCKET")

    def generate_upload_url(self, model_name: str, version: str):
        """Generates a secure URL for the client to upload a model file."""
        object_name = f"models/{model_name}/{version}/model.tar.gz"
        try:
            response = self.s3_client.generate_presigned_post(
                self.bucket_name,
                object_name,
                ExpiresIn=3600  # Link expires in 1 hour
            )
            return response
        except ClientError as e:
            return None

    def generate_download_url(self, s3_path: str):
        """Generates a secure link for a service to download the model."""
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': s3_path},
                ExpiresIn=3600
            )
            return url
        except ClientError as e:
            return None
