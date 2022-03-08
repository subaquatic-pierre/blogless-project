from abc import ABC
from bucket_proxy import BucketProxy
from post_meta import PostMetaData


class Post:
    def __init__(self, meta_data: PostMetaData, bucket_proxy: BucketProxy) -> None:
        self.id = meta_data.id
        self.bucket_proxy = bucket_proxy
        self.meta_data = meta_data

    @property
    def title(self):
        return self.meta_data.title

    @property
    def content(self):
        content = self.bucket_proxy.get_json("content.json")

    def __str__(self):
        return f"ID: {self.id}, Title: {self.meta_data.title}"
