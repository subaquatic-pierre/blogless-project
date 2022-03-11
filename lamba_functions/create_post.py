from time import time
from post_manager import PostManager
from post_meta import PostMetaData
from bucket_proxy import BucketProxy
from post import Post


def create_post(title, content, image, post_manager: PostManager):
    new_id = post_manager.get_latest_id()
    timestamp = int(time())

    bucket_proxy = BucketProxy(
        post_manager.bucket_proxy.bucket_name,
        f"{post_manager.bucket_proxy.root_dir}{new_id}/",
    )
    meta = PostMetaData(new_id, title, timestamp, post_manager.template_name)

    post = Post(meta, bucket_proxy, content, image)
    post_manager.save_post(post)

    return post
