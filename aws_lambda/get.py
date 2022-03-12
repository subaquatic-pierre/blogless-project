from postmanager.manager import PostManager
from postmanager.proxy import BucketProxy


bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)


def get_by_id(id):
    post = post_manager.get_by_id(id)
    return post


def get_id_from_title(title):
    return post_manager.title_to_id(title)
