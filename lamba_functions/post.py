from abc import ABC
from bucket_proxy import BucketProxy
from post_meta import PostMetaData


class Post:
    def __init__(self, meta_data: PostMetaData, bucket_proxy: BucketProxy) -> None:
        self.id = meta_data.id
        self.title = meta_data.title
        self.bucket_proxy = bucket_proxy
        self.meta_data = meta_data
