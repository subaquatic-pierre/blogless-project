from unittest.mock import MagicMock

from manager import PostManager
from post import Post
from meta import PostMeta
from proxy import BucketProxy


BUCKET_NAME = "serverless-blog-contents"
BUCKET_ROOT_DIR = "blog/"


def create_dummy_bucket_proxy():
    bucket_proxy = BucketProxy(BUCKET_NAME, BUCKET_ROOT_DIR)

    bucket_proxy.get_json = MagicMock()
    bucket_proxy.save_json = MagicMock()
    bucket_proxy.delete_files = MagicMock()
    bucket_proxy.list_dir = MagicMock()
    return bucket_proxy


def create_dummy_post():
    # Create post
    post_id = 0
    post_title = "Sometitle"
    timestamp = 000
    post_template = "Blog"
    content = "My amazing content"
    post_bucket_proxy = BucketProxy(
        BUCKET_NAME, f"{BUCKET_NAME,BUCKET_ROOT_DIR}{post_id}"
    )

    post_bucket_proxy = MagicMock()

    post_meta = PostMeta.from_json(
        {
            "id": id,
            "title": post_title,
            "timestamp": timestamp,
            "template_name": post_template,
        }
    )
    post = Post(post_meta, post_bucket_proxy, content)

    post.save = MagicMock()

    return post
