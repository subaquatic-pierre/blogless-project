from manager import PostManager
from proxy import BucketProxy


bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)


def get(id):
    post = post_manager.get_by_id(id)
    return post.to_json()
