from time import time
from meta import PostMeta
from post import Post
from proxy import BucketProxy, MockBucketProxy, BucketProxyBase
from exception import BucketProxyException, PostManagerException
from utils import BUCKET_NAME


class PostManager:
    def __init__(self, bucket_proxy: BucketProxyBase, template_name: str) -> None:
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
        id = int(id)

        meta = [meta_data for meta_data in self.index if meta_data["id"] == id]
        self._verify_meta(meta, "No blog with that ID found")
        post_meta = PostMeta.from_json(
            {
                "id": id,
                "title": meta[0]["title"],
                "timestamp": meta[0]["timestamp"],
                "template_name": self.template_name,
            }
        )

        content = self._get_post_content(post_meta.id)
        post = self.create_post(post_meta, content)

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
        post_root_dir = f"{self.bucket_proxy.root_dir}{post_meta.id}/"

        post_bucket_proxy = self._create_post_bucket_proxy(post_root_dir)

        post = Post(post_bucket_proxy, post_meta, content)

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

        except Exception as e:
            raise Exception(f"Post could not be saved, {str(e)}")

    def delete_post(self, id: int):
        post = self.get_by_id(id)
        post_files = post.list_files()

        # Add root dir to filenames
        post_files.append(post.bucket_proxy.root_dir)
        self.bucket_proxy.delete_files(post_files)

        # Update index
        index = self.index
        new_index = [meta for meta in index if meta["id"] != id]
        self._update_index(new_index)

    def get_meta(self, post_id):
        for meta_index, item in enumerate(self.index):
            if item["id"] == int(post_id):
                break
            else:
                meta_index = -1

        if meta_index == -1:
            raise PostManagerException("Meta data not found")

        return PostMeta.from_json(self.index[meta_index])

    # Private methods
    def _get_post_content(self, post_id):
        return self.bucket_proxy.get_json(f"{post_id}/content.json")

    def _create_post_bucket_proxy(self, post_root_dir, mock_config={}):
        if self.bucket_proxy.__class__.__name__ == "MockBucketProxy":
            return MockBucketProxy(
                self.bucket_proxy.bucket_name, post_root_dir, mock_config=mock_config
            )
        else:
            return BucketProxy(self.bucket_proxy.bucket_name, post_root_dir)

    def _get_latest_id(self):
        return len(self.index)

    def _update_index(self, new_index: list):
        self.bucket_proxy.save_json(new_index, "index.json")

    def _init_bucket(self):
        try:
            self.bucket_proxy.get_json("index.json")

        except BucketProxyException:
            self.bucket_proxy.save_json([], "index.json")

    def _verify_meta(self, meta, error_message):
        if len(meta) > 1:
            raise PostManagerException("More than one blog with that title found")
        elif len(meta) == 0:
            raise PostManagerException(error_message)

    # Static methods
    def setup_post_manager(event):
        path = event.get("path")
        testing = event.get("test_api", False)
        mock_config = event.get("mock_config", {})
        template_str = path.split("/")[1]
        template_name = template_str.capitalize()

        if testing:
            bucket_proxy = MockBucketProxy(
                bucket_name=BUCKET_NAME,
                root_dir=f"{template_str}/",
                mock_config=mock_config,
            )
        else:
            bucket_proxy = BucketProxy(
                bucket_name=BUCKET_NAME,
                root_dir=f"{template_str}/",
            )

        post_manager = PostManager(bucket_proxy, template_name)

        return post_manager
