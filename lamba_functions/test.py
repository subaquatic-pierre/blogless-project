from post_manager import PostManager
from bucket_proxy import BucketProxy

bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)

all_posts = post_manager.list_all()
print(all_posts)
