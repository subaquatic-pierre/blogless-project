from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy


bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)


def delete_post(post_id):
    post_manager.delete_post(post_id)
