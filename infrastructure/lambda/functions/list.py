from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy


def list_all(event, context):
    bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
    post_manager = PostManager("Blog", bucket_proxy)
    return post_manager.index
