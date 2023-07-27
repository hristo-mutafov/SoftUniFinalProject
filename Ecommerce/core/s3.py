import os

import boto3


class S3Service:
    def __init__(self):
        access_key = os.getenv('AWS_ACCESS_KEY')
        secret_key = os.getenv('AWS_SECRET_KEY')
        self.region_name = os.getenv('AWS_REGION')

        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.client = boto3.client(
            's3',
            region_name=self.region_name,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )

    def upload(self, path, key):
        self.client.upload_file(path, self.bucket_name, key)
        return f'https://{self.bucket_name}.s3.{self.region_name}.amazonaws.com/{key}'

    def delete(self, key):
        self.client.delete_object(
            Bucket=self.bucket_name,
            Key=key
        )


s3 = S3Service()
