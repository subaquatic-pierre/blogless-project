from abc import ABC
from post import Post
from bucket_proxy import BucketProxy


class PostManager:
    def __init__(self, template_name: str, bucket_proxy: BucketProxy) -> None:
        self.bucket_proxy = bucket_proxy
        self.template_name = template_name

    @property
    def index(self):
        obj_json = self.bucket_proxy.get_json_data("index.json")
        return obj_json

    def get_by_id(self, id) -> Post:
        pass

    def title_to_id(self, title: str) -> int:
        titles = [title for blog_meta in self.index]
