from post_manager import PostManager
from bucket_proxy import BucketProxy
import json

bucket_proxy = BucketProxy("serverless-blog-contents", "blog/")
post_manager = PostManager("Blog", bucket_proxy)

all_posts = post_manager.list_all()
print(all_posts)

title = post_manager.title_to_id("Recursing Hypatia")
print(title)

post = post_manager.get_by_id(0)
print(post.content)

# Create test post
file = open("blog_template/content.json")
content = json.loads(file.read())
file.close()
