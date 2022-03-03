from abc import ABC, abstractmethod
import json
import boto3

s3 = boto3.resource("s3")


class BaseBucketProxy(ABC):
    def __init__(self, bucket_name, root_dir) -> None:
        self.bucket_name = bucket_name
        self.root_dir = root_dir

    @abstractmethod
    def get_json_data(self, filename):
        pass


class BucketProxy(BaseBucketProxy):
    def get_json_data(self, object_key):
        object = s3.Object(self.bucket_name, f"{self.root_dir}{object_key}")
        object_res = object.get()
        object_json = json.loads(object_res["Body"].read())
        return object_json
