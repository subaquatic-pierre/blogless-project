from manager import PostManager
from proxy import BucketProxy


bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)


def update(id: int, **kwargs):
    post = post_manager.get_by_id(id)
    for kwarg in kwargs:
        post.__setattr__(kwarg, kwargs.get(kwarg))
        post_manager.save_post(post)
