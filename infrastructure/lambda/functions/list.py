from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy
from postmanager.response import Response


def list_all(event, context):
    bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
    post_manager = PostManager("Blog", bucket_proxy)

    response = Response(post_manager.index)

    return response.to_json()
