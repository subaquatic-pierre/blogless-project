from time import time
from meta import PostMeta
from post import Post
from proxy import BucketProxy


class PostManager:
    def __init__(self, template_name: str, bucket_proxy: BucketProxy) -> None:
        self.bucket_proxy = bucket_proxy
        self.template_name = template_name
        self._init_bucket()

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
        self._verify_meta(meta, "No blog with that ID found")
        post_dir_bucket_key = f"{self.bucket_proxy.root_dir}{id}/"
        post_bucket_proxy = BucketProxy(
            self.bucket_proxy.bucket_name, post_dir_bucket_key
        )

        post_meta = PostMeta.from_json(
            {
                "id": id,
                "title": meta[0]["title"],
                "timestamp": meta[0]["timestamp"],
                "template_name": self.template_name,
            }
        )

        # content = post_bucket_proxy.get_json("content.json")
        post = self.create_post(post_meta, post_bucket_proxy)
        return post

    def title_to_id(self, title: str) -> int:
        meta = [blog_meta for blog_meta in self.index if blog_meta["title"] == title]
        self._verify_meta(meta, "No blog with that title found")
        return meta[0]["id"]

    def create_meta(self, title: str) -> PostMeta:
        template_name = self.template_name
        timestamp = int(time())
        new_id = self._get_latest_id()

        post_meta = PostMeta.from_json(
            {
                "id": new_id,
                "title": title,
                "timestamp": timestamp,
                "template_name": template_name,
            }
        )

        return post_meta

    def create_post(self, post_meta: PostMeta, content) -> Post:
        # New post args
        bucket_name = self.bucket_proxy.bucket_name
        post_root_dir = f"{self.bucket_proxy.root_dir}{post_meta.id}/"
        post_bucket_proxy = BucketProxy(bucket_name, post_root_dir)

        post = Post(post_meta, post_bucket_proxy, content)

        return post

    def save_post(self, post: Post):
        # Update index and save post
        try:
            index = [meta for meta in self.index]

            meta_index = None
            for i in range(len(index)):
                if index[i]["id"] == post.id:
                    meta_index = i

            if meta_index != None:
                index[i] = post.meta_data.to_json()

            else:
                index.append(post.meta_data.to_json())

            post.save()
            self._update_index(index)

            return post

        except Exception:
            raise Exception("Post could not be saved")

    def delete_post(self, id: int):
        try:
            post = self.get_by_id(id)
            post_files = post.list_files()

            # Add root dir to filenames
            post_files.append(post.bucket_proxy.root_dir)
            self.bucket_proxy.delete_files(post_files)

            # Update index
            index = self.index
            new_index = [meta for meta in index if meta["id"] != id]
            self._update_index(new_index)

        except Exception as e:
            raise Exception(e)

    def _get_latest_id(self):
        return len(self.index)

    def _update_index(self, new_index: list):
        self.bucket_proxy.save_json(new_index, "index.json")

    def _init_bucket(self):
        try:
            self.bucket_proxy.get_json("index.json")

        except Exception:
            self.bucket_proxy.save_json([], "index.json")

    def _verify_meta(self, meta, error_message):
        if len(meta) > 1:
            raise Exception("More than one blog with that title found")
        elif len(meta) == 0:
            raise Exception(error_message)
