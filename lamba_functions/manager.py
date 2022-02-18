import boto3

import boto3

s3 = boto3.resource('s3')


class PostManager:
    def __init__(self, bucket_name: str, dir_key: str, template_name: str) -> None:
        self.bucket_project = bucket = s3.Bucket(bucket_name)
        self.bucket_name = bucket_name
        self.dir_key = dir_key
        self.template_name = template_name

    @property
    def index(self):
        s3.