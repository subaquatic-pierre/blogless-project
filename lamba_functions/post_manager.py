from time import time
from post_meta import PostMetaData
from post import Post
from bucket_proxy import BucketProxy


class PostManager:
    def __init__(self, template_name: str, bucket_proxy: BucketProxy) -> None:
        self.bucket_proxy = bucket_proxy
        self.template_name = template_name

    @property
    def index(self):
        obj_json = self.bucket_proxy.get_json("index.json")
        return obj_json

    def list_all_files(self):
        return self.bucket_proxy.list_dir()

    def get_json(self, filename):
        return self.bucket_proxy.get_json(filename)

    def get_by_id(self, id) -> Post:
        meta = [meta_data for meta_data in self.index if meta_data["id"] == id]
        self._verify_meta(meta)
        post_dir_bucket_key = f"{self.bucket_proxy.root_dir}{id}/"
        post_bucket_proxy = BucketProxy(
            self.bucket_proxy.bucket_name, post_dir_bucket_key
        )
        post_meta = PostMetaData(id, meta[0]["title"], meta[0]["time_stamp"])
        post = Post(post_meta, post_bucket_proxy)
        return post

    def title_to_id(self, title: str) -> int:
        meta = [blog_meta for blog_meta in self.index if blog_meta["title"] == title]
        self._verify_meta(meta)
        return meta[0]["id"]

    def list_all(self) -> dict:
        all_posts = self.bucket_proxy.get_json("index.json")
        return all_posts

    def create_post(self, title, content, image=None):
        new_id = self._get_latest_id()
        timestamp = int(time())

        bucket_proxy = BucketProxy(
            self.bucket_proxy.bucket_name, f"{self.bucket_proxy.root_dir}{new_id}/"
        )
        meta = PostMetaData(new_id, title, timestamp)
        post = Post(meta, bucket_proxy, content, image)
        post.save()

        return post

    def _get_latest_id(self):
        return len(self.index)

    def _verify_meta(self, meta):
        if len(meta) > 1:
            raise Exception("More than one blog with that title found")
        elif len(meta) == 0:
            raise Exception("No blog with that title found")
