from turtle import title
import boto3
import json

import boto3

s3 = boto3.resource("s3")


class PostMetaData:
    def __init__(self, post_id, title, dir_key, time_stamp) -> None:
        self.id = post_id
        self.title = title
        self.dir_key = dir_key
        self.time_stamp = time_stamp


class Post:
    def __init__(self, meta_data, bucket_proxy) -> None:
        self.id = meta_data.id
        self.title = meta_data.title
        self.bucket_proxy = bucket_proxy
        self.meta_data = meta_data


class BucketProxy:
    def __init__(self, bucket_name, root_dir) -> None:
        self.bucket_name = bucket_name
        self.root_dir = root_dir

    def get_json_data(self, object_key):
        index_object = s3.Object(self.bucket_name, f"{self.root_dir}{object_key}")
        object_res = index_object.get()
        object_json = json.loads(object_res["Body"].read())
        return object_json


class PostManager:
    def __init__(self, bucket_name: str, root_dir: str, template_name: str) -> None:
        self.bucket_proxy = BucketProxy(bucket_name, root_dir)
        self.bucket_name = bucket_name
        self.root_dir = root_dir
        self.template_name = template_name

    @property
    def index(self):
        obj_json = self.bucket_proxy.get_json_data("index.json")
        return obj_json

    def get_post_by_id(self, id):
        pass
