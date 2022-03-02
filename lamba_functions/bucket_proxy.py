from abc import ABC
import boto3
import json

s3 = boto3.resource("s3")


class BucketProxy:
    def __init__(self, bucket_name, root_dir) -> None:
        self.bucket_name = bucket_name
        self.root_dir = root_dir

    def get_json_data(self, object_key):
        index_object = s3.Object(self.bucket_name, f"{self.root_dir}{object_key}")
        object_res = index_object.get()
        object_json = json.loads(object_res["Body"].read())
        return object_json
